# Audit: melting_point ("The Froglight Crucible" chapter)

Mod(s) referenced: Productive Frogs (Froglight Crucible, Casting Mold, melt/cast recipes, heat data maps), Ex Deorum (Oak Crucible, Tier 0), Powah (Blazing Crystal Froglight), JEI (recipe viewer), All The Ores (molten iron tag). Generated chapter: no.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| The Froglight Crucible | Crucible melts Froglights into fluids (water, lava, molten metal), no GUI/no power, heat from block underneath | PF `crucible_melt_*.json` (type `crucible_melting`); `data_maps/block/crucible_heat.json` keys are placed blocks under the basin | MATCHES |
| The Froglight Crucible | Crucible built from iron + bricks (cobble -> dust -> clay -> bricks, framed in iron) | PF `recipe/crucible.json` = shaped, key I=iron_ingot, B=minecraft:brick, pattern frames iron over bricks | MATCHES (craft is iron+brick; the cobble->dust->clay->brick path is the Ex Deorum/hammer bootstrap to bricks, accurate) |
| The Froglight Crucible | "Oak Crucible wringing water out of leaves" (Tier 0 callback) | exdeorum-3.10.jar lang: `block.exdeorum.oak_crucible` family exists; wooden crucible melts leaves -> water | MATCHES |
| The Froglight Crucible | Park Crucible over a torch to start | `crucible_heat.json` torch=1 (lowest non-zero heat) | MATCHES |
| Feed the Fire | Heat ladder torch -> campfire -> fire -> lava | `crucible_heat.json`: torch=1, campfire=2, lava=3, fire=5 | WRONG (ordering): ascending heat is torch(1) < campfire(2) < lava(3) < fire(5). Prose lists fire before lava, but lava is COOLER than fire. -- VERIFY: VERIFIED. PF jar `data/productivefrogs/data_maps/block/crucible_heat.json`: torch=1, campfire=2, lava=3, fire=5. froglight_heat: lava=3, blaze=6 (>fire 5), blazing=10. So lava (3) IS cooler than fire (5); correct ascending order is torch->campfire->lava->fire. AFTER edit (torch, campfire, lava, fire) is correct -- apply. |
| Feed the Fire | Placed Lava Froglight heats like lava | `data_maps/.../froglight_heat.json`: `productivefrogs:lava` = 3; lava block = 3 | MATCHES |
| Feed the Fire | Blaze Froglight burns hotter than fire | froglight_heat blaze=6; crucible_heat fire=5 (6 > 5) | MATCHES |
| Feed the Fire | Powah's Blazing Crystal Froglight is the hottest plate in the mod | froglight_heat `blazing`=10 (powah-conditional); Powah-6.2.8.jar present; name `block.productivefrogs.configurable_froglight.blazing` = "Blazing Crystal Froglight" | MATCHES |
| Feed the Fire | "JEI's heat-ladder category lists every source" | jei-19.27.0 present; PF JEI category `productivefrogs.jei.category.crucible_heat` = "Crucible Heat Sources" | MATCHES (category exists; exact name is "Crucible Heat Sources") |
| Feed the Fire | Task: craft a campfire | chapter task = item `minecraft:campfire` x1 | MATCHES |
| Water | Water Froglight melts into a full bucket (1000 mB) of water | `crucible_melt_water.json` result `minecraft:water` amount 1000 | MATCHES |
| Water | Water slime craft: water bucket + 4 stone + 3 sweetslime + Cave frogspawn bottle, bucket returns empty | pack override `cave_slime_chain.js` fluids loop: `minecraft:water_bucket` + 4x stone + 3x sweetslime + cave frog_egg, shapeless (bucket returns) | MATCHES |
| Water | Task: turn in Water Froglight | chapter task = `configurable_froglight` w/ slime_variant water, strict | MATCHES |
| Lava | Lava Froglight melts into a full bucket (1000 mB) of lava | `crucible_melt_lava.json` result `minecraft:lava` amount 1000 | MATCHES |
| Lava | Lava slime craft: lava bucket + 4 stone + 3 sweetslime + Cave frogspawn bottle; whole loop at Tier 1 | `cave_slime_chain.js` fluids loop (lava); Cave = Tier 1 | MATCHES |
| The Casting Mold | Mold turns molten metal back into ingots; pour with bucket, pipe it, or tower heat+Crucible+Mold so Mold drinks from the basin | `mold_cast_iron.json` type `mold_casting`, fluid `c:molten_iron` 90 mB -> 1 iron_ingot; CastingMoldBlockEntity + casting_tower.png image | MATCHES |
| The Casting Mold | Task: craft a Casting Mold | chapter task = `productivefrogs:casting_mold` x1; recipe `casting_mold.json` = iron+brick | MATCHES |
| The Tower | A metal Froglight melts into TWO ingots worth of molten metal (the pack's ore doubling) | iron melt = 180 mB molten iron (`crucible_melt_iron.json` w/ alltheores, `_pf` fallback 180); mold cast = 90 mB/ingot -> 180/90 = 2 ingots. Smelting one froglight = 1 ingot (`configurable_froglight_iron_to_iron_ingot.json`). | MATCHES (2x vs smelting) |

## Per-quest findings

### The Froglight Crucible (quest.3E17000000000002)
- Disposition: EDIT
- Issues: Voice/verbosity: the build paragraph packs the entire cobble->dust->clay->brick bootstrap into one long sentence; tighten without losing the steps. Terminology is clean ("Froglights", "Froglight Crucible"). No accuracy errors.
- BEFORE:
  ```
  quest.3E17000000000002.quest_desc: [
  	"Remember the &eOak Crucible&r wringing water out of leaves? Meet its big sibling: a &fbrick-and-iron basin&r that melts &bFroglights&r into &9fluids&r - water, lava, molten metal - no GUI, no power, just heat rising from whatever block sits underneath."
  	""
  	"The build is &firon&r and &cbricks&r: hammer cobblestone all the way down to &7dust&r, mix the dust into a &9water barrel&r for clay, smelt the clay into bricks, and frame them in iron."
  	""
  	"Craft the &eCrucible&r and park it over a &etorch&r to start."
  ]
  ```
- AFTER:
  ```
  quest.3E17000000000002.quest_desc: [
  	"Remember the &eOak Crucible&r wringing water out of leaves? Meet its big sibling: a &fbrick-and-iron basin&r that melts &bFroglights&r into &9fluids&r - water, lava, molten metal - no GUI, no power, just heat rising from the block underneath it."
  	""
  	"You need &cbricks&r and &firon&r. Hammer cobblestone down to &7dust&r, mix the dust with &9water&r for clay, smelt the clay into bricks, and frame them in iron."
  	""
  	"Craft the &eCrucible&r and set it over a &etorch&r to start."
  ]
  ```

### Feed the Fire (quest.3E17000000000005)
- Disposition: EDIT
- Issues: Factual (ordering): heat ladder lists "torch -> campfire -> fire -> lava", but lava (heat 3) is COOLER than fire (heat 5). Correct ascending order is torch -> campfire -> lava -> fire. Voice/verbosity: dense run-on; trim.
- BEFORE:
  ```
  quest.3E17000000000005.quest_desc: [
  	"The ladder climbs from &etorch&r to &6campfire&r to &cfire&r to &6lava&r - and Froglights burn too: a placed &6Lava Froglight&r heats like lava, a &cBlaze Froglight&r burns hotter than fire, and Powah's &cBlazing Crystal Froglight&r is the hottest plate in the mod. Your farmed decor doubles as the smelter's fire. JEI's heat-ladder category lists every source."
  	""
  	"Craft a &6campfire&r - the first real step up from the torch."
  ]
  ```
- AFTER:
  ```
  quest.3E17000000000005.quest_desc: [
  	"Hotter heat melts faster. The ladder climbs &etorch&r, &6campfire&r, &6lava&r, &cfire&r - and Froglights burn too: a placed &6Lava Froglight&r heats like lava, a &cBlaze Froglight&r hotter than fire, and Powah's &cBlazing Crystal Froglight&r is the hottest source in the mod."
  	""
  	"Your farmed decor doubles as the smelter's fire. Check JEI's &eCrucible Heat Sources&r page for the full list."
  	""
  	"Craft a &6campfire&r - the first step up from the torch."
  ]
  ```

### Water (quest.3E17000000000008)
- Disposition: CLEAN
- Note: Subtitle "The ocean, bottled." and desc all verified accurate (1000 mB water, slime craft = water bucket + 4 stone + 3 sweetslime + cave frogspawn bottle, empty bucket returns, Cave frog source). "&bWater Froglight&r" in the turn-in line vs "&9Water Froglight&r" earlier is a harmless color shift, not an error. No edit needed.

### Lava (quest.3E1700000000000B)
- Disposition: CLEAN
- Note: All claims verified (1000 mB lava, lava-bucket slime craft, Tier 1 loop, the lava bucket comes from the Tier 0 cobble crucible). Color codes balanced. No edit needed.

### The Casting Mold (quest.3E1700000000000E)
- Disposition: CLEAN
- Note: Mold casts molten metal -> ingots (90 mB/ingot for iron); bucket-pour / pipe / three-block auto-tower all match the block entity + casting_tower.png. Image reference valid. Codes balanced. No edit needed.

### The Tower (quest.3E17000000000011)
- Disposition: CLEAN
- Note: "Ore doubling" claim verified - iron Froglight melts to 180 mB, mold consumes 90 mB/ingot = 2 ingots, vs 1 ingot from smelting the same Froglight. Task is a checkmark ("Tick when your tower casts its first doubled ingot") matching chapter task type `checkmark`. No edit needed.

## Chapter summary
- Quests: 6 total, 2 EDIT, 4 CLEAN
- Accuracy bugs (WRONG ledger rows): 1
  - Feed the Fire: heat ladder ordering wrong - text orders "fire -> lava" but lava (heat 3) is cooler than fire (heat 5); correct order torch(1) -> campfire(2) -> lava(3) -> fire(5).
- Highest-severity finding: the Feed the Fire heat-ladder ordering error - a new player following the stated ladder would think lava is the top tier when fire (and the Froglights) sit above it. Factual fix, low blast radius, fixed in the AFTER above.
