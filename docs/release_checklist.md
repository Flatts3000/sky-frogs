# Release checklist

Step-by-step for cutting a Sky Frogs release. The narrative/why lives in [`distribution.md`](./distribution.md); this is the do-list. Releases are **tag-driven** - pushing a `vX.Y.Z` tag fires `.github/workflows/release.yml`, which builds + publishes everything.

## 0. Pick the version (SemVer, pre-1.0)

- **patch** (`0.9.0 -> 0.9.1`): bug fixes, recipe gating, doc/QoL only - no new content.
- **minor** (`0.9.1 -> 0.10.0`): new content (a chapter, a mod, a tier, a PF feature wave).
- **major** (`-> 1.0.0+`): reserved for the v1.0 launch; post-1.0, world-breaking changes bump major and are called out loudly in the CHANGELOG.

Only release what is already on `main`. Quest/reward content must have been playtested before its PR merged (the standing hold rule), so by release time it is already vetted.

## 1. If this release includes a Productive Frogs pin bump

Do the standing PF-bump sweep first, on a feature branch, and merge it before releasing:

1. `cd pack && packwiz update productive-frogs -y`
2. `python tools/sync_instance.py` (Minecraft closed) - mirrors the new jar into the dev instance.
3. `python tools/gen_singularities.py` and `python tools/gen_completionist_chapters.py` - regenerate from the new jar. Inspect `git status`: if new vanilla variants landed, the singularity JSONs / census chapters change (and the census frog may need redrawing if a zone overflows - the generator exits loudly). Machinery-only bumps show zero drift.
4. Add any **new item ids** the bump introduced (blocks, items used as quest icons/tasks) to `tools/data/item_ids.txt` - the dump predates the new version, so hand-add them (verify against the jar). Q-ITEM-EXISTS needs them.
5. `python tools/validate_quests.py` - must exit 0.
6. Read the PF release notes and quest/wire any new content per the usual pattern (chamber rows, census columns, chapters). Update CLAUDE.md's pin line + `docs/pf_pin_history.md`.

## 2. Cut the release (on `main`, clean tree)

1. `git checkout main && git pull` - start from latest, working tree clean.
2. **CHANGELOG.md**: rename the `## [Unreleased]` section to `## [X.Y.Z] - YYYY-MM-DD`, add a one-line summary blurb under the heading, and leave a fresh empty `## [Unreleased]` above it. The heading MUST be exactly `## [X.Y.Z]` - `release.yml` regex-extracts that section for the GitHub release notes and the CurseForge changelog. ASCII punctuation only (no em/en dashes).
3. **pack/pack.toml**: bump `version = "X.Y.Z"`. It MUST equal the tag - the workflow's guard step fails the release otherwise.
4. `python tools/pack_refresh.py` - regenerates `index.toml` and updates pack.toml's `[index]` hash. **Stage `pack/index.toml` AND `pack/pack.toml` in the SAME commit** as the version bump; nothing else auto-catches a stale index (the #55 -> #56 follow-up).
5. Commit: `commit "chore: release vX.Y.Z" "<one-line body>"` on `main` (this is the authorized exception to no-direct-commits-on-main).
6. `git push`
7. `git tag vX.Y.Z && git push origin vX.Y.Z`

## 3. Watch the pipeline

`gh run watch $(gh run list --workflow release.yml --limit 1 --json databaseId --jq '.[0].databaseId') --exit-status`

`release.yml` runs: version guard -> CF client export -> changelog extract -> GitHub release (client zip attached; `0.x` = prerelease) -> **dedicated-server pack build + attach** -> CurseForge upload (client) -> CurseForge **server pack as a child file** (parentFileID) -> Discord #changelog post. All steps should be green.

## 4. Verify

- [ ] GitHub release `vX.Y.Z` exists with **both** `Sky.Frogs-X.Y.Z.zip` (client) and `sky-frogs-server-X.Y.Z.zip`.
- [ ] CurseForge shows the new client file, with the server pack under its "Additional Files".
- [ ] Discord #changelog has the release post.

## Gotchas (learned the hard way)

- **Version must match the tag** (workflow guard) - bump pack.toml before tagging.
- **Stage index.toml + pack.toml together** after `pack_refresh.py` - a stale index ships hashes no committed file has.
- **CHANGELOG heading format is load-bearing** - `## [X.Y.Z]` exactly, or the notes/CF-metadata extraction misses the section.
- **`releaseType`**: `0.x` -> `beta`, `1.x+` -> `release` (the workflow derives this; CF requires it even on the server child upload).
- **Secrets**: `CF_API_TOKEN` and `DISCORD_CHANGELOG_WEBHOOK` are repo secrets. If unset, those steps warn-and-skip (the GitHub release still ships); upload/post manually.
- **Server-pack build** is `continue-on-error` - a CurseForge third-party-download hiccup won't sink the client release, but check it actually built. A client-only mod mistagged `side = "both"` can break the server build; see [`distribution.md`](./distribution.md) server-pack section.
- **`actions/setup-java@v4`** is Node-20 (deprecated); bump to a Node-24 version when convenient.
