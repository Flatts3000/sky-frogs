<!--
  Thanks for contributing! Please fill out the sections below. Brevity is fine —
  the goal is to give the reviewer the context they need to evaluate the change.
-->

## Summary

<!-- 1-3 sentences. What does this PR do and why? -->

## Type of Change

<!-- Check all that apply -->

- [ ] `feat` — new pack content (quests, variants, configs, scripts)
- [ ] `fix` — bug fix (broken quest, mis-tagged item, wrong recipe)
- [ ] `refactor` — restructuring with no player-visible change
- [ ] `docs` — documentation only
- [ ] `chore` — tooling, build, or infrastructure
- [ ] `ci` — CI/CD changes
- [ ] `perf` — load-time or runtime performance

## Scope Check

<!-- Sky Frogs ships pack-side content only. Confirm this change doesn't require Java. -->

- [ ] This change is pack-side only (KubeJS, configs, datapack JSON, quests, docs)
- [ ] If a Java change is implied, a corresponding issue exists on [productive-frogs](https://github.com/Flatts3000/productive-frogs/issues) — link it below

## Design / Docs Impact

<!-- Does this change require updates to any /docs/*.md files? List them. -->
<!-- If this resolves an open question in docs/backlog.md, mark it processed there. -->

- [ ] No design or docs changes needed
- [ ] Docs updated in this PR (list files below)
- [ ] A DRAFT banner was dropped from `/docs/*.md` because this PR settled the question
- [ ] Working assumption in `CLAUDE.md` promoted out of "NOT yet canonical"

## Testing

<!-- How did you verify the change in-game? Type-checks aren't enough for a pack. -->

- [ ] Loaded the pack in a fresh world and verified the change
- [ ] Verified affected quest chapter loads and is satisfiable
- [ ] Checked `latest.log` for new errors / warnings
- [ ] N/A — docs-only

## Checklist

- [ ] `packwiz refresh` runs cleanly inside `pack/` (skip if pre-packwiz scaffold work)
- [ ] Commits follow [Conventional Commits](https://www.conventionalcommits.org/)
- [ ] New mods (if any) are justified per [`docs/mod_list.md`](../docs/mod_list.md) selection criteria
- [ ] New Resource Slime variant JSONs use `neoforge:conditions → mod_loaded`
- [ ] `CHANGELOG.md` updated under the relevant section (once it exists)

## Notes for Reviewer

<!-- Anything reviewers should pay extra attention to? Known limitations?
     Screenshots of new quests / textures / panoramas welcome. -->
