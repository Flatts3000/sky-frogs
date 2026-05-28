#!/usr/bin/env python3
"""Sync the local dev instance's mods to the pack pins via packwiz-installer.

Why this exists
---------------
The Sky Frogs dev instance junction-links the repo's `kubejs/server_scripts`,
`kubejs/data`, and `config/ftbquests/quests`, so those edits are live in-game. The
`mods/` folder is NOT junctioned: packwiz stores mod *metadata* (`pack/mods/*.pw.toml`),
not jars, so `packwiz update` / `packwiz cf add` never reaches the instance. Mod
changes therefore have to be pushed into the instance separately.

This drives the canonical packwiz tool, `packwiz-installer`, to do that:

    tools/pack_refresh.py           # LF-normalize, then index.toml reflects the pins
    packwiz serve                   # serve the working-tree pack over HTTP
    java -jar packwiz-installer ...  # download/verify pinned mods into the instance

packwiz-installer downloads each pinned mod straight from its source (CurseForge),
hash-verifies it, and tracks `.packwiz-installer-manifest.json` so add / update /
remove all happen cleanly - and it works on any machine, not just one that already
has the jars. Jars whose CurseForge entry disables third-party API downloads cannot
be fetched automatically; the installer reports those for manual download.

Safety
------
- Refuses to run while the instance's Minecraft is running (loaded jars are locked).
- Idempotent: a run that finds every jar already present and hash-matching downloads
  nothing.

Usage
-----
    python tools/sync_instance.py                       # sync the Sky Frogs instance
    python tools/sync_instance.py --side both           # install client+server+both
    python tools/sync_instance.py --instance "C:\\...\\Other"   # a different instance
    python tools/sync_instance.py --port 8123           # if :8080 is busy
"""
from __future__ import annotations

import argparse
import shutil
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PACK = REPO / "pack"
TOOLS = REPO / "tools"
BOOTSTRAP = TOOLS / "packwiz-installer-bootstrap.jar"
# packwiz's own docs point instance setups at this always-current asset; the
# bootstrap is forward-compatible and self-updates the real installer jar.
BOOTSTRAP_URL = ("https://github.com/packwiz/packwiz-installer-bootstrap/"
                 "releases/latest/download/packwiz-installer-bootstrap.jar")

CF_ROOT = Path(r"C:\Users\User\curseforge\minecraft")
DEFAULT_INSTANCE = CF_ROOT / "Instances" / "Sky Frogs"
UA = "Mozilla/5.0 (sky-frogs sync_instance.py)"


def minecraft_running(instance: Path) -> bool:
    """Best-effort: is a java process running this instance? (Windows/PowerShell)."""
    needle = instance.name.replace("'", "''")
    ps = (
        "Get-CimInstance Win32_Process -Filter \"Name='java.exe' OR Name='javaw.exe'\" "
        f"| Where-Object {{ $_.CommandLine -like '*{needle}*' }} "
        "| Select-Object -First 1 -ExpandProperty ProcessId"
    )
    try:
        out = subprocess.run(["powershell", "-NoProfile", "-Command", ps],
                             capture_output=True, text=True, timeout=30)
        return bool(out.stdout.strip())
    except Exception:  # noqa: BLE001 - no PowerShell / odd env: don't block on the check
        return False


def ensure_bootstrap() -> None:
    if BOOTSTRAP.is_file() and BOOTSTRAP.stat().st_size > 1024:
        return
    print(f"fetching packwiz-installer-bootstrap.jar -> {BOOTSTRAP} ...")
    req = urllib.request.Request(BOOTSTRAP_URL, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except Exception as exc:  # noqa: BLE001
        sys.exit(f"could not download packwiz-installer-bootstrap.jar: {exc}")
    if len(data) < 1024:
        sys.exit("bootstrap download looks wrong (too small); aborting")
    BOOTSTRAP.write_bytes(data)


def free_port() -> int:
    """Ask the OS for an unused TCP port so we never collide with another service."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def wait_for_serve(url: str, proc: subprocess.Popen, timeout: float = 30.0) -> str | None:
    """Return the served pack.toml body once it answers, or None if serve dies/times out."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if proc.poll() is not None:
            return None  # `packwiz serve` exited early (e.g. port in use)
        try:
            with urllib.request.urlopen(url, timeout=2) as resp:
                if resp.status == 200:
                    return resp.read().decode("utf-8", "replace")
        except Exception:  # noqa: BLE001 - connection refused until the server is up
            time.sleep(0.4)
    return None


def expected_pack_name() -> str:
    """The pack's declared name, used to confirm `packwiz serve` is serving OUR pack."""
    for line in (PACK / "pack.toml").read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("name"):
            return line.split("=", 1)[1].strip().strip('"')
    return ""


def main() -> int:
    ap = argparse.ArgumentParser(description="Sync pack-pinned mods into the dev instance "
                                             "using packwiz-installer.")
    ap.add_argument("--instance", type=Path, default=DEFAULT_INSTANCE, help="instance dir")
    ap.add_argument("--side", choices=["client", "server", "both"], default="client",
                    help="which side's mods to install (default: client = client+both)")
    ap.add_argument("--port", type=int, default=0,
                    help="port for `packwiz serve` (default: auto-pick a free one)")
    args = ap.parse_args()
    # Flush our prints at each newline so they interleave correctly with the
    # subprocess output we inherit (otherwise pipe buffering reorders them).
    sys.stdout.reconfigure(line_buffering=True)
    port = args.port or free_port()

    if not (PACK / "pack.toml").is_file():
        sys.exit(f"pack not found at {PACK} (expected pack.toml)")
    if not args.instance.is_dir():
        sys.exit(f"instance dir not found: {args.instance}")
    for tool in ("packwiz", "java"):
        if shutil.which(tool) is None:
            sys.exit(f"`{tool}` not found on PATH - install it / add it to PATH and retry.")
    if minecraft_running(args.instance):
        sys.exit("ABORT: Minecraft appears to be running this instance. Close it first "
                 "(loaded jars are locked), then retry.")

    ensure_bootstrap()

    # Use the repo's LF-normalizing refresh, not bare `packwiz refresh`: the
    # junctioned quest/lang files can be CRLF on disk after the game loads a world,
    # and bare refresh would record CRLF hashes in index.toml (the "LF/CRLF tax").
    print("normalizing line endings + packwiz refresh (tools/pack_refresh.py) ...")
    if subprocess.run([sys.executable, str(TOOLS / "pack_refresh.py")]).returncode != 0:
        sys.exit("tools/pack_refresh.py failed")

    url = f"http://127.0.0.1:{port}/pack.toml"
    expected_name = expected_pack_name()
    print(f"serving pack on 127.0.0.1:{port} ...")
    # --refresh=false: pack_refresh.py already refreshed the index. Without it,
    # `packwiz serve` re-hashes the working tree on every query - wasteful, and it
    # could re-record CRLF hashes that pack_refresh.py just normalized away.
    serve = subprocess.Popen(["packwiz", "serve", "--port", str(port), "--refresh=false"],
                             cwd=PACK, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        body = wait_for_serve(url, serve)
        if body is None:
            sys.exit(f"`packwiz serve` did not come up on :{port} "
                     "(is the port already in use? try --port).")
        # Confirm the responder is OUR pack, not another HTTP server that grabbed the
        # port between free_port() releasing it and packwiz binding it.
        if expected_name and expected_name not in body:
            sys.exit(f"server on :{port} is not pack '{expected_name}' - aborting rather "
                     "than risk syncing the instance to the wrong pack.")
        print(f"running packwiz-installer (side={args.side}) in {args.instance} ...\n")
        rc = subprocess.run(
            ["java", "-jar", str(BOOTSTRAP), "-g", "-s", args.side, url],
            cwd=args.instance,
        ).returncode
    finally:
        serve.terminate()
        try:
            serve.wait(timeout=10)
        except subprocess.TimeoutExpired:
            serve.kill()

    if rc == 0:
        print("\nSync complete - the instance's mods now match the pack pins. "
              "Relaunch the instance to load them.")
    else:
        print(f"\npackwiz-installer exited {rc}. Any mod it could not download "
              "automatically (e.g. CurseForge third-party downloads disabled) is named "
              "above - fetch those manually into the instance's mods/ folder.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
