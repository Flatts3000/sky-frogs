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
| **Productive Frogs**  | The mod the pack is built around                                     | Published on CurseForge (1.21.1 / NeoForge). Pinned at **v1.11.0** (Flux Networks + full Powah compat, blaze rod resource; full bump history in [`pf_pin_history.md`](./pf_pin_history.md)). |

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
| **Cobblegen Galore** (SHIPPED) | Configurable block generators (cobblestone -> gravel hammer path) | Infrastructure. Source of the **Geode gravel filler** for the seed-chains (alongside Ex Deorum). **Curated per the #90 ruling** (`cobblegen_curation.js`): default-deny - only the seven builders' stone generators survive; netherrack/obsidian/tuff (frog resources) and any future blockgen additions are stripped. |
| **Immersive Engineering** | Hop graphite coke, copper, aluminum, silver, nickel, uranium      | Bog, Cave (candidate)                                 |
| **Opolis Utilities / BBL Utility** (SHIPPED 2026-06-06, pinned 4.11.10 + BBL Core) | Drying/Soaking Tables, Cloche, Item Repairer, Home/Death Stones, Breaker/Placer/Clicker, curated Resource Generator | **Curated per the six #85 rulings** (`opolis_curation.js`): Resource Generator = builders' stone lane (only stones no frog produces); Fluid Generator, Catalogue/B-Bucks economy, and glow_squid/squid summons stripped; Clicker + Ender Ore kept as shipped. |
| **Industrial Foregoing** + **Industrial Foregoing Souls** (SHIPPED) | Latex, plastic, pink slime, biofuel; Soul Surges (Warden) | **Bog-tier verb.** Plastic is hard-gated behind the Bog plastic-frog (`if_plastic_gate.js`); pink_slime is the **Bog capstone** (`bog_slime_chain.js`), not Tide. **Souls** was dropped 2026-06-06 as dead content, then re-added once a Discord member's correction proved the Warden reachable: Ex Deorum's Sculk Core + the pack's `kubejs:void/sculk_shrieker` recipe (frog-farmed sculk/echo shards/bone block) complete the chain (#75, #82). |
| **Powah! (Rearchitected)** (SHIPPED 2026-06-06, 6.2.8 per ATM10SKY + GuideME dep) | Tiered FE generation (Furnator -> Reactor), Energizing Orb, Energy Cells, Ender Network | The **power-scaling arc** alongside Mekanism's Geode verb. PF 1.11 farms all 7 Powah materials: uraninite + energized_steel (Cave), dry_ice (Tide), blazing (Infernal), niotic/spirited/nitro (Void). Skyblock bootstrap: no ore gen, so the Cave pool's **split-discovery** rolls the first uraninite - the frog IS the uranium mine. Energizing Orb outputs screened: all mod-internal, no frog resources, no fluid gen. Questing deferred with the other modded variants. (#105) |
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
| **Flux Networks** (SHIPPED 2026-06-06, 8.0.0 per ATM10SKY) | Wireless power transport — keeps the build tidy. PF 1.11 farms `flux_dust` (Infernal, shares obsidian's tier - dust is born from redstone dropped on obsidian, which doubles as the in-world bootstrap). Recipe outputs screened: all `fluxnetworks:` internal. Questing deferred with the other modded variants. (#84) |
| **Pipez**             | Cheap pipes for early-game item/fluid transfer                        |
| **Cable Facades** (SHIPPED 2026-06-06, 1.5.1 per Techopolis/Skyopolis) | Wrap pipes/cables in any block's texture - machine rooms read as builds, not spaghetti. Default allowlist already covers Pipez + the Mekanism cable family; pure decor (facade = dyes + wool, wrench = iron). (#100, suggested by Dergib on Discord) |
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
| **FTB Filter System** (SHIPPED) | Smart item filters in routers/AE; available for questbook tag-based tasks (`ftbfiltersystem:smart_filter`), though no quest uses one today                                      |
| **Waystones**         | Teleportation network                                                 |
| **Easy Villagers**    | Trade with villagers from blocks (no need for trading halls)          |
| **AppleSkin** (SHIPPED) | Saturation + exact food-value overlay on the HUD and item tooltips (client-side QoL) |
| **Extreme Sound Muffler** (SHIPPED 2026-06-06, 3.55 per ATM10SKY; client-side) | Per-sound muffling - toggle individual sounds globally or via radius anchors. The frog-farm answer: deafen the plap plaps, keep everything else. Unanimous precedent (all 5 local reference packs ship it). Default config on purpose - muffling stays opt-in for players who like the frogs audible. (#103, suggested by Dergib on Discord) |
| **GraveStone Mod** (SHIPPED 2026-06-06, 1.0.24 per Techopolis/Skyopolis) | Grave at your death point holding items + XP, obituary paper; ghost spawning off by default. Chosen over Corail Tombstone (whose perk/teleport progression conflicts with the pack's no-parallel-economy rulings). Complements FTB Essentials /back. (#92, requested by RayRayZCB on Discord) |
| **Fast Leaf Decay** (SHIPPED) | Leaves break/fall quickly once supporting logs are removed - QoL for tree farms (tree-felling itself is handled by FTB Ultimine) |
| **Torchmaster** (SHIPPED 2026-06-07, 21.1.9) | Mega Torch blocks hostile natural spawns in radius - skyblock islands are spawn surfaces by design. CRITICAL pack config: PF's species slimes are monster-category natural spawns (the Tier 0 swamp cave_slime farm), so `config/torchmaster.toml` exempts all `productivefrogs:*` slimes from the torch - it kills the creepers and leaves the economy alone. (#134, suggested by Dergib on Discord) |
| **More Dragon Eggs** (SHIPPED 2026-06-07, 5.0, per ATM10SKY) | Every dragon kill drops a Dragon Egg (vanilla: once per world, ever). Load-bearing for Trophy Pond's Egg altar: six Dragon Egg Catalysts cost six eggs, which vanilla math can never pay. Mixin-only, MIT, by Darkere (ATM team). |
| **Farmer's Delight** + **Cooking for Blockheads** + **Croptopia** + **Farmer's Croptopia** + **Farming for Blockheads** + **Right Click Harvest** + **Squat Grow** | Skyblock food economy   |
| **Botany Pots** (SHIPPED, 21.1.42) + **Botany Trees** (SHIPPED 2026-06-06, 21.1.3 per ATM10SKY) | Self-tending planters for crops/flowers (quested in Scaling the Colony); the Trees addon makes them grow trees too - base Botany Pots never did, despite the natural assumption (#96, reported by Dergib on Discord). Wood is open economy: no frog resource, no gate touched. |
| **Mouse Tweaks** + **Inventory Tweaks** + **Crafting Tweaks** + **Polymorph** + **Inventory Essentials** (SHIPPED 2026-06-06, 21.1.2 per Techopolis/OceanBlock 2; ctrl-shift-click bulk transfers, Discord suggestion #88) | Inventory ergonomics                              |
| **Trash Slot** + **Trash Cans** | Discard items                                              |
| **Just Enough Mekanism Multiblocks** | Visual multiblock previews                                    |
| **Searchables**, **Controlling**, **Configured** (SHIPPED 2026-06-06, pinned 2.6.3 per ATM10SKY; in-game config editing, Discord suggestion #74), **JamLib**, **YACL** | Settings UX                                |
| **Tips Mod**          | Loading-screen tips (custom Sky Frogs tips — TBD)                     |
| **Patchouli** + **Guideme** | In-game manuals (used by many of the above mods)                   |
| **Bookshelf**, **Placebo**, **Cucumber**, **Resourceful Lib**, **LibX**, **Nirvana Lib**, **Konkrete**, **EpheroLib**, **EdivadLib**, **mcjtylib**, **Titanium**, **SuperMartijn642 Core/Config Lib**, **PolyLib**, **SilentLib**, **Curios**, **CodeChickenLib**, **Architectury**, **GeckoLib**, **Balm**, **Common Networking**, **Athena**, **Fusion**, **Moonlight**, **Cloth Config**, **Fzzy Config**, **JamLib**, **JustDireThings** | Required libraries / coremods |

### 6. Visuals & decoration

| Mod                   | Role                                                                  |
|-----------------------|------------------------------------------------------------------------|
| **Chipped** + **Rechiseled** + **Rechiseled: Chipped** | Hundreds of decorative variants per base block (frog-farmed stone/dirt/etc. -> build blocks) |
| **Chisel Reborn** + **Chisel-Chipped Integration** | Classic in-world chiseling, bridged into the Chipped catalog          |
| **FramedBlocks**      | Camouflage / "framed" blocks (slabs, slopes, panes textured with any block)          |
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
| **Sodium** (SHIPPED 2026-06-06) | Client rendering performance + better video settings UI. Pinned 0.6.13 stable (the ATM10SKY build; latest CF file is an 0.8 alpha). Client-side only. Discord suggestion #73. |
| **FancyMenu** + **Konkrete** + **Melody** (SHIPPED 2026-06-06, 3.8.1 per ATM10SKY; client-side) | Branded title screen (#89): Discord + GitHub buttons live now; wordmark + void panorama slots wired, awaiting art. The frog splash pool ships separately as a vanilla asset override (`kubejs/assets/minecraft/texts/splashes.txt`). |
| **Lithium** (SHIPPED 2026-06-06)          | Server-side performance — game logic optimization (0.15.3, per ATM10SKY)  |
| **FerriteCore** (SHIPPED 2026-06-06)      | Memory savings (7.0.3, per ATM10SKY)                                 |
| **ModernFix** (SHIPPED 2026-06-06)        | Startup + runtime mixins (5.27.11)                                   |
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
| **Handcrafted** | Dropped 2026-06-05 - its cupboard recipes collide with Functional Storage drawers, and the alternate-craft picker doesn't surface in Refined Storage, so drawers couldn't be autocrafted (#62). Removed rather than chase the recipe-conflict resolution. Reconsider if the conflict is resolvable upstream. |
| ~~**Industrial Foregoing Souls**~~ (RE-ADDED 2026-06-06) | Dropped 2026-06-06 as dead content (#75: no Warden path was believed to exist), then a Discord member's correction proved otherwise - Ex Deorum's Sculk Core makes placed shriekers summon-capable; the pack only lacked a shrieker source (its Ex Deorum drop lives in the disabled netherite-mesh sieve lane). Re-added with a curated shrieker recipe; the chain is frog-farmable at Tier 6 (#82). A "Wake the Warden" quest branch is the open follow-up. |

This list will shift as we playtest. Anything moved into or out of the pack needs a corresponding KubeJS-overrides and quest-book update.

## Open questions

- Do we ship **Create**? It would supplant several lower-tier processing roles and add transport delight, but it's a big mod with a steep learning curve. Defer to v1.x.
- Do we ship **JourneyMap** vs FTB Chunks' built-in minimap? Both is overkill; one must go.
- **Modular Bees** is in the SBR mod list — do we want **Modular Frogs** equivalent if one exists? (Unlikely on 1.21.1 — none observed.) Track as a stretch goal in [`backlog.md`](./backlog.md).
- **Hostile Neural Networks** is interesting but partially overlaps the frog loop's "predictable resource generation" identity. Include but gate quests behind late-tier so it feels like a parallel side path, not a frog replacement.
