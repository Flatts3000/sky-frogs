# Progression

> **Status:** DRAFT. Tiers 0-3 (Welcome, Cave, Geode, Bog) are built and live; Tier 4-6 (Tide, Infernal, Void) remain a sketch. The premise (frog species gate progress) and the order (Cave -> Geode -> Bog -> Tide -> Infernal -> Void) are settled; the Tier 4-6 resource lists, gates, and playtimes below are still a sketch.
>
> **Version note:** the pack consumes **Productive Frogs v1.6.0** (organic Bog roster + Industrial Foregoing plastic/pink_slime variants, component-driven Slime Milk, bottle-of-frogspawn). The Tier 0-3 content described here is built against that pin and live in the pack. PF continues to publish to CurseForge gradually; the pack `packwiz update`s to newer PF as it clears.

## The premise

**Frog species gate progression.** Each Productive Frogs species is a self-contained quest group ("tier"). You complete one species' line to unlock the next. There is no separate resource-tier abstraction — the species *is* the tier, and each species owns a thematic family of resources (inherited from PF's slime-variant data).

**Order (settled):**

| Tier | Species | Resource theme (built unless noted) |
|------|---------|-----------------------------------------|
| 0    | *(bootstrap)* | Get on your feet + a cave_slime farm |
| 1    | **Cave**     | Ores & metals: iron -> copper -> gold -> coal -> redstone (the built chain). Lapis moved to Geode in PF 1.5.1; diamond is a Geode resource; obsidian deferred to Infernal. |
| 2    | **Geode**    | Gems & crystals: lapis -> tuff -> calcite -> amethyst -> emerald -> diamond |
| 3    | **Bog**      | Organic & swamp: dirt -> mud -> clay_ball -> moss -> mycelium -> lily_pad -> leather -> feather -> plastic -> pink_slime (the last two are Industrial Foregoing items; IF is a hard pack dependency) |
| 4    | **Tide**     | Aquatic: sponge, prismarine, prismarine crystals, ink sac (+ modded aquatics). *Sketch.* |
| 5    | **Infernal** | Nether: blaze, nether quartz, soul sand/soil, netherrack, glowstone, netherite scrap. *Sketch.* |
| 6    | **Void**     | End & endgame: ender pearl, chorus fruit, shulker shell (+ modded endgame: nitro, mythril, orichalcum). *Sketch.* |

Modded resources per tier are PF's conditional variants — they register only when the relevant mod ships in the pack, so the actual per-tier resource set tracks the Sky Frogs mod list.

## Design principles

1. **Species gate progress.** Each tier unlocks a new *family* of resources, not a faster version of the last.
2. **Each tier bootstraps the next.** A tier's quest line ends by crafting the next species' starter kit (see "Tier transitions"). You never have to find the next slime in the wild.
3. **The pack owns spawning; the mod supports it.** Only the **Cave** parent spawns naturally (the Tier 0 dark-room farm). Every later species comes from a crafted Slime Milk source, not from spawning. PF supplies the spawn-placement hook; the pack disables PF's default biome spawns and decides what spawns where.
4. **No tier requires automation.** PF V1 is hand-operated. The pack must be completable with hoppers, water streams, and patience. Automation (tech mods / PF V2) is *faster*, not *required*.
5. **Froglight-check principle (pack-wide design law).** Per-tier resource quests detect the variant **Froglight** (`productivefrogs:configurable_froglight` carrying a `productivefrogs:slime_variant` component), *not* the smelted resource, so the frog loop can't be bypassed by obtaining the resource another way. Two deliberate exceptions: the **Your First Iron Ingot** capstone keeps checking `iron_ingot` (it is the tutorial that teaches the smelt, and the Froglight route is already gated upstream by its "Feed the Frog" quest), and the main Mekanism **Steel** quest keeps checking `ingot_steel` (steel via the Metallurgic Infuser is a Mekanism craft, not a frog resource) while the *optional* steel-slime quest carries the Froglight check.
6. **One new verb per tier (anti-repetition).** Each tier layers exactly one new verb onto the frog loop so the gameplay doesn't just repeat at a higher number:
   - **Cave** = crafting upgrades / storage (Sophisticated + Functional storage, quartz-free networks).
   - **Geode** = automation (Mekanism: power, Metallurgic Infuser, Enrichment Chamber).
   - **Bog** = Industrial Foregoing (plastic hard-gated behind the Bog plastic-frog; pink_slime capstone). The machine climb (Pity frame -> Fluid Extractor for latex -> **Dissolution Chamber**) lives in the `industrial_foregoing.snbt` chapter.
   - **Infernal** = earmarked for Refined Storage (*sketch*).

## Tier transitions (the gate mechanic)

Each species' quest line **ends by opening the next species**, in two halves:

1. **Frog side (the Spawnery).** Prime the Spawnery with a tier-specific **primer item** to draw the *next* species' **Frogspawn** bottle (a `frog_egg` carrying the next `contained_category`). The pack overrides each `spawnery_primer/<species>` tag to a resource the player has by the prior tier's end. The built primers: **Geode is primed by redstone** (Cave's last resource: `spawnery_primer/geode` -> `minecraft:redstone`), and **Bog is primed by enriched diamond** (a Mekanism craft: `spawnery_primer/bog` -> `mekanism:enriched_diamond`). Place the frogspawn on water to start the next species' frogs.
2. **Slime side (the seed-chain bootstrap).** The next tier's *resource* slimes come from a custom (KubeJS) **slime-in-a-bucket** recipe seeded from the current tier's outputs (the same pattern as Cave's iron -> copper -> ... chain), milked for a renewable supply. This lives in the *next* tier's chapter, not the gateway. Each step also consumes **4 of a tier-themed filler block** (see "Per-tier filler blocks" below). The *intended* end state is for the Industrial Foregoing **Dissolution Chamber** (the Bog tech verb) to take over this bootstrap from Tier 4 on and to bulk-make any already-unlocked slime; that is currently blocked by an IF/Titanium recipe-sync limitation and **deferred** pending a PF feature ([productive-frogs#127](https://github.com/Flatts3000/productive-frogs/issues/127)), so the crafting-table seed-chain remains the mechanism for every built tier.

> **Not slime milk for parents.** PF's Slime Milk is keyed by `SLIME_VARIANT` and spawns that *resource-variant* slime, not the bare parent species (the parent comes from a spawn egg / splitting). So the next tier is bootstrapped via frogspawn (Spawnery) + a resource-slime seed-chain, *not* a "parent slime milk" source. (Corrected 2026-05-27; the earlier draft of this section described a parent-spawning milk that PF does not implement.)

So: finish the **Cave** line at redstone → prime the Spawnery with redstone for **Geode Frogspawn** → **Geode** tier opens (its resource seed-chain is the Geode chapter's job). Then Geode → Bog (primed with enriched diamond), and so on down the order.

### Per-tier filler blocks

Each tier's slime-in-a-bucket seed-chain recipe spends **4 of a tier-themed filler block** per step. The constraint: a tier's filler must be mass-attainable *at that tier* (not a chain output, not gated behind a later tier). The same per-tier filler is intended to carry into the Dissolution Chamber slime recipes (deferred, see productive-frogs#127).

| Tier | Filler block | Source |
|------|--------------|--------|
| Cave  | **stone** | smelted/farmed at Tier 1 |
| Geode | **gravel** | the Ex Deorum block you sieve gems from |
| Bog   | **mossy cobblestone** | crafted in Mekanism's Metallurgic Infuser / Enrichment Chamber (the Geode-era machines) |

Tide / Infernal / Void fillers are TBD.

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
- Infuse with ore primers → Iron → Copper → Gold → Coal → Redstone Slimes (+ modded metals if those mods ship). (Lapis and diamond are Geode resources; obsidian is deferred to Infernal.)
- Cave Frogs → Configurable Froglights → smelt → ingots.
- **New verb:** crafting upgrades / storage. Sophisticated + Functional storage, with quartz-free network recipes (the Cave-tier "Storage and Crafting" interlude).
- **Gate to Tier 2:** prime the Spawnery with **redstone** for a Bottle of Geode Frogspawn, then run the Geode seed-chain.

Estimated playtime: **3–6 hours** (it's the widest tier — most resources live here).

## Tier 2 — Geode (gems)

**Chapter:** *Geode*. Faceted materials for better tooling, and the tier where automation arrives.

- Geode Frogs + Geode Slimes (from the crafted Geode seed-chain).
- Infuse with gem primers → Lapis → Tuff → Calcite → Amethyst → Emerald → Diamond Slimes.
- **New verb:** automation. Mekanism (power, Metallurgic Infuser, Enrichment Chamber). The Mekanism machines also craft the mossy cobblestone the Bog seed-chain needs.
- **Slime Milk catalysts** (PF v1.7.0): a short branch off the diamond capstone introduces the four catalysts (Count / Speed / Quantity / Infinite Count) that buff placed Slime Milk sources. Infinite Count's recipe needs a diamond, so it gates naturally here; the Quantity catalyst is re-issued with redstone instead of glowstone for skyblock (`catalyst_recipes.js`).
- **Gate to Tier 3:** prime the Spawnery with **enriched diamond** (a Mekanism craft) for Bog Frogspawn, then run the Bog seed-chain.

Estimated playtime: **3–5 hours**.

## Tier 3 — Bog (organics & mob-drops)

**Chapter:** *Bog*. The overworld/swamp catch-all: the renewable source of organic materials a skyblock normally grinds for.

- Bog Frogs + Bog Slimes (from the crafted Bog seed-chain, bridged off diamond Slime Milk).
- Infuse → Dirt → Mud → Clay_ball → Moss → Mycelium → Lily_pad → Leather → Feather → Plastic → Pink_slime Slimes. The last two (plastic, pink_slime) are Industrial Foregoing items; IF is a hard pack dependency.
- **New verb:** Industrial Foregoing (the `industrial_foregoing.snbt` chapter). Plastic is hard-gated behind the Bog plastic-frog; the machine climb runs Pity Machine Frame -> Fluid Extractor (latex) -> **Dissolution Chamber**, with an optional Plant Gatherer + Sludge Refiner branch. Making the Dissolution Chamber the slime engine (bulk-making unlocked slimes, bootstrapping Tier 4+) is the intended payoff but is **deferred** pending productive-frogs#127 - an IF/Titanium recipe-sync limitation blocks the component-keyed input.
- **Gate to Tier 4:** craft the Tide starter kit; the Tide gateway will depend on the Dissolution Chamber capstone the way Bog's gateway depends on the Mekanism capstone. *(Tier 4-6 unbuilt.)*

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
| Welcome              | Tier 0 bootstrap (cave_slime farm) -> first Cave frogs |
| Tier 1: Cave         | Your First Iron Ingot, Scaling the Colony, Cave Frogs, Storage and Crafting (ores & metals) |
| Tier 2: Geode        | Road to Geode, Geode Frogs, Mekanism (gems & automation) |
| Tier 3: Bog          | Road to Bog, Bog Frogs (organics & Industrial Foregoing) |
| Drowned Riches       | Tier 4 (Tide), aquatic *(unbuilt)*        |
| Heat & Flame         | Tier 5 (Infernal), nether *(unbuilt)*     |
| Void Mastery / The End | Tier 6 (Void), end & endgame *(unbuilt)* |
| Master Pond          | Endgame singularity loop *(unbuilt)*      |
