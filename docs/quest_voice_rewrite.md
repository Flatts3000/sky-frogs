# Quest Voice Rewrite

**Status:** Spec / not started. Implementation is held until the user gives the go (see [`../CLAUDE.md`](../CLAUDE.md) and the memory note `feedback-quest-copy-reads-as-ai`).

**Owner of the problem:** player feedback says the quest descriptions "look like AI." This doc specs the fix.

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
- [ ] `welcome` - first thing every player reads
- [ ] `cave_frogs` - Tier 1 species, first resource loop

> After P0, the user reviews and edits. Their edits recalibrate the spec before any P1 work begins.

### P1 - early game, high traffic
- [ ] `your_first_iron_ingot`
- [ ] `storage_and_crafting` (kicker-formula heavy)
- [ ] `tools_and_things` (kicker-formula heavy)
- [ ] `scaling_the_colony`
- [ ] `road_to_geode`
- [ ] `geode_frogs`

### P2 - mid game
- [ ] `powered_up`
- [ ] `mekanism`
- [ ] `melting_point`
- [ ] `road_to_bog`
- [ ] `bog_frogs`
- [ ] `road_to_tide`
- [ ] `drowned_riches`
- [ ] `take_flight`

### P3 - late game / endgame
- [ ] `road_to_infernal`
- [ ] `infernal_frogs`
- [ ] `the_network`
- [ ] `terrarium`
- [ ] `road_to_void`
- [ ] `void_frogs`
- [ ] `the_ultimate_table`
- [ ] `master_pond`
- [ ] `trophy_pond`

### P4 - generated (edit the generator, not the lang)
- [ ] `sister_ponds` - via `gen_completionist_chapters.py` template
- [ ] `whole_pond` - via `gen_completionist_chapters.py` template

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

## 9. Baseline metrics (2026-06-29, pre-rewrite)

- Quest titles: 339
- Quests with descriptions: 245
- Subtitles: 245 (all fragment-formula)
- ` - ` dash-as-reveal occurrences: 301
- Rhetorical-question openers: ~12
