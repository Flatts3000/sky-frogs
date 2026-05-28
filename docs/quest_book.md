# Quest Book

> **Status:** DRAFT — non-canonical. The 22-chapter / 750-quest target was lifted from Sky Bees Reborn as a scale reference, not as a goal. Sky Frogs' questbook should have its own shape — possibly fewer, denser chapters; possibly a wholly different organizing axis (per-category instead of per-mod). The proposal below is a starting point.

The FTB Quests structure for Sky Frogs. Initial scale reference: ~22 chapters / ~750 quests (mirroring Sky Bees Reborn). Whether that's the right shape for Sky Frogs is an open question.

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

Sky Frogs mirrors this organization closely — six tier chapters drive progression, mod-specific chapters teach individual tech mods, and special chapters cover dimensions and endgame.

## Sky Frogs chapter list (target v1.0)

### Core progression chapters (6)

| Chapter file              | Title                  | Covers                                                |
|---------------------------|------------------------|--------------------------------------------------------|
| `bog_mastery.snbt`        | Bog Mastery            | Tier 1 — iron/copper/gold via Bog Frog                 |
| `cave_veins.snbt`         | Cave Veins             | Tier 2 — redstone/lapis/coal via Cave Frog             |
| `geode_workshop.snbt`     | The Geode Workshop     | Tier 3 — diamond/emerald via Geode Frog                |
| `drowned_riches.snbt`     | Drowned Riches         | Tier 4 — prismarine/Tide resources via Tide Frog       |
| `heat_and_flame.snbt`     | Heat & Flame           | Tier 5 — nether resources via Infernal Frog            |
| `void_mastery.snbt`       | Void Mastery           | Tier 6 — ender/draconic via Void Frog                  |

### Bootstrap & framing chapters (3)

| Chapter file              | Title                  | Covers                                                |
|---------------------------|------------------------|--------------------------------------------------------|
| `welcome.snbt`            | Welcome to Sky Frogs   | Tier 0 — cobble gen, second water source via Ex Deorum barrel, mob farm, slime collection. Final reward: 2× Bog frog egg. Includes a **cooldown-repeatable "Replacement Frog egg" emergency quest** for when frogs die / jump off the island. |
| `getting_started.snbt`    | Getting Started        | (Merged into `welcome.snbt`; chapter removed — Sky Frogs has no separate Ex Deorum bootstrap chapter since sieving is disabled.) |
| `productive_frogs.snbt`   | Productive Frogs       | Core mod teaching — placing frogspawn, breeding, slime infusion, milking, feeding (no tier gate, runs alongside Bog Mastery) |

### Dimension chapters (2)

| Chapter file              | Title                  | Covers                                                |
|---------------------------|------------------------|--------------------------------------------------------|
| `we_need_to_go_deeper.snbt` | We Need To Go Deeper | Nether arrival + basic Nether base (Tier 5 prelude)    |
| `the_end.snbt`            | The End                | End access, dragon fight, outer islands (Tier 6 prelude) |

### Tech mod chapters (~7-9)

One per significant tech mod, mirroring SBR. Each chapter teaches the mod within the Sky Frogs progression — they're optional-but-recommended infrastructure.

| Chapter file                | Title                       | Mod taught                            |
|-----------------------------|-----------------------------|----------------------------------------|
| `mekanism.snbt`             | Mekanism                    | Mekanism                               |
| `applied_energistics.snbt`  | Applied Energistics 2       | AE2 + AE2 ecosystem                    |
| `immersive_engineering.snbt`| Immersive Engineering       | IE                                     |
| `industrial_foregoing.snbt` | Industrial Foregoing        | IF                                     |
| `powah.snbt`                | Powah!                      | Powah                                  |
| `ender_io.snbt`             | Ender IO                    | EnderIO                                |
| `iron_furnaces.snbt`        | Iron Furnaces               | Iron Furnaces (and processing scaling) |
| `flux_networks.snbt`        | Flux Networks               | Wireless power                         |
| `storage.snbt`              | Storage Logistics           | Sophisticated Storage / Drawers / etc. |

### Side / endgame chapters (2-3)

| Chapter file              | Title                  | Covers                                                |
|---------------------------|------------------------|--------------------------------------------------------|
| `mob_slayer.snbt`         | Mob Slayer             | Combat / spawner manipulation (Apothic Spawners + HNN side path) |
| `master_pond.snbt`        | Master Pond            | Endgame singularity loop — Ultimate Singularity, creative trophy |
| `useful_mods.snbt`        | Useful Mods            | Catch-all for the QoL mods (Waystones, Backpacks, etc.) |
| `challenges.snbt`         | Challenges             | Optional self-set challenges (kill the dragon under-tier, etc.) |

**Total: ~22 chapters**, matching Sky Bees Reborn structurally.

## Chapter sizing (settled 2026-05-27)

The chapter boundary is set by **theme + arc, not node count**: a chapter is *one thing the player holds in their head* and *one completion milestone*. Node count is an output of that, not the dial.

- **Target ~8-20 nodes per chapter.** Below ~5 it's a section, not a chapter (the completion milestone means nothing, and cross-chapter dependency plumbing piles up). Above ~25 the node map tangles and the player goes too long with no payoff.
- **One chapter per progression beat** - a tier, a major system, or a dimension. Split when a chapter is trying to be two things; merge when one can't stand on its own as a milestone.
- **Use chapter groups** (`chapter_groups.snbt`) to organize the sidebar (Tiers / Systems / Tech / Dimensions), so "more, focused chapters" doesn't bloat navigation.

This supersedes the SBR-scale ~30-40/chapter target below. Sky Frogs is frog-spined, not mod-sprawled, so it runs fewer, denser, theme-driven chapters than SBR's 22/750. Shipped chapters so far: Welcome (22, top of range), Your First Iron Ingot (7), Scaling the Colony (11), Cave Frogs (6, including the Geode-gateway capstone - kept lean by design; modded Cave metals live in their tech-mod chapters rather than padding this one), and Storage and Crafting (10, the Tier 1 storage interlude). These four progression chapters sit under a "Tier 1: Cave" chapter group; Welcome stays ungrouped at the top.

## Quest density per chapter (SBR-scale reference - superseded by the sizing principle above)

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

High-level (chapter-to-chapter dependencies):

```
welcome ─────────────┐
   ↓                 ↓
bog_mastery          productive_frogs
   ↓
cave_veins ──────────┐
   ↓                 ↓
geode_workshop       mekanism (unlocks at any Tier 2+)
   ↓                 ↓
drowned_riches       applied_energistics (Tier 3+)
   ↓
heat_and_flame ──→ we_need_to_go_deeper
   ↓                 ↓
void_mastery ────→ the_end
   ↓
master_pond
```

Tech mod chapters unlock progressively as the player accumulates the resources to engage with them. `mekanism.snbt` is unlockable at any Tier 2+, `applied_energistics.snbt` at Tier 3+, etc. — this avoids the "unlock everything at once" feeling.

## Within-chapter dependency style

Mirror Sky Bees Reborn's `master_hive.snbt` structure: a central spine of mandatory quests for the chapter, with optional branches for resource variants. Sample for `bog_mastery.snbt`:

```
[breed first frog] ─→ [hatch bog egg] ─→ [first iron froglight]
                                                ↓
                          ┌────────────────────┼────────────────────┐
                          ↓                    ↓                    ↓
                  [iron variant complete] [copper variant]   [gold variant]
                          ↓                    ↓                    ↓
                  ┌───────┴───────┐    [osmium variant]    [aluminum variant]
                  ↓               ↓                                   ↓
            [tin variant]   [zinc variant]                  [nickel variant]
```

The "spine" mandatory quests gate Tier 2 unlock. Optional variant quests grant bonus rewards (slime spawn eggs for tier-1 modded slime species, XP bottles, etc.).

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
9. **Kill 8 bog slimes.** `productivefrogs:bog_slime` spawns in the dark room because the island is forced to the `minecraft:swamp` biome and PF already ships bog_slime spawning there. Reward: a few slimeballs (in case loot RNG was unkind).
10. **Collect 16 slimeballs total.** Resource bar for frog breeding + crafting.
11. **(Optional spine branch)** — split-discover an Iron Slime. Tooltip hint: keep farming, it's random.
12. **(Final)** Complete the chapter → **reward: 2× Bog frog egg**. Now Tier 1 is unlocked.

**Repeatable emergency quest** (always visible in the Welcome chapter):

- **"My frogs are gone"** — visible from the moment the chapter opens; completable at any time.
  - Cooldown: 1 hour real-time (FTB Quests `cooldown` field).
  - Cost: 4 slimeballs (so the player has to keep the farm running to use it; prevents infinite frog cheese).
  - Reward: 2× Bog frog egg.
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

## Open quest-book questions

- **Quest item icons** for the six Resource Frog category quests — do we use the Configurable Froglight (already category-colored) or the Frog entity directly? Probably Froglight for legibility in the chapter sidebar.
- **Loot bag contents** — do we hand-author or use FTB Quests' weighted reward tables? Hand-authoring scales poorly past ~100 quests; weighted tables are the only viable path. Bake those during quest authoring.
- **Translatable quest text** — FTB Quests supports lang files. Ship en_us only at v1.0; community translations welcomed via PR.
- **Patchouli book vs. FTB Quests opening** — Sky Bees Reborn opens FTB Quests directly on first join. We could also ship a Patchouli "Welcome to Sky Frogs" book as a tutorial layer above the questbook. TBD; defer.
