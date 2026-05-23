# Backlog

> **Status:** living document — items are explicitly non-canonical until promoted. The other docs in this folder are also DRAFT; this one is the meta-parking-lot.

Parking lot for open questions, deferred features, and post-1.0 ideas. Move items into proper docs when they crystallize into design decisions.

## Open design questions

### Productive Frogs feature requests blocking pack work

- [ ] **Productive Frogs distribution channel.** PF is not yet on Modrinth or CurseForge — only a local jar at `../productive-frogs/build/libs/`. The pack can't ship to either platform until PF has a public release. Decide: publish PF first (Modrinth + CF), or bundle PF's jar directly into pack overrides (CF zip only; Modrinth forbids it). Tracking as v0.1 blocker.
- [ ] **Datapack-driven parent species spawn** — verify whether Productive Frogs exposes biome-locked spawn recipes that Sky Frogs can KubeJS-override (mirror the Sky Bees Reborn `bee_spawning` pattern). If not, file a feature request upstream against [`productive-frogs`](../../productive-frogs). Workaround for v0.1: distribute parent species via quest-reward spawn eggs.
- [ ] **Slime Milker automation hooks** — Productive Frogs V1 is hand-operated only. For v0.x of Sky Frogs we live with that and lean on Modular Routers + hoppers + water streams for "almost-automation." Real automation (PF V2) is the long-term unlock.
- [ ] **Configurable Froglight data component schema** — confirm the variant component name is stable before we hard-code it into KubeJS scripts and quest checks.
- [ ] **Froglight smelting recipes** — verify whether PF ships default smelt + crush recipes per variant, or whether we need to generate them pack-side. If pack-side, add to `slime_variant_codegen.py`.

### Pack-internal decisions

- [ ] **Frog source on first launch** — starter chest spawn egg vs quest-reward spawn egg vs custom Patchouli book reward. Leaning starter chest for least friction.
- [ ] **Bootstrap slimeball source** — Ex Deorum sieve drop chances need tuning. Target: a player should average ~5 slimeballs in 30 minutes of sieving (enough for the first frog breed + a few infusions).
- [ ] **Slimeball-as-currency creep** — slimeballs are central to multiple loops (frog breeding, slime infusion, vanilla magma cream). Don't make any single loop demand huge quantities or scarcity becomes the bottleneck.
- [ ] **Custom Sky Frogs Master Frog trophy item** — needs a 3D model + texture + Patchouli completion page. Could be a KubeJS-defined item (no Java needed) or a custom resourcepack-overridden item with components.
- [ ] **Endgame "creative" tier** — what does the player get after the Master Frog trophy? Sky Bees Reborn has a `creative.snbt` chapter with creative-mode-style infinite resource items. Probably ape the same pattern.
- [ ] **Do we ship Create?** Tracked in [`mod_list.md`](./mod_list.md) — defer to v1.x with a "Create as alternative processing path" chapter rather than a tier.
- [ ] **Pink Slime category mapping** — Industrial Foregoing's pink slime is mechanically aquatic-ish (lives in water, drops liquid). Treat as an Aquatic Resource Slime — that's the cleanest fit and gives the chapter a unique "you can produce pink slime ingots without an IF cow farm" moment.

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
- **Modrinth modpack rich-presence integration** — Discord rich presence showing current tier.
- **Anti-cheat hooks** — beyond the fake-player block in `anti.js`, monitor for obvious cheats (e.g., creative-mode flag in survival worlds).

### Marketing / community

- **YouTube playthrough series** — partner with a let's-player for the v1.0 launch.
- **Twitter/Bluesky devlog account** — `@SkyFrogsMC`, post screenshots and changelog excerpts.
- **Pack Discord server** — only worth doing if community size justifies it (post-1k downloads).

## Known risks

- **Productive Frogs V1 might not be feature-complete by Sky Frogs v0.1 target.** Slime Milker is the load-bearing block for the Tier 1 "scale up" beat; without it, players are stuck producing one Iron Froglight every ~10 minutes (single slime, no milking). Mitigation: gate Sky Frogs v0.1 release on Slime Milker landing in PF V1.
- **Mod-update churn through NeoForge 1.21.x** could force a re-pin pass on each PF bump. We're now on 1.21.11 (matched to PF). Mitigation: hold a single MC version per pack release; bump deliberately when PF bumps, not opportunistically.
- **CurseForge approval delays** could block v0.1 launch on CF. Mitigation: ship Modrinth-first, follow with CF when approval lands.
- **FTB mods are CurseForge-only.** FTB Library / Quests / Teams / Chunks / Ranks / Essentials are not on Modrinth. `packwiz modrinth export` falls back to inlining the jars as `overrides/mods/*.jar`, which Modrinth's uploader will reject on redistribution policy grounds. **Effective state: CurseForge-only distribution until either FTB publishes to Modrinth or we replace the FTB stack.** Tracked as a v0.1 distribution decision.
- **License compatibility check** — verify every bundled mod's license allows redistribution in a modpack. Most do (MIT, ARR-with-modpack-permission, GPL, etc.). One or two outliers might require explicit author permission. Audit before v0.1.
- **Productive Frogs is an in-development mod by the pack author**. Risk: pack might inadvertently expose / depend on private APIs that change. Mitigation: pin exact PF version per release; bump deliberately.

## Stretch goals (no commitment)

- **Cross-pack-compatible difficulty modifier** — could the Sky Frogs config layer extend to support modpacks bundling Productive Frogs without the full Sky Frogs treatment? Probably not — this is over-abstraction.
- **Companion website** — `skyfrogs.flatts.example` with progression tree visualization, slime variant browser, mod credits. Cute but low-priority.
- **In-game tutorial NPC** — a villager that walks new players through Tier 0. Hard to make non-annoying; skip.
- **Speedrun category support** — clean kill-the-dragon timing, no-cheats verification. Defer until there's a runner.

## Recently moved out of backlog (changelog)

- (none yet — this is the initial state)

When items leave the backlog, log them here briefly so we can see what's been processed.
