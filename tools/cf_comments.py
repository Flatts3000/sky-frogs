#!/usr/bin/env python3
"""Read CurseForge project comments (Sky Frogs by default).

CurseForge's official Studios API (api.curseforge.com) has no comments endpoint, but the
website's own undocumented v1 API does and needs no auth:

    GET https://www.curseforge.com/api/v1/mods/<projectId>/comments?index=<n>

It returns {"data": [comment, ...], "pagination": {index, totalCount, pageSize}}. Each
comment has id, text (plain), body (html), author{displayName,username}, datePosted (epoch
ms), isPinned, status, and an optional nested `replies` array. Undocumented => could change;
if it 403s or stops returning JSON, fall back to driving the logged-in page with Playwright.

Default mode prints only comments not seen on a previous run (state in
tools/data/cf_comments_seen_<projectId>.json) and marks them seen, so it surfaces just new
feedback for triage into GitHub issues (see docs/github_issues_best_practices.md).

Usage:
    python tools/cf_comments.py                  # new Sky Frogs comments since last run
    python tools/cf_comments.py --all            # every comment
    python tools/cf_comments.py --peek            # show new but DON'T update state
    python tools/cf_comments.py --project productive-frogs
    python tools/cf_comments.py --project 1552728 --all --json

Discord relay: pass --discord-webhook <url> (or set DISCORD_CF_WEBHOOK) and each NEW
comment is also posted as an embed to the community server's #cf-feedback channel.
The webhook URL comes from the sky-frogs-community repo:
    terraform output -raw cf_feedback_webhook_url
Relay only fires in new-comments mode (not --all / --json) so it can't replay history.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
STATE_DIR = REPO / "tools" / "data"

# Known project slug -> CurseForge numeric id (the v1 API keys on the numeric id).
KNOWN_PROJECTS = {
    "sky-frogs": 1558075,
    "productive-frogs": 1552728,
}
DEFAULT_PROJECT = "sky-frogs"

# Numeric id -> public page (per-comment deep link is ?comment=<id>).
PROJECT_PAGES = {
    1558075: "https://www.curseforge.com/minecraft/modpacks/sky-frogs",
    1552728: "https://www.curseforge.com/minecraft/mc-mods/productive-frogs",
}
CF_ORANGE = 0xF16436

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
BASE = "https://www.curseforge.com/api/v1/mods/{pid}/comments?index={index}"


def resolve_project(arg: str) -> int:
    if arg.isdigit():
        return int(arg)
    if arg in KNOWN_PROJECTS:
        return KNOWN_PROJECTS[arg]
    raise SystemExit(
        f"Unknown project '{arg}'. Use a numeric CurseForge id, or one of: "
        f"{', '.join(sorted(KNOWN_PROJECTS))}."
    )


def fetch_page(pid: int, index: int) -> dict:
    req = urllib.request.Request(
        BASE.format(pid=pid, index=index),
        headers={"User-Agent": UA, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        if resp.status != 200:
            raise SystemExit(f"CurseForge returned HTTP {resp.status} for project {pid}.")
        return json.loads(resp.read().decode("utf-8"))


def fetch_all(pid: int) -> list[dict]:
    """Top-level comments across all pages (replies stay nested under each)."""
    out: list[dict] = []
    index, total = 0, None
    while True:
        page = fetch_page(pid, index)
        data = page.get("data") or []
        out.extend(data)
        pg = page.get("pagination") or {}
        total = pg.get("totalCount", len(out))
        size = pg.get("pageSize") or 20
        index += size
        if index >= total or not data:
            break
    return out


def flatten(comments: list[dict]) -> list[dict]:
    """Top-level comments + nested replies, each tagged with depth and parent."""
    rows: list[dict] = []

    def walk(c: dict, depth: int, parent: int | None):
        rows.append({**c, "_depth": depth, "_parent": parent})
        for r in c.get("replies") or []:
            walk(r, depth + 1, c.get("id"))

    for c in comments:
        walk(c, 0, None)
    return rows


def author_name(c: dict) -> str:
    a = c.get("author") or {}
    return a.get("displayName") or a.get("username") or "unknown"


def fmt_date(epoch_ms) -> str:
    try:
        return datetime.fromtimestamp(epoch_ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    except Exception:
        return str(epoch_ms)


def state_path(pid: int) -> Path:
    return STATE_DIR / f"cf_comments_seen_{pid}.json"


def load_seen(pid: int) -> set[int]:
    p = state_path(pid)
    if not p.exists():
        return set()
    try:
        return set(json.loads(p.read_text(encoding="utf-8")).get("seen_ids", []))
    except Exception:
        return set()


def save_seen(pid: int, ids: set[int]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_path(pid).write_text(
        json.dumps({"seen_ids": sorted(ids), "last_checked": datetime.now(timezone.utc).isoformat()}, indent=2),
        encoding="utf-8",
    )


def post_discord(webhook: str, pid: int, rows: list[dict]) -> None:
    """Mirror comments to the community server's #cf-feedback via webhook embeds.

    One POST per comment (typical volume is single digits; Discord's webhook
    rate limiter would 429 a flood, so a failure on one embed warns and moves on).
    """
    page = PROJECT_PAGES.get(pid)
    for r in rows:
        text = " ".join((r.get("text") or "").split())
        if len(text) > 1900:
            text = text[:1900] + " [...]"
        reply = f" (reply to #{r['_parent']})" if r.get("_parent") else ""
        embed = {
            "title": f"{author_name(r)} on comment page{reply}" if reply else f"New comment by {author_name(r)}",
            "description": text or "(no text)",
            "color": CF_ORANGE,
            "footer": {"text": f"project {pid} | comment #{r.get('id')}"},
        }
        ts = r.get("datePosted")
        if isinstance(ts, (int, float)):
            embed["timestamp"] = datetime.fromtimestamp(ts / 1000, tz=timezone.utc).isoformat()
        if page:
            embed["url"] = f"{page}?comment={r.get('id')}"
        payload = json.dumps({"username": "CurseForge Comments", "embeds": [embed]}).encode("utf-8")
        req = urllib.request.Request(
            webhook, data=payload, headers={"Content-Type": "application/json", "User-Agent": UA}
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status not in (200, 204):
                    print(f"  [discord] HTTP {resp.status} posting comment #{r.get('id')}", file=sys.stderr)
        except Exception as e:  # relay is best-effort; never block the digest
            print(f"  [discord] failed posting comment #{r.get('id')}: {e}", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description="Read CurseForge project comments.")
    ap.add_argument("--project", default=DEFAULT_PROJECT, help="slug or numeric id (default: sky-frogs)")
    ap.add_argument("--all", action="store_true", help="show every comment, not just new ones")
    ap.add_argument("--peek", action="store_true", help="show new comments but do NOT update the seen state")
    ap.add_argument("--json", action="store_true", help="emit raw JSON (flattened) instead of a digest")
    ap.add_argument(
        "--discord-webhook",
        default=os.environ.get("DISCORD_CF_WEBHOOK"),
        help="Discord webhook URL to mirror NEW comments to #cf-feedback "
        "(default: $DISCORD_CF_WEBHOOK; ignored with --all/--json)",
    )
    args = ap.parse_args()

    pid = resolve_project(args.project)
    rows = flatten(fetch_all(pid))
    seen = load_seen(pid)

    if args.all:
        shown = rows
    else:
        shown = [r for r in rows if r.get("id") not in seen]

    if args.json:
        print(json.dumps(shown, indent=2, ensure_ascii=False))
    else:
        label = "all" if args.all else "new"
        print(f"CurseForge project {pid}: {len(shown)} {label} comment(s) "
              f"({len(rows)} total on the page).\n")
        if not shown:
            print("  (nothing new since last check)")
        for r in shown:
            indent = "    " * r["_depth"]
            reply = f" (reply to #{r['_parent']})" if r["_parent"] else ""
            pin = " [PINNED]" if r.get("isPinned") else ""
            text = " ".join((r.get("text") or "").split())
            print(f"{indent}#{r.get('id')} - {author_name(r)} - {fmt_date(r.get('datePosted'))}{pin}{reply}")
            print(f"{indent}  {text}\n")

    if args.discord_webhook and not args.all and not args.json and shown:
        post_discord(args.discord_webhook, pid, shown)
        print(f"  [discord] mirrored {len(shown)} comment(s) to #cf-feedback")

    if not args.peek and not args.json:
        save_seen(pid, seen | {r["id"] for r in rows if "id" in r})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
