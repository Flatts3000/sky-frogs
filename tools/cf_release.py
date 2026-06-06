#!/usr/bin/env python3
"""Upload a packwiz-exported modpack zip to CurseForge as a new file.

CurseForge's author upload API only uploads FILES - it cannot set the project
description (that is dashboard-only; the description source of truth is
docs/curseforge_page.md - paste everything below its PASTE MARKER manually).

The API token is read from the CURSEFORGE_API_KEY environment variable, or, if
unset, from productive-frogs/.env (same author account; see docs/distribution.md).
The token is never printed.

Game-version IDs are the modpack-class IDs CurseForge requires (NOT the mod-class
ones): 11779 = Minecraft 1.21.1, 10150 = NeoForge. Sending the mod-class MC id or a
Java-version id makes CF reject the upload (errorCode 1009). See docs/distribution.md.

Usage:
    python tools/cf_release.py --zip "pack/Sky Frogs-0.2.0.zip" \
        --display-name "Sky Frogs 0.2.0" \
        --release-type beta \
        --changelog-file release_changelog.md
"""
import argparse
import json
import os
import sys
import uuid
from urllib import request, error

PROJECT_ID = 1558075          # Sky Frogs on CurseForge (docs/distribution.md)
GAME_VERSIONS = [11779, 10150]  # MC 1.21.1 (modpack class) + NeoForge
UPLOAD_URL = "https://minecraft.curseforge.com/api/projects/%d/upload-file"
ENV_FALLBACK = r"F:\minecraft-repos\productive-frogs\.env"


def resolve_token():
    token = os.environ.get("CURSEFORGE_API_KEY")
    if token:
        return token.strip()
    if os.path.exists(ENV_FALLBACK):
        for line in open(ENV_FALLBACK, encoding="utf-8"):
            if line.startswith("CURSEFORGE_API_KEY"):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("No CURSEFORGE_API_KEY in env or %s" % ENV_FALLBACK)


def encode_multipart(metadata, zip_path):
    boundary = "----skyfrogs" + uuid.uuid4().hex
    crlf = b"\r\n"
    parts = []
    parts.append(b"--" + boundary.encode())
    parts.append(b'Content-Disposition: form-data; name="metadata"')
    parts.append(b"")
    parts.append(metadata.encode("utf-8"))
    parts.append(b"--" + boundary.encode())
    fname = os.path.basename(zip_path)
    parts.append(('Content-Disposition: form-data; name="file"; filename="%s"' % fname).encode())
    parts.append(b"Content-Type: application/zip")
    parts.append(b"")
    with open(zip_path, "rb") as handle:
        parts.append(handle.read())
    parts.append(b"--" + boundary.encode() + b"--")
    parts.append(b"")
    return boundary, crlf.join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", required=True, help="Path to the packwiz-exported CF zip")
    parser.add_argument("--display-name", required=True, help='Human file name, e.g. "Sky Frogs 0.2.0"')
    parser.add_argument("--release-type", default="beta", choices=["alpha", "beta", "release"])
    parser.add_argument("--changelog-file", help="Path to a markdown changelog for this file")
    parser.add_argument("--changelog", default="", help="Inline changelog (ignored if --changelog-file given)")
    parser.add_argument("--project-id", type=int, default=PROJECT_ID)
    parser.add_argument("--dry-run", action="store_true", help="Build the request but do not POST")
    args = parser.parse_args()

    if not os.path.exists(args.zip):
        sys.exit("Zip not found: %s" % args.zip)
    changelog = args.changelog
    if args.changelog_file:
        changelog = open(args.changelog_file, encoding="utf-8").read()

    metadata = json.dumps({
        "changelog": changelog,
        "changelogType": "markdown",
        "displayName": args.display_name,
        "gameVersions": GAME_VERSIONS,
        "releaseType": args.release_type,
    })

    boundary, body = encode_multipart(metadata, args.zip)
    print("Uploading %s (%d bytes) as %s [%s] to project %d ..." % (
        os.path.basename(args.zip), os.path.getsize(args.zip),
        args.display_name, args.release_type, args.project_id))
    if args.dry_run:
        print("--dry-run: not sending. metadata=%s" % metadata)
        return

    token = resolve_token()
    req = request.Request(
        UPLOAD_URL % args.project_id,
        data=body,
        headers={
            "X-Api-Token": token,
            "Content-Type": "multipart/form-data; boundary=%s" % boundary,
            "User-Agent": "sky-frogs-release/1.0",
        },
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=120) as resp:
            payload = resp.read().decode("utf-8", "replace")
            print("HTTP %d: %s" % (resp.status, payload))
            try:
                file_id = json.loads(payload).get("id")
                if file_id:
                    print("Uploaded. File ID: %s" % file_id)
                    print("https://www.curseforge.com/minecraft/modpacks/sky-frogs/files/%s" % file_id)
            except (ValueError, AttributeError):
                pass
    except error.HTTPError as exc:
        sys.exit("Upload failed: HTTP %d\n%s" % (exc.code, exc.read().decode("utf-8", "replace")))
    except error.URLError as exc:
        sys.exit("Upload failed (network): %s" % exc.reason)


if __name__ == "__main__":
    main()
