#!/usr/bin/env python3
"""Generate Extended Crafting singularity definitions from Productive Frogs slime_variant data.

The Tier 6 / Void endgame requires one EC singularity per *vanilla* froglight resource (modded
variants are skipped - they are not pinned in the pack). Each singularity is flagged
``inUltimateSingularity`` so EC's auto-generated Ultimate Singularity recipe demands the full set:
a literal "you automated every frog" capstone. The compressor input is the item the variant's
Froglight SMELTS to - read from PF's own smelting recipes - because EC's singularity ingredient
and the Quantum Compressor's Cucumber ``IngredientWithCount`` input are both item/tag-value only
and cannot match a froglight's ``slime_variant`` data component (see
``pack/config/extendedcrafting/singularities/README.md``).

It reads the smelt result rather than the variant's ``primer_item`` (what you feed a slime to
make that variant) because the two are NOT interchangeable: they agree for every vanilla variant
but `experience`, whose primer is ``minecraft:book`` while its Froglight smelts to
``minecraft:experience_bottle``. Generating off the primer made the Experience Singularity demand
1000 books - an item the Experience frog never produces (#245).

Each singularity's gradient is taken straight from the frog variant's own
``primary_color`` / ``secondary_color`` so the cube matches the frog that feeds it.

The committed JSONs under ``pack/config/extendedcrafting/singularities/`` and the EC lang file are
the source of truth; re-run this only when Productive Frogs adds or removes vanilla variants.

Usage:
    python tools/gen_singularities.py [--jar PATH_TO_PRODUCTIVEFROGS_JAR]
"""
import argparse
import json
import os
import sys

import pf_jar

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "pack", "config", "extendedcrafting", "singularities")
LANG = os.path.join(REPO, "pack", "kubejs", "assets", "extendedcrafting", "lang", "en_us.json")

# The FLUID PAIR gets no singularity (maintainer ruling, #131): water and lava
# are fluid resources - their froglights melt in the Crucible and have no
# farmable item-form (the primer items kelp / pointed_dripstone have NO source
# on this skyblock, which made both singularities uncraftable and the Ultimate
# with them). Excluded HERE so a PF pin bump cannot resurrect the pair.
EXCLUDED = {"water", "lava"}


def find_jar(explicit):
    jar = pf_jar.find_jar(explicit)
    if jar is None:
        sys.exit("Could not locate a productivefrogs jar; pass --jar PATH explicitly.")
    return jar


def title(slug):
    return " ".join(word.capitalize() for word in slug.split("_"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", help="Path to the productivefrogs jar (default: Sky Frogs instance)")
    args = parser.parse_args()
    jar = find_jar(args.jar)

    resources = pf_jar.load_froglight_resources(jar)

    # Resolve every variant BEFORE writing anything. The ambiguity guard below is
    # fatal, and a mid-loop exit would leave the folder half-regenerated with the
    # stale-file sweep never run - a worse state to debug than the PF change that
    # triggered it.
    plan = []
    skipped = []
    for variant, data in sorted(pf_jar.load_variants(jar).items()):
        if not pf_jar.is_vanilla(data) or variant in EXCLUDED:
            skipped.append(variant)
            continue
        # A vanilla variant with no single smelt result has no resource to compress.
        # Today that cannot happen (only the excluded fluid pair lacks a smelting
        # recipe, and only the modded `silicon` carries two) - so treat it as a PF
        # change the maintainer must rule on, not something to guess through.
        results = resources.get(variant, [])
        if len(results) != 1:
            sys.exit(
                "Variant %r has %d Froglight smelt results (%s) - expected exactly 1. A PF "
                "change needs a ruling: exclude the variant, or pick the resource by hand. "
                "Nothing was written."
                % (variant, len(results), ", ".join(results) or "none")
            )
        plan.append((variant, data, results[0]))

    lang = {}
    written = []
    for variant, data, resource in plan:
        key = "singularity.extendedcrafting.%s" % variant
        obj = {
            "name": key,
            "colors": [
                format(data["primary_color"] & 0xFFFFFF, "06x"),
                format(data["secondary_color"] & 0xFFFFFF, "06x"),
            ],
            "ingredient": {"item": resource},
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

    # The generator owns the folder: delete singularity JSONs for variants that
    # are excluded or no longer vanilla, so removals propagate without hand-rm
    # (added with the #131 fluid-pair exclusion).
    removed = []
    for name in os.listdir(OUT_DIR):
        if name.endswith(".json") and name[:-5] not in written:
            os.remove(os.path.join(OUT_DIR, name))
            removed.append(name[:-5])

    with open(LANG, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(lang, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    print("Source jar: %s" % os.path.basename(jar))
    print("Wrote %d vanilla singularities + %d lang entries." % (len(written), len(lang)))
    print("  " + ", ".join(written))
    print("Skipped %d modded/excluded variants." % len(skipped))
    if removed:
        print("Removed %d stale singularity file(s): %s" % (len(removed), ", ".join(removed)))


if __name__ == "__main__":
    main()
