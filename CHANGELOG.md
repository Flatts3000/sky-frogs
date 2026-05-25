# Changelog

Follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) and [SemVer](https://semver.org/spec/v2.0.0.html). World-breaking changes are called out at the top of the affected release and bump the major version post-1.0.

## [Unreleased]

### Added
- Initial packwiz scaffold (MC 1.21.1 / NeoForge 21.1.230) with FTB utility stack, JEI, Jade, and Tier 0 substrate (Skyblock Builder, Ex Deorum, Forgiving Void, Rain Shield).
- Productive Frogs v1.0.1 added from CurseForge (project-id 1552728) — the pack's load-bearing core mod is now pinned via packwiz instead of pending a local jar.
- KubeJS 2101.7.2 (+ Rhino) added for pack-side scripting and datapack overrides.
- Tier 0 KubeJS scripts: `first_join.js` (first-launch inventory grant via a persistent guard), `anti.js` (disables Ex Deorum sieving — recipe types, sieve/mesh crafting, mesh tooltips, fake-player block cancel), and `slime_spawns.json` biome modifier (adds `minecraft:slime` to overworld monster spawns; pairs with the pending PF placement-rule flag, productive-frogs#107).
- Design docs under `docs/` and community health files.

### Changed
- Pinned to MC 1.21.1 (Ex Deorum and Skyblock Builder have no 1.21.4+ NeoForge builds).
- CurseForge-only distribution (FTB stack blocks Modrinth).
- Tier 0 bootstrap reshaped: no sieving, vanilla slime farm via KubeJS spawn override; Ex Deorum demoted to porcelain bucket + crucibles + rain-collection barrels.

### Removed
- Rain Shield (conflicted with Ex Deorum barrel rain collection inside the player's claim).

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
