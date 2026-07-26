#!/usr/bin/env python3
"""Check that every pack config override is durable, not just present.

Why this exists
---------------
The pack overrides mod configs to encode deliberate design decisions - the one that
prompted this script is `tadpoleGrowthTicks = 3600` in `productivefrogs-common.toml`,
which cuts the first-frogs wait from ~23 minutes to ~6 (issue #63).

Shipping those in `pack/config/` alone is fragile. `config/` is live per-instance
state, written once when the pack is installed. If NeoForge ever has to recreate the
file - it backs a config up to `<name>-N.toml.bak` and writes a fresh one when the
existing file cannot be parsed or restored - the pack's values are gone and the mod's
own defaults take over. Nothing re-applies them, and nothing reports it. The player
just silently gets different gameplay.

`defaultconfigs/` is the directory NeoForge provides for exactly this. Verified
against the loader the pack pins (fancymodloader 4.0.43, NeoForge 21.1.244):
`ConfigTracker` checks whether the config file exists and, when it does not, copies
`defaultconfigs/<name>.toml` into place (`defaultConfigPath` + `Files.copy`), only
falling back to `createDefaultConfig` from the mod's spec if no default is supplied.
So a config seeded from `defaultconfigs/` survives recreation; one that lives only in
`config/` does not.

This script enforces that every FML-managed config the pack overrides exists in BOTH
places with identical bytes - `config/` so existing behaviour is unchanged, and
`defaultconfigs/` so the value survives.

What is deliberately excluded
-----------------------------
- `botanypots.json` and anything else non-TOML: not FML-managed, so NeoForge never
  consults `defaultconfigs/` for it. A copy there would be dead weight.
- Files in `config/` subdirectories (ftbquests, bbl, almostunified, ...): those are
  mod-owned data trees, not FML mod configs, and are keyed by path rather than by the
  flat `<name>.toml` lookup `defaultconfigs/` uses.

Note `bcc-common.toml` carries the modpack version, which `release.yml` stamps from
the tag at export time. It stamps BOTH copies; this script's byte-identity check is
what keeps them from drifting apart.

Usage
-----
    python tools/check_pack_configs.py          # exits 1 on a problem
    python tools/check_pack_configs.py --fix    # copy config/ -> defaultconfigs/
"""
from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG = REPO / "pack" / "config"
DEFAULTS = REPO / "pack" / "defaultconfigs"

# Non-TOML config files in config/ that NeoForge does not manage, so defaultconfigs/
# is not consulted for them. Listed explicitly so a new one has to be triaged.
NOT_FML = {"botanypots.json"}


def tracked_configs() -> list[Path]:
    """Top-level FML-managed config files the pack overrides."""
    return sorted(p for p in CONFIG.glob("*")
                  if p.is_file() and p.suffix == ".toml" and p.name not in NOT_FML)


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Verify pack config overrides survive config recreation.")
    ap.add_argument("--fix", action="store_true",
                    help="copy config/ files into defaultconfigs/ to resolve findings")
    args = ap.parse_args()

    if not CONFIG.is_dir():
        sys.exit(f"missing {CONFIG}")
    DEFAULTS.mkdir(exist_ok=True)

    problems: list[str] = []
    checked = 0

    for src in tracked_configs():
        checked += 1
        dst = DEFAULTS / src.name
        if not dst.is_file():
            if args.fix:
                shutil.copy2(src, dst)
                print(f"  fixed  {src.name}: copied into defaultconfigs/")
            else:
                problems.append(
                    f"{src.name}: in config/ but NOT in defaultconfigs/ - the override "
                    f"is lost if NeoForge ever recreates the file")
        elif not filecmp.cmp(src, dst, shallow=False):
            if args.fix:
                shutil.copy2(src, dst)
                print(f"  fixed  {src.name}: defaultconfigs/ copy resynced")
            else:
                problems.append(
                    f"{src.name}: config/ and defaultconfigs/ copies DIFFER - a fresh "
                    f"install and a recreated config would behave differently")

    # A stale default with no counterpart is its own trap: it would seed a config for
    # a mod the pack no longer ships, or under a name nothing reads.
    for orphan in sorted(DEFAULTS.glob("*")):
        if orphan.is_file() and not (CONFIG / orphan.name).is_file():
            problems.append(
                f"{orphan.name}: in defaultconfigs/ with no config/ counterpart - "
                f"stale, remove it")

    skipped = sorted(n for n in NOT_FML if (CONFIG / n).is_file())
    print(f"checked {checked} FML-managed config override(s) in pack/config/")
    if skipped:
        print(f"skipped (not FML-managed): {', '.join(skipped)}")

    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        if not args.fix:
            print("\nRe-run with --fix to sync defaultconfigs/ from config/.")
        sys.exit(1)

    print("OK: every override is present in both config/ and defaultconfigs/.")


if __name__ == "__main__":
    main()
