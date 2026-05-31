# Quest Testing & Validation Strategy

> **Status:** IMPLEMENTED (2026-05-30). A two-layer safety net for the FTB Quests content
> so the authoring bugs this pack keeps hitting are caught mechanically instead of
> one-at-a-time through in-game play. Built: `tools/validate_quests.py` (Layer 1, all
> structural/match-components/lang/recipe-drift checks), `.github/workflows/validate-quests.yml`
> (CI gate), `.githooks/pre-commit` (commit gate), and `pack/kubejs/server_scripts/selftest.js`
> (`/sf_selftest`, Layer 2 runtime canaries). The only dormant piece is `Q-ITEM-EXISTS`, which
> stays a no-op (reported "not run") until `tools/data/item_ids.txt` is generated from a
> `/kubejs export` dump - see that check below.

## Why this exists

Quest bugs in this pack fall into two distinct classes, and they need different tools:

1. **Authoring / data bugs** - the quest SNBT or lang is structurally wrong or violates a
   known FTB/pack rule. Examples hit so far:
   - Item tasks that specify a discriminating `components` filter but omit `match_components`,
     so FTB matches by item id only and **one Copper Froglight completes every Cave quest**
     (and a Cave frogspawn completes Road to Geode). 32 tasks across 9 chapters had this.
   - Negative-leading quest IDs (hex `8-F`) parse as negative longs, get regenerated on load,
     and **drop every dependency that referenced them** (the severed Welcome branch).
   - Two quests that check the same variant (copy-paste), or a task whose lang title was
     written inline and silently wiped.
   These are **decidable from the files alone**. A static validator catches them with
   certainty, catches *every* instance in one pass, and prevents regressions forever.

2. **Runtime / mod-behavior bugs** - the data is well-formed but the *mod* does something
   unexpected. Examples:
   - FTB Quests ignoring the component filter (the *behavior* behind class 1's symptom).
   - Slime Milk buckets returning an empty bucket as a craft remainder, **duplicating a
     bucket** every slime craft.
   These are **not decidable from quest files**. They require running the game (manual play)
   or an in-game harness that exercises the real mod code.

**A Python validator addresses class 1 only.** It would have flagged all 32 `match_components`
omissions in one run instead of surfacing them through play, and it permanently guards against
the next one - but it could not have discovered "FTB ignores components" or caught the bucket
dupe. Manual playtesting and the optional KubeJS harness (Layer 2) cover class 2.

## Scope & non-goals

| Layer | Catches | Does NOT catch |
|-------|---------|----------------|
| **L1: static validator** (`tools/validate_quests.py`) | structural integrity, rule-conformance, lang sync, quest/recipe drift | FTB runtime matching, item/block runtime behavior, balance, UX |
| **L2: KubeJS harness** (in-game) | canary runtime assertions (does a copper froglight satisfy only the copper task; is the dupe gone) | exhaustive coverage; anything not explicitly asserted |
| **Manual play** | UX, balance, pacing, emergent behavior | nothing automatable |

Neither layer replaces playtesting. L1 is the high-ROI piece and the rest of this spec is
mostly about it; L2 is a smaller complementary layer specced at the end.

---

## Layer 1 - Static quest validator

### Invocation & output

```
python tools/validate_quests.py [--strict] [--json]
```

- Scans `pack/config/ftbquests/quests/chapters/*.snbt`, `lang/en_us.snbt`, `chapter_groups.snbt`,
  and (for cross-checks) `pack/kubejs/server_scripts/*_slime_chain.js` + `dissolution_slime_recipes.js`.
- **Exit codes:** `0` clean, `1` at least one ERROR, `2` warnings only (treated as pass unless `--strict`).
- **Output:** one line per finding, `SEVERITY  CHECK-ID  chapter.snbt:line  message`, grouped by
  severity, then a summary count. `--json` emits machine-readable findings for CI annotations.

### Parsing approach

FTB SNBT is not standard JSON (unquoted keys, no commas between object members, `0.0d` floats).
v1 uses **regex/line-based extraction** keyed to FTB's machine-generated, consistently-indented
format - the same lenient approach `tools/fix_quest_ids.py` already uses, so it stays robust to
the files FTB actually writes. A proper SNBT tokenizer is a future hardening (only needed if the
checks grow beyond field extraction). Each quest is reduced to a record: `{id, deps[], tasks[], rewards[], x, y, chapter}` where each task is `{id, type, item_id, components, match_components}`.

### Check catalog

Each check encodes a lesson from a real bug. Severity: **ERROR** blocks (would ship a broken
quest), **WARN** is a smell worth a human look.

#### Structural integrity

| ID | Sev | Rule | Encodes |
|----|-----|------|---------|
| **Q-ID-POSITIVE** | ERROR | every quest/task/reward `id` leads with hex `0-7` (parses as a positive long) | the severed Welcome branch; overlaps `fix_quest_ids.py` but as a gate, not a fixer |
| **Q-ID-UNIQUE** | ERROR | all ids globally unique across every chapter (FTB regenerates on collision, breaking deps) | latent collision risk |
| **Q-DEP-RESOLVES** | ERROR | every `dependencies` entry resolves to a real quest id in the loaded set | dangling deps / orphaned branches |
| **Q-DEP-ACYCLIC** | ERROR | no quest depends on itself; no dependency cycle | progression deadlock |
| **Q-CHAPTER-GROUP** | WARN | every chapter's `group` is a real id in `chapter_groups.snbt` (or intentionally ungrouped, like Welcome) | sidebar-grouping drift |

#### Component-matching correctness (the tier-skip class)

| ID | Sev | Rule | Encodes |
|----|-----|------|---------|
| **Q-MATCH-COMPONENTS** | ERROR | any item task whose `item` carries a `components` filter MUST set `match_components` (`strict` or `fuzzy`) | **the tier-skip exploit** - the single highest-value check |
| **Q-NO-DUP-TASK** | ERROR | within a chapter, no two quests share an identical `(item_id, components)` task. If two quests check the same item with the same (or no) discriminator, one completing auto-completes the other | copy-paste where two quests check the same variant |
| **Q-VARIANT-DISTINCT** | WARN | in a known resource-chain chapter (cave/geode/bog/tide_frogs), each resource quest checks a *distinct* `slime_variant` / `Variant` (no two quests target copper) | silent copy-paste of the variant id |

#### Lang sync

| ID | Sev | Rule | Encodes |
|----|-----|------|---------|
| **Q-LANG-TITLE** | ERROR | every quest has a `quest.<id>.title` in `lang/en_us.snbt` (FTB wipes inline titles; missing = blank quest) | inline-text-gets-wiped rule |
| **Q-LANG-ORPHAN** | WARN | every `quest.<id>.{title,quest_desc}` in lang maps to a real quest id | dead lang entries from deleted/renumbered quests |
| **Q-NO-DASHES** | ERROR | no em-dash (U+2014) or en-dash (U+2013) in any authored lang value | house rule (ASCII punctuation only) |

#### Reward tables (the loot-crate class)

| ID | Sev | Rule | Encodes |
|----|-----|------|---------|
| **Q-REWARD-TABLE-RESOLVES** | ERROR | every `loot`/`random`/`choice` reward carries a `table_id` that resolves to a real `reward_tables/<hexid>.snbt` (the decimal long == `int(hexid, 16)`) | a typo'd/empty `table_id` ships a reward that grants nothing (the Good Food Loot Crate feature) |
| **Q-REWARD-TABLE-ORPHAN** | WARN | every reward table is referenced by at least one quest | a dead table left after a quest was renumbered/removed |

Reward-table ids and their entry ids share the same 64-bit id space as quests, so they also flow
through `Q-ID-POSITIVE` / `Q-ID-UNIQUE`, and their granted items through `Q-ITEM-EXISTS`.

#### Item & recipe cross-checks (needs an item allowlist - Phase 2)

| ID | Sev | Rule | Encodes |
|----|-----|------|---------|
| **Q-ITEM-EXISTS** | ERROR | every item id referenced in a task/reward exists in the pack's registry | the "Missing Item" version-gap bugs (sweetslime pinned too low, etc.) |
| **Q-VARIANT-MADE** | WARN | for each resource quest, the `slime_variant` / `Variant` it checks is actually produced by a shipped recipe (a `*_slime_chain.js` step or a `SLIME_TIERS` row in `dissolution_slime_recipes.js`) | quest-vs-recipe drift (a quest for a variant no recipe makes) |
| **Q-FROGLIGHT-IS-CHECK** | WARN | per-tier *resource* quests check the variant Froglight (`configurable_froglight` + `slime_variant`), not the smelted resource, per the froglight-check principle (documented exceptions: Your First Iron Ingot, the main Mekanism Steel quest) | the no-bypass design law |

`Q-ITEM-EXISTS` needs the set of valid item ids. Source it from a one-time registry dump
(`/kubejs export` writes `kubejs/exported/item_registry.json` in the dev instance) committed as
`tools/data/item_ids.txt`, refreshed when the mod list changes. Without it, `Q-ITEM-EXISTS` is
skipped (reported as "not run") rather than guessed.

### Extension protocol (the ratchet)

Every new gotcha becomes a check. When a quest bug is found and fixed:
1. Add a row to the catalog above with the bug it encodes.
2. Implement the check; confirm it FAILS on the bug pre-fix and PASSES post-fix.
3. The bug can now never silently return.

This is the entire point: in-game testing *discovers* a class of bug once; the validator makes
it impossible to reintroduce across the remaining tiers (Tide finish, Infernal, Void).

### Integration

- **Pre-commit hook** (`.git/hooks/pre-commit` or a `pre-commit` config): run on staged `.snbt`/lang
  changes; block the commit on ERROR. Keeps bad data out of history.
- **CI gate** in the future `release.yml`: `python tools/validate_quests.py --strict` before the
  CF export step; a release never ships a tier-skip exploit.
- **Manual:** run anytime; pairs with `tools/fix_quest_ids.py` (fix IDs, then validate the rest).

---

## Layer 2 - KubeJS in-game runtime harness (optional)

For the class a Python script *cannot* reach: does the mod actually behave?

- A server command, e.g. `/sf_selftest`, registered in `pack/kubejs/server_scripts/selftest.js`,
  runs a fixed list of **canary assertions** and prints `PASS/FAIL` counts to chat + log.
- Representative assertions (not exhaustive - one per invariant):
  - Construct `configurable_froglight[slime_variant=copper]`; assert it satisfies the Cave *copper*
    task and **not** the gold task. (Directly tests the `match_components` fix at runtime.)
  - Construct each tier's first slime bucket; assert its chamber recipe resolves.
  - Simulate the milk-bucket craft; assert the result is exactly one slime bucket with **no** empty
    bucket remainder. (Tests the dupe fix.)
- **Scope:** a canary per known invariant, run on demand after a `/reload`. It is a smoke test,
  not coverage. It runs only in-game, so it is not a CI gate - it is a faster, repeatable
  substitute for hand-clicking through the questbook to confirm a runtime fix held.

L2 is worth building only if runtime regressions (FTB version bumps, PF behavior changes) become
frequent. Until then, the canaries can live as a documented manual checklist instead of code.

---

## Build plan (phased, by ROI)

| Phase | Deliverable | Catches | Status |
|-------|-------------|---------|--------|
| **1** | `validate_quests.py` with structural + match-components + lang checks (Q-ID-*, Q-DEP-*, Q-MATCH-COMPONENTS, Q-NO-DUP-TASK, Q-LANG-*, Q-NO-DASHES) | today's tier-skip + dependency + lang bugs, all instances, forever | **DONE** |
| **2** | cross-checks (Q-VARIANT-MADE DONE; Q-ITEM-EXISTS dormant pending `tools/data/item_ids.txt`; Q-FROGLIGHT-IS-CHECK deferred - too heuristic to define without false positives) | "Missing Item" gaps, quest/recipe drift | **PARTIAL** |
| **3** | `.github/workflows/validate-quests.yml` CI gate + `.githooks/pre-commit` (enable: `git config core.hooksPath .githooks`) | regression prevention at commit + PR/push | **DONE** |
| **4** | KubeJS `/sf_selftest` canaries | runtime confirmation of fixes after `/reload` | **DONE** (the craft-remainder canary reads `ItemStack.getCraftingRemainingItem()` - the NeoForge 1.21 name; `getCraftingRemainder` does not exist) |

The validator is self-verifying: it runs clean on the current pack, and injecting a missing
`match_components` or a dangling dependency makes it exit non-zero with the exact finding. To
finish `Q-ITEM-EXISTS`, run `/kubejs export` in the dev instance and write the item ids
(one per line) to `tools/data/item_ids.txt`.
