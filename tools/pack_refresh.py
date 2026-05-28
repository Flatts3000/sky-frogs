#!/usr/bin/env python3
"""Normalize pack text files to LF, then run `packwiz refresh`.

Why this wrapper exists
-----------------------
FTB Quests (and some mods) rewrite their data files - chapters, lang, configs -
with the platform's native line endings every time a world loads. On Windows
that is CRLF. packwiz hashes the *working-tree bytes* into `pack/index.toml`,
while git stores those same files as LF (`.gitattributes`: `*.snbt text eol=lf`,
and the sibling `text eol=lf` rules).

So if `packwiz refresh` runs after the game has rewritten a file to CRLF, the
hash it records is the CRLF hash. git then normalizes the blob back to LF on
commit, and the committed `index.toml` ends up pointing at a hash that no
committed file actually has - the pack's own integrity index is silently wrong.

Fix: before refreshing, rewrite every LF-governed pack file to LF on disk (the
same transform git's clean filter applies on commit). Then `packwiz refresh`
hashes LF bytes, matching the committed blobs. Run this instead of bare
`packwiz refresh` any time pack files may have been touched - by the game, by
hand edits, or by an FTB world load.

Usage: python tools/pack_refresh.py
"""
import subprocess
import sys
from pathlib import Path

# Extensions git forces to LF (mirrors the `text eol=lf` lines in .gitattributes).
# `.bat` / `.cmd` / `.ps1` are deliberately excluded - those are `eol=crlf`.
LF_EXTS = {".md", ".toml", ".json", ".json5", ".snbt", ".js", ".mcmeta", ".yml", ".yaml"}

PACK = Path(__file__).resolve().parent.parent / "pack"


def normalize_lf(pack: Path) -> list[str]:
    """Rewrite CRLF -> LF on disk for every LF-governed file under `pack`.

    Idempotent: files already LF are left untouched (no rewrite, so packwiz
    won't see a spurious mtime bump). Lone CR is left alone, matching git's
    `text` clean filter, which only collapses CRLF. Returns the files changed.
    """
    changed = []
    for f in pack.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in LF_EXTS:
            continue
        data = f.read_bytes()
        if b"\r\n" not in data:
            continue
        f.write_bytes(data.replace(b"\r\n", b"\n"))
        changed.append(f.relative_to(pack).as_posix())
    return changed


def main() -> int:
    if not PACK.is_dir():
        sys.exit(f"pack dir not found: {PACK}")

    changed = normalize_lf(PACK)
    if changed:
        print(f"normalized {len(changed)} file(s) CRLF -> LF:")
        for c in changed:
            print(f"  {c}")
    else:
        print("line endings already LF, nothing to normalize.")

    print("running `packwiz refresh`...")
    try:
        return subprocess.run(["packwiz", "refresh"], cwd=PACK).returncode
    except FileNotFoundError:
        sys.exit("ABORT: `packwiz` not found on PATH. Install it or add it to PATH.")


if __name__ == "__main__":
    sys.exit(main())
