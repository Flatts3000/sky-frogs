# CurseForge Submission Checklist (v0.1.0)

> One-time-use guide for the first CF project submission. Once the slug is claimed
> and approved, future releases ship via `release.yml` + `tools/build_cf_zip.sh`
> (TBD) - this doc captures the manual flow.
>
> Cross-references: page copy is in [`curseforge_page.md`](./curseforge_page.md);
> the channel decision and longer-term workflow live in [`distribution.md`](./distribution.md);
> identity/version/branding constants are in [`pack_metadata.md`](./pack_metadata.md).

## Before you start

- [x] **Pack icon ready** - `pack/icon.png`, 256x256 RGBA PNG, ~61 KB (well under
  the 500 KB ceiling). "SKY / FROGS" wordmark over the mossy frog on void per
  [`branding.md`](./branding.md). AI-assisted composite; refine post-claim if
  desired.
- [ ] **`pack/pack.toml` version = `0.1.0`** (or whatever you're submitting as).
  This is the manifest version that CF reads; bump it before exporting.
- [ ] **Pack zip built**: from inside `pack/`, run `packwiz refresh && packwiz curseforge export`.
  Output is `Sky Frogs-0.1.0.zip` (~53 KB - manifest + overrides only; mods are
  CF references, not bundled).
- [ ] **CF account** in good standing (no active project bans).

## Step 1 - Create the project

Go to <https://www.curseforge.com/dashboard/projects/create>.

| Field | Value (paste-ready) |
|---|---|
| **Type** | Modpack |
| **Name** | `Sky Frogs` |
| **Slug** | `sky-frogs` (auto-derived from name; verify it isn't taken) |
| **Summary** (≤120 chars) | `A skyblock where frogs do the mining. Breed Resource Frogs, feed them slimes, and watch the ore, gems, and ender pearls fall out.` |
| **Categories** | `Skyblock` (primary), `Quests` (secondary). Add `Tech` if a third slot exists. |
| **Description** | Paste from [`curseforge_page.md`](./curseforge_page.md) - everything below the `PASTE MARKER` comment. It is paste-ready (no meta labels to strip): the `# Sky Frogs` heading down through the License section goes straight into the CF Description field. (The doc is the single source of truth; the old derived `cf_description.md` was consolidated into it 2026-06-06.) |
| **License** | `MIT` (pack content). The page copy already includes the "each bundled mod retains its own license" disclaimer. |
| **Source code URL** | `https://github.com/Flatts3000/sky-frogs` |
| **Issue tracker** | `https://github.com/Flatts3000/sky-frogs/issues` |
| **Discord** | `https://discord.gg/r6MhZ73nsM` (the community server, Terraform-managed in `sky-frogs-community`). |
| **Cover image** | Upload `pack/icon.png` (or a banner if you have one - 512x288 is the CF banner size, but the icon doubles as cover for the alpha). |

Click **Submit for review**. CF moderation: typically 1-3 business days.

## Step 2 - While waiting for approval

CF projects under review are not publicly visible. You can still:

- **Upload the zip as a file** (see Step 3) - it queues for the same review pass.
- **Add screenshots** to the gallery via the dashboard once images exist.
- **Set up the GitHub release** for the same `v0.1.0` tag so the artifact is mirrored:
  ```sh
  git tag v0.1.0
  git push origin v0.1.0
  gh release create v0.1.0 "pack/Sky Frogs-0.1.0.zip" --title "v0.1.0 - first playtest milestone" --notes-file CHANGELOG.md
  ```

## Step 3 - Upload the file

> The v0.1.0 alpha file was uploaded via the **CF Upload API** (file id `8167200`), not the
> web form. If you script future uploads, read the "CF upload API quirks" section in
> [`distribution.md`](./distribution.md) first - the modpack-class game-version IDs are
> `[11779, 10150]` and a Java-version ID must NOT be sent. The web-form fields below are the
> manual fallback.

From the approved project dashboard, **Files** -> **Upload File**:

| Field | Value |
|---|---|
| **File** | `pack/Sky Frogs-0.1.0.zip` |
| **Display name** | `Sky Frogs v0.1.0 (alpha)` |
| **Release type** | **Alpha** (mark it explicitly so curious players know expectations) |
| **Game version** | `1.21.1` (pick by name; the web form resolves the modpack-class ID for you - only the API needs the raw `11779`) |
| **Mod loader** | `NeoForge` (version `21.1.244` if asked) |
| **Java version** | Skip - the modpack class does not take a Java-version selector (CF rejects one on the API; the web form omits the field). Java is implied by the loader. |
| **Changelog** | First release - paste the `## [Unreleased]` block from `CHANGELOG.md` and retitle to `## [v0.1.0] - YYYY-MM-DD`. |

Submit. The file goes through a separate moderation pass (usually faster than the project pass).

## Step 4 - After approval

Once the project is live at `curseforge.com/minecraft/modpacks/sky-frogs`:

- [ ] **Gallery shots** - capture 4-6 in-game screenshots per the order in
  [`curseforge_page.md`](./curseforge_page.md) ("Screenshots (TBD)" section). 1920x1080.
- [ ] **Banner** - 512x288 PNG per [`branding.md`](./branding.md). Upload via dashboard's
  Logo/Header section.
- [ ] **Hero / first gallery slide** - 1280x720 PNG, frog visible in frame, void
  backdrop, one tier accent colour dominant.
- [ ] **Cross-promotion** - add a line to the [Productive Frogs CF page](https://www.curseforge.com/minecraft/mc-mods/productive-frogs):
  "Featured in the [Sky Frogs](https://www.curseforge.com/minecraft/modpacks/sky-frogs) modpack."
- [ ] **`release.yml` + `tools/build_cf_zip.sh`** - automate future tag-driven releases
  per the workflow in [`distribution.md`](./distribution.md#release-workflow).

## What CF can bounce you for

- **Missing icon** - the single most common rejection. Don't submit without it.
- **Short / placeholder description** - moderators want to know what the pack is.
  The `curseforge_page.md` body is well past the threshold.
- **License mismatch** - the project license, the manifest's `author` field, and
  any bundled-mod attribution must align. Sky Frogs is MIT for pack content +
  per-mod licenses (already documented in `curseforge_page.md` License section).
- **Forbidden mod bundling** - the manifest references CF mods by `projectID` /
  `fileID`, not by bundled jar. `packwiz curseforge export` does this correctly
  by default; the resulting zip should have *no* `.jar` files anywhere. The current
  export is 53 KB - that's the right order of magnitude for a manifest-only zip.

## Troubleshooting

- **"Project name already exists"** - someone else grabbed `sky-frogs`. Pivot to
  `sky-frogs-pack` or similar. The internal pack name in `pack.toml` can stay
  `Sky Frogs`; only the CF URL slug changes.
- **"File rejected: invalid manifest"** - usually a mod with a missing or
  mismatched `projectID`. Run `packwiz refresh` then re-export.
- **"Productive Frogs not found"** - PF is CF-API-excluded for *third-party*
  fetches, but the CF launcher (first-party) downloads it fine. Reviewers do
  spot-check installs - if they see a PF download error, link them to the PF
  CF page to confirm it's a real project.
