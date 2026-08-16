# Repo Layout

> **Status:** Current. packwiz is the tooling, the tree below is the tree, and CI is three workflows (`validate-quests.yml`, `validate-pack.yml`, `release.yml`). Seventeen helper scripts exist and are listed under [Helper scripts](#helper-scripts-tools); the only things still unbuilt are the two marked **planned** there.

How the Sky Frogs repo is organized, what tooling builds it, and where each kind of content lives.

## Tool: packwiz

We use [**packwiz**](https://github.com/packwiz/packwiz) - a CLI that manages mod versions in TOML files and exports CurseForge zip outputs (and Modrinth `.mrpack`, which we don't use - see [`distribution.md`](./distribution.md)). Industry-standard for community NeoForge packs in 2026.

Install: `go install github.com/packwiz/packwiz@latest`. (packwiz has no GitHub releases and isn't on winget; Go install from source is the only path.)

## Directory layout

What the repo actually looks like. `pack/` is the packwiz tree and the only part that reaches a player;
everything else is authoring, tooling, or record.

```
sky-frogs/                            # this repo root
├── README.md, CHANGELOG.md, CLAUDE.md, LICENSE, NOTICE.md
├── CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md
├── .gitattributes                    # LF for sources/configs/docs, CRLF for .bat/.cmd/.ps1
├── .githooks/                        # pre-commit: runs the quest validator
├── .github/
│   └── workflows/
│       ├── validate-quests.yml       # the FTB Quests validator, on quest + mod-pin changes
│       ├── validate-pack.yml         # index integrity + config/defaultconfigs byte-parity
│       └── release.yml               # on tag: CF client + server packs, GH release, CF upload, Discord
├── docs/                             # 28 markdown docs; CLAUDE.md's doc map is the index
├── pack/                             # the packwiz tree (everything below ships)
│   ├── pack.toml                     # pack metadata (name, version, MC, loader)
│   ├── index.toml                    # generated - regenerate with tools/pack_refresh.py, never bare refresh
│   ├── icon.png
│   ├── mods/                         # one .pw.toml per mod, named after the CurseForge slug
│   │   ├── productive-frogs.pw.toml
│   │   ├── skyblock-builder.pw.toml
│   │   ├── ex-deorum.pw.toml
│   │   ├── ftb-quests-forge.pw.toml
│   │   └── ... (one per pinned mod)
│   ├── config/                       # live mod configs, including config/ftbquests/quests/
│   ├── defaultconfigs/               # what NeoForge seeds a missing config from - keep in sync
│   └── kubejs/                       # server_scripts/, startup_scripts/, client_scripts/, data/, assets/
├── tools/                            # the helper scripts, listed below; tools/data/ holds their inputs
├── gen/                              # generator scratch output, not shipped
├── branding/                         # logo and art sources
└── build/, dist/                     # local export output (gitignored)
```

## The `pack/` overrides tree

Anything inside `pack/` other than `pack.toml`, `index.toml`, and `mods/` is shipped verbatim to the player's game folder. Mirrors what's in `sky-bees-reborn-reference/extracted/`:

```
pack/
├── pack.toml
├── index.toml
├── mods/
│   └── *.pw.toml                     # per-mod manifests, no jars
├── config/                           # mod config files
│   ├── ftbquests/
│   │   └── quests/
│   │       ├── chapters/             # ~22 .snbt files (one per chapter)
│   │       └── ...
│   ├── mekanism/
│   ├── productivefrogs-common.toml   # our PF config
│   └── ...
├── defaultconfigs/                   # same overrides again - what NeoForge seeds a
│                                     # MISSING config from, so pack values survive
│                                     # the file being recreated (check_pack_configs.py)
├── kubejs/
│   ├── startup_scripts/
│   │   ├── global.js
│   │   ├── registry.js
│   │   └── slime_variant_generator.js   # the generator we discussed in kubejs_overrides.md
│   ├── server_scripts/
│   │   ├── anti.js
│   │   ├── productive_frogs.js
│   │   ├── sieve.js
│   │   ├── tags.js
│   │   └── ... (one per mod that needs overrides)
│   ├── client_scripts/
│   │   ├── jei.js
│   │   └── lang.js
│   ├── data/
│   │   └── skyfrogs/                 # our datapack namespace
│   │       ├── productivefrogs/
│   │       │   └── slime_variant/    # generated JSONs land here
│   │       └── tags/
│   └── assets/
│       └── skyfrogs/
│           ├── lang/
│           │   └── en_us.json
│           └── textures/             # custom textures if any
└── packmenu/                         # custom main menu branding (optional)
```

## Build flow

```
1. pack.toml + per-mod .pw.toml + overrides
        ↓ (packwiz refresh)
2. index.toml regenerated
        ↓ (packwiz curseforge export)
3. sky-frogs-<version>.zip             → upload to CurseForge + attach to GH Release
```

## Helper scripts (`tools/`)

Everything that exists today, in one place. The two with the longest explanations keep their own
sections below; the rest are one-liners because their own docstrings carry the detail.

| Script | What it does |
|---|---|
| `pack_refresh.py` | LF-normalize the pack's text files, then `packwiz refresh`. Use instead of bare refresh (see below). |
| `sync_instance.py` | Mirror the pinned mods into the dev instance via `packwiz-installer`. Minecraft must be closed. |
| `sync_instance_loader.py` | Check, and with `--apply` set, the dev instance's NeoForge loader against the pack pin. |
| `validate_quests.py` | The static FTB Quests validator. Clean exit required; the pre-commit hook and CI both run it. |
| `fix_quest_ids.py` | Remap quest IDs that parse as negative signed longs (see below). |
| `score_quest_voice.py` | Score quest descriptions for mechanical AI-tells; regenerates `docs/quest_rewrite_candidates.md`. |
| `gen_singularities.py` | Regenerate the Extended Crafting singularity JSONs from PF variant data. |
| `gen_completionist_chapters.py` | Regenerate the two census chapters from PF variant data + the loaded mods. |
| `gen_froglight_slime_recipes.py` | Regenerate the Froglight to Slime-in-a-Bucket recipes for every variant. |
| `gen_starter_island.py` | Generate the starter-island structure NBT for Skyblock Builder. |
| `pf_jar.py` | Shared access to the pinned Productive Frogs jar, the ground truth the three generators read. |
| `ironjetpacks_tiers.py` | Work out which coil each jetpack takes, since Iron Jetpacks assigns them by tier position. |
| `check_pack_configs.py` | Verify every FML-managed override is byte-identical in `config/` and `defaultconfigs/`. `--fix` syncs. |
| `build_server.py` | Build the dedicated-server pack (`sky-frogs-server-<version>.zip`). Also how the release workflow builds it. |
| `cf_release.py` | Upload a packwiz-exported zip to CurseForge as a new file. Files only; the description is dashboard-only. |
| `check_server_pack_flag.py` | Audit whether each published CurseForge file is *typed* as a Server Pack (the manual post-release step). |
| `cf_comments.py` | Read the CurseForge project's comments through the website's undocumented v1 API. No auth needed. |

Two scripts named below are still **planned** and do not exist: `build_cf_zip.sh` and
`slime_variant_codegen.py`.

### `tools/pack_refresh.py` (exists)

Wrapper around `packwiz refresh`. FTB Quests and some mods rewrite their data files (`*.snbt`, configs) with the platform's native line endings on every world load - CRLF on Windows - while git stores them as LF (`.gitattributes`). packwiz hashes the working-tree bytes, so a bare `packwiz refresh` run against post-load CRLF disk state records hashes that the committed LF blobs don't have, leaving `index.toml` silently wrong. This script normalizes the LF-governed pack files back to LF on disk (the same transform git's clean filter applies on commit), then runs `packwiz refresh`. Use it instead of bare `packwiz refresh` whenever the game may have touched pack files. Run from anywhere: `python tools/pack_refresh.py`.

### `tools/fix_quest_ids.py` (exists)

Remaps FTB Quests IDs whose leading hex digit is 8-F (these parse as negative signed longs, get rejected on load, and drop their dependency links). Run after hand-editing any chapter: `python tools/fix_quest_ids.py <snbt-file> ...`.

### `tools/build_cf_zip.sh` (planned)
```sh
#!/usr/bin/env bash
set -euo pipefail
python "$(dirname "$0")/pack_refresh.py"   # LF-normalize + refresh (not bare `packwiz refresh`)
cd "$(dirname "$0")/../pack"
packwiz curseforge export
mv ./*.zip ../dist/
```

### `tools/slime_variant_codegen.py`

Reads a YAML manifest of slime variants and emits one JSON per variant under `pack/kubejs/data/skyfrogs/productivefrogs/slime_variant/`. Re-runs on `make refresh`. Manifest looks like:

```yaml
- mod: mekanism
  variants:
    - id: osmium
      category: bog
      primer: mekanism:ingot_osmium
      smelt: mekanism:ingot_osmium
      crush: { item: mekanism:dust_osmium, count: 2 }
    - id: tin
      category: bog
      primer: mekanism:ingot_tin
      smelt: mekanism:ingot_tin
```

Lighter than embedding generation in KubeJS startup scripts, and the JSON files are inspectable in JEI without booting the game.

## CI workflows

Three, not one. Each is path-triggered on both `pull_request` and `push`, so a change lands the same
check whichever way it arrives.

### `.github/workflows/validate-quests.yml`

Runs `tools/validate_quests.py`. Triggers on `pack/config/ftbquests/**`, `pack/kubejs/**`, `pack/mods/**`
and `tools/*.py` - the last one deliberately wider than the validator itself, because the validator
imports `pf_jar`, `gen_completionist_chapters` and `ironjetpacks_tiers`, and pinning the trigger to the
entry point once let a change to a check's own data source skip CI. The job takes seconds; running it on
an unrelated tool edit is the cheaper mistake. The same check runs locally through `.githooks/pre-commit`.

### `.github/workflows/validate-pack.yml`

Runs `tools/check_pack_configs.py`, which enforces that every FML-managed override is byte-identical in
`pack/config/` and `pack/defaultconfigs/`. Triggers on either config tree or on the script.

### `.github/workflows/release.yml` - on tag push (`v*`)

The whole publish, in order: resolve the version from the tag, **guard that `pack.toml` matches it**,
stamp the version into the BCC and BBL configs, build the CurseForge export, extract the matching
`CHANGELOG.md` section, create the GitHub release, build the dedicated-server pack, attach it, upload
both to CurseForge (the server pack as a child file), print the reminder that the server pack still
needs typing by hand in the Authors Console, post to Discord #changelog, and finally **fail the run if
no server pack shipped**. See [`distribution.md`](./distribution.md) for the why and
[`release_checklist.md`](./release_checklist.md) for the do-list.

## Adding a mod

```sh
cd pack/
packwiz cf add <curseforge-slug>        # CurseForge is the sole distribution channel
packwiz refresh
git add mods/<new-mod>.pw.toml index.toml
git commit -m "feat: add <mod> for <reason from mod_list.md>"
```

If the mod doesn't exist on CurseForge yet (e.g., a dev version of Productive Frogs), use `packwiz url add` with a direct URL.

## Removing a mod

```sh
cd pack/
packwiz remove <mod-slug>
packwiz refresh
git add mods/ index.toml
git commit -m "chore: remove <mod> (<reason>)"
```

When removing a tier-supplier mod, also update `kubejs_overrides.md` and the `slime_variant_codegen.py` manifest to remove the now-orphaned variants.

## Editing a quest

Open the chapter `.snbt` file directly in any editor (FTB Quests uses a JSON-like format). Or boot the pack, edit in-game via FTB Quests' built-in editor (creator mode), then copy the regenerated SNBT back into the repo.

The in-game flow is faster for adding quests; direct-edit is better for bulk renaming or refactoring chapter dependencies.

## Open layout questions

- **packwiz vs `kotlin-modpack-helper` vs raw scripts** - packwiz is the strongest community choice in 2026 even for CF-only distribution.
- **Where do build artifacts live** - `dist/` at repo root, gitignored. Release uploads pull from there.
- **Subrepo vs monorepo with productive-frogs** - Sky Frogs stays its own repo. Productive Frogs is a sibling project, pulled by version pin. No git submodule.
