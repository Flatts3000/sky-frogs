# Quest System Audit - 2026-05-31

Holistic review of the FTB Quests questbook, benchmarked against the full FTB Quests
capability set ([`../ftbquests_reference.md`](../ftbquests_reference.md)) and AAA packs
(All the Mods, Sky Bees Reborn, Vault Hunters, Enigmatica). Sources: a hard inventory of
all 14 chapters, three parallel deep-dives (rewards / content+UX / capability+polish), and
the FTB jar's type registry.

---

## Verdict

The questbook is **mechanically excellent and structurally clean** (the validator is green;
voice is sharp; onboarding and the gateway/verb chapters are genuinely strong) but **uses a
narrow slice of FTB Quests and leans on repetitive rewards**. It reads today as a *very good,
competent* questbook, not yet a *AAA, world-class* one. The gap is not correctness - it's
**variety, reward dopamine, and presentation**. Closing it is almost entirely **additive**
(no rewrites), and the highest-leverage 20% gets ~80% of the "AAA feel."

**One-line summary:** we built a correct skeleton; AAA is the muscle and skin - reward
excitement, task variety, reveal/choice pacing, and visual polish.

---

## Capability scorecard (what we use vs what FTB offers)

| Dimension | We use | FTB offers | Utilization |
|---|---|---|---|
| **Task types** | `item`, `checkmark` | item, checkmark, observation, advancement, dimension, biome, kill, stat, location, fluid, energy, xp, stage, structure, custom | **2 of ~16** |
| **Reward types** | `item`, `xp` | item, xp, xp_levels, loot, random, choice, all_table, command, currency, advancement, stage, toast, custom | **2 of ~13** |
| **Reward tables / loot crates** | none (`reward_tables/` empty) | weighted random + guaranteed rolls, physical crates | **unused** |
| **Quest shapes** | `hexagon` (29 milestones), `diamond` (1) | circle, square, hexagon, diamond, octagon, pentagon, gear, heart | **2 of 8 (hierarchy only for milestones)** |
| **Subtitles** | none | `quest_subtitle` per quest | **unused** |
| **Chapter images** | none (banners/art) | decorative + interactive canvas overlays | **unused** |
| **Visibility control** | none | `hide_until_deps_complete/visible`, `hide_dependency_lines` | **unused** |
| **Dependency choice** | `all_completed` only | `one_completed`, `*_started`, `min_required_dependencies` | **unused** |
| **`optional`** | 3 quests | per-quest optional side content | **barely used** |
| **`quest_links`** | empty arrays everywhere | cross-chapter ghost copies | **unused** |

Used well: `match_components` (strict/fuzzy, validator-enforced), positive IDs, autofocus,
hexagon milestones, cross-chapter dependency gating, lang extraction, the pack voice.

---

## What's already AAA-grade (keep, don't touch)

- **The Welcome onboarding.** 22 quests, multiple parallel branches (water / bed / cobble /
  frog-eggs) converging on the Spawnery. This rivals Sky Bees Reborn.
- **The voice.** "Frogs, Not Pickaxes", "you out-frogged the game" - dry, warm, premise-selling.
  Matches `voice_and_tone.md` consistently. The color convention (`&e` machines, `&b` goals,
  `&f` materials) is solid.
- **The gateway + verb chapters.** `your_first_iron_ingot`, `road_to_tide` (two converging
  paths), `take_flight` (vertical coil tiers), `tools_and_things` (spine + optional BG branch)
  are well-paced and varied.
- **Structural integrity.** Clean ID scheme, no dangling deps, no cycles, lang in sync - all
  enforced by `tools/validate_quests.py`. This is the foundation everything else builds on.

---

## Gaps & analysis

### A. Rewards are flat and repetitive (the headline gap)

Every reward is `item` or `xp`. The single most common reward is a **storage drawer**
(`functionalstorage:oak_1` + `compacting_drawer` ~29 times), and three species chapters
(cave/geode/bog_frogs) reward a drawer on **every** spine quest. Food (from
`gen/good_food_map.md`) is the only humanizing variation, used on ~9% of quests. There is:

- **No reward-value scaling by tier.** A Tier-4 capstone (the Dissolution Chamber - the
  pack's slime engine, the gate to all future tiers) rewards the same ~25 XP as a mid-tier
  routine quest. Capstones are *marked* (hexagon) but not *rewarded* distinctly.
- **No randomness or excitement.** Zero reward tables / loot crates. The player always knows
  exactly what they're getting - a drawer.
- **No player agency.** Zero `choice` rewards. The player never decides.
- **No celebration.** Zero `toast` / `stage` rewards. Tier unlocks are gated but not marked
  with any fanfare.

This is the biggest single lever on "feel." AAA packs make rewards *vary, scale, surprise,
and celebrate*.

### B. Task monotony - everything is "obtain item" or "click checkmark"

198 item tasks, 15 checkmarks, **zero** observation / location / stat / dimension / advancement.
The species chains (cave/geode/bog/drowned) are 6-10 quests of identical structure: submit the
next variant's Froglight. The player never *watches* the Dissolution Chamber cook, *sees* a
slime spawn in the dark room, or *flies* (the jetpack "Fuel and Fly" quest is a self-reported
checkmark). FTB's `observation` task ("look at X for N ticks") is tailor-made for "see the
machine work" beats and is completely unused.

### C. Species-chain monotony (the structural weak point)

`cave_frogs`, `geode_frogs`, `bog_frogs`, `drowned_riches` are single-column linear chains
where the whole 6-10 step grid is visible from the start - the player sees "6 identical quests"
up front. This is forced by Productive Frogs' recipe chain (each variant needs the prior's
milk), but the *questbook* doesn't have to *present* it as a flat list. Contrast the engaging
chapters (Welcome, your_first_iron_ingot, road_to_tide) which branch and converge.

### D. Presentation is utilitarian

The canvas is nodes + dependency lines. No chapter banners/art, no shape hierarchy beyond
hexagon-for-milestone, no subtitles, no within-chapter section markers, `show_lock_icons:
false`. It reads as "a spec of the frog progression" rather than "a world to explore." Top
packs use shape families, banners, and subtitles so the canvas is legible and themed at a glance.

### E. No reveal/choice pacing

`hide_until_deps_complete` (reveal one step at a time = discovery), `optional` side content,
and `dependency_requirement: one_completed` (player-choice branches) are all unused. The book
is a single visible rail.

---

## Prioritized roadmap

Ordered by leverage-per-hour. P0/P1 deliver most of the AAA jump; P2/P3 are deepening.
**All additive.** Each item names the FTB feature to use.

### P0 - Quick wins (high leverage, low effort, low risk)

1. **`hide_until_deps_complete: true` on species-chain steps** (one line per non-first quest in
   cave/geode/bog/drowned_riches). Turns "6 quests in a grid" into one-at-a-time discovery.
   ~20 lines, ~1 hr. Biggest UX-per-byte change in the pack.
2. **Capstone reward escalation + celebration.** Bump tier-gateway and chapter-capstone XP onto
   a real curve (e.g. Tier 1 caps ~40, Tier 4 gateway ~75) and add a `toast` reward
   (`title` + `description`) to each tier transition. Add a `stage` reward at tier gateways so
   later content can gate/branch on it. ~14 capstones, ~2 hrs. **Verify `toast`/`stage` reward
   types work in our build first** (build one in the editor, read the snbt).
3. **Subtitles.** Add `quest.<id>.quest_subtitle` one-liner hooks to resource and milestone
   quests ("Copper / the first new metal"). Pure lang-file work, big readability gain. ~2 hrs.
4. **Global settings polish.** `data.snbt`: `show_lock_icons: true` + a `lock_message`. 5 min.

### P1 - The reward overhaul (high leverage, medium effort)

5. **Reward tables / loot crates for the resource grind.** Create 4 tier-themed tables in
   `reward_tables/` (Froglight crates: weighted drawer / food / bonus resource / XP, 2 rolls
   each), and switch the ~40 species-chain `item` rewards to `type: "loot", table_id: ...`.
   Kills the 29-drawer monotony AND adds the "what did I get?" hit. ~6 hrs. This is the single
   highest-impact reward change. **New file type for us - validate `table_id` references resolve
   (extend the validator, see Risks).**
6. **Diversify the filler rewards.** Where a drawer repeats, swap ~half for tier-appropriate
   items (hoppers/cauldrons at Cave, Mekanism upgrades at Geode, JDT/IF parts at Bog, jetpack
   prep at Tide) so the *items you collect* show progression. ~2 hrs.
7. **A handful of `observation` tasks at marquee beats** - watch a Cave Slime spawn (Welcome
   dark room), watch the Dissolution Chamber run (road_to_tide capstone), watch an Item
   Collector vacuum (tools_and_things). 5-8 tasks, immersion per beat. ~2 hrs. **Verify the
   `observation` task's exact field names in the editor first.**

### P2 - Presentation pass (the visual AAA lift)

8. **Shape hierarchy.** Give quest *types* distinct shapes (hexagon = milestone, square =
   resource check, diamond = optional, default circle = step) so the canvas is legible at a
   glance. ~2 hrs of tagging.
9. **Chapter banners** via the `images[]` field - one tier-themed banner per chapter group
   (4 images, reused across each tier's chapters). Requires sourcing/designing 4 images.
   This is the difference between "spreadsheet" and "curated book." ~half a day incl. art.
10. **Within-chapter section markers** for the long chapters (Scaling, Mekanism) - invisible or
    `gear`-shaped lore nodes that label sections.

### P3 - Depth (do if the pack wants it; higher effort/risk)

11. **`choice` rewards** on variant branches (pick storage vs food vs XP) - real agency, but
    test the SNBT shape (it nests reward objects in `table_data`).
12. **Optional side-quests** in species chapters (catalyst-mastery, "the whole swamp"
    collection challenges) - reward scaling the operation, break the linear rail.
13. **`dependency_requirement: one_completed`** for player-choice resource branches - high
    agency, but it changes the progression model; prototype on one chapter first.
14. **`stat`/`location` tasks** for measured milestones (jetpack flight distance, be-above-Y) -
    some need a KubeJS `custom` task for custom stats.

---

## Risks and how to de-risk

- **New reward/task types may not serialize as expected.** `loot`/`choice`/`toast`/`stage`
  rewards and `observation` tasks are unused here. For each, **build one in the in-game editor,
  read the resulting snbt, and copy that exact shape** before hand-authoring at scale (the
  reference doc flags exact field names as version-sensitive). This is the same discipline that
  caught the `getCraftingRemainder` vs `getCraftingRemainingItem` and the jetpack-component issues.
- **Extend the validator alongside new features (the ratchet).** When we add reward tables, add
  a `Q-REWARD-TABLE-RESOLVES` check (every `table_id` points at a real `reward_tables/` id). When
  we add `choice`/`loot`, ensure the validator parses nested reward objects. When we add
  `observation`/`stage` tasks, confirm `Q-MATCH-COMPONENTS` and the task-type assumptions still
  hold. Each new capability becomes a new guard - same model as `docs/quest_testing.md`.
- **Don't adopt everything at once.** Pick P0 + P1 (rewards), ship and playtest, then decide on
  P2/P3. Over-decorating an unproven layout wastes the art.

---

## Open correctness items (carried from playtesting)

- **Bucket-dupe fix** - `/sf_selftest` now uses the real `getCraftingRemainingItem()` API;
  needs one in-game run for the verdict (all-green = fixed).
- **Iron Jetpack** - confirm the "Off the Ground" task shows an Iron Jetpack (the
  `jetpack_id` component fix) and that a crafted one assembles from frog-attainable parts.
- **`Q-ITEM-EXISTS` is dormant** - generate `tools/data/item_ids.txt` from `/kubejs export` to
  switch on the "Missing Item" guard (would also protect the new reward-item ids).

---

## Definition of "AAA" (target state)

A player playing the finished book should:
1. **Be surprised and delighted by rewards** - loot rolls, the occasional choice, escalating
   value, and a celebratory toast/stage when a tier opens.
2. **Do varied things** - not just "obtain item" 200 times; they *watch* machines work, *fly*,
   *stand* somewhere, *see* the systems they built.
3. **Discover the path** - chains reveal a step at a time; optional side content rewards mastery.
4. **Read a themed, legible canvas** - shape families, banners, subtitles - not a spreadsheet.
5. Keep the strengths we already have: the voice, the onboarding, the tight tier gating, and the
   validator-enforced correctness.

We are at #5 fully, and partway into #1-#4. The roadmap above is the path to all five.
