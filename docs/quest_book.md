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
| `metallic_mastery.snbt`   | Metallic Mastery       | Tier 1 — iron/copper/gold via Metallic Frog            |
| `mineral_veins.snbt`      | Mineral Veins          | Tier 2 — redstone/lapis/coal via Mineral Frog          |
| `gem_workshop.snbt`       | The Gem Workshop       | Tier 3 — diamond/emerald via Gem Frog                  |
| `drowned_riches.snbt`     | Drowned Riches         | Tier 4 — prismarine/aquatic resources via Aquatic Frog |
| `heat_and_flame.snbt`     | Heat & Flame           | Tier 5 — nether resources via Infernal Frog            |
| `arcane_mastery.snbt`     | Arcane Mastery         | Tier 6 — ender/draconic via Arcane Frog                |

### Bootstrap & framing chapters (3)

| Chapter file              | Title                  | Covers                                                |
|---------------------------|------------------------|--------------------------------------------------------|
| `welcome.snbt`            | Welcome to Sky Frogs   | First-launch quest unlocking the rest                  |
| `getting_started.snbt`    | Getting Started        | Tier 0 — Ex Deorum bootstrap, first water/dirt/wood    |
| `productive_frogs.snbt`   | Productive Frogs       | Core mod teaching — bottling, priming, hatching, feeding (no tier gate, runs alongside Metallic Mastery) |

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

## Quest density per chapter

Aim for **~30-40 quests per chapter** on average (22 × 35 ≈ 770). Distribution skews:

| Chapter group          | Average quests | Rationale                                             |
|------------------------|---------------:|--------------------------------------------------------|
| Welcome                |             5 | Onboarding only — tutorial steps                       |
| Getting Started        |            20 | Bootstrap loop with optional side quests               |
| Tier 1-6 (6 chapters)  | 50 each = 300 | Densest — these are the spine. Per-resource subquests. |
| Productive Frogs       |            30 | Mechanics teaching with explicit per-feature quests    |
| Tech mods (9 chapters) | 40 each = 360 | Each teaches the mod from zero                         |
| Dimensions (2)         | 20 each = 40  | Dimension-specific tasks                               |
| Side / endgame (4)     | 25 each = 100 | Various                                                |

This is ~855 total which gives us 15% headroom for cutting. Target ship is ~750.

## Quest dependency graph

High-level (chapter-to-chapter dependencies):

```
welcome
   ↓
getting_started ─────┐
   ↓                 ↓
metallic_mastery     productive_frogs
   ↓
mineral_veins ───────┐
   ↓                 ↓
gem_workshop         mekanism (unlocks at any Tier 2+)
   ↓                 ↓
drowned_riches       applied_energistics (Tier 3+)
   ↓
heat_and_flame ──→ we_need_to_go_deeper
   ↓                 ↓
arcane_mastery ──→ the_end
   ↓
master_pond
```

Tech mod chapters unlock progressively as the player accumulates the resources to engage with them. `mekanism.snbt` is unlockable at any Tier 2+, `applied_energistics.snbt` at Tier 3+, etc. — this avoids the "unlock everything at once" feeling.

## Within-chapter dependency style

Mirror Sky Bees Reborn's `master_hive.snbt` structure: a central spine of mandatory quests for the chapter, with optional branches for resource variants. Sample for `metallic_mastery.snbt`:

```
[breed first frog] ─→ [hatch metallic egg] ─→ [first iron froglight]
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
