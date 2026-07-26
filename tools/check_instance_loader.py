#!/usr/bin/env python3
"""Check the dev instance's NeoForge loader against the pack's pin.

Why this exists
---------------
`sync_instance.py` mirrors *jars*. Nothing syncs the **loader**, so bumping
`[versions] neoforge` in `pack/pack.toml` leaves the instance behind, and every mod
requiring the newer build dies at load with:

    Mod apotheosis requires neoforge 21.1.235 or above
    Currently, neoforge is 21.1.230

That is not a pack bug and cannot be debugged as one - the pack is correct and the
instance is stale. It bit on the 21.1.233 -> 21.1.244 bump (v1.5.3), where the
instance was found on 21.1.230, two bumps behind, so local playtests had never once
run the loader the pack actually shipped.

Why this only *checks*
----------------------
The loader cannot be changed from outside the CurseForge app. It is stored twice:

    Instances/<folder>/minecraftinstance.json          `baseModLoader`
    %LOCALAPPDATA%/Overwolf/Curse/GameInstances/MinecraftGameInstance.json

The second is CurseForge's own app-level store, and it wins: CurseForge rewrites the
per-instance file from it when the instance launches. Editing the instance JSON alone
looks like it worked - it reads back correctly - and is silently reverted on the next
launch. So this script deliberately does not write. Change the loader in the
CurseForge app (instance -> settings -> modloader version); CurseForge then updates
both stores and downloads the build itself.

Note the display name can differ from the folder name - this repo's dev instance
lives in `Instances/Sky Frogs` but shows in CurseForge as **Sky Frogs (DEV)**, and
there is a second, non-junctioned `Sky Frogs` instance in `Instances/Sky Frogs (1)`.
Changing the wrong one is easy, so this reports both names.

Usage
-----
    python tools/check_instance_loader.py            # exits 1 on drift
    python tools/check_instance_loader.py --instance "C:\\...\\Other"
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PACK_TOML = REPO / "pack" / "pack.toml"

CF_ROOT = Path(r"C:\Users\User\curseforge\minecraft")
DEFAULT_INSTANCE = CF_ROOT / "Instances" / "Sky Frogs"
CF_STORE = (Path(os.environ.get("LOCALAPPDATA", r"C:\Users\User\AppData\Local"))
            / "Overwolf" / "Curse" / "GameInstances" / "MinecraftGameInstance.json")

JUNCTIONS = ("config/ftbquests/quests", "kubejs/data", "kubejs/server_scripts")


def pinned_version() -> str:
    if not PACK_TOML.is_file():
        sys.exit(f"pack.toml not found: {PACK_TOML}")
    m = re.search(r'^\s*neoforge\s*=\s*"([^"]+)"',
                  PACK_TOML.read_text(encoding="utf-8"), re.M)
    if not m:
        sys.exit("no [versions] neoforge entry in pack.toml")
    return m.group(1)


def app_store_loader(display_name: str) -> str | None:
    """What CurseForge's own store thinks this instance's loader is (the one that wins)."""
    if not CF_STORE.is_file():
        return None
    try:
        entries = json.loads(CF_STORE.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001 - a schema/format change must not break the check
        return None
    if not isinstance(entries, list):
        return None
    for e in entries:
        if isinstance(e, dict) and e.get("name") == display_name:
            return (e.get("baseModLoader") or {}).get("forgeVersion")
    return None


def junction_count(instance: Path) -> int:
    n = 0
    for rel in JUNCTIONS:
        p = instance.joinpath(*rel.split("/"))
        if p.is_dir() and str(Path(os.path.realpath(p))).lower().startswith(
                str(REPO).lower()):
            n += 1
    return n


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Check the dev instance's NeoForge loader against pack.toml.")
    ap.add_argument("--instance", type=Path, default=DEFAULT_INSTANCE)
    args = ap.parse_args()

    inst_file = args.instance / "minecraftinstance.json"
    if not inst_file.is_file():
        sys.exit(f"instance config not found: {inst_file}")

    inst = json.loads(inst_file.read_text(encoding="utf-8"))
    display = inst.get("name") or args.instance.name
    on_disk = inst["baseModLoader"]["forgeVersion"]
    pin = pinned_version()
    in_app = app_store_loader(display)

    print(f"pack pins        : {pin}")
    print(f"instance folder  : {args.instance.name}")
    print(f"CurseForge name  : {display}")
    print(f"loader (instance): {on_disk}")
    print(f"loader (CF store): {in_app or '(not found)'}")
    print(f"repo junctions   : {junction_count(args.instance)}/{len(JUNCTIONS)}")

    # The app-level store is authoritative - CurseForge rewrites the instance file
    # from it on launch - so believe it whenever we could read it.
    effective = in_app or on_disk
    if effective == pin:
        print("\nOK: the instance will launch on the pinned loader.")
        return

    print(f"\nDRIFT: the instance will launch on {effective}, not the pinned {pin}.")
    if in_app and in_app != on_disk:
        print(f"       (the instance file says {on_disk}, but CurseForge's store "
              f"says {in_app} and overwrites it on launch)")
    print(f"\nFix it in the CurseForge app - it cannot be done by editing files:")
    print(f"  instance \"{display}\" -> settings -> modloader version -> {pin}")
    print("Then re-run this check. Until it passes, any launch test is meaningless:")
    print("it either fails for a reason unrelated to the pack, or passes on a loader")
    print("you are not shipping.")
    sys.exit(1)


if __name__ == "__main__":
    main()
