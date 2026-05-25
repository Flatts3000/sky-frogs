# Progression

> **Status:** DRAFT — for mark-up. This is the species-gated rewrite (2026-05-25) replacing the earlier resource-theme ordering. The premise (frog species gate progress) and the order (Cave → Geode → Bog → Tide → Infernal → Void) are settled; per-tier resource lists, gates, and playtimes are a sketch.
>
> **Version note:** this targets **Productive Frogs v1.1+** (57 thematic slime variants, component-driven Slime Milk, bottle-of-frogspawn). The pack currently consumes **PF v1.0.1** from CurseForge (only 12 variants, Bog empty, older milk). PF is published to CurseForge gradually, gated by CF review; the pack `packwiz update`s to newer PF as it clears. Until then, the live content lags this doc.

## The premise

**Frog species gate progression.** Each Productive Frogs species is a self-contained quest group ("tier"). You complete one species' line to unlock the next. There is no separate resource-tier abstraction — the species *is* the tier, and each species owns a thematic family of resources (inherited from PF's slime-variant data).

**Order (settled):**

| Tier | Species | Resource theme (from PF v1.1 variants) |
|------|---------|-----------------------------------------|
| 0    | *(bootstrap)* | Get on your feet + your first Cave frogs |
| 1    | **Cave**     | Ores & metals — iron, copper, gold, coal, lapis, redstone, diamond, obsidian, echo shard (+ modded metals) |
| 2    | **Geode**    | Gems & crystals — emerald, amethyst (+ modded: certus quartz, fluix, fluorite, silicon) |
| 3    | **Bog**      | Organic & mob-drops — bone, string, feather, leather, gunpowder, clay, rotten flesh (+ modded: pink slime, inferium/supremium) |
| 4    | **Tide**     | Aquatic — sponge, prismarine, prismarine crystals, ink sac (+ modded aquatics) |
| 5    | **Infernal** | Nether — blaze, nether quartz, soul sand/soil, netherrack, glowstone, netherite scrap |
| 6    | **Void**     | End & endgame — ender pearl, chorus fruit, shulker shell (+ modded endgame: nitro, mythril, orichalcum) |

Modded resources per tier are PF's conditional variants — they register only when the relevant mod ships in the pack, so the actual per-tier resource set tracks the Sky Frogs mod list.

## Design principles

1. **Species gate progress.** Each tier unlocks a new *family* of resources, not a faster version of the last.
2. **Each tier bootstraps the next.** A tier's quest line ends by crafting the next species' starter kit (see "Tier transitions"). You never have to find the next slime in the wild.
3. **The pack owns spawning; the mod supports it.** Only the **Cave** parent spawns naturally (the Tier 0 dark-room farm). Every later species comes from a crafted Slime Milk source, not from spawning. PF supplies the spawn-placement hook; the pack disables PF's default biome spawns and decides what spawns where.
4. **No tier requires automation.** PF V1 is hand-operated. The pack must be completable with hoppers, water streams, and patience. Automation (tech mods / PF V2) is *faster*, not *required*.

## Tier transitions (the gate mechanic)

Each species' quest line **ends by crafting two things** for the next species, via custom (KubeJS) recipes whose ingredients are the current tier's outputs:

1. A **Bottle of <Next> Frog Frogspawn** — PF's `frog_egg` bottle carrying the next category. Place it on water to start the next species' frogs.
2. A **bucket of <Next> Slime Milk** — place it as a source block; it spawns that species' parent slimes, giving the next tier its renewable slime supply with no natural spawning.

So: finish the **Cave** line → craft a Bottle of Geode Frogspawn + Geode Slime Milk → **Geode** tier opens. Finish **Geode** → craft the **Bog** kit. And so on down the order.

## The per-tier loop (same shape every tier)

Once a species is unlocked:

1. **Hatch the frogs.** Place the frogspawn bottle on water → primed frog egg → tadpoles → Resource Frogs of that species.
2. **Get parent slimes.** Place the species' Slime Milk source → it spawns that species' parent slimes. (Tier 1 Cave also farms them naturally in the dark room.)
3. **Infuse to a resource.** Right-click a parent slime with a resource's **primer item** (exact match, species-locked) → a Resource Slime of that variant. E.g. Cave Slime + iron → Iron Slime. A Cave Slime can only become a Cave variant; wrong-species primers are rejected.
4. **Feed the frog.** The matching-species frog eats the Resource Slime → drops a **Configurable Froglight** stamped with that variant (`productivefrogs:slime_variant` component).
5. **Process.** Smelt the Froglight → the resource. (Crush+smelt via a tech mod → 2×, later.)
6. **Scale.** Milk Resource Slimes through a **Slime Milker** for more milk sources; hoppers + water streams move everything.

## Tier 0 — Bootstrap

The Welcome quest chapter. Player spawns on the starter island with the first-join grant (saplings, water + lava buckets, food, quest book). No frog content yet — the goal is a slime farm and your first Cave frogs.

- **Wood → tools → crafting table.**
- **Cobblestone generator** (vanilla water + lava).
- **Second water source** via an Ex Deorum rain-collection barrel → infinite water. (Ex Deorum's barrel is the only Tier 0 Ex Deorum mechanic; sieving is disabled pack-wide.)
- **Dark-room mob farm.** The starter island is forced to a biome where **Cave Slimes** spawn (the pack adds `cave_slime` to the island biome; PF's light-based placement rule does the rest). Cave Slimes are the Tier 1 parent.
- **Collect slimeballs**, and split-discover the occasional resource slime.
- **Complete the chapter → reward: a Bottle of Cave Frog Frogspawn** (a breeding pair's worth). Place it on water to begin Tier 1.

Estimated playtime: **30–60 min**.

## Tier 1 — Cave (the ore engine)

**Chapter:** *Cave* (working title). The foundational tier — this is where "frogs replace mining" becomes real.

- Hatch Cave Frogs from the Tier 0 reward.
- Farm Cave Slimes (dark room) and/or place Cave Slime Milk sources.
- Infuse with ore primers → Iron/Copper/Gold/Coal/Lapis/Redstone/Diamond Slimes (+ modded metals if those mods ship).
- Cave Frogs → Configurable Froglights → smelt → ingots.
- **Gate to Tier 2:** craft a Bottle of Geode Frogspawn + Geode Slime Milk.

Estimated playtime: **3–6 hours** (it's the widest tier — most resources live here).

## Tier 2 — Geode (gems)

**Chapter:** *Geode*. Faceted materials for better tooling and the first modded-crystal pipelines (AE2 certus/fluix, etc., if shipped).

- Geode Frogs + Geode Slimes (from the crafted Geode Slime Milk).
- Infuse with gem primers → Emerald/Amethyst Slimes (+ certus quartz, fluix, fluorite, silicon if modded).
- **Gate to Tier 3:** craft the Bog starter kit.

Estimated playtime: **3–5 hours**.

## Tier 3 — Bog (organics & mob-drops)

**Chapter:** *Bog*. The overworld/swamp catch-all — the renewable source of mob-drop materials a skyblock normally grinds spawners for.

- Bog Frogs + Bog Slimes (crafted milk).
- Infuse → Bone/String/Feather/Leather/Gunpowder/Clay/Rotten-Flesh Slimes (+ pink slime, Mystical Agriculture inferium/supremium if modded).
- **Gate to Tier 4:** craft the Tide starter kit.

Estimated playtime: **3–5 hours**.

## Tier 4 — Tide (aquatic)

**Chapter:** *Drowned Riches* (working title). Ocean materials without an ocean.

- Tide Frogs + Tide Slimes (crafted milk).
- Infuse → Sponge/Prismarine/Prismarine-Crystal/Ink Slimes.
- **Gate to Tier 5:** craft the Infernal starter kit.

Estimated playtime: **3–6 hours**.

## Tier 5 — Infernal (nether)

**Chapter:** *Heat & Flame* (working title). Nether materials; an optional small Nether base for ambiance, but Infernal frogs are the real path.

- Infernal Frogs + Infernal Slimes (crafted milk).
- Infuse → Blaze/Quartz/Soul-Sand/Netherrack/Glowstone/Netherite-Scrap Slimes.
- **Netherite line** is gated here.
- **Gate to Tier 6:** craft the Void starter kit.

Estimated playtime: **6–10 hours**.

## Tier 6 — Void (end & endgame)

**Chapter:** *Void Mastery* + *The End*. Endgame.

- Void Frogs + Void Slimes (crafted milk).
- Infuse → Ender-Pearl/Chorus/Shulker Slimes (+ modded endgame materials).
- **Endgame creative loop:** scale Froglights → Singularities (Extended Crafting) → Ultimate Singularity → a custom **Sky Frogs Master Frog** trophy. (Design TBD; see [`backlog.md`](./backlog.md).)

Estimated playtime: **15+ hours** to fully clear.

## Total estimated runtime

**~40–70 hours** from fresh world to creative trophy, single-player normal difficulty.

## Chapter-to-tier mapping (preview)

For the full questbook structure see [`quest_book.md`](./quest_book.md).

| Quest chapter        | Covers                                   |
|----------------------|-------------------------------------------|
| Welcome              | Tier 0 bootstrap → first Cave frogs       |
| Cave                 | Tier 1 (Cave) — ores & metals             |
| Geode                | Tier 2 (Geode) — gems                      |
| Bog                  | Tier 3 (Bog) — organics & mob-drops        |
| Drowned Riches       | Tier 4 (Tide) — aquatic                    |
| Heat & Flame         | Tier 5 (Infernal) — nether                 |
| Void Mastery / The End | Tier 6 (Void) — end & endgame            |
| Master Pond          | Endgame singularity loop                  |
| (per-mod side chapters) | One per significant tech mod, optional-but-recommended |
