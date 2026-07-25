#!/usr/bin/env python3
"""Generate the two completionist census chapters (#121).

- **The Whole Pond** (``whole_pond.snbt``): one froglight-check quest per VANILLA
  variant, laid out as a top-down tree frog - head = Cave, body = Bog, the four
  limbs = Geode / Tide / Infernal / Void, toes and all (StephJ2Fan's pitch).
- **Sister Ponds** (``sister_ponds.snbt``): one quest per MODDED variant whose
  owning mod is in the pack, clustered into one column per mod.

Both chapters end in a capstone that depends on every census quest.

Quest ids are DETERMINISTIC (sha1 of the variant name, leading nibble forced
into 0-7), so re-running this after a PF bump adds new variants WITHOUT
changing existing ids - player completion survives regeneration. The script
also owns its lang entries: it strips every ``quest.<prefix>``/``chapter.<id>``
line it previously wrote from ``lang/en_us.snbt`` and splices a fresh block.

Re-run after every PF pin bump (alongside gen_singularities.py); the spare
layout slots absorb roster growth, and the script exits loudly when a zone
overflows so the frog can be redrawn deliberately.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pf_jar

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(REPO, "pack", "config", "ftbquests", "quests", "chapters")
LANG = os.path.join(REPO, "pack", "config", "ftbquests", "quests", "lang", "en_us.snbt")
ITEM_IDS = os.path.join(REPO, "tools", "data", "item_ids.txt")

GROUP = "0C4F0E0000000007"  # Completionist (the victory-lap shelf after Tier 6)
GOODFOOD = "9151543141235425281L"

VANILLA_PREFIX = "7F0C"  # The Whole Pond id block
MODDED_PREFIX = "70DD"   # Sister Ponds id block
VANILLA_CHAPTER_ID = VANILLA_PREFIX + "000000000001"
MODDED_CHAPTER_ID = MODDED_PREFIX + "000000000001"

# Every loaded-mod variant is craftable, so the census lists them all
# (maintainer ruling, reversing the brief only-craftable cut): the ATO metals
# chain off osmium milk (ato_slime_chain.js), fluorite enriches from calcite
# (fluorite_enriching.js), and uraninite orb-crafts from chain-farmed uranium.

# Mod ids that ship in the pack (variant conditions reference these).
LOADED_MODS = {
    "alltheores", "mekanism", "industrialforegoing", "refinedstorage",
    "powah", "fluxnetworks", "justdirethings",
}
MOD_LABELS = {  # column order + display
    "alltheores": "All the Ores",
    "powah": "Powah",
    "refinedstorage": "Refined Storage",
    "mekanism": "Mekanism",
    "industrialforegoing": "Industrial Foregoing",
    "fluxnetworks": "Flux Networks",
    "justdirethings": "Just Dire Things",
}
MOD_ORDER = ["alltheores", "powah", "refinedstorage", "mekanism",
             "industrialforegoing", "fluxnetworks", "justdirethings"]
# The three registries above are hand-maintained and consumed independently
# (LOADED_MODS gates inclusion, MOD_ORDER drives column emission, MOD_LABELS
# titles them) - a mod present in one but not the others would be SILENTLY
# dropped from the census. Keep them identical or fail loudly (PR #126 review).
assert LOADED_MODS == set(MOD_ORDER) == set(MOD_LABELS), \
    "LOADED_MODS / MOD_ORDER / MOD_LABELS drifted - the three mod registries must list the same mods"

# Column order within a mod: progression rank where the mod HAS a ladder,
# else tier order then name. ATO = the osmium seed-chain order
# (ato_slime_chain.js), Powah = the material ladder (orb energy cost),
# RS = base material then processor tiers, IF = the Bog chain order.
TIERS = ["cave", "geode", "bog", "tide", "infernal", "void"]
VARIANT_RANK = {
    "osmium": 0, "aluminum": 1, "lead": 2, "nickel": 3,
    "silver": 4, "tin": 5, "uranium": 6, "zinc": 7,
    "uraninite": 0, "energized_steel": 1, "dry_ice": 2, "blazing": 3,
    "niotic": 4, "spirited": 5, "nitro": 6,
    "silicon": 0, "quartz_enriched_iron": 1, "basic_processor": 2,
    "improved_processor": 3, "advanced_processor": 4,
    "plastic": 0, "pink_slime": 1,
    # Just Dire Things (#188): the material ladder (Ferricore t1 -> Eclipse
    # Alloy t4) first, then the Crucible fuel lane (Blaze/Voidflame/Eclipse
    # Ember). Material-then-fuel reads as JDT's own progression.
    "ferricore": 0, "blazegold": 1, "celestigem": 2, "eclipsealloy": 3,
    "blaze_ember": 4, "voidflame": 5, "eclipse_ember": 6,
}


def column_key(variants):
    def key(name):
        if name in VARIANT_RANK:
            return (0, VARIANT_RANK[name], name)
        cat = variants[name].get("category", "")
        return (1, TIERS.index(cat) if cat in TIERS else 9, name)
    return key

# Explicit census icons. Takes PRECEDENCE over primer_item (so a variant whose
# primer is not the intuitive icon can override it): used for tag-primed
# variants that have no primer_item AND for the JDT fuels, whose primer is a
# coal tier but whose payoff (and the more recognizable icon) is the refined
# fuel bucket the Crucible melts the Froglight into.
ICON_OVERRIDES = {
    "aluminum": "alltheores:aluminum_ingot",
    "lead": "alltheores:lead_ingot",
    "nickel": "alltheores:nickel_ingot",
    "osmium": "alltheores:osmium_ingot",
    "silver": "alltheores:silver_ingot",
    "tin": "alltheores:tin_ingot",
    "uranium": "alltheores:uranium_ingot",
    "zinc": "alltheores:zinc_ingot",
    "steel": "mekanism:ingot_steel",
    "fluorite": "mekanism:fluorite_gem",
    "refined_obsidian": "mekanism:ingot_refined_obsidian",
    "refined_glowstone": "mekanism:ingot_refined_glowstone",
    # JDT tag-primed materials (#188); celestigem is item-primed (resolves on
    # its own).
    "ferricore": "justdirethings:ferricore_ingot",
    "blazegold": "justdirethings:blazegold_ingot",
    "eclipsealloy": "justdirethings:eclipsealloy_ingot",
    # The JDT fuels prime off a coal tier, but the Crucible melts the Froglight
    # to the refined fuel bucket - show that, not the coal.
    "blaze_ember": "justdirethings:refined_t2_fluid_bucket",
    "voidflame": "justdirethings:refined_t3_fluid_bucket",
    "eclipse_ember": "justdirethings:refined_t4_fluid_bucket",
}

# --------------------------------------------------------------------------- #
# The frog. Top-down tree frog, drawn in half-step art units (scaled x1.5 on
# emit). Each zone is an ORDERED list of (x, y) slots, sized with spares so
# new variants fill in without redrawing. Category fill order is the chamber
# chain order (parsed from the jar is overkill - alphabetical within category
# would shuffle on additions, so we sort by name for stability).
# --------------------------------------------------------------------------- #
ZONES = {
    # head + bulging eyes (Cave, 9 today, 12 slots)
    "cave": [(-1, -7), (1, -7),                       # the eyes
             (0, -6), (-1.5, -5.5), (1.5, -5.5),
             (-0.75, -5), (0.75, -5), (0, -4.25),
             (-1.5, -4.25), (1.5, -4.25), (-0.75, -3.5), (0.75, -3.5)],
    # body (Bog, 14 today, 16 slots - widened for the PF 1.14 mob-drop wave)
    "bog": [(0, -2.5), (-1.25, -2), (1.25, -2),
            (-0.6, -1.25), (0.6, -1.25),
            (-1.4, -0.75), (1.4, -0.75), (0, -0.5),
            (-0.7, 0.1), (0.7, 0.1),
            (-1.4, 0.6), (1.4, 0.6), (0, 0.85),
            (-0.7, 1.6), (0.7, 1.6), (0, 2.35)],
    # front-left limb + 3 toes (Geode, 6 today, 8 slots)
    "geode": [(-2.25, -2.75), (-3.25, -3.25),
              (-4.25, -4.25), (-5, -3.5), (-4.5, -5.25),  # toes
              (-3.5, -2.25), (-2.75, -1.75), (-3, -4)],
    # front-right limb + toes (Tide, 9 today, 10 slots)
    "tide": [(2.25, -2.75), (3.25, -3.25), (3, -4),
             (4.25, -4.25), (5, -3.5), (4.5, -5.25),     # toes
             (3.5, -2.25), (2.75, -1.75), (3.75, -2.75), (4, -1.75)],
    # back-left limb + toes (Infernal, 12 today, 14 slots - the boss wave
    # thickened the thigh; extras APPEND so earlier slots stay put)
    "infernal": [(-2.25, 1.5), (-3.25, 2.25), (-3, 3.25),
                 (-4.25, 4.25), (-5, 3.5), (-4.5, 5.25),  # toes
                 (-3.5, 1), (-2.75, 2.75), (-3.75, 2.75), (-4, 1.75),
                 (-2.5, 0.5), (-4.5, 0.75), (-4.75, 2.5), (-5.25, 4.5)],
    # back-right limb + toes (Void, 9 today, 14 slots - mirrors Infernal)
    "void": [(2.25, 1.5), (3.25, 2.25), (3, 3.25),
             (4.25, 4.25), (5, 3.5), (4.5, 5.25),         # toes
             (3.5, 1), (2.75, 2.75), (3.75, 2.75), (4, 1.75),
             (2.5, 0.5), (4.5, 0.75), (4.75, 2.5), (5.25, 4.5)],
}
CAPSTONE_POS = (0, 4.0)  # below the body: the lily pad the frog sits toward


def det_id(prefix: str, key: str, salt: str = "") -> str:
    """Deterministic 16-hex id: prefix + 12 sha1 hex chars. The prefix's first
    char (7) keeps the long positive."""
    h = hashlib.sha1(f"{key}|{salt}".encode()).hexdigest().upper()
    return prefix + h[:12]


# Variant slugs whose in-game display name a plain title_case() gets wrong (issue #169).
# Keyed on the variant slug; value is the exact name shown in-game (and in JEI), so the
# census title matches what the player is hunting for. Verified against the mod jars' lang.
DISPLAY_OVERRIDES = {
    "clay_ball": "Clay",             # PF froglight display is "Clay Froglight" (not "Clay Ball")
    "blazing": "Blazing Crystal",    # Powah
    "niotic": "Niotic Crystal",      # Powah
    "spirited": "Spirited Crystal",  # Powah
    "nitro": "Nitro Crystal",        # Powah
    "eclipsealloy": "Eclipse Alloy", # Just Dire Things renders it two words
}


def title_case(slug: str) -> str:
    if slug in DISPLAY_OVERRIDES:
        return DISPLAY_OVERRIDES[slug]
    return " ".join(w.capitalize() for w in slug.split("_"))


def load_allowlist() -> set[str]:
    return {l.strip() for l in open(ITEM_IDS, encoding="utf-8") if l.strip()}


def variant_mod(data: dict) -> str | None:
    c = data.get("neoforge:conditions")
    if not c:
        return None
    mods = re.findall(r'"modid":\s*"([a-z_0-9]+)"', json.dumps(c))
    if not mods:
        return None
    # Multi-provider variants (only silicon today: an `or` of ae2 / refinedstorage)
    # list several modids. Take the one this pack actually loads, not just the first
    # in the JSON - else silicon binds to ae2 (listed first, never shipped here) and
    # falls out of the census entirely.
    for m in mods:
        if m in LOADED_MODS:
            return m
    return mods[0]


def quest_block(qid, tid, icon, variant, x, y, deps=None, rewards=None,
                task=None, shape=None, size=None):
    # The half-step art units x1.5 produce float artifacts (0.6 * 1.5 ->
    # 0.8999999999999999); round so the emitted SNBT reads as drawn.
    x, y = round(x, 4), round(y, 4)
    dep_line = ""
    if deps:
        dep_line = "\t\t\tdependencies: [" + ", ".join(f'"{d}"' for d in deps) + "]\n"
    shape_line = f'\t\t\tshape: "{shape}"\n' if shape else ""
    size_line = f"\t\t\tsize: {size}d\n" if size else ""
    if task is None:
        task = (f'\t\t\ttasks: [{{\n\t\t\t\tid: "{tid}"\n'
                f'\t\t\t\titem: {{ components: {{ "productivefrogs:slime_variant": "productivefrogs:{variant}" }}, count: 1, id: "productivefrogs:configurable_froglight" }}\n'
                f'\t\t\t\tmatch_components: "strict"\n\t\t\t\ttype: "item"\n\t\t\t}}]')
    reward_line = rewards or ""
    return (f"\t\t{{\n{dep_line}\t\t\ticon: {{\n\t\t\t\tid: \"{icon}\"\n\t\t\t}}\n"
            f"\t\t\tid: \"{qid}\"\n{shape_line}{size_line}{reward_line}{task}\n"
            f"\t\t\tx: {x}d\n\t\t\ty: {y}d\n\t\t}}")


def loot_reward(rid):
    return (f"\t\t\trewards: [{{\n\t\t\t\texclude_from_claim_all: true\n"
            f"\t\t\t\tid: \"{rid}\"\n\t\t\t\ttable_id: {GOODFOOD}\n"
            f"\t\t\t\ttype: \"loot\"\n\t\t\t}}]\n")


def main():
    variants = pf_jar.load_variants(pf_jar.find_jar() or sys.exit("no PF jar - run sync_instance.py"))
    allow = load_allowlist()

    vanilla = sorted(n for n, d in variants.items() if pf_jar.is_vanilla(d))
    modded = {}
    for n, d in sorted(variants.items()):
        if pf_jar.is_vanilla(d):
            continue
        mod = variant_mod(d) or (d.get("primer_item") or ":").split(":")[0]
        if mod in LOADED_MODS:
            modded.setdefault(mod, []).append(n)
    for mod in modded:
        # A ranked column with an unranked newcomer would SILENTLY sort it to
        # the bottom, breaking the progression order (the exact playtest catch
        # that created VARIANT_RANK). Fail loudly instead (PR #126 review).
        if any(n in VARIANT_RANK for n in modded[mod]):
            unranked = [n for n in modded[mod] if n not in VARIANT_RANK]
            if unranked:
                sys.exit(f"mod '{mod}' sorts by VARIANT_RANK but {', '.join(unranked)} "
                         f"has no rank entry - add it so the column keeps progression order")
        modded[mod].sort(key=column_key(variants))

    lang: list[str] = []
    used_ids: set[str] = set()

    def claim(i):
        assert i not in used_ids, f"id collision: {i}"
        used_ids.add(i)
        return i

    # ---------------- The Whole Pond ----------------
    by_cat: dict[str, list[str]] = {}
    for n in vanilla:
        by_cat.setdefault(variants[n]["category"], []).append(n)
    quests = []
    all_vanilla_qids = []
    for cat, slots in ZONES.items():
        names = by_cat.get(cat, [])
        if len(names) > len(slots):
            sys.exit(f"zone '{cat}' overflow: {len(names)} variants, {len(slots)} slots - redraw the frog")
        for name, (zx, zy) in zip(names, slots):
            qid = claim(det_id(VANILLA_PREFIX, name))
            tid = claim(det_id(VANILLA_PREFIX, name, "task"))
            icon = ICON_OVERRIDES.get(name) or variants[name].get("primer_item") \
                or f"minecraft:{name}"
            if icon not in allow:
                icon = "productivefrogs:configurable_froglight"
            quests.append(quest_block(qid, tid, icon, name, zx * 1.5, zy * 1.5))
            lang.append(f'\tquest.{qid}.title: "{title_case(name)}"')
            all_vanilla_qids.append(qid)
    cap_q = claim(det_id(VANILLA_PREFIX, "__capstone__"))
    cap_t = claim(det_id(VANILLA_PREFIX, "__capstone__", "task"))
    cap_r = claim(det_id(VANILLA_PREFIX, "__capstone__", "reward"))
    quests.append(quest_block(
        cap_q, cap_t, "minecraft:lily_pad", None,
        CAPSTONE_POS[0] * 1.5, CAPSTONE_POS[1] * 1.5,
        deps=all_vanilla_qids, rewards=loot_reward(cap_r),
        task=f'\t\t\ttasks: [{{\n\t\t\t\tid: "{cap_t}"\n\t\t\t\ttype: "checkmark"\n\t\t\t}}]',
        shape="hexagon", size=2.0))
    lang += [
        # Single-line array on purpose: FTB collapses a one-string desc onto one
        # line when it rewrites the file on world save, so emitting that form
        # keeps a regen a true no-op instead of churning the diff every time.
        f'\tquest.{cap_q}.quest_desc: ["Every vanilla resource the frogs make, accounted for."]',
        f'\tquest.{cap_q}.quest_subtitle: "Sit. You\'ve earned the lily pad."',
        f'\tquest.{cap_q}.title: "The Whole Pond"',
        f'\tchapter.{VANILLA_CHAPTER_ID}.title: "The Whole Pond"',
    ]
    chapter = (f'{{\n\tautofocus_id: "{cap_q}"\n\tdefault_hide_dependency_lines: true\n'
               f'\tdefault_quest_shape: ""\n\tfilename: "whole_pond"\n\tgroup: "{GROUP}"\n'
               f'\ticon: {{\n\t\tid: "minecraft:lily_pad"\n\t}}\n\tid: "{VANILLA_CHAPTER_ID}"\n'
               f"\torder_index: 0\n\tquest_links: [ ]\n\tquests: [\n"
               + "\n".join(quests) + "\n\t]\n}\n")
    open(os.path.join(CHAPTERS, "whole_pond.snbt"), "w", encoding="utf-8", newline="\n").write(chapter)

    # ---------------- Sister Ponds ----------------
    quests = []
    all_mod_qids = []
    for col, mod in enumerate(m for m in MOD_ORDER if m in modded):
        x = col * 2.0
        for row, name in enumerate(modded[mod]):
            qid = claim(det_id(MODDED_PREFIX, name))
            tid = claim(det_id(MODDED_PREFIX, name, "task"))
            icon = ICON_OVERRIDES.get(name) or variants[name].get("primer_item") \
                or "productivefrogs:configurable_froglight"
            if icon not in allow:
                icon = "productivefrogs:configurable_froglight"
            quests.append(quest_block(qid, tid, icon, name, x, row * 1.5))
            lang.append(f'\tquest.{qid}.title: "{title_case(name)} ({MOD_LABELS[mod]})"')
            all_mod_qids.append(qid)
    cap_q = claim(det_id(MODDED_PREFIX, "__capstone__"))
    cap_t = claim(det_id(MODDED_PREFIX, "__capstone__", "task"))
    cap_r = claim(det_id(MODDED_PREFIX, "__capstone__", "reward"))
    n_cols = len([m for m in MOD_ORDER if m in modded])
    quests.append(quest_block(
        cap_q, cap_t, "productivefrogs:sweetslime", None,
        (n_cols - 1), -2.5,
        deps=all_mod_qids, rewards=loot_reward(cap_r),
        task=f'\t\t\ttasks: [{{\n\t\t\t\tid: "{cap_t}"\n\t\t\t\ttype: "checkmark"\n\t\t\t}}]',
        shape="hexagon", size=2.0))
    lang += [
        f'\tquest.{cap_q}.quest_desc: ["Every modded resource the frogs make, accounted for."]',
        f'\tquest.{cap_q}.quest_subtitle: "Diplomacy, by froglight."',
        f'\tquest.{cap_q}.title: "Sister Ponds"',
        f'\tchapter.{MODDED_CHAPTER_ID}.title: "Sister Ponds"',
    ]
    chapter = (f'{{\n\tautofocus_id: "{cap_q}"\n\tdefault_hide_dependency_lines: true\n'
               f'\tdefault_quest_shape: ""\n\tfilename: "sister_ponds"\n\tgroup: "{GROUP}"\n'
               f'\ticon: {{\n\t\tid: "productivefrogs:sweetslime"\n\t}}\n\tid: "{MODDED_CHAPTER_ID}"\n'
               f"\torder_index: 1\n\tquest_links: [ ]\n\tquests: [\n"
               + "\n".join(quests) + "\n\t]\n}\n")
    open(os.path.join(CHAPTERS, "sister_ponds.snbt"), "w", encoding="utf-8", newline="\n").write(chapter)

    # ---------------- lang splice (the script owns its keys) ----------------
    text = open(LANG, encoding="utf-8").read()
    # The value branch order matters (#223). FTB collapses a short array onto one
    # line when it rewrites the file on world save, so a multi-line-array pattern
    # tried first will match that single-line "[" and then run on to the NEXT
    # multi-line "]" in the file, deleting every hand-authored key in between.
    # Only treat "[" as multi-line when the line actually ends there.
    text = re.sub(r"\t(?:quest\.(?:" + VANILLA_PREFIX + "|" + MODDED_PREFIX + r")[0-9A-F]+|chapter\.(?:"
                  + VANILLA_CHAPTER_ID + "|" + MODDED_CHAPTER_ID + r"))\.[a-z_]+:(?: \[\n[\s\S]*?\n\t\]|[^\n]*)\n",
                  "", text)
    # The splice lands just above the Cave Frogs lang block (7CA7 prefix) so the
    # census keys sit together. That chapter is NOT this script's to control -
    # if its keys ever vanish (regenerated ids, hand edit, FTB rewrite), exit
    # with a real message instead of an AttributeError (PR #126 review).
    anchor = re.search(r"\tquest\.7CA7", text)
    if anchor is None:
        sys.exit("lang splice anchor 'quest.7CA7' (the Cave Frogs block) not found in "
                 "en_us.snbt - pick a new anchor in gen_completionist_chapters.py "
                 "before regenerating")
    block = "\n".join(lang) + "\n"
    text = text[:anchor.start()] + block + text[anchor.start():]
    open(LANG, "w", encoding="utf-8", newline="\n").write(text)

    print(f"whole_pond: {len(all_vanilla_qids)} census quests + capstone")
    print(f"sister_ponds: {len(all_mod_qids)} census quests + capstone "
          f"({', '.join(m for m in MOD_ORDER if m in modded)})")
    print(f"lang: {len(lang)} lines spliced")


if __name__ == "__main__":
    main()
