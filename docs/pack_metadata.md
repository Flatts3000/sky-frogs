# Pack Metadata

> **Status:** DRAFT — non-canonical. Slugs, version scheme, channel choices, and branding direction are all proposals, not decisions.

## Identity

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| **Pack name**    | Sky Frogs                                                          |
| **Slug**         | `sky-frogs` (CurseForge - claimed)                                 |
| **CF project ID**| `1558075` (load-bearing for future `release.yml` automation; set as `CF_PROJECT_ID` GitHub secret) |
| **Author**       | Flatts3000                                                         |
| **Tagline**      | Skyblock where frogs replace mining                                |
| **Long pitch**   | A void-skyblock NeoForge 1.21.1 modpack built around Productive Frogs. Iron, gold, diamonds, and beyond are won by breeding Resource Frogs and feeding them matching Resource Slimes — automated mining is disabled. |
| **License**      | MIT (pack content); bundled mods retain their own licenses         |
| **Source**       | [github.com/Flatts3000/sky-frogs](https://github.com/Flatts3000/sky-frogs) |

## Platform Targets

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| **MC version**   | `1.21.1` — single version, no multi-version build matrix           |
| **Loader**       | NeoForge `21.1.233` - version pinned in `pack/pack.toml`            |
| **Java**         | Java 21 (NeoForge 1.21.1 requirement)                              |
| **Launcher**     | CurseForge launcher (primary); Prism / ATLauncher / MultiMC also work via the CurseForge manifest |
| **Server**       | Yes — server zip ships alongside client                            |

## Version Scheme

Semantic versioning with a leading `0.` until v1.0:

- **`v0.x.y` — pre-1.0.** `x` bumps on each minor playtest milestone; `y` bumps on hotfixes.
- **`v1.0.0`** — first "feature complete" release: all six tiers, ~750 quests, all dimensions wired.
- **`v1.x` — post-1.0.** `x` bumps when adding new mods, new chapters, or significant balance changes; `y` bumps on configs-only / KubeJS-only fixes.
- **Breaking changes** (world wipes, mod removals that drop player items) bump the **major** version. World safety matters; warn loudly in changelogs.

## Distribution Channels

CurseForge is the sole distribution channel. The FTB utility stack (FTB Library / Quests / Teams / Chunks / Ranks / Essentials) is CurseForge-only, and Modrinth forbids inlining CF jars as overrides — so a Modrinth release isn't possible without dropping FTB Quests, which is non-negotiable. Productive Frogs is also CF-only by the same downstream constraint.

| Channel        | Format            | Notes                                                          |
|----------------|-------------------|----------------------------------------------------------------|
| **CurseForge** | `manifest.json` + overrides zip | Sole primary channel. Requires CurseForge mod project IDs in manifest. |
| **GitHub Releases** | source-of-truth artifact mirror | CF zip + server zip attached to each tag for transparency and rollback. Not a player install path. |

Build tool: [`packwiz`](https://github.com/packwiz/packwiz) drives the CF export from a single `pack.toml` + `index.toml` + per-mod `.pw.toml` files. See [`repo_layout.md`](./repo_layout.md).

## Update Cadence

- **Pre-1.0:** ship a new `0.x.0` whenever a major content tier becomes playable. Hotfix as needed.
- **Post-1.0:** monthly minor releases is the aspiration. Hotfixes (`x.y.z` where `z` bumps) ship same-week if a bug is gameplay-blocking.
- **Mod updates** are bundled into the next minor release unless a critical security or world-corruption fix is published — those get same-day hotfixes.

## Branding Assets (TBD)

- 256×256 logo (frog silhouette on a void background — TBD)
- 512×288 banner (CurseForge "header" dimensions)
- 1280×720 hero (CurseForge gallery first slide)
- A short demo gif (~5s, ~3MB) showing the egg→tadpole→frog→froglight loop

All assets ship from `docs/branding/` (TBD directory). Use the same color palette as the Productive Frogs categories — six accent colors keyed to `Category.tintArgb()`.

## Required External Accounts

| Account        | Needed for                                              |
|----------------|---------------------------------------------------------|
| CurseForge     | Pack project, manifest upload                           |
| GitHub         | Source hosting, Actions release pipeline                |

## Compatibility

- **Server:** Yes. A server zip ships alongside each release (built from the same packwiz tree).
- **Multiplayer:** Yes, but balance is single-player-tuned. Multiplayer-specific tuning (frog spawn rates, slime cap multipliers) is a v1.x stretch goal.
- **Custom client mods:** Acceptable for cosmetic-only client mods (shaders, minimaps via JourneyMap if shipped, etc.). Any client mod that affects game logic should not be added without testing.

## Changelog Format

Keep a Changelog format in `CHANGELOG.md` at repo root once we have any releases. Sections per release:
- **Added** — new mods, new quests, new slime variants
- **Changed** — recipe overrides, balance tweaks, mod version bumps
- **Removed** — mod removals (loud warnings if player-facing items vanish)
- **Fixed** — bug fixes
- **World-breaking** — anything that requires a fresh world or migration steps

## Telemetry

None. Sky Frogs ships no telemetry or analytics. If a bundled mod ships its own telemetry, it's documented in the mod-list rationale ([`mod_list.md`](./mod_list.md)).
