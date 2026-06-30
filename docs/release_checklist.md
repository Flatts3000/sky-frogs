# Release checklist

Step-by-step for cutting a Sky Frogs release. The narrative/why lives in [`distribution.md`](./distribution.md); this is the do-list. Releases are **tag-driven** - pushing a `vX.Y.Z` tag fires `.github/workflows/release.yml`, which builds + publishes everything.

## 0. Pick the version (SemVer)

Post-1.0 SemVer is now in effect (v1.0.0 shipped 2026-06-14):

- **patch** (`1.0.0 -> 1.0.1`): bug fixes, recipe gating, doc/QoL only - no new content.
- **minor** (`1.0.1 -> 1.1.0`): new content (a chapter, a mod, a tier, a PF feature wave).
- **major** (`-> 2.0.0`): world-breaking changes (world wipes, mod removals that drop player items) - called out loudly at the top of the CHANGELOG section.

Only release what is already on `main`. Quest/reward content must have been playtested before its PR merged (the standing hold rule), so by release time it is already vetted.

## 0.5. Check the NeoForge pin is current and not a known-bad build

The loader pin in `pack/pack.toml` (`[versions] neoforge`) needs the same periodic-bump hygiene as the PF pin - a stale loader silently ships a buggy build to every new downloader. Before cutting a release:

1. Compare the pin against the latest 21.1.x: `curl -s https://maven.neoforged.net/releases/net/neoforged/neoforge/maven-metadata.xml | grep -oE "21\.1\.[0-9]+" | sort -t. -k3 -n | tail -3`.
2. If the pin is several patches behind, bump it to the latest 21.1.x (edit `pack/pack.toml` + the references in `CLAUDE.md` / `docs/pack_metadata.md` / `docs/cf_submission_checklist.md`), and **launch-test the dev instance on the new loader** before shipping.
3. Watch for known-bad builds: **21.1.230** applied the `GuiGraphics` tooltip patch unreliably and crashed some fresh installs at load (Apotheosis `GuiGraphicsAccessor` / `tooltipStack`); fixed by 21.1.233 (v0.13.1). A crash that is fresh-install- or machine-specific and survives reinstalls is a loader-build smell - suspect the pin first.

## 1. If this release includes a Productive Frogs pin bump

Do the standing PF-bump sweep first, on a feature branch, and merge it before releasing:

1. `cd pack && packwiz update productive-frogs -y`
2. `python tools/sync_instance.py` (Minecraft closed) - mirrors the new jar into the dev instance.
3. `python tools/gen_singularities.py`, `python tools/gen_completionist_chapters.py`, and `python tools/gen_froglight_slime_recipes.py` - regenerate from the new jar. Inspect `git status`: if new vanilla variants landed, the singularity JSONs / census chapters / froglight-slime recipes change (and the census frog may need redrawing if a zone overflows - the generator exits loudly). Machinery-only bumps show zero drift; a new variant adds one froglight-slime recipe automatically.
4. Add any **new item ids** the bump introduced (blocks, items used as quest icons/tasks) to `tools/data/item_ids.txt` - the dump predates the new version, so hand-add them (verify against the jar). Q-ITEM-EXISTS needs them.
5. `python tools/validate_quests.py` - must exit 0.
6. Read the PF release notes and quest/wire any new content per the usual pattern (chamber rows, census columns, chapters). Update CLAUDE.md's pin line + `docs/pf_pin_history.md`.

## 1.5. Quest-text editorial review (standing pre-release gate)

Any release that touched quest text (`config/ftbquests/quests/lang/en_us.snbt`) or shipped new chapters needs an editorial check before it goes out. The full corpus was reviewed once for v1.0 (issue #169, audit at `docs/audits/quest_editorial_2026_06_11/`); from here on, review what changed:

1. For every quest whose text describes a mod mechanic, **ground-truth it against the actual mod, not memory** - in authority order: pack KubeJS overrides (`pack/kubejs/`), then **Productive Frogs' own datapack** (`data/productivefrogs/recipe/` inside the jar), then **AlmostUnified** unification (`config/almostunified/unification/materials.json` rewrites unified dust/ingot/gem item ids by mod priority), then the named mod's jar. The recurring failure mode is LLM-authored text inventing a plausible mechanic, or declaring one "missing" because a hidden datapack/unification layer was skipped (both bit issue #169).
2. Check terminology (player-facing item names match in-game lang; "Froglight" not "Configurable Froglight"; "Bottle of <Species> Frog Eggs" not "Frogspawn"), ASCII-only punctuation (no em/en dashes), and balanced `&` color codes.
3. Generated census chapters (`whole_pond`, `sister_ponds`): fix text in `tools/gen_completionist_chapters.py` and regenerate, never the lang file directly.
4. `python tools/validate_quests.py` must exit 0.

## 2. Cut the release (on `main`, clean tree)

1. `git checkout main && git pull` - start from latest, working tree clean.
2. **CHANGELOG.md**: rename the `## [Unreleased]` section to `## [X.Y.Z] - YYYY-MM-DD`, add a one-line summary blurb under the heading, and leave a fresh empty `## [Unreleased]` above it. The heading MUST be exactly `## [X.Y.Z]` - `release.yml` regex-extracts that section for the GitHub release notes and the CurseForge changelog. ASCII punctuation only (no em/en dashes).
3. **pack/pack.toml**: bump `version = "X.Y.Z"`. It MUST equal the tag - the workflow's guard step fails the release otherwise. You do **not** need to touch the version strings in `pack/config/bcc-common.toml` (BCC client-vs-server check, #205) or `pack/config/bbl/core/modpack.toml` (BBL `/modpack` readout) - `release.yml` stamps both from the tag at export time, so they can't drift. (Their committed values are just a current-as-of default for the dev instance.)
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
- **`actions/setup-java`** is pinned at `@v5` (Node-24); the old `@v4` was Node-20, force-deprecated by GitHub on 2026-06-16. Keep workflow actions on Node-24 majors.

---

# The v1.0 launch (the 0.x -> 1.0 gate)

> **DONE: v1.0.0 shipped 2026-06-14**, out of beta, live on CurseForge. The gate below was passed with **three items consciously waived** as post-1.0 follow-ups: the **Master Frog final art** (still a placeholder texture), the **branding gallery** (`branding.md`), and the **final license audit**. This section is retained as historical reference for the 1.0 readiness criteria; the checkboxes are not a live to-do list anymore.

`1.0.0` is a milestone, not a routine tag: it's the promise that the pack is stable, polished, and ready for a broad audience. Everything above (section 2 onward) still applies to the actual tag cut - this section is the **readiness gate** that gated the 1.0 launch. The gate was passed (or boxes consciously waived) before the tag was cut.

The content campaign is already complete (all six tiers + Trophy Pond + Terrarium + the Completionist census, content-sized by the theme+arc principle - **not** the old "~750 quests / 22 chapters" SBR-scale target, which is superseded; see [`quest_book.md`](./quest_book.md)). So 1.0 is mostly polish, art, and launch ops, not new content.

## Content + balance

- [ ] **No soft-locks** - a fresh world is completable spawn -> Master Frog with no dead ends. Playtest each tier transition (or have testers do it); confirm the `progression.md` time estimates roughly hold.
- [ ] **Open issues triaged** - close or consciously defer everything in the milestone. (Standing open: #82 Warden quests.)
- [ ] **Slime variant catalog complete** - every shipped mod has at least one variant per applicable category (the Sister Ponds census is the audit surface).
- [ ] **`/sf_selftest` green** on a fresh world after `/reload`, and `tools/validate_quests.py` clean.
- [ ] **(Optional) difficulty config** - the deferred `config/skyfrogs.json` (spawn rates / milk counts / drop chances) if easy/normal/hard presets make the 1.0 cut.

## Art + branding (the big remaining bucket)

- [ ] **Master Frog trophy final art** - replace the placeholder texture (`kubejs/assets/kubejs/textures/item/master_frog.png`) with a real model/texture. The endgame payoff shouldn't ship as a spawn-egg glyph. (backlog)
- [ ] **Branding assets complete** per [`branding.md`](./branding.md): logo set, pack icon, CF banner, hero shot, full gallery (one set piece per tier + the singularity/Terrarium builds), social card, demo gif. (Title-screen wordmark is done.) **NOT AI-generated** - maintainer rule.
- [ ] **(Optional) custom main menu** - packmenu panorama + Tips Mod loading tips with Sky-Frogs-specific copy.

## Public-facing copy

- [ ] **CHANGELOG cleaned for players** - the 1.0 notes read like player-facing release notes, not dev shorthand. ASCII punctuation.
- [ ] **CurseForge page polished** - hook, features, How-to-play, FAQ, mod credits all current ([`curseforge_page.md`](./curseforge_page.md) is the source; edit there, push to CF). No SBR / Productive Bees comparisons in public copy (maintainer rule).
- [ ] **README / docs** - drop the DRAFT banners on docs whose decisions are now settled.

## Legal

- [ ] **Final license audit** - every bundled mod's license permits redistribution in a CurseForge pack. Most are fine (MIT / GPL / ARR-with-modpack-permission); chase explicit permission for any outlier. `NOTICE.md` reflects the bundled set.

## Versioning flip (takes effect at 1.0)

- [ ] **SemVer changes meaning post-1.0**: world-breaking changes now bump **major** (`2.0.0`) and must be called out loudly at the top of the CHANGELOG section. Minor = new content, patch = fixes (unchanged).
- [ ] **`releaseType` flips to `release`** - the workflow already derives `release` for `1.x+` (vs `beta` for `0.x`), so CurseForge will mark 1.0 a full release automatically. No action, just be aware the prerelease flag drops off the GitHub release too.

## Launch ops (after the tag is live + verified)

- [ ] **r/feedthebeast announcement** post.
- [ ] **Cross-link from the Productive Frogs CurseForge page** ("Now featured in the Sky Frogs modpack").
- [ ] **Discord announcement** beyond the automated #changelog post.
- [ ] **(Optional) launch-day let's-player / devlog** per the marketing backlog.

Then run sections 2-4 above to cut and verify the `v1.0.0` tag.
