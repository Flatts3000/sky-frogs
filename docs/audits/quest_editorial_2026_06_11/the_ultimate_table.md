# Audit: the_ultimate_table ("The Ultimate Table")

Mod(s) referenced: Extended Crafting (1.21.1-7.0.8), Productive Frogs (1.20.0), Mekanism. Generated chapter: no.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Black Iron | Endgame crafting spine is Extended Crafting | chapter icons + EC recipes | MATCHES |
| Black Iron | Iron + black dye -> Black Iron | EC `recipe/black_iron_ingot.json` (shapeless: `c:ingots/iron` + `c:dyes/black`) | MATCHES |
| Black Iron | Black dye is "your Tide frog's ink" | PF `slime_variant/ink_sac.json` (category `tide`, primer `minecraft:ink_sac`); ink_sac -> black dye | MATCHES |
| Luminessence | Glowstone, redstone, gunpowder fuse into Luminessence | EC `recipe/luminessence.json` (2x `c:dusts/glowstone` + `c:dusts/redstone` + `minecraft:gunpowder` -> 2 Luminessence) | MATCHES |
| Luminessence | "the spark inside every Extended Crafting component" | EC `recipe/basic_component.json` contains `extendedcrafting:luminessence` | MATCHES |
| Basic Table | "3x3 table that eats the Luminessence components" | EC book `tables.page.1` (3x3/5x5/7x7/9x9); basic_table built from basic_component (contains Luminessence) | MATCHES |
| Advanced Table | "5x5, feed it a gold block and the basic table" | EC `recipe/advanced_table.json` (`I: c:storage_blocks/gold`, `C: basic_table`) | MATCHES |
| Elite Table | "7x7, built on a diamond block" | EC `recipe/elite_table.json` (`I: c:storage_blocks/diamond`, `C: advanced_table`) | MATCHES |
| Ultimate Table | "9x9, crowned with an emerald block" | EC `recipe/ultimate_table.json` (`I: c:storage_blocks/emerald`, `C: elite_table`) | MATCHES |
| Ultimate Table | "the only one that can craft a Master Frog" | pack `void_recipes.js` Master Frog is a **vanilla 3x3** `event.shaped`, NOT an Ultimate Table recipe; the Ultimate Table crafts the Ultimate **Singularity** (EC `recipe/ultimate_singularity.json`, type `extendedcrafting:ultimate_singularity`), which is then the key ingredient of the 3x3 Master Frog craft | WRONG - the Ultimate Table crafts the Ultimate Singularity, not the Master Frog; the Master Frog is a normal 3x3 craft |
| | | | VERIFY: VERIFIED - `void_recipes.js` `kubejs:master_frog` is `event.shaped` (vanilla 3x3, FFF/FUF/sFs). EC `ultimate_singularity.json` is type `extendedcrafting:ultimate_singularity` (Ultimate Crafting Table recipe). Ultimate Table crafts the Singularity, not the Master Frog. AFTER fix correct. |
| Ultimate Catalyst | Compressor "burns" the catalyst to fold thousands into one | EC default singularity recipes consume the catalyst (`defaultCatalyst = extendedcrafting:ultimate_catalyst` in `extendedcrafting-common.toml`; pack README + toml note "+40 Ultimate Catalysts" consumed across the set) | MATCHES |
| Quantum Compressor | "presses a thousand of a frog's resource into a single Singularity" | `extendedcrafting-common.toml` `defaultMaterialsRequired = 1000` | MATCHES |
| Quantum Compressor | "one for every resource the frogs make" | `config/extendedcrafting/singularities/` = 57 JSONs (water/lava excluded; clarified in the next chapter's quest) | MATCHES (in-context) |
| Quantum Compressor | "It runs on power - wire it to your Mekanism grid" | EC book `compression.page.2` ("powered machine... only use power while crafting"); EC consumes FE, Mekanism supplies FE-compatible power | MATCHES |

## Per-quest findings

### Black Iron (quest.6EC0000000000002)
- Disposition: CLEAN

### Luminessence (quest.6EC0000000000005)
- Disposition: CLEAN
- Note: recipe yields 2 Luminessence per craft; "Make some; you will need a lot" already implies repetition, no change needed.

### The Basic Table (quest.6EC0000000000008)
- Disposition: CLEAN
- Note: in-game block name is "Basic Crafting Table"; quest uses "Basic Table" (the pack's established short form, consistent across the chapter). Acceptable.

### The Advanced Table (quest.6EC000000000000B)
- Disposition: CLEAN

### The Elite Table (quest.6EC000000000000E)
- Disposition: CLEAN

### The Ultimate Table (quest.6EC0000000000011)
- Disposition: EDIT
- Issues: Factual accuracy: "the only one that can craft a Master Frog" is wrong. The Master Frog is crafted on a **vanilla 3x3 grid** (`void_recipes.js`), not the Ultimate Table. What the Ultimate Table uniquely crafts is the **Ultimate Singularity**, which is then the key ingredient in the Master Frog recipe. Fix names the real mechanic without losing the "this is the endgame table" beat.
- BEFORE:
  quest.6EC0000000000011.quest_desc: [
  	"&69x9&r, crowned with an emerald block. The biggest grid in the pack, and the only one that can craft a Master Frog. Build the &6Ultimate Table&r."
  ]
- AFTER:
  quest.6EC0000000000011.quest_desc: [
  	"&69x9&r, crowned with an emerald block. The biggest grid in the pack, and the only one that can craft the &bUltimate Singularity&r - the key to the Master Frog. Build the &6Ultimate Table&r."
  ]

### The Ultimate Catalyst (quest.6EC0000000000014)
- Disposition: CLEAN
- Note: "burns" is correct for singularity recipes (the catalyst IS consumed, one per singularity; verified via toml + README). The general EC book line "does not get used up" applies to ordinary compression recipes, not the pack's singularity recipes.

### The Quantum Compressor (quest.6EC0000000000017)
- Disposition: CLEAN
- Note: in-game block name is exactly "Quantum Compressor" - matches. Power claim verified. "one for every resource the frogs make" is loose (water/lava excluded) but the immediately-following chapter quest states the exclusion explicitly, so it reads fine in sequence.

## Chapter summary
- Quests: 8 total, 1 EDIT, 7 CLEAN
- Accuracy bugs (WRONG ledger rows): 1
  - The Ultimate Table: "the only one that can craft a Master Frog" - the Master Frog is a vanilla 3x3 craft; the Ultimate Table crafts the Ultimate Singularity (the Master Frog's key ingredient).
- Highest-severity finding: The Ultimate Table quest mis-states what the table crafts (Master Frog vs Ultimate Singularity). Single-sentence fix; everything else in the chapter ground-truths clean.
