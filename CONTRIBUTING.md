# Contributing to Sky Frogs

Thanks for your interest in contributing! Sky Frogs is a **content modpack** built around [Productive Frogs](https://github.com/Flatts3000/productive-frogs). This document covers how to file issues, what kinds of contributions are welcome here vs. upstream, and how to submit pull requests.

## Scope: what belongs in this repo

Sky Frogs ships only pack-side content. **Java code does not live here.** If a contribution would require new mod behavior — new blocks, items, entities, hooks, or registry-level changes — file it against [Productive Frogs](https://github.com/Flatts3000/productive-frogs/issues) instead and reference the pack-side need.

Acceptable contributions to this repo:

- KubeJS scripts (`kubejs/{startup,server,client}_scripts/`)
- Datapack overrides (`kubejs/data/<ns>/`) — including new Resource Slime variant JSONs
- Resourcepack overrides (`kubejs/assets/<ns>/`)
- Mod configs (`config/`, `defaultconfigs/`)
- FTB Quests data (`config/ftbquests/quests/`)
- Pack metadata (`pack.toml`, `index.toml`, `manifest.json`)
- Pack-level docs (`docs/`, `README.md`)

If you're not sure where something belongs, open a Discussion before writing code.

## Reporting Issues

- **Pack bugs**: open an issue using the **Bug Report** template. Include the pack version, Minecraft version, NeoForge version, launcher (CurseForge / Prism / other), and steps to reproduce. Attach `latest.log` from `.minecraft/logs/` — long logs go in a gist.
- **Mod inclusion / variant suggestions**: use the **Mod Suggestion** template. The pack is intentionally curated — most suggestions are declined per [`docs/mod_list.md`](./docs/mod_list.md). That's not a rejection of your taste; it's a scope decision. Suggestions that fit the existing tier structure or fill a clear gap are the ones most likely to land.
- **Design / progression feedback**: use the **Feature Request** template. Frame it as the problem you're trying to solve, not just the change you want.
- **General questions**: use [GitHub Discussions](https://github.com/Flatts3000/sky-frogs/discussions) rather than the issue tracker.

Don't open issues for security vulnerabilities — see [SECURITY.md](./SECURITY.md).

### Issues that belong upstream, not here

| Symptom                                           | Where to file                                                         |
|---------------------------------------------------|------------------------------------------------------------------------|
| A specific frog or slime behaves wrong            | [productive-frogs](https://github.com/Flatts3000/productive-frogs/issues) |
| A specific mod crashes or behaves wrong on its own | That mod's issue tracker                                              |
| The pack disables an item you wanted to use       | Here — open a Feature Request explaining the use case                  |
| A quest is broken / unsatisfiable                 | Here — Bug Report                                                      |
| You want a new modded resource to be frog-farmable | Here — Mod Suggestion (variant request)                                |

## Submitting Pull Requests

### Branching

- `main` is protected — all changes land via PR.
- Create a feature branch from `main` named like `feat/add-mekanism-osmium-variant` or `fix/tier3-gem-chapter-typos`.
- Don't push directly to `main` (docs-only changes by the maintainer are the exception).

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <short subject>

<body — explain WHY, not what>
```

Types we use:

- `feat:` — new pack content (quests, variants, configs, scripts)
- `fix:` — bug fix (broken quest, mis-tagged item, wrong recipe)
- `refactor:` — restructuring with no player-visible change
- `docs:` — documentation only
- `chore:` — tooling, build config, infrastructure
- `ci:` — CI/CD changes
- `perf:` — load-time or runtime performance work

One logical change per commit. Squash trivially-related work locally before PR.

### Content Quality Expectations

- **Stay in scope.** Don't add a mod, recipe override, or KubeJS rule that isn't motivated by the [progression](./docs/progression.md). The pack defines an intended path; the bar for breaking from it is high and needs a written rationale.
- **Cross-mod compat is JSON, not Java.** When adding Resource Slime variants for a new mod, use `neoforge:conditions → mod_loaded` so the JSON is inert without that mod present. See [`docs/kubejs_overrides.md`](./docs/kubejs_overrides.md) Pillar 3.
- **Quests are SNBT.** Edit chapter `.snbt` files directly, or use the in-game FTB Quests editor (creator mode) and copy the regenerated SNBT back into the repo. Keep chapter IDs stable — players in active worlds depend on them.
- **Don't add mods casually.** Each new mod is a maintenance and load-time tax. PRs that add mods need a one-paragraph justification matching the [`docs/mod_list.md`](./docs/mod_list.md) selection criteria.
- **Docs in the same PR.** Pack-level changes that affect player experience should update the relevant `/docs/*.md` file. If a design DRAFT becomes a decision because of your PR, drop the DRAFT banner and update the working assumptions in [`CLAUDE.md`](./CLAUDE.md).

### Adding a Resource Slime Variant

Most variant contributions need no script changes — just a JSON drop:

1. Add a JSON to `kubejs/data/skyfrogs/productivefrogs/slime_variant/<name>.json` following the schema in [`docs/kubejs_overrides.md`](./docs/kubejs_overrides.md) Pillar 3.
2. Wrap in `neoforge:conditions → mod_loaded` if the variant is mod-specific.
3. If the variant is part of a generated batch, add it to the manifest in `tools/slime_variant_codegen.py` (once that tool exists) rather than writing the JSON by hand.
4. Open a PR with the new file plus a one-line `CHANGELOG.md` entry under `### Added`.

### Before You Open a PR

1. `packwiz refresh` runs cleanly inside `pack/` (once the `pack/` tree exists).
2. New `.snbt` quest files parse — open the pack in Minecraft and verify the chapter loads.
3. New KubeJS scripts don't throw on `/reload` (check `latest.log`).
4. Docs updated where relevant.
5. PR description explains the **why** — the **what** is in the diff.

### Review

- The maintainer reviews when bandwidth permits — this is an OSS hobby project, expect days, not hours.
- Review feedback is collaborative; address comments or push back if you disagree. Both are fine.
- Approved + green CI + no unresolved threads → maintainer squash-merges. `main` enforces squash-only and deletes the branch on merge.

## What We Probably Won't Accept

- **Fabric / Quilt support.** Sky Frogs is NeoForge-only by design — Productive Frogs is NeoForge-only.
- **Kitchen-sink mod additions.** "I like this mod" isn't a justification; "this mod supplies a Tier 4 resource we currently can't farm" is.
- **Re-enabling intentionally disabled items** (laser drills, mining lenses, digital miner). The progression depends on these being off.
- **Java mods bundled into the pack.** If a feature needs Java, it goes in [productive-frogs](https://github.com/Flatts3000/productive-frogs).
- **PRs that ship balance changes without playtesting evidence.** "I changed the sieve drop rate from 5% to 12%" needs to come with "I played through Tier 0 and counted slimeballs over N minutes."

## Maintainer Cadence

This is a hobby OSS project. Realistic expectations:

- Issue triage: within ~1 week of opening.
- PR review: ~1 week, sometimes longer.
- Releases: irregular, driven by significant content batches, upstream Productive Frogs releases, or critical fixes.

If something is urgent (security, major upstream break), ping the maintainer in the relevant issue/PR; they'll prioritize.

Thanks again for contributing! 🐸
