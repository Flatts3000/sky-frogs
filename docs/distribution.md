# Distribution

> **Status:** DRAFT — non-canonical except for the CurseForge-only call (decided 2026-05-23, see `docs/backlog.md`). Versioning policy and changelog format are first-draft proposals; the release workflow is implemented (`.github/workflows/release.yml`).

How Sky Frogs ships, where players install it from, and how releases happen.

## Channels

| Channel             | URL pattern                                          | Format        | Primary? |
|---------------------|------------------------------------------------------|---------------|----------|
| **CurseForge**      | `curseforge.com/minecraft/modpacks/sky-frogs`        | manifest zip  | Yes      |
| **GitHub Releases** | `github.com/Flatts3000/sky-frogs/releases`           | CF zip + server zip mirror | Artifact mirror — not an install path |

**CurseForge is the sole player-facing channel.** Modrinth was considered but ruled out:

- The FTB utility stack (FTB Library / Quests / Teams / Chunks / Ranks / Essentials) is CurseForge-only.
- `packwiz modrinth export` inlines CF-only mods as `overrides/mods/*.jar`. Modrinth's uploader rejects this on redistribution policy grounds.
- FTB Quests is the canonical questbook (load-bearing for the pack), so dropping the FTB stack to enable Modrinth isn't an option.
- Productive Frogs is also CF-only by the same constraint.

GitHub Releases mirrors each tag's CF zip + server zip for transparency, rollback, and source-of-truth artifact hosting. Players are directed to CurseForge.

## Setup checklist (one-time, before v0.1)

- [x] **Claim CurseForge slug `sky-frogs`** — submitted 2026-05-29 with the v0.1.0 alpha file (file id `8167200`) at project ID `1558075`. Project + file are queued for CF moderation (typically 1-3 business days); not yet confirmed live.
- [x] **GitHub repo** — `Flatts3000/sky-frogs` exists; community health files landed.
- [x] **CurseForge API token** — reuses the token from `productive-frogs/.env` (`CURSEFORGE_API_KEY`, same author account). Set as the repo secret **`CF_API_TOKEN`** consumed by `release.yml`.
- [x] **CurseForge project ID** — `1558075`. Hardcoded in `release.yml`'s `env` (public, not a secret).
- [ ] **Branding assets** — upload logo / banner / hero / gallery to the CF project page. See [`pack_metadata.md`](./pack_metadata.md) for asset spec.

### CF upload API quirks discovered on first submission

The CF upload API rejects modpack uploads that include game-version IDs from the wrong type:

- **MC 1.21.1**: use `11779` (type 77784 = the modpack-class MC version), NOT `12735` (type 1 = the mod-class MC version). CF returns `errorCode 1009: Invalid game version ID ... belongs to an invalid dependency` if the wrong one is sent.
- **NeoForge**: `10150` (type 68441).
- **Java version**: do NOT send a Java-version ID in the `gameVersions` payload for modpacks. CF rejects it. Java is implied by the loader for modpack class.

So the canonical `gameVersions` payload for any Sky Frogs file going forward is `[11779, 10150]`. The future `release.yml` should pin these.

## Release workflow

Once everything's set up, releases are a tag push:

```sh
# from sky-frogs repo root
git tag v0.1.0
git push origin v0.1.0
```

`.github/workflows/release.yml` (**shipped**) takes over:

1. Checks out the tag and asserts `pack/pack.toml`'s version matches the tag (bump it before tagging).
2. Installs packwiz and runs `packwiz refresh && packwiz curseforge export` (inline — there is no separate `build_cf_zip.sh`).
3. Creates a GitHub release with the CF zip attached and the matching `## [x.y.z]` section of `CHANGELOG.md` as the notes (marked prerelease for `0.x` and `-suffix` tags).
4. Uploads the CF zip to CurseForge via the upload API, sending `gameVersions: [11779, 10150]` and `releaseType: beta` for `0.x` (`release` otherwise).

Requires the repo secret **`CF_API_TOKEN`** (the CF upload token). If it is unset, step 4 is skipped with a warning and the GitHub release still ships. The CF project id (`1558075`) is hardcoded in the workflow `env` — it is public, not a secret.

Manual release path (fallback) if the action fails: download the artifact from the GitHub release page, upload manually via the CurseForge web UI.

## Versioning policy (recap from pack_metadata.md)

- **`v0.x.y`** — pre-1.0. `x` for playtest milestones, `y` for hotfixes.
- **`v1.0.0`** — first feature-complete release.
- **`v1.x` post-1.0** — `x` for content additions / mod additions, `y` for configs-only fixes.
- **Breaking changes** that require world wipes bump the **major** version. Communicate loudly.

## Changelog format

`CHANGELOG.md` lives at repo root and uses [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format. Sections per release:

```markdown
## [v0.1.0] - 2026-06-15

### Added
- Initial release.
- All six Productive Frogs tier chapters playable.
- Skyblock Builder void world with starter island.
- ~120 starter quests across 22 chapters.

### Changed
- Disabled Industrial Foregoing ore laser drill.
- Disabled Actually Additions Lens of the Miner.

### Removed
- (none)

### Fixed
- (none)

### World-breaking
- (none — fresh world recommended but not required)
```

For 0.x releases the changelog can be brisk; for 1.x and beyond, write player-facing notes (avoid technical jargon).

## Server pack

Each release ships a `sky-frogs-server-<version>.zip` alongside the client artifact. Built by `tools/build_server.sh` (TBD), which:

1. Resolves all mod jars locally via `packwiz install`.
2. Copies `config/`, `defaultconfigs/`, `kubejs/`, `mods/` into a fresh directory.
3. Adds `install.bat`, `install.sh`, `user_jvm_args.txt` (NeoForge installer scripts).
4. Zips the lot.

Server pack is uploaded to GitHub Releases only — CurseForge's server-pack workflow is per-platform and clunky. Pack hosts pull from GH Releases.

## Cross-promotion / discoverability

For initial launch (v0.1):

- **r/feedthebeast** subreddit announcement post — link CurseForge, GitHub.
- **r/Minecraft** modded showcase post (optional, lower priority — usually noisy).
- **Cross-link from Productive Frogs mod page** on CurseForge — should mention "Now featured in the Sky Frogs modpack!"

Avoid:
- Cross-posting to /r/Minecraft general — wrong audience.
- Self-promotion in unrelated mod project pages — bad form.

## Update policy

- **Mod updates** auto-tracked by packwiz when running `packwiz update --all`. Pin major versions; allow patch+minor bumps freely.
- **Pre-1.0:** ship a `0.x` bump for any update batch that touches >5 mods OR adds a new tier of content.
- **Post-1.0:** ship a `1.x.y` bump for any update batch. Hotfixes (`x.y.z` where z bumps) ship same-day for game-breaking issues.

## Documentation

The CurseForge project page should contain:

- **One-paragraph hook** — "Skyblock where frogs replace mining."
- **A short feature list** — five bullets.
- **A "How to play" section** — first-island steps from `progression.md` Tier 0.
- **A screenshot gallery** — 4-6 in-game screenshots showing each tier's frog and its outputs.
- **Mod credits** — link to every bundled mod's listing page.
- **A short FAQ** — "Why frogs not bees? Is this related to Productive Bees? Can I add my own modded resource as a frog target?"
- **Cross-link to GitHub repo** for issue reporting and source.

## Issue reporting

- **Bugs:** GitHub Issues — `github.com/Flatts3000/sky-frogs/issues`. Template: pack version, MC version, mod loader version, steps to reproduce, log excerpt.
- **Balance feedback:** GitHub Discussions.
- **Suggestions for new mods to include:** GitHub Discussions, tagged `mod-suggestion`. Most will be declined per the [`mod_list.md`](./mod_list.md) selection criteria — that's fine, it's about being intentional, not blanket-rejecting.

## License notes (recap)

MIT for pack-authored content only. CurseForge has a "license" field — set to MIT but include in the description: *"Each bundled mod retains its own license. Refer to each mod's CurseForge page for license terms."*

## Open distribution questions

- Do we set up a **dedicated server template** (Pterodactyl egg, Docker compose) for community hosts? Defer to post-v1.0 unless community demand emerges.
- Do we offer a **client launcher one-click install** beyond the CurseForge launcher? E.g., `prismlauncher://...` URLs. Probably overengineering for v0.1.
- Should we ship a **localization workflow** (Crowdin? Weblate?) for community translations? Defer; en_us only at v1.0.
- **Sponsorship / donations** — do we accept? If so, Ko-fi link in pack pages. Decision is the author's call, not a technical question.
