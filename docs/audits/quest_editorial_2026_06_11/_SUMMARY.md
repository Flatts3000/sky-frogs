# Quest-Text Editorial Audit - Master Summary

**Issue:** [#169 - Pre-release: holistic editorial review of all quest text](https://github.com/Flatts/sky-frogs/issues/169)
**Date:** 2026-06-11
**Scope:** All 27 FTB Quests chapters / ~332 quest blocks in `config/ftbquests/quests/lang/en_us.snbt`
**Method:** 27 read-only per-chapter audit agents (ground-truthed every mechanic claim against pack KubeJS overrides, Productive Frogs' own datapack, and the mod jars), then 3 adversarial-verification agents re-checked every accuracy finding. Per-chapter detail (mechanic-claims ledger + per-quest before/after) lives in the sibling `<chapter>.md` files.

## Headline numbers

- **27 chapters audited and signed off.**
- **~59 quests flagged for edit; ~273 clean.**
- **~33 confirmed factual-accuracy bugs** (the issue's top priority) - things a player following the text literally would get wrong.
- **1 false positive caught and rejected** by the verify pass (Mekanism Enrichment Chamber - see below).
- **2 generated chapters** (`whole_pond`, `sister_ponds`): fixes route to `tools/gen_completionist_chapters.py`, not the lang file.
- **2 structural (non-text) issues** flagged out of editorial scope.

## The false positive (why the verify pass earned its keep)

The Mekanism `Enrichment Chamber` quest promises "frog metals, doubled." The first-pass agent flagged this as mechanically impossible (it only checked the Mekanism jar + pack KubeJS). **It is real:** Productive Frogs ships the doubling in its OWN jar datapack - `data/productivefrogs/recipe/mekanism/*.json`, `mekanism:enriching`, metallic Froglight -> 2 dust (11 metals, mod-gated). Confirmed by an in-game JEI screenshot. The quest text is correct; no edit. Lesson recorded so cross-mod froglight mechanics are always checked against PF's datapack first.

## Confirmed accuracy bugs (the high-value fixes)

| Chapter | Quest | Bug | Fix |
|---------|-------|-----|-----|
| tools_and_things | First Goo | "mix in mycelium" - real `gooblock_tier1` uses **dirt** (clay+dirt+rotten flesh+sugar) | name dirt |
| tools_and_things | First Goo / Ferricore | invented "seed the soil" mechanic; real is `goospread` into an adjacent **iron block** | rewrite to goospread |
| tools_and_things | First Goo | "Primogel Goo Block" - item is **Primogel Goo** | drop "Block" |
| tools_and_things | Slime Churn | output named "Slime in a Bucket" - real is **Bucket of [Variant] Slime** | rename |
| tools_and_things | Ferricore Ingot | subtitle "starter alloy" - ferricore is a base metal | fix subtitle |
| tools_and_things | Vacuum the Floor | "a diamond and an ender pearl" - recipe is 1 diamond + **2 ender pearls** + 2 hoppers + 3 ferricore | fix count |
| cave_frogs | Redstone | "glow ink milk -> Redstone Slime" - real chain step is **breeze rod milk** | fix the chain |
| cave_frogs | Beyond Iron | lists lapis/obsidian (Geode/Infernal resources) as Cave; stale `(Chapter stub)` placeholder | trim scope, drop stub |
| cave_frogs | Breeze Rod | "wind charges and all" - froglight only yields a breeze rod | drop the claim |
| geode_frogs | Count/Speed/Quantity/Endless catalysts | quest names (Count/Speed/Quantity/Infinite) don't match in-game **Bountiful/Rapid/Teeming/Endless** | use real names |
| your_first_iron_ingot | Milk It | "Infinite Count Catalyst" - real item is **Endless Catalyst** | rename |
| scaling_the_colony | Raising the Line | breeding climb "1 in 5" - live config is **0.40 (~2 in 5)**; + `(new page placeholder text)` scaffolding | fix odds, remove scaffold |
| bog_frogs | Clay | "concrete starts with clay" (false) and "Botany Pot soil" (unsupported) | trim to terracotta/bricks |
| drowned_riches | Prismarine Crystals | sea lantern recipe stated backwards - real is **5 crystals + 4 shards** | fix recipe |
| infernal_frogs | Obsidian | "netherrack **milk** presses into..." - chamber takes the netherrack **item**, isn't a press | fix wording |
| void_frogs | Chorus Fruit | "Chorus Froglight" - item is **Chorus Fruit Froglight** | rename |
| welcome | String from Silk | "break the infested leaves for string" - real string comes from **crooking** them (breaking drops nothing) | fix mechanic |
| take_flight | Ultimate Coil | "emerald, the Geode capstone" - **diamond** is the capstone (emerald is just the ingredient) | drop "capstone" |
| mekanism | Steel | "smelt enriched iron into a Steel Ingot" - needs a **2nd carbon infusion** to steel dust, then smelt | add the step |
| melting_point | Feed the Fire | heat ladder "fire -> lava" - **lava (3) is cooler than fire (5)** | reorder |
| the_network | Disk Drive | "scale to 64k and beyond" - RS 2.0.8 caps at **64k** | drop "and beyond" |
| road_to_void | Into the End | "6 slices per cake" - End Cake is vanilla cake = **7 eats** | drop the number |
| the_ultimate_table | The Ultimate Table | "only one that can craft a Master Frog" - it crafts the **Ultimate Singularity** (the Master Frog is a 3x3 craft) | fix |
| master_pond | The Master Frog | "ring it with Froglights" - recipe is 6 Froglights + 1 Ultimate Singularity + **2 Sweetslime** | add sweetslime |
| sister_ponds (gen) | Powah crystals, Eclipse Alloy | census titles "Blazing/Niotic/Spirited/Nitro" -> "...Crystal"; "Eclipsealloy" -> "Eclipse Alloy" | fix in generator |
| whole_pond (gen) | Clay Ball | census title "Clay Ball" -> PF display name **Clay** | fix in generator |

(Plus ~25 voice/terminology/formatting EDITs - per-chapter files have the full before/after.)

## Cross-cutting decision needed: "Frogspawn" vs "Eggs"

The pack calls the species-unlock item "Bottle of <Species> Frog **Frogspawn**" in ~29 places (gateway chapters + Synthesize Life + Your First Iron Ingot). Productive Frogs' actual item name is "Bottle of <Species> Frog **Eggs**." This is a deliberate pack flavor term, but a new player searching JEI for "frogspawn" finds nothing. **Decision for the maintainer** (keep the flavor, or switch all to "Eggs" for JEI-searchability) - tracked, not yet applied either way.

## Structural / out-of-text-scope (route to issues, not this pass)

1. **`void_recipes.js` source comment** repeats the "6 slices" End Cake miscount - worth a one-line follow-up.

## Rejected during verification (false positives - do NOT act on)

1. **mekanism / Enrichment Chamber "doubling impossible":** REJECTED. The doubling ships in PF's own datapack (`data/productivefrogs/recipe/mekanism/*.json`). Quest text is correct.
2. **mekanism / Steel task item id mismatch:** REJECTED. AlmostUnified (`config/almostunified/unification/materials.json`, `mod_priorities: [minecraft, alltheores, mekanism]`) unifies `c:ingots/steel` and rewrites the Mekanism steel-ingot recipe output to `alltheores:steel_ingot` - the exact item the task requires. The task is completable; no structural fix needed. (The Steel *text* fix - naming the second carbon infusion - still stands; that's about recipe steps, not item identity.)

## Cross-cutting decision RESOLVED

- **Frogspawn vs Eggs:** maintainer chose **switch all to "Eggs"** (match PF's in-game item name for JEI-searchability). Apply across all ~29 occurrences.

## Acceptance (issue #169)

- [x] Every chapter reviewed and signed off (27/27).
- [ ] Apply verified fixes to `lang/en_us.snbt` + the generator; re-run `tools/validate_quests.py`.
- [ ] Add a "quest-text editorial review" gate to `docs/release_checklist.md`.
