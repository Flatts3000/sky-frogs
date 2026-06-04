# GitHub Issues - Best Practices (Sky Frogs)

How this repo uses GitHub Issues. Tailored to a curated modpack whose bug reports
and mod suggestions arrive mostly from CurseForge comments, and which already keeps
a deep written knowledge base in [`known_issues.md`](./known_issues.md) and
[`backlog.md`](./backlog.md).

> **Platform note up front.** `Flatts3000/sky-frogs` is a **user-owned** repo. GitHub's
> native **issue types** and **sub-issues** are **organization-only** features (GA 2025,
> still org-scoped). They are not available here unless the repo moves into a (free)
> organization. Everything below is written to work on a user repo: **labels carry the
> type**, and **tasklists + linked issues** stand in for sub-issues.

---

## 1. What belongs in an issue (and what does not)

An issue is for **one concrete, actionable piece of work** the pack owns:

- A pack bug (config, quest, KubeJS, datapack/resourcepack override, mod interaction).
- A specific pack change (new quest, override tweak, balance fix).
- A mod-list decision (add / replace / a new Resource Slime variant).

Route everything else away from the tracker (the repo's `config.yml` already does this):

- **Usage questions / open design chatter** -> GitHub Discussions.
- **Bugs in frog mechanics, slime behavior, froglight components** -> the
  [productive-frogs](https://github.com/Flatts3000/productive-frogs/issues) repo. The
  pack only owns config/quests/scripts; mod behavior is upstream. File there and
  cross-link.
- **Security issues** -> private GitHub Security Advisory, never a public issue.
- **Vague "design question" with no decision yet** -> stays in `backlog.md` until it
  is concrete enough to act on. Do not open an issue just to think out loud.

**One issue = one problem.** If a CurseForge comment reports two bugs (as happened with
the steel-ingot quest and the Metallurgic Infuser), open **two** issues. Bundled issues
can never be cleanly closed, labeled, or linked to a single PR.

## 2. Before opening: search

Always `gh issue list --search "<keywords>" --state all` first. Duplicates fragment the
discussion and the fix. If it is a dup, comment with the canonical number and close as
`duplicate`.

## 3. Titles

- Specific and scannable. The title is what you read in a list of 50.
- Lead with the templates' tag so type is obvious at a glance: `[Bug]`, `[Feature]`,
  `[Mod Suggestion]` (the existing templates set these).
- Name the surface. Good: `[Bug] Steel quest requires mekanism:ingot_steel, uncraftable under AlmostUnified`.
  Bad: `[Bug] quest broken`.
- Describe the symptom, not your guessed cause (the cause often turns out different,
  as the infuser bug did).

## 4. Templates and forms

The repo already ships markdown templates (`bug_report.md`, `feature_request.md`,
`mod_suggestion.md`) and a good `config.yml` (blank issues off, contact links routing
to Discussions / upstream / security). Keep these.

**Recommended upgrade (optional):** migrate the three markdown templates to **Issue
Forms** (YAML in `.github/ISSUE_TEMPLATE/*.yml`). Forms let you mark fields **required**
(version, launcher, "is this actually a PF bug?") so reports arrive complete, and they
can auto-apply labels. Markdown templates cannot enforce fields. This matters most for
the bug form, where missing version/launcher/log is the usual back-and-forth.

## 5. Labels

Native issue types are unavailable on a user repo, so **labels do all the
classification**. Keep a small, orthogonal scheme - every issue gets at most one from
each family:

**Type** (mutually exclusive; the template applies one):
- `bug`, `enhancement`, `mod-suggestion`, `documentation`

**Tier** (which Productive Frogs category it touches; optional but high-signal here):
- `tier:cave`, `tier:geode`, `tier:bog`, `tier:tide`, `tier:infernal`, `tier:void`,
  `tier:bootstrap` (pre-Tier-1), `tier:cross-tier`

**Area** (what part of the pack):
- `area:quests`, `area:kubejs`, `area:config`, `area:worldgen`, `area:mod-list`,
  `area:recipes`, `area:tooling`

**Status / triage**:
- `needs-triage` (default on inbound), `confirmed`, `playtest` (fix written, awaiting
  in-game verification - mirrors the held-for-playtest workflow), `blocked-upstream`
  (waiting on a Productive Frogs change), `wontfix`, `duplicate`

**Source** (provenance, for prioritizing real player pain):
- `source:curseforge` (came from a CF comment), `source:playtest`, `source:internal`

**Priority** (optional, only when it matters):
- `priority:high`, `priority:low`

Gaps to close on day one: the `mod_suggestion.md` template references a `mod-suggestion`
label that **does not exist yet** - create it, plus the families above. Create labels via
`gh label create "<name>" --color <hex> --description "<text>"`.

## 6. Triage flow

1. Inbound issue lands with `needs-triage` (+ its type label from the template).
2. Reproduce or assess. Add `confirmed` (or close as `duplicate` / `wontfix` with a
   one-line reason - never close silently).
3. Apply `tier:*` and `area:*` so it is filterable.
4. If it needs a mod change, label `blocked-upstream`, open the PF issue, cross-link.
5. Assign a **milestone** (see section 8) once it is slated for a release.
6. Remove `needs-triage` once it has been triaged. An issue should never sit in two
   contradictory states.

## 7. Attribute CurseForge reporters

Player reports are the highest-value inbound. When you open an issue from a CF comment,
**credit the reporter by username** in the body ("Reported on CurseForge by `username`
on YYYY-MM-DD") and quote their words. It preserves provenance, lets you follow up, and
is just good manners to the people testing the pack for free.

## 8. Milestones = releases

Create a milestone per planned version (`v0.3.0`, `v0.4.0`) and attach issues you intend
to ship in it. This makes the milestone page a live changelog-in-progress and keeps
scope honest. When the tag ships, the closed issues in that milestone are exactly the
CHANGELOG `[x.y.z]` section - cross-check the two so they agree.

## 9. Link issues to PRs and commits

- In the PR body, use a **closing keyword**: `Fixes #12`, `Closes #13`. Merging the PR
  auto-closes the issue and stamps it with the commit. This is the single most important
  habit - it ties the "why" (issue) to the "what" (diff) permanently.
- One PR can close several issues (`Fixes #12, fixes #13`) when one change resolves
  multiple reports - but prefer a focused PR per issue when the fixes are independent.
- Reference without closing using a bare `#12` when a commit is related but not the full
  fix.
- For work held for playtest (this repo's norm): open the PR, link it, but leave the
  issue **open with `playtest`** until you confirm in-game, then close with a comment
  citing the verifying session.

## 10. Breaking down large work

Native sub-issues are org-only, so for an epic (e.g., "Tier 7" or "rebalance all Geode
recipes") use one of:

- A **tracking issue** with a markdown **tasklist** (`- [ ] #21`, `- [ ] #22`). GitHub
  renders linked issues in a tasklist with live open/closed state and a progress bar.
- A **`epic` / `tracking` label** on the parent plus `Part of #20` in each child's body.

Keep child issues independently closeable; the tracker just aggregates.

## 11. Relationship to the docs knowledge base

GitHub Issues and the `docs/` trackers are **not** redundant - they have different jobs.
Do not copy content between them; **link**.

| | GitHub Issues | `known_issues.md` | `backlog.md` |
|---|---|---|---|
| **Role** | Live inbound + triage + work tracking | Deep diagnosed-bug archive | Open design questions + decision log |
| **Best at** | Attribution, PR/commit linking, milestones, public visibility, status | Long root-cause writeups, "corrected misdiagnosis" trails, verification notes | Framing undecided questions, recording why a decision went the way it did |
| **Audience** | Players + maintainer | Maintainer / future-you | Maintainer / design |

Division of labor:

- A **player-reported bug** opens as an **issue** (attribution, milestone, PR link). If
  the diagnosis gets deep (multi-paragraph root cause, like the infuser NBT trap), the
  full writeup lives in `known_issues.md` and the issue links to it with one line. The
  issue tracks *state*; the doc holds *knowledge*.
- A **design question** stays in `backlog.md` until it is decided/actionable, then a
  concrete issue is opened for the implementation. The decision record stays in
  `backlog.md`'s changelog.
- When an issue closes, if it taught something durable, make sure the lesson is captured
  in the relevant doc (or `tools/validate_quests.py` as a new check) - the issue thread
  alone is too easy to lose.

## 12. Closing hygiene

- Close with a **comment**, never silently: link the PR/commit, name the release it
  ships in, or state why it is `wontfix`/`duplicate`.
- For `playtest` items, the closing comment should cite the in-game verification ("Confirmed
  in-game 2026-06-10, fresh world").
- Re-open rather than open-a-new-dup if a "fixed" bug recurs - the history is valuable.

## 13. Handy `gh` commands

```sh
gh issue list --state all --search "steel"          # search before filing
gh issue create --template bug_report.md            # use a template
gh issue create -t "[Bug] ..." -b "..." -l bug,tier:cave,source:curseforge
gh issue edit 12 --add-label confirmed --milestone v0.3.0
gh label create "tier:cave" --color 8B5A2B --description "Tier 1 - Cave"
gh issue comment 12 --body "Fixed in #15, ships in v0.3.0."
gh issue list --label playtest                      # what is awaiting verification
```

(Per the repo workflow, prefer the `gh` CLI for all of this; never the web UI when the
CLI can do it.)

---

## TL;DR

1. One issue, one problem. Search for dups first.
2. Labels carry type/tier/area/status/source (no native issue types on a user repo).
3. Attribute CurseForge reporters by name.
4. `Fixes #N` in the PR; hold open with `playtest` until verified in-game.
5. Milestones map 1:1 to releases and to the CHANGELOG.
6. Issues track *state*; `known_issues.md` / `backlog.md` hold *knowledge* - link, do not copy.
