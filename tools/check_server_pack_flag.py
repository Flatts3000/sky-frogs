#!/usr/bin/env python3
"""Audit whether Sky Frogs' CurseForge files are typed as Server Packs.

Every release attaches `sky-frogs-server-<version>.zip` to its client file via the
upload API's `parentFileID` (see `.github/workflows/release.yml`). That makes the zip
public under "Additional Files" - but it does NOT make CurseForge treat it as a
*Server Pack*. Those are two different things:

  additional file  -> visible on the file page, downloadable by humans
  server pack      -> the above, PLUS `serverPackFileId` / `isServerPack` set in CF's
                      Core API, which is what server hosts and launcher "create a
                      server" flows read (BisectHosting, Akliz, Nodecraft, Pterodactyl
                      eggs, itzg/docker-minecraft-server AUTO_CURSEFORGE).

The CurseForge **upload API cannot set that flag** - `upload-file` accepts only
changelog / changelogType / displayName / parentFileID / gameVersions /
gameVersionNames / releaseType / isMarkedForManualRelease / relations, and
`update-file` is the same minus parentFileID. CF support confirmed there is no
documented way (henkelmax/upload-curseforge-modpack-action#1, where sending
`isServerPack: true` in the metadata was tested and silently ignored). So the flag is
a MANUAL step in the Authors Console, once per release:

    Authors Console -> project -> Files -> click the client file
      -> the attached server file -> set "Additional File Info" to "Server Pack"
         (default is "None")

This script is the verification half of that manual step. It reads the website's own
undocumented v1 API - no API key, same surface `cf_comments.py` uses:

    GET https://www.curseforge.com/api/v1/mods/<projectId>/files?pageIndex=&pageSize=

Each file carries `hasServerPack` (bool) and `additionalServerPackFilesCount` (int)
alongside `additionalFilesCount`. A correctly-typed release reads
additionalFilesCount >= 1 AND hasServerPack true; ours read 1 / false when the manual
step was missed. Undocumented => could change; if the fields disappear, fall back to
the file page (the same values are embedded in its Next.js payload).

Usage:
    python tools/check_server_pack_flag.py              # latest 5 files
    python tools/check_server_pack_flag.py --all
    python tools/check_server_pack_flag.py --limit 10
    python tools/check_server_pack_flag.py --version 1.4.4
    python tools/check_server_pack_flag.py --json
    python tools/check_server_pack_flag.py --project 1552728   # another CF project

Exit codes: 0 = every checked file is typed, 1 = at least one is not, 2 = lookup
failed (network / API shape drift). Non-zero is the point - wire it into the release
checklist rather than trusting the CF page to look right.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

SKY_FROGS_PROJECT_ID = 1558075
FILES_API = "https://www.curseforge.com/api/v1/mods/{project}/files"
CONSOLE_URL = "https://authors.curseforge.com/projects/{project}/files"
PAGE_SIZE = 50
MAX_PAGES = 20  # 1000 files; a hard stop so API drift can't spin forever


def fetch_files(project: int) -> list[dict]:
    """Every published file for a project, newest first."""
    out: list[dict] = []
    for page in range(MAX_PAGES):
        url = f"{FILES_API.format(project=project)}?pageIndex={page * PAGE_SIZE}&pageSize={PAGE_SIZE}"
        req = urllib.request.Request(url, headers={"User-Agent": "sky-frogs-server-pack-audit"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = json.load(resp)
        except (urllib.error.URLError, json.JSONDecodeError, TimeoutError) as exc:
            raise SystemExit(f"error: CurseForge file lookup failed ({exc}). "
                             f"URL: {url}") from exc
        batch = body.get("data") or []
        if not batch:
            break
        out += batch
        if len(batch) < PAGE_SIZE:
            break
    return out


def classify(f: dict) -> tuple[bool, str]:
    """(ok, reason) for one client file."""
    # `hasServerPack` is the field the CF site itself renders off; the count is a
    # cross-check so a single renamed field can't silently pass the audit.
    typed = bool(f.get("hasServerPack")) or int(f.get("additionalServerPackFilesCount") or 0) > 0
    attached = int(f.get("additionalFilesCount") or 0) > 0
    if typed:
        return True, "typed as Server Pack"
    if attached:
        return False, 'attached but NOT typed - set "Additional File Info" to "Server Pack"'
    return False, "no server pack attached at all - did the build step fail?"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", type=int, default=SKY_FROGS_PROJECT_ID,
                    help=f"CurseForge project id (default {SKY_FROGS_PROJECT_ID} = Sky Frogs)")
    ap.add_argument("--limit", type=int, default=5, help="how many recent files to check (default 5)")
    ap.add_argument("--all", action="store_true", help="check every published file")
    ap.add_argument("--version", help="check one release by version, e.g. 1.4.4")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    files = fetch_files(args.project)
    if not files:
        print("error: no published files returned - project id wrong, or the API changed shape.")
        return 2

    if args.version:
        want = args.version.lstrip("v")
        files = [f for f in files if want in (f.get("displayName") or "")
                 or want in (f.get("fileName") or "")]
        if not files:
            print(f"error: no published file matching version {args.version!r}.")
            return 2
    elif not args.all:
        files = files[: args.limit]

    rows = []
    for f in files:
        ok, reason = classify(f)
        rows.append({
            "fileId": f.get("id"),
            "displayName": f.get("displayName"),
            "additionalFiles": f.get("additionalFilesCount"),
            "serverPackFiles": f.get("additionalServerPackFilesCount"),
            "hasServerPack": f.get("hasServerPack"),
            "ok": ok,
            "reason": reason,
        })

    failures = [r for r in rows if not r["ok"]]

    if args.json:
        print(json.dumps({"checked": len(rows), "failures": len(failures), "files": rows}, indent=2))
        return 1 if failures else 0

    width = max(len(r["displayName"] or "") for r in rows)
    for r in rows:
        mark = "OK  " if r["ok"] else "FAIL"
        print(f"{mark}  {(r['displayName'] or ''):<{width}}  "
              f"addl={r['additionalFiles']} serverPack={r['serverPackFiles']}  {r['reason']}")

    print()
    if not failures:
        print(f"All {len(rows)} checked file(s) are typed as Server Packs.")
        return 0

    print(f"{len(failures)} of {len(rows)} checked file(s) are NOT typed as Server Packs.")
    print()
    print("Fix (manual - the CurseForge upload API has no field for this):")
    print(f"  1. {CONSOLE_URL.format(project=args.project)}")
    print("  2. Click the client file, then the attached server file.")
    print('  3. Set "Additional File Info" from "None" to "Server Pack" and save.')
    print("  4. Re-run this script to confirm.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
