# Backlog

> **Status:** living document — items are explicitly non-canonical until promoted. The other docs in this folder are also DRAFT; this one is the meta-parking-lot.

Parking lot for open questions, deferred features, and post-1.0 ideas. Move items into proper docs when they crystallize into design decisions.

## Open design questions

### Productive Frogs feature requests blocking pack work

- [x] **Bog slime spawning on a void island** - RESOLVED. The starter island is forced to `minecraft:swamp` and the pack adds its own parent via a biome modifier. (Note: the parent is `cave_slime`, not bog_slime - see the parent-species item below; Cave is Tier 1, the starter.)
- [x] **Datapack-driven parent species spawn** - RESOLVED. The pack owns spawning: all 6 PF default slime spawns are disabled, and `add_cave_slime_island.json` adds `productivefrogs:cave_slime` to the swamp island. The earlier "Bog parent free-spawns via PF's shipped swamp spawning" premise is wrong - Cave is the starter, and the pack distributes the other parents via quest-reward frogspawn bottles in their tier chapters.
- [x] **Slime Milker automation hooks** - RESOLVED. PF 1.5.3 shipped the Slime Milker (with JEI pages), retiring the PF-V1 load-bearing risk for Tier 1 scale-up.
- [x] **Configurable Froglight data component schema** - RESOLVED. `productivefrogs:slime_variant` is stable and used across all chain scripts (`cave_slime_chain.js`, `geode_slime_chain.js`, `bog_slime_chain.js`) and the froglight-check quests.
- [x] **Froglight smelting recipes** - RESOLVED. The build relies on PF's per-variant smelts; steel is handled in `steel_slime_infusing.js`. No pack-side codegen script needed (`slime_variant_codegen.py` never built).

### Pack-internal decisions

- [x] **Category-typed frog egg as a PF item** - RESOLVED. PF ships placeable category frog eggs that hatch a tadpole with no priming step. NOTE: the old rationale ("Welcome rewards 2x bog_frog_egg") is superseded by the Cave-starter pivot - Welcome now leads into the Cave tier (Tier 1), so the bootstrap parent is cave_slime, not Bog.
- [x] **Swamp-biome island assignment** - BUILT. The SkyblockBuilder starter island is forced to `minecraft:swamp` and the pack's `add_cave_slime_island.json` biome modifier adds cave_slime to it.
- [ ] **Ex Deorum barrel rain-collection mechanic specifics** — confirm the player can place a barrel outside the Skyblock Builder claim and have it accumulate rainwater, and confirm the timing (in-game ticks per fill). Verify during Phase 1 implementation; document in `worldgen.md`.
- [ ] **Slimeball-as-currency creep** — slimeballs are central to multiple loops (frog breeding, slime infusion, vanilla magma cream). Don't make any single loop demand huge quantities or scarcity becomes the bottleneck.
- [~] **Custom Sky Frogs Master Frog trophy item** — MECHANIC BUILT 2026-06-01. Shipped as a KubeJS-defined item `kubejs:master_frog` (`startup_scripts/master_frog_item.js`) crafted in the Extended Crafting Ultimate Table from the Ultimate Singularity + six froglights (`server_scripts/void_recipes.js`); the `master_pond.snbt` capstone hands out the recipe and an epilogue. **Remaining (art only):** the placeholder texture (a PF frog spawn-egg glyph at `kubejs/assets/kubejs/textures/item/master_frog.png`) needs a real 3D model + texture, and an optional Patchouli completion page.
- [ ] **Endgame "creative" tier** — what does the player get after the Master Frog trophy? Sky Bees Reborn has a `creative.snbt` chapter with creative-mode-style infinite resource items. Probably ape the same pattern.
- [ ] **Do we ship Create?** Tracked in [`mod_list.md`](./mod_list.md) — defer to v1.x with a "Create as alternative processing path" chapter rather than a tier.
- [x] **Pink Slime category mapping** - DECIDED AGAINST the Tide proposal. Pink slime is the **Bog capstone**, not a Tide parent: `bog_slime_chain.js` makes plastic -> pink_slime the final step of the Bog organic chain, with IF plastic hard-gated behind the Bog plastic-frog (`if_plastic_gate.js`). Bog won.
- [x] **Obsidian gates the Infernal tier (DECIDED 2026-05-27) - SUPERSEDED 2026-05-31.** The original plan (obsidian via the Cave frog -> build a nether portal -> unlock Infernal) predated PF v1.0.0's species-as-category model. The **built** Infernal tier uses the same Spawnery-primer gate as every other tier: the Tide capstone (nautilus_shell) primes the Spawnery for Infernal Frogspawn - no obsidian portal involved (`road_to_infernal.snbt`). So obsidian is simply **omitted** from the questbook: it's a Cave-category PF variant, but unreachable on skyblock without a diamond pickaxe and not needed for progression. The Cave chain covers iron/copper/gold/coal/redstone (lapis -> Geode); nether materials come from the Infernal frog (netherrack/quartz/glowstone/soul_sand/soul_soil/blaze/netherite_scrap), not from mining obsidian.
- [x] **Chapter order + sugar source (DECIDED 2026-05-27).** IMPLEMENTED. Cave vanilla chain order shipped as iron -> copper -> gold -> coal -> redstone in `cave_slime_chain.js` (prior Slime Milk + 4 stone + 3 sweetslime + a Cave frogspawn bottle per step). Sugar -> sweetslime grant lands in `scaling_the_colony.snbt`. Lapis moved to the Geode tier; obsidian deferred to the Infernal gate; glow_ink_sac omitted. (The "currently pinned 1.4.3" note is stale - PF is now at 1.6.0.) See changelog below.
- [x] **Modded Cave metals -> their tech-mod chapters (DECIDED 2026-05-27).** IMPLEMENTED. The Cave frog produces the modded metals; each gets a one-time bootstrap slime-bucket recipe in the tech-mod chapter that needs it. Osmium's bootstrap (`osmium_slime_bucket.js`) is the opening of the Mekanism chapter, resolving "Cave gating Mekanism." See changelog below.

## Deferred features (post-v0.1)

### Quality-of-life

- **Pack-level difficulty config** — single `config/skyfrogs.json` driving frog spawn rates, milk source counts, sieve drop chances. Useful for "easy/normal/hard" presets and for streamers who want a slower / faster pace.
- **Custom main menu** — branded panorama, custom button colors, version display. Use `packmenu` mod.
- **Custom loading-screen tips** — Tips Mod is shipped; populate with Sky-Frogs-specific tips.
- **Achievement / advancement tree** — vanilla advancements that mirror the questbook. Lower priority since FTB Quests is the canonical progression UI.

### Content

- **Modded Resource Slime variants from Botania, Blood Magic, Create** if we ship those mods later.
- **Custom slime species in our namespace** — `skyfrogs:plasma_slime`, `skyfrogs:rainbow_slime`, etc. for joke variants and challenges.
- **Cross-pack content from Productive Bees** — if we ever decide a hybrid bee+frog pack would be fun, that's a separate pack project (not Sky Frogs).
- **Custom dimension** — "Frog Paradise" — a void dimension reachable post-Tier 6 where frog spawn rates are maximized. Unlock via mass-singularity recipe.

### Infrastructure

- **Server template** — Pterodactyl egg, Docker compose, one-line shell installer.
- **Localization workflow** — Crowdin or Weblate integration for community translations.
- **Anti-cheat hooks** — beyond the fake-player block in `anti.js`, monitor for obvious cheats (e.g., creative-mode flag in survival worlds).

### Marketing / community

- **YouTube playthrough series** — partner with a let's-player for the v1.0 launch.
- **Twitter/Bluesky devlog account** — `@SkyFrogsMC`, post screenshots and changelog excerpts.

## Known risks

- ~~**Productive Frogs V1 might not be feature-complete by Sky Frogs v0.1 target.** Slime Milker is the load-bearing block for the Tier 1 "scale up" beat.~~ RESOLVED: PF 1.5.3 shipped the Slime Milker (with JEI pages), so the scale-up beat is no longer gated.
- **Mod-update churn through NeoForge 1.21.x** could force a re-pin pass on each PF bump. We're now on 1.21.1 — rolled back from 1.21.11 because Ex Deorum and Skyblock Builder have no 1.21.4+ NeoForge builds. Mitigation: hold the pack to whatever MC version the bootstrap-substrate mods are on, not whatever PF is on. PF can be rebuilt to match.
- **CurseForge approval delays** could block v0.1 launch on CF. Since CF is our sole channel, an approval delay = no v0.1 launch. Mitigation: submit the empty CF project for approval as early as possible in the v0.1 cycle so the approval window runs in parallel with content work.
- **License compatibility check** — verify every bundled mod's license allows redistribution in a modpack. Most do (MIT, ARR-with-modpack-permission, GPL, etc.). One or two outliers might require explicit author permission. Audit before v0.1.
- **Productive Frogs is an in-development mod by the pack author**. Risk: pack might inadvertently expose / depend on private APIs that change. Mitigation: pin exact PF version per release; bump deliberately.

## Stretch goals (no commitment)

- **Cross-pack-compatible difficulty modifier** — could the Sky Frogs config layer extend to support modpacks bundling Productive Frogs without the full Sky Frogs treatment? Probably not — this is over-abstraction.
- **Companion website** — `skyfrogs.flatts.example` with progression tree visualization, slime variant browser, mod credits. Cute but low-priority.
- **In-game tutorial NPC** — a villager that walks new players through Tier 0. Hard to make non-annoying; skip.
- **Speedrun category support** — clean kill-the-dragon timing, no-cheats verification. Defer until there's a runner.

## Recently moved out of backlog (changelog)

- **2026-06-01 - BUILT: Tier 6 Void + Extended Crafting (the content campaign's capstone).** Added four chapters (`road_to_void`, `void_frogs`, `the_ultimate_table`, `master_pond`; 28 quests) and the Void mechanical layer. The gate is a one-time **dragon expedition** (no stronghold on a void skyblock, so a 12-frame End portal is crafted from frog-farmed glowstone + soul sand via `void_recipes.js`; enter the End, slay the dragon). Verb = **Extended Crafting** (pinned 7.0.8). The endgame compresses each species' Froglight 1000:1 into a **Singularity** (a proof-of-automation gate, `config/extendedcrafting/singularities/*.json` using a `neoforge:components` froglight-variant ingredient), six Singularities -> the Ultimate Singularity -> the **Master Frog** trophy. Dissolution `VOID` row filler = soul soil (Infernal resource; end stone would be circular). Six vanilla Void variants quested; modded Void variants deferred. Closes the "Void verb / filler / primer TBD" open questions. Held for playtest on `feat/tier-6-void`.
- **2026-05-29 - BUILT: Tier 3 Bog + Industrial Foregoing.** Added the `road_to_bog.snbt` + `bog_frogs.snbt` chapters and `bog_slime_chain.js`. Bog's verb is Industrial Foregoing: plastic is hard-gated behind the Bog plastic-frog (`if_plastic_gate.js`), and pink_slime is the chain capstone (closing the "Pink Slime category mapping" item - Bog won over the Tide proposal). Shipped Industrial Foregoing + IF Souls. Bog chain filler block is mossy cobblestone.
- **2026-05-29 - BUILT: Tier 2 Geode + Mekanism.** Added the `road_to_geode.snbt` + `geode_frogs.snbt` + `mekanism.snbt` chapters and `geode_slime_chain.js` (filler block: gravel). Geode's verb is automation (Mekanism + Generators + Tools). Lapis lands here (moved out of Cave per PF 1.5.1). The Mekanism chapter opens with the osmium slime-bucket bootstrap (`osmium_slime_bucket.js`), so Mekanism hands the player the osmium path itself instead of depending on a missing Cave node. The Mekanism Digital Miner is disabled in `anti.js`. Closes the two DECIDED-2026-05-27 items (chapter order/sugar source + modded-Cave-metals-to-tech-chapters).
- **2026-05-29 - RETROFIT: pack-wide froglight-check principle + per-tier filler blocks.** Per-tier resource quests now detect the variant Froglight (the frog's proof), not the smelted resource (which is gameable). Exceptions: the iron_ingot capstone and the main Mekanism steel quest. Per-tier slime-chain filler blocks settled: Cave = stone, Geode = gravel, Bog = mossy cobblestone.
- **2026-05-28 - BUILT: Tier 1 Cave + Storage and Crafting.** Added `your_first_iron_ingot.snbt`, `scaling_the_colony.snbt`, `cave_frogs.snbt`, `storage_and_crafting.snbt`. Cave is Tier 1 (the starter), with chain order iron -> copper -> gold -> coal -> redstone (`cave_slime_chain.js`, filler block: stone) and the sugar -> sweetslime grant in Scaling the Colony. Cave's verb is crafting upgrades / storage: Sophisticated Storage (bumped) + Functional Storage, with quartz-free networks via `storage_quartz_free.js`. Also shipped cobblegen-galore and All The Ores (ato), and the logs-direct convenience recipes (`log_recipes.js`) + the Squat Grow / FTB Ultimine info quest (both implemented 2026-05-26).
- **2026-05-25 — DONE: Productive Frogs published to CurseForge and added to the pack.** PF shipped a 1.21.1 / NeoForge build as v1.0.1 (project-id 1552728), resolving both the "produce a 1.21.1 PF build artifact" and "publish PF to CurseForge" open items in one move. Added via `packwiz cf add productive-frogs` — pinned at `productivefrogs-1.0.1.jar`, no longer a local-override jar. Clears the v0.1 release gate that blocked shipping. See `docs/{mod_list,roadmap}.md` and `CLAUDE.md` versioning targets.
- **2026-05-23 — DECIDED: Tier 0 bootstrap is the slime farm, not sieving.** Removed sieving from Sky Frogs entirely. Ex Deorum stays in the pack for porcelain bucket + crucibles + barrels (rain-collection barrel is the second-water-source mechanic), but sieves and meshes are KubeJS-disabled in `anti.js`. Rain Shield removed from the pack (conflicted with Ex Deorum barrel rain collection inside the player's claim). First-join grant simplified to saplings + water bucket + lava bucket + food. Tier 0 reshape: cobble gen + second water source + dark-room mob farm + bog-slime farming. The farmed parent is `productivefrogs:bog_slime` (the Bog parent per PF's `ParentSpeciesEntry`); PF v1.0.0 already ships bog_slime spawning for `minecraft:swamp` + `minecraft:mangrove_swamp`, so the pack forces the starter island to `minecraft:swamp` and PF's shipped spawning handles the dark room (no pack-side spawn override). Welcome quest chapter rewards 2× Bog frog egg (breeding pair); cooldown-repeatable emergency replacement quest covers the "frog jumped off the island" case. Closes "Frog source on first launch" and "Bootstrap slimeball source" open questions. See `docs/{worldgen,progression,kubejs_overrides,quest_book}.md`.
- **2026-05-23 — DECIDED: Pack pinned to MC 1.21.1 (rolled back from 1.21.11).** Probed every 1.21.x patch from 1.21.1 through 1.21.11 — Ex Deorum and Skyblock Builder both stuck on the 1.21.1 release with no newer NeoForge builds. Since both are load-bearing (Tier 0 bootstrap + skyblock worldgen respectively), 1.21.1 is the only viable MC version for the pack as designed. Productive Frogs now needs to be rebuilt for 1.21.1 to match (tracked as open item above). Closes the prior "verify Skyblock Builder 1.21.11 release exists before adding" note in mod_list.md — confirmed it doesn't.
- **2026-05-23 — DECIDED: CurseForge-only distribution.** The FTB utility stack (FTB Library / Quests / Teams / Chunks / Ranks / Essentials) is CurseForge-only. `packwiz modrinth export` falls back to inlining the FTB jars as `overrides/mods/*.jar`, which Modrinth's uploader rejects on redistribution policy grounds. Since FTB Quests is the canonical questbook (load-bearing), Modrinth is off the table for v0.1 and the foreseeable future. The same constraint applies to Productive Frogs — it'll publish CF-only too. See `docs/distribution.md`.

When items leave the backlog, log them here briefly so we can see what's been processed.
