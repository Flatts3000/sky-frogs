# Audit: terrarium ("The Terrarium")

Mod(s) referenced: Productive Frogs (productivefrogs-1.20.0.jar). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| The Terrarium | Controller recipe needs quartz, glowstone, blaze rods, magma cream, nether brick | recipe `terrarium_controller.json`: GQG/BCB/NNN = glowstone, quartz_block, blaze_rod, magma_cream, nether_bricks | MATCHES |
| Terrarium Controller | Controller takes Slime Milk piped/clicked into its outward face, rations to ceiling Sprinklers | `TerrariumControllerBlockEntity` (MilkCharge.fromBucket, sprinkler top-up), JEI `terrarium_controller.info` | MATCHES |
| Terrarium Controller | Does NOT accept boss Slime Milk (wither/dragon trophies stay on catalyst altars) | `TerrariumControllerBlockEntity.requiresCatalystAltar -> SlimeMilkSourceBlock.variantRequiresCatalyst`; boss variants (wither_skeleton_skull/nether_star/dragon_egg/dragon_breath) require an altar, so the controller refuses them | MATCHES |
| Terrarium Controller | Recipe: glowstone, a quartz block, blaze rods, magma cream, nether bricks | recipe `terrarium_controller.json` (Q = `quartz_block`) | MATCHES |
| Terrarium Controller | Build it first, structure forms around it; takes one wall block on a flat face, facing OUT | validator: controller is the origin block; `machine_on_edge` rejects corner/edge; controller faces out of cavity | MATCHES |
| Terrarium Controller | Walls can be any solid block | validator `TERRARIUM_SHELL` tag + `not_solid` message; JEI "any solid blocks" | MATCHES |
| Sprinklers | Sprinklers form the ceiling and rain slimes on the same rules as a placed Slime Milk source (cadence, per-bucket budget, catalysts) | JEI `sprinkler.info` "rains that variant's slimes ... on the exact placed-source schedule - catalysts and all" | MATCHES |
| Sprinklers | At least one needed; up to 25 fit a ceiling | JEI `sprinkler.info` "Sits in the Terrarium ceiling (up to 25)"; cap 25 (5x5 ceiling) | MATCHES |
| Sprinklers | Drop a catalyst on a Sprinkler from above to upgrade in place | catalyst-on-source application carries through Sprinkler (same source rules); JEI confirms catalysts carry | MATCHES |
| Sprinklers | Right-click a Sprinkler with an empty bucket to pull its Slime Milk back | `SprinklerBlock` use -> `SprinklerBlockEntity.drainToBucket`, BUCKET_FILL sound; JEI "Right-click with an empty bucket to drain it back out" | MATCHES |
| Sprinklers | Catalysts named "Speed, Quantity, Count, Endless" | PF item names: Rapid/Teeming/Bountiful/Endless; pack's own Geode chapter calls them Count/Speed/Quantity/**Infinite Count** Catalyst | MATCHES (effect names) but inconsistent with pack's "Infinite Count Catalyst" - see findings VERIFY: VERIFIED - PF lang confirms `count_catalyst`="Bountiful", `speed_catalyst`="Rapid", `quantity_catalyst`="Teeming", `infinite_catalyst`="Endless Catalyst". So "Endless" is PF's real item name (NOT factually wrong); the edit to "Infinite Count" is a pack-consistency choice, correctly classed as a low-severity terminology nit, not an accuracy bug. |
| Incubators | Incubators raise frogspawn/tadpoles into frogs inside the box, stats intact | JEI `incubator.info` "matures and releases the frog into the cavity with its stats intact" | MATCHES |
| Incubators | Frogs bred in the cavity lay back into an Incubator (not water) | JEI `incubator.info` "Frogs bred inside a formed Terrarium lay into the nearest Incubator instead of seeking water" | MATCHES |
| Incubators | A Sweetslime right-clicked in speeds incubation | recipe uses Sweetslime; GUI `incubator.sweetslime_hint` "Right-click with a Sweetslime to speed up" | MATCHES |
| Incubators | One Incubator raises one frog at a time; stops releasing at frog cap (8 by default) | JEI "At the frog cap it holds the matured frog until there's room"; config `[terrarium] frogCap = 8` (pack does not override) | MATCHES |
| Incubators | Incubators are optional - the box forms with none | `TerrariumValidator.validate` references INCUBATOR block as a valid machine but never emits `no_incubator`; the `no_incubator` lang string is dead/leftover. JEI `terrarium_controller.info` "Add Incubators (optional)" | MATCHES (1.20.0 - incubators optional) |
| The Hatch | Froglights drop straight into the Hatch, no item entity | JEI `hatch.info` "every Froglight a frog produces drops straight into this 18-slot inventory - no item entities" | MATCHES |
| The Hatch | Hatch also vacuums loose slimeballs, magma cream, raw frog legs | tag `hatch_collectible.json` = slime_ball, magma_cream, froglights, `productivefrogs:raw_frog_legs` (item name "Raw Frog Legs") | MATCHES |
| The Hatch | Opens as a chest, pipes out its outward face | Hatch has 18-slot inventory + menu; recipe is chest-based; JEI "Pipe them out, or right-click to open it" | MATCHES |
| The Hatch | When full, frogs stop eating until cleared (nothing voided) | JEI `hatch.info` "When it's full the frogs stop eating until you clear space" | MATCHES |
| The Hatch | Exactly one Hatch, on a wall facing IN | validator emits `no_hatch` / `multiple_hatches`; machine must face into cavity | MATCHES |
| Seal the Box | Interior is 5 wide, 5 deep, 4 tall | `TerrariumValidator`: FOOTPRINT=5 (X/Z), HEIGHT=4 (sizeOf(Y)=iconst_4). **Executable truth = 5x5x4.** NB: PF's own JEI/config strings say "5x5x5" - that is a stale PF lang bug; the chapter's 5x5x4 is correct | MATCHES (chapter right, PF JEI wrong) |
| Seal the Box | Right-click Controller -> tells formed state, points at first wrong block until "formed" | `TerrariumControllerBlock` use shows validation; lang `terrarium.formed` / `problem_at` / per-problem messages | MATCHES |
| Prime the Sprinklers | Controller buffers one variant at a time and feeds Sprinklers; pipe/pour Slime Milk into outward face | `TerrariumControllerBlockEntity` single-variant buffer (TankVariant tag), MilkCharge; GUI `controller.buffer` | MATCHES |
| Stock the Incubators | Load frogspawn/tadpoles into an Incubator, or lead/net a frog in if Incubators skipped; any species works | JEI incubator + "lead caught frogs in yourself"; froglight is per-variant of the frog inside | MATCHES |
| Hands Off | Milk in one wall, Froglights out another, automated loop | composite of above | MATCHES |

## Per-quest findings

### The Terrarium (quest.53A0000000000002)
- Disposition: CLEAN
- Recipe shopping-list (quartz/glowstone/blaze rods/magma cream/nether brick) matches the Controller recipe; prose is accurate and well-paced. No changes.

### Terrarium Controller (quest.53A0000000000005)
- Disposition: CLEAN
- Boss-milk rejection, outward-facing placement, any-solid walls, and the recipe all ground-truth as correct. Dense but each clause earns its place (the boss-milk caveat prevents a real player trap). No changes.

### Sprinklers (quest.53A0000000000008)
- Disposition: EDIT
- Terminology/consistency: The catalyst list ends with "Endless," but the pack's own Geode catalyst chapter (quest.6E0DE0000000001A and the "Infinite Count Catalyst" capstone) names this catalyst **Infinite Count Catalyst** throughout. PF's raw item name is "Endless Catalyst," so "Endless" is not wrong, but it's inconsistent with how every other Sky Frogs quest refers to it. Align to the pack's established term to avoid a player thinking they're two different items. (Low severity - single word.)
- BEFORE:
  `	"&eSprinklers&r make up the ceiling of the box and rain slimes down into it, spawning on the exact same rules a placed Slime Milk source uses - cadence, per-bucket budget, and &dcatalysts&r (Speed, Quantity, Count, Endless) all carry through from the milk. You need &eat least one&r; up to 25 fit a ceiling, so make as many as you want for faster rain."`
- AFTER:
  `	"&eSprinklers&r make up the ceiling of the box and rain slimes down into it, spawning on the exact same rules a placed Slime Milk source uses - cadence, per-bucket budget, and &dcatalysts&r (Speed, Quantity, Count, Infinite Count) all carry through from the milk. You need &eat least one&r; up to 25 fit a ceiling, so make as many as you want for faster rain."`

### Incubators (quest.53A000000000000B)
- Disposition: CLEAN
- Frog cap (8), optional-forms-with-none, Sweetslime speed-up, lay-into-Incubator breeding, and "release ceiling not a wall on the cavity" all verified accurate against the jar/config. Three paragraphs is long, but the content is all load-bearing (the cap nuance and the optional note both prevent confusion). No changes.

### The Hatch (quest.53A000000000000E)
- Disposition: CLEAN
- Collection list (slimeballs, magma cream, raw frog legs) matches the `hatch_collectible` tag exactly; "no item entity," chest-open, pipe-out, and fill-pause-nothing-voided all verified. No changes.

### Seal the Box (quest.53A0000000000011)
- Disposition: CLEAN
- Interior 5x5x4 is the executable truth from the validator (PF's own JEI string says 5x5x5 and is wrong - the chapter is correct). Controller-readout-as-blueprint flow matches. No changes.
- Note for orchestrator: do NOT "correct" this to 5x5x5 to match PF's JEI; the validator (HEIGHT=4) is authoritative.

### Prime the Sprinklers (quest.53A0000000000014)
- Disposition: CLEAN
- Single-variant buffer + pipe-or-pour into outward face verified. Concise. No changes.

### Stock the Incubators (quest.53A0000000000017)
- Disposition: CLEAN
- Title says "Stock the Incubators" but the body correctly handles the no-Incubator path (lead/net a frog in). Task is a checkmark for "a frog is living in the Terrarium," which the body matches. Any-species claim is correct. No changes.

### Hands Off (quest.53A000000000001A)
- Disposition: CLEAN
- Pure flavor capstone, accurate to the built loop. No changes.

## Chapter summary
- Quests: 9 total, 1 EDIT, 8 CLEAN
- Accuracy bugs (WRONG ledger rows): 0 - every mechanic claim ground-truthed as MATCHES against productivefrogs-1.20.0.jar. The chapter is unusually accurate.

VERIFY PASS (adversarial re-check): CONFIRMED 0 accuracy bugs. Spot-checked the catalyst-name nit (PF `infinite_catalyst` does display as "Endless Catalyst" - the edit is consistency, not a factual fix) and the 5x5x4 vs PF-JEI-5x5x5 note (left to the orchestrator's authoritative-validator ruling; not an audit-text error). No false positives.
- Highest-severity finding: the single EDIT (quest 008) is a terminology-consistency nit - the catalyst is called "Endless" here but "Infinite Count Catalyst" in the Geode catalyst chapter; align to the pack's established name. No factual errors, no formatting/punctuation issues, no em/en dashes.
- Cross-checks worth flagging to the orchestrator: (1) the Terrarium interior is 5x5x4 per the validator - PF's own JEI and config comment string say "5x5x5" and are stale; the chapter is right, leave it. (2) PF ships a dead `no_incubator` lang string but the 1.20.0 validator never enforces it, so the chapter's "Incubators are optional" is correct.
