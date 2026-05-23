# CLAUDE.md

Guidance for Claude Code working in this repo.

## What this is

**Sky Frogs** is a modpack (not a mod) built around [Productive Frogs](../productive-frogs). The pack is in **early exploratory planning** — everything in `docs/` is marked DRAFT and explicitly non-canonical. The pack is looking for its own identity; do not treat any design choice as decided.

A read-only reference copy of Sky Bees Reborn lives at [`../sky-bees-reborn-reference/extracted/`](../sky-bees-reborn-reference/) as a **study object** — its `kubejs/server_scripts/`, `config/ftbquests/quests/`, and mod selection are useful for seeing how the genre has been solved before. They are **not** templates to mirror. Sky Frogs needs its own answers. When pulling patterns from SBR, attribute the inspiration but justify the choice on Sky-Frogs-specific grounds.

## Versioning targets

- Minecraft: **1.21.1** (matches Productive Frogs)
- Loader: **NeoForge**
- Java: **21**
- Distribution: **Modrinth `.mrpack`** + **CurseForge manifest** (both)
- Productive Frogs version: **latest 1.21.1 release** — pinned in `pack.toml`

## Project Conventions

- **Docs filenames:** snake_case (e.g. `design_overview.md`), per the global rule.
- **Line endings:** `.gitattributes` forces LF for source/config/docs and CRLF for `.bat`/`.cmd`/`.ps1`. Don't fight it.
- **Conventional Commits:** `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`, `ci:`. Body explains the **why**. `main` is protected; changes via PR.
- **License:** MIT for pack-authored content. Bundled mods retain their own licenses.

## Scope discipline

This repo is a **content pack**. Java code does **not** belong here — if a feature would require a Java mod, it goes in [productive-frogs](../productive-frogs) instead.

Acceptable surfaces inside this repo:
- KubeJS scripts (`kubejs/{server,startup,client}_scripts/`)
- Datapack overrides (`kubejs/data/<ns>/`)
- Resourcepack overrides (`kubejs/assets/<ns>/`)
- Mod configs (`config/`, `defaultconfigs/`)
- FTB Quests data (`config/ftbquests/quests/`)
- Pack metadata (`pack.toml`, `index.toml`, `manifest.json`)
- Pack-level docs (`docs/`, `README.md`)

If something needs new Java behavior, file an issue against Productive Frogs and reference the pack-side need.

## Working assumptions (NOT yet canonical)

The current `docs/` write-ups lean on these working assumptions. None of them are decided — every one is up for revision and should be challenged when better ideas emerge:

1. **Frogs as the spine of resource generation.** Whether this means "frogs replace mining entirely" or "frogs are the headline path among several" is unresolved. See [`docs/design_overview.md`](./docs/design_overview.md).
2. **Six categories follow Productive Frogs.** This one is the closest to canonical because it inherits from the mod's enum — but the *progression order* and tier-mapping are open.
3. **Cross-mod compat via datapack JSONs.** Inherited from how Productive Frogs already works; the pack-side workflow for generating those JSONs is unresolved.
4. **Hand-operated appliances only in v0.x.** Tied to Productive Frogs V1 scope; if PF V2 ships earlier than expected this assumption flips.

When a working assumption gets challenged and we settle the question, **promote it out of this list** into a dedicated decision record (and drop the DRAFT banner from the affected doc).

## Common commands

TBD until packwiz is installed and wired up. See [`docs/repo_layout.md`](./docs/repo_layout.md).
