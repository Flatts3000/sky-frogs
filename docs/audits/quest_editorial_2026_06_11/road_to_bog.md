# Audit: road_to_bog ("The Road to Bog" / Tier 3 gateway)

Mod(s) referenced: Productive Frogs (Spawnery, Slime Milker, Froglight, slime/milk buckets, frogspawn), Mekanism (Enrichment Chamber, Metallurgic Infuser), vanilla (mossy cobblestone, diamond, dirt). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Enrich a Diamond | Run a diamond through the Enrichment Chamber -> Enriched Diamond | Mekanism `data/mekanism/recipe/enriching/enriched/diamond.json`: `mekanism:enriching`, input tag `c:gems/diamond` -> `mekanism:enriched_diamond` | MATCHES |
| The Road to Bog | Prime the Spawnery with the Enriched Diamond (+ slime ball fuel) -> Bog Frogspawn bottle | pack override `kubejs/data/productivefrogs/tags/item/spawnery_primer/bog.json` = `["mekanism:enriched_diamond"]` (PF jar default is `clay_ball`; pack REPLACES); SpawneryBlockEntity.class string `"spawnery @%s: ignite, slime ball consumed"` confirms slime-ball fuel + primer model; `config/productivefrogs-common.toml` `[spawnery] enabled=true` | MATCHES |
| Mossy Cobblestone | Infuse cobblestone with Bio in the Metallurgic Infuser (10 mB each) -> mossy cobblestone | Mekanism `data/mekanism/recipe/metallurgic_infusing/mossy/cobblestone.json`: `metallurgic_infusing`, item_input cobblestone + chemical_input 10 mB tag `mekanism:bio`, `per_tick_usage:false` -> `minecraft:mossy_cobblestone` | MATCHES (chemical's in-game display name is "Biomass", not "bio fuel" - see terminology) VERIFY: VERIFIED - Mekanism lang `chemical.mekanism.bio` = "Biomass"; `tag.item.c.fuels.bio` = "Bio Fuels" (the separate feedstock item). The chemical that goes in the Infuser displays as "Biomass"; "bio fuel" mislabels it. Fix to "Biomass" correct. |
| Mossy Cobblestone | Mossy cobblestone seeds the first Bog slime (the tier filler) | pack `kubejs/server_scripts/bog_slime_chain.js` (every Bog step takes 4x `minecraft:mossy_cobblestone`); `mossy_cobblestone_gate.js` header confirms it is the Bog filler block | MATCHES |
| A Dirt Slime in a Bucket | Craft from diamond Slime Milk + 4 mossy cobblestone + 3 sweetslime + Bog frogspawn | pack `bog_slime_chain.js` bridge bootstrap: `diamond_slime_milk_bucket` + 4x `mossy_cobblestone` + 3x `sweetslime` + `frog_egg[contained_category=bog]` -> dirt slime bucket | MATCHES |
| A Bucket of Dirt Slime Milk | Run the Dirt Slime through the Slime Milker -> Dirt Slime Milk; pour it out and Dirt Slimes spawn | PF jar `assets` lang `block.productivefrogs.slime_milker = Slime Milker`; SlimeMilkerBlockEntity present; chapter task = `productivefrogs:dirt_slime_milk_bucket`; placed milk spawns the matching variant slime (PF milk-spawn economy) | MATCHES |
| Dirt | Feed Dirt Slimes to the Bog Frog -> Dirt Froglight; smelt -> dirt | PF jar `data/productivefrogs/recipe/configurable_froglight_dirt_to_dirt.json`: smelting, `slime_variant=dirt` -> `minecraft:dirt`; lang `...froglight.dirt = Dirt Froglight`; chapter task = `configurable_froglight` w/ `slime_variant:dirt` | MATCHES |

## Per-quest findings

### Enrich a Diamond (quest.70B000000000000E)
- Disposition: CLEAN
- Enrichment Chamber + tag `c:gems/diamond` -> enriched diamond verified. Voice tight, second-person, codes balanced (`&d`/`&b`/`&e` all closed with `&r`). "Crush it for more" subtitle fits the enriching grind flavor. No dashes.

### The Road to Bog (quest.70B0000000000002)
- Disposition: CLEAN
- Spawnery primer (enriched diamond, pack override) + slime-ball fuel both ground-truthed against the block entity and the primer tag. "Bog Frogspawn" framing matches the bottle the player gets. Codes balanced, ASCII-only ("-" used, no em/en dash).

### Mossy Cobblestone (quest.70B0000000000011)
- Disposition: EDIT
- Issues: Terminology - the Metallurgic Infuser's chemical input `mekanism:bio` displays in-game as **"Biomass"** (`chemical.mekanism.bio = Biomass`), not "bio fuel". "Bio Fuels" (`tag.item.c.fuels.bio`) is the *item* tag you compost/process to GET Biomass, a different thing - so "bio fuel" mislabels what goes in the machine's chemical tank. The "(10 mB of Bio each)" parenthetical is correct (the recipe is 10 mB, `per_tick_usage:false`). Light term-only fix; mechanic and amount are accurate.
- BEFORE:
  quest.70B0000000000011.quest_desc: [
  	"Stone doesn't belong in a swamp - it has to go &amossy&r first."
  	""
  	"Infuse &7cobblestone&r with &abio fuel&r in the &eMetallurgic Infuser&r (10 mB of Bio each). Mossy cobblestone is the organic stand-in for plain stone that seeds the first Bog slime."
  ]
- AFTER:
  quest.70B0000000000011.quest_desc: [
  	"Stone doesn't belong in a swamp - it has to go &amossy&r first."
  	""
  	"Infuse &7cobblestone&r with &aBiomass&r in the &eMetallurgic Infuser&r (10 mB each). Mossy cobblestone is the organic stand-in for plain stone that seeds the first Bog slime."
  ]

### A Dirt Slime in a Bucket (quest.70B0000000000005)
- Disposition: CLEAN
- Recipe (diamond Slime Milk + 4 mossy cobblestone + 3 sweetslime + Bog frogspawn) matches `bog_slime_chain.js` bridge bootstrap exactly: counts, filler, and the diamond-milk -> dirt-slime crossover all verified. Title "A Dirt Slime in a Bucket" vs the item's literal name "Bucket of Dirt Slime" is the established pack convention (used across every tier's slime-bucket quest), so not flagged. Single-line desc, codes balanced, no dashes-as-punctuation.

### A Bucket of Dirt Slime Milk (quest.70B0000000000008)
- Disposition: CLEAN
- "Slime Milker" is the exact block name; "Dirt Slime Milk" matches the fluid/block lang (item is "Bucket of Dirt Slime Milk"). "Run the Dirt Slime through the Slime Milker" is the pack-wide phrasing for the milking step (Cave/Geode use the same) and reads true to the milk-spawn loop. Concise, balanced.

### Dirt (quest.70B000000000000B)
- Disposition: CLEAN
- Dirt Froglight drop + smelt-to-dirt both verified against the smelting recipe and the froglight lang. Task is the Froglight (slime_variant=dirt), per the pack's froglight-check law - prose ("Turn one in - then smelt the rest") matches. "Froglight" used correctly (never "Configurable Froglight"). Codes balanced, ASCII-only.

## Chapter summary
- Quests: 6 total, 1 EDIT, 5 CLEAN
- Accuracy bugs (WRONG ledger rows): 0 - every mechanic claim ground-truthed and MATCHES (Mekanism enriching/infusing recipes, the pack's `spawnery_primer/bog` override to enriched diamond, the Spawnery slime-ball fuel model, the bog slime-chain bridge recipe, and the dirt froglight smelt).
- Highest-severity finding: the lone edit is terminology only - quest 70B0000000000011 calls the Metallurgic Infuser's chemical input "bio fuel" when its in-game name is "Biomass" ("Bio Fuels" is the separate feedstock item tag). Mechanic and the 10 mB figure are correct.
