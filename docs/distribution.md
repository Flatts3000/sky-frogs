# Distribution

> **Status:** DRAFT — non-canonical. Modrinth + CurseForge dual-publishing is the working assumption. Versioning policy, changelog format, and release workflow are first-draft proposals.

How Sky Frogs ships, where players install it from, and how releases happen.

## Channels

| Channel        | URL pattern                                          | Format     | Primary?  |
|----------------|------------------------------------------------------|------------|-----------|
| **Modrinth**   | `modrinth.com/modpack/sky-frogs`                     | `.mrpack`  | Yes       |
| **CurseForge** | `curseforge.com/minecraft/modpacks/sky-frogs`        | manifest zip | Yes     |
| **GitHub Releases** | `github.com/Flatts3000/sky-frogs/releases`      | both       | Mirror    |

Modrinth is the primary channel because:
- Free hosting with no review backlog for new modpacks.
- Better revision history and version pinning UX.
- Open-source community alignment matches the MIT pack content.
- packwiz outputs `.mrpack` natively.

CurseForge is co-equal in priority because of the **user base size** — it's still the default launcher for many players. The cost is going through CF's modpack approval process (1–3 days first time, faster on subsequent versions).

## Setup checklist (one-time, before v0.1)

- [ ] **Claim Modrinth slug `sky-frogs`** — create empty project, mark as Modpack, set description, license MIT.
- [ ] **Claim CurseForge slug `sky-frogs`** — submit empty project for approval. Allow 1-3 business days.
- [ ] **GitHub repo** — create `Flatts3000/sky-frogs` (public), push existing local commits.
- [ ] **Modrinth API token** — generate in Modrinth account → settings → API tokens. Save as GitHub secret `MODRINTH_TOKEN`.
- [ ] **CurseForge API token** — generate in CurseForge account → API. Save as `CF_API_TOKEN`.
- [ ] **Modrinth project ID** — save as `MODRINTH_PROJECT_ID` secret (referenced by the release action).
- [ ] **CurseForge project ID** — save as `CF_PROJECT_ID`.
- [ ] **Branding assets** — upload logo / banner / hero / gallery to both project pages. See [`pack_metadata.md`](./pack_metadata.md) for asset spec.

## Release workflow

Once everything's set up, releases are a tag push:

```sh
# from sky-frogs repo root
git tag v0.1.0
git push origin v0.1.0
```

The `release.yml` GitHub Action takes over:

1. Checks out the tag commit.
2. Runs `tools/build_mrpack.sh` and `tools/build_cf_zip.sh`.
3. Creates a GitHub release with both artifacts attached and a changelog excerpt from `CHANGELOG.md`.
4. Uploads the `.mrpack` to Modrinth via API.
5. Uploads the CF zip to CurseForge via API.
6. Both uploads set the same version number, changelog, and `game_versions: [1.21.1]`, `loaders: [neoforge]`.

Manual release path (fallback) if the action fails: download artifacts from the GitHub release page, upload manually via each platform's web UI.

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

Each release ships a `sky-frogs-server-<version>.zip` alongside the client artifacts. Built by `tools/build_server.sh` (TBD), which:

1. Resolves all mod jars locally via `packwiz install`.
2. Copies `config/`, `defaultconfigs/`, `kubejs/`, `mods/` into a fresh directory.
3. Adds `install.bat`, `install.sh`, `user_jvm_args.txt` (NeoForge installer scripts).
4. Zips the lot.

Server pack is uploaded to GitHub releases only — not to Modrinth/CurseForge (their server-pack workflow is per-platform and clunky).

## Cross-promotion / discoverability

For initial launch (v0.1):

- **r/feedthebeast** subreddit announcement post — link Modrinth, CurseForge, GitHub.
- **r/Minecraft** modded showcase post (optional, lower priority — usually noisy).
- **Discord communities** — FTB Discord modpacks channel, NeoForge Discord modpack-showcase.
- **Cross-link from Productive Frogs mod page** — both Modrinth and CurseForge listings for the mod should mention "Now featured in the Sky Frogs modpack!"

Avoid:
- Cross-posting to /r/Minecraft general — wrong audience.
- Self-promotion in unrelated mod project pages — bad form.

## Update policy

- **Mod updates** auto-tracked by packwiz when running `packwiz update --all`. Pin major versions; allow patch+minor bumps freely.
- **Pre-1.0:** ship a `0.x` bump for any update batch that touches >5 mods OR adds a new tier of content.
- **Post-1.0:** ship a `1.x.y` bump for any update batch. Hotfixes (`x.y.z` where z bumps) ship same-day for game-breaking issues.

## Documentation

Modrinth and CurseForge project pages should both contain:

- **One-paragraph hook** — "Skyblock where frogs replace mining."
- **A short feature list** — five bullets.
- **A "How to play" section** — first-island steps from `progression.md` Tier 0.
- **A screenshot gallery** — 4-6 in-game screenshots showing each tier's frog and its outputs.
- **Mod credits** — link to every bundled mod's listing page.
- **A short FAQ** — "Why frogs not bees? Is this related to Productive Bees? Can I add my own modded resource as a frog target?"
- **Cross-link to GitHub repo** for issue reporting and source.

Keep both project pages identical content-wise. Edit one, edit the other; templates live in `docs/distribution/page_templates.md` (TBD).

## Issue reporting

- **Bugs:** GitHub Issues — `github.com/Flatts3000/sky-frogs/issues`. Template: pack version, MC version, mod loader version, steps to reproduce, log excerpt.
- **Balance feedback:** GitHub Discussions or a dedicated Discord channel.
- **Suggestions for new mods to include:** GitHub Discussions, tagged `mod-suggestion`. Most will be declined per the [`mod_list.md`](./mod_list.md) selection criteria — that's fine, it's about being intentional, not blanket-rejecting.

## License notes (recap)

MIT for pack-authored content only. Modrinth and CurseForge both have "license" fields — set to MIT but include in the description: *"Each bundled mod retains its own license. Refer to each mod's CurseForge or Modrinth page for license terms."*

## Open distribution questions

- Do we set up a **dedicated server template** (Pterodactyl egg, Docker compose) for community hosts? Defer to post-v1.0 unless community demand emerges.
- Do we offer a **client launcher one-click install** beyond Modrinth App and CurseForge launcher? E.g., `prismlauncher://...` URLs. Probably overengineering for v0.1.
- Should we ship a **localization workflow** (Crowdin? Weblate?) for community translations? Defer; en_us only at v1.0.
- **Sponsorship / donations** — do we accept? If so, Ko-fi link in pack pages. Decision is the author's call, not a technical question.
