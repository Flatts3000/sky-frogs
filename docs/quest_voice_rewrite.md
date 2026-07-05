# Quest Voice Rewrite

**Status:** Editorial pass **SHIPPED** - v1.4.2 (chapters 1-3) and v1.4.3 (all remaining), covering every P0-P3 chapter in section 5. Measured against the section 9 baseline it cut the loudest mechanical tells hard: dash-as-reveal **301 -> 47**, rhetorical-question openers **~12 -> 0**, and the wordy/long descriptions trimmed (the regenerated ranking in [`quest_rewrite_candidates.md`](./quest_rewrite_candidates.md) is now **0 HIGH / 21 MED**, down from 0 HIGH / 91 MED). What it did **not** do: reach the section-8 "near-zero dashes" definition of done (47 dash-reveals remain), rework the P4 generated census chapters, or settle whether players still read the copy as AI - that perception check is a playtest question and stays the user's call (see [`../CLAUDE.md`](../CLAUDE.md) and the memory note `feedback-quest-copy-reads-as-ai`). Treat the rest of this doc as the standing voice spec plus the residual worklist, not an unstarted project.

**Owner of the problem:** player feedback says the quest descriptions "look like AI." This doc specs the fix; the v1.4.2-v1.4.3 editorial pass is its first execution.

---

## 1. The problem

Players report that Sky Frogs quest descriptions read as obviously AI-written. The copy is not crude. It already went through one editorial pass (issue #169), which made it punchy and voicey. That polish, applied with the **same shape to every quest**, is what now reads as machine-written. Two parts:

- **Prose / voice** - a uniform rhythm and a small set of repeated rhetorical moves.
- **Accuracy** - some descriptions are subtly wrong or invented; confident-but-off is itself an AI signal and compounds the impression.

## 2. Diagnosis (measured, not guessed)

Counts taken from `pack/config/ftbquests/quests/lang/en_us.snbt` on 2026-06-29:

| Signal | Count | Why it reads as AI |
| --- | --- | --- |
| ` - ` dash-as-reveal | **301** across 245 described quests | Nearly every description leans on a spaced hyphen doing em-dash work ("turns it into raw ore - mine it and you're off"). Loudest single tell. Also violates the repo's hard anti-em/en-dash rule (these hyphens are em-dashes in disguise). |
| Punchy fragment subtitles | **245 / 245** | Every subtitle is a 3-5 word kicker ("Build it twice.", "Rock, on tap.", "Water from the sky."). Any one is good; 245 identical-shape fragments in a row is a cadence no human produces. |
| "Earnest setup -> snappy one-line button" body shape | pervasive | The internal rhythm of each description repeats the same arc. Uniformity is the fingerprint. |
| Rhetorical-question openers ("Tired of...? Done chasing...?") | ~12 | Smaller tell, but clustered. |

**Conclusion:** the fix is **not** "write it better." A regenerated batch would re-apply the same formula in new words. The fix is to **break the uniformity on purpose**, strip the dash habit, and put a human pass on every line.

## 3. Voice spec (the rules the rewrite is held to)

1. **Kill the dash-as-reveal.** Replace ` - ` with two short sentences, a comma, or a colon. Target: near-zero ` - ` constructions pack-wide (hard rule, also satisfies the global anti-dash rule).
2. **Vary structure deliberately.** Across any chapter, roughly: a third of quests get a kicker line, a third are plain instruction with no flourish, a third open mid-action. No quest repeats its neighbor's shape.
3. **Let some quests be boring.** A craft-this-block quest may simply say craft this block. Relentless wit reads as trying-too-hard AI.
4. **Retire the formula subtitles.** Not every quest needs a punchy fragment. Some subtitles can be plain, some omitted. Vary length and register.
5. **Drop the rhetorical-question openers** except where one genuinely earns its place (cap ~2-3 pack-wide).
6. **Ground-truth every mechanic** against the mod / recipes / PF datapack before writing. No invented behavior. (Accuracy is half the AI impression.) Cross-check the hidden recipe layers per `project_pf_ships_crossmod_recipes` memory.
7. **Stay inside existing voice law:** factual not technical, helpful not verbose, both new and expert players (`feedback-quest-voice-target`); player-facing names only, "Froglight" not "Configurable Froglight" (`feedback-froglight-naming`).
8. **One human pass, every line.** The reviewer reads each rewritten quest before it ships. This pass is what actually kills the residual tell.
9. **Use real in-game actions, not invented verbs.** The copy must name actions the game actually has. You don't "pour" anything in Minecraft: you **use** (right-click) a water bottle on dirt to make mud, and you **empty** a bucket to place a fluid or milk source. Describing a "pour" is an accuracy tell (confident copy for an action that doesn't exist) and, on a recipe-instruction quest, it actively misleads.
   - **Literal-action offenders to fix** (these describe real bucket/bottle actions): "A glass bottle of water **poured** onto a block of dirt" (Make Mud, the worst, it's a recipe step), "**Pour** it out and Lapis Slimes spawn", "**Pour** that milk out", "**Pour** it on water", "**Pour** the slime into a Slime Milker", "Run the loop: milk it, **pour out** the Slime Milk", "**Pipe (or pour)** a bucket of Slime Milk".
   - **Leave alone, deliberate metaphor** (not a literal game action): "Tier 0's groundwork is **poured**", subtitles "Iron you can **pour**" / "Dirt you can **pour**" / "**Pour** one out", "a Point **pours** it out", "water and lava, which **pour** rather than press".
   - Replacements: "empty the bucket onto…", "use a water bottle on a dirt block", "tip the milk out", "right-click to place the milk".

## 4. Scope

**In scope (hand-authored narrative chapters, 25):** the `quest_desc` and `quest_subtitle` strings in `lang/en_us.snbt` for the chapters listed in section 5. Titles are mostly fine; touch only the ones that themselves read as formula.

**Out of scope / handle separately:**
- **Generated census chapters** `sister_ponds` and `whole_pond` are emitted by `tools/gen_completionist_chapters.py`. Their prose is templated (4 description strings in the generator). Hand-editing the lang file for these gets **overwritten on the next regen** - if their text needs work, edit the generator template, not the lang file. Low priority: they are "collect X Froglight" census quests with minimal prose.
- **Structure** lives in `chapters/*.snbt`; this rewrite only touches text in `lang/en_us.snbt` (per `project_ftbquests_lang_format`).

## 5. Work breakdown (worst offenders first)

Priority is first-impression + traffic + formula density. Each chapter is one reviewable unit: rewrite -> human review -> calibrate.

### P0 - calibration sample (do first, prove the voice)
- [x] `welcome` - first thing every player reads
- [x] `cave_frogs` - Tier 1 species, first resource loop

> Historical workflow: P0 shipped first as the calibration sample, the user reviewed, and their edits recalibrated the spec before the P1-P3 chapters followed in v1.4.3. All are now shipped; the boxes above track that.

### P1 - early game, high traffic
- [x] `your_first_iron_ingot`
- [x] `storage_and_crafting` (kicker-formula heavy)
- [x] `tools_and_things` (kicker-formula heavy)
- [x] `scaling_the_colony`
- [x] `road_to_geode`
- [x] `geode_frogs`

### P2 - mid game
- [x] `powered_up`
- [x] `mekanism`
- [x] `melting_point`
- [x] `road_to_bog`
- [x] `bog_frogs`
- [x] `road_to_tide`
- [x] `drowned_riches`
- [x] `take_flight`

### P3 - late game / endgame
- [x] `road_to_infernal`
- [x] `infernal_frogs`
- [x] `the_network`
- [x] `terrarium`
- [x] `road_to_void`
- [x] `void_frogs`
- [x] `the_ultimate_table`
- [x] `master_pond`
- [x] `trophy_pond`

### P4 - generated (edit the generator, not the lang)
- [~] `sister_ponds` - templated in the generator; via `gen_completionist_chapters.py` template
- [~] `whole_pond` - templated in the generator; via `gen_completionist_chapters.py` template

## 6. Workflow

1. Branch: `feat/quest-voice-rewrite` (or per-priority-tier branches). Hold on the branch; do **not** merge to `main` until the user playtests/reads and says go (`feedback-hold-quest-merges`).
2. Rewrite one chapter's `quest_desc`/`quest_subtitle` strings in `lang/en_us.snbt` to the section 3 spec.
3. Run validation (section 7).
4. User reviews that chapter. Capture their edits as deltas to the spec.
5. Repeat per chapter, in P0 -> P4 order.

## 7. Validation (run after every chapter)

- `python tools/validate_quests.py` - must exit clean (catches em-dash, recipe drift, dangling deps, bad ids).
- Dash-count regression check: ` - ` occurrences in the rewritten chapter trend toward zero; pack-wide count falls well below the 301 baseline.
- `python tools/pack_refresh.py` before committing, stage `index.toml`/`pack.toml` in the same commit (`feedback-pack-refresh-before-commit`).
- In-game smoke after a `/reload`: `/sf_selftest` (op level 2).

## 8. Definition of done

- All P0-P3 chapters rewritten to the spec and human-reviewed.
- Pack-wide ` - ` dash-as-reveal count near zero in rewritten chapters.
- Subtitle shapes visibly varied (not 245 uniform fragments).
- `validate_quests.py` clean; no accuracy regressions found in review.
- Generated chapters (P4) addressed at the generator if their text needs it.
- Branch merged only after user sign-off.

## 9. Metrics (pre-rewrite vs current)

Regenerate the current column with `python tools/score_quest_voice.py --check` and a `grep` on the lang file.

| Signal | 2026-06-29 (pre-rewrite) | 2026-07-05 (post v1.4.3) |
| --- | --- | --- |
| Quest titles | 339 | 383 |
| Quests with descriptions | 245 | 249 |
| Subtitles | 245 (all fragment-formula) | 249 (still mostly short kickers) |
| ` - ` dash-as-reveal occurrences | 301 | **47** |
| Rhetorical-question openers | ~12 | **0** |
| Candidate score distribution | 0 HIGH / 91 MED / 153 LOW / 3 CLEAN | 0 HIGH / 21 MED / 214 LOW / 14 CLEAN |

The dash-as-reveal count fell ~85% but is not yet near-zero (section 8), and subtitles are still predominantly short fragments (spec rule 4 only partly applied). Those two are the bulk of the residual worklist in `quest_rewrite_candidates.md`.

## Appendix A - Verb accuracy audit (the "pour" sweep)

Full pack-wide pass for verbs that name actions Minecraft does not have (rule 9). Generated 2026-06-29. **Line numbers are pre-PR-#201** and have since shifted, re-grep `pour` in `lang/en_us.snbt` before sweeping. The Make Mud case (was line 184) is **already fixed** in #201; the rest remain.

### ERROR (fix - verb names a non-existent action; "place/empty the bucket", not "pour")

| Quest | Phrase | Fix |
|---|---|---|
| The Slime Churn | "pouring out Slime Milk" | "placing Slime Milk" |
| ~~Make Mud~~ | ~~"poured onto a block of dirt"~~ | **DONE in #201** ("use ... on a block of dirt") |
| Lapis milk | "Pour it out and Lapis Slimes spawn" | "Place the milk and ..." |
| Milk It (Iron) | "Pour that milk out" | "Place that milk" |
| Amethyst | "pour out the Amethyst Slime Milk" | "place the Amethyst Slime Milk" |
| Dirt milk | "Pour it out and Dirt Slimes" | "Place the milk and ..." |
| Tide eggs | "Pour it on water" | "Tip it onto water" (matches the other tiers) |
| Copper | "pour out the Copper Slime Milk" | "place the Copper Slime Milk" |
| Prime the Sprinklers | "Pipe (or pour) a bucket" | "Pipe (or empty) a bucket" |
| Milk It (Netherrack) | "Pour the slime into a Slime Milker" | "Drop the bucketed slime into the Milker's top slot" |

### WATCH (maintainer confirm before touching)

- **Casting Mold** "pour with a bucket" - if it's just bucket-emptying, fix; if PF surfaces a real cast/pour, keep.
- **Powah** "Orb"/"Orbed" verb (Energizing Orb) - real machine action, likely fine; confirm it reads clearly.
- **Botany Pot** "Plant it" - pot-insert vs world-place; likely fine.

### METAPHOR (do NOT touch - deliberate wordplay)

"groundwork is poured"; subtitle "Pour one out"; "water and lava, which pour rather than press"; Fluid Placer "pours"/"Pour fluids"; Fluid Collector "slurps"/"Scoop"; Flux Point "pours it out"; "Iron you can pour"; "Dirt you can pour"; "pouring off a frog"; "scoop from the middle"; Milker "squeezes"/"presses"; "vacuums up".
