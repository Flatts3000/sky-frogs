# Changelog

Follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) and [SemVer](https://semver.org/spec/v2.0.0.html). World-breaking changes are called out at the top of the affected release and bump the major version post-1.0.

## [Unreleased]

### Added
- Initial packwiz scaffold (MC 1.21.1 / NeoForge 21.1.230) with FTB utility stack, JEI, Jade, and Tier 0 substrate (Skyblock Builder, Ex Deorum, Forgiving Void, Rain Shield).
- Productive Frogs v1.0.1 added from CurseForge (project-id 1552728) — the pack's load-bearing core mod is now pinned via packwiz instead of pending a local jar.
- KubeJS 2101.7.2 (+ Rhino) added for pack-side scripting and datapack overrides.
- Tier 0 KubeJS scripts: `first_join.js` (first-launch inventory grant, persistent-guarded) and `anti.js` (disables Ex Deorum sieving — recipe types, sieve/mesh crafting, mesh tooltips, fake-player block cancel).
- Tier 0 slime spawning is pack-owned: a biome modifier adds `productivefrogs:cave_slime` (the Cave / Tier 1 starter parent) to the swamp island, and PF's six default slime-spawn biome modifiers are disabled via `neoforge:none` overrides, so only Cave spawns. PF's light-based placement hook makes it spawn in a dark room.
- `config/skyblockbuilder/world.json5` forces the overworld to `minecraft:swamp` (on-theme; spawns are pack-controlled), and `starter_inventory.json5` is emptied so SkyblockBuilder's default kit doesn't stack on the KubeJS grant.
- Welcome (Tier 0) FTB Quests chapter: 16 quests bootstrapping to the first Cave frogs, ending with a Bottle of Cave Frog Frogspawn. Written in the pack voice (`docs/voice_and_tone.md`).
- Design docs under `docs/` and community health files.

### Changed
- Pinned to MC 1.21.1 (Ex Deorum and Skyblock Builder have no 1.21.4+ NeoForge builds).
- CurseForge-only distribution (FTB stack blocks Modrinth).
- Adopted Productive Frogs v1.0.0's species category names across all docs (METALLIC to Bog, MINERAL to Cave, GEM to Geode, AQUATIC to Tide, ARCANE to Void; Infernal unchanged). Vanilla `minecraft:slime` / `magma_cube` are no longer parent species.
- Tier 0 reshaped to the species-gated model: the starter species is **Cave** (ores), farmed as a dark-room `cave_slime` farm. Progression is Cave -> Geode -> Bog -> Tide -> Infernal -> Void, each tier gated by crafting the next species' frogspawn bottle + Slime Milk. Ex Deorum is porcelain bucket + crucibles + rain-collection barrels only.

### Removed
- Rain Shield (conflicted with Ex Deorum barrel rain collection inside the player's claim).
- Pack-side `slime_spawns.json` biome modifier (it targeted vanilla `minecraft:slime`, which PF v1.0.0 no longer uses as a parent; PF ships its own `bog_slime` biome modifier).

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

[Unreleased]: https://github.com/Flatts3000/sky-frogs/compare/main...HEAD
