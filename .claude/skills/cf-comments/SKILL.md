---
name: cf-comments
description: Read new CurseForge comments on the Sky Frogs (or another) project and triage them into GitHub issues. Use when checking player feedback on the CurseForge page, when the user says "read the CF comments" / "check CurseForge", or pastes CF comments and wants them handled.
---

# CurseForge comment triage

Pull player feedback from a CurseForge project's comment section and route it into the
repo's GitHub Issues workflow. CurseForge's official Studios API has no comments endpoint;
the fetch uses the website's undocumented `v1` JSON API (no auth), wrapped by
`tools/cf_comments.py`.

## 1. Fetch

```sh
python tools/cf_comments.py            # NEW comments since last run (Sky Frogs), marks them seen
python tools/cf_comments.py --all      # every comment on the page
python tools/cf_comments.py --peek     # show new but DON'T update the seen state
python tools/cf_comments.py --project productive-frogs   # or a numeric CF project id
python tools/cf_comments.py --all --json                 # raw structured output
```

Default mode prints only comments not seen on a prior run (state in the gitignored
`tools/data/cf_comments_seen_<projectId>.json`) and marks them seen, so repeat runs surface
only fresh feedback. Replies are shown threaded under their parent. If it ever returns
non-JSON / a 403 (the endpoint is undocumented and could change, or hit Cloudflare), fall
back to reading the logged-in comments page with the Playwright MCP.

**Discord relay:** `--discord-webhook <url>` (or env `DISCORD_CF_WEBHOOK`) also mirrors each
NEW comment as an embed into the community server's private `#cf-feedback` channel. The
webhook URL lives in the `sky-frogs-community` repo's Terraform state:
`terraform output -raw cf_feedback_webhook_url`. Relay fires only in default new-comments
mode - never with `--all`/`--json` (history) **or `--peek`** (peek skips the seen-state
update, so relaying there would re-mirror the same comments every run). The guarantee is
one Discord post per comment, ever; failures are warn-and-continue.

## 2. Triage each new comment

Classify and act per [`docs/github_issues_best_practices.md`](../../../docs/github_issues_best_practices.md):

- **Bug report** -> open a GitHub issue: `gh issue create` with `bug` + the right `tier:*` /
  `area:*` + `source:curseforge` labels. **Credit the reporter** ("Reported on CurseForge by
  `<displayName>`, <date>") and quote them. Add `confirmed` once reproduced.
- **Mod / feature suggestion** -> `mod-suggestion` or `enhancement` issue, `needs-triage`,
  attributed. (Pack-identity calls stay the user's decision.)
- **Balance feedback** (spawn rates, timings) -> `enhancement` + the relevant `tier:*`, or a
  backlog note if it's a judgement call rather than a defect.
- **Support question / user error** -> usually no issue; it's typically answered in-thread on
  CurseForge. Note it and move on.
- **Already tracked / duplicate** -> skip; mention the existing issue number.

## 3. Confirm before filing

Opening issues is outward-facing. Summarize the proposed issues (title + labels + which
comment) and **get the user's OK before running `gh issue create`** - never auto-file. After
filing, report the issue numbers and links.

## Notes

- Known project slugs are mapped in the script (`sky-frogs` = 1558075, `productive-frogs` =
  1552728); any numeric CF project id also works.
- The script is read-only against CurseForge (a GET); it never posts. Replying to commenters
  is done by the user on the CF site.
