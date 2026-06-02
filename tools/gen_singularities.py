#!/usr/bin/env python3
"""Generate Extended Crafting singularity definitions from Productive Frogs slime_variant data.

The Tier 6 / Void endgame requires one EC singularity per *vanilla* froglight resource (modded
variants are skipped - they are not pinned in the pack). Each singularity is flagged
``inUltimateSingularity`` so EC's auto-generated Ultimate Singularity recipe demands the full set:
a literal "you automated every frog" capstone. The compressor input is the smelted resource
(``primer_item``) because EC's singularity ingredient and the Quantum Compressor's Cucumber
``IngredientWithCount`` input are both item/tag-value only and cannot match a froglight's
``slime_variant`` data component (see ``pack/config/extendedcrafting/singularities/README.md``).

Each singularity's gradient is taken straight from the frog variant's own
``primary_color`` / ``secondary_color`` so the cube matches the frog that feeds it.

The committed JSONs under ``pack/config/extendedcrafting/singularities/`` and the EC lang file are
the source of truth; re-run this only when Productive Frogs adds or removes vanilla variants.

Usage:
    python tools/gen_singularities.py [--jar PATH_TO_PRODUCTIVEFROGS_JAR]
"""
import argparse
import glob
import json
import os
import sys
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "pack", "config", "extendedcrafting", "singularities")
LANG = os.path.join(REPO, "pack", "kubejs", "assets", "extendedcrafting", "lang", "en_us.json")
VARIANT_PREFIX = "data/productivefrogs/productivefrogs/slime_variant/"


def find_jar(explicit):
    if explicit:
        return explicit
    patterns = [
        os.path.expanduser("~/curseforge/minecraft/Instances/Sky Frogs/mods/productivefrogs-*.jar"),
        "C:/Users/User/curseforge/minecraft/Instances/Sky Frogs/mods/productivefrogs-*.jar",
    ]
    for pat in patterns:
        matches = sorted(glob.glob(pat))
        if matches:
            return matches[-1]
    sys.exit("Could not locate a productivefrogs jar; pass --jar PATH explicitly.")


def title(slug):
    return " ".join(word.capitalize() for word in slug.split("_"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", help="Path to the productivefrogs jar (default: Sky Frogs instance)")
    args = parser.parse_args()
    jar = find_jar(args.jar)

    lang = {}
    written = []
    skipped = []
    with zipfile.ZipFile(jar) as archive:
        names = sorted(
            n for n in archive.namelist()
            if n.startswith(VARIANT_PREFIX) and n.endswith(".json")
        )
        for name in names:
            data = json.loads(archive.read(name))
            variant = name[len(VARIANT_PREFIX):-len(".json")]
            primer = data.get("primer_item", "")
            if "neoforge:conditions" in data or not primer.startswith("minecraft:"):
                skipped.append(variant)
                continue
            key = "singularity.extendedcrafting.%s" % variant
            obj = {
                "name": key,
                "colors": [
                    format(data["primary_color"] & 0xFFFFFF, "06x"),
                    format(data["secondary_color"] & 0xFFFFFF, "06x"),
                ],
                "ingredient": {"item": primer},
                "inUltimateSingularity": True,
            }
            path = os.path.join(OUT_DIR, "%s.json" % variant)
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                json.dump(obj, handle, indent=2)
                handle.write("\n")
            # EC's SingularityItem renders the display name as "%s Singularity" (its own
            # item.extendedcrafting.singularity lang), filling %s with this value - so emit the
            # BARE resource name here, NOT "<X> Singularity", or it doubles to "Iron Singularity
            # Singularity". Matches EC's own convention (singularity.extendedcrafting.iron = "Iron").
            lang[key] = title(variant)
            written.append(variant)

    with open(LANG, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(lang, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    print("Source jar: %s" % os.path.basename(jar))
    print("Wrote %d vanilla singularities + %d lang entries." % (len(written), len(lang)))
    print("  " + ", ".join(written))
    print("Skipped %d modded variants." % len(skipped))


if __name__ == "__main__":
    main()
