# Audit: road_to_tide ("Road to Tide")

Mod(s) referenced: Industrial Foregoing (Pity Machine Frame, Dissolution Chamber, Latex), Productive Frogs (Crucible, Spawnery, Slime Milker, Froglight, slime variants). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| The Machine Frame | Pity Machine Frame crafts from logs + iron + a block of redstone, no plastic | IF `data/industrialforegoing/recipe/machine_frame_pity.json` (pattern WIW/IRI/WIW; I=`c:ingots/iron`, R=`c:storage_blocks/redstone`, W=`minecraft:logs`) | MATCHES |
| The Machine Frame | The Dissolution Chamber bolts onto the frame | IF dissolution_chamber recipes use machine_frame variants; pack uses the frame as the chamber base | MATCHES |
| A Bucket of Latex | Melt a plastic Froglight in the PF Crucible -> Liquid Latex | PF `data/productivefrogs/recipe/crucible_melt_plastic.json` (`productivefrogs:crucible_melting`, ingredient = `configurable_froglight` w/ `slime_variant: plastic`, result `industrialforegoing:latex` amount 1000) | MATCHES |
| A Bucket of Latex | Latex is the fluid the Dissolution Chamber runs on | `dissolution_slime_recipes.js` line 271/314: `inputFluid: industrialforegoing:latex, amount: 100` | MATCHES |
| A Bucket of Latex | "No Fluid Extractor, no rubber trees - the plastic frog is the source" | PF crucible_melt_plastic is the only pack latex path; IF Tree Fluid Extractor exists but pack routes around it | MATCHES |
| The Slime Engine | Chamber: prior resource + tier filler + sweetslime + latex -> variant Slime in a Bucket | `dissolution_slime_recipes.js` lines 259-281 (1x prior resource, 4x filler, 3x sweetslime, 100mB latex -> slime_bucket stamped Variant+Category) | MATCHES |
| The Slime Engine | Iron threads off bone meal (the exception) | `dissolution_slime_recipes.js` line 44 `['iron','minecraft:bone_meal']` + comment | MATCHES |
| The Slime Engine | Cave/Geode/Bog have hand-craft chains; Tide on is chamber-only | cave/geode/bog_slime_chain.js exist; no tide_slime_chain.js; header comment lines 30-35 | MATCHES |
| The Slime Engine | Frame the chamber with plastic; plastic slime supplies it | IF dissolution_chamber base is the machine_frame; plastic is the Bog plastic variant (PF) | MATCHES (plastic-frame framing is IF-standard) |
| Tide Frogspawn | Feed pink slime to the Spawnery to prime it for Tide | PACK OVERRIDE `kubejs/data/productivefrogs/tags/item/spawnery_primer/tide.json` = `{replace:true, values:["industrialforegoing:pink_slime"]}` (overrides PF default `minecraft:prismarine_shard`) | MATCHES (pack override is authority) |
| Tide Frogspawn | Pour the bottle on water; Tide Frogs hatch | PF parent_species/tide_slime spawns in oceans; frogspawn-on-water is the PF standard hatch | MATCHES |
| Tide Frogspawn | Tide frogs "hungry for sponge, prismarine, and ink" | prismarine/sponge/ink_sac are real Tide variants (chamber rows 86-89); flavor for the resource set | MATCHES (flavor) |
| A Bucket of Prismarine Slime | Chamber: pink slime + mycelium + sweetslime + latex -> Bucket of Prismarine Slime | `dissolution_slime_recipes.js` line 86 `['prismarine','industrialforegoing:pink_slime']`, TIDE filler `minecraft:mycelium` line 85 | MATCHES |
| Milk It | Run Prismarine Slime through a Slime Milker for Prismarine Slime Milk | PF `data/productivefrogs/recipe/slime_milker.json` (crafts the block); Milker converts slime bucket -> milk bucket (`slime_milker.info`); task item `prismarine_slime_milk_bucket` | MATCHES |
| Milk It | Place the milk and prismarine slimes spawn for the Tide Frog to eat | PF slime_milk.info: "Place in the world... periodically spawns a [variant] slime" | MATCHES |
| First Prismarine | Feed a prismarine slime to a Tide Frog -> Prismarine Froglight | standard PF frog loop; task item = `configurable_froglight` w/ `slime_variant: prismarine` | MATCHES |
| First Prismarine | Smelt the Froglight for prismarine shards | PF `configurable_froglight_prismarine_to_prismarine_shard.json` (smelting -> `minecraft:prismarine_shard`) | MATCHES |
| First Prismarine | Crystals, sponge, ink, sea pickle, nautilus wait in Drowned Riches | prismarine_crystals/sponge/ink_sac/sea_pickle/nautilus_shell are real Tide chamber rows (86-98) | MATCHES |

## Per-quest findings

### The Machine Frame (quest.71DE000000000002)
- Disposition: CLEAN
- All claims verified against IF machine_frame_pity.json. Voice is tight, color codes balanced. "humblest" + "bolts onto" register fits the pack.

### A Bucket of Latex (quest.71DE000000000005)
- Disposition: CLEAN
- Crucible melt of a plastic Froglight -> latex confirmed against PF crucible_melt_plastic.json. Terminology correct ("Froglight", "Liquid Latex" matches IF fluid display). Note for verify pass: PF yields a FULL bucket (1000 mB); prose says "a bucket" / "Fill a bucket" - accurate, no count needed.

### The Slime Engine (quest.71DE000000000008)
- Disposition: EDIT
- Issues: Voice/verbose: the middle paragraph restates the full chamber threading law (within-tier vs boundary vs iron-bone-meal exception) at a level of mod-internal detail that belongs in the recipe comments, not player text. A new player at the Tide gate does not need the iron<-bone-meal exception or the "previous tier's last" boundary rule to succeed; JEI shows the exact recipe. The shape and "feed it a prior resource + tier filler + sweetslime + latex" is enough. Trim to keep the engine concept + the chamber-only-from-Tide rule (the one fact that changes what the player does), drop the within/at-boundary/iron taxonomy.
- BEFORE:
  ```
  quest.71DE000000000008.quest_desc: [
  	"Industrial Foregoing's &eDissolution Chamber&r dissolves a pile of items in a fluid and presses out something new. Frame it with &fplastic&r (your &bplastic slime&r already supplies it), feed it the &flatex&r you rendered from a plastic Froglight, and it becomes the pack's &eslime engine&r."
  	""
  	"Every variant in &eCave&r, &eGeode&r, &eBog&r, and &eTide&r has a chamber recipe: feed it a prior resource (within a tier, the previous variant's; at a tier boundary, the previous tier's last) + tier filler + sweetslime + latex, and out comes that variant's &bSlime in a Bucket&r. Iron is the exception - it threads off &fbone meal&r. Cave, Geode, and Bog also have hand-craft chains; from &eTide&r on, the chamber is the only way."
  	""
  	"This chapter is the &eRoad to Tide&r - the bridge that closes out &eBog&r and opens &eTide&r. The engine is online; below, you'll prime your first &bTide Frog&r and pull a &bPrismarine Froglight&r out of the void-sea."
  	""
  	"Claim your reward; the engine is online."
  ]
  ```
- AFTER:
  ```
  quest.71DE000000000008.quest_desc: [
  	"Industrial Foregoing's &eDissolution Chamber&r dissolves a pile of items in a fluid and presses out something new. Frame it with &fplastic&r (your &bplastic slime&r already supplies it), feed it the &flatex&r you rendered from a plastic Froglight, and it becomes the pack's &eslime engine&r."
  	""
  	"Every resource slime - &eCave&r, &eGeode&r, &eBog&r, and now &eTide&r - has a chamber recipe: a prior resource, tier filler, sweetslime, and latex press out that variant's &bSlime in a Bucket&r. Check JEI for any one you need. Cave, Geode, and Bog also have hand-craft chains; from &eTide&r on, the chamber is the only way."
  	""
  	"This chapter is the &eRoad to Tide&r - the bridge that closes out &eBog&r and opens &eTide&r. The engine is online; below, you'll prime your first &bTide Frog&r and pull a &bPrismarine Froglight&r out of the sea."
  	""
  	"Claim your reward; the engine is online."
  ]
  ```
  (Also drops "void-sea" -> "sea": prismarine is ocean stone; "void-sea" is a confusing coinage for a skyblock with no real ocean. "the sea" reads cleaner. Minor.)

### Tide Frogspawn (quest.71DE00000000000E)
- Disposition: CLEAN
- Pink-slime priming VERIFIED against the pack override `spawnery_primer/tide.json` (replace:true -> `industrialforegoing:pink_slime`); the PF jar default (prismarine_shard) is correctly overridden, so the prose is accurate. "Frogspawn" wording is the pack-wide convention (see Chapter summary note), not an error here. Color codes balanced.

### A Bucket of Prismarine Slime (quest.71DE000000000014)
- Disposition: CLEAN
- Chamber inputs (pink slime + mycelium + sweetslime + latex) match `dissolution_slime_recipes.js` TIDE row + filler. "Bucket of Prismarine Slime" matches PF lang exactly. Chamber-only restatement is consistent with quest 08.

### Milk It (quest.71DE000000000017)
- Disposition: CLEAN
- Slime Milker conversion + placed-milk spawning confirmed against PF slime_milker.info / slime_milk.info. Task item `prismarine_slime_milk_bucket` matches "Prismarine Slime Milk". Tight and correct.

### First Prismarine (quest.71DE00000000001A)
- Disposition: CLEAN
- Froglight-from-frog loop + smelt-to-prismarine-shard confirmed (`configurable_froglight_prismarine_to_prismarine_shard.json`). "Prismarine Froglight" / "prismarine shards" correct. The Drowned Riches forward-reference (crystals, sponge, ink, sea pickle, nautilus) all map to real Tide variants. "ocean stone, no monument required" is accurate flavor (prismarine normally needs an ocean monument).

## Chapter summary
- Quests: 7 total, 1 EDIT, 6 CLEAN
- Accuracy bugs (WRONG ledger rows): 0 - every mechanic claim ground-truthed and MATCHES. The one claim that looked wrong on the jar (Tide primer = prismarine_shard) is correctly inverted by the pack override to pink_slime, so the prose is right.

VERIFY PASS (adversarial re-check): CONFIRMED 0 accuracy bugs. Re-verified the highest-risk "override saves it" claim: pack `data/productivefrogs/tags/item/spawnery_primer/tide.json` = `{replace:true, ["industrialforegoing:pink_slime"]}` vs PF jar default `{replace:false, ["minecraft:prismarine_shard"]}`. Override is authority; prose (pink-slime primer) is correct. No false positives to flag; the lone EDIT is verbosity-only.
- Highest-severity finding: quest 08 "The Slime Engine" is verbose - it dumps the full chamber threading taxonomy (within-tier / boundary / iron-bone-meal exception) into player text. Factually correct but over-technical for the voice target; trim to the engine concept + chamber-only-from-Tide rule. No accuracy or terminology defects anywhere in the chapter.
- Pack-wide note (NOT a per-chapter fix): PF 1.20's lang renamed the `frog_egg` item to "Bottle of [Species] Frog Eggs", but every Sky Frogs gateway quest (Cave/Geode/Bog/Infernal/Void + this one) uses "Frogspawn" as the deliberate player-facing term. Quest 0E ("Tide Frogspawn" / "Bottle of Tide Frog Frogspawn") is consistent with that pack convention. If the pack ever decides to track PF's "Frog Eggs" naming, it must be a coordinated pass across all gateway chapters - flagging it in this one chapter alone would break consistency.
