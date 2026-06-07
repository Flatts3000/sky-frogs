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
- [`docs/roadmap.md`](./docs/roadmap.md) — phase-by-phase path from current state to v1.0 launch, with explicit user-vs-Claude ownership per deliverable
- [`docs/backlog.md`](./docs/backlog.md) — open questions, deferred features, known risks
- [`docs/pf_pin_history.md`](./docs/pf_pin_history.md) — Productive Frogs bump-by-bump pin history (what each version brought, breaking changes)
- [`CHANGELOG.md`](./CHANGELOG.md) — Keep a Changelog format; `[Unreleased]` captures work landed on `main` since last tag

## Versioning targets

- Minecraft: **1.21.1** (rolled back from 1.21.11 on 2026-05-23 — Ex Deorum and Skyblock Builder have no 1.21.4+ NeoForge builds, and they're load-bearing for Tier 0 bootstrap and skyblock worldgen respectively. Productive Frogs needs to be rebuilt for 1.21.1 to match.)
- Loader: **NeoForge 21.1.230**
- Java: **21**
- Distribution: **CurseForge only.** Modrinth is off the table because the FTB utility stack (FTB Library / Quests / Teams / Chunks / Ranks / Essentials) is CF-only and Modrinth forbids inlining CF jars as overrides. This same constraint applies to Productive Frogs — PF is CF-only too.
- Productive Frogs: **published on CurseForge** (slug `productive-frogs`, project-id `1552728`) as of 2026-05-25. Added via `packwiz cf add productive-frogs`; currently pinned at **`productivefrogs-1.13.0.jar`** (1.21.1 / NeoForge; 2026-06-07 - water/lava re-homed to Cave [lava primer now pointed_dripstone] + six vanilla stragglers; with 1.12's Crucible/Mold wave the Ultimate Singularity went 40 -> 50). The full bump-by-bump history (every version since 1.0.1, what each brought, the 1.8.0 breaking milk split) lives in [`docs/pf_pin_history.md`](./docs/pf_pin_history.md). PF ships no slime-milk-bucket tag, so the pack's `slime_milk_tags.js` stays load-bearing. Pull newer files with `packwiz update productive-frogs`.

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
2. **Six categories follow Productive Frogs.** This one is the closest to canonical because it inherits from the mod's enum — but the *progression order* and tier-mapping are open. Settled 2026-05-25: PF v1.0.0's species-as-category redesign means the enum is now BOG / CAVE / GEODE / TIDE / INFERNAL / VOID (biome-species names, player-facing). Sky Frogs adopts these names; the tier mapping is now **settled and built** as Tier 1 = Cave, Tier 2 = Geode, Tier 3 = Bog, with Tier 4 = Tide **fully built** (`road_to_tide` bridge + `drowned_riches` species chapter + `take_flight` verb chapter; the Tide verb is **jetpacks/mobility** via Iron Jetpacks, the pack's first mobility verb), and **Tier 5 = Infernal fully built** (2026-05-31: `road_to_infernal` gateway + `infernal_frogs` species chapter [quartz->glowstone->soul_sand->soul_soil->blaze->netherite_scrap capstone] + `the_network` verb chapter; the Infernal verb is **Refined Storage** [RS 2.0, the digital-storage + autocrafting network], gated on nether quartz which only the Infernal frog produces - the nether-on-skyblock tier. **Tier 6 = Void fully built** (2026-06-01: `road_to_void` gateway + `void_frogs` species chapter [ender_pearl in the gateway, then end_stone->chorus_fruit->echo_shard->sculk->shulker_shell capstone] + `the_ultimate_table` verb chapter + `master_pond` endgame; the Void verb is **Extended Crafting** [singularity engine, pinned 7.0.8], the gate is a one-time **dragon expedition** [craft a 12-frame End portal from frog-farmed glowstone+soul_sand since no stronghold generates, enter the End, slay the dragon], and the endgame compresses one **Singularity per vanilla froglight resource** (one per vanilla variant - 50 as of PF 1.13, growing with PF's roster; `config/extendedcrafting/singularities/*.json`, generated by `tools/gen_singularities.py` from PF's `slime_variant` data, frog-matched colors) in the Quantum Compressor - 1000 of each resource, a proof you automated every farm - then folds the full set into the **Ultimate Singularity** (EC ships zero default singularities, so the auto-generated Ultimate needs exactly this set) -> the KubeJS-defined **Master Frog** trophy [placeholder texture; final art is a backlog item]. The compressor input is the smelted resource, not the Froglight directly: EC's singularity `ingredient` and the compressor's Cucumber `IngredientWithCount` input are both item/tag-only and reject `neoforge:components`, and a tag can't help since all variants share one item id - so per-variant froglight singularities are impossible without an upstream PF item-split; on this skyblock each resource's only source is its frog, so the singularities stay froglight-gated. The content campaign is now complete; the 6 vanilla Void variants are quested, modded Void variants deferred. **Merged to `main` 2026-06-02 (PR #47).** Two pack-wide design laws settled earlier: per-tier resource quests check the variant Froglight rather than the smelted resource (so the frog loop can't be bypassed; iron-ingot capstone and the main Mekanism steel quest are the exceptions), and each tier's slime-chain recipe uses a tier-themed filler block (Cave = stone, Geode = gravel, Bog = mossy cobblestone, Tide = mycelium, Infernal = prismarine, Void = soul_soil - Tide/Infernal/Void deliberately break the "filler is a plain non-resource block" precedent by reusing a *prior* tier's mass-renewable chain resource [netherrack would be circular for Infernal, end_stone for Void]).
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

**After the game has loaded a world** (FTB Quests and some mods rewrite their data files to CRLF on Windows), run `python tools/pack_refresh.py` from the repo root **instead of** bare `packwiz refresh`. It normalizes the LF-governed pack files (`*.snbt`, configs, etc.) back to LF on disk, then refreshes, so `index.toml` records hashes that match the committed LF blobs. Running bare `packwiz refresh` against CRLF disk state writes hashes that no committed file has (the pack's own integrity index goes silently wrong).

**After a mod pin changes** (`packwiz cf add` / `update` / `remove`), the junction-linked dev instance keeps running the old jars - its `mods/` folder is *not* junctioned (packwiz tracks metadata, not jars). With Minecraft closed, run `python tools/sync_instance.py` from the repo root to mirror the pinned mods into the instance. It drives the canonical `packwiz-installer` (auto-picks a free port, `packwiz serve`, then the official installer jar), which downloads each pin from source, hash-verifies it, and does clean add/update/remove - and refuses to run while Minecraft holds the jar locks. `--side both` to include server-only mods; `--instance <path>` to target a different instance.

`tools/` helper scripts that exist: `fix_quest_ids.py` (remap negative-leading quest IDs after editing a chapter), `validate_quests.py` (static FTB Quests validator - run after any chapter/lang edit; catches the tier-skip / dangling-dep / bad-id / em-dash / quest-recipe-drift classes, the PF-jar drift classes [singularity-ingredient + dissolution-threading vs the pinned jar, #101], and the chain-mirror classes [table chains vs the chamber, #125; the ATO chain vs the modded rows, #126 review]; see [`docs/quest_testing.md`](./docs/quest_testing.md)), `gen_singularities.py` (regenerates the EC singularity JSONs from PF variant data - rerun on PF variant/resource changes), `gen_completionist_chapters.py` (regenerates the two census chapters from PF variant data + loaded mods - rerun alongside it; ids are deterministic so completion survives), `pf_jar.py` (shared pinned-jar access for the two above), `gen_starter_island.py`, `pack_refresh.py` (above), `sync_instance.py` (above). `build_cf_zip.sh` and `slime_variant_codegen.py` are still planned per [`docs/repo_layout.md`](./docs/repo_layout.md) but not yet created.

Quest-authoring guardrail: after editing any `config/ftbquests/quests/` file, run `python tools/validate_quests.py` (a clean exit is required; the `.githooks/pre-commit` hook and the `validate-quests` CI workflow enforce it). The in-game runtime smoke test is `/sf_selftest` (op level 2) after a `/reload`.

Releases will be tag-driven (`git tag v0.x.y && git push origin v0.x.y`) once `.github/workflows/release.yml` lands. See [`docs/distribution.md`](./docs/distribution.md).
