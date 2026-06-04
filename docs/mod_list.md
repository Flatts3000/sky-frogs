# Mod List

> **Status:** PARTIAL DRAFT. The Tier 0-3 mod stack is **shipped and pinned** in `pack/mods/*.pw.toml` (Productive Frogs, Mekanism family, Industrial Foregoing family, Ex Deorum, Cobblegen Galore, ATO, the FTB/QoL utility stack). The rest of this list is still **candidate** framing for Tier 4-6 and beyond - expect it to be cut and reshaped. Entries are tagged **SHIPPED** where they're pinned in the pack today.

This document captures both the shipped Tier 0-3 stack and the **candidate mod categories** for later tiers. Concrete version pins live in `pack/mods/*.pw.toml`.

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
| **Productive Frogs**  | The mod the pack is built around                                     | Published on CurseForge (1.21.1 / NeoForge). Pinned at **v1.8.0** (organic Bog roster + IF plastic/pink_slime variants, per-variant Slime Milk). |

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
| **Mekanism** (SHIPPED) | Osmium, steel; Metallurgic Infuser + Enrichment Chamber             | **Geode-tier automation verb** (power, infuser, enrichment). Osmium is the Cave->Mekanism bootstrap (`osmium_slime_bucket.js`); steel via the infuser (`steel_slime_infusing.js`). |
| **Mekanism Generators** (SHIPPED) | Renewable power infrastructure                            | Part of the Geode automation verb (power for the machines above) |
| **Mekanism Tools** (SHIPPED) | Tier-specific tools using Mekanism alloys                     | Tool sink for Cave + Geode outputs                    |
| **ATO - All the Ores** (SHIPPED) | Cross-mod ore set (osmium etc.)                                | Cave. PF's osmium `slime_variant` is gated on ATO being loaded; supplies the osmium the Mekanism bootstrap primes. |
| **Cobblegen Galore** (SHIPPED) | Configurable block generators (cobblestone -> gravel hammer path) | Infrastructure. Source of the **Geode gravel filler** for the seed-chains (alongside Ex Deorum). |
| **Immersive Engineering** | Hop graphite coke, copper, aluminum, silver, nickel, uranium      | Bog, Cave (candidate)                                 |
| **Industrial Foregoing** + **Industrial Foregoing Souls** (SHIPPED) | Latex, plastic, pink slime, biofuel       | **Bog-tier verb.** Plastic is hard-gated behind the Bog plastic-frog (`if_plastic_gate.js`); pink_slime is the **Bog capstone** (`bog_slime_chain.js`), not Tide. |
| **Powah!**            | Uraninite, niotic crystal, energizing orb resources                    | Cave, Void                                            |
| **Ender IO**          | Vibrant alloy components, capacitors, glite                            | Void (advanced)                                       |
| **Applied Energistics 2** + **AE2 Things** + **Advanced AE** + **ExtendedAE** + **MegaCells** + **Applied Mekanistics** + **AppliedFlux** + **ae2wtlib** + **ae2importexportcard** + **ae2jeiintegration** + **soulplied_energistics** | Storage logistics + certus quartz, fluix, sky stone | Geode (certus, fluix), Void (sky stone) |
| **Extended Crafting** (SHIPPED, 7.0.8) | Tiered crafting tables + Quantum Compressor + froglight Singularities + Ultimate Singularity | **Void-tier verb** (`the_ultimate_table.snbt`) + the Master Pond endgame: each species' Froglight compresses 1000:1 into a Singularity (a proof-of-automation gate), six -> the Ultimate Singularity -> the Master Frog trophy. |
| **Productive Metalworks** | Smeltery-line alloys                                                | Tier processing (smelting Froglights → ingots, melting alloys) |
| **Silent Gear** + **Silent Lib** + **sgearmetalworks** | Modular tools — accepts modded mats         | Tool sink across all tiers                            |
| **Actually Additions** | Wide grab-bag — black quartz, crystals                                | Cave, Geode (candidate; NOT currently in the pack). The mining-shortcut disable that actually ships is the Mekanism Digital Miner in `anti.js`, not AA's lens of the miner (AA isn't pinned). |
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
| **Sophisticated Backpacks** + **Sophisticated Storage** + **Sophisticated Core** (SHIPPED) | Upgraded backpacks + barrels. Sophisticated Storage pinned at `1.5.52.1756`. Its controller recipe is re-issued quartz-free in `storage_quartz_free.js` so the analog network is a Cave-era stopgap. |
| **DimStorage**        | Cross-dimensional storage                                             |
| **Refined Storage** (core 2.0.8) + addons: **Extra Storage**, **Extra Disks**, **RS Curios / Mekanism / JEI Integration**, **RS Quartz Arsenal** (+ EdivadLib dep) (SHIPPED) | The digital storage network - the **Tier 5 (Infernal) verb**. Naturally gated: RS components need Quartz Enriched Iron (quartz), which is Infernal-only, so it stays locked until the Infernal frog produces quartz. The Mekanism integration ties it to the Geode-tier power. The ATM10 RS set. |
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
| **FTB Filter System** (SHIPPED) | Smart item filters in routers/AE; also backs the questbook's tag-based tasks (the Steel quest uses `item_tag(c:ingots/steel)` via `ftbfiltersystem:smart_filter`)                                      |
| **Waystones**         | Teleportation network                                                 |
| **Easy Villagers**    | Trade with villagers from blocks (no need for trading halls)          |
| **AppleSkin** (SHIPPED) | Saturation + exact food-value overlay on the HUD and item tooltips (client-side QoL) |
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
| **Chipped** + **Rechiseled** + **Rechiseled: Chipped** | Hundreds of decorative variants per base block (frog-farmed stone/dirt/etc. -> build blocks) |
| **Chisel Reborn** + **Chisel-Chipped Integration** | Classic in-world chiseling, bridged into the Chipped catalog          |
| **FramedBlocks**      | Camouflage / "framed" blocks (slabs, slopes, panes textured with any block)          |
| **Handcrafted**       | Furniture proper (chairs, tables, benches, shelves, dishware)                         |
| **Supplementaries**   | Decoration grab-bag (signs, lamps, planters, faucets; some functional)               |
| **Macaw's** suite (10 mods) | Bridges, Doors, Windows, Roofs, Fences & Walls, Trapdoors, Paths & Pavings, Lights & Lamps, Paintings, Furniture - the workhorse build-decor set |
| **Connected Glass** + **Glassential** | Seamless/decorative glass; light-passing and one-way variants         |
| **CTM** + **Fusion**  | Connected-textures libraries powering the chisel/variant mods (deps: Athena, Moonlight, Resourceful Lib, Cryonic Config) |
| **Colorful Hearts**   | Per-effect heart colors                                               |
| **Nyctography**       | Aesthetic darkness                                                    |
| **Showcase Item**     | Display items as pedestals                                            |
| **Construction Sticks** | Quick build sticks                                                  |
| **Building Gadgets 2** | Larger build tools                                                   |
| **Iron Jetpacks**     | Tiered, FE-charged jetpacks - the **Tide-tier mobility verb** (`take_flight`) |
| **Cucumber Library**  | Library dependency of Iron Jetpacks                                  |

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
