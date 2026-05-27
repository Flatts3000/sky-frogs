#!/usr/bin/env python3
"""Remap FTB Quests IDs that parse as negative signed longs.

FTB Quests parses quest/task/reward/chapter IDs as signed 64-bit longs and only
accepts positive values (leading hex digit 0-7). Hand-authored IDs with a leading
hex digit 8-F parse as negative, so FTB rejects them on load, assigns fresh IDs,
and drops every `dependencies: [...]` reference that pointed at the old ID - which
silently severs the quest tree.

Fix: for every 16-hex-digit ID whose leading digit is >= 8, subtract 8 from that
leading digit (8->0, 9->1, A->2, ... F->7). This lands the value in the positive
range while keeping the remaining 60 bits identical, so the transform is
deterministic and applies the same way to an ID and to every dependency that
references it - keeping links intact. Aborts if any remap would collide.

Usage: python tools/fix_quest_ids.py <snbt-file> [<snbt-file> ...]
"""
import re
import sys

ID_RE = re.compile(r'"([0-9A-F]{16})"')


def remap(token: str) -> str:
    lead = int(token[0], 16)
    if lead < 8:
        return token
    return format(lead - 8, "X") + token[1:]


def process(paths: list[str]) -> int:
    """Remap negative-leading IDs across all given files as one ID namespace.

    FTB Quests IDs must be unique across every chapter, not just within one file,
    so collision detection runs over the union of IDs from all inputs and the
    same mapping is applied to each file.
    """
    texts = {p: open(p, "r", encoding="utf-8").read() for p in paths}

    originals = set()
    for text in texts.values():
        originals.update(ID_RE.findall(text))
    mapping = {tok: remap(tok) for tok in originals}
    changed = {k: v for k, v in mapping.items() if k != v}

    if not changed:
        print("no negative IDs found, nothing to do.")
        return 0

    # Collision guard (global, across all inputs): no two distinct source IDs may
    # map to the same target, and no target may collide with an ID left untouched.
    untouched = {k for k, v in mapping.items() if k == v}
    targets = list(mapping.values())
    if len(targets) != len(set(targets)):
        sys.exit("ABORT: remap produced a duplicate target ID across inputs.")
    for src, dst in changed.items():
        if dst in untouched:
            sys.exit(f"ABORT: {src} -> {dst} collides with an untouched ID.")

    # Replace whole quoted tokens so we never touch item ids / component values.
    for path, text in texts.items():
        new_text = ID_RE.sub(lambda m: '"' + mapping[m.group(1)] + '"', text)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new_text)
        n = sum(1 for tok in ID_RE.findall(text) if tok in changed)
        print(f"{path}: remapped {n} IDs")

    for src in sorted(changed):
        print(f"  {src} -> {changed[src]}")
    return len(changed)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: fix_quest_ids.py <snbt-file> [...]")
    process(sys.argv[1:])
