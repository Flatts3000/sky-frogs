# Worldgen

> **Status:** DRAFT — non-canonical. Skyblock Builder is a candidate, not a commitment. Starter island contents, dimension strategy, and parent-species seeding approach are all open. The "void overworld" assumption itself is up for revisiting — a different generator could give Sky Frogs a distinct opening.

How the player's world is generated, what's on the starting island, and how dimension-specific Productive Frogs parent species are seeded without their natural biomes.

## Generator

**Skyblock Builder** (mod ID `skyblockbuilder`) — same generator Sky Bees Reborn uses. Provides:

- A void Overworld with a single configurable starting structure (the island template).
- Per-player island system: each player or team gets their own island.
- An in-game UI to create / leave / invite to islands.
- Spawn-control config to prevent player from accidentally regenerating mid-game.

We ship a custom **island template** as a Skyblock Builder template NBT. See [`repo_layout.md`](./repo_layout.md) for where the template file lives in the packwiz overrides.

## Starting island contents

A 3×3 dirt platform at y=64. No starting blocks beyond the dirt itself.

**First-join inventory grant** (via KubeJS `PlayerEvents.loggedIn` first-join hook, not a chest):

- 2-3× oak sapling (wood bootstrap; multiple in case the first fails to grow)
- 1× water bucket
- 1× lava bucket
- ~16× cooked beef (food economy buffer for the first session)
- (FTB Quests book auto-opened on first join — no inventory slot needed)

The grant is intentionally minimal. The player builds everything else from these primitives:

1. **Cobble generator** — vanilla water + lava (one bucket each, placed adjacent → infinite cobble).
2. **Second water source** — the grant has only 1 water bucket, which is 1 source. Infinite water needs 2 sources adjacent (the standard vanilla pattern). The player gets the second source via **Ex Deorum's rain-collection barrel** — set a barrel outside, wait for rain to fill it, bucket out → second source → vanilla infinite water square. This gives Ex Deorum a load-bearing Tier 0 role beyond just "extras."
3. **Mob farm** — built from the cobble. Vanilla `minecraft:slime` spawns via KubeJS-overridden spawn rule (the Metallic parent per PF's `ParentSpeciesEntry`). Player collects slimeballs and occasionally split-discovers Iron Slimes via PF's `SlimeSplitDiscoveryHandler`.
4. **First Resource Frog** — Welcome quest chapter rewards **2× Metallic Frogspawn** (category-typed, so no priming step needed) at completion. Two for a breeding pair.

The first Iron Configurable Froglight is the first iron source — smelting it gives the first iron ingot. No sieving, no Ex Deorum hammers needed.

Why inventory grant, not a chest: modern skyblock packs put first-join items directly in the player's inventory. Lower friction (no "where do I open this?"), survives the player breaking the chest before taking everything, KubeJS hook guards against re-granting on re-login.

Why minimal grant: the design wants the player engaged with the mob-farm loop within minutes, not hand-feeding a bootstrap inventory through 20 minutes of crafting. Saplings + water + lava + food + the questbook is everything needed to reach a slime farm in ~30 min.

## Dimensions

### Overworld
- **Type:** void
- **Y-range:** standard 1.21.x (`-64` to `319`)
- **Biomes:** the default biome of the starter chunk is `minecraft:plains` (the Skyblock Builder default). Frogs spawned here will be the **temperate** variant — informational only since our category model doesn't depend on vanilla frog variants.

### Nether
- **Type:** void (or near-void)
- **Y-range:** standard nether
- **Access:** unlocked via Tier 4 quest reward (Nether Portal Kit — 14 obsidian + 1 flint+steel, granted as a quest reward).
- **Biomes:** standard nether biomes, all reachable. Player can build a small nether base for ambient atmosphere; infernal frogs farm everything in their skyblock.
- **Surface generation:** intentionally minimal — we override most ore generation via KubeJS to force the frog path. Nether quartz, basalt deltas, etc. exist but yields are sparse.

### End
- **Type:** standard end islands (not void)
- **Access:** unlocked via Tier 6 quest reward, OR by defeating the Dragon (which requires assembling the End Portal from skyblock-farmed obsidian, eyes of ender, etc.).
- **Why standard, not void:** dragon fight is part of the endgame; needs proper End geometry. The outer end islands also provide chorus fruit and end stone via natural worldgen (these resources are also farmable via Arcane frogs, but the dragon arc needs the dimension).

### Custom dimensions (RFTools, Compact Machines)
- **Compact Machines:** kept — used heavily in late-game builds.
- **RFTools dimensions:** disabled in v0.x — too easy to bypass progression by spawning a custom dimension with whatever ore generation you want. Reconsider for v1.x with carefully-tuned dimlet costs.

## Productive Frogs parent species — the void problem

Productive Frogs ships six parent slime species, each conceptually tied to a vanilla biome:

| Parent species               | PF category | Default biome target          |
|------------------------------|-------------|-------------------------------|
| `minecraft:slime`            | METALLIC    | swamps + slime chunks         |
| `minecraft:magma_cube`       | INFERNAL    | nether wastes / basalt deltas |
| `productivefrogs:cave_slime` | MINERAL     | dripstone caves / deep dark   |
| `productivefrogs:geode_slime`| GEM         | lush caves / geodes           |
| `productivefrogs:tide_slime` | AQUATIC     | warm oceans                   |
| `productivefrogs:void_slime` | ARCANE      | end / void                    |

In a void skyblock **none of these biomes exist** in the meaningful sense (the player is in a single Plains chunk surrounded by void). So we need to seed parent species via an alternative path.

**Our solution (KubeJS-driven):**

1. **Quest reward** at the start of each tier chapter grants the player one parent species spawn egg. So Tier 1 grants `minecraft:slime` spawn egg, Tier 2 grants `productivefrogs:cave_slime`, etc.
2. The player breeds the parent species with slimeballs (vanilla mechanic for `minecraft:slime`) or PF's equivalent breeding mechanic for custom species. Self-sustaining once the player has two.
3. We override the **`productivebees:bee_spawning`-equivalent** recipes for PF parent species (if PF has analogous recipes for "spawn this species near these blocks") via KubeJS to allow spawning in any biome — same pattern Sky Bees Reborn uses for bee nests.

Concrete reference: see Sky Bees Reborn's [`kubejs/server_scripts/productivebees.js`](../../sky-bees-reborn-reference/extracted/kubejs/server_scripts/productivebees.js) `bee_nests` array — it remaps every nest's biome target via `event.custom({ type: 'productivebees:bee_spawning', biomes: '#minecraft:is_overworld', ... })`. We need to verify whether Productive Frogs exposes equivalent datapack-driven spawn recipes; if not, we file a feature request upstream and rely on quest-reward egg distribution in v0.x.

### Open worldgen questions

- Does Productive Frogs ship `parent_species` spawn JSONs we can KubeJS-override, or is parent species spawning purely entity-attribute based? File an issue if not exposed.
- Should we ship a custom dimension for "frog paradise" lategame — a void dimension with maximized frog spawn rates? Defer to v1.x; see [`backlog.md`](./backlog.md).
- Skyblock Builder vs. **Lost Cities** — both viable void generators. Skyblock Builder wins on UX (per-player island UI). Lost Cities would give a totally different feel (player starts in a ruined city). Locked in on Skyblock Builder.
