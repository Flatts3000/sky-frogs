# Changelog

Follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) and [SemVer](https://semver.org/spec/v2.0.0.html). World-breaking changes are called out at the top of the affected release and bump the major version post-1.0.

## [Unreleased]

### Fixed

- **The Rainbow Slime can be made now.** v1.8.0 said frogs make dye, and they
  did not: there was no way to get a Rainbow Slime in the first place. The only
  recipe for one was the Froglight smelt-back, which wants the Rainbow Froglight
  you would have needed the slime to produce. Productive Frogs' own answer is to
  show a dye to a wild Bog Slime, but this pack spawns Cave Slimes and nothing
  else, and priming refuses a slime of the wrong species, so that path was never
  open here. It now takes a dye in the Dissolution Chamber, the same way the
  Experience Slime takes a book. Reported by **monkeyhealz**.
- **The check that was supposed to catch that now covers every slime.** A
  validator has guarded against exactly this loop since #167, but it only looked
  at slimes belonging to another mod. The Rainbow Slime belongs to no mod and is
  not primed by a plain item either, so it fell out of the guard without a word,
  which is the same reason it went missing from both Completionist chapters when
  it arrived. The guard now asks whether a slime ships in the pack at all, and
  fails on any that has no way to be made.

## [1.8.0] - 2026-08-30

Frogs make dye now, and the seeds you were missing come out of mud.

### Added

- **Mud sifts into seeds.** Put mud in the oak sieve with a string mesh and you
  get the food mods' seeds: 58 seeds and saplings from Mama's Herbs and Harvest,
  plus Farmer's Delight's cabbage, tomato, onion and rice. None of them had a
  source before this. Both mods hand their seeds out through structure chests
  and wild crops, and a void skyblock generates neither, which is why the Good
  Food crate kept giving you dishes you had no way to cook. Mud is dirt and a
  water bottle, so the lane is open from day one. Each seed is a one-time find,
  since the grown crop drops its own seed. Suggested by **Seeker**, who had
  already built it as a datapack and handed it over, and backed by
  **Nic_Knack819**.
- **Berries and mushrooms sift from moss.** Checking that the seeds above
  actually covered every recipe turned up sweet berries and glow berries, which
  the pack had no way to get at all. Sweet berries now come off dirt and moss,
  glow berries off moss. Mushrooms join them on moss for a different reason:
  you could already get those, but only as a byproduct of turning a barrel of
  water into witch water with mycelium on top, which is not something you find
  without reading the mod's files. This was never only a cooking problem, it
  also blocked mushroom stew, rabbit stew, suspicious stew and growing any of
  them in a Botany Pot, since each of those wants a mushroom or a berry you
  already own.

### Changed

- **Twenty-six mods moved up, Productive Frogs among them.** Routine currency
  pass, nothing forced: JEI, KubeJS, FTB Quests and Teams, Sophisticated
  Core/Storage/Backpacks, Supplementaries and Moonlight, Sodium, ModernFix,
  Farmer's Delight, Mama's Herbs and Harvest, Titanium, Skyblock Builder,
  Torchmaster, Fusion, FancyMenu, Cable Tiers, Cable Facades, Apothic
  Enchanting, Crafting Tweaks, Construction Sticks, Inventory Essentials and
  GraveStone. Supplementaries takes the biggest step (3.8.10 to 3.9.6) and wants
  Moonlight 3.5.2, which came along in the same pass. The set was booted on a
  dedicated server before shipping: everything loaded, all 31 KubeJS server
  scripts ran, no failed recipes.
- **Productive Frogs 1.25.4 to 1.26.0, and there is a new frog product in it.**
  Show a dye to a slime and it turns Rainbow. A Bog Frog that eats one drops a
  Rainbow Froglight, and the shape you lay those out in on a crafting table
  decides which of the sixteen dyes you get - one on its own is white, two side
  by side is light gray, three in a row is red, on through the set. Every shape
  pays the same per Froglight, so the deep colours are not a worse deal, they
  just arrive in bigger batches: one Froglight is eight dye, two is sixteen,
  three is twenty-four. JEI lists all sixteen shapes. There is one crafting
  recipe for it on the pack side, the usual Rainbow Froglight to Slime in a
  Bucket, on mossy cobblestone like the rest of the Bog chain.
- **The Rainbow Froglight gets no Singularity.** Every other Froglight smelts
  down to one item, which is the thing the Quantum Compressor asks a thousand of.
  This one does not smelt at all - it crafts into dyes - so there is nothing to
  compress and it stays out. Same call as water and lava. It is out of the
  Completionist census for now too, which is a decision that can go the other
  way later.
- Productive Frogs also tidied the Virtual Terrarium's window: the frog in the
  dome is now drawn in its own species colour, with a slime beside it in the
  colour of whatever it is currently eating, and no slime when it is idle. A
  glance at the glass now tells you what the machine is and whether it is
  running.

## [1.7.0] - 2026-08-16

Shaders load now, and the mod list is current again.

### Added

- **Shaders work now.** The pack ships Iris, so the Shader Packs button is in
  Video Settings and anything you drop in `shaderpacks/` will load. No shader
  pack comes with the pack, pick your own. It is client-side, so nobody on a
  server has to install anything. Asked for on Discord by **kenny7** and
  **Nferno**, and **Seeker** had already tried it against the pack with
  Complementary Reimagined and reported back that it worked.

### Changed

- Fourteen mods brought up to current: FTB Quests, JEI, Supplementaries,
  Moonlight Lib, Balm, LibX, FancyMenu, FTB XMod Compat, Construction Sticks,
  SuperMartijn642's Core Lib, Trash Cans, and the Sophisticated Core /
  Backpacks / Storage set. Trash Cans is the one you will notice: its screen
  now has a tab holding the last six things you threw away, so a misclick is
  recoverable. Sodium stays on 0.8.12 again, the newer build is still a beta
  and the renderer is not worth the gamble.

## [1.6.2] - 2026-08-09

Iron Furnaces stops eating your Froglights, in both of the ways it was doing it.

### Fixed

- **Iron Furnaces takes your Froglights again.** Some players found that no
  Froglight would go into an Iron Furnace at all, by hand or by pipe, while a
  vanilla furnace took them fine, and that restarting the game fixed it until it
  came back. Iron Furnaces remembers whether an item can be smelted in a list
  keyed by the item, and every Froglight variant is the same item, so the first
  Froglight a furnace ever saw decided the answer for all of them until the game
  closed. A Froglight with no variant on it, the kind a Copy-Paste Gadget makes,
  has nothing to smelt into, and one of those was enough to lock out every other
  Froglight for the rest of the session. Froglights are now asked about one at a
  time. Reported on CurseForge by **user_qqgd4audept0i3qy**, **Larronos** and
  **user_w647p447peuez0hl**, and on Discord by more people than we can list.
- **Iron Furnaces no longer turns one Froglight variant into another.** If you
  ran Froglights through a factory Iron Furnace with **auto-split** switched on,
  the furnace treated every Froglight as the same item and levelled the counts
  across its input slots. Each slot kept its own variant, so a furnace holding
  64 of one Froglight and 1 of another came out holding 32 and 33. Your total
  never changed, which is why nothing ever looked wrong; what changed was which
  variant you owned. It has been in the pack since v1.4.3, and it ran on its
  own, in either direction - you could lose a stack of Nether Star Froglights or
  mint one. Anything storing its identity the way a Froglight does was affected
  the same way. This is Iron Furnaces' bug, reported to them and still open, so
  the fix ships in Productive Frogs instead: slots are now matched on variant as
  well as item. A furnace holding one variant behaves exactly as it always did.
  Thanks to **abyssquidd** (#225) and **millllehzh** (#220) for the reports.
- **Slimes appear in the pen with your frogs instead of on top of its wall.** A
  Slime Milk source looked for something solid beside it and put the slime
  there, so in any pen with a wall or a raised rim next to the milk, slimes
  landed outside the enclosure, out of reach of the frogs, and could hop away.
- **A milk source spreads its slimes around the pool** instead of stacking every
  one of them in the same square, and will not drop them over open air, so a
  pool built out over a ledge stops feeding slimes to the void.

### Changed

- Productive Frogs 1.25.2 -> **1.25.4**, which carries all three fixes above:
  1.25.3 ("Sorting It Out") for the auto-split variant swap and the two Slime
  Milk placement fixes, 1.25.4 ("Second Opinion") for the furnace that refused
  Froglights until a restart. (Corrected 2026-08-16: this line originally read
  "-> 1.25.3", but the tag shipped 1.25.4.)
- Nine other mods brought up to current: FTB Quests, Skyblock Builder,
  Moonlight Lib, JEI, Jade, SuperMartijn642's Core Lib, and the Sophisticated
  Core / Backpacks / Storage set. Sodium stays on 0.8.12; its newer build is a
  beta, and the renderer is not something to ship untested.

## [1.6.1] - 2026-08-06

A hotfix for the mod that builds the island, and six others brought up to current.

### Fixed

- **Skyblock Builder can make an island again.** v1.6.0 shipped Skyblock Builder 21.1.32, and that build broke island creation and could put you in the wrong dimension. It was the version's own regression, nothing pack-side, and 21.1.33 hotfixes both. If a world made on v1.6.0 came up wrong, the fix does not repair it: stop, delete the world folder, start again.

### Changed

- **7 mods updated to their current builds.** Skyblock Builder, the Sophisticated suite (Core, Storage, Backpacks), FTB Library, Supplementaries and Moonlight. Nothing changes about how the pack plays, and the loader pin is unchanged. Sodium stays on 0.8.12 for the same reason as last time: the newer build is a beta and the pack has no need of anything in it.

## [1.6.0] - 2026-08-03

Two new quests off the back of a week of Discord reports, a server that can no longer generate the wrong world, and drawers that finally compact the things frogs make most of.

### Added

- **The quest book introduces the field guide (#253).** Productive Frogs ships a book of its own, separate from the quest book, with a page for every frog, slime and appliance, and build previews that project the multiblocks into the world before you place anything. You have always been handed one on your first login, but nothing ever said so, and people were losing hours on the boss altars without knowing it was sitting in their inventory. An optional Welcome quest now names it, says what it is for, and hands out another copy if yours went missing. Both altar quests point at it for the build, and they also say plainly that Dragonsbane and Witherbane are frogs. (Reported by RastoMast and Wolley on Discord.)
- **An optional Bog quest for bees and honey (#255).** Honey has been reachable this whole time and nobody knew it, so the assumption took hold that the pack had no bees at all. Grow a birch sapling beside a flower, both of which come off the builders' sieve, and there is a chance the tree comes up with a bee nest already attached and bees inside. Silk Touch it home and you have honey, and honey blocks. The new quest is a checklist that walks the whole route. It is optional and nothing else waits on it.

### Fixed

- **A dedicated server always generates the skyblock now (#251).** The server pack has always shipped the right world type, but that setting lives in `server.properties`, and most hosting panels rewrite that file from their own control panel on every boot. Lose the line and you got an ordinary Minecraft world. Every world type in the pack now generates the skyblock, so there is nothing left to lose. One thing this cannot repair: a server that already made a normal world keeps it, because generation is decided once and never revisited. Stop it, delete the world folder, start again. (Reported by Robosapien on Discord.)
- **The Void quests no longer send you hunting a slime that does not exist (#252).** Two of them told you to prime a wild Void Slime. The pack switches off every wild slime spawn Productive Frogs adds, so there were none to find in any biome, and people went looking anyway. Both quests now describe the Dissolution Chamber route, which is the intended one and has always worked. (Reported by Shado on Discord.)
- **The Ferricore Ingot quest hands out the right drawer (#250).** It gave a Compacting Drawer, which holds three tiers: nugget, ingot, block. Ferricore has no nugget, so the third slot was dead space. It is a Simple Compacting Drawer now, matching every other two-form resource in the pack. The rest were checked while fixing it, and iron, gold, osmium, steel and ice were all already correct. (Reported by Incline on Discord.)
- **Honeycomb, clay, snowballs, magma cream and prismarine shards stack up in a compacting drawer.** A compacting drawer works out its own tiers by checking that a block crafts back down into the items it was made from. None of these five do: four of each make a block, and none of those blocks ever uncrafts. So the drawer never saw the pair and the second slot stayed empty. All five are spelled out now, the same way Functional Storage already does it for glowstone and quartz. All five are frog resources, so all five are things you end up with by the thousand.
- **Pack settings survive NeoForge rebuilding a config file (#240).** The pack's own values for a handful of mods lived only in `config/`, which is per-install state. If NeoForge ever had to recreate one of those files, and it does that whenever it cannot parse or restore the old one, the pack's settings were gone and the mod's own defaults quietly took over. Those overrides now ship in `defaultconfigs/` as well, which is where NeoForge seeds a missing config from, so they come back instead of disappearing.
- **The Experience Singularity takes Bottles o' Enchanting, not books (#245).** Every other Singularity asks for a thousand of the resource its frog produces. This one asked for books, which the Experience frog does not make - its Froglight smelts to Bottles o' Enchanting. It was craftable, just wrong, and it quietly put you on a second production line the endgame never asks for anywhere else. Nothing else moved: the other 57 Singularities are unchanged. (Reported by Hunyol on Discord.)
- **The quest book no longer tells you to make an Ultimate Catalyst per Singularity (#241).** The Ultimate Catalyst sits in the Quantum Compressor's catalyst slot and stays there; it is not spent. The Long Compression and Your First Singularity both said otherwise, and so did the field guide, which put the bill at roughly 58 catalysts where one covers the whole endgame. All three now describe the slot correctly. (Reported by Hunyol on Discord.)

### Changed

- **19 mods updated to their current builds.** Apotheosis, JEI, the FTB suite (Library, Quests, Chunks, Ranks, XMod Compat), Supplementaries and Moonlight, Sophisticated Backpacks, Skyblock Builder, GraveStone, Fusion, FancyMenu, Balm, Cobblegen Galore, Mama's Herbs and Harvest, SuperMartijn642's Core Lib, and Spawn Detective. Nothing changes about how the pack plays, and the loader pin is unchanged. Sodium deliberately stays on 0.8.12: the newer build is a beta and the pack has no need of anything in it.

## [1.5.3] - 2026-07-25

Gets Grass Seeds working again, and brings the whole mod list up to current builds.

### Fixed

- **Grass Seeds and Mycelium Spores work on dirt again.** Ex Deorum 3.11 pointed both of them at the wrong block list, the crimson nylium one, which is netherrack and nylium. Dirt was not on it, so right-clicking dirt with either just did nothing. Grass Seeds drop from the builders' sieve and are the only way to get a grass block out here, so that has been dead since v1.4.4. Ex Deorum 3.12 gives each spore its own list back. (Found by Sam Gomez on Discord.)
- **Take Flight now describes the jetpack ladder Iron Jetpacks actually has (#233).** The chapter handed you a Basic Coil and then asked for an Iron Jetpack, which is not a recipe that exists: only the wood jetpack is built from parts, and every one above it is an upgrade with your current jetpack in the middle of the grid. The iron tier also wants the Advanced Coil, the gold one, not the Basic. The quests now walk the real path, wood to stone to iron, and say which coil each tier takes. Nothing was blocked before this, the route was just undocumented. (Reported by Hunyol on Discord.)

### Changed

- **NeoForge updated to 21.1.244, and 34 mods moved to their current builds.** Apotheosis and Apothic Attributes now want a loader newer than the one the pack was pinned to, so the loader moves up with them. Sodium also comes off the beta line onto 0.8.12 proper. Nothing changes about how the pack plays.

## [1.5.2] - 2026-07-25

Unblocks the Wither Altar, which has been asking for an uncraftable item since v1.2.0. Also updates Spawn Detective and tidies the docs.

### Fixed

- **The Wither Altar quest can actually be finished now.** The Trophy Pond quest asks for a Withered Star, and the Withered Star was impossible to craft: it and the Nether Star Catalyst were both a Nether Star ringed in obsidian, so the table only ever gave you the catalyst. The Wither Altar Hatch had the same problem against the End Dragon Altar Hatch. Productive Frogs 1.25.2 gives both Wither Altar pieces their own recipes - the Withered Star is a Nether Star wrapped in soul sand, the Hatch is obsidian and soul sand around a chest - so the whole altar is buildable. The other two recipes are unchanged.

### Changed

- **A Slime Milk source tells you when it has stopped because it is crowded.** A source pauses once too many of its slimes are already nearby, but it used to do that silently, which made it look broken. Look at one with Jade and it now reads "Paused: 30 / 30 Diamond slimes nearby". The limit also counts only that source's own resource instead of its whole species, so you can pack different resources of one species side by side without them fighting over one shared cap. Both come from Productive Frogs 1.25.1.
- **Spawn Detective updated to 0.1.0-alpha.3.** A green verdict no longer over-promises on a spot the natural spawner almost never picks - on a small platform in a void world every gate passes and the farm still sits empty, so the report now measures how often a spawn attempt anchors at that block's height and shows it beside the verdict. The same rate travels with a mob that only sometimes clears its own rules. The mob caps are also visible again on every surface (report screen, Jade, and the command), and a full cap reads as "competing for a slot" rather than "this block is dead", because a full monster cap is the normal state of an overworld.

## [1.5.1] - 2026-07-24

### Fixed

- **Spawn Detective's report screen is no longer blurred out.** Opening the Spawn Probe report with Minecraft's Menu Background Blur on (the default) smeared the whole report, and it was only readable if you turned that setting off. Updates Spawn Detective to 0.1.0-alpha.2, which draws the report on top of the blur instead of under it, so it stays sharp whatever your video settings.

## [1.5.0] - 2026-07-24

### Added

- **Productive Frogs updated to 1.25.0 ("Second Helpings"), with quests for its two new blocks.** The **Virtual Terrarium** runs one frog's whole loop hands-off inside two blocks (Processor + glass Display Dome): drop in a netted frog, pour in its milk, and it drops the output out the bottom with nothing loose on the ground and no floor space used. Four upgrade slots tune output, speed, smelting/melting, and an RF overclock. Its quest lives in the Void tier and it's gated to Void by recipe (it takes echo shards, which only the Void frog produces here). The **Slime Milk Basin** is a milk source you can pipe and leave: pour in any Slime Milk and it spawns that variant's slimes on the same budget as a placed pool, but when it runs dry it just waits for the next bucket instead of draining away. Its quest lives in the Bog tier. The update also fixes the Terrarium Hatch shift-click item dupe and stops a dispenser from wiping Slime Milk's catalysts when it scoops the bucket.
- **Added Spawn Detective, with an optional Welcome-chapter quest that grants its Spawn Probe.** The probe tells you why a mob won't spawn on a block: light, the floor, the mob cap, or you standing too close. It checks the game's real spawn rules instead of guessing. Hold it, pick a mob, and read any block live with Jade to find the dead spots in a dark room. Client and server; adds one item, no world content.

### Fixed

- **Server packs are now flagged as Server Packs on CurseForge.** Every release since v0.1.0 attached `sky-frogs-server-<version>.zip` to its client file, so the download has always been public - but CurseForge never treated it as a *typed* server pack, which is what server hosts read to offer one-click installs. The release pipeline now prints the manual Authors Console step (CurseForge's upload API has no field for it), fails the run outright if a release ships without a server pack at all, and `tools/check_server_pack_flag.py` audits published files so this can't silently regress.

## [1.4.4] - 2026-07-05

Maintenance release: updates Productive Frogs to 1.24.6 ("Fresh Coat"). No pack content or quests changed.

### Changed

- **Productive Frogs updated to 1.24.6 ("Fresh Coat").** A texture refresh backported from the 2.x line: sharper contents art for the Slime Bucket and Tadpole Bucket, each now with a proper bucket base of its own, and upgraded Slime Milk fluid textures. Slime Milk tints to its variant, so every milk in the mod gets the nicer look. Purely cosmetic - no recipes, data, or saves change, and the roster is unchanged (singularities 58, froglight recipes 102, census 60/34), so no quests changed.

## [1.4.3] - 2026-07-04

Editorial release: a full rewrite pass over the rest of the quest book, finishing what 1.4.2 started with the Cave tier. Every remaining quest description was rewritten to a plainer, clearer voice - teach a new player, guide an experienced one, nothing else - and several had their mechanics corrected against the actual mods. No pack content, recipes, or progression changed; no quests were added or removed.

### Changed

- **All remaining quest chapters rewritten** - the Geode, Bog, Tide, Infernal, and Void tiers, plus the Terrarium, Trophy Pond, Master Pond, and Completionist chapters. Descriptions are shorter and plainer, with marketing tone, filler, and forced flourishes cut. Personality now lives in the titles and subtitles; the bodies stick to teaching and guiding.

### Fixed

- **Quest descriptions that misdescribed a mechanic, recipe, item name, or number now match the mods.** Among the corrections: Refined Storage cabling is Quartz Enriched Copper (not Iron); the Terrarium's Incubators seed from bottled frog eggs only (not tadpoles); the Flux Dust ritual is built on bedrock; the Dissolution Chamber is the only slime path from the Tide tier onward (the old copy said Tier 5); and several recipe and reward names were fixed (for example the Simple Compacting Drawer).

## [1.4.2] - 2026-07-03

Editorial + maintenance release: the first three quest chapters rewritten to a clearer, more consistent voice, plus small mod bumps. No new content, no world-breaking changes.

### Changed

- **The first three quest chapters (Welcome, Your First Iron Ingot, Scaling the Colony) rewritten** for clearer, tighter descriptions, with several mechanics corrected against the actual mods.
- **Froglight names now render one consistent color** (gold) across every quest, so an item name reads the same everywhere and no longer shares a color with Slime-in-a-Bucket.
- **"Name Your Frogs" rewards an anvil** instead of name tags. Naming is cosmetic, and an anvil is otherwise a steep iron cost on a void island; the quest is optional and its text now says so.
- **Productive Frogs updated to 1.24.5 ("Deep Breath").** A hotfix: **Resource Frogs and their tadpoles no longer drown.** Vanilla frogs breathe underwater, but ours never could - a frog kept in a flooded pen or a submerged farm chamber would quietly run out of air and die while the vanilla frog beside it swam on, a bug present since the mod's first release. They now breathe underwater exactly like their vanilla cousins. No new variants or items, so the roster is unchanged (singularities 58, froglight recipes 102, census 60/34) and no quests changed.
- **Sophisticated Backpacks and Sophisticated Core bumped** to their latest 1.21.1 builds.

### Fixed

- **The Spawnery quest now requires the Cobblestone quest.** Crafting the Spawnery costs cobblestone, but the frog branch never depended on the branch that teaches cobble-making, so a player could reach it without being shown how. The dependency now gates the teaching in the right order.

## [1.4.1] - 2026-06-30

Maintenance release: updates Productive Frogs to 1.24.4 ("Growing Pains"). No pack content or quests changed.

### Changed

- **Productive Frogs updated to 1.24.4 ("Growing Pains").** A behavior/QoL release: tadpoles that grow up in a tight spot (under a low ceiling, in a one-block pool, wedged in a corner) no longer suffocate - a frog now appears in the nearest space it fits, and waits to mature if there's genuinely no room ([PF #276](https://github.com/Flatts3000/productive-frogs/issues/276)); and tadpoles can now be fed Sweetslime to speed growth, not just slime balls ([PF #277](https://github.com/Flatts3000/productive-frogs/issues/277)). No new variants or items, so the pack's roster is unchanged (singularities 58, froglight recipes 102, census 60/34) and no quests changed.

## [1.4.0] - 2026-06-30

A small content + fix release: a new optional Cave quest for the Dark Utilities slime filter, Functional Storage drawers now compact Opolis' Mini Coal and Mini Charcoal, and Better Compatibility Checker finally reports the pack version so the client-vs-server match check actually works.

### Added

- **Optional "Slimes Only" quest** (Cave tier), next to Players Only - the Dark Utilities Mob Filter (Slime) reads as solid to you and your frogs but lets slimes pass through, so you can sort and route the slimes a frog farm produces. ([#209](https://github.com/Flatts3000/sky-frogs/pull/209))
- **Mini Coal and Mini Charcoal now compact in Functional Storage drawers.** Opolis ships these at an 8:1 ratio that a compacting drawer's auto-detect skips; explicit compacting tiers register them, so one drawer spans Mini Coal -> Coal -> Block of Coal (and Mini Charcoal -> Charcoal). ([#206](https://github.com/Flatts3000/sky-frogs/issues/206), [#208](https://github.com/Flatts3000/sky-frogs/pull/208))

### Fixed

- **Better Compatibility Checker now reports a real version.** The pack shipped no `bcc-common.toml`, so its modpack version was an unset placeholder and the client-vs-server match check always passed (green even on a mismatch). The pack now ships the config, and the release pipeline stamps the version from the git tag into it (and the BBL `/modpack` readout), so a mismatch is actually flagged. ([#205](https://github.com/Flatts3000/sky-frogs/issues/205), [#207](https://github.com/Flatts3000/sky-frogs/pull/207))

## [1.3.0] - 2026-06-30

### Added

- **The experience (XP) Void variant is now craftable and quested.** It was census-only before (weight 0, so a Void frog never produces it on its own). A new Dissolution Chamber recipe self-keyed on a book (its primer, mirroring Productive Frogs' slime infusion) makes the experience slime, and an optional quest forking off the Void chain documents the path and the smelt to a Bottle o' Enchanting.
- **Optional "Name Your Frogs" quest** in Scaling the Colony. Name tags craft from string and paper (both on hand by then); the quest hands you four to christen a starting colony.

### Changed

- **Quest description polish.** Tightened the wordiest quest descriptions for clarity and consistency: trimmed padding, smoother phrasing, and corrected a few verbs to match the real in-game action (you use or empty a bucket, not "pour"). No mechanics changed.
- **Early-game quest clarity from playtest feedback.** "A Dark Room" now explains the ~24-block mob spawn distance (and corrects the "spawn protection" misconception); "A Place for Frogs" surfaces the mud recipe where it's first needed and warns that tadpoles must stay in water; the breeding quest states the cooldown and that pairs lay in the pool. "Raising the Line" was split into a short breeding-action quest plus the stat-strategy quest.

### Fixed

- **Productive Frogs 1.24.2 -> 1.24.3 ("Muddy Waters"):** a bred frog now lays its egg even when standing on **mud**, a slab, or other sub-full blocks beside the pool (a footing-aware contact lay). This fixes [productive-frogs#270](https://github.com/Flatts3000/productive-frogs/issues/270), where a mud-floored breeding pen never produced eggs, so the pack's own mud-floor guidance is finally correct. Pure behavior fix: no new variants/items, zero roster drift.

## [1.2.0] - 2026-06-29

A content + maintenance release: Productive Frogs moves to the 1.24.2 line (redstone-toggleable Terrarium Sprinklers), three new optional endgame quests (the Warden, the Dragon Altar, the Wither Altar), Functional Storage now compacts clay and snow, and froglight quest drawer rewards fit each resource.

### Added
- **Optional "Wake the Warden" quest** (Void tier) - a guided path to top-tier Apothic Enchanting: craft and activate a Sculk Shrieker, summon the Warden, and claim the Warden Tendril.
- **Optional Dragon Altar and Wither Altar quests** (Trophy Pond) - surfacing Productive Frogs' contained, repeatable boss farms: build the End Dragon Altar on the End exit portal, and the Wither Altar from your first Nether Star.
- **Clay and snow now compact in Functional Storage drawers** - added the missing decompress recipes (clay block to 4 clay balls, snow block to 4 snowballs) so both pack down like every other resource.

### Changed
- **Froglight quest drawer rewards now fit the resource** - 3-tier metals reward a Compacting Drawer, 2-tier resources a Simple Compacting Drawer, and single items a plain drawer, so no compaction slots go to waste.
- **Terrarium quest text** clarified - appliances are placed from outside the shell, the controller is not locked to a fixed height, and Sprinklers are now redstone-toggleable; the Hatch is renamed "Terrarium Hatch".
- **Productive Frogs 1.22.0 -> 1.24.2** (four releases). **1.24.2 "Name Tags"**: renames the Terrarium "Hatch" to "Terrarium Hatch" (display name only - same `productivefrogs:hatch` id and recipe) so it no longer collides with the two altar hatches; the pack's Terrarium Hatch quest text was updated to match. **1.24.1 "No Crossed Wires"**: fixes the v1.24.0 Sprinkler redstone control leaking to neighbouring Sprinklers (#264), so per-Sprinkler staging works as the quest text describes - this was the bug the pack held for before release. Re-swept at 1.24.2 with zero roster drift (singularities 58, froglight 102, census 60/34). **1.24.0 "Flip the Switch"**: Terrarium **Sprinklers can now be switched off with redstone** - a powered Sprinkler pauses (its held milk and remaining spawns freeze, then resume when the signal drops), and each Sprinkler is controlled on its own, so you can stage which resources run or wire a comparator off a full chest to self-throttle. This directly answers standing Discord requests to toggle slime production against the mob cap (PF #263). **1.23.0 "The Midas Touch"**: adds an opt-in, endgame **Equivalence/transmutation lane** (Alembic -> Mimic Slime -> Midas frog -> Prismatic Froglight -> Distiller, an equivalent-exchange engine) that is **off by default** (`equivalence.enabled`), so the pack is unaffected unless it opts in; it also **fixes the Wither Altar to form in all four orientations** (previously only one compass orientation assembled; PF #247). The 1.22 -> 1.24 jump adds **one new vanilla variant, `experience`** (void category): the sweep regenerated deterministically - singularities **57 -> 58**, froglight->slime recipes **101 -> 102**, vanilla census **59 -> 60** (modded census unchanged at 34), validator clean. The variant is tracked in the census; slotting it into a tier's species chapter is deferred.
- **Refreshed all other mod pins** via `packwiz update --all` (~37 routine version bumps). Sodium moves to `0.8.12-beta.2`: the updated Supplementaries requires Sodium >= `0.8.12-beta.1`, and the `0.8.x` line is the current Sodium for NeoForge 1.21.1 (beta-only - no stable that new exists). Pinning Sodium back to stable `0.6.13` crashed the game at load on a Supplementaries dependency check.

## [1.1.0] - 2026-06-16

A maintenance release: Productive Frogs jumps to 1.22.0 "Apex Predators", bringing two contained, repeatable boss farms (an Ender Dragon altar and a Wither altar), and the Functional Storage controllers stop colliding with their extension recipes.

### Changed
- **Productive Frogs 1.21.0 -> 1.22.0 "Apex Predators".** Adds two boss-tier automated farms with no new resource variants. The **End Dragon Altar**: build it on the End exit portal for a hands-off, repeatable Ender Dragon harvest - a replica dragon rises and is devoured by a special frog, dropping a Dragon Breath Froglight, a renewable Dragon Egg Froglight, the Princess's Kiss, and XP into a hatch you can pipe with hoppers (no real boss, no portal regrowth). The **Wither Altar**: after your first Wither kill, its Nether Star crafts the altar's keystone, and from then on you summon and farm a contained replica Wither in a soul-forged arena for a Nether Star Froglight and XP - no boss bar, no exploding blocks. Both altars harvest the existing boss froglight variants, so the census, singularities, and froglight recipes are unchanged (zero drift). The pack pins no boss config, so both altars are available at the boss tier; the new altar blocks are not quested yet (deferred to a follow-up).

### Fixed
- **Functional Storage controllers no longer share a recipe with their extension blocks (#186).** The pack's quartz-free storage rewrite had accidentally given the Storage Controller and its Controller Extension (and the framed pair) the exact same recipe, so crafting one could hand back the other, and a crafting-station's output picker got stuck on the wrong result. The controllers now use a distinct redstone-block center, so every block has its own unambiguous recipe. (Reported by tamsen2207 on Discord.)

## [1.0.0] - 2026-06-14

Sky Frogs 1.0 - out of beta. The full pack: all six tiers (Cave through Void), the Trophy Pond boss campaign, the Terrarium automation chapter, and the Completionist census, complete and shipping as a stable release. This launch also lands a full editorial pass over every quest, Productive Frogs 1.21 (an in-game field guide granted on join, the Sweetslimed Lily Pad perch, and reworked breeding), a Sky Frogs section in that guide, new Crusher and Bio Fuel quests in the Bog tier, and an Apotheosis loot fix.

### Added
- **Crusher + Bio Fuel quests in the Bog tier.** Two new quests in `road_to_bog` before Mossy Cobblestone, spelling out the missing intermediate step: craft a Mekanism **Crusher** to grind plant matter into **Bio Fuel**, the infusion material the Metallurgic Infuser drinks to turn cobblestone mossy. The chain (Crusher -> Bio Fuel -> Mossy Cobblestone) was implied by the Mossy Cobblestone quest text but never quested; now the player is walked through it.
- **A Sky Frogs section in the field guide.** The pack now extends the Productive Frogs guide book with its own "Sky Frogs (Pack)" category - the void-skyblock premise, the Dissolution Chamber slime engine, the recipe swaps that differ from stock PF (quartz-free storage, the redstone Teeming catalyst, the per-tier Spawnery primers), and the singularity endgame. It merges into the same book rather than shipping a second one, so there's one guide to flip through.
- **The Productive Frogs field guide is now in everyone's hands.** PF 1.21 ships an in-game Patchouli guide book (`productivefrogs:guide`), and the pack grants it to **every player on join** - new players get it on first login, and anyone who already started a world gets it once on their next login (a one-time grant separate from the quest-book first-join, in `first_join.js`). It stays craftable too (a vanilla book + a slime ball). The book is built to be extended, so the pack can later add its own pages without forking it.

### Changed
- **Productive Frogs 1.20.0 -> 1.21.0 "By the Book".** Brings the in-game field guide (above), a new **Sweetslimed Lily Pad perch** (right-click a placed lily pad with a Sweetslime so a Resource Frog claims it and holds position - handy over a hopper by a Slime Milk source), a **boss-altar fix** (a sealed altar no longer traps its slime inside the source block), and a **breeding rework**: an offspring's stats are now the average of its parents and then have a chance to climb higher, breeding never goes backward, and every breed improves at least one stat. The pack pins no breeding config, so the new model flows through; the **Raising the Line** quest text was rewritten to match (its old odds-based wording is now inaccurate). No new resource variants, so the census, singularities, and froglight recipes are unchanged.
- **Holistic editorial pass over all quest text (issue #169).** Reviewed every quest across all 27 chapters for factual accuracy, voice, terminology, and formatting - ground-truthing each described mechanic against the mod jars, Productive Frogs' own datapack, and AlmostUnified rather than memory. Fixed roughly 30 accuracy bugs, the kind a player following the text would get stuck on, including: the Just Dire Things Primogel Goo now describes the real goospread mechanic (the goo spreads into an adjacent iron/coal block and turns it into raw ore - not the invented "seed the soil" step that triggered this review); the sea lantern recipe (5 prismarine crystals + 4 shards); the Cave Redstone slime threads off breeze-rod milk; the Mekanism steel chain needs a second carbon infusion before smelting; the Geode Slime Milk catalysts now use their real in-game names (Bountiful / Rapid / Teeming / Endless); and the Item Collector and Disk Drive descriptions match their actual recipes/limits.
- **Species-unlock item renamed "Frogspawn" -> "Bottle of <Species> Frog Eggs" in all quest text.** Matches Productive Frogs' real item name, so a new player can find it in JEI. ~21 strings across the gateway chapters.
- **Census titles corrected** (generated chapters): the Powah crystals now read "Blazing/Niotic/Spirited/Nitro Crystal", "Eclipsealloy" -> "Eclipse Alloy", and the vanilla "Clay Ball" -> "Clay", all matching the in-game names. Fixed in `tools/gen_completionist_chapters.py`; quest IDs are deterministic so completion survives.

### Fixed
- **Mobs no longer drop affixed Froglight Cleavers (issue #184).** Apotheosis was treating the Productive Frogs Froglight Cleaver - the crafted boss-tier endgame weapon - as affixable loot, so an over-statted affixed copy could drop from the mob farm and bypass the whole endgame. The Cleaver is now excluded from Apotheosis affix loot via the mod's own `loot_category_overrides` data map (set to `apotheosis:none`, the same exclusion the mod uses for shulker shells). The affix system is otherwise untouched - other gear still rolls affixes normally.

## [0.14.0] - 2026-06-10

A content-and-fixes drop: the Bog quest chain splits into two lanes (a clean spine to Tide plus an optional mob-drop lane), Productive Frogs reaches its stable 1.0 ("Full Bloom") with the Jade tadpole-timer and Slime Milk fluid fixes, and the Bog reward crate stops handing out four spyglasses.

### Changed
- **Productive Frogs 1.19.1 -> 1.20.0 "Full Bloom".** PF hit its stable 1.0 milestone (out of beta). The jump also folds in 1.19.2, which **fixes the Jade tadpole "Growing time" readout** (it now shows the real remaining time when a pack speeds up tadpole growth - the Bog tadpole that read ~10m draining too fast), stops the Slime Bucket from dumping a water source on release, and stops foreign fluids from washing away Slime Milk pools; plus a standalone Advancements tab (complementary to the quest book). No new variants or items - zero roster drift (singularities 57, census 34, froglight recipes 101); pin-only on the pack side.
- **The Bog quest chain is now two lanes.** The long Bog chapter is split into a canonical spine (organics + Industrial Foregoing, the path to Tide) and a terminal mob-drop lane (bone -> gunpowder -> ... -> honeycomb) that branches off the Pink Slime capstone. The mob lane bootstraps from bone meal and chains down, so the un-farmable drops (armadillo scute, honeycomb) come from the chain - no armadillos or bees needed. All quest IDs preserved, so existing completion survives.

### Fixed
- **The Bog reward crate gives one spyglass, not four.** It had been lumped into a uniform x4 group; a spyglass is a reusable tool you only need one of.

## [0.13.1] - 2026-06-10

A launch-crash hotfix: bumps the pinned loader off a flaky NeoForge build.

### Fixed
- **Some fresh installs crashed on the loading screen (no crash report).** The pack pinned NeoForge `21.1.230`, which applied its `GuiGraphics` tooltip patch unreliably on certain machines; when the field was missing, Apotheosis's required tooltip accessor failed to apply and the game closed ~10-15s into loading with no crash report. Bumped the pinned loader to **NeoForge 21.1.233** (latest 21.1.x), which patches reliably. Diagnosed from a player log (Apotheosis `GuiGraphicsAccessor` / `tooltipStack`); the same bad build also hit other NeoForge 1.21.1 packs. No mod or content changes.

## [0.13.0] - 2026-06-10

A QoL-and-fixes drop: Refined Storage gains infinite-range wireless (the Interdimensional Wireless Transmitter) and tiered cables, frogs breed up faster (Productive Frogs 1.19.1), the Refined Storage silicon variant is fully integrated into the Dissolution Chamber and the census, and the Just Dire Things goo quests now describe the real goo-spreading mechanic.

### Added
- **Interdimensional Wireless Transmitter** (+ **Cable Tiers** and its **Refined Types** dependency): Refined Storage addons matching the main ATM10 pack's RS set. The transmitter broadcasts your network to a Wireless Grid at **infinite, cross-dimensional range**, fixing the base 48-block wireless cap (Discord report, Dergib). It's endgame-gated by recipe (4 Wireless Transmitters + 4 Nether Stars + an Elytra) - boss-tier nether stars are frog-farmable and the Elytra comes from the vanilla End's cities. Cable Tiers adds faster tiered cables; Refined Types is its dependency (and a general FE storage disk).

### Changed
- **Productive Frogs 1.19.0 -> 1.19.1 "Survival of the Fittest".** Tuning only: the default frog-stat improvement chance rises from `0.20` to `0.40` per stat, so a breed now improves at least one of the three stats about 78% of the time (up from ~49%) - a brisker climb to a maxed frog without a giveaway (a single breed still usually moves one or two stats, not all three). The pack doesn't pin this value, so the new default flows through from the jar with no pack-side change. Zero roster drift (singularities 57, census 34, froglight recipes 101). (Prompted by Discord feedback that breeding felt slow.)

### Fixed
- **Silicon is craftable in the Dissolution Chamber and quested in Sister Ponds.** The Refined Storage silicon variant (the only PF variant gated `ae2 OR refinedstorage`) was missing its Dissolution Chamber recipe and its census quest, leaving the Froglight smelt-back as its only path - which read as circular. It now has a self-keyed chamber recipe (smelt nether quartz -> RS Silicon -> prime a slime) and a Sister Ponds entry; the census generator now picks the loaded provider for multi-provider variants. (#168, Discord report.)
- **JDT goo/ferricore quest text corrected.** "First Goo" and "Ferricore Ingot" described a non-existent "right-click the soil to seed it" mechanic that stuck a player. They now describe JDT's real goo-spreading: place Primogel Goo and stack iron blocks against it, and each spreads into Raw Ferricore Ore to mine and smelt. (#170, Discord report.)

## [0.12.0] - 2026-06-10

A content-and-polish drop: a real pack logo/icon, Productive Frogs 1.18 + 1.19 (Lava Froglights as furnace fuel, the Crucible melting stone to lava), Spice of Life food variety, Ender Storage, craft-any-slime-from-its-Froglight, a reliable flint recipe, and the fluorite JEI fix.

### Added
- **Spice of Life: Carrot Edition**: eating a variety of foods grants bonus max hearts, rewarding the pack's broad food economy. Tuned reward-only - you start at vanilla 10 hearts (never lower), the first bonus heart comes at just 10 unique foods, and you don't lose earned hearts when you die. (#160, suggested on Discord.)
- **Flint from gravel.** A shapeless recipe: 3 gravel -> 1 flint, so flint (for Flint & Steel and the Nether portal) has a reliable source on a void skyblock instead of relying on gravel's random drop. (#159, suggested on Discord.)
- **New pack logo / icon.** The frog on a cloud sky with a two-row "SKY FROGS" wordmark in the authentic Minecraft title style (Minecraft Ten + mangrove texture, the same generator as the title screen). Ships as the 256x256 launcher icon (`pack/icon.png`); 512 master in `branding/`.
- **Ender Storage**: color-frequency wireless storage - EnderChest, EnderPouch, and EnderTank, all sharing inventory by dye-code across any distance (and dimensions). Wireless access to your base from the field, and wireless fluid hauling via the tank. (Suggested by Dergib on Discord.)
- **Craft any slime back from its Froglight.** Once you've got a variant's Froglight, you can craft it straight into that variant's Slime in a Bucket: an empty bucket + 4 tier-filler + 3 sweetslime around the Froglight in the center. A recovery/scaling path for every slime (vanilla and modded) - the Froglight is proof you already have the frog, so it doesn't skip any gate. (Suggested by Dergib on Discord.)

### Changed
- **Productive Frogs 1.17.0 -> 1.19.0.** Two upstream bumps: **1.18 "Made to Measure"** added pack-author config switches (Sky Frogs keeps everything on, so no player change), and **1.19 "Stone Soup"** makes **Lava Froglights burn as furnace fuel** (one Froglight = a lava bucket's worth of smelting) and lets the **Froglight Crucible melt stone/cobblestone/gravel/netherrack into lava**. No new variants; zero roster drift.

### Fixed
- **Fluorite slime now shows its recipe in JEI.** The Bucket of Fluorite Slime took the `c:gems/fluorite` tag, which both Mekanism and ATO register a fluorite into - so JEI's "uses" page for the Mekanism fluorite you actually get (from the calcite Enrichment Chamber recipe) didn't reverse-resolve the tag and the path looked missing. It now takes the concrete `mekanism:fluorite_gem` (the only fluorite obtainable on a void skyblock), so the calcite -> fluorite -> slime chain is discoverable end to end. (Discord report, Dergib.)

## [0.11.0] - 2026-06-09

The Frog Legs and Fairy Tales update: Productive Frogs 1.17 brings frog legs, the Frog Net, the Froglight Cleaver, and Princess's Kiss (all quested), Apotheosis joins as a combat/enchanting/loot layer, and Elevators + Time in a Bottle round out the QoL - plus two progression fixes from Discord.

### Added
- **Elevators** (OpenBlocks Elevator): place colored elevator blocks at the same spot on different floors, jump to go up and sneak to drop down - quick vertical travel for multi-level bases, no flying required.
- **Time in a Bottle**: store passing time in a bottle and spend it to fast-forward a block - speed up your machines and farms on demand. (Both suggested by Dergib on Discord.)
- **Apotheosis**: an affix-loot, enchanting, and boss layer - affixed gear drops from mobs (and salvages into its own gem/sigil economy, not vanilla resources), a reworked enchanting system, gems and gem-cutting, and the occasional mini-boss invasion. Brought in to enrich combat and the endgame; most of its deadly/worldgen content stays dormant on a void skyblock. Balance tuning (affix rate, boss frequency, the enchanting rework vs. the early Enchanting Table) is pending playtest. Ships with its hard dependencies Apothic Enchanting, Apothic Attributes, Apothic Spawners, and Patchouli.
- **Productive Frogs 1.17.0 "Frog Legs and Fairy Tales."** Killing a frog now drops **Frog Legs** (renewable meat for a skyblock - raw, or cooked if the frog was on fire), plus a **Frog Legs Soup**. New tools and items arrive too: the **Frog Net** (catch a Resource Frog and relocate it with its bred stats intact - restock a Terrarium without leashing), the **Froglight Cleaver** (an endgame sword that drops a slime's Froglight when it kills it), **Princess's Kiss** (the Ender Dragon drops it; right-click a frog to turn it into a villager - a dragon-gated path to a trading economy), and a **Potion of Hopping** (leap forward, land soft). The **Terrarium** got friendlier: Incubators are now optional (it forms with none - lead or net frogs in yourself), and the Hatch collects frog legs alongside everything else.
- **Three quests for the new 1.17 content.** The **Frog Net** is taught early (right after your first frog, in the opening chapter) so you can relocate frogs from day one. The **Froglight Cleaver** becomes the **Trophy Pond capstone** (replacing the old "Apex Pond" checkmark finale) - forge it from the Nether Star and Dragon Egg Froglights wrapped in Dragon's Breath, exactly the trophies the chapter already farms. **Princess's Kiss** is a Void-tier quest after slaying the dragon - claim the Kiss, turn a frog into a villager, and bootstrap a trading economy. (Frog Legs are intentionally left unquested - the pack won't push you to kill your frogs.)

### Changed
- **Road to Tide no longer routes through the Fluid Extractor.** That quest is now "A Bucket of Latex" - you get latex by melting a plastic Froglight in the Crucible (it renders down into exactly one bucket of latex), the same Tier-0 block that bootstrapped your lava. The Fluid Extractor was never needed for plastic (the plastic frog is the only plastic source), and now it isn't needed for the Chamber's latex either - the frog supplies both. Fixes the misleading "Sap into plastic" subtitle and the Chamber/Fluid-Collector quest text that still pointed at the extractor. (Discord, dlswimmer.)

### Fixed
- **Emergency items now actually hand you a sapling.** The quest book's empty-inventory recovery had its cooldown set but its item list left empty, so the safety net gave nothing. It now grants one oak sapling - the standard skyblock anti-softlock for a wiped-out player who lost their only renewable wood source.
- **Mobs no longer spawn carrying loot-filled backpacks.** Sophisticated Backpacks' default "entity backpack additions" let hostiles spawn wearing backpacks stuffed from structure-chest loot tables, handing players iron and other resources before they ever bred a frog - a straight bypass of the frog-as-resource-spine progression. Disabled (`chance = 0.0`); you still craft and upgrade backpacks normally. (Discord report, RayRayZCB.)

## [0.10.1] - 2026-06-09

A polish patch from community feedback: clearer quest hints and the official server in your multiplayer list.

### Added
- **The Sky Frogs server is in your multiplayer tab.** The pack now ships the official server (`skyfrogs.benbenlaw.com`) via BBL Core, so it's right there in the multiplayer list on first launch - plus `/modpack` and `/discord` commands wired up.

### Changed
- **The questbook points you at the infinite-milk fix.** The early "Milk It" quest now tells you the Geode-tier Infinite Count Catalyst makes a Slime Milk source never run dry, so milk depletion reads as "fix incoming," not a dead end (Discord feedback - players were getting stuck thinking milk couldn't be automated).
- **Terrarium quest clarifications.** The Sprinklers quest notes you can pull milk back out with an empty bucket; the Incubators quest explains the 8-frog cap is the incubators' release ceiling (not a hard limit - you can lead more in by hand) and that you run several incubators for throughput.

## [0.10.0] - 2026-06-08

The automation update: Productive Frogs 1.16 brings The Terrarium - a sealed multiblock that runs the frog loop hands-off - and the pack gives it a full build-it-yourself chapter in the Infernal tier.

### Added
- **The Terrarium chapter** (Infernal tier): Productive Frogs 1.16 ships The Terrarium - a sealed 5x4x5 multiblock that runs the whole frog loop hands-off (a Controller pipes Slime Milk to ceiling Sprinklers that rain slimes, Incubators raise stat-intact frogs, and a Hatch collects the Froglights for piping out). The new chapter walks you through it: craft the four blocks, seal the box (right-click the Controller and it tells you what's wrong until it reads "formed"), prime the sprinklers, stock the incubators, and walk away. It's the pack's first automation of the frog loop - the Infernal-tier payoff for six tiers of doing it by hand.

### Changed
- **Productive Frogs 1.15.0 -> 1.16.0** (The Terrarium). No roster change - machinery only - so singularities and the census are unchanged.

## [0.9.1] - 2026-06-08

A crafting-fidelity patch: the recipe picker now works inside Refined Storage grids, and mossy cobblestone is back to coming only from the Metallurgic Infuser the way the quest intends.

### Added
- **Polymorphic Refined Storage** (#137, reported by Dergib on Discord): the Polymorph recipe picker now works inside Refined Storage's Crafting and Pattern grids. When two mods share a recipe (the two chisels, for one), you can finally pick which result you want from within an RS grid instead of being stuck with whichever one wins by default.

### Changed
- **Mossy cobblestone is gated to the Metallurgic Infuser** (reported by Dergib on Discord). Mossy cobblestone is the Bog tier's filler block, and the "Mossy Cobblestone" quest teaches the intended path: infuse cobblestone with Bio in Mekanism's Metallurgic Infuser. The cheap bypasses are now closed - the vanilla `cobblestone + vine` and `cobblestone + moss block` crafting recipes are removed, Rechiseled can no longer chisel cobblestone into mossy cobblestone (a self-contained mossy group still lets you chisel cosmetic mossy variants once you hold the real thing), and Ex Deorum's `grass seeds -> moss block` craft is gone (moss block is a Bog frog resource, not a Tier 0 sieve product). The Infuser recipe itself is untouched.

## [0.9.0] - 2026-06-08

The frogs make friends with Just Dire Things - its metals, gems, and fuels all farm through the loop now - and the Slime Churn lets you turn milk back into bucketed slimes with no slime to chase.

### Changed
- **Productive Frogs 1.14.0 -> 1.15.0.** The frogs make friends with Just Dire Things:
  - **Just Dire Things, farmed through frogs**: Ferricore (Cave), Blazegold and Celestigem (Infernal), and Eclipse Alloy (Void) become frog-farmable - prime a slime with the ingot or gem, feed the matching frog, smelt the Froglight back. Three JDT fuels (Blaze Ember, Voidflame Coal, Eclipse Ember) farm too, melting in the Froglight Crucible straight into refined fuel and skipping JDT's own coal-refining chain. JDT is now the seventh column in Sister Ponds (the modded census grows 26 -> 33).
  - **The Slime Churn**: a hand-operated block that runs the Slime Milker backwards - load a variant's Slime Milk bucket plus empties and it fills them with that variant's Slime Buckets, on the same rules (and catalysts) a placed milk source spawns by. No entity to chase; loop the emptied bucket back in for a self-feeding line. Quested in Tools and Things (Bog tier).

## [0.8.0] - 2026-06-07

The boss farming update: the frogs go to war. Productive Frogs 1.14 makes the Wither and the dragon renewable - and Trophy Pond, a whole new chapter, walks you through entombing their toxic milk in catalysts of their own substance. Along the way: potions brewed straight into Froglights, four new Bog resources and a fifth for the Infernal, a Mega Torch that knows not to starve your frogs, and a world where dragon eggs finally obey YOU.

### Added
- **Torchmaster** (#134, suggested by Dergib on Discord): the Mega Torch keeps hostile natural spawns off your island. The pack ships a config exempting every Productive Frogs slime from the torch - your swamp's cave slimes keep spawning right next to it, only the actual menaces stay away.
- **Trophy Pond - the boss campaign chapter** (Void group): an intro warning ("Do Not Touch the Milk"), two wings, and a capstone. Each boss arc is a trophy hunt (show one real drop; six more go into the build) into a containment build (six catalysts of the boss's own substance, sealing every face of a Slime Milk source) into the Froglight. The Wither wing runs fortress skulls into Withers into Nether Stars; the Dragon wing respawns the dragon for eggs and bottled breath. The story: boss milk Withers its keeper, and the catalyst blocks exist to ENTOMB it - sealed, the poison farms FOR you. Apex Pond caps it with all four boss Froglights.
- **More Dragon Eggs** (5.0, the ATM10-family mixin by Darkere): every dragon kill drops a Dragon Egg. Without it, vanilla's one-egg-per-world law makes the six-egg Dragon Egg altar mathematically impossible.
- **Five new resource quests**: bone, gunpowder, rotten flesh, and string thread into the Bog chain after honeycomb; magma cream slots before the Infernal capstone. Same froglight-check law as every resource quest.
- **Brewed Froglights get their intro**: a two-quest branch off the Blaze quest - splash a potion on a slime, the Froglight captures the effect as a toggleable aura, then wear it in the Curios charm slot. Honor-system checkmarks, on purpose.

### Changed
- **Productive Frogs 1.13.0 -> 1.14.0.** The frogs learn boss farming and potion work:
  - **Brewed Froglights**: splash or linger a potion onto a slime before its frog eats it and the Froglight captures the effect - placed, it is a toggleable aura (good or bad: Poison perimeter, Regeneration room); held, it buffs you; with Curios it rides a dedicated Froglight charm slot.
  - **Boss resources**: Wither Skeleton Skull and Nether Star (Infernal), Dragon Egg and Dragon Breath (Void) become farmable - prime the first slime with the real drop, then wall the farm behind a catalyst altar (boss Slime Milk inflicts Wither on you, not the slimes).
  - **Five new vanilla resources**: bone, string, gunpowder, rotten flesh (Bog) and magma cream (Infernal), plus **Refined Glowstone** (Mekanism, Infernal).
  - Resource Slimes render their inner block again (snow/ice/mob-drop batch).
- **The Ultimate Singularity wants 57** (was 48): one Singularity per new resource, boss trophies included - a thousand Nether Stars is exactly the kind of automation this endgame exists to prove.
- **The slime chains grew**: Bog's chamber + crafting-table chains thread the four mob drops in after honeycomb (string is the new bridge into plastic), magma cream slots before the Infernal capstone, and the boss slimes are deliberately self-keyed in the Dissolution Chamber - each boss slime costs one real drop, so the chamber never bypasses the kill.
- **The census frog grew**: The Whole Pond now counts 59 vanilla froglights (the Bog body widened, both back limbs thickened), Sister Ponds counts 26.

## [0.7.2] - 2026-06-07

An endgame unblocker: the two Singularities nobody could ever craft are gone, the Ultimate wants 48, and kelp finds its way into the moss sieve.

### Fixed
- **The Water and Lava Singularities are gone - they were uncraftable** (#131, reported by Dergib on Discord): both demanded 1000 of an item with zero sources on a void skyblock (kelp and pointed dripstone - no ocean, no caves, sand sieving disabled, and the fluid-pair Froglights melt to fluid rather than smelting to an item). The **Ultimate Singularity now wants 48**; mid-campaign players will see its recipe shrink, and already-crafted Water/Lava Singularities become inert curios. The exclusion lives in the generator, so future PF bumps cannot resurrect the pair.

### Added
- **Kelp sifts from moss** (#131, Dergib's suggestion, accepted): the Builders' Sieve moss lane gains kelp at Ex Deorum's own 10% - with its singularity gone, kelp is decor and dried-kelp food again, exactly what the lane is for.

## [0.7.1] - 2026-06-07

A same-day title-screen patch: the menu stops showing players its editing scaffolding, and the wordmark is rebuilt by hand in the authentic vanilla title style - mossy mangrove green, the look of the update that brought frogs to the game.

### Fixed
- **FancyMenu no longer greets players in customization mode** (#130, reported by Dergib on Discord): the pack shipped layouts but no FancyMenu options, so fresh installs got the editing overlay on the title screen. The pack now ships `config/fancymenu/options.txt` with [modpack mode](https://docs.fancymenu.net/docs/en-US/modpacks) on - no overlays, no hotkeys, no welcome screen, just the finished menu. Tinkerers can flip `modpack_mode` back to `false` in that file.

### Changed
- **The title-screen wordmark is hand-built now, not AI-generated** (maintainer rule: no AI assets fronting the pack). The new SKY FROGS logo is rendered with Ewan Howell's Minecraft Title Generator (the community-standard Blockbench plugin; renders free to use) in the authentic vanilla title style: **Minecraft Ten** font, **Mangrove (Wild Update)** texture - the look of the very update that brought frogs to Minecraft. Recipe documented in `docs/branding.md`, reproducible in five minutes.

## [0.7.0] - 2026-06-07

The completionist update: the questbook gets its victory lap. Two census chapters count every froglight you can farm - the vanilla fifty drawn as an actual frog, the modded twenty-five column by column - in their own Completionist section, and every name on the list is genuinely craftable, no lottery tickets. Along the way: the Froglight Crucible melts froglights into real fluids, the Mace becomes a weapon you can actually hold, Powah gets its questline, and the title screen finally knows what pack it is.

### Added
- **The Mace is obtainable** (#127): no trial chambers generate over the void, so the **Heavy Core** now presses out of the **Dissolution Chamber** - 4 iron blocks + 4 prismarine under latex, Tide-gated by construction (the chamber is built at the Tide boundary, and prismarine is the Tide frog's resource). Deliberate synergy: the weapon that scales with fall height lands in the same tier as the jetpack. Two new Take Flight quests teach it (**The Heavy Core** -> **Drop the Hammer**), including the breeze rod -> 4 wind charges combo.
- **The census chapters** (#121, suggested by StephJ2Fan on Discord and seconded twice): two end-of-book checklists in their own **Completionist** sidebar section after Tier 6. **The Whole Pond** is every vanilla froglight (50 today) arranged as an actual top-down tree frog - head is Cave, body is Bog, the four limbs are the other tiers, suckers on every toe - with a lily-pad capstone that demands the lot. **Sister Ponds** is the modded census, one column per mod (All the Ores, Powah, Refined Storage, Mekanism, Industrial Foregoing, Flux Networks - 25 quests today, every loaded-mod variant). Both are generator-built with stable ids, so they grow with future frogs without resetting anyone's progress. Riding along: the 13 modded variants that had quests but no recipe (the ATO metals, RS set, fluorite, refined obsidian) now have self-keyed chamber rows - tag-primed variants take their tag, exactly like PF's own priming. Osmium gets a chamber row too (review catch): it always had the table bootstrap, but every census variant should scale in the chamber.
- **Every modded resource is now craftable** (#121 follow-through; a census you can't finish is a taunt, not a checklist). The seven ore-less **All the Ores metals** get a seed chain off Osmium - aluminum, lead, nickel, silver, tin, uranium, zinc, each slime crafted from the prior metal's Slime Milk exactly like the Cave chain. **Fluorite** presses out of frog-farmed calcite in Mekanism's own Enrichment Chamber (Geode mineral to Geode mineral). And **Uraninite** stops being a pure lottery ticket: Powah's Orb already turns uranium ingots into uraninite, and uranium is now farmable - the Powered Up quest teaches the route. Split-discovery still works as the lucky shortcut everywhere.

> **Heads-up for endgame players:** the Ultimate Singularity now demands **50** singularities (was 40) - PF 1.12 adds ice, snow, water, and lava, and PF 1.13 adds breeze rod, ghast tear, phantom membrane, both scutes, and honeycomb, each with its own Singularity. Already-crafted Ultimates are unaffected; mid-campaign players will see the recipe grow. Also: if you primed Lava Slimes with a magma block, the primer is now **pointed dripstone** (existing lava slimes/froglights/milk carry over and re-home to Cave on world load).

### Changed
- **Productive Frogs 1.11.0 -> 1.13.0**: the **Froglight Crucible** and **Casting Mold** arrive - melt Froglights into real fluids over a heat source (water and lava become renewable; metal Froglights melt at ore-doubling yield; IF's plastic and pink slime get their liquids), then cast molten metal back to ingots. This is the liquid-crafting future the Discord was promised. TEN new vanilla variants ride along: **Ice and Snow** (Tide - no cold biome needed ever again, and Powah's Dry Ice finally orb-crafts from frog-made blue ice), **Water and Lava** (Cave as of 1.13 - renewable fluids are day-one business; item-forms kelp and pointed dripstone), and 1.13's mob-drop stragglers: **breeze rod** (Cave), **ghast tear** (Infernal), **phantom membrane** (Void), **armadillo scute and honeycomb** (Bog), **turtle scute** (Tide). All ten get chamber rows, Singularities, and froglight quests - eight threaded into their tier chains, while **the fluid pair (water/lava) sits outside the seed chains by design**: their slimes craft (table and chamber alike) from the FLUID BUCKETS - barrel water and Tier 0 crucible lava - plus the usual stone, sweetslime, and Cave frogspawn. (#108, PF#155, PF#164, PF#161)
- **The Melting Point chapter** (#123): the Crucible and Casting Mold get their own Tier 1 questline, slotted between Cave Frogs and Storage & Crafting - craft the basin (iron + hammer-chain bricks), learn the heat ladder (Froglights are heat sources too), the **Water and Lava Froglight quests live here**, then the Mold and the three-block tower that turns metal Froglights into doubled ingots, hands-free.

### Fixed
- **Flux Dust is actually obtainable now** (#120, reported by Dergib on Discord; island idea by StephJ2Fan): Flux Networks' dust ritual needs obsidian resting on BEDROCK - and a void skyblock had none, so the first dust was impossible. Now **every new starter island carries one bedrock block at its bottom-center** - the island's heart - so the mod's real ritual works at home, exactly as Flux Networks intended. Alongside it, a crafting recipe presses one dust from redstone sandwiched between two obsidian - the ritual's economics in grid form, for anywhere the heart isn't.

### Added
- **The Powered Up chapter** (#109, now in the Tide group - its variant loop runs through the Dissolution Chamber, so it lives where the chamber does): the v0.6.0 power mods get their questline - 15 quests in a side chapter that climbs the whole campaign. Dielectric paste (hammer-chain clay) opens the Furnator; the Energizing Orb teaches the pack's make-it-first law (orb a resource yourself once and the Dissolution Chamber will slime it); Uraninite and Dry Ice explain split-discovery (the only way to a first roll on a skyblock with no ore and no ice); the crystal ladder runs Blazing -> Niotic -> Spirited -> Nitro; the Flux Networks branch teaches the redstone-on-obsidian craft and goes wireless; the Starter Reactor caps it. All eight modded variants get froglight-check quests. Also: the Botany Pot quest now mentions trees, and the Energy Cell quest gifts a stack of Cable Facades for the cable runs ahead. (The Aerial Pearl stays unquested pending the jetpack-overlap verdict.)

### Fixed
- **Opolis loot boxes actually stay severed now** (#115, reported by Dergib on Discord): slimes were dropping Basic Loot Boxes - labeled DISABLED, yet openable for dirt and cobblestone. The #85 curation cut the recipes but missed BBL Core's global loot modifier and the boxes' own loot tables. Mob drops are off (`Mob Drop Chance = 1.0`), all three box loot tables are overridden empty (boxes already in your chests open to nothing), and the box items are hidden from JEI entirely - no loot boxes from BBL, anywhere. Curation lesson recorded: screen mods for global loot modifiers, not just recipes.
- **The ghost ATM furnace recipes are gone from JEI** (#116, reported by Dergib on Discord): Iron Furnaces ships its Allthemodium/Vibranium/Unobtainium FURNACE recipes unconditioned (unlike the upgrades, which are properly mod-gated), so they rendered in JEI with empty ingredient tags - uncraftable bait. Removed; and no, ATM ores are not planned for the pack.

### Added
- **A title screen that knows what pack it is** (#89, first pass): FancyMenu 3.8.1 (+ Konkrete/Melody, all client-side) with Discord and GitHub buttons on the title screen, and a fully frog-themed splash pool ("Frogs, not pickaxes!", "Plap plap plap plap plap", 28 in all). The **Sky Frogs wordmark** (single line of mossy-stone lettering, a lily pad for the O) replaces the Minecraft logo over the vanilla panorama, with Discord and GitHub buttons bottom-right.

## [0.6.0] - 2026-06-06

The power-and-polish update, and the most community-driven release yet: two power mods join with every one of their materials frog-farmable on day one, the pond gets quieter, your cables get prettier, your pots grow trees, your stuff survives dying, and the welcome chapter now hands you a Discord invite - because most of this release started as somebody's Discord message.

### Fixed
- **The IF Laser Drill is actually disabled now** (playtest catch): the Ore Laser Base and its 46 ore-from-thin-air recipes were live in JEI all along - an old code note wrongly assumed Industrial Foregoing shipped without them. The whole family is stripped (ore recipes, the lava/ether fluid recipes, and the three machine crafts), with DISABLED tooltips. Laser lenses stay craftable as inert decor. Ores and fluids come from frogs.

### Changed
- **Productive Frogs 1.10.0 -> 1.11.0**: Flux Networks and full Powah compat upstream (both dormant here until those mods ship - the PF half of #84 is done), niotic/nitro crystal color fix, and **the Blaze resource is now the blaze rod** (primer and Froglight smelt output; was blaze powder). The pack follows: the netherite scrap slime's chamber input is a blaze rod, the Blaze Singularity compresses rods, and the Blaze quest icon/text match. Existing blaze slimes, Froglights, buckets, and milk carry over untouched; the Spawnery's Infernal primer is still blaze powder (one rod crafts two).
- **Cobblegen Galore curated** (#90): the netherrack, obsidian, and tuff generator recipes are removed - all three outputs are frog resources (Infernal x2, Geode) and singularity inputs, and the #85 ruling stands: no easy way to make resources that frogs are meant to make. The seven builders' stone generators (stone, cobblestone, granite, diorite, andesite, basalt, cobbled deepslate) are untouched; the curation is default-deny, so any generator a future mod update adds stays disabled until reviewed.

### Added
- **Join the Pond** (#111): the welcome chapter now invites you to the community Discord - click the Discord badge floating beside the first quest to open the invite (`discord.gg/r6MhZ73nsM`). Half of this very update started as Discord messages; come say hi. Zero-effort checkmark quest, gates nothing.
- **Powah! (Rearchitected) 6.2.8** (#105, + GuideME): the power-scaling arc. Furnator to Reactor, Energy Cells, the Energizing Orb - and **your frogs farm every Powah material** as of Productive Frogs 1.11: uraninite and energized steel from Cave, dry ice from Tide, blazing from Infernal, niotic/spirited/nitro from Void. On a void skyblock with no ore gen, the Cave pool's split-discovery rolls your first uraninite - the frog is the uranium mine.
- **Flux Networks 8.0.0** (#84): wireless power across your whole base, no cable runs (or facade them where you keep them). **Flux Dust is frog-farmable** (Infernal, alongside obsidian) as of Productive Frogs 1.11 - and the classic bootstrap still works: drop redstone onto obsidian.
- **Dissolution Chamber rows for all eight new variants** - with a new law for modded resources: the chamber input is the resource ITSELF (make energized steel in the Orb before a frog will farm it; drop the redstone on the obsidian yourself first). Vanilla chains keep their prior-resource threading; modded variants are self-keyed so the mod's own mechanic stays in the loop. Uraninite's first copy still comes from Cave-pool split-discovery (its Orb recipes all want ore this skyblock doesn't have); the chamber scales it from one.
- **Extreme Sound Muffler 3.55** (#103, suggested by Dergib on Discord): per-sound muffling, because a full frog farm's plap plaps deserve a volume knob of their own. The muffler button in your inventory lists sounds as they play - silence any of them globally, or drop an anchor that quiets just the pond. Client-side; muffling is opt-in, nothing is deafened by default. The same build ATM10 To the Sky ships (and every other reference pack we checked).
- **Cable Facades 1.5.1** (#100, suggested by Dergib on Discord): wrap your pipes and cables in any block's texture, so the machine room reads as a build instead of spaghetti. The default allowlist already covers Pipez and the whole Mekanism cable family; facades craft from dyes and wool (16 at a time), the removal wrench from iron. Same build Techopolis 3 and Skyopolis Evolved run.
- **Botany Trees 21.1.3** (#96, reported by Dergib on Discord): Botany Pots can finally grow trees. The base mod only ever handled crops and flowers - everyone (the maintainer included) assumed trees worked. The official addon closes the gap; same build ATM10 To the Sky ships.
- **Botany Pots go toolless** (`config/botanypots.json`, new): harvest tools never take durability damage, and every pot acts as if shears are inserted when its tool slot is empty - so leaves and other shears-gated drops just work, no tool upkeep in your automation. (A deliberate divergence from ATM10SKY, which keeps stock tool behavior.)
- **GraveStone Mod 1.0.24** (#92, requested by RayRayZCB on Discord): your items and XP now wait in a grave at your death point instead of despawning in 5 minutes - timely, with the Warden and the dragon both in the campaign. Obituary included; ghosts off. (Corail Tombstone was considered and declined: its perk/teleport progression is a parallel economy.)
- **Inventory Essentials 21.1.2** (#88, Discord suggestion): ctrl-shift-click moves every stack of an item at once, plus single-item and bulk modifier-click transfers - the one gap in the Mouse/Inventory/Crafting Tweaks lineup.
- **Opolis Utilities (BBL Utility) 4.11.10**, curated per six maintainer rulings (#85): the QoL slice ships whole (Drying/Soaking Tables, Cloche, Item Repairer, Home/Death Stones, Breaker/Placer/Crafters, Clicker, Redstone Clock), the **Resource Generator becomes the Builders' Stone Lane** (generates only the 13 stone variants no frog produces - granite to red sandstone), and the rest is severed: no Fluid Generator (fluids are planned frog business), no Catalogue/B-Bucks shop economy, no glow squid/squid summons (their drops are frog resources). Severed items carry DISABLED tooltips.
- **The Builders' Sieve dirt lane grows**: grass seeds at 10% (Discord suggestion by bizarr0, #87 - right-click dirt for grass blocks) plus the classic food lane restored at Ex Deorum's own chances - wheat/pumpkin/melon/beetroot seeds, potatoes, carrots, and the occasional poisonous potato. Food is not a frog resource, so nothing is bypassed; Tier 0 islands just get a seed source besides luck.
- **Industrial Foregoing Souls is back** - with its Warden actually reachable this time. A Discord member's correction (the v0.5.0 removal note was wrong: Ex Deorum's **Sculk Core** makes placed shriekers summon-capable) exposed that the only real gap was a shrieker source. The pack now adds a **Sculk Shrieker recipe** from frog-farmed materials (sculk + echo shards + a bone block), so the chain runs: Void frogs -> shrieker + Sculk Core -> three shrieks -> Warden -> Soul Laser. (#75, #82)

## [0.5.0] - 2026-06-06

The community-suggestions release: the endgame's last crafting gap closed, a decor sieve for builders, a proper performance stack, and a dead mod removed (hence the minor bump). Every change in here traces to player feedback - CurseForge comments and the new community Discord.

### Fixed
- **The Ultimate Singularity is craftable again** (#79, reported by eager_goodall7): `glow_ink_sac` and `obsidian` were the only 2 of the 40 required resources with no slime recipe and no quest. **Glow Ink** joins the Cave chain before redstone (coal -> glow ink -> redstone; redstone stays the capstone and the Geode bridge), with table + chamber recipes and a `cave_frogs` quest. **Obsidian** joins the Infernal chain as netherrack's portal-stone partner (netherrack -> obsidian -> quartz), chamber-only, quested in `infernal_frogs`. Ships with **Productive Frogs 1.10.0**, which reclasses obsidian (and refined_obsidian) cave -> infernal (productive-frogs#142/#143) so the Infernal frog is the one that produces them. `validate_quests.py` grew `Q-SINGULARITY-COVERAGE` so a future variant can never silently reopen this gap.

### Added
- **The Builders' Sieve** (Discord suggestion by Dergib, #76): a curated, manual-only sieving lane for decor - oak sieve + string mesh over **dirt** (every overworld sapling, bamboo, sugar cane, cactus) and **moss** (azaleas, vines, glow lichen, dripleaf, all the flowers). Strictly cosmetic flora: Ex Deorum's default drop tables (ores/gems/seeds) stay disabled, the other five meshes stay dead, and the Mechanical Sieve stays uncraftable. Resources still come from the frogs.
- **Performance stack** (Discord suggestion, #73): Sodium 0.6.13 (client rendering + a far better video settings screen), Lithium 0.15.3, FerriteCore 7.0.3, ModernFix 5.27.11 - the same four ATM10SKY runs on this MC/loader.
- **Configured 2.6.3** (Discord suggestion, #74): edit most mods' configs from inside the game instead of digging through files.

### Removed
- **Industrial Foregoing Souls** (#75). Its entire loop needs a captured Warden, which was unreachable in this pack - it was never quested, dead content, reported by an endgame player. **Heads-up:** any placed Soul Laser / soul pipe blocks become missing content. *(Correction, 2026-06-06, credit to a sharp-eyed Discord member: the original note blamed vanilla's "player-placed shriekers can't summon" rule, but Ex Deorum's Sculk Core specifically overrides that. The actual blocker in Sky Frogs is that no sculk shrieker source ships - Ex Deorum's shrieker drop lives in the netherite-mesh sieve lane this pack disables. A frog-farmable Warden path is therefore buildable if ever wanted; tracked in #82.)*

## [0.4.0] - 2026-06-05

The Tier 6 End gate redesign: bake your way into the End instead of wrestling portal frames, plus the upstream chorus fix. Both reported by eager_goodall7 on CurseForge - thanks!

### Changed
- **The End gate is now the End Cake.** The hand-built 12-frame End portal proved a trap - frames must face inward and a wrong-facing ring silently never lights, which hard-blocked a player at the campaign's climax (#68). The `road_to_void` gateway now bakes Ex Deorum's **End Cake** instead: 3 buckets of milk (plain milk **or any Slime Milk** via the new `#productivefrogs:slime_milk_buckets` tag), an egg between 2 eyes of ender, 3 wheat. Place it and take a bite to reach the End; each cake holds 6 teleports. The eyes-of-ender quest drops from 12 to 2 to match.

### Removed
- **The craftable End Portal Frame recipe** (`kubejs:void/end_portal_frame`, glowstone + soul sand + obsidian). The End Cake is the way in; no orientation trap remains. Frames already placed in existing worlds keep working. (#68)

### Fixed
- **Echo shard slime is craftable again:** Productive Frogs 1.8.1 -> **1.9.2** fixes the Chorus Froglight to smelt to raw chorus fruit instead of popped chorus - the only variant whose froglight output didn't match its primer item - unblocking the echo-shard slime chain and the chorus Singularity (#69). The bump also brings PF 1.8.2 (placed-milk drain timing), 1.8.3 (Coal/Blaze Froglights burn as furnace fuel), and 1.9.0 (Refined Storage support).

### Internal
- New `#productivefrogs:slime_milk_buckets` item tag, built at runtime in `slime_milk_tags.js` via a regex over the registered per-variant milk buckets (PF ships no grouping tag for its 70 buckets).
- Repaired 23 quest descriptions whose sentences were shattered across blank-line paragraph breaks (manual hard-wraps in the lang arrays); `validate_quests.py` grew a `Q-DESC-MIDBREAK` check so the class can't recur.

## [0.3.0] - 2026-06-05

Quality and balance pass on the v0.2 beta: a faster opening, a smoother Cave Slime farm, a drawer-crafting fix, and a mod removal (hence the minor bump).

### Removed
- **Handcrafted.** Its cupboard recipes collided with Functional Storage drawers and broke drawer autocrafting in Refined Storage (#62). Removed rather than chase the recipe conflict. **Heads-up:** any placed Handcrafted furniture in an existing world shows as missing content after updating - it was decorative only.

### Changed
- **Faster opening:** tadpole growth cut from 20 min to 3 min, so your first frogs arrive in ~6 minutes instead of ~23. (#63)
- **Cave Slime farm:** tripled the Cave Slime spawn weight (200 -> 600) so slimes dominate the dark-room pool, and the "A Dark Room" quest now prescribes a minimum room size - at least 5x5 across and 3 blocks tall, with bigger rooms spawning faster. (#65)

### Fixed
- **Refined Storage drawers** now craft and autocraft correctly instead of defaulting to cupboards. (#62)

### Internal
- Added a `cf-comments` tool + skill to read CurseForge feedback and triage it into GitHub issues.
- CI: the release workflow now runs on `actions/setup-go@v6` (Node 24).

## [0.2.2] - 2026-06-04

Hotfix: Cave Slimes now spawn on the starter island.

### Fixed
- **Cave Slimes wouldn't spawn on the starter island.** SkyblockBuilder's default spawn protection disables mob spawning in the chunks around world origin, so the Tier 1 dark-room farm produced nothing until you ran `/skyblock create` to make a distant island. The pack now ships `config/skyblockbuilder/spawn.json5` with `spawnProtectionRadius: 0`, so slimes spawn on the starter island as intended. (#58 - reported by rerezcb + n3twoik)

## [0.2.1] - 2026-06-04

Bug-fix and quality-of-life release on top of the v0.2.0 campaign beta. Fixes two Mekanism-chapter blockers found in playtest and adds three QoL mods.

### Added
- **AppleSkin** - saturation and exact food-value overlay on the HUD and item tooltips. (#53)
- **Fast Leaf Decay** - leaves break shortly after their supporting logs are removed. (#54)
- **FTB Filter System** - smart item filters for Modular Routers / AE2.

### Fixed
- **Steel quest was uncompletable.** It required Mekanism's steel ingot, but AlmostUnified makes the AllTheOres steel ingot the only craftable one. The quest now accepts the AllTheOres Steel Ingot. (#51)
- **Couldn't make Steel Slimes.** The Metallurgic Infuser rejected survival-obtained Iron Slime buckets (an NBT-matching bug); the recipe now takes a Bucket of Iron Slime Milk + carbon. (#52)
- Refreshed the packwiz integrity index (stale file hashes left by the steel-fix commits). (#56)

### Changed
- CI: bumped `actions/checkout` v4 -> v6 and `actions/setup-python` v5 -> v6. (#48, #49)
- Tooling: the quest validator now understands FTB filter-item tasks; added a GitHub Issues workflow guide (`docs/github_issues_best_practices.md`).

### World-breaking
- (none)

## [0.2.0] - 2026-06-02

**First complete-campaign beta.** All six Productive Frogs species tiers are built and playable end-to-end - Cave (ores), Geode (gems), Bog (organics), Tide (the ocean + jetpacks), Infernal (the Nether, via a real fortress expedition), and Void (the End, via a dragon expedition) - capped by the singularity endgame and the Sky Frogs Master Frog trophy. This supersedes the v0.1.0 alpha (Tiers 0-4); the full detail of everything in the build is below. Beta: balance, polish, and art are still in progress. A fresh world is recommended (the Void tier ships a traditional vanilla End).

### Added
- Initial packwiz scaffold (MC 1.21.1 / NeoForge 21.1.230) with FTB utility stack, JEI, Jade, and Tier 0 substrate (Skyblock Builder, Ex Deorum, Forgiving Void, Rain Shield).
- Productive Frogs added from CurseForge (project-id 1552728), pinned at **v1.6.0** - the pack's load-bearing core mod, via packwiz (initially v1.0.1; v1.2.0 unlocked the 57-variant resource set, component-driven Slime Milk, and data-driven spawn eggs; v1.3.0 adds the `mod_loaded`-gated cross-mod crush recipes; v1.4.0 ships the Spawnery appliance, which this pack enables; v1.4.1-1.4.3 add Jade appliance tooltips and rebalance the Geode/Tide/Void resource rosters; **v1.5.0 adds frog stats (Appetite/Bounty/Reach) + breeding via Sweetslime** - which the Scaling the Colony chapter depends on; v1.5.1 moves Lapis from Cave to Geode; v1.5.2 is a patch bump; **v1.5.3 adds JEI recipe pages for the Spawnery + Slime Milker** (frogspawn / slime-milk recipe lookups, tag-driven so pack primer overrides show through) - all additive, pack overrides unaffected; **v1.6.0** ships the organic Bog roster the Tier 3 chapters consume: dirt, mud, clay_ball, moss, mycelium, lily_pad, leather, feather, plus the Industrial Foregoing plastic and pink_slime variants).
- KubeJS 2101.7.2 (+ Rhino) added for pack-side scripting and datapack overrides.
- Tier 0 KubeJS scripts: `first_join.js` (first-launch inventory grant, persistent-guarded) and `anti.js` (disables Ex Deorum sieving - recipe types, sieve/mesh crafting, mesh tooltips, fake-player block cancel).
- Tier 0 slime spawning is pack-owned: a biome modifier adds `productivefrogs:cave_slime` (the Cave / Tier 1 starter parent) to the swamp island, and PF's six default slime-spawn biome modifiers are disabled via `neoforge:none` overrides, so only Cave spawns. PF's light-based placement hook makes it spawn in a dark room.
- `config/skyblockbuilder/world.json5` forces the overworld to `minecraft:swamp` (on-theme; spawns are pack-controlled), and `starter_inventory.json5` is emptied so SkyblockBuilder's default kit doesn't stack on the KubeJS grant.
- Custom chestless starter island: a 5x5 grass-topped dirt platform shipped as a SkyblockBuilder template (generated by `tools/gen_starter_island.py`, wired via `config/skyblockbuilder/templates.json5`), replacing the built-in default island and its chest. First-join grant bumped to 6 oak saplings.
- Welcome (Tier 0) FTB Quests chapter: a 22-quest bootstrap (one of them an optional aside) in the pack voice (`docs/voice_and_tone.md`) - a four-quest intro spine forking into four branches (water source, a bed, cobblestone, and the frog-eggs spine), ending by crafting the Spawnery and synthesizing the first two Bottles of Cave Frog Frogspawn (a breeding pair). Active as of the Productive Frogs v1.4.0 pin.
- Spawnery enablement, pack-side (active as of Productive Frogs **v1.4.0**): `config/productivefrogs-common.toml` sets `[spawnery] enabled = true` (PF ships it off; a normal world has swamps), and a datapack override (`kubejs/data/productivefrogs/tags/item/spawnery_primer/cave.json`, `replace: true`) gates the Cave frog on **cobblestone** instead of PF's iron-ingot default - iron is frog-gated on skyblock and would soft-lock the loop. The Welcome frog-eggs branch builds to it.
- Almost Unified (`almostunified` 1.4.2) with config at `config/almostunified/` to collapse duplicate ingots/dusts/nuggets/etc. that multiple tech mods (Mekanism, All the Ores) each provide into one canonical variant - hiding the rest from the recipe viewer and rewriting recipe outputs. Priority is `minecraft > alltheores > mekanism` (All the Ores wins for ingots/dusts; vanilla always wins). Safe for Productive Frogs: PF's cross-mod slime variants prime off `c:` item tags, so unification doesn't break frog priming.
- Reward-candidate convenience mods, for use as quest rewards: Curios API (accessory-slot framework - slots only, no content mod yet), Crafting on a Stick (portable access to a crafting table and other workstations), and Crafting Station: J/EMI Edition Updated (a crafting block that remembers its recipe and pulls from adjacent inventories; the JEI-integrated fork - modId still `craftingstation` - so JEI's recipe-transfer button works), plus Polymorph as the fork's optional recipe-conflict resolver.
- Food/farming mods (the food set ATM10SKY ships): Farmer's Delight (crops + cooking), Cooking for Blockheads (kitchen multiblock, cookbook, water sink), and Mama's Herbs and Harvest (additional crops/herbs). Establishes a sustainable food economy; starter seeds are granted via quest rewards rather than worldgen.
- Plant/harvest QoL mods: Squat Grow (sneak/"twerk" near saplings and crops to fast-grow them - pairs with the farming mods and bootstraps the first tree quickly) and FTB Ultimine (hold a key to harvest a whole tree or crop patch at once; no ore to vein-mine in the void, so it doesn't dent the no-mining pillar). Squat Grow pulled in Cloth Config API as a dependency.
- Opening-loop conveniences: an optional **"Two Shortcuts"** Welcome-chapter quest that teaches Squat Grow + FTB Ultimine and how to use them, and **logs-direct crafting recipes** via KubeJS (`kubejs/server_scripts/log_recipes.js`) - 2 logs -> 16 sticks and 8 logs -> 4 chests off the `#minecraft:logs` tag (break-even ratios, every wood), so early crafting can skip the plank step.
- Toast Control (`toastcontrol`, depends on Placebo which we already ship) with `config/toastcontrol-client.toml` blocking the vanilla **tutorial** ("Move with WASD" etc.), **recipe-unlock**, and **advancement** toasts - FTB Quests is the progression UI, so the vanilla toasts are redundant noise.
- **Your First Iron Ingot** (Tier 1 Cave) FTB Quests chapter (`config/ftbquests/quests/chapters/your_first_iron_ingot.snbt`): two converging paths off the Welcome frogspawn gate - a **frog path** (build an enclosed habitat; craft a lead so frogs can't jump into the void) and a **slime path** (craft a Slime Milker, craft an Iron Slime in a Bucket, milk it into Iron Slime Milk) - meeting where a Cave Frog eats an Iron Slime to drop an Iron Froglight, smelted into the first iron ingot. Rewards: Good Food (Noodle Soup, Pasta with Meatballs, Barbecue on a Stick), an empty bucket, a Diamond Stick, and XP.
- Iron Slime bootstrap recipe (`kubejs/server_scripts/iron_slime_bucket.js`): a shaped KubeJS recipe - cave frogspawn bottle + slime balls + string + bone meal + an empty bucket -> an Iron Slime in a Bucket (`productivefrogs:slime_bucket` stamped with the iron variant). Breaks PF's iron-ingot priming soft-lock on a void skyblock: no iron is spent. Milked in the Slime Milker it yields Iron Slime Milk that spawns Iron Slimes (each placed source depletes after a batch, so you re-milk to sustain it). The output carries both `Variant` and `Category` in `bucket_entity_data` to match PF's JEI subtype.
- Construction Sticks (`constructionstick`, project-id 1156098, `1.3.0`) - the tiered building-stick mod ATM10 ships; its **Diamond Stick** is the "Milk It" quest reward.
- Functional Storage (`functionalstorage` 1.5.5) + its Titanium dependency - the drawers mod the ATM packs ship. The Welcome chapter's Cobblestone Generator quest now rewards an Oak Drawer (1x1) instead of XP.
- FTB XMod Compat + FTB JEI Extras (the builds both ATM reference packs ship) - XMod Compat wires FTB Quests into JEI/REI/EMI (recipe viewing + the quest editor's item picker); JEI Extras is a stand-in JEI helper for mods lacking their own plugin.
- **Scaling the Colony** FTB Quests chapter (`config/ftbquests/quests/chapters/scaling_the_colony.snbt`): the post-iron sustainability chapter, two branches off the Your First Iron Ingot capstone. A **sugar branch** - hammer cobble -> dust, barrel-mix to clay, fire terracotta + a flower pot, craft a Botany Pot (-> sugar cane), then sweetslime - which unlocks frog breeding, capped by a breeding/stats quest that teaches PF's Appetite / Bounty / Reach. A **mud branch** - compost organic matter into dirt, water-bottle it into mud, lay a 3x3 mud-over-hopper floor, and feed it into an Iron Furnace - that auto-catches and smelts Froglights hands-free (mud's reduced height lets dropped items fall through into the hopper below). Rewards include a hopper, a Functional Storage drawer, sugar cane, sweetslime, and good food.
- Iron Furnaces (`ironfurnaces` 4.3.2, the ATM build) - its furnace auto-pushes smelted output into an adjacent inventory, the heart of the hands-free Froglight auto-smelter.
- **Tier 1: Cave Frogs** chapter (`cave_frogs.snbt`): the vanilla Cave ore chain, threaded so each step needs the prior resource's Slime Milk - Beyond Iron (gated behind Scaling the Colony) -> Copper -> Gold -> Coal -> Redstone, each tasking the player to produce that resource via the frog loop. Each material quest rewards a Functional Storage **Compacting Drawer** (one per metal - a per-resource drawer wall; the iron drawer sits on the Your First Iron Ingot capstone), and the **Advanced Feeding Upgrade** moved to the chapter-closing **The Road to Geode**. Backed by the seed-chain recipes (`kubejs/server_scripts/cave_slime_chain.js`): prior Slime Milk + 4 stone + 3 sweetslime + 1 Cave frogspawn -> the next resource's slime-in-a-bucket. Lapis moved to Geode (PF v1.5.1), obsidian deferred to the Infernal gate, glow_ink_sac omitted, and the modded Cave metals (osmium, tin, ...) are deferred to their tech-mod chapters (osmium = the Mekanism opener).
- Cave -> Geode tier gateway: the Cave Frogs capstone "The Road to Geode" primes the Spawnery with **redstone** (via a `spawnery_primer/geode` -> `minecraft:redstone` datapack override) to draw a Geode Frogspawn bottle, opening Tier 2 - redstone is the Cave chain's finale, so finishing Cave hands you the key to Geode. Corrected the tier-transition mechanic in `progression.md` (Spawnery-frogspawn + a resource seed-chain, **not** "parent slime milk," which PF doesn't implement), and recorded the chapter-sizing principle (theme + arc, ~8-20 nodes, one per progression beat) in `quest_book.md`.
- **Storage and Crafting** chapter (`storage_and_crafting.snbt`): the Tier 1 storage interlude after Cave Frogs (gated off Cave's Copper quest). A branch-and-merge layout - a barrels limb (Sophisticated barrel, tier it to gold, parallel stack + pickup upgrades, then a Sophisticated controller network), a drawers limb (a Functional fluid drawer, then network the Cave compacting-drawer wall via a Functional controller), and an extras limb (a Mekanism Basic Fluid Tank - iron + redstone - and a Trash Can) - all converging on a capstone that requires the full suite. Nodes pay out thematic storage gear; the drawer nodes also grant the Functional **Configuration** and **Linking** tools and "One Window" grants the Sophisticated **Storage Tool**, sidestepping their emerald/diamond/ender-pearl crafting gates.
- Quartz-free storage networking (`kubejs/server_scripts/storage_quartz_free.js`): re-issues the Sophisticated + Functional storage controller recipes without nether quartz (comparator -> repeater, quartz_block -> redstone block), making the analog no-power network a Cave-era stopgap. Refined Storage at the Infernal tier stays the real digital upgrade.
- Inventory Tweaks ReFoxed (`invtweaks` 1.21.1-1.3.2) - the ATM-standard inventory sorter; bind "Sort Inventory Under Cursor" to the middle mouse button for middle-click sort, plus auto-refill.
- FTB Quests **chapter groups**: `chapter_groups.snbt` defines a "Tier 1: Cave" sidebar header grouping Your First Iron Ingot, Scaling the Colony, Cave Frogs, and Storage and Crafting; Welcome stays ungrouped at the top. The chapter formerly titled "Tier 1: Cave Frogs" is now just "Cave Frogs" (the prefix lives in the group header).
- Adopted FTB Quests' lang-file format: quest titles and descriptions live in `config/ftbquests/quests/lang/en_us.snbt` (keyed by quest ID); chapter files hold structure only. Generated `data.snbt` (questbook settings, `progression_mode: linear`) alongside.
- **Tier 2: Geode** chapters (`road_to_geode.snbt`, `geode_frogs.snbt`, `mekanism.snbt`): the gem tier. **Road to Geode** bridges Cave to Geode with Cave-era means - prime the Spawnery with redstone (`spawnery_primer/geode` -> `minecraft:redstone`) for a Geode Frogspawn bottle, then bootstrap the first gem off the Cave's last resource (a redstone-milk -> lapis-slime seed). **Geode Frogs** runs the gem chain lapis -> tuff -> calcite -> amethyst -> emerald -> diamond. **Mekanism** is the tier's automation verb: osmium bootstrap (`kubejs/server_scripts/osmium_slime_bucket.js`) -> heat generator -> Metallurgic Infuser -> steel -> Enrichment Chamber. Backed by `kubejs/server_scripts/geode_slime_chain.js`.
- **Slime Milk catalysts** (PF v1.7.0) introduced via a quest branch off the Geode diamond capstone (`geode_frogs.snbt`): Count -> Speed -> Quantity -> **Infinite Count** (its recipe rings 8 Count catalysts around a diamond, so it lands exactly at the diamond gate). Drop a catalyst into a placed Slime Milk source to buff it (more spawns before drying up / faster / more per batch / never runs dry); buffs save to the source and survive bucketing. `kubejs/server_scripts/catalyst_recipes.js` re-issues the Quantity catalyst with **redstone** instead of glowstone (glowstone is Infernal-gated on a void skyblock), so all four are craftable at the diamond point; PF's default glowstone recipe is untouched for other packs.
- Steel Slime via the Metallurgic Infuser (`kubejs/server_scripts/steel_slime_infusing.js`): infuse an Iron Slime in a Bucket with carbon into a Steel Slime (the same iron-and-carbon trick that makes steel itself; the input uses a `neoforge:components` ingredient so only the iron slime matches). Feeds the optional Mekanism-chapter Steel Slime quest, which carries the steel Froglight check; the main Steel quest stays a Mekanism craft (`mekanism:ingot_steel`).
- Geode-chapter mods: **Building Gadgets** (`buildinggadgets2`, the Enrichment Chamber quest reward + the Exchanging Gadget optional in the Tools and Things chapter), plus **Dark Utilities**, **More Overlays Updated**, and the alternate-glyph mods **Nyctography**, **Pig-Pen Cipher**, and **Runelic** (utility and decorative, added in the same pass; not yet wired into quests).
- **Just Dire Things** (`justdirethings` 1.5.7) - Direwolf20's utility mod, added for the **Item Collector** capstone of the Tools and Things chapter (vacuums dropped Froglights/slimes off the habitat floor). Tiered automation blocks and a deep utility set the pack can lean on more in later tiers.
- **Tier 3: Bog** chapters (`road_to_bog.snbt`, `bog_frogs.snbt`): the organic/swamp tier. **Road to Bog** bridges Geode to Bog (Enrich a Diamond in the Enrichment Chamber -> prime the Spawnery with enriched diamond, `spawnery_primer/bog` -> `mekanism:enriched_diamond`, for a Bog Frogspawn -> a mossy-cobblestone-gated dirt-slime bootstrap) and depends on both the gem chain and the Mekanism Enrichment Chamber, so the tier cannot open before the player has the means to enter it. **Bog Frogs** runs the organic chain dirt -> mud -> clay_ball -> moss -> mycelium -> lily_pad -> leather -> feather -> plastic -> pink_slime (capstone). Seed-chain recipes in `kubejs/server_scripts/bog_slime_chain.js`.
- **Industrial Foregoing** + **Industrial Foregoing Souls**: the Bog tier's verb. `kubejs/server_scripts/if_plastic_gate.js` removes IF's only traditional plastic recipe (by id, so the Bog plastic Froglight's smelt survives), making the Bog plastic-frog the sole source of plastic and hard-gating all of Industrial Foregoing behind the Bog tier. The pink-slime Froglight is the Bog capstone (rewards one each of tier-2 Speed / Efficiency / Processing machine addons).
- **Tools and Things chapter** (`config/ftbquests/quests/chapters/tools_and_things.snbt`): the Bog tier's verb chapter, walking the player through **Just Dire Things' natural tier-1 progression**. Spine: Primogel Goo Block (intro hexagon, gated on the bog_frogs mycelium quest) -> Ferricore Ingot -> Fluid Collector -> Fluid Placer -> Item Collector (hexagon capstone). Optional **Building Gadgets 2** side branch: Exchanging Gadget -> Copy/Paste Gadget. The JDT fluid pair (Collector + Placer) anchors the spine so the player commits to building it, not skips past as an optional. Simple Block Breaker / Auto-Breaker dropped from the spine (player will discover it via JEI when they need an auto-farm loop; the JDT description text already tells them how). Simple Generator dropped (the player has Mekanism power infrastructure from Geode by this point - free RF for the JDT machines). Simple Clicker dropped (recipe needs ender_eye / blaze powder, Infernal-gated on skyblock). Primogel Goo Block's recipe is overridden to require mycelium in the centre (`kubejs/server_scripts/jdt_recipes.js`), so the JDT entry gates naturally on Bog's mid-tier mycelium frog.
- **Road to Tide chapter** (`config/ftbquests/quests/chapters/road_to_tide.snbt`) in a new **Tier 4: Tide** chapter group: the Industrial Foregoing spine that ends Bog and bridges into Tide. Pity Machine Frame (intro hexagon) -> Fluid Extractor -> **Dissolution Chamber** (capstone hexagon, "The Slime Engine"). Entry gates on the bog_frogs pink_slime capstone, so the chapter opens when Bog finishes. The chamber description introduces the **pack's slime engine** - every variant in Cave/Geode/Bog has a resource-threaded chamber recipe (21 rows in `kubejs/server_scripts/dissolution_slime_recipes.js`; iron bootstraps off bone meal); Tier 4+ rows land per tier as each ships. Resource-keyed inputs sidestep IF/Titanium's JSON-codec drop of `neoforge:components` ingredients (PF declined a per-variant component-free handle; closed [productive-frogs#127](https://github.com/Flatts3000/productive-frogs/issues/127) as won't-fix). Existing crafting-table chains stay as a parallel hand-craft path. Tide-specific content (Spawnery primer, first Tide slime, Tide frogs) extends this chapter when Tier 4 ships.
- **Froglight-check principle** (pack-wide): per-tier resource quests detect the variant Froglight (`productivefrogs:configurable_froglight` carrying a `productivefrogs:slime_variant` component) rather than the smelted resource, so the frog loop cannot be bypassed with a resource obtained another way. Exceptions: the Your First Iron Ingot capstone (the tutorial that teaches the smelt; the Froglight is already gated upstream by its Feed the Frog quest) and the main Mekanism Steel quest (steel via the infuser is a craft, not a frog resource), where the optional steel-slime quest carries the check instead.
- **Per-tier slime-chain filler blocks**: each tier's slime-in-a-bucket seed-chain recipe takes 4 of a tier-themed block per step, for flavor and anti-repetition - Cave = stone, Geode = gravel (the Ex Deorum block you sieve gems from), Bog = mossy cobblestone (made in Mekanism's Metallurgic Infuser or Enrichment Chamber). A tier's filler must be mass-attainable at that tier (not gated behind a later tier).
- **Road to Tide bridge (Tier 4 gateway)**: extended `road_to_tide.snbt` past the Dissolution Chamber into the Bog -> Tide transition - Tide Frogspawn (Spawnery primed with pink_slime) -> A Bucket of Prismarine Slime (from the chamber) -> Milk It -> First Prismarine (Froglight capstone). Wired the Tide tier into the slime engine: a TIDE row in `dissolution_slime_recipes.js` (the 6 aquatic variants - prismarine, prismarine_crystals, sponge, ink_sac, sea_pickle, nautilus_shell - prismarine bridging off `industrialforegoing:pink_slime`, `minecraft:mycelium` filler) and a `spawnery_primer/tide.json` override (pink_slime primes Tide). **Tide and every later tier are Dissolution-Chamber-only** - no crafting-table slime chain (the chamber is built by Tier 4); Cave/Geode/Bog keep their hand-craft chains as the path to the chamber. Tide's filler is **mycelium** - the first filler that is itself a frog-chain resource (the Bog mycelium variant), a deliberate convention departure that's safe because mycelium is mass-renewable via the Bog loop before Tide. Only the first variant (prismarine) is quested this pass; the remaining 5 wait on the `drowned_riches` species chapter.
- **Tier 4 (Tide) finished**: the `drowned_riches.snbt` species chapter quests the rest of the aquatic roster (prismarine_crystals -> sponge -> ink_sac -> sea_pickle -> nautilus_shell, all chamber-made, each a Froglight check with `match_components: strict`), and the `take_flight.snbt` chapter introduces Tide's **new verb: jetpacks (mobility)** via **Iron Jetpacks** (added, with its Cucumber Library dependency). Coil-tiered progression - Leather Strap -> Basic Coil -> first jetpack -> Fuel and Fly (charge with Geode RF) -> Advanced/Elite/Ultimate Coil - on frog-farmed resources (iron -> gold -> diamond -> emerald) plus Forge Energy from the Geode-era Mekanism setup; no recipe override needed (every ingredient is frog-attainable). First *mobility* verb in the pack (all prior verbs were stationary).
- **Quest validation system** ([`docs/quest_testing.md`](docs/quest_testing.md)): `tools/validate_quests.py` statically checks every chapter + lang file for the bug classes this pack keeps hitting - the tier-skip exploit (`match_components` missing), dangling/cyclic dependencies, negative-leading or duplicate IDs, em-dashes, dead lang entries, and quest-vs-recipe variant drift. Self-verifying (clean on the current pack; fails on an injected bug). Gated by a CI workflow (`.github/workflows/validate-quests.yml`) and an opt-in pre-commit hook (`.githooks/pre-commit`). Complemented by an in-game `/sf_selftest` (`pack/kubejs/server_scripts/selftest.js`) that confirms runtime fixes - per-variant items exist and Slime Milk buckets carry no craft remainder.
- **Good Food Loot Crate** ([`reward_tables/7F00D00000000001.snbt`](pack/config/ftbquests/quests/reward_tables/7F00D00000000001.snbt)): the pack's first FTB reward table - a 32-food pool (the whole `gen/good_food_map.md` set minus the retired vegetable_soup) granted as a `type: "loot"` physical openable crate (table_id `9151543141235425281L`). The 20 pre-existing hand-picked food rewards across 9 chapters were bulk-converted to it, retiring the manual per-quest draw-queue; FTB now rolls the random food at claim time. SNBT shape modeled on the Sky Bees Reborn reference table. New validator guards `Q-REWARD-TABLE-RESOLVES` (every `loot`/`random`/`choice` `table_id` resolves to a real table) and `Q-REWARD-TABLE-ORPHAN`, with reward-table ids/entries flowing through the existing id and item checks.
- **Players Only** (optional Cave-tier quest in `cave_frogs.snbt`): introduces Dark Utilities' **Mob Filter** blocks - a solid wall everything but one entity type can pass through. The Player filter (only you pass) seals a frog pen without a ledge-lead; the description points players at the rest of the family (Slime, Hostile, Animal, Undead, ...). An optional diamond-shaped side branch off the Cave **Gold** quest (the `filter_player` recipe needs a golden pickaxe, so it is naturally Cave-gold-gated), rewarding a Good Food Crate. Dark Utilities was already pinned (`darkutils` 21.1.1).
- **Quest subtitles** (P0 of the [quest-system audit](docs/audits/quest_system_audit_2026_05_31.md)): all 123 named quests now carry a one-line `quest_subtitle` hook in `lang/en_us.snbt` (e.g. Copper -> "The first new metal", Diamond -> "From a frog. Really."), written in the pack voice. Pure additive lang work; shape verified against ATM10SKY's lang. Big readability gain on the canvas with no mechanical change.
- **Decoration mod pack-in** (21 mods, all from the ATM10-To-the-Sky 1.21.1 set): the **Macaw's** suite (Bridges, Doors, Windows, Roofs, Fences & Walls, Trapdoors, Paths & Pavings, Lights & Lamps, Paintings, Furniture), **Supplementaries**, **Handcrafted**, **FramedBlocks**, the chiseling/variant stack (**Chipped**, **Chisel Reborn** + **Chisel-Chipped Integration**, **Rechiseled** + **Rechiseled: Chipped**, **CTM**), and glass (**Connected Glass**, **Glassential Renewed**). Pulls in five library deps (Moonlight, Resourceful Lib, Athena, Fusion, Cryonic Config). Gives builders hundreds of variants off frog-farmed base blocks plus full build-decor coverage, with no new ore/resource requirements. Added via `packwiz cf add`; Chisel Reborn pinned by project id (551763) to disambiguate from the legacy Chisel slug.
- **Tier reward crates** (`reward_tables/7F1C…`/`7F2E…`/`7F3B…`/`7F4D…`): four category loot crates (Cave / Geode / Bog / Tide), each a weighted 3-group table - a rare **processing block** (Blast Furnace, Enchanting Table, Jukebox, Chiseled Bookshelf, ...), occasional **components** (4x Hopper, 4x Redstone Repeater, 4x Lightning Rod, ...), and a common **resource stack** (64x Glass, 64x Smooth Stone, 64x Cut Copper, ...). Weighting is stack-common / components-occasional / block-rare for a "jackpot" feel. Contents are restricted to **fully-prior-tier + Tier-0 materials and recipe-gate-checked**, so a crate never grants something the player cannot yet craft - no quartz / glowstone / obsidian below Infernal, even where hidden in a recipe (comparators, observers, diorite/andesite/granite all secretly need quartz); the Enchanting Table is a single deliberate vanilla-style out-of-order grant.
- **Quest shape hierarchy** (P2 of the [quest-system audit](docs/audits/quest_system_audit_2026_05_31.md)): quest types now read at a glance on the canvas - **hexagon** = milestone/capstone (29), **square** = resource-check Froglight quest (22), **diamond** = optional side content (6), default **circle** = process step. Pure presentation; no mechanical change.
- **Refined Storage suite** (the ATM10 set, all 1.21.1 / NeoForge): **Refined Storage** core (2.0.8) + **Extra Storage**, **Extra Disks**, **RS Curios Integration**, **RS Mekanism Integration**, **RS JEI Integration**, **RS Quartz Arsenal** (+ EdivadLib dep). This is the planned **Tier 5 (Infernal) verb** - the digital storage network. Naturally progression-gated: RS components require Quartz Enriched Iron (nether quartz), which on this skyblock only the Infernal frog produces, so RS stays inert until Infernal. Added ahead of the Tier 5 quest content.
- **Tier 5 (Infernal)** - the nether-on-skyblock tier (chapter group "Tier 5: Infernal", 3 chapters, 20 quests). The Infernal frog produces the materials a void skyblock can't otherwise reach: quartz, glowstone, blaze, netherrack, soul sand/soil, and netherite scrap.
  - **Road to Infernal** (gateway): the pack's one real **Nether expedition.** A Portal to the Nether (the gateway grants 14 obsidian + flint) -> Into the Nether (dimension task) -> Raid a Fortress (mine nether brick) -> Infernal Frogspawn (prime the Spawnery with nether brick) -> Netherrack Slime (chamber) -> Milk It -> First Netherrack. The Infernal Spawnery primer is **nether brick** (`spawnery_primer/infernal.json = minecraft:nether_bricks`): it isn't craftable pre-Infernal (netherrack is the first Infernal resource), so a fortress is its only source - which forces the expedition. Nether fortresses + bastions are enabled via `config/skyblockbuilder/structures.json5` (SkyblockBuilder whitelists no structures by default; matches ATM10-To-the-Sky). The Tide jetpack makes the void-Nether crossing feasible.
  - **Infernal Frogs** (species chain): quartz -> glowstone -> soul sand -> soul soil -> blaze -> **netherite scrap** (the vanilla-endgame capstone), Froglight checks.
  - **The Network** (verb = **Refined Storage**): Quartz Enriched Iron -> Controller -> Grid -> Disk Drive -> Cable -> External Storage -> Import/Export -> Crafting Grid -> **Autocrafting** (Pattern Grid + Autocrafter). Gated on quartz (RS components need Quartz Enriched Iron), so it stays inert until Infernal.
  - Dissolution `INFERNAL` row (filler = **prismarine**, a Tide resource - netherrack would be circular), the nether-themed **Infernal tier crate**, full lang.
  - `Q-ITEM-EXISTS` allowlist extended with the 512 Refined Storage-family item ids.
- **Tier 6 (Void)** - the campaign's final tier and endgame (chapter group "Tier 6: Void", 4 chapters, 28 quests). The Void frog produces the End's materials, and the tier ends in the Master Frog trophy. **Completes the content campaign - all six species playable end to end.**
  - **Road to the Void** (gateway): the pack's one real **End expedition.** Pearls from the Dark (gather 12 ender pearls from dark-room endermen) -> Eyes of Ender -> Frame the Void (craft a 12-frame End portal - no stronghold generates on a void skyblock, so glowstone + soul sand press into `end_portal_frame` via `kubejs/server_scripts/void_recipes.js`) -> Into the End -> **Slay the Dragon** (a `kill` task; the climax) -> the frog sub-chain (Void Frogspawn -> Ender Pearl Slime -> Milk It -> First Ender Pearl). The resource chain branches off *reaching* the End, so the dragon kill gates only the endgame, not progression. Void Spawnery primer = **ender pearl** (`spawnery_primer/void.json`).
  - **Void Frogs** (species chain): end_stone -> chorus_fruit -> echo_shard -> sculk -> **shulker_shell**, Froglight checks. Six vanilla End variants total (ender_pearl in the gateway); modded Void variants stay deferred until their mods join.
  - **The Ultimate Table** (verb = **Extended Crafting**, pinned 7.0.8): black iron -> luminessence -> basic/advanced/elite/**ultimate** crafting tables -> the **Quantum Compressor**. All ingredients frog-farmable (iron/gold/diamond/emerald blocks + black dye from Tide ink); no recipe overrides needed.
  - **Master Pond** (endgame): one **Singularity** per vanilla froglight resource - **40 in all** (`config/extendedcrafting/singularities/*.json`, generated by `tools/gen_singularities.py` from PF's `slime_variant` data, frog-matched colors). Each compresses from 1000 of its resource in the Quantum Compressor (40,000 resources + 40 Ultimate Catalysts across the set - a proof you automated *every* farm). All 40 fold into the **Ultimate Singularity** (EC ships zero default singularities, so the auto-generated Ultimate requires exactly these 40) -> the **Sky Frogs Master Frog** trophy (`kubejs:master_frog`, a KubeJS item with a placeholder texture) -> a closing epilogue. EC's per-singularity material count lowered 25000 -> 1000 (`extendedcrafting-common.toml`). (The compressor input is the smelted resource, not the Froglight directly: EC's singularity `ingredient` and the compressor's Cucumber `IngredientWithCount` input are both item/tag-only and reject the `neoforge:components` matcher needed to tell froglight variants apart, and a tag cannot help since all variants share one item id - confirmed by reading the EC + Cucumber jars. On this skyblock each resource's only source is its frog, so every singularity stays froglight-gated.)
  - Dissolution `VOID` row (filler = **soul soil**, an Infernal resource - end stone would be circular), the End-themed **Void tier crate** (`7F60…`), full lang. `Q-ITEM-EXISTS` allowlist extended with the Extended Crafting item ids + `kubejs:master_frog`.
- Design docs under `docs/` and community health files.

### Changed
- Pinned to MC 1.21.1 (Ex Deorum and Skyblock Builder have no 1.21.4+ NeoForge builds).
- CurseForge-only distribution (FTB stack blocks Modrinth).
- Adopted Productive Frogs v1.0.0's species category names across all docs (METALLIC to Bog, MINERAL to Cave, GEM to Geode, AQUATIC to Tide, ARCANE to Void; Infernal unchanged). Vanilla `minecraft:slime` / `magma_cube` are no longer parent species.
- Tier 0 reshaped to the species-gated model: the starter species is **Cave** (ores), farmed as a dark-room `cave_slime` farm. Progression is Cave -> Geode -> Bog -> Tide -> Infernal -> Void, each tier gated by crafting the next species' frogspawn bottle + Slime Milk. Ex Deorum is porcelain bucket + crucibles + rain-collection barrels only.
- Quest reward cleanup: any quest whose reward set already grants an item no longer also grants XP (the Your First Iron Ingot capstone, the Storage and Crafting capstone, and Cave's The Road to Geode). XP-only milestone quests are unchanged.
- Productive Frogs pin **v1.5.3 -> v1.7.0** (v1.6.0: organic Bog roster - dirt / mud / clay_ball / moss / mycelium / lily_pad / leather / feather, plus the Industrial Foregoing plastic and pink_slime variants the Bog chapters consume; v1.7.0: the four Slime Milk catalysts that buff placed Slime Milk sources). Additive; pack overrides unaffected.
- Productive Frogs pin **v1.7.0 -> v1.8.0** (per-variant Slime Milk: each variant now has its own fluid + source block + bucket, so tank/pipe automation preserves the variant). **Not additive** - the old single `productivefrogs:slime_milk_bucket` (variant in a `slime_variant` component) is replaced by per-variant items `productivefrogs:<variant>_slime_milk_bucket`, so the pack remapped all 11 milk-bucket references: the Cave / Geode / Bog seed-chain scripts + the osmium bootstrap (`*_slime_chain.js`, `osmium_slime_bucket.js`) and the iron / lapis / dirt milk-bucket quest tasks + icons (`your_first_iron_ingot.snbt`, `road_to_geode.snbt`, `road_to_bog.snbt`). Upstream this is world-breaking (Slime Milk placed in a pre-1.8 world, and milk buckets in inventories, become air); on a pre-release alpha the fix is to re-mill from Slime Buckets.
- Productive Frogs pin **v1.8.0 -> v1.8.1** (Slime Bucket fixes: a dispenser can release a captured slime; releasing no longer dumps a water source; a released slime is always size 1). Bugfix/additive - no item-id or recipe changes, pack unaffected.
- Sophisticated Storage pin bumped to `1.5.52.1756` (matched a CurseForge-launcher patch bump that landed in the dev instance; patch only, no other pins touched).
- IF optional branch swap (historical, superseded by the Tools and Things rewrite): the Plant Gatherer (redundant with Botany Pots) and Sludge Refiner quests were dropped in favour of an Item Collector + Exchanging Gadget showcase before the chapter was renamed to Tools and Things and the spine refocused on JDT's tier-1 progression.
- JDT **Primogel Goo Block** (`justdirethings:gooblock_tier1`) re-issued with **mycelium** instead of dirt (`kubejs/server_scripts/jdt_recipes.js`). Mycelium is a Bog Frogs chain variant, so this gates the JDT entry into the Bog mid-tier progression naturally; JDT's stock dirt recipe is left intact for other packs.
- `road_to_bog` capstone quest title **"First Dirt" -> "Dirt"** (the "First X" gateway pattern reads awkward; the resource-name pattern from the gem chain reads cleaner). The `road_to_geode` capstone still says "First Lapis" - left for a separate decision.
- Quest UX (P0 of the [quest-system audit](docs/audits/quest_system_audit_2026_05_31.md)): lock icons are now shown (`show_lock_icons: true`) with a themed `lock_message`. (A `hide_until_deps_complete` step-by-step reveal on the species chains was tried and **reverted** - playtest feedback wanted resource chains fully visible, and it wrongly concealed the optional Geode catalyst side-branch.)
- Quest reward model: the placeholder XP rewards are replaced by a **mix of crates** - hexagon milestone quests roll their tier's category crate, routine process steps roll the Good Food Crate (Welcome stays on Food; 25 Food + 14 category backfills). **Every existing item/block reward is left untouched** (the per-resource drawers, capstone items, etc. stand as they were).

### Removed
- All `type: "xp"` quest rewards - they were placeholders; rewards are now item/block grants and loot crates (see Changed).
- Rain Shield (conflicted with Ex Deorum barrel rain collection inside the player's claim).
- Pack-side `slime_spawns.json` biome modifier (it targeted vanilla `minecraft:slime`, which PF v1.0.0 no longer uses as a parent; PF ships its own `bog_slime` biome modifier).

### Fixed
- **Tier-skip exploit: quest item tasks ignored their component filter.** One Copper Froglight completed every Cave Frogs quest, and a Cave frogspawn completed The Road to Geode. FTB Quests item tasks match by item id and ignore the `components` filter unless `match_components` is set; our froglight / frogspawn / slime-bucket tasks specified the discriminating component but lacked the flag. Added `match_components: "strict"` to all 32 component-discriminated item tasks across 9 chapters (strict = exact match, which fits since every checked component is exactly stamped on the item).
- **Slime-chain crafting duplicated the bucket.** PF Slime Milk buckets carry a `minecraft:bucket` craft remainder, so a `milk bucket -> slime in a bucket` craft returned the empty bucket on top of the slime bucket (net +1 bucket per craft). `kubejs/startup_scripts/milk_bucket_no_remainder.js` clears the craft remainder on all `*_slime_milk_bucket` items, so the milk bucket now becomes the slime bucket (1 in, 1 out). The slime chains are the only crafting use of milk buckets, so there's no collateral.
- Sweetslime showed "Missing Item" in the Scaling the Colony quests: the pack was pinned at PF **1.4.3**, but `productivefrogs:sweetslime` (and the frog-stats breeding system the chapter teaches) are **v1.5.0** features. Updated the PF pin **1.4.3 -> 1.5.1** (also makes Lapis -> Geode live). The 1.5.x changes are additive plus the Lapis recategorization, which the Cave chain already excludes - no collateral.
- Removed the redundant "Wire up the auto-smelter" checkmark from the Hands-Free Froglights quest; crafting the Iron Furnace is the single task.
- Welcome chapter dependency tree was severed: the four branches (water / bed / cobble / frog-eggs) drew no dependency lines and Wood to Stand On showed "No Dependants". Root cause was hand-authored FTB Quests IDs that lead with hex `8-F` - FTB parses IDs as signed longs and rejects negative ones, regenerating them on load and dropping every dependency that referenced them. Remapped all 62 negative-leading IDs into the positive range (leading digit minus 8) via the new `tools/fix_quest_ids.py`; dependency references remap identically and stay linked. Authoring rule going forward: FTB Quests IDs must lead with hex `0-7`.

---

## Release template

```markdown
## [v0.x.y] - YYYY-MM-DD

### World-breaking
### Added
### Changed
### Removed
### Fixed
```

[Unreleased]: https://github.com/Flatts3000/sky-frogs/compare/v1.8.0...HEAD
[1.8.0]: https://github.com/Flatts3000/sky-frogs/compare/v1.7.0...v1.8.0
[1.7.0]: https://github.com/Flatts3000/sky-frogs/compare/v1.6.2...v1.7.0
[1.6.2]: https://github.com/Flatts3000/sky-frogs/compare/v1.6.1...v1.6.2
[1.6.1]: https://github.com/Flatts3000/sky-frogs/compare/v1.6.0...v1.6.1
[1.6.0]: https://github.com/Flatts3000/sky-frogs/compare/v1.5.3...v1.6.0
[1.6.0]: https://github.com/Flatts3000/sky-frogs/compare/v1.5.3...v1.6.0
[1.5.3]: https://github.com/Flatts3000/sky-frogs/compare/v1.5.2...v1.5.3
[1.5.2]: https://github.com/Flatts3000/sky-frogs/compare/v1.5.1...v1.5.2
[1.5.1]: https://github.com/Flatts3000/sky-frogs/compare/v1.5.0...v1.5.1
[1.5.0]: https://github.com/Flatts3000/sky-frogs/compare/v1.4.4...v1.5.0
[1.4.4]: https://github.com/Flatts3000/sky-frogs/compare/v1.4.3...v1.4.4
[1.4.3]: https://github.com/Flatts3000/sky-frogs/compare/v1.4.2...v1.4.3
[1.4.2]: https://github.com/Flatts3000/sky-frogs/compare/v1.4.1...v1.4.2
[1.4.1]: https://github.com/Flatts3000/sky-frogs/compare/v1.4.0...v1.4.1
[1.4.0]: https://github.com/Flatts3000/sky-frogs/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/Flatts3000/sky-frogs/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/Flatts3000/sky-frogs/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/Flatts3000/sky-frogs/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.14.0...v1.0.0
[0.14.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.13.1...v0.14.0
[0.13.1]: https://github.com/Flatts3000/sky-frogs/compare/v0.13.0...v0.13.1
[0.13.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.12.0...v0.13.0
[0.12.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.10.1...v0.11.0
[0.10.1]: https://github.com/Flatts3000/sky-frogs/compare/v0.10.0...v0.10.1
[0.10.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.9.1...v0.10.0
[0.9.1]: https://github.com/Flatts3000/sky-frogs/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.7.2...v0.8.0
[0.7.2]: https://github.com/Flatts3000/sky-frogs/compare/v0.7.1...v0.7.2
[0.7.1]: https://github.com/Flatts3000/sky-frogs/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/Flatts3000/sky-frogs/compare/v0.2.2...v0.3.0
[0.2.2]: https://github.com/Flatts3000/sky-frogs/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/Flatts3000/sky-frogs/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/Flatts3000/sky-frogs/releases/tag/v0.2.0
