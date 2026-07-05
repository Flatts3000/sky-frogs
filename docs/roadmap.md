# Roadmap

> **Status:** living document. Phases are sequencing, not deadlines. Treat checkboxes as work units, not commitments. Update as scope shifts.

The path from "pack scaffold boots in a launcher" to "Sky Frogs v1.0 lives on CurseForge." Written for an author building their first modpack — explicit about what code/scripts handle vs. what the human has to do directly.

## Where we are right now

The pack is **live on CurseForge** (v1.4.4, shipped 2026-07-05), shipping tag-driven releases (client + dedicated-server packs) to CurseForge and GitHub. Productive Frogs is pinned at **1.24.6** (Fresh Coat - a cosmetic bucket / Slime Milk texture refresh). The frog loop and full campaign are built and merged: a couple dozen KubeJS override scripts (anti.js, first_join.js, the per-tier slime chains, the Dissolution Chamber engine + every tier's rows, the spawnery primers, the storage/plastic/steel/log/catalyst/mossy-gate/JDT/boss overrides) and **27 quest chapters / ~343 quests spanning all six tiers** plus the Trophy Pond boss campaign (with the optional Dragon + Wither altar quests), the Terrarium automation chapter, the Completionist census, and the optional Void-tier Warden expedition. The mod set spans every tier's verb (Mekanism, Industrial Foregoing, Just Dire Things + Building Gadgets, Iron Jetpacks, Refined Storage, Extended Crafting) plus Powah/Flux Networks, Apotheosis (a combat/enchanting/loot layer), the decoration suite, and the QoL stack.

All six tiers (Welcome -> Cave -> Geode -> Bog -> Tide -> Infernal -> Void) are built and playable end to end, through the Master Pond endgame and the Sky Frogs Master Frog trophy. The content campaign is complete and v1.0.0 has shipped; the remaining post-1.0 work is the three consciously-waived launch-gate items (Master Frog final art, the branding gallery, the license audit), plus balance and optional side chapters.

## Phases at a glance

| Phase | Target | What it unlocks |
|-------|--------|-----------------|
| **0. Foundation** ✅ | Repo + scaffold + decisions | A buildable pack and a public GitHub repo |
| **1. Tier 0 playable** ✅ | `0.0.x` pre-alpha | Bootstrap loop: cobble gen + dark-room cave_slime farm → iron |
| **2. First Iron Froglight** ✅ | `0.1.0` alpha | Productive Frogs integrated; Tier 1 (Cave) reachable |
| **3. Mid-tier alpha** ✅ | `0.2.0` → `0.5.0` | Tiers 2-5 (Geode, Bog, Tide, Infernal) built |
| **4. Feature-complete** | `0.6.0` ✅ → `0.9.0` | Tier 6 (Void) endgame ✅ + per-mod side chapters (#109 ✅ shipped v0.7.0) + reward/polish passes. (Reality note: the release train ran ahead of this table - content was tier-complete by v0.2/v0.3, and v0.3+ became community-driven polish/mod releases. v0.6.0 shipped 2026-06-06: Powah + Flux Networks, the QoL wave, the Discord-linked welcome chapter. v0.7.0 shipped 2026-06-07: the completionist update - census chapters in their own Completionist section, every modded resource craftable, PF 1.13 + the Melting Point chapter, the Powered Up chapter, the chamber-pressed Heavy Core/Mace, the FancyMenu title screen.) |
| **5. v1.0 launch** ✅ | `1.0.0` (shipped 2026-06-14) | Polish, balance pass, CF page live; gate consciously waived on Master Frog art / branding gallery / license audit (now post-1.0) |
| **6. Maintenance** | `1.x.y` | Mod updates, content additions, hotfixes |

## Phase 1 — Tier 0 playable ✅

**Goal:** a fresh world is playable to first iron ingot without crashes or dead ends. No frogs yet — just the bootstrap loop.

**Blockers:**
- Category-typed frog egg must exist as a PF item (so it can be a quest reward). PF ships placeable frog eggs that hatch a tadpole with no priming step, so this is satisfied.

**Deliverables:**
- [x] **First-join inventory grant** implemented in `pack/kubejs/server_scripts/first_join.js` (KubeJS `PlayerEvents.loggedIn` with a persistent-data first-join guard): saplings, water bucket, lava bucket, cooked food. FTB Quests book auto-opens.
- [x] **`anti.js`** KubeJS file - disables Ex Deorum sieves + meshes (per [`docs/kubejs_overrides.md`](./kubejs_overrides.md) Pillar 1), plus the Mekanism Digital Miner now that tech mods ship.
- [x] **Cave-slime starter island** - the SkyblockBuilder starter island is forced to `minecraft:swamp` and a pack biome modifier (`add_cave_slime_island.json`) adds `productivefrogs:cave_slime` to it. Cave is Tier 1, so cave_slime (not bog_slime) is the bootstrap parent. All 6 PF default slime spawns are disabled; the pack owns spawning.
- [x] **Welcome quest chapter** (`welcome.snbt`) in FTB Quests, including the cooldown-repeatable replacement-frog emergency quest.

**You drive:**
- Confirm the first-join grant final list (saplings count, food type/amount).
- Confirm the cave_slime spawn rate feels right after first playtest.
- Confirm the Welcome quest spine reads well in-game.

**I drive:**
- Write the KubeJS scripts (`first_join.js`, `anti.js`).
- Force the starter island to `minecraft:swamp` and add cave_slime via the biome modifier, then verify spawns in a dark room.
- Write the FTB Quests `welcome.snbt` SNBT.
- Document the Ex Deorum barrel water-collection mechanic specifics during implementation.

## Phase 2 — First Iron Froglight (v0.1 alpha) ✅

**Goal:** a player can follow the questbook from spawn to producing their first Iron Configurable Froglight. The pack's core loop is provable.

**Blockers:**
- ✅ **Productive Frogs on CurseForge** (resolved 2026-05-25) - PF published for 1.21.1 / NeoForge and added to the pack via `packwiz cf add`. This was the v0.1 release gate.

**Deliverables:**
- [x] Productive Frogs added via `packwiz cf add productive-frogs` (now pinned at v1.8.0).
- [x] **Pillar 2 parent species** ([`docs/kubejs_overrides.md`](./kubejs_overrides.md)) - the Cave parent (Tier 1) spawns on the starter island via the `add_cave_slime_island.json` biome modifier; the other parents are distributed via quest-reward frogspawn bottles in their tier chapters.
- [x] **KubeJS recipe overrides** - `your_first_iron_ingot.snbt` plus `iron_slime_bucket.js` thread the first frog ingredients into the metal path; the pack-wide froglight-check principle (quests detect the variant Froglight, not the smelted resource) lands here too.
- [x] **First slime variants** for the vanilla metallics, threaded through the Cave slime chain (`cave_slime_chain.js`: iron -> copper -> gold -> coal -> redstone).
- [x] **Tier 1 (Cave) quest chapters** in FTB Quests: `your_first_iron_ingot.snbt`, `scaling_the_colony.snbt`, `cave_frogs.snbt`, `storage_and_crafting.snbt`. The Cave verb is crafting upgrades / storage (Sophisticated + Functional, quartz-free networks via `storage_quartz_free.js`).
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

**Goal:** the mid-tiers each become playable, one per minor release. Each tier layers ONE new verb onto the frog loop (anti-repetition).

| Version | Tier | Category | Verb + mods                                      | Status |
|---------|------|----------|--------------------------------------------------|--------|
| `v0.1`  | 1    | Cave     | Crafting upgrades / storage (Sophisticated + Functional, quartz-free) | ✅ done |
| `v0.2`  | 2    | Geode    | Automation (Mekanism + Generators + Tools)       | ✅ done |
| `v0.3`  | 3    | Bog      | Just Dire Things tier-1 progression + Building Gadgets in `tools_and_things.snbt`; plastic hard-gated behind the Bog plastic-frog; pink-slime capstone. IF spine moved to `road_to_tide.snbt` (Tier 4 gateway). | ✅ done |
| `v0.4`  | 4    | Tide     | Jetpacks/mobility (Iron Jetpacks) in `take_flight.snbt`; aquatic chain in `drowned_riches.snbt`; nautilus_shell capstone. | ✅ done |
| `v0.5`  | 5    | Infernal | Refined Storage (digital storage + autocrafting) in `the_network.snbt`; nether chain in `infernal_frogs.snbt`; netherite_scrap capstone. The nether-on-skyblock tier. | ✅ done |
| `v0.6`  | 6    | Void     | Extended Crafting (singularity endgame) in `the_ultimate_table.snbt`; End chain in `void_frogs.snbt`; dragon-expedition gate in `road_to_void.snbt`; the Master Frog trophy in `master_pond.snbt`. The content campaign's capstone. | ✅ shipped (merged #47, 2026-06-02) |

Note: the built tier order is Cave=Tier 1 (the starter), Geode=Tier 2, Bog=Tier 3, Tide=Tier 4, Infernal=Tier 5, Void=Tier 6. Per-tier slime-chain filler blocks: Cave = stone, Geode = gravel, Bog = mossy cobblestone, Tide = mycelium, Infernal = prismarine, Void = soul soil.

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

**Goal:** Tier 6 (Void) reachable; per-mod side chapters added; endgame creative trophy exists.

**Deliverables:**
- [x] Tier 6 chapters: `road_to_void` (dragon-expedition gateway) + `void_frogs` (End chain) + `the_ultimate_table` (Extended Crafting verb). **Built 2026-06-01.**
- [x] Endgame singularity loop (`master_pond.snbt`): froglight Singularities -> Ultimate Singularity -> Master Frog. **Built.**
- [x] **Sky Frogs Master Frog trophy item** — shipped as a KubeJS-defined item (`kubejs:master_frog`) with a placeholder texture; final 3D art remains a [`backlog.md`](./backlog.md) item.
- [ ] Per-mod side chapters: one for each significant tech mod (Mekanism, AE2, IF, Powah, EnderIO, etc.). These are optional-but-recommended infrastructure guides.
- [ ] Full slime variant catalog — every shipped mod has at least one variant per applicable category.

**You drive:**
- Endgame trophy design (visual + reward UX).
- Final balance pass on tier transitions (does the player get stuck anywhere?).
- Remaining gallery screenshots (Tier 5/6 set pieces, singularity altar).

**I drive:**
- All authored content.

## Phase 5 — v1.0 launch ✅ (shipped 2026-06-14)

**Goal:** the pack is ready for a broad public release.

> **v1.0.0 shipped 2026-06-14**, out of beta, live on CurseForge (client + dedicated-server packs). The launch gate was met with **three items consciously waived** as post-1.0 follow-ups: the **Master Frog final art** (still a placeholder texture), the **branding gallery** (`branding.md`), and the **final license audit**. The historical gate checklist lives in [`release_checklist.md`](./release_checklist.md) ("The v1.0 launch"). The deliverables below are the original Phase 5 sketch, kept for context.

**Deliverables:**
- [x] All v0.1 success criteria from [`docs/design_overview.md`](./design_overview.md) met.
- [x] ~~All v1.0 success criteria met (~750 quests across ~22 chapters...).~~ **Superseded** - the "~750 quests / 22 chapters" SBR-scale target was dropped for the theme+arc chapter-sizing principle (see [`quest_book.md`](./quest_book.md)). The content campaign is complete at ~335 quests / 27 chapters; 1.0 was polish/launch, not quest volume.
- [ ] **Branding assets complete** per [`docs/branding.md`](./branding.md): logo set, pack icon, CF banner, hero, full gallery, social card, demo gif. **Waived at 1.0; post-1.0 follow-up.** (Logo/icon/title-screen wordmark are done.)
- [x] **(Optional) `packmenu` + Tips Mod** - the FancyMenu title screen shipped (v0.7.0).
- [x] CHANGELOG cleaned up for public-facing release notes (less technical, more player-friendly).
- [x] CurseForge page polished: hook, features, How-to-play, FAQ all updated.
- [ ] **Final license audit** — verify every bundled mod's license allows redistribution. **Waived at 1.0; post-1.0 follow-up.**
- [ ] r/feedthebeast announcement post + cross-link from PF mod page on CurseForge.
- [x] Tag `v1.0.0`, release. **Done 2026-06-14.**

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

1. ~~**Productive Frogs V1 might not be feature-complete** by v0.1 target. Slime Milker is the load-bearing block for Tier 1 scale-up.~~ RESOLVED: PF 1.5.3 shipped the Slime Milker (with JEI pages), so the scale-up beat is unblocked.
2. **Skyblock Builder / Ex Deorum staying on 1.21.1.** If either mod dies and we need to migrate MC versions, the entire bootstrap design needs rework. Track those mods' release activity.
3. **CurseForge approval delay** on first project submission. CF is our sole channel; an approval delay = no launch. Submit the empty CF project as soon as you're ready to claim the slug, well before v0.1.
4. **License compatibility** — one or two bundled mods might require explicit author permission to redistribute in a pack. Audit before v0.1.

## Decision points coming up

(In rough order. Each one is a question for you when we hit it.)

- **Tier 4 (Tide) verb** - which new verb does Tide layer onto the frog loop? (Cave=storage, Geode=automation, Bog=IF; Tide is open.)
- **Endgame trophy** — KubeJS item vs. resourcepack-overridden item (Phase 4).
- **Custom panorama / main menu** for v0.1 or defer to v1.0.

## How to update this roadmap

When a deliverable lands, check it off in the relevant phase. When a phase completes, mark it ✅ in the "Phases at a glance" table. When scope or sequencing changes, edit the phases — don't add notes around them. The roadmap is a snapshot of the current plan, not a history of past plans.
