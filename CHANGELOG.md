# Changelog

All notable changes to Sky Frogs are documented in this file.

The format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release groups changes under: **Added**, **Changed**, **Removed**, **Fixed**, **World-breaking**. Empty sections are omitted. World-breaking changes (recipe removals that orphan items, mod removals that erase blocks, worldgen changes that require fresh world generation) are called out at the top of the release and bump the **major** version post-1.0.

## [Unreleased]

Tracks work landed on `main` since the last tagged release. Roll into the next version section on tag.

### Added
- Initial packwiz scaffold at `pack/` (MC 1.21.1, NeoForge 21.1.230).
- FTB utility stack: FTB Library, FTB Quests, FTB Teams, FTB Chunks, FTB Ranks, FTB Essentials.
- Resource browser and tooltips: JEI, Jade.
- Tier 0 skyblock substrate: Skyblock Builder (void worldgen), Ex Deorum (sieve / hammer / crucible bootstrap), Forgiving Void (no instant death from falling off the island), Rain Shield (no rain in island area).
- Auto-pulled mod dependencies: Architectury API, LibX, Balm.
- Repo community health files: LICENSE (MIT), NOTICE, CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, PR template, issue templates, dependabot.yml.
- Design documentation under `docs/`: design_overview, progression, worldgen, mod_list, kubejs_overrides, quest_book, pack_metadata, repo_layout, distribution, backlog, curseforge_page, branding.

### Changed
- MC version pinned to 1.21.1 (after a brief 1.21.11 attempt — Ex Deorum and Skyblock Builder have no 1.21.4+ NeoForge builds).
- Distribution scoped to CurseForge only (FTB utility stack is CurseForge-only; Modrinth rejects packs that inline CF jars).

### Notes
- Productive Frogs is not yet bundled — needs a 1.21.1 build artifact and CF publication. Tracked in `docs/backlog.md`.
- No content (KubeJS overrides, FTB Quests chapters, slime variant JSONs) has shipped yet. Pack is scaffolding-only.

---

## Release template

Copy this section and rename the heading to the new version + date when cutting a release. Strip any sections that don't apply.

```markdown
## [v0.x.y] - YYYY-MM-DD

### World-breaking
- (anything that requires a fresh world or item migration — call out loudly)

### Added
- (new features, mods, quests, slime variants, configs)

### Changed
- (behavior changes, balance tuning, recipe edits)

### Removed
- (mods removed, recipes stripped, features deprecated)

### Fixed
- (bug fixes — name the symptom, not just "fixed bug")
```

[Unreleased]: https://github.com/Flatts3000/sky-frogs/compare/main...HEAD
