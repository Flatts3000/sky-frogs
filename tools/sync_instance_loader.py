#!/usr/bin/env python3
"""Sync the local dev instance's NeoForge loader to the pack's pinned version.

Why this exists
---------------
`sync_instance.py` mirrors *jars*. It does not touch the loader, which lives in the
CurseForge app's own `minecraftinstance.json` (`baseModLoader`). So bumping
`[versions] neoforge` in `pack/pack.toml` leaves the instance behind, and a mod that
requires the newer loader fails at load with:

    Mod apotheosis requires neoforge 21.1.235 or above
    Currently, neoforge is 21.1.230

That is not a crash you can debug from the pack - the pack is fine, the instance is
stale. It bit on the 21.1.233 -> 21.1.244 bump (v1.5.3), where the instance turned out
to still be on 21.1.230, two bumps behind, so local playtests had never once run the
loader the pack actually shipped.

What it does
------------
1. Reads the target version from `pack/pack.toml` (override with `--version`).
2. Installs that NeoForge build into the CurseForge *shared* install directory if it
   is not already there, by running the official NeoForge installer's `--install-client`.
   The installer needs a `launcher_profiles.json` to inject into; CurseForge does not
   ship one, so a stub is created if absent.
3. Copies the vanilla client jar into `versions/neoforge-<v>/` - the installer does not
   place it, but CurseForge's launcher expects `versions/<id>/<id>.jar`. Every installed
   loader for the same Minecraft version carries a byte-identical copy.
4. Rewrites `baseModLoader` in `minecraftinstance.json`, preserving CurseForge's exact
   key set, after backing the file up.

Doing this through the CurseForge UI works too, and is the supported path; this exists
so the loader half of a pin bump is scriptable alongside the jar half.

Safety
------
- Refuses to run while the instance's Minecraft is running.
- Idempotent: re-running once the instance already matches the pin is a no-op.
- Asserts the rewritten `baseModLoader` keeps the same key set CurseForge wrote, so a
  future CurseForge schema change fails loudly instead of silently dropping a field.
- Backs up `minecraftinstance.json` before writing.

Usage
-----
    python tools/sync_instance_loader.py                  # match pack.toml's pin
    python tools/sync_instance_loader.py --version 21.1.244
    python tools/sync_instance_loader.py --instance "C:\\...\\Other"
    python tools/sync_instance_loader.py --dry-run
"""
from __future__ import annotations

import argparse
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PACK_TOML = REPO / "pack" / "pack.toml"

CF_ROOT = Path(r"C:\Users\User\curseforge\minecraft")
CF_INSTALL = CF_ROOT / "Install"
DEFAULT_INSTANCE = CF_ROOT / "Instances" / "Sky Frogs"

MAVEN = "https://maven.neoforged.net/releases/net/neoforged/neoforge"
UA = "Mozilla/5.0 (sky-frogs sync_instance_loader.py)"


def pinned_version() -> str:
    """Read `[versions] neoforge` out of pack.toml."""
    if not PACK_TOML.is_file():
        sys.exit(f"pack.toml not found: {PACK_TOML}")
    m = re.search(r'^\s*neoforge\s*=\s*"([^"]+)"',
                  PACK_TOML.read_text(encoding="utf-8"), re.M)
    if not m:
        sys.exit("no [versions] neoforge entry in pack.toml")
    return m.group(1)


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


def download_installer(version: str, dest: Path) -> Path:
    url = f"{MAVEN}/{version}/neoforge-{version}-installer.jar"
    print(f"downloading {url} ...")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = resp.read()
    except Exception as exc:  # noqa: BLE001
        sys.exit(f"could not download the NeoForge {version} installer: {exc}\n"
                 f"(is {version} a real 21.1.x build?)")
    if len(data) < 100_000:
        sys.exit("installer download looks wrong (too small); aborting")
    dest.write_bytes(data)
    return dest


def install_loader(version: str, installer: Path) -> None:
    """Run the official installer against CurseForge's shared install directory."""
    # The installer injects a profile and refuses to run without this file. CurseForge
    # does not create one (it does not use the vanilla launcher's profile system), so
    # a stub is enough - nothing reads it back.
    profiles = CF_INSTALL / "launcher_profiles.json"
    if not profiles.is_file():
        profiles.write_text('{"profiles":{},"settings":{},"version":3}',
                            encoding="utf-8")
        print(f"created stub {profiles.name} (the installer requires one)")

    print(f"installing NeoForge {version} into {CF_INSTALL} ...")
    proc = subprocess.run(
        ["java", "-jar", str(installer), "--install-client", str(CF_INSTALL)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if proc.returncode != 0 or "Successfully installed" not in proc.stdout:
        tail = "\n".join((proc.stdout + proc.stderr).splitlines()[-15:])
        sys.exit(f"NeoForge installer failed (exit {proc.returncode}):\n{tail}")
    print("installer reported success")


def ensure_version_jar(version: str) -> None:
    """Place versions/<id>/<id>.jar, which the installer does not create.

    It is the vanilla client jar; CurseForge keeps an identical copy under every
    installed loader for the same Minecraft version, so any sibling works as source.
    """
    versions = CF_INSTALL / "versions"
    target = versions / f"neoforge-{version}" / f"neoforge-{version}.jar"
    if target.is_file():
        return
    for sibling in sorted(versions.glob("neoforge-*/neoforge-*.jar"), reverse=True):
        shutil.copy2(sibling, target)
        print(f"copied client jar from {sibling.parent.name}")
        return
    print(f"WARNING: no sibling loader to copy a client jar from; {target.name} is "
          f"missing and CurseForge may refuse to launch. Install any NeoForge build "
          f"through the CurseForge UI once, then re-run.")


def build_loader_block(old: dict, version: str, installer: Path) -> dict:
    """Rewrite baseModLoader for `version`, preserving CurseForge's key set."""
    version_json = CF_INSTALL / "versions" / f"neoforge-{version}" / f"neoforge-{version}.json"
    if not version_json.is_file():
        sys.exit(f"missing {version_json} - loader install did not complete")

    with zipfile.ZipFile(installer) as z:
        install_profile = json.loads(z.read("install_profile.json"))

    new = dict(old)  # carry through any key we do not model
    new["forgeVersion"] = version
    new["name"] = f"neoforge-{version}"
    new["filename"] = f"neoforge-{version}.jar"
    # Stored verbatim: verified byte-identical to the on-disk version manifest.
    new["versionJson"] = json.dumps(
        json.loads(version_json.read_text(encoding="utf-8")), separators=(",", ":"))
    new["installProfileJson"] = json.dumps(install_profile, separators=(",", ":"))
    new["librariesInstallLocation"] = old["librariesInstallLocation"].replace(
        old["forgeVersion"], version)
    new["latest"] = False
    new["recommended"] = False

    if sorted(new) != sorted(old):
        sys.exit("baseModLoader key set drifted from what CurseForge wrote; "
                 "inspect minecraftinstance.json by hand rather than trusting this")
    return new


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Point the dev instance's NeoForge loader at the pack's pin.")
    ap.add_argument("--version", help="loader version (default: pack.toml's pin)")
    ap.add_argument("--instance", type=Path, default=DEFAULT_INSTANCE,
                    help="instance dir")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would change, write nothing")
    args = ap.parse_args()

    version = args.version or pinned_version()
    inst_file = args.instance / "minecraftinstance.json"
    if not inst_file.is_file():
        sys.exit(f"instance config not found: {inst_file}")

    inst = json.loads(inst_file.read_text(encoding="utf-8"))
    old = inst["baseModLoader"]
    current = old.get("forgeVersion")
    print(f"pack pins  : {version}")
    print(f"instance is: {current}")

    if current == version:
        print("already in sync, nothing to do")
        return
    if args.dry_run:
        print(f"[dry-run] would install NeoForge {version} (if absent) and "
              f"repoint the instance at it")
        return
    if minecraft_running(args.instance):
        sys.exit("Minecraft is running for this instance - close it and re-run")

    with tempfile.TemporaryDirectory() as tmp:
        installer = Path(tmp) / f"neoforge-{version}-installer.jar"
        download_installer(version, installer)
        if not (CF_INSTALL / "versions" / f"neoforge-{version}" /
                f"neoforge-{version}.json").is_file():
            install_loader(version, installer)
        else:
            print(f"NeoForge {version} already installed; reusing it")
        ensure_version_jar(version)
        inst["baseModLoader"] = build_loader_block(old, version, installer)

    backup = inst_file.with_suffix(".json.bak-loader")
    shutil.copy2(inst_file, backup)
    # CurseForge writes this file as UTF-8 without a BOM; keep it that way.
    io.open(inst_file, "w", encoding="utf-8", newline="").write(
        json.dumps(inst, indent=2, ensure_ascii=False))

    print(f"backup     : {backup.name}")
    print(f"instance now on NeoForge {version} - relaunch to pick it up")


if __name__ == "__main__":
    main()
