# Quest coverage audit: Productive Frogs features vs Sky Frogs quests

**Date:** 2026-07-24
**PF baseline:** pinned `1.24.6`; audited against the `1.25.0` ("Second Helpings") feature set, since that is today's bump target.
**Method:** the audit spine is Productive Frogs' own in-game guide entries plus its item/block registry (`PFItems.java`, `PFBlocks.java`) - the mod's canonical feature surface. Each feature was cross-referenced against every task, reward, and icon in `pack/config/ftbquests/quests/chapters/*.snbt` and the titles in `lang/en_us.snbt`. "Quested" means a dedicated quest tasks or teaches the feature; an icon-only appearance without a teaching quest does not count.

---

## Summary: the real gaps

An enabled PF feature with no quest. Ordered by priority.

Two quests to add, both from PF 1.25.0, both gated on the bump landing on CurseForge before they can be built (their item ids don't exist in the pinned jar yet):

| # | Feature | PF version | Placement (decided) | Status |
|---|---------|-----------|--------------------|--------|
| 1 | **Virtual Terrarium** (+ Display Dome + 5 upgrades) | 1.25.0 (NEW) | **Void tier** (maintainer). Stock recipe is only ~Infernal (ender eye = overworld ender pearl + blaze powder; needs the Terrarium Controller). **Gate: KubeJS recipe override requiring a void Froglight** (decided 2026-07-24) - matches the pack's froglight-check law. Specific void variant TBD (suggest the void capstone, shulker_shell). | To build after bump |
| 2 | **Slime Milk Basin** | 1.25.0 (NEW) | **~Bog tier** - recipe-gated: 8x packed mud + slime ball | To build after bump |

Everything else in the mod is quested (see the full table). Everything below is **no quest by decision** (maintainer, 2026-07-24), not a gap:

- **Potion of Hopping** - dropped. Its only brewing recipe is awkward potion + **raw frog legs** (glowstone upgrades to Hopping II), and raw frog legs drop only from killing a frog (the Frog Net relocates, it doesn't yield legs). Questing it pushes the same frog-killing the Frog Legs decision rejects, so it's out too.
- **Frog Legs / Soup** (raw / cooked / soup) - questing it pushes players to kill their own resource frogs.
- **Tadpole Bucket** (`resource_tadpole_bucket`) - not worth a quest.
- **Sprinkler redstone switch** (1.24.0) - the Sprinkler is quested; the redstone control is a refinement the pack leaves to the guide.
- **Equivalence / Midas lane** (1.23.0) - `equivalence.enabled` defaults off and the pack doesn't enable it, so nothing in the lane is craftable.
- **Equivalence / Midas lane** (Alembic, Mimic Slime/Milk, Midas frog, Prismatic Froglight, Distiller - PF 1.23.0). **Off by default** (`equivalence.enabled`), and the pack's `productivefrogs-common.toml` does not enable it, so none of it is craftable in-pack. Correctly unquested. If the pack ever opts in, this whole lane needs a chapter.
- **Reinforced boss Froglights + the three receptacles.** These are build sub-components of the two boss altars, folded into the altar quests rather than tasked individually. Not a gap.

---

## Priority calls for the 1.25.0 bump (today)

You asked especially about new features. Both 1.25.0 additions are unquested and both are genuine automation upgrades a player would want pointed at:

1. **Virtual Terrarium - highest priority.** It is a whole void-tier automation machine (Processor + Dome, netted frog, milk in, results out the bottom, four upgrade slots, RF Overclock). **Placement decided (maintainer, 2026-07-24): void tier, gated by void recipes.** Note the stock recipe does NOT gate to void on its own: `virtual_terrarium` = 4x ender eye + 4x amethyst block + Terrarium Controller; ender pearls come from overworld endermen (dark-room farmable, even on skyblock), so the real stock gate is blaze powder + the Controller = Infernal. **Gate decided (2026-07-24): KubeJS recipe override requiring a void Froglight** (`productivefrogs:configurable_froglight` with a void `slime_variant` component), matching the pack's froglight-check law - the same component-ingredient pattern used in `dissolution_slime_recipes.js` / `froglight_slime_recipes.js`. Swap it in for one of the stock ingredients (e.g. the 4 amethyst blocks, since the 3x3 is already full). Suggest the void capstone variant `shulker_shell` for a true-endgame gate; confirm the variant at build. The Dome (`tinted_glass` + `amethyst_shard`) is Geode-cheap; the Processor is the part to gate. Teach: form it (Dome on Processor), feed the frog its own-species milk (Mimic Milk for Midas), and the upgrade slots (Bounty/Appetite, Smelter *or* Melter, Overclock needs power). Full guide entry ships, so the quest can stay short.

2. **Slime Milk Basin - second.** A pipeable, leave-alone milk source: pour milk in, it spawns that variant's slimes on the same budget as a placed pool, and when it runs dry it just waits for the next bucket instead of draining away. **Placement decided (maintainer, 2026-07-24): by its crafting recipe** - 8x packed mud + 1 slime ball, which is cheap and mud-centric, so it lands around the Bog tier where mud is trivially available. Confirm the exact chapter at build time against where packed mud first comes free. Teach the one real gotcha: breaking it loses the milk inside, and it refuses boss-tier milk (not an altar bypass).

Both are new item/block ids, so on the bump they must be hand-added to `tools/data/item_ids.txt` (the dump predates 1.25.0) or `Q-ITEM-EXISTS` will fail once they are tasked. New ids: `virtual_terrarium`, `virtual_terrarium_dome`, `vt_upgrade_bounty`, `vt_upgrade_appetite`, `vt_upgrade_smelter`, `vt_upgrade_melter`, `vt_upgrade_overclock`, `slime_milk_basin`.

No other new quests. Frog Legs, Potion of Hopping, the Tadpole Bucket, and the Sprinkler redstone switch are all deliberately unquested (see the summary list above) - the first two because they push players to kill their own frogs.

---

## Full coverage table

### Core loop and progression - fully quested
Frogs, the six species (Cave/Geode/Bog/Tide/Infernal/Void), Resource Slimes, Slime Milk, Froglights, breeding/stats, and per-tier resources are the pack's spine and are covered end to end across the tier chapters.

### Appliances

| Feature | Quested? | Where |
|---|---|---|
| Spawnery | Yes | `welcome` |
| Slime Milker | Yes | milk chapters |
| Slime Churn | Yes | `sister_ponds` (JDT) |
| Crucible + Casting Mold | Yes | `melting_point` |
| Terrarium Controller / Sprinkler / Incubator / Hatch | Yes | `terrarium` |
| Sprinkler **redstone switch** (1.24.0) | No, by decision | Sprinkler quested; redstone control left to the guide (maintainer call) |
| **Virtual Terrarium** + Dome + upgrades (1.25.0) | **No** | - |
| **Slime Milk Basin** (1.25.0) | **No** | - |

### Frogs and items

| Feature | Quested? | Where |
|---|---|---|
| Frog Net | Yes | referenced in tier chapters |
| Froglight Cleaver | Yes | `trophy_pond` |
| Sweetslime | Yes | multiple |
| Lily Pad Perch (`sweetslimed_lily_pad`) | Yes | `bog_frogs` - "A Frog Perch" |
| Brewed Froglights + Curios slot | Yes | "Charmed, I'm Sure" |
| Princess's Kiss | Yes | `road_to_void` (dragon drop) |
| **Frog Legs / Soup** (raw/cooked/soup) | **No** | - |
| Tadpole Bucket | No, by decision | Maintainer call 2026-07-24 - do not quest |
| **Potion of Hopping** | **No** | - |

### Boss tier and endgame - fully quested

| Feature | Quested? | Where |
|---|---|---|
| Wither Skeleton Skull / Nether Star / Dragon Egg / Dragon Breath resources | Yes | `trophy_pond` |
| The four boss catalysts | Yes | `trophy_pond` |
| End Dragon Altar | Yes | `trophy_pond` - "The End Dragon Altar" |
| Wither Altar | Yes | `trophy_pond` - "The Wither Altar" |
| Master Frog / singularity compression | Yes | `master_pond`, kubejs |

> Note: this corrects the stale CLAUDE.md line that says the two altars are unquested with "10 new content item ids ... unquested." Both altars now have quests; the reinforced Froglights and receptacles are folded into them as build materials. Update that note when convenient.

### Bug fixes / behavior (no quest needed)
Underwater breathing (1.24.5), mud-bank laying (1.24.3), tadpole suffocation on maturity (1.24.4), Hatch shift-click dupe (1.24.7), dispenser milk-upgrade preservation (1.24.7), Sweetslime tadpole feeding (1.24.4). These are correctness/QoL and need no quest.

### Intentionally unquested (disabled in-pack)
Equivalence / Midas lane (1.23.0) - `equivalence.enabled` defaults off and the pack does not override it. Not craftable, correctly unquested.

---

## Reminder for whoever runs the 1.25.0 bump

The census generator's lang splice still silently drops the ~34 non-census quest keys on regen (memory `project_census_gen_lang_drops_keys`; re-confirmed 2026-07-24 on the 1.24.7 dry run: `en_us.snbt` went 844 -> 810 keys). On the real bump, after running `gen_completionist_chapters.py`, diff `en_us.snbt` key-set before/after and discard/repair the drop before committing. If 1.25.0 adds no new vanilla variant (Second Helpings is machines-only, so likely zero roster drift), the census lang change can be discarded wholesale like the 1.24.7 dry run.
