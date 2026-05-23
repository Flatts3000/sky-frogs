# CLAUDE.md

Guidance for Claude Code working in this repo.

## What this is

**Sky Frogs** is a modpack (not a mod) built around [Productive Frogs](../productive-frogs). The pack is in **early exploratory planning** — everything in `docs/` is marked DRAFT and explicitly non-canonical. The pack is looking for its own identity; do not treat any design choice as decided.

A read-only reference copy of Sky Bees Reborn lives at [`../sky-bees-reborn-reference/extracted/`](../sky-bees-reborn-reference/) as a **study object** — its `kubejs/server_scripts/`, `config/ftbquests/quests/`, and mod selection are useful for seeing how the genre has been solved before. They are **not** templates to mirror. Sky Frogs needs its own answers. When pulling patterns from SBR, attribute the inspiration but justify the choice on Sky-Frogs-specific grounds.

### Sibling repos on this machine

- `../productive-frogs` — the Java mod this pack is built around. File issues there for anything that needs new mod behavior.
- `../sky-bees-reborn-reference/extracted/` — read-only SBR reference. Useful subpaths: `kubejs/server_scripts/anti.js`, `kubejs/server_scripts/productivebees.js`, `config/ftbquests/quests/`, `kubejs/data/productivebees/productivebees/`.

### Doc map (start here)

All design docs are DRAFT. When you settle a question, drop the DRAFT banner on the affected doc and update [`CLAUDE.md`](./CLAUDE.md) working assumptions or [`docs/backlog.md`](./docs/backlog.md).

- [`docs/design_overview.md`](./docs/design_overview.md) — concept, core loop, target audience, success criteria
- [`docs/progression.md`](./docs/progression.md) — tier-by-tier player journey (the six PF categories)
- [`docs/mod_list.md`](./docs/mod_list.md) — what ships and why; selection criteria
- [`docs/kubejs_overrides.md`](./docs/kubejs_overrides.md) — the four pillars (anti, parent spawn, slime variants, recipe forcing)
- [`docs/quest_book.md`](./docs/quest_book.md) — FTB Quests chapter outline
- [`docs/worldgen.md`](./docs/worldgen.md) — void skyblock setup, starter island, parent species distribution
- [`docs/pack_metadata.md`](./docs/pack_metadata.md) — pack identity, versioning policy, asset spec
- [`docs/repo_layout.md`](./docs/repo_layout.md) — packwiz tree, CI shape, helper scripts
- [`docs/distribution.md`](./docs/distribution.md) — CurseForge release workflow
- [`docs/curseforge_page.md`](./docs/curseforge_page.md) — public-facing CurseForge listing copy (hook, features, FAQ, mod credits) — edit here first, push to CF
- [`docs/branding.md`](./docs/branding.md) — visual identity spec: category color palette (sourced from PF's `Category.tintArgb()`), asset list, logo/hero composition guidelines
- [`docs/backlog.md`](./docs/backlog.md) — open questions, deferred features, known risks
- [`CHANGELOG.md`](./CHANGELOG.md) — Keep a Changelog format; `[Unreleased]` captures work landed on `main` since last tag

## Versioning targets

- Minecraft: **1.21.1** (rolled back from 1.21.11 on 2026-05-23 — Ex Deorum and Skyblock Builder have no 1.21.4+ NeoForge builds, and they're load-bearing for Tier 0 bootstrap and skyblock worldgen respectively. Productive Frogs needs to be rebuilt for 1.21.1 to match.)
- Loader: **NeoForge 21.1.230**
- Java: **21**
- Distribution: **CurseForge only.** Modrinth is off the table because the FTB utility stack (FTB Library / Quests / Teams / Chunks / Ranks / Essentials) is CF-only and Modrinth forbids inlining CF jars as overrides. This same constraint applies to Productive Frogs — PF is CF-only too.
- Productive Frogs: **not yet published** to CurseForge. Local jar lives at `../productive-frogs/build/libs/productivefrogs-0.1.0.jar`. Once PF is on CF, add via `packwiz cf add productive-frogs`.

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

`pack/` is initialized (packwiz, MC 1.21.1 / NeoForge 21.1.230). All packwiz commands run from inside `pack/`:

```sh
packwiz refresh                          # regenerate index.toml after editing any .pw.toml
packwiz cf add <curseforge-slug>         # add a mod (CurseForge — sole distribution channel)
packwiz remove <mod-slug>                # remove a mod
packwiz update --all                     # pull latest versions of all pinned mods
packwiz curseforge export                # build the .zip for CurseForge
```

`packwiz mr add` and `packwiz modrinth export` are intentionally unused — see "Distribution" in Versioning targets above.

`tools/` helper scripts (`build_cf_zip.sh`, `slime_variant_codegen.py`) are still planned per [`docs/repo_layout.md`](./docs/repo_layout.md) but not yet created.

Releases will be tag-driven (`git tag v0.x.y && git push origin v0.x.y`) once `.github/workflows/release.yml` lands. See [`docs/distribution.md`](./docs/distribution.md).
