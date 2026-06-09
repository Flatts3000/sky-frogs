# Progression

> **Status:** All six tiers (Welcome, Cave, Geode, Bog, Tide, Infernal, Void) are built and live, through the Master Pond endgame and the Sky Frogs Master Frog trophy. The premise (frog species gate progress) and the order (Cave -> Geode -> Bog -> Tide -> Infernal -> Void) are settled. The content campaign is complete; remaining work is balance, art (the Master Frog texture), and optional modded-variant expansion.
>
> **Version note:** the pack consumes **Productive Frogs 1.16.0** (the full roster through the mob-drop + boss resources, per-variant Slime Milk that survives pipe automation, the four Slime Milk catalysts, the Crucible/Mold, Brewed Froglights, the Slime Churn, and **The Terrarium** automation multiblock). All six tiers plus the Trophy Pond boss campaign and the Terrarium chapter are built against this pin and live. The full bump-by-bump pin history is in [`pf_pin_history.md`](./pf_pin_history.md); the pack `packwiz update`s to newer PF as it publishes.

## The premise

**Frog species gate progression.** Each Productive Frogs species is a self-contained quest group ("tier"). You complete one species' line to unlock the next. There is no separate resource-tier abstraction — the species *is* the tier, and each species owns a thematic family of resources (inherited from PF's slime-variant data).

**Order (settled):**

| Tier | Species | Resource theme (built unless noted) |
|------|---------|-----------------------------------------|
| 0    | *(bootstrap)* | Get on your feet + a cave_slime farm |
| 1    | **Cave**     | Ores & metals: iron -> copper -> gold -> coal -> glow_ink_sac -> redstone (the built chain; glow ink joined in v0.5.0, #79). Lapis moved to Geode in PF 1.5.1; diamond is a Geode resource; obsidian moved to Infernal in PF 1.10.0. |
| 2    | **Geode**    | Gems & crystals: lapis -> tuff -> calcite -> amethyst -> emerald -> diamond |
| 3    | **Bog**      | Organic & swamp: dirt -> mud -> clay_ball -> moss -> mycelium -> lily_pad -> leather -> feather -> plastic -> pink_slime (the last two are Industrial Foregoing items; IF is a hard pack dependency) |
| 4    | **Tide**     | Aquatic: prismarine -> prismarine_crystals -> sponge -> ink_sac -> sea_pickle -> nautilus_shell (the built chain). |
| 5    | **Infernal** | Nether: netherrack -> obsidian -> quartz -> glowstone -> soul_sand -> soul_soil -> blaze -> netherite_scrap (the built chain; obsidian joined in v0.5.0 as netherrack's portal-stone partner, #79; netherite scrap is the endgame capstone). |
| 6    | **Void**     | End & endgame: ender pearl, end stone, chorus fruit, echo shard, sculk, shulker shell. Earned by a one-time dragon expedition; ends in the Master Frog trophy. |

Modded resources per tier are PF's conditional variants — they register only when the relevant mod ships in the pack, so the actual per-tier resource set tracks the Sky Frogs mod list.

## Design principles

1. **Species gate progress.** Each tier unlocks a new *family* of resources, not a faster version of the last.
2. **Each tier bootstraps the next.** A tier's quest line ends by crafting the next species' starter kit (see "Tier transitions"). You never have to find the next slime in the wild.
3. **The pack owns spawning; the mod supports it.** Only the **Cave** parent spawns naturally (the Tier 0 dark-room farm). Every later species comes from a crafted Slime Milk source, not from spawning. PF supplies the spawn-placement hook; the pack disables PF's default biome spawns and decides what spawns where.
4. **No tier requires automation.** The pack must be completable with hoppers, water streams, and patience. Automation is *faster*, not *required* - and it now exists in-line: PF 1.16's **Terrarium** (a sealed multiblock that runs the frog loop hands-off, quested in the Infernal tier) is the automation payoff, not a gate. ("PF V2 is just a name, not a rule" - the old hand-operated-only stance is retired.)
5. **Froglight-check principle (pack-wide design law).** Per-tier resource quests detect the variant **Froglight** (`productivefrogs:configurable_froglight` carrying a `productivefrogs:slime_variant` component), *not* the smelted resource, so the frog loop can't be bypassed by obtaining the resource another way. Two deliberate exceptions: the **Your First Iron Ingot** capstone keeps checking `iron_ingot` (it is the tutorial that teaches the smelt, and the Froglight route is already gated upstream by its "Feed the Frog" quest), and the main Mekanism **Steel** quest keeps checking `ingot_steel` (steel via the Metallurgic Infuser is a Mekanism craft, not a frog resource) while the *optional* steel-slime quest carries the Froglight check.
6. **One new verb per tier (anti-repetition).** Each tier layers exactly one new verb onto the frog loop so the gameplay doesn't just repeat at a higher number:
   - **Cave** = crafting upgrades / storage (Sophisticated + Functional storage, quartz-free networks).
   - **Geode** = automation (Mekanism: power, Metallurgic Infuser, Enrichment Chamber).
   - **Bog** = Just Dire Things' tier-1 progression (Primogel Goo -> Ferricore -> Fluid Collector -> Fluid Placer -> Item Collector) plus a Building Gadgets 2 side branch. Lives in `tools_and_things.snbt`. Mekanism RF from Geode powers the JDT machines.
   - **Tide** = **jetpacks (mobility)** - Iron Jetpacks' coil-tiered progression (basic/iron -> advanced/gold -> elite/diamond -> ultimate/emerald), charged with Geode-era Mekanism RF. Lives in `take_flight.snbt`. The first *mobility* verb - every prior verb was stationary, and a sprawling void island wants flight.
   - **Infernal** = **Refined Storage** (RS 2.0): the digital storage + autocrafting network. Lives in `the_network.snbt` - Quartz Enriched Iron -> Controller -> Grid -> Disk Drive -> External Storage -> Import/Export -> Crafting Grid -> Autocrafting. Naturally gated on nether quartz (RS parts need Quartz Enriched Iron), which only the Infernal frog produces.
   - **Void** = **Extended Crafting** (the singularity endgame): black iron -> luminessence -> the tiered crafting tables (basic/advanced/elite/ultimate) -> the Quantum Compressor. Lives in `the_ultimate_table.snbt`. The compressor folds a thousand Froglights into one **Singularity** (per species), so it doubles as a proof-of-automation gate - you cannot hand-make the inputs. Six Singularities combine into the Ultimate Singularity, which crafts the **Master Frog** trophy (the `master_pond.snbt` endgame chapter).

## Tier transitions (the gate mechanic)

Each species' quest line **ends by opening the next species**, in two halves:

1. **Frog side (the Spawnery).** Prime the Spawnery with a tier-specific **primer item** to draw the *next* species' **Frogspawn** bottle (a `frog_egg` carrying the next `contained_category`). The pack overrides each `spawnery_primer/<species>` tag to a resource the player has by the prior tier's end. The built primers: **Geode** by redstone (Cave's last: `spawnery_primer/geode` -> `minecraft:redstone`), **Bog** by enriched diamond (a Mekanism craft: `spawnery_primer/bog` -> `mekanism:enriched_diamond`), **Tide** by pink_slime (Bog's last: `spawnery_primer/tide` -> `industrialforegoing:pink_slime`), and **Infernal** by **nether brick** (`spawnery_primer/infernal` -> `minecraft:nether_bricks`). Place the frogspawn on water to start the next species' frogs.

**The Infernal gate is the exception - a real Nether expedition.** Nether brick is the only primer not handed to you by the prior tier, on purpose: it isn't craftable before Infernal (netherrack, the first Infernal resource, is gated behind the very frog you're trying to summon), so its only source is a **Nether fortress**. To enter Infernal the player builds a portal (the gateway grants the obsidian), flies the void Nether on their Tide-tier **jetpack**, raids a floating fortress for nether brick, and primes the Spawnery with it. After that one trip the frog automates the Nether forever. This needs `config/skyblockbuilder/structures.json5` to whitelist `minecraft:fortress` (SkyblockBuilder generates no structures by default).
2. **Slime side (the seed-chain bootstrap).** The next tier's *resource* slimes come from a custom (KubeJS) **slime-in-a-bucket** recipe seeded from the current tier's outputs (the same pattern as Cave's iron -> copper -> ... chain), milked for a renewable supply. This lives in the *next* tier's chapter, not the gateway. Each step also consumes **4 of a tier-themed filler block** (see "Per-tier filler blocks" below). The Industrial Foregoing **Dissolution Chamber** (taught in `road_to_tide.snbt`, the Tier 4 gateway, gated on completing `bog_frogs`) is the pack's slime engine. Each recipe consumes a prior vanilla resource (the previous tier's last resource for the first variant in a tier; the previous variant's resource for each step after) + tier filler + sweetslime + latex - the same chain shape as the Cave/Geode/Bog crafting-table chains, just transposed into the machine. Cave/Geode/Bog all ship today as chamber recipes alongside the existing crafting tables (iron bootstraps off bone meal in the chamber; the crafting tables remain a parallel hand-craft path); Tier 4 (Tide) onward land as those tiers ship. Resource-keyed inputs sidestep IF/Titanium's JSON-codec drop of component ingredients (the milk-keyed approach hit the codec wall; PF declined a component-free per-variant handle, see [productive-frogs#127](https://github.com/Flatts3000/productive-frogs/issues/127)).

> **Not slime milk for parents.** PF's Slime Milk is keyed by `SLIME_VARIANT` and spawns that *resource-variant* slime, not the bare parent species (the parent comes from a spawn egg / splitting). So the next tier is bootstrapped via frogspawn (Spawnery) + a resource-slime seed-chain, *not* a "parent slime milk" source. (Corrected 2026-05-27; the earlier draft of this section described a parent-spawning milk that PF does not implement.)

So: finish the **Cave** line at redstone → prime the Spawnery with redstone for **Geode Frogspawn** → **Geode** tier opens (its resource seed-chain is the Geode chapter's job). Then Geode → Bog (primed with enriched diamond), and so on down the order.

### Per-tier filler blocks

Each tier's slime-in-a-bucket seed-chain recipe spends **4 of a tier-themed filler block** per step. The constraint: a tier's filler must be mass-attainable *at that tier* (not gated behind a later tier). The same per-tier filler carries into the Dissolution Chamber slime recipes (Cave=stone, Geode=gravel, Bog=mossy cobblestone, Tide=mycelium, Infernal=prismarine, Void=soul soil, all live).

| Tier | Filler block | Source |
|------|--------------|--------|
| Cave  | **stone** | smelted/farmed at Tier 1 |
| Geode | **gravel** | the Ex Deorum block you sieve gems from |
| Bog   | **mossy cobblestone** | crafted in Mekanism's Metallurgic Infuser / Enrichment Chamber (the Geode-era machines) |
| Tide  | **mycelium** | a Bog chain resource, mass-renewable via the Bog frog loop by Tier 4 |
| Infernal | **prismarine** | a Tide chain resource, mass-renewable via the Tide frog loop by Tier 5 |
| Void  | **soul soil** | an Infernal chain resource, mass-renewable via the Infernal frog loop by Tier 6 |

**Note on Tide's, Infernal's, and Void's fillers:** Cave/Geode/Bog fillers are all plain non-resource blocks. Tide's mycelium (a Bog chain resource), Infernal's prismarine (a Tide chain resource), and Void's soul soil (an Infernal chain resource) are the exceptions: each reuses a *prior* tier's mass-renewable chain output. Safe because that resource is fully produced before the tier in question, so there's no circular dependency. For Infernal the obvious nether-themed pick, netherrack, would be circular (you'd need netherrack to make the first netherrack slime), so prismarine is used; for Void the same logic rules out end stone, so soul soil is used.

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
- Infuse with ore primers → Iron → Copper → Gold → Coal → Glow Ink → Redstone Slimes (+ modded metals if those mods ship). (Lapis and diamond are Geode resources; obsidian is an Infernal variant as of PF 1.10.0.)
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
- **New verb:** **Just Dire Things tier-1 progression** + Building Gadgets 2 side branch (the `tools_and_things.snbt` chapter). Spine: Primogel Goo Block (mycelium-gated) -> Ferricore Ingot -> Fluid Collector -> Fluid Placer -> Item Collector (hexagon capstone). Optionals: Exchanging Gadget -> Copy/Paste Gadget (BG side). Mekanism RF from Geode powers the JDT machines.
- **Gate to Tier 4:** complete `bog_frogs` (capstone = pink_slime). That unlocks the `road_to_tide` chapter, which holds the Industrial Foregoing spine (Pity Machine Frame -> Fluid Extractor -> **Dissolution Chamber**, the pack's slime engine for the Cave/Geode/Bog/Tide chamber recipes; iron bootstraps off bone meal). The chapter then **bridges into Tide** as two converging paths: a **machine path** (Pity Machine Frame -> Fluid Extractor -> Dissolution Chamber) and a **frog path** (Tide frogspawn, Spawnery primed with pink_slime), meeting at the first **Prismarine slime** (made in the chamber), then a single tail: milk -> first **Prismarine Froglight** (capstone). **Tide and every later tier are Dissolution-Chamber-only** - there's no crafting-table slime chain (the chamber is already built by Tier 4). The rest of the aquatic chain (crystals, sponge, ink_sac, sea_pickle, nautilus_shell) is wired in the TIDE Dissolution rows and waits on the `drowned_riches` species chapter.

Estimated playtime: **3–5 hours**.

## Tier 4 — Tide (aquatic)

**Chapters:** *Drowned Riches* (the aquatic resource chain) + *Take Flight* (the jetpack verb). **Built.** Ocean materials without an ocean.

- Tide Frogs + Tide Slimes, Dissolution-Chamber only (no crafting-table chain from Tier 4 on).
- The roster: prismarine (in `road_to_tide`), then prismarine_crystals, sponge, ink_sac, sea_pickle, nautilus_shell in `drowned_riches`.
- **New verb:** jetpacks (Iron Jetpacks), the `take_flight` chapter - coil-tiered mobility (iron -> gold -> diamond -> emerald) on frog-farmed metals + Geode RF.
- **Gate to Tier 5:** the Nether expedition (the `road_to_infernal` gateway). Build a portal, fly the void Nether on your jetpack to a fortress, mine nether brick, and prime the Spawnery with it for the Infernal Frogspawn. The Tide mobility verb is the literal key to Infernal.

Estimated playtime: **3–6 hours**.

## Tier 5 — Infernal (nether)

**Chapters:** *Road to Infernal* (gateway) + *Infernal Frogs* (the nether resource chain) + *The Network* (the Refined Storage verb). **Built.** The Nether without a Nether - the Infernal frog produces the materials a void skyblock otherwise can't reach.

- Infernal Frogs + Infernal Slimes, Dissolution-Chamber only (filler = prismarine, a Tide resource - netherrack would be circular).
- The roster: netherrack (in `road_to_infernal`), then obsidian (v0.5.0, the portal-stone partner), quartz, glowstone, soul_sand, soul_soil, blaze, **netherite_scrap** in `infernal_frogs`. Netherite is the vanilla-endgame capstone (kept in Infernal, not deferred to Void).
- **New verb:** **Refined Storage** (RS 2.0), the `the_network` chapter - the digital storage + autocrafting network (Quartz Enriched Iron -> Controller -> Grid -> Disk Drive -> External Storage -> Import/Export -> Crafting Grid -> Autocrafting). Gated on nether quartz, which only the Infernal frog produces.
- **Automation (PF 1.16):** the `terrarium` chapter - **The Terrarium**, a sealed 5x4x5 multiblock that runs the frog loop hands-off (Controller -> ceiling Sprinklers raining slimes -> Incubators raising frogs -> Hatch collecting Froglights). Recipe-gated on Infernal materials; the pack's first automation. Boss Slime Milk is rejected by the Controller - boss farming stays manual (see Trophy Pond).
- **Boss campaign (Trophy Pond):** off the Infernal capstone, the wither and dragon trophies (wither skull, nether star, dragon egg, dragon breath) become farmable via catalyst altars - their Slime Milk is toxic, so they stay hand-walled. Sits with the endgame (after Master Pond) but unlocks here.
- **Gate to Tier 6:** the **dragon expedition** (the `road_to_void` gateway). Farm ender pearls from dark-room endermen, craft 2 eyes of ender, and (since no stronghold generates on a void skyblock) bake Ex Deorum's **End Cake** - 3 buckets of milk (plain milk or any Slime Milk via the `#productivefrogs:slime_milk_buckets` tag), an egg between the 2 eyes, 3 wheat. Each of its 6 slices teleports the eater to the End. Slay the dragon. The Tide jetpack verb makes the void-island crossings feasible; the dragon kill gates the endgame. (Replaced the hand-built 12-frame End portal on 2026-06-05 - the frames-must-face-inward gotcha hard-blocked a player; CF #8041724.)

Estimated playtime: **6–10 hours**.

## Tier 6 — Void (end & endgame). Built.

**Chapters:** *Road to the Void* (the dragon expedition gateway) + *Void Frogs* (the End resource chain) + *The Ultimate Table* (the Extended Crafting verb) + *Master Pond* (the singularity endgame). **Built.** The End without a stronghold, and a frog for every resource in the game.

- Void Frogs + Void Slimes, Dissolution-Chamber only (filler = soul soil, an Infernal resource - end stone would be circular).
- The roster: **ender_pearl** (in `road_to_void`), then end_stone, chorus_fruit, echo_shard, sculk, **shulker_shell** in `void_frogs`. Six vanilla End variants; the modded Void variants (Powah / Mystical Agriculture / Mythic Metals) stay deferred until those mods join the pack.
- **New verb:** **Extended Crafting**, the `the_ultimate_table` chapter - black iron -> luminessence -> basic/advanced/elite/ultimate tables -> the Quantum Compressor.
- **Endgame (`master_pond`):** one **Singularity** per vanilla froglight resource - **57 today** (the 59-variant vanilla roster minus the water/lava fluid pair, which is excluded; the count grows with PF's roster) - each compressed in the Quantum Compressor from 1000 of that resource (a proof you automated *every* farm). Fold them all into the **Ultimate Singularity** -> the **Sky Frogs Master Frog** trophy + a closing epilogue. The Master Frog is a KubeJS-defined item (placeholder texture; final art is a backlog item). The singularity JSONs are generated by `tools/gen_singularities.py` from PF's `slime_variant` data. (The compressor input is the smelted resource, not the Froglight directly: EC's singularity ingredient and the compressor's Cucumber input are both item/tag-only and cannot match a froglight's `slime_variant` component; on this skyblock each resource has no source but its frog, so every singularity is still froglight-gated.)

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
| Tier 3: Bog          | Road to Bog, Bog Frogs, Tools and Things (organics + JDT tier-1 progression / Building Gadgets) |
| Tier 4: Tide         | Road to Tide, Drowned Riches, Take Flight (aquatic resources + Iron Jetpacks mobility) |
| Tier 5: Infernal     | Road to Infernal, Infernal Frogs, The Network (Refined Storage), The Terrarium (PF 1.16 automation multiblock) |
| Tier 6: Void         | Road to the Void, Void Frogs, The Ultimate Table (end resources + Extended Crafting) |
| Master Pond          | Endgame singularity loop -> the Sky Frogs Master Frog trophy |
| Trophy Pond          | The boss campaign (wither + dragon trophies via catalyst altars), after Master Pond |
| Completionist        | The Whole Pond (vanilla census) + Sister Ponds (modded census) |
