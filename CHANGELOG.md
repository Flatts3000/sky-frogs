# Changelog

Follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) and [SemVer](https://semver.org/spec/v2.0.0.html). World-breaking changes are called out at the top of the affected release and bump the major version post-1.0.

## [Unreleased]

### Added
- Initial packwiz scaffold (MC 1.21.1 / NeoForge 21.1.230) with FTB utility stack, JEI, Jade, and Tier 0 substrate (Skyblock Builder, Ex Deorum, Forgiving Void, Rain Shield).
- Productive Frogs v1.0.1 added from CurseForge (project-id 1552728) — the pack's load-bearing core mod is now pinned via packwiz instead of pending a local jar.
- KubeJS 2101.7.2 (+ Rhino) added for pack-side scripting and datapack overrides.
- Tier 0 KubeJS scripts: `first_join.js` (first-launch inventory grant via a persistent guard) and `anti.js` (disables Ex Deorum sieving — recipe types, sieve/mesh crafting, mesh tooltips, fake-player block cancel). The dark-room slime farm uses `productivefrogs:bog_slime`, which PF v1.0.0 already spawns in swamps; the pack forces the starter island to `minecraft:swamp` rather than shipping a spawn override.
- `config/skyblockbuilder/world.json5` forces the overworld to a single `minecraft:swamp` biome, so PF's shipped `bog_slime` spawning fires in a Tier 0 dark room with no pack-side spawn code.
- Design docs under `docs/` and community health files.

### Changed
- Pinned to MC 1.21.1 (Ex Deorum and Skyblock Builder have no 1.21.4+ NeoForge builds).
- CurseForge-only distribution (FTB stack blocks Modrinth).
- Adopted Productive Frogs v1.0.0's species category names across all docs (METALLIC to Bog, MINERAL to Cave, GEM to Geode, AQUATIC to Tide, ARCANE to Void; Infernal unchanged). Vanilla `minecraft:slime` is no longer a parent species; the Tier 0 parent is `productivefrogs:bog_slime`.
- Tier 0 bootstrap reshaped: no sieving, bog-slime farm on a swamp-biome island via PF's shipped bog_slime spawning (no pack-side spawn override); Ex Deorum demoted to porcelain bucket + crucibles + rain-collection barrels.

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
