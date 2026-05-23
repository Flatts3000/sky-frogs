# Changelog

Follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) and [SemVer](https://semver.org/spec/v2.0.0.html). World-breaking changes are called out at the top of the affected release and bump the major version post-1.0.

## [Unreleased]

### Added
- Initial packwiz scaffold (MC 1.21.1 / NeoForge 21.1.230) with FTB utility stack, JEI, Jade, and Tier 0 substrate (Skyblock Builder, Ex Deorum, Forgiving Void, Rain Shield).
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
