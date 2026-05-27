# Backlog

> **Status:** living document — items are explicitly non-canonical until promoted. The other docs in this folder are also DRAFT; this one is the meta-parking-lot.

Parking lot for open questions, deferred features, and post-1.0 ideas. Move items into proper docs when they crystallize into design decisions.

## Open design questions

### Productive Frogs feature requests blocking pack work

- [x] **Bog slime spawning on a void island** — RESOLVED by PF v1.0.0, which already ships bog_slime spawning end to end: a biome modifier (`add_bog_slime_spawn.json`) adding `productivefrogs:bog_slime` to `minecraft:swamp` + `minecraft:mangrove_swamp`, plus a light-based placement rule (`checkParentSlimeSpawnRules`, registered via `RegisterSpawnPlacementsEvent` REPLACE). The pack only needs to force the starter island to `minecraft:swamp`; no pack-side spawn override, no pack biome modifier, no PF feature request. The earlier `minecraft:slime` + `slimesSpawnAnywhere` flag plan is obsolete.
- [ ] **Datapack-driven parent species spawn (cave/geode/tide/void)** — verify whether Productive Frogs exposes biome-locked spawn recipes for the four non-Bog parents that Sky Frogs could override datapack-side. If not, distribute those four via quest-reward spawn eggs in their tier chapters (the planned v0.x approach). The Bog parent is unaffected — it free-spawns via PF's shipped swamp spawning.
- [ ] **Slime Milker automation hooks** — Productive Frogs V1 is hand-operated only. For v0.x of Sky Frogs we live with that and lean on Modular Routers + hoppers + water streams for "almost-automation." Real automation (PF V2) is the long-term unlock.
- [ ] **Configurable Froglight data component schema** — confirm the variant component name is stable before we hard-code it into KubeJS scripts and quest checks.
- [ ] **Froglight smelting recipes** — verify whether PF ships default smelt + crush recipes per variant, or whether we need to generate them pack-side. If pack-side, add to `slime_variant_codegen.py`.

### Pack-internal decisions

- [x] **Category-typed Bog frog egg as a PF item** — RESOLVED. PF v1.0.1 ships `productivefrogs:bog_frog_egg`, a placeable block that hatches a Bog tadpole with no priming step (equivalently, `productivefrogs:frog_egg` carrying the `productivefrogs:contained_category` data component set to `"bog"`). Sky Frogs' Welcome quest rewards 2× `productivefrogs:bog_frog_egg` at completion, so the player skips priming.
- [ ] **Swamp-biome island assignment** — confirm the SkyblockBuilder starter island can be forced to `minecraft:swamp` (template biome assignment or single-biome source) so PF's shipped bog_slime spawning fires in the dark room. Verify during Phase 1 implementation; document in `worldgen.md`.
- [ ] **Ex Deorum barrel rain-collection mechanic specifics** — confirm the player can place a barrel outside the Skyblock Builder claim and have it accumulate rainwater, and confirm the timing (in-game ticks per fill). Verify during Phase 1 implementation; document in `worldgen.md`.
- [ ] **Slimeball-as-currency creep** — slimeballs are central to multiple loops (frog breeding, slime infusion, vanilla magma cream). Don't make any single loop demand huge quantities or scarcity becomes the bottleneck.
- [ ] **Custom Sky Frogs Master Frog trophy item** — needs a 3D model + texture + Patchouli completion page. Could be a KubeJS-defined item (no Java needed) or a custom resourcepack-overridden item with components.
- [ ] **Endgame "creative" tier** — what does the player get after the Master Frog trophy? Sky Bees Reborn has a `creative.snbt` chapter with creative-mode-style infinite resource items. Probably ape the same pattern.
- [ ] **Do we ship Create?** Tracked in [`mod_list.md`](./mod_list.md) — defer to v1.x with a "Create as alternative processing path" chapter rather than a tier.
- [ ] **Pink Slime category mapping** — Industrial Foregoing's pink slime is mechanically water-themed (lives in water, drops liquid). Treat as a Tide Resource Slime — that's the cleanest fit and gives the chapter a unique "you can produce pink slime ingots without an IF cow farm" moment.
- [ ] **Obsidian gates the Infernal tier (DECIDED 2026-05-27).** Obsidian is a Cave-category slime variant (`primer_item: minecraft:obsidian`), but on a void skyblock the obsidian *item* is unreachable (water+lava makes the block; harvesting needs a diamond pickaxe, and diamond is not a Cave resource here). We intentionally withhold the obsidian *primer seed* from the **Tier 1: Cave Frogs** chapter so obsidian stays scarce. The obsidian seed/quest lives in the later **Infernal-prelude chapter**: producing obsidian via the Cave frog you've had all along builds the nether portal, which unlocks the Infernal tier. So the Cave Frogs vanilla section covers only copper / gold / coal / lapis / redstone / glow_ink_sac; obsidian is deferred. When building the Infernal chapter, add the obsidian-slime bootstrap there.
- [ ] **Chapter order + sugar source (DECIDED 2026-05-27).** Sidebar order is Welcome (0) -> Your First Iron Ingot (1) -> **Scaling the Colony (2)** -> **Tier 1: Cave Frogs (3)**. Scaling the Colony comes before Cave Frogs and is where the player gets a **sugar cane** grant (sugar -> `productivefrogs:sweetslime`, PF's frog breeding food). This unblocks both frog breeding and the Cave Frogs **seed-chain**: each Cave resource's "slime in a bucket" recipe takes the prior resource's Slime Milk + slime balls + sweetslime (e.g. copper = iron milk + slime balls + sweetslime), so the chain needs sweetslime and therefore sugar. Cave Frogs' intro ("Beyond Iron") is gated behind the Automation intro to enforce the sequence. Vanilla chain order: iron (done) -> copper -> gold -> lapis -> redstone -> coal -> glow_ink_sac.

## Deferred features (post-v0.1)

### Quality-of-life

- **Pack-level difficulty config** — single `config/skyfrogs.json` driving frog spawn rates, milk source counts, sieve drop chances. Useful for "easy/normal/hard" presets and for streamers who want a slower / faster pace.
- **Custom main menu** — branded panorama, custom button colors, version display. Use `packmenu` mod.
- **Custom loading-screen tips** — Tips Mod is shipped; populate with Sky-Frogs-specific tips.
- **Achievement / advancement tree** — vanilla advancements that mirror the questbook. Lower priority since FTB Quests is the canonical progression UI.
- **[implemented 2026-05-26]** **Logs-direct convenience recipes** - craft sticks/chests/etc. straight from logs (e.g. 2 logs -> 16 sticks, 8 logs -> 4 chests), skipping the plank step. Noticed in playtest: the Crafting Station makes nothing from bare logs, which feels clunky early. Options: the [Convenience Recipes](https://www.curseforge.com/minecraft/mc-mods/convenience-recipes) mod (broad set + packing/unpacking + higher stair/wall yields), [Just Another Simple Recipes](https://www.curseforge.com/minecraft/mc-mods/just-another-simple-recipes) (exact ratios above), or - preferred for this content-over-mods pack - a few KubeJS `ServerEvents.recipes` lines keyed off the `#minecraft:logs` tag (no new mod, works with modded woods). Lean KubeJS unless we want the wider recipe set a mod brings.
- **[implemented 2026-05-26]** **Info quest: Squat Grow + FTB Ultimine how-to** - an optional Welcome-chapter checkmark quest that simply tells the player about the two QoL mechanics the pack ships: **Squat Grow** (crouch / hold Sneak next to saplings and crops to grow them, like free bone meal) and **FTB Ultimine** (bind the Ultimine key under Options -> Controls, then hold it and break one block to fell a whole tree or clear a crop patch). Pure info, token XP. Placement idea: an `optional` node hanging off "The Road to Iron" / "Wood to Stand On" near the tree step (around x 1.5, y 4.5). Verify the Ultimine default keybind in-game when building (it may ship unbound).

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

- **Productive Frogs V1 might not be feature-complete by Sky Frogs v0.1 target.** Slime Milker is the load-bearing block for the Tier 1 "scale up" beat; without it, players are stuck producing one Iron Froglight every ~10 minutes (single slime, no milking). Mitigation: gate Sky Frogs v0.1 release on Slime Milker landing in PF V1.
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

- **2026-05-25 — DONE: Productive Frogs published to CurseForge and added to the pack.** PF shipped a 1.21.1 / NeoForge build as v1.0.1 (project-id 1552728), resolving both the "produce a 1.21.1 PF build artifact" and "publish PF to CurseForge" open items in one move. Added via `packwiz cf add productive-frogs` — pinned at `productivefrogs-1.0.1.jar`, no longer a local-override jar. Clears the v0.1 release gate that blocked shipping. See `docs/{mod_list,roadmap}.md` and `CLAUDE.md` versioning targets.
- **2026-05-23 — DECIDED: Tier 0 bootstrap is the slime farm, not sieving.** Removed sieving from Sky Frogs entirely. Ex Deorum stays in the pack for porcelain bucket + crucibles + barrels (rain-collection barrel is the second-water-source mechanic), but sieves and meshes are KubeJS-disabled in `anti.js`. Rain Shield removed from the pack (conflicted with Ex Deorum barrel rain collection inside the player's claim). First-join grant simplified to saplings + water bucket + lava bucket + food. Tier 0 reshape: cobble gen + second water source + dark-room mob farm + bog-slime farming. The farmed parent is `productivefrogs:bog_slime` (the Bog parent per PF's `ParentSpeciesEntry`); PF v1.0.0 already ships bog_slime spawning for `minecraft:swamp` + `minecraft:mangrove_swamp`, so the pack forces the starter island to `minecraft:swamp` and PF's shipped spawning handles the dark room (no pack-side spawn override). Welcome quest chapter rewards 2× Bog frog egg (breeding pair); cooldown-repeatable emergency replacement quest covers the "frog jumped off the island" case. Closes "Frog source on first launch" and "Bootstrap slimeball source" open questions. See `docs/{worldgen,progression,kubejs_overrides,quest_book}.md`.
- **2026-05-23 — DECIDED: Pack pinned to MC 1.21.1 (rolled back from 1.21.11).** Probed every 1.21.x patch from 1.21.1 through 1.21.11 — Ex Deorum and Skyblock Builder both stuck on the 1.21.1 release with no newer NeoForge builds. Since both are load-bearing (Tier 0 bootstrap + skyblock worldgen respectively), 1.21.1 is the only viable MC version for the pack as designed. Productive Frogs now needs to be rebuilt for 1.21.1 to match (tracked as open item above). Closes the prior "verify Skyblock Builder 1.21.11 release exists before adding" note in mod_list.md — confirmed it doesn't.
- **2026-05-23 — DECIDED: CurseForge-only distribution.** The FTB utility stack (FTB Library / Quests / Teams / Chunks / Ranks / Essentials) is CurseForge-only. `packwiz modrinth export` falls back to inlining the FTB jars as `overrides/mods/*.jar`, which Modrinth's uploader rejects on redistribution policy grounds. Since FTB Quests is the canonical questbook (load-bearing), Modrinth is off the table for v0.1 and the foreseeable future. The same constraint applies to Productive Frogs — it'll publish CF-only too. See `docs/distribution.md`.

When items leave the backlog, log them here briefly so we can see what's been processed.
