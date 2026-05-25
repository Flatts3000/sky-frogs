# Progression

> **Status:** DRAFT — non-canonical. The six-tier structure follows the Productive Frogs category enum and that's load-bearing; everything else (chapter sequencing, playtime estimates, gate-unlock items, bootstrap shape) is a sketch. The actual identity of Sky Frogs lives in *how* progression feels, and that's not yet decided.

The Sky Frogs player journey — from spawning on a 3×3 island to building an automated Configurable Froglight farm of every category.

## Design principles

1. **Six clear tiers** — one per Productive Frogs category. Each tier is a quest chapter (sometimes two).
2. **Every tier gates a new category of resources.** The player should always feel they're unlocking a new *kind* of thing, not just a faster version of the previous tier.
3. **Bootstrap is friendly, mid-game is demanding.** Tier 0–1 should be reachable in a couple hours. Tier 6 should take a long campaign.
4. **No tier requires automation.** Productive Frogs V1 ships hand-operated appliances only. The pack must be completable with hoppers, water streams, and patience. Automation (when PF V2 lands or via tech mods) is *faster*, not *required*.

## Tier 0 — Bootstrap

Player spawns on a 3×3 dirt island with the first-join inventory grant (saplings, water bucket, lava bucket, food). The FTB Quests book auto-opens. No frog content yet; the goal is building a slime farm.

**Goals:**
- **Wood bootstrap.** Plant saplings → grow tree → wooden tools.
- **Cobble generator.** Vanilla water + lava (one bucket of each, placed adjacent) → infinite cobble. Source of all build material.
- **Second water source.** The grant has 1 water bucket = 1 source. Vanilla infinite water needs 2 sources adjacent. Player builds an **Ex Deorum barrel outside their claim**, collects rainwater, buckets the second source → infinite water square. (Ex Deorum's barrel is the only Tier 0 mechanic from Ex Deorum the player touches — sieving is disabled pack-wide.)
- **Mob farm.** Standard dark-room slime farm built from cobble. `productivefrogs:bog_slime` (the Bog parent per PF's `ParentSpeciesEntry`) spawns in the dark room. PF v1.0.0 already ships bog_slime spawning (a biome modifier that adds it to `minecraft:swamp` + `minecraft:mangrove_swamp`, plus a light-based placement rule), so all the pack does is force the SkyblockBuilder island to the `minecraft:swamp` biome and PF's shipped spawning handles the rest. No pack-side spawn override needed.
- **Collect slimeballs.** Bog slime kills drop slimeballs. Occasionally a slime split produces an Iron Slime via PF's `SlimeSplitDiscoveryHandler` (configurable rate).
- **Complete the Welcome quest chapter** → reward is **2× Bog frog egg** (the placeable `productivefrogs:bog_frog_egg` block; no priming step needed; two so the player has a breeding pair from minute one).

**Unlock for Tier 1:** the moment the player places one Bog frog egg on water. That's the start of the frog loop.

Estimated playtime: **30–60 min**.

**No iron sourcing in Tier 0.** The player's first iron ingot is the smelted output of the first Iron Configurable Froglight, which their Bog Resource Frog produces from an Iron Slime. Iron is a Tier 1 emergent property of the slime farm + frog loop, not a Tier 0 deliverable.

## Tier 1 — Bog (gateway)

**Quest chapter:** *Bog Mastery*

The player has iron. Now: frogs.

1. Find or trap vanilla frogs. **Skyblock problem:** vanilla frogs don't spawn naturally. We solve this via the **first-join inventory grant** (one frogspawn item, one slime spawn egg) or a **questbook reward** for completing the bootstrap.
2. Breed frogs with slimeballs → frogspawn on water.
3. Right-click frogspawn with empty glass bottle → **Frog Egg item**.
4. Place Frog Egg on water → Frog Egg block.
5. Right-click Frog Egg block with any **Bog primer** (iron ingot / copper ingot / gold ingot or any modded primer tagged `productivefrogs:primer/bog`).
6. Block becomes a **Bog Frog Egg**, ingot consumed.
7. Hatch into **Bog Tadpole** → grows into **Bog Frog**.
8. **Get an Iron Slime:**
   - **Infusion path (deterministic):** right-click a bog slime with an iron ingot → it becomes an Iron Slime. Costs 1 ingot per slime.
   - **Discovery path (random):** kill a bog slime; each split has a chance to convert.
9. **Scale via milking:**
   - Bucket the size-1 Iron Slime → **Bucket of Iron Slime**.
   - Place bucket in a **Slime Milker** appliance block → **Bucket of Iron Slime Milk**.
   - Place milk source blocks near your Bog Frog enclosure. Each source spawns size-1 Iron Slimes every ~20s (default 16 spawns per block).
10. Bog Frog eats spawning Iron Slimes → drops **Iron Configurable Froglight** item entities.
11. Collect via hopper → smelt → 1 iron ingot per Froglight, or crush+smelt via Mekanism / Productive Metalworks → 2 ingots.

**Resources unlocked at Tier 1 (Bog):**
- Vanilla: iron, copper, gold
- Modded (via tag): osmium (Mekanism), aluminum (IE), nickel (IE), zinc, lead (Mekanism), silver (IE), tin (Mekanism)

**Unlock for Tier 2:** redstone dust (or any item in `productivefrogs:primer/cave`).

Estimated playtime: **2–4 hours**.

## Tier 2 — Cave

**Quest chapter:** *Cave Veins*

Same loop, new category.

1. Acquire redstone dust (via crushing Tier 1 Bog outputs in Mekanism's enrichment chamber from sieved cobblestone? Or as a quest reward bridging the gap.)
2. Prime a new Frog Egg with redstone → **Cave Frog Egg** → **Cave Frog**.
3. Get a **Cave Slime** parent species — the PF Cave parent (`productivefrogs:cave_slime`). Spawns from PF's data-driven `parent_species` registry; we acquire it via a quest-reward spawn egg (no overworld biome needed).
4. Infuse parent Cave Slime with redstone (or lapis, coal, etc.) → category-matching Cave Resource Slime.
5. Cave Frog eats it → drops Configurable Froglight of that variant.

**Resources unlocked at Tier 2 (Cave):**
- Vanilla: redstone, lapis, coal, quartz (overworld), amethyst shards
- Modded: certus quartz (AE2), niotic crystal (Powah), fluix dust, black quartz (Actually Additions), industrial diamond seeds

**Unlock for Tier 3:** diamond or any item in `productivefrogs:primer/geode`.

Estimated playtime: **3–6 hours**.

## Tier 3 — Geode

**Quest chapter:** *The Geode Workshop*

By now the player has a real economy, several frog enclosures, and is starting to demand more sophisticated tools.

1. Prime with diamond / emerald / amethyst → **Geode Frog**.
2. Use **Geode Slime** parent species (PF Geode parent).
3. Infuse with diamond → Diamond Slime; emerald → Emerald Slime; etc.

**Resources unlocked at Tier 3 (Geode):**
- Vanilla: diamond, emerald
- Modded: fluorite (Mekanism), certus crystal (AE2 grown), peridot/sapphire/ruby (Silent Gear), industrial diamonds

**Unlock for Tier 4:** prismarine shard or item in `productivefrogs:primer/tide`.

Estimated playtime: **4–8 hours**.

## Tier 4 — Tide

**Quest chapter:** *Drowned Riches*

Tide resources are slightly harder to bootstrap on a void skyblock (no ocean), so the chapter starts with helping the player build a small water arena.

1. Prime with prismarine shard / scute / nautilus shell → **Tide Frog**.
2. Use **Tide Slime** parent species (PF Tide parent).
3. Infuse parent with Tide primers.

**Resources unlocked at Tier 4 (Tide):**
- Vanilla: prismarine, sea pickles, kelp, ink/glow ink sacs, sponge
- Modded: pink slime (IF), latex (IF), aqueous resources from Mekanism / Powah

**Special:** Tide frogs power **Industrial Foregoing's Pink Slime line** — once Tier 4 is online, the player can produce pink slime ingots without an IF mob farm.

**Unlock for Tier 5:** blaze rod or item in `productivefrogs:primer/infernal`.

Estimated playtime: **3–6 hours**.

## Tier 5 — Infernal

**Quest chapter:** *Heat & Flame*

Player can now visit the Nether via a portal kit reward from late Tier 4. The Nether dimension is intentionally limited — the player will build a small base for ambient Nether environment, but Infernal frog farming is still the main path.

1. Prime with blaze rod / netherite ingot → **Infernal Frog**.
2. Use **Infernal Slime** parent species (`productivefrogs:infernal_slime`, PF Infernal parent).
3. Infuse with infernal primers → blaze slime, magmatic slime, etc.

**Resources unlocked at Tier 5 (Infernal):**
- Vanilla: blaze rods, ghast tears, nether quartz, glowstone, magma cream
- Modded: nether-themed Mekanism resources, hop graphite coke (IE), crimson iron (Productive Metalworks)
- **Netherite line** is gated through this tier — netherite scrap requires Infernal Froglight smelting + Tier 3+ Geode ancient debris equivalent.

**Unlock for Tier 6:** ender pearl or item in `productivefrogs:primer/void`.

Estimated playtime: **6–10 hours**.

## Tier 6 — Void

**Quest chapter:** *Void Mastery* and *The End*

Endgame. The player has dragon-egg-tier ambitions.

1. Prime with ender pearl / chorus fruit / dragon's breath → **Void Frog**.
2. Use **Void Slime** parent species (PF Void parent).
3. Infuse with Void primers.

**Resources unlocked at Tier 6 (Void):**
- Vanilla: ender pearls, chorus fruit, popped chorus fruit, dragon's breath, end stone
- Modded: sky stone (AE2), vibrant alloy components (EnderIO), dimensional shards (RFTools), draconic-tier modded resources

**The endgame creative loop:**
- Late-Void: produce **Singularities** (Extended Crafting) at scale.
- Combine into **Ultimate Singularity**.
- Combine into a custom **Sky Frogs Master Frog** item — placeholder for the creative trophy. (Specific design TBD; see [`backlog.md`](./backlog.md).)

Estimated playtime: **15+ hours** to fully clear.

## Total estimated runtime

**~50–80 hours** from fresh world to creative trophy on a single-player normal-difficulty run. This is comparable to Sky Bees Reborn.

## Chapter-to-tier mapping (preview)

For the full questbook structure see [`quest_book.md`](./quest_book.md). High-level mapping:

| Quest chapter           | Covers tier(s)                                |
|-------------------------|-----------------------------------------------|
| Welcome                 | First-launch only                             |
| Getting Started         | Tier 0 bootstrap                              |
| Bog Mastery             | Tier 1 (Bog)                                  |
| Cave Veins              | Tier 2 (Cave)                                 |
| The Geode Workshop      | Tier 3 (Geode)                                |
| Drowned Riches          | Tier 4 (Tide)                                 |
| Heat & Flame            | Tier 5 (Infernal)                             |
| Void Mastery            | Tier 6 (Void) — overworld portion            |
| The End                 | Tier 6 dimension                              |
| Master Hive (Pond)      | Endgame singularity loop                      |
| (per-mod side chapters) | One per significant tech mod (Mek/AE2/IE/IF/etc.) |

The "per-mod side chapters" mirror Sky Bees Reborn's structure: a chapter each for `mekanism.snbt`, `applied_energistics.snbt`, `industrial_foregoing.snbt`, etc. — these are optional-but-recommended, providing the infrastructure the player will want to scale up.
