# Mod List

> **Status:** DRAFT — non-canonical. The mod choices below are exploratory candidates. Many were seeded from inspecting Sky Bees Reborn's pack; that's a data point, not a vote. Expect this list to be cut hard and reshaped before v0.1 — the question isn't "what would SBR ship?" but "what does *this* pack need to feel like itself?"

This document captures **candidate mod categories and what they'd be for**, with potential mods per slot. Concrete version pins land in `pack.toml` once packwiz is wired up.

## Selection criteria

Every mod ships for one of three reasons:

1. **Frog mechanic dependency** — the mod IS or feeds the central loop (e.g. Productive Frogs itself, Ex Deorum for lava-handling + second water source).
2. **Tier supplier** — provides a category of resources that frogs will farm via Resource Slimes (e.g. Mekanism = osmium/uranium/fluorite Bog+Geode slimes).
3. **Infrastructure** — skyblock fundamentals (worldgen, water source, item logistics) or unavoidable QoL (JEI, Jade, FTB Library family).

Any mod that fails all three is rejected.

## Categories

### 1. Frog mechanic (load-bearing core)

| Mod                   | Role                                                                 | Notes                                                |
|-----------------------|----------------------------------------------------------------------|------------------------------------------------------|
| **Productive Frogs**  | The mod the pack is built around                                     | Published on CurseForge (1.21.1 / NeoForge). Pinned at v1.0.1 in the pack. |

### 2. Skyblock fundamentals

| Mod                   | Role                                                                 | Notes                                                |
|-----------------------|----------------------------------------------------------------------|------------------------------------------------------|
| **Skyblock Builder**  | Void worldgen + starting island template + per-player island UI      | 1.21.1 (`21.1.29`). No 1.21.4+ builds exist — partial reason pack is pinned to 1.21.1. |
| **Ex Deorum**         | Porcelain bucket, crucibles, barrels — lava-safe early bucket, leaves→lava crucible, **rain-collection barrels for second water source** (needed to bootstrap an infinite water source). **No sieving** — sieve recipes + meshes are KubeJS-disabled in `anti.js`. |
| **Forgiving Void**    | Don't die instantly from falling off your island                     | Quality-of-life — strongly preferred for skyblock    |

### 3. Tier suppliers — the resources frogs farm

Each entry here directly maps to one or more PF category slime variants (see [`progression.md`](./progression.md) for the full mapping).

| Mod                   | Resources it adds that frogs will farm                                | PF categories supplied                                |
|-----------------------|------------------------------------------------------------------------|-------------------------------------------------------|
| **Mekanism**          | Osmium, tin, lead, uranium, fluorite, refined glowstone               | Bog, Cave, Geode                                      |
| **Mekanism Generators** | Renewable power infrastructure                                       | (Infrastructure, not a tier supplier itself)          |
| **Mekanism Tools**    | Tier-specific tools using Mekanism alloys                              | Tool sink for Bog + Geode outputs                     |
| **Immersive Engineering** | Hop graphite coke, copper, aluminum, silver, nickel, uranium      | Bog, Cave                                             |
| **Industrial Foregoing** | Latex, pink slime, biofuel, ether gas                              | Tide (pink slime is a great Resource Slime parent)    |
| **Powah!**            | Uraninite, niotic crystal, energizing orb resources                    | Cave, Void                                            |
| **Ender IO**          | Vibrant alloy components, capacitors, glite                            | Void (advanced)                                       |
| **Applied Energistics 2** + **AE2 Things** + **Advanced AE** + **ExtendedAE** + **MegaCells** + **Applied Mekanistics** + **AppliedFlux** + **ae2wtlib** + **ae2importexportcard** + **ae2jeiintegration** + **soulplied_energistics** | Storage logistics + certus quartz, fluix, sky stone | Geode (certus, fluix), Void (sky stone) |
| **Extended Crafting** | Singularities + ultimate singularity (endgame sink)                    | Endgame                                               |
| **Productive Metalworks** | Smeltery-line alloys                                                | Tier processing (smelting Froglights → ingots, melting alloys) |
| **Silent Gear** + **Silent Lib** + **sgearmetalworks** | Modular tools — accepts modded mats         | Tool sink across all tiers                            |
| **Actually Additions** | Wide grab-bag — black quartz, crystals, lens of the miner (DISABLED) | Cave, Geode; lens-of-the-miner is KubeJS-disabled     |
| **RFTools Base/Builder/Storage/Utility** | Quark, infused diamond, dimensional shards          | Void                                                  |
| **Hostile Neural Networks** | Predict mob loot via simulation                                  | Endgame mob-drop substitution path                    |
| **Apothic Spawners** + **Apothic Enchanting** + **Apothic Attributes** | Spawner manipulation + enchanting + RPG attributes | Mob-drop side path |

### 4. Power, logistics, storage

| Mod                   | Role                                                                  |
|-----------------------|------------------------------------------------------------------------|
| **Flux Networks**     | Wireless power transport — keeps the build tidy                       |
| **Pipez**             | Cheap pipes for early-game item/fluid transfer                        |
| **Modular Routers**   | Item routing                                                          |
| **Super Factory Manager** | Programmable factory automation (endgame)                          |
| **XNet** + **XNetGases** | Channeled item/fluid/gas transport                                 |
| **LaserIO**           | Compact laser-based item transport                                    |
| **Functional Storage** | Drawer storage                                                       |
| **Sophisticated Backpacks** + **Sophisticated Storage** + **Sophisticated Core** | Upgraded backpacks + barrels  |
| **DimStorage**        | Cross-dimensional storage                                             |
| **Iron Furnaces**     | Tiered furnaces — needed for fast Froglight smelting                  |

### 5. Quality of life & UX

| Mod                   | Role                                                                  |
|-----------------------|------------------------------------------------------------------------|
| **JEI**               | Recipe browser — non-negotiable                                       |
| **Jade**              | In-world block info HUD                                               |
| **Mek Jade Upgrade**  | Show Mekanism multiblock info in Jade                                 |
| **FTB Library**       | Required for FTB Quests / FTB Chunks / etc.                           |
| **FTB Quests**        | The questbook                                                         |
| **FTB Chunks**        | Chunk claiming + minimap                                              |
| **FTB Teams**         | Team / party system                                                   |
| **FTB Ultimine**      | Hold a key to mine veins (mostly cosmetic in this pack)               |
| **FTB Essentials**    | /home, /tpa, etc.                                                     |
| **FTB Ranks**         | Server-side permission ranks                                          |
| **FTB Filter System** | Smart item filters in routers/AE                                      |
| **Waystones**         | Teleportation network                                                 |
| **Easy Villagers**    | Trade with villagers from blocks (no need for trading halls)          |
| **Farmer's Delight** + **Cooking for Blockheads** + **Croptopia** + **Farmer's Croptopia** + **Farming for Blockheads** + **Right Click Harvest** + **Squat Grow** | Skyblock food economy   |
| **Mouse Tweaks** + **Inventory Tweaks** + **Crafting Tweaks** + **Polymorph** | Inventory ergonomics                              |
| **Trash Slot** + **Trash Cans** | Discard items                                              |
| **Just Enough Mekanism Multiblocks** | Visual multiblock previews                                    |
| **Searchables**, **Controlling**, **Configured**, **Jamlib**, **YACL** | Settings UX                                |
| **Tips Mod**          | Loading-screen tips (custom Sky Frogs tips — TBD)                     |
| **Patchouli** + **Guideme** | In-game manuals (used by many of the above mods)                   |
| **Bookshelf**, **Placebo**, **Cucumber**, **Resourceful Lib**, **LibX**, **Nirvana Lib**, **Konkrete**, **EpheroLib**, **EdivadLib**, **mcjtylib**, **Titanium**, **SuperMartijn642 Core/Config Lib**, **PolyLib**, **SilentLib**, **Curios**, **CodeChickenLib**, **Architectury**, **GeckoLib**, **Balm**, **Common Networking**, **Athena**, **Fusion**, **Moonlight**, **Cloth Config**, **Fzzy Config**, **JamLib**, **JustDireThings** | Required libraries / coremods |

### 6. Visuals & decoration

| Mod                   | Role                                                                  |
|-----------------------|------------------------------------------------------------------------|
| **Chipped** + **Rechiseled** + **Rechiseled Chipped** | Variants of blocks for builders                  |
| **FramedBlocks**      | Camouflage-able blocks                                                |
| **Handcrafted**       | Decorative furniture                                                  |
| **Supplementaries**   | Decoration grab-bag (also some functional items)                      |
| **Glassential**       | Light-passing glass variants                                          |
| **Simply Light** + **Mcw Lights**  | Light blocks                                            |
| **Colorful Hearts**   | Per-effect heart colors                                               |
| **Nyctography**       | Aesthetic darkness                                                    |
| **Showcase Item**     | Display items as pedestals                                            |
| **Construction Sticks** | Quick build sticks                                                  |
| **Building Gadgets 2** | Larger build tools                                                   |

### 7. Performance & system

| Mod                   | Role                                                                  |
|-----------------------|------------------------------------------------------------------------|
| **Lithium**           | Server-side performance — game logic optimization                    |
| **FerriteCore**       | Memory savings                                                       |
| **ModernFix**         | Startup + runtime mixins                                             |
| **Clumps**            | Combine XP orbs                                                       |
| **Fast Leaf Decay**   | Reduce tick load from decaying leaves                                 |
| **NoChatReports**     | Strip chat reporting capability — server-tuning preference            |
| **NeoAuth**           | Local-auth helper for offline launchers                               |
| **Pylons** + **Trenzalore**  | Server housekeeping                                            |

### 8. Mods we are NOT shipping (and why)

| Mod                   | Why excluded                                                          |
|-----------------------|------------------------------------------------------------------------|
| **Productive Bees**   | Direct conflict with the pack's identity — frogs replace bees here    |
| **Resourceful Bees**  | Same reason                                                           |
| **Create**            | Powerful but very high learning cost; redundant with Mekanism + IE for our needs. Reconsider for v1.x. |
| **Botania**           | Beautiful but its progression is its own pillar; doesn't slot into a frog tier. Reconsider for v1.x with custom quests. |
| **Blood Magic**       | Same — strong progression that would dwarf the frog loop              |
| **Quark**             | Overlaps with many of our QoL choices; risk of feature bloat          |
| **Twilight Forest** / other dimensional adventure mods | We want the player on their skyblock, not exploring a new dimension. End remains the only adventure dimension. |

This list will shift as we playtest. Anything moved into or out of the pack needs a corresponding KubeJS-overrides and quest-book update.

## Open questions

- Do we ship **Create**? It would supplant several lower-tier processing roles and add transport delight, but it's a big mod with a steep learning curve. Defer to v1.x.
- Do we ship **JourneyMap** vs FTB Chunks' built-in minimap? Both is overkill; one must go.
- **Modular Bees** is in the SBR mod list — do we want **Modular Frogs** equivalent if one exists? (Unlikely on 1.21.1 — none observed.) Track as a stretch goal in [`backlog.md`](./backlog.md).
- **Hostile Neural Networks** is interesting but partially overlaps the frog loop's "predictable resource generation" identity. Include but gate quests behind late-tier so it feels like a parallel side path, not a frog replacement.
