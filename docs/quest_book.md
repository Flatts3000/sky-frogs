# Quest Book

> **Status:** All six tiers (Welcome, Cave, Geode, Bog, Tide, Infernal, Void) are built and live, through the Master Pond endgame and the Sky Frogs Master Frog trophy. The optional per-mod tech side chapters below remain future work. The questbook's shape is the **chapter-sizing principle** (theme + arc, ~8-20 nodes per chapter, see below), not the old 22-chapter / 750-quest SBR scale reference, which is superseded.

The FTB Quests structure for Sky Frogs. The questbook is organized per-tier (one chapter group per frog species, plus per-tier "Road to" gateway chapters), with the [chapter-sizing principle](#chapter-sizing-settled-2026-05-27) setting chapter boundaries.

## Reference structure

Sky Bees Reborn's questbook lives at [`../sky-bees-reborn-reference/extracted/config/ftbquests/quests/chapters/`](../../sky-bees-reborn-reference/extracted/config/ftbquests/quests/chapters/) and has 22 chapter files:

```
apophic_spawners.snbt
apothic_enchanting.snbt
applied_energistics.snbt
challenges.snbt
creative.snbt
ender_io.snbt
flux_networks.snbt
getting_started.snbt
hostile_neural_networks.snbt
immersive_engineering.snbt
industrial_foregoing.snbt
iron_furnaces.snbt
master_hive.snbt
mekanism.snbt
mob_slayer.snbt
powah.snbt
productive_bees.snbt
storage.snbt
the_end.snbt
useful_mods.snbt
we_need_to_go_deeper.snbt
welcome.snbt
```

Sky Frogs does **not** mirror this organization. SBR is mod-sprawled (one chapter per tech mod); Sky Frogs is frog-spined (one chapter group per tier, with tech mods folded into the tier whose verb they supply). SBR is a study object for FTB Quests mechanics, not a structural template.

## Sky Frogs chapter list

### Built chapters (Tiers 0-5)

These are the 25 chapter files that exist in `config/ftbquests/quests/chapters/`. They sit under seven chapter groups (`chapter_groups.snbt`): "Tier 1: Cave" through "Tier 6: Void", plus "Completionist" (the census shelf after the campaign); Welcome stays ungrouped at the top. Note the **"Road to <tier>" gateway-chapter pattern**: each later tier opens with a short gateway chapter that crafts the next species' frogspawn (Spawnery + primer) and runs the seed-chain bridge, before the species' own chapter.

| Tier group | Chapter file                  | Covers                                                |
|------------|-------------------------------|--------------------------------------------------------|
| Tier 0     | `welcome.snbt`                | Bootstrap: cobble gen, second water source via Ex Deorum barrel, dark-room **cave_slime** farm, slime collection. Final reward: a Bottle of **Cave** Frog Frogspawn. Includes a **cooldown-repeatable "Replacement Frog egg" emergency quest** for when frogs die / jump off the island, and **Join the Pond** (#111): a dependency-free Discord-invite quest with a clickable badge image. |
| Tier 1: Cave | `your_first_iron_ingot.snbt` | The tutorial tier: place frogspawn, breed, infuse, feed, smelt -> first iron ingot. (The deliberate `iron_ingot` froglight-check exception, see below.) |
| Tier 1: Cave | `scaling_the_colony.snbt`    | Scale the Cave loop: breeding via Sweetslime, frog stats, Slime Milker, the iron -> copper -> gold -> coal -> glow_ink_sac -> redstone resource chain. |
| Tier 1: Cave | `cave_frogs.snbt`            | The Cave species' resource quests + the Geode-gateway capstone (lean by design; modded Cave metals live in their tech chapters - osmium/steel in `mekanism.snbt`, Powah's uraninite + energized steel in `powered_up.snbt`). |
| Tier 1: Cave | `melting_point.snbt`         | The **Froglight Crucible + Casting Mold** questline (#123), between Cave Frogs and Storage & Crafting: build the basin (iron + hammer-chain bricks), the heat ladder, the Water and Lava froglight quests (fluid-bucket slime crafts), the Mold, and The Tower ore-doubling capstone. |
| Tier 1: Cave | `storage_and_crafting.snbt`  | The Cave-tier **new verb**: crafting upgrades / storage (Sophisticated + Functional storage, quartz-free networks). |
| Tier 2: Geode | `road_to_geode.snbt`        | Gateway: prime the Spawnery with **redstone** for Geode frogspawn, run the lapis seed-chain bridge. |
| Tier 2: Geode | `geode_frogs.snbt`          | The Geode species: lapis -> tuff -> calcite -> amethyst -> emerald -> diamond, plus a **Slime Milk catalyst** branch off the diamond capstone (Count -> Speed -> Quantity -> Infinite Count; PF v1.7.0). |
| Tier 2: Geode | `mekanism.snbt`             | The Geode-tier **new verb**: automation (Mekanism power, Metallurgic Infuser, Enrichment Chamber). Steel quest keeps the `ingot_steel` check; the optional steel-slime quest carries the froglight check. |
| Tier 3: Bog | `road_to_bog.snbt`           | Gateway: prime the Spawnery with **enriched diamond** (a Mekanism craft) for Bog frogspawn, run the diamond -> dirt seed-chain bridge. |
| Tier 3: Bog | `bog_frogs.snbt`             | The Bog species: dirt -> mud -> clay_ball -> moss -> mycelium -> lily_pad -> leather -> feather -> plastic -> pink_slime (plastic hard-gated behind its frog, pink_slime capstone). |
| Tier 3: Bog | `tools_and_things.snbt` | The Bog-tier **new verb**: **Just Dire Things' natural tier-1 progression** plus a Building Gadgets 2 side branch. Spine: Primogel Goo Block (intro; mycelium-gated) -> Ferricore Ingot -> Fluid Collector -> Fluid Placer -> Item Collector (hexagon capstone). Optionals: Exchanging Gadget -> Copy/Paste Gadget (BG side). Mekanism RF from Geode powers the JDT machines. |
| Tier 4: Tide | `powered_up.snbt`            | The **power-scaling arc** (#109): Powah from Furnator to Starter Reactor + the Flux Networks crossover, rooted at the Dissolution Chamber quest - the chapter's variant loop runs through the chamber, so it lives where the chamber does. Froglight-check quests for all 8 modded variants; teaches the make-it-first chamber law and split-discovery. |
| Tier 4: Tide | `road_to_tide.snbt` | Tier 4 gateway. First the Industrial Foregoing spine that ends Bog: Pity Machine Frame -> Fluid Extractor -> **Dissolution Chamber** (hexagon, "The Slime Engine") - the **pack's slime engine** (resource-threaded chamber rows for Cave/Geode/Bog/Tide in `kubejs/server_scripts/dissolution_slime_recipes.js`; iron bootstraps off bone meal). Then the **Bog -> Tide bridge** as two paths off the Bog gate that converge: a **machine path** (Pity Machine Frame -> Fluid Extractor -> Dissolution Chamber) and a **frog path** (Tide Frogspawn, Spawnery primed with pink_slime), meeting at **A Bucket of Prismarine Slime** (made in the chamber), then a single tail: Milk It -> **First Prismarine** (hexagon capstone). Both paths gate on the bog_frogs pink_slime capstone. **Tide onward is chamber-only** (no crafting-table chain). |
| Tier 4: Tide | `drowned_riches.snbt` | The Tide species chapter: the rest of the aquatic roster, all chamber-made - prismarine_crystals -> sponge -> ink_sac -> sea_pickle -> nautilus_shell (hexagon capstone). Each quest checks that variant's Froglight (`match_components: strict`). Gates off the road_to_tide First Prismarine capstone. |
| Tier 4: Tide | `take_flight.snbt` | The Tide **new verb**: **jetpacks (mobility)** via Iron Jetpacks. Spine: Leather Strap -> Basic Coil -> first jetpack (hexagon) -> Fuel and Fly (charge with Geode RF) -> Advanced Coil -> Elite Coil -> Ultimate Coil (hexagon capstone). Coils tier on frog-farmed resources (iron -> gold -> diamond -> emerald); no recipe override needed. Side branch off the first jetpack (#127): **The Heavy Core** (chamber-pressed, `heavy_core_recipe.js`) -> **Drop the Hammer** (the Mace - fall-height weapon in the flight tier, on purpose). |
| Tier 5: Infernal | `road_to_infernal.snbt` | Tier 5 gateway - **the one real Nether expedition.** A Portal to the Nether (granted obsidian + flint) -> Into the Nether (dimension task) -> Raid a Fortress (mine nether brick - the only thing the void Nether yields, enabled by `structures.json5`) -> Infernal Frogspawn (prime the Spawnery with **nether brick**) -> A Bucket of Netherrack Slime (chamber, prismarine filler) -> Milk It -> **First Netherrack** (hexagon capstone). The Tide jetpack is what makes the void-Nether crossing feasible. |
| Tier 5: Infernal | `infernal_frogs.snbt` | The Infernal species: obsidian -> quartz -> glowstone -> soul_sand -> soul_soil -> blaze -> **netherite_scrap** (hexagon capstone, the vanilla endgame). All chamber-made Froglight checks (`match_components: strict`). Gates off the road_to_infernal First Netherrack capstone. |
| Tier 5: Infernal | `the_network.snbt` | The Infernal **new verb**: **Refined Storage** (RS 2.0). Spine: Quartz Enriched Iron (the quartz gate) -> Controller -> Grid -> Disk Drive + disk -> Cable -> External Storage -> Importer/Exporter -> Crafting Grid -> **Autocrafting** (Pattern Grid + Autocrafter, hexagon capstone). Gated on nether quartz, which only the Infernal frog produces. |

### Tier 6 (Void) chapters - BUILT

Void follows the same per-tier shape (a "Road to" gateway + a species chapter + that tier's new-verb chapter), plus a dedicated endgame chapter:

| Chapter             | File | Covers                                                |
|---------------------|------|--------------------------------------------------------|
| Road to the Void    | `road_to_void.snbt` | The **dragon expedition** gateway: ender pearls (dark-room endermen) -> 2 eyes -> bake the **End Cake** (milk/Slime Milk + egg + wheat + the eyes; each slice teleports to the End, since no stronghold generates) -> Into the End -> **Slay the Dragon** -> the frog sub-chain (frogspawn -> slime -> milk -> First Ender Pearl). |
| Void Frogs          | `void_frogs.snbt` | The End resource chain: end_stone -> chorus_fruit -> echo_shard -> sculk -> **shulker_shell** Froglight checks. |
| The Ultimate Table  | `the_ultimate_table.snbt` | The Void **new verb**: **Extended Crafting**. Black iron -> luminessence -> basic/advanced/elite/**ultimate** crafting tables -> the **Quantum Compressor**. |
| Master Pond         | `master_pond.snbt` | The endgame: froglight Singularities (one per species, a proof-of-automation gate) -> the **Ultimate Singularity** -> the **Sky Frogs Master Frog** trophy + a closing epilogue. |
| Completionist | `whole_pond.snbt`            | **The Whole Pond** (#121, generated by `tools/gen_completionist_chapters.py`): the vanilla census - one froglight quest per vanilla variant (50 today), laid out as a top-down tree frog (head = Cave, body = Bog, four limbs = the other tiers, toes and all), capped by a lily-pad checkmark depending on every one. Deterministic sha-derived ids survive regeneration. |
| Completionist | `sister_ponds.snbt`          | **Sister Ponds** (#121, same generator): the modded census - one column per loaded mod (ATO, Powah, RS, Mekanism, IF, Flux Networks; 25 quests today), same capstone pattern. Re-run the generator on every PF pin bump. |

## Chapter sizing (settled 2026-05-27)

The chapter boundary is set by **theme + arc, not node count**: a chapter is *one thing the player holds in their head* and *one completion milestone*. Node count is an output of that, not the dial.

- **Target ~8-20 nodes per chapter.** Below ~5 it's a section, not a chapter (the completion milestone means nothing, and cross-chapter dependency plumbing piles up). Above ~25 the node map tangles and the player goes too long with no payoff.
- **One chapter per progression beat** - a tier, a major system, or a dimension. Split when a chapter is trying to be two things; merge when one can't stand on its own as a milestone.
- **Use chapter groups** (`chapter_groups.snbt`) to organize the sidebar (Tiers / Systems / Tech / Dimensions), so "more, focused chapters" doesn't bloat navigation.

This supersedes the SBR-scale ~30-40/chapter target below. Sky Frogs is frog-spined, not mod-sprawled, so it runs fewer, denser, theme-driven chapters than SBR's 22/750. Shipped chapters so far: Welcome (22, top of range), Your First Iron Ingot (7), Scaling the Colony (11), Cave Frogs (6, including the Geode-gateway capstone - kept lean by design; modded Cave metals live in their tech-mod chapters rather than padding this one), and Storage and Crafting (10, the Tier 1 storage interlude). These four progression chapters sit under a "Tier 1: Cave" chapter group; Welcome stays ungrouped at the top.

## Quest density per chapter (SBR-scale reference - SUPERSEDED, historical only)

> Superseded by the chapter-sizing principle above. The ~22-chapter / ~750-quest target was an SBR-scale guess from before the pack found its frog-spined shape; the built tiers run fewer, denser chapters (Welcome 22, Your First Iron Ingot 7, Scaling the Colony 11, Cave Frogs 6, Storage and Crafting 10). Kept below for context, not as a target.

Aim for **~30-40 quests per chapter** on average (22 × 35 ≈ 770). Distribution skews:

| Chapter group          | Average quests | Rationale                                             |
|------------------------|---------------:|--------------------------------------------------------|
| Welcome                |            18 | Tier 0 bootstrap: spawn, cobble gen, water source, mob farm, slime collection, first frogspawn reward, emergency replacement quest. |
| Tier 1-6 (6 chapters)  | 50 each = 300 | Densest — these are the spine. Per-resource subquests. |
| Productive Frogs       |            30 | Mechanics teaching with explicit per-feature quests    |
| Tech mods (9 chapters) | 40 each = 360 | Each teaches the mod from zero                         |
| Dimensions (2)         | 20 each = 40  | Dimension-specific tasks                               |
| Side / endgame (4)     | 25 each = 100 | Various                                                |

This is ~855 total which gives us 15% headroom for cutting. Target ship is ~750.

## Quest dependency graph

High-level (chapter-to-chapter dependencies). All chapters built:

```
welcome
   |
your_first_iron_ingot
   |
scaling_the_colony
   |
cave_frogs ----------------+
   |                       |
storage_and_crafting       | (Cave new verb: storage)
   |
road_to_geode  (prime Spawnery w/ redstone)
   |
geode_frogs ---------------+
   |                       |
mekanism                   | (Geode new verb: automation)
   |
road_to_bog    (prime Spawnery w/ enriched diamond)
   |
bog_frogs ------------------+
   |                        |
tools_and_things            | (Bog new verb: JDT tier-1 progression + BG side branch)
   |
road_to_tide   (IF spine: Pity Frame -> Fluid Extractor -> Dissolution Chamber capstone)
   |
drowned_riches ------------+
   |                       |
take_flight                | (Tide new verb: Iron Jetpacks mobility)
   |
road_to_infernal  (Nether expedition: portal -> fortress -> nether brick)
   |
infernal_frogs ------------+
   |                       |
the_network                | (Infernal new verb: Refined Storage)
   |
road_to_void   (End expedition: eyes -> End Cake -> slay the dragon)
   |                       |
void_frogs                 |
   |                       |
the_ultimate_table         | (Void new verb: Extended Crafting)
   |
master_pond    (froglight Singularities -> Ultimate Singularity -> Master Frog trophy)
```

The "Road to <tier>" gateway chapters are where the tier transition fires (Spawnery primer / expedition + seed-chain bridge). Each tier's new-verb chapter branches off its species chapter; `master_pond` depends on both the dragon kill and the Extended Crafting Quantum Compressor.

## Within-chapter dependency style

A central spine of mandatory quests for the chapter, with optional branches for resource variants. Sample for the Cave tier (`cave_frogs.snbt` + its lead-ins):

```
[breed first Cave frog] -> [hatch Cave egg] -> [first iron froglight]
                                                 |
                          +----------------------+----------------------+
                          |                      |                      |
                  [iron variant complete] [copper variant]       [gold variant]
                                                 |                      |
                                          [coal variant]        [redstone variant]
```

Resource quests check the variant **Froglight** the frog drops (the froglight-check principle), not the smelted resource. The "spine" mandatory quests gate the Geode unlock. Optional variant quests grant bonus rewards (slime spawn eggs for modded Cave metals, XP bottles, etc.).

## Quest rewards

Standardized reward tiers (mirror SBR pattern):

| Tier label   | Used for                           | Contents                                        |
|--------------|------------------------------------|--------------------------------------------------|
| Trivial      | Onboarding quests                  | A few items, small XP                            |
| Standard     | Spine quests                       | 1 loot bag (random useful stack), 10-30 XP       |
| Notable      | Tier-completion quests             | 1 loot bag + 1 named reward (e.g., spawn egg)    |
| Milestone    | Chapter-completion / Tier-unlock   | Multiple loot bags + tier-specific tool / hint   |
| Legendary    | Endgame creative trophy            | Custom Sky Frogs Master Frog trophy item         |

## The Welcome chapter (Tier 0 detail)

Drafted quest spine for the `welcome.snbt` chapter — the only mandatory Tier 0 content:

1. **Plant a sapling** — sapling from first-join grant placed on dirt.
2. **Harvest wood + craft a wooden axe + pickaxe.**
3. **Place your water source** — bucket the water onto the platform.
4. **Place your lava source adjacent to water → first cobblestone.** Player understands the vanilla cobble generator.
5. **Set up an Ex Deorum barrel outside your claim.** (Tooltip: Rain Shield is not in this pack — your claim does get rain inside, but the barrel works anywhere.)
6. **Wait for rain → bucket the second water source.** Now infinite water.
7. **Mine 64 cobblestone.** Scaling material.
8. **Build a dark room** — minimum 5×5×3 enclosed space at light level 0.
9. **Kill 8 cave slimes.** `productivefrogs:cave_slime` spawns in the dark room because the pack adds `cave_slime` to the (forced) island biome and PF's light-based placement rule does the rest. Reward: a few slimeballs (in case loot RNG was unkind).
10. **Collect 16 slimeballs total.** Resource bar for frog breeding + crafting.
11. **(Optional spine branch)** — split-discover a resource slime. Tooltip hint: keep farming, it's random.
12. **(Final)** Complete the chapter → **reward: a Bottle of Cave Frog Frogspawn**. Now Tier 1 (Cave) is unlocked.

**Repeatable emergency quest** (always visible in the Welcome chapter):

- **"My frogs are gone"** — visible from the moment the chapter opens; completable at any time.
  - Cooldown: 1 hour real-time (FTB Quests `cooldown` field).
  - Cost: 4 slimeballs (so the player has to keep the farm running to use it; prevents infinite frog cheese).
  - Reward: a Bottle of Cave Frog Frogspawn.
  - Quest description text: "Frogs jump. Frogs occasionally jump off your island. Frogs occasionally drown. This quest gets you back on your feet. Please consider building a fence around your enclosure."

The intent is that a player who somehow loses every single frog AND has no frogspawn in inventory can recover, but it's friction-laden enough that the player will build a fence after the first use.

## Special: the "Master Pond" chapter

Sky Bees Reborn's `master_hive.snbt` chapter is the singularity-grinding endgame. Sky Frogs' equivalent — *Master Pond* — chains the player from "I have all six tiers running" to "I have an Ultimate Singularity" to "I have crafted the Sky Frogs Master Frog trophy."

Loosely:

1. Build a Pond shrine — 6 enclosures, one per tier, each producing 1 Froglight/min.
2. Channel into Mekanism Compactors → Singularities (one per resource family).
3. Combine via Extended Crafting → Ultimate Singularity.
4. Craft into **Sky Frogs Master Frog** (custom item, 3D model TBD).
5. Place on display pedestal → quest completion → questbook reveals an epilogue page.

## Resolved: the froglight-check principle

Per-tier resource quests **detect the variant Froglight** (`productivefrogs:configurable_froglight` carrying a `productivefrogs:slime_variant` component), not the smelted resource, so the frog loop can't be bypassed by obtaining the resource another way. This also settles the old quest-icon question: the Froglight is the check target *and* the natural quest icon (it's already category-colored). Two deliberate exceptions keep an ingot check: **Your First Iron Ingot** (the tutorial that teaches the smelt, gated upstream by its "Feed the Frog" quest) checks `iron_ingot`, and the main Mekanism **Steel** quest checks `ingot_steel` (a Mekanism craft, not a frog resource) while the *optional* steel-slime quest carries the froglight check.

## Open quest-book questions
- **Loot bag contents** — do we hand-author or use FTB Quests' weighted reward tables? Hand-authoring scales poorly past ~100 quests; weighted tables are the only viable path. Bake those during quest authoring.
- **Translatable quest text** — FTB Quests supports lang files. Ship en_us only at v1.0; community translations welcomed via PR.
- **Patchouli book vs. FTB Quests opening** — Sky Bees Reborn opens FTB Quests directly on first join. We could also ship a Patchouli "Welcome to Sky Frogs" book as a tutorial layer above the questbook. TBD; defer.
