# Roadmap

> **Status:** living document. Phases are sequencing, not deadlines. Treat checkboxes as work units, not commitments. Update as scope shifts.

The path from "pack scaffold boots in a launcher" to "Sky Frogs v1.0 lives on CurseForge." Written for an author building their first modpack — explicit about what code/scripts handle vs. what the human has to do directly.

## Where we are right now

Pack version `0.0.3`. The scaffold boots in the CurseForge launcher with the FTB utility stack, JEI, Jade, and the Tier 0 substrate mods (Skyblock Builder, Ex Deorum, Forgiving Void, Rain Shield). No quests yet. No KubeJS overrides yet. No Productive Frogs yet (waiting on the 1.21.1 rebuild).

The pack currently loads into a void world with a starter island — but every recipe is vanilla and nothing has been tuned for skyblock progression.

## Phases at a glance

| Phase | Target | What it unlocks |
|-------|--------|-----------------|
| **0. Foundation** ✅ | Repo + scaffold + decisions | A buildable pack and a public GitHub repo |
| **1. Tier 0 playable** | `0.0.x` pre-alpha | Bootstrap loop: dirt → sieve → iron |
| **2. First Iron Froglight** | `0.1.0` alpha | Productive Frogs integrated; Tier 1 reachable |
| **3. Mid-tier alpha** | `0.2.0` → `0.5.0` | Tiers 2 through 5 each get a chapter and slime variants |
| **4. Feature-complete** | `0.6.0` → `0.9.0` | Tier 6 + Arcane endgame + per-mod side chapters |
| **5. v1.0 launch** | `1.0.0` | Polish, balance pass, branding assets, CF page live |
| **6. Maintenance** | `1.x.y` | Mod updates, content additions, hotfixes |

## Phase 1 — Tier 0 playable (current phase)

**Goal:** a fresh world is playable to first iron ingot without crashes or dead ends. No frogs yet — just the bootstrap loop.

**Blockers:**
- Category-typed Metallic Frogspawn must exist as a PF item (so it can be a quest reward). If PF doesn't expose it, this becomes a PF-side feature request. Tracked in [`docs/backlog.md`](./backlog.md).

**Deliverables:**
- [ ] **First-join inventory grant** implemented in `pack/kubejs/server_scripts/first_join.js` (KubeJS `PlayerEvents.loggedIn` with a persistent-data first-join guard): 2-3× oak sapling, 1× water bucket, 1× lava bucket, ~16× cooked beef. FTB Quests book auto-opens.
- [ ] **`anti.js`** KubeJS file — disables Ex Deorum sieves + meshes (per [`docs/kubejs_overrides.md`](./kubejs_overrides.md) Pillar 1). No tech-mod disables yet; scaffolds Phase 3+.
- [ ] **`slime_spawning.js`** KubeJS file — overrides vanilla `minecraft:slime` spawn rules to allow any biome at low light (Pillar 2). Sanity-test the spawn rate in a dark 5×5×3 room.
- [ ] **Welcome quest chapter** (`welcome.snbt`) in FTB Quests: ~18 quests per [`docs/quest_book.md`](./quest_book.md) spine, including the cooldown-repeatable "Replacement Frogspawn" emergency quest.
- [ ] **Pack version bump** to `0.0.5` (next after the 0.0.4 design-pivot reset). Reimport and verify a fresh-world player reaches their first Iron Configurable Froglight in ~30-60 min following only the questbook.

**You drive:**
- Confirm the first-join grant final list (saplings count, food type/amount).
- Confirm the slime spawn rate feels right after first playtest.
- Confirm the Welcome quest spine reads well in-game.

**I drive:**
- Write the KubeJS scripts (`first_join.js`, `anti.js`, `slime_spawning.js`).
- Write the FTB Quests `welcome.snbt` SNBT.
- Document the Ex Deorum barrel water-collection mechanic specifics during implementation.

## Phase 2 — First Iron Froglight (v0.1 alpha)

**Goal:** a player can follow the questbook from spawn to producing their first Iron Configurable Froglight. The pack's core loop is provable.

**Blockers:**
- ✅ **Productive Frogs on CurseForge** (resolved 2026-05-25) — PF published as v1.0.1 for 1.21.1 / NeoForge and added to the pack via `packwiz cf add`. This was the v0.1 release gate.

**Deliverables:**
- [x] Productive Frogs added via `packwiz cf add productive-frogs` (pinned at v1.0.1).
- [ ] **KubeJS Pillar 2** — Productive Frogs parent species spawn overrides ([`docs/kubejs_overrides.md`](./kubejs_overrides.md)). Verify whether PF exposes datapack spawn recipes; if not, use quest-reward eggs as fallback.
- [ ] **KubeJS Pillar 4** — first recipe override to force frog ingredients in the metal smelting path (or accept the unmodified path for alpha).
- [ ] **First slime variant JSONs** for vanilla metallics (iron, copper, gold). Drop directly in `pack/kubejs/data/skyfrogs/productivefrogs/slime_variant/`.
- [ ] **Tier 1 quest chapter** ("Metallic Mastery") in FTB Quests. ~15-20 quests walking from breeding to milking to first ingot.
- [ ] **CurseForge project claimed** and submitted for approval. Allow 1-3 business days.
- [ ] **CHANGELOG `[Unreleased]` rolled into `[v0.1.0]`** with date.
- [ ] Tag `v0.1.0`, push, upload zip to CF.

**You drive:**
- PF build + CF publication.
- CurseForge account, project submission, first upload.
- Playtest the Tier 1 loop end-to-end. Report broken quests, mistuned drop rates, missing recipes.
- Branding assets: logo, pack icon, hero shot, first 1-2 gallery screenshots (Tier 1 enclosure). See [`docs/branding.md`](./branding.md).

**I drive:**
- KubeJS scripts, slime variant JSONs, FTB Quests SNBT for Tier 1 chapter, recipe overrides.
- Updated docs / CHANGELOG.
- Tag + release workflow scaffolding.

## Phase 3 — Mid-tier alpha (v0.2 → v0.5)

**Goal:** Tiers 2 through 5 each become playable, one per minor release.

| Version | Tier | Category | New mods needed                                  |
|---------|------|----------|--------------------------------------------------|
| `v0.2`  | 2    | Mineral  | (Optional) Mekanism for modded variants          |
| `v0.3`  | 3    | Gem      | (Optional) AE2 for certus quartz variant         |
| `v0.4`  | 4    | Aquatic  | (Optional) Industrial Foregoing for pink slime   |
| `v0.5`  | 5    | Infernal | Portal kit mod for Nether access; Productive Metalworks for nether-themed metals |

**Per-tier deliverables (repeat for each):**
- [ ] Quest chapter authored in FTB Quests.
- [ ] Slime variant JSONs for the tier's resources (vanilla + any modded).
- [ ] KubeJS recipe overrides to force frog ingredients in tier-relevant recipes.
- [ ] "Mining shortcut" disables added to `anti.js` as we add tech mods (laser drill, mining lens, digital miner, quarry cards).
- [ ] Gallery screenshot for the tier (per [`docs/curseforge_page.md`](./curseforge_page.md) capture order).
- [ ] CHANGELOG updated, release tagged, CF uploaded.

**You drive:**
- Decide which tech mods ship in each minor release (the mod selection criteria in [`docs/mod_list.md`](./mod_list.md) apply).
- Playtest each tier — they should each take 2-8 hours per progression.md estimates.
- Capture the tier's screenshot for the CF gallery.

**I drive:**
- Mod additions via packwiz, KubeJS overrides, quest authoring, slime variants.

## Phase 4 — Feature-complete (v0.6 → v0.9)

**Goal:** Tier 6 (Arcane) reachable; per-mod side chapters added; endgame creative trophy exists.

**Deliverables:**
- [ ] Tier 6 chapter ("Arcane Mastery") + The End chapter.
- [ ] Endgame singularity loop ("Master Hive (Pond)" chapter — see [`docs/quest_book.md`](./quest_book.md)).
- [ ] **Sky Frogs Master Frog trophy item** — KubeJS-defined item or resourcepack-overridden custom item with components. Resolution captured in [`docs/backlog.md`](./backlog.md).
- [ ] Per-mod side chapters: one for each significant tech mod (Mekanism, AE2, IF, Powah, EnderIO, etc.). These are optional-but-recommended infrastructure guides.
- [ ] Full slime variant catalog — every shipped mod has at least one variant per applicable category.

**You drive:**
- Endgame trophy design (visual + reward UX).
- Final balance pass on tier transitions (does the player get stuck anywhere?).
- Remaining gallery screenshots (Tier 5/6 set pieces, singularity altar).

**I drive:**
- All authored content.

## Phase 5 — v1.0 launch

**Goal:** the pack is ready for a broad public release.

**Deliverables:**
- [ ] All v0.1 success criteria from [`docs/design_overview.md`](./design_overview.md) met.
- [ ] All v1.0 success criteria met (~750 quests across ~22 chapters, all categories have 5+ slime variants).
- [ ] **Branding assets complete** per [`docs/branding.md`](./branding.md): logo set, pack icon, CF banner, hero, full gallery, social card, demo gif.
- [ ] **(Optional) `packmenu` + Tips Mod** added with custom title screen, panorama, loading-screen tips.
- [ ] CHANGELOG cleaned up for public-facing release notes (less technical, more player-friendly).
- [ ] CurseForge page polished: hook, features, How-to-play, FAQ all updated.
- [ ] **Final license audit** — verify every bundled mod's license allows redistribution.
- [ ] r/feedthebeast announcement post + cross-link from PF mod page on CurseForge.
- [ ] Tag `v1.0.0`, release.

**You drive:**
- All visual assets.
- License audit (asking individual mod authors for permission where needed).
- Launch announcement.

**I drive:**
- Polish passes on docs, KubeJS, quest balance, configs.
- Pre-launch QA checklist.

## Phase 6 — Maintenance

**Goal:** keep the pack alive past launch.

- Monthly minor releases bundling mod updates + content additions.
- Same-week hotfixes for game-breaking bugs.
- Community PR review per [`CONTRIBUTING.md`](../CONTRIBUTING.md).
- Quarterly re-eval: should we bump MC version? Are bootstrap mods still maintained? Are there new mods worth adding?

## Top risks (track in `docs/backlog.md`)

1. **Productive Frogs V1 might not be feature-complete** by v0.1 target. Slime Milker is the load-bearing block for Tier 1 scale-up; without it, players are stuck at one Iron Froglight per ~10 minutes. v0.1 gates on Slime Milker landing in PF V1.
2. **Skyblock Builder / Ex Deorum staying on 1.21.1.** If either mod dies and we need to migrate MC versions, the entire bootstrap design needs rework. Track those mods' release activity.
3. **CurseForge approval delay** on first project submission. CF is our sole channel; an approval delay = no launch. Submit the empty CF project as soon as you're ready to claim the slug, well before v0.1.
4. **License compatibility** — one or two bundled mods might require explicit author permission to redistribute in a pack. Audit before v0.1.

## Decision points coming up

(In rough order. Each one is a question for you when we hit it.)

- **First-join inventory grant contents** (Phase 1).
- **Sieve drop rate tuning** (Phase 1). Target: ~5 slimeballs in 30 min of sieving.
- **First-launch frog source** (Phase 2) — inventory grant egg vs. quest reward.
- **Mekanism in v0.2 or wait?** Decision on tech mods per tier.
- **Endgame trophy** — KubeJS item vs. resourcepack-overridden item (Phase 4).
- **Custom panorama / main menu** for v0.1 or defer to v1.0.

## How to update this roadmap

When a deliverable lands, check it off in the relevant phase. When a phase completes, mark it ✅ in the "Phases at a glance" table. When scope or sequencing changes, edit the phases — don't add notes around them. The roadmap is a snapshot of the current plan, not a history of past plans.
