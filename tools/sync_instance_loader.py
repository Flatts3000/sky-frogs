#!/usr/bin/env python3
"""Check, and optionally set, the dev instance's NeoForge loader against the pack pin.

Why this exists
---------------
`sync_instance.py` mirrors *jars*. Nothing syncs the **loader**, so bumping
`[versions] neoforge` in `pack/pack.toml` leaves the instance behind and every mod
requiring the newer build dies at load:

    Mod apotheosis requires neoforge 21.1.235 or above
    Currently, neoforge is 21.1.230

That is not a pack bug and cannot be debugged as one. It bit on the
21.1.233 -> 21.1.244 bump (v1.5.3), where the instance was found on 21.1.230 - two
bumps behind - so local playtests had never once run the loader the pack shipped.

The three things that make this work
------------------------------------
Learned the hard way; each one silently defeats the change on its own.

1. **The loader is stored twice, and the app-level store wins.**

       Instances/<folder>/minecraftinstance.json                  -> baseModLoader
       %LOCALAPPDATA%/Overwolf/Curse/GameInstances/MinecraftGameInstance.json

   CurseForge rewrites the per-instance file from the app-level store on launch.
   Patching only the instance file reads back correctly and is then silently
   reverted - a convincing false success. Both are written here.

2. **CurseForge must be fully closed** (including the Overwolf tray icon). While it
   runs it holds every instance in memory and writes them out on launch, clobbering
   any external edit. This refuses to run if it finds the processes.

3. **Do not hand-install the loader.** CurseForge installs it itself from its own
   catalog on the next launch. Pre-placing files under `Install/versions/` and
   `Install/libraries/` from the NeoForge installer makes CurseForge's install task
   fail outright with `InstallTaskFailedException` ("Failed to launch modpack"),
   because it finds a partial install it did not create. This script never touches
   the install directory; if a foreign install is present it says so and stops.

The `baseModLoader` block is taken from CurseForge's own API record for the build
(`/v1/minecraft/modloader/neoforge-<version>`), which is exactly what CurseForge
would write itself, rather than being reconstructed by hand.

Watch which instance
--------------------
The CurseForge display name is not the folder name: this repo's dev instance lives in
`Instances\\Sky Frogs` but shows as **"Sky Frogs (DEV)"**, while `Instances\\Sky Frogs (1)`
shows as plain **"Sky Frogs"** and is not junctioned. Both are printed.

Usage
-----
    python tools/sync_instance_loader.py            # check only; exits 1 on drift
    python tools/sync_instance_loader.py --apply    # write both stores (CF closed)
    python tools/sync_instance_loader.py --apply --version 21.1.240
"""
from __future__ import annotations

import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PACK_TOML = REPO / "pack" / "pack.toml"

CF_ROOT = Path(r"C:\Users\User\curseforge\minecraft")
CF_INSTALL = CF_ROOT / "Install"
DEFAULT_INSTANCE = CF_ROOT / "Instances" / "Sky Frogs"
STORE = (Path(os.environ.get("LOCALAPPDATA", r"C:\Users\User\AppData\Local"))
         / "Overwolf" / "Curse" / "GameInstances" / "MinecraftGameInstance.json")
API = "https://api.curseforge.com/v1/minecraft/modloader/neoforge-{}"

JUNCTIONS = ("config/ftbquests/quests", "kubejs/data", "kubejs/server_scripts")


def pinned_version() -> str:
    if not PACK_TOML.is_file():
        sys.exit(f"pack.toml not found: {PACK_TOML}")
    m = re.search(r'^\s*neoforge\s*=\s*"([^"]+)"',
                  PACK_TOML.read_text(encoding="utf-8"), re.M)
    if not m:
        sys.exit("no [versions] neoforge entry in pack.toml")
    return m.group(1)


def curseforge_running() -> int:
    ps = ("@(Get-Process | Where-Object { $_.ProcessName -match "
          "'CurseForge|Overwolf' }).Count")
    try:
        out = subprocess.run(["powershell", "-NoProfile", "-Command", ps],
                             capture_output=True, text=True, timeout=60)
        return int((out.stdout or "0").strip() or 0)
    except Exception:  # noqa: BLE001 - never block the check on a shell hiccup
        return 0


def store_entry(entries: list, display: str) -> dict | None:
    for e in entries:
        if isinstance(e, dict) and e.get("name") == display:
            return e
    return None


def junction_count(instance: Path) -> int:
    n = 0
    for rel in JUNCTIONS:
        p = instance.joinpath(*rel.split("/"))
        if p.is_dir() and str(Path(os.path.realpath(p))).lower().startswith(
                str(REPO).lower()):
            n += 1
    return n


def save(path: Path, data) -> None:
    backup = path.with_suffix(path.suffix + ".bak-loader")
    shutil.copy2(path, backup)
    # CurseForge writes these UTF-8 without a BOM; keep it that way.
    io.open(path, "w", encoding="utf-8", newline="").write(
        json.dumps(data, indent=2, ensure_ascii=False))
    print(f"  wrote {path.name}  (backup: {backup.name})")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Check (or set) the dev instance's NeoForge loader.")
    ap.add_argument("--apply", action="store_true",
                    help="write the change; requires CurseForge to be closed")
    ap.add_argument("--version", help="loader version (default: pack.toml's pin)")
    ap.add_argument("--instance", type=Path, default=DEFAULT_INSTANCE)
    args = ap.parse_args()

    inst_file = args.instance / "minecraftinstance.json"
    if not inst_file.is_file():
        sys.exit(f"instance config not found: {inst_file}")

    pin = args.version or pinned_version()
    inst = json.loads(inst_file.read_text(encoding="utf-8"))
    display = inst.get("name") or args.instance.name
    on_disk = inst["baseModLoader"]["forgeVersion"]

    entries = json.loads(STORE.read_text(encoding="utf-8")) if STORE.is_file() else []
    entry = store_entry(entries, display)
    in_app = (entry or {}).get("baseModLoader", {}).get("forgeVersion")

    print(f"target version   : {pin}")
    print(f"instance folder  : {args.instance.name}")
    print(f"CurseForge name  : {display}")
    print(f"loader (instance): {on_disk}")
    print(f"loader (CF store): {in_app or '(not found)'}   <- authoritative")
    print(f"repo junctions   : {junction_count(args.instance)}/{len(JUNCTIONS)}")

    effective = in_app or on_disk
    if effective == pin and on_disk == pin:
        print("\nOK: the instance will launch on the target loader.")
        return

    print(f"\nDRIFT: the instance will launch on {effective}, not {pin}.")
    if not args.apply:
        print("Re-run with --apply (CurseForge fully closed) to fix it.")
        sys.exit(1)

    n = curseforge_running()
    if n:
        sys.exit(f"\nCurseForge/Overwolf is running ({n} processes). Quit it fully, "
                 f"including the Overwolf tray icon, or the change will be reverted "
                 f"on the next launch.")
    if entry is None:
        sys.exit(f"\nno '{display}' entry in {STORE.name}; refusing to write a "
                 f"half-change that CurseForge would revert")

    # A foreign hand-install makes CurseForge's own install task fail; let it install.
    stray = CF_INSTALL / "versions" / f"neoforge-{pin}"
    if stray.is_dir() and not (stray / f"neoforge-{pin}.json").is_file():
        sys.exit(f"\n{stray} looks partially installed. Delete it (and "
                 f"Install/libraries/net/neoforged/neoforge/{pin}) and re-run - "
                 f"CurseForge must install the loader itself.")

    print(f"\nCurseForge is closed - fetching its own record for neoforge-{pin} ...")
    try:
        with urllib.request.urlopen(API.format(pin), timeout=60) as r:
            rec = json.load(r)["data"]
    except Exception as exc:  # noqa: BLE001
        sys.exit(f"could not fetch CurseForge's modloader record: {exc}")
    print(f"  latest={rec.get('latest')} recommended={rec.get('recommended')}")

    def rebuild(old: dict) -> dict:
        new = dict(old)
        for k in old:
            if k in rec:
                new[k] = rec[k]
        # CurseForge stores this path with its local separator convention.
        new["librariesInstallLocation"] = old["librariesInstallLocation"].replace(
            old["forgeVersion"], pin)
        if sorted(new) != sorted(old):
            sys.exit("baseModLoader key set drifted; inspect by hand")
        if new["forgeVersion"] != pin or new["name"] != f"neoforge-{pin}":
            sys.exit("CurseForge's record did not match the requested version")
        return new

    entry["baseModLoader"] = rebuild(entry["baseModLoader"])
    save(STORE, entries)
    inst["baseModLoader"] = rebuild(inst["baseModLoader"])
    save(inst_file, inst)

    print(f"\nboth stores now on NeoForge {pin}.")
    print("Reopen CurseForge and launch - it installs the loader itself.")


if __name__ == "__main__":
    main()
