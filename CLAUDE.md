# CLAUDE.md

Guidance for Claude Code working in this repo.

## What this is

**Sky Frogs** is a modpack (not a mod). It bundles existing NeoForge 1.21.1 mods — most importantly [Productive Frogs](../productive-frogs) — with configs, KubeJS overrides, a datapack, and an FTB Quests questbook to deliver a void-skyblock experience where frogs are the only viable material source. It is the Productive-Frogs analog of [Sky Bees Reborn](https://www.curseforge.com/minecraft/modpacks/sky-bees-reborn).

A read-only reference copy of Sky Bees Reborn lives at [`../sky-bees-reborn-reference/extracted/`](../sky-bees-reborn-reference/) — its `kubejs/server_scripts/`, `config/ftbquests/quests/`, and mod selection are the canonical priors when designing equivalent surfaces in Sky Frogs.

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

## Key design priors (encoded in `docs/`)

These have been litigated. Read the relevant doc before making non-trivial changes:

1. **Frogs replace mining** — automated mining mods (laser drills, mining lenses) are KubeJS-disabled. Manual Ex Deorum sieving is kept as the early-game bootstrap, mirroring Sky Bees Reborn. See [`docs/kubejs_overrides.md`](./docs/kubejs_overrides.md).
2. **Six categories define tier progression** — quest chapters are organized around the six Productive Frogs categories (Metallic, Mineral, Gem, Aquatic, Infernal, Arcane). See [`docs/progression.md`](./docs/progression.md) and [`docs/quest_book.md`](./docs/quest_book.md).
3. **Datapack-driven slime variants are the cross-mod compat surface** — adding a modded resource to the pack means dropping a `slime_variant` JSON under a KubeJS datapack namespace, never adding a Java compat module. See [`docs/kubejs_overrides.md`](./docs/kubejs_overrides.md).
4. **No automation in v0.x — Slime Milker is the scaling tool** — Productive Frogs V1 ships hand-operated appliance blocks only. Real automation (hoppers, power, multiblocks) is Productive Frogs V2 territory. Sky Frogs v0.x will feel intentionally artisanal as a result; that's the tradeoff. See [`docs/backlog.md`](./docs/backlog.md).

## Common commands

TBD until packwiz is installed and wired up. See [`docs/repo_layout.md`](./docs/repo_layout.md).
