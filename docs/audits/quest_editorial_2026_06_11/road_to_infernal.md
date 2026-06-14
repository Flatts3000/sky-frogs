# Audit: road_to_infernal ("Road to the Infernal" / Tier 5 gateway)

Mod(s) referenced: Productive Frogs (Spawnery, Slime Milker, Froglight, slime/milk buckets), Industrial Foregoing (Dissolution Chamber), vanilla (Nether portal, Nether Fortress, nether bricks), Iron Jetpacks (Tide verb, implied). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| A Portal to the Nether | 10 obsidian + flint & steel builds a corner-skippable portal frame | chapter task: 10x obsidian + 1x flint_and_steel; vanilla minimal portal = 10 obsidian | MATCHES |
| Into the Nether | The Nether here is a floorless/ceilingless void you fly with a jetpack | config/skyblockbuilder/dimensions.json5 ("the Nether stays the SkyblockBuilder void Nether"), world.json5 | MATCHES |
| Raid a Fortress | A Nether Fortress floats out in the void; mine its nether brick | config/skyblockbuilder/structures.json5 (fortress + bastion whitelisted); task = 4x minecraft:nether_bricks | MATCHES (but item is the BLOCK "Nether Bricks", not "Nether Brick" - see terminology) |
| | | | VERIFY: VERIFIED - turn-in is `minecraft:nether_bricks` (block "Nether Bricks"); `minecraft:nether_brick` is the smelted item "Nether Brick". Terminology fix correct. |
| Raid a Fortress | Nether brick is "the only thing the void Nether hands out" | structures.json5 enables fortress/bastion (whole fortress loot reachable); the void Nether also yields blaze rods, wither skulls, etc. via fortress mobs | OVERSTATED (nether brick is the unique *block* the terrain gives, but the fortress hands out more); minor - acceptable as flavor |
| Infernal Frogspawn | Prime the Spawnery with a Nether Brick -> draws an Infernal Frogspawn | pack override data/productivefrogs/tags/item/spawnery_primer/infernal.json = `["minecraft:nether_bricks"]` (PF jar default is blaze_powder; pack REPLACES it) | MATCHES (pack override is truth; the item is "Nether Bricks" the block) |
| | | | VERIFY: VERIFIED - pack override `spawnery_primer/infernal.json` = `{"replace":true,"values":["minecraft:nether_bricks"]}` (the BLOCK), replacing PF jar default `blaze_powder`. This is the easy-to-miss PF-override class and the audit caught it. "Nether Brick" -> "Nether Bricks" fix correct. |
| A Bucket of Netherrack Slime | Dissolution Chamber: Nautilus Shell + prismarine filler -> Netherrack Slime bucket | pack override kubejs/server_scripts/dissolution_slime_recipes.js line 101: `['netherrack','minecraft:nautilus_shell']` under INFERNAL filler `minecraft:prismarine` | MATCHES |
| | | | VERIFY: VERIFIED - line 101 `['netherrack','minecraft:nautilus_shell']`, INFERNAL filler `minecraft:prismarine`. PF lang `slime_bucket.netherrack` = "Bucket of Netherrack Slime". Desc terminology fix ("...in a Bucket" -> "Bucket of...") correct. |
| A Bucket of Netherrack Slime | "Same Dissolution Chamber from the Tide" (IF machine) | dissolution_slime_recipes.js header: "Industrial Foregoing tech; chamber lives in road_to_tide.snbt" | MATCHES |
| Milk It | Slime Milker turns the slime bucket into Netherrack Slime Milk; placed milk spawns Netherrack Slimes | PF jar assets lang: "Slime Milker"; jei.slime_milker.info (Slime Bucket -> matching Slime Milk bucket); jei.slime_milk.info (placed -> periodically spawns the variant slime) | MATCHES |
| First Netherrack | Infernal frog eats a Netherrack Slime, leaves a Netherrack Froglight; smelt -> netherrack | PF jar data/productivefrogs/recipe/configurable_froglight_netherrack_to_netherrack.json (smelting, slime_variant=netherrack -> minecraft:netherrack); task = configurable_froglight w/ slime_variant netherrack | MATCHES |

## Per-quest findings

### A Portal to the Nether (quest.5140000000000002)
- Disposition: CLEAN
- Mechanics accurate (10 obsidian, corner-skip, flint and steel, void Nether). Voice good, codes balanced.

### Into the Nether (quest.5140000000000007)
- Disposition: CLEAN
- Void-Nether-with-jetpack framing matches dimensions.json5. Concise, balanced codes.

### Raid a Fortress (quest.514000000000000A)
- Disposition: EDIT
- Issues: Terminology: the turn-in item is the BLOCK `minecraft:nether_bricks` ("Nether Bricks"), not the item "Nether Brick"; text says "nether brick" (singular). Minor accuracy: "the only thing the void Nether hands out" overstates it (the fortress yields more); soften to keep it true without losing the flavor.
- BEFORE:
  quest.514000000000000A.quest_desc: [
  	"Somewhere out in the dark a &cNether Fortress&r floats. Find it, fly to it, mine its &enether brick&r - the only thing the void Nether hands out, and the key to the Infernal frog."
  ]
- AFTER:
  quest.514000000000000A.quest_desc: [
  	"Somewhere out in the dark a &cNether Fortress&r floats. Find it, fly to it, and mine its &eNether Bricks&r - the void Nether's one terrain block, and the key to the Infernal frog."
  ]

### Infernal Frogspawn (quest.514000000000000D)
- Disposition: EDIT
- Issues: Terminology: the primer item is the block "Nether Bricks" (`minecraft:nether_bricks`), so "Nether Brick" reads as the wrong item. Match the block name for clarity (the override and the prior quest's turn-in are both the block). Subtitle has the same singular.
- BEFORE:
  quest.514000000000000D.quest_desc: [
  	"Home again. Prime the &eSpawnery&r with a &eNether Brick&r and it draws an &cInfernal Frogspawn&r."
  	""
  	"The fortress trip was the toll; the frog automates the rest."
  ]
  quest.514000000000000D.quest_subtitle: "Feed the brick to the Spawnery."
- AFTER:
  quest.514000000000000D.quest_desc: [
  	"Home again. Prime the &eSpawnery&r with your &eNether Bricks&r and it draws an &cInfernal Frogspawn&r."
  	""
  	"The fortress trip was the toll; the frog automates the rest."
  ]
  quest.514000000000000D.quest_subtitle: "Feed the bricks to the Spawnery."

### A Bucket of Netherrack Slime (quest.5140000000000010)
- Disposition: EDIT
- Issues: Terminology: the chamber output item is "Bucket of Netherrack Slime" (PF lang `slime_bucket.netherrack`); desc calls it "Netherrack Slime in a Bucket" (stale ordering). Title already uses the correct "A Bucket of Netherrack Slime" - align the desc to it.
- BEFORE:
  quest.5140000000000010.quest_desc: [
  	"Same &eDissolution Chamber&r from the Tide. Feed it a &bNautilus Shell&r and &eprismarine&r filler for a &cNetherrack Slime in a Bucket&r."
  ]
- AFTER:
  quest.5140000000000010.quest_desc: [
  	"Same &eDissolution Chamber&r from the Tide. Feed it a &bNautilus Shell&r and &eprismarine&r filler for a &cBucket of Netherrack Slime&r."
  ]

### Milk It (quest.5140000000000013)
- Disposition: CLEAN
- Slime Milker mechanic (slime bucket -> Netherrack Slime Milk; placed milk spawns slimes) matches PF JEI text. "Pour the slime into a Slime Milker" is a fair plain-language gloss of the input slot. Codes balanced.

### First Netherrack (quest.5140000000000016)
- Disposition: CLEAN
- Froglight smelt chain (Netherrack Froglight -> netherrack) verified against PF recipe. "Froglight" used correctly (not "Configurable Froglight"). Codes balanced.

## Chapter summary
- Quests: 7 total, 3 EDIT, 4 CLEAN
- Accuracy bugs (WRONG ledger rows): 0 hard WRONG. One OVERSTATED claim (Raid a Fortress: "the only thing the void Nether hands out") softened in the EDIT. Three terminology fixes where text used "Nether Brick"/"Netherrack Slime in a Bucket" instead of the real in-game names "Nether Bricks" / "Bucket of Netherrack Slime".
- Highest-severity finding: Terminology drift on the load-bearing primer item - quests call the fortress drop / Spawnery primer "Nether Brick" (singular item), but both the task and the pack's `spawnery_primer/infernal.json` override use the BLOCK `minecraft:nether_bricks` ("Nether Bricks"). A new player searching JEI for "Nether Brick" finds the wrong (smelted) item. Note for the verify pass: the infernal primer is a PACK OVERRIDE (PF jar default is blaze_powder) - the "Nether Bricks" claim is correct only because of `pack/kubejs/data/productivefrogs/tags/item/spawnery_primer/infernal.json`.
