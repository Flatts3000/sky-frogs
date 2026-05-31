#!/usr/bin/env python3
"""Static validator for the FTB Quests content (Sky Frogs).

Layer 1 of docs/quest_testing.md: catches the *authoring / data* class of quest bug
(structural integrity, component-match correctness, lang sync, quest <-> recipe drift)
with certainty, across every chapter, in one pass. It does NOT verify FTB's runtime
matching or item/recipe runtime behavior - that needs in-game testing (see the KubeJS
self-test, Layer 2).

Each check encodes a lesson from a real bug. See docs/quest_testing.md for the catalog.

Usage:
    python tools/validate_quests.py [--strict] [--json]

Exit codes: 0 = clean (or warnings only), 1 = at least one ERROR,
            2 = warnings only AND --strict was passed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
QUESTS = REPO / "pack" / "config" / "ftbquests" / "quests"
CHAPTERS_DIR = QUESTS / "chapters"
LANG_FILE = QUESTS / "lang" / "en_us.snbt"
GROUPS_FILE = QUESTS / "chapter_groups.snbt"
RECIPE_DIR = REPO / "pack" / "kubejs" / "server_scripts"
ITEM_ALLOWLIST = REPO / "tools" / "data" / "item_ids.txt"

ERROR, WARN, INFO = "ERROR", "WARN", "INFO"
HEX_POSITIVE = set("01234567")


# --------------------------------------------------------------------------- #
# Minimal SNBT parser
# --------------------------------------------------------------------------- #
# FTB SNBT is relaxed JSON: unquoted keys, members separated by whitespace and/or
# commas, numbers carry a type suffix (0.0d, 1.5d, 12b). We only need structure, so
# scalars are kept as raw strings. The files are machine-generated with consistent
# formatting, so this tolerant reader is robust against what FTB actually writes.
class SNBTError(Exception):
    pass


class SNBT:
    def __init__(self, s: str):
        self.s = s
        self.i = 0
        self.n = len(s)

    def parse(self):
        self._ws()
        v = self._value()
        return v

    def _ws(self):
        while self.i < self.n and self.s[self.i] in " \t\r\n,":
            self.i += 1

    def _value(self):
        self._ws()
        if self.i >= self.n:
            raise SNBTError("unexpected end of input")
        c = self.s[self.i]
        if c == "{":
            return self._obj()
        if c == "[":
            return self._arr()
        if c == '"':
            return self._string()
        return self._scalar()

    def _obj(self) -> dict:
        self.i += 1  # consume {
        d: dict = {}
        while True:
            self._ws()
            if self.i >= self.n:
                raise SNBTError("unterminated object")
            if self.s[self.i] == "}":
                self.i += 1
                return d
            key = self._key()
            self._ws()
            if self.i >= self.n or self.s[self.i] != ":":
                raise SNBTError(f"expected ':' after key {key!r}")
            self.i += 1
            d[key] = self._value()

    def _arr(self) -> list:
        self.i += 1  # consume [
        a: list = []
        while True:
            self._ws()
            if self.i >= self.n:
                raise SNBTError("unterminated array")
            if self.s[self.i] == "]":
                self.i += 1
                return a
            a.append(self._value())

    def _key(self) -> str:
        self._ws()
        if self.s[self.i] == '"':
            return self._string()
        j = self.i
        while self.i < self.n and self.s[self.i] not in " \t\r\n:":
            self.i += 1
        return self.s[j:self.i]

    def _string(self) -> str:
        self.i += 1  # consume opening "
        out = []
        while self.i < self.n:
            c = self.s[self.i]
            if c == "\\":
                self.i += 1
                out.append(self.s[self.i] if self.i < self.n else "")
            elif c == '"':
                self.i += 1
                return "".join(out)
            else:
                out.append(c)
            self.i += 1
        raise SNBTError("unterminated string")

    def _scalar(self) -> str:
        j = self.i
        while self.i < self.n and self.s[self.i] not in " \t\r\n,}]":
            self.i += 1
        tok = self.s[j:self.i]
        return tok


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #
class Chapter:
    def __init__(self, path: Path):
        self.path = path
        self.name = path.name
        self.raw = path.read_text(encoding="utf-8")
        self.data = SNBT(self.raw).parse()
        self.quests = self.data.get("quests", []) or []

    def line_of(self, token: str) -> int:
        """1-based line of the first occurrence of `token` (e.g. a quest id), or 0."""
        idx = self.raw.find(token)
        if idx < 0:
            return 0
        return self.raw.count("\n", 0, idx) + 1


def load_chapters() -> list[Chapter]:
    out = []
    for p in sorted(CHAPTERS_DIR.glob("*.snbt")):
        out.append(Chapter(p))
    return out


def load_group_ids() -> set[str]:
    if not GROUPS_FILE.exists():
        return set()
    data = SNBT(GROUPS_FILE.read_text(encoding="utf-8")).parse()
    return {g["id"] for g in data.get("chapter_groups", []) if "id" in g}


LANG_KEY_RE = re.compile(r'^\s*(quest|chapter|chapter_group)\.([0-9A-Fa-f]+)\.')


def load_lang_ids() -> dict[str, set[str]]:
    """Map kind -> set of ids that appear as lang keys (quest./chapter./chapter_group.)."""
    out = {"quest": set(), "chapter": set(), "chapter_group": set()}
    if not LANG_FILE.exists():
        return out
    for line in LANG_FILE.read_text(encoding="utf-8").splitlines():
        m = LANG_KEY_RE.match(line)
        if m:
            out[m.group(1)].add(m.group(2))
    return out


def load_item_allowlist() -> set[str] | None:
    if not ITEM_ALLOWLIST.exists():
        return None
    ids = set()
    for line in ITEM_ALLOWLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            ids.add(line)
    return ids


def makeable_variants() -> set[str]:
    """Heuristic: PF slime variants the pack's recipes actually produce.

    Collected from the slime-bucket output stamps in the chain scripts and the
    SLIME_TIERS rows in dissolution_slime_recipes.js. Used by Q-VARIANT-MADE (WARN).
    """
    variants: set[str] = set()
    if not RECIPE_DIR.exists():
        return variants
    # Slime-bucket outputs are stamped Variant:"..." (recipe-id strings, double-quoted) or
    # Variant: '...' (KubeJS object literals, single-quoted, e.g. steel_slime_infusing.js).
    out_stamp = re.compile(r"""Variant:\s*["']productivefrogs:([a-z_]+)["']""")
    tier_row = re.compile(r"\[\s*'([a-z_]+)'\s*,\s*'[^']+'\s*\]")
    for js in RECIPE_DIR.glob("*.js"):
        text = js.read_text(encoding="utf-8")
        variants.update(out_stamp.findall(text))
        if js.name == "dissolution_slime_recipes.js":
            variants.update(tier_row.findall(text))
    return variants


# --------------------------------------------------------------------------- #
# Findings
# --------------------------------------------------------------------------- #
class Finding:
    __slots__ = ("severity", "check", "file", "line", "message")

    def __init__(self, severity, check, file, line, message):
        self.severity = severity
        self.check = check
        self.file = file
        self.line = line
        self.message = message

    def as_dict(self):
        return {
            "severity": self.severity,
            "check": self.check,
            "file": self.file,
            "line": self.line,
            "message": self.message,
        }


# --------------------------------------------------------------------------- #
# Helpers for walking the parsed model
# --------------------------------------------------------------------------- #
def iter_quests(chapters):
    for ch in chapters:
        for q in ch.quests:
            yield ch, q


def deps_of(q) -> list[str]:
    d = q.get("dependencies")
    if d is None:
        return []
    if isinstance(d, list):
        return [x for x in d if isinstance(x, str)]
    if isinstance(d, str):
        return [d]
    return []


def item_tasks(q):
    for t in q.get("tasks", []) or []:
        if isinstance(t, dict) and t.get("type") == "item":
            yield t


def components_repr(item) -> str:
    """Canonical string for an item task's component filter, '' if none."""
    if not isinstance(item, dict):
        return ""
    comps = item.get("components")
    if not comps:
        return ""
    return json.dumps(comps, sort_keys=True)


# --------------------------------------------------------------------------- #
# Checks
# --------------------------------------------------------------------------- #
def check_ids(chapters, ctx):
    """Q-ID-POSITIVE + Q-ID-UNIQUE."""
    f = []
    seen: dict[str, tuple] = {}
    HEXID = re.compile(r"^[0-9A-Fa-f]{16}$")
    for ch in chapters:
        # chapter-level id
        if "id" in ch.data:
            _check_one_id(ch.data["id"], "chapter", ch, ch.data["id"], seen, f, HEXID)
        for q in ch.quests:
            qid = q.get("id", "")
            _check_one_id(qid, "quest", ch, qid, seen, f, HEXID)
            for t in q.get("tasks", []) or []:
                if isinstance(t, dict) and "id" in t:
                    _check_one_id(t["id"], "task", ch, qid, seen, f, HEXID)
            for r in q.get("rewards", []) or []:
                if isinstance(r, dict) and "id" in r:
                    _check_one_id(r["id"], "reward", ch, qid, seen, f, HEXID)
    return f


def _check_one_id(theid, kind, ch, anchor, seen, findings, hexre):
    if not isinstance(theid, str) or not hexre.match(theid):
        findings.append(Finding(ERROR, "Q-ID-POSITIVE", ch.name, ch.line_of(str(theid)),
                                f"{kind} id {theid!r} is not a 16-hex-digit id"))
        return
    if theid[0] not in HEX_POSITIVE:
        findings.append(Finding(ERROR, "Q-ID-POSITIVE", ch.name, ch.line_of(theid),
                                f"{kind} id {theid} leads with hex {theid[0]} (>=8 parses as a "
                                f"negative long; FTB regenerates it and drops dependencies). "
                                f"Run tools/fix_quest_ids.py."))
    if theid in seen:
        pk, pch = seen[theid]
        findings.append(Finding(ERROR, "Q-ID-UNIQUE", ch.name, ch.line_of(theid),
                                f"{kind} id {theid} duplicates the {pk} id in {pch} "
                                f"(FTB regenerates on collision, breaking dependencies)"))
    else:
        seen[theid] = (kind, ch.name)


def check_dependencies(chapters, ctx):
    """Q-DEP-RESOLVES + Q-DEP-ACYCLIC."""
    f = []
    quest_ids = ctx["quest_ids"]
    graph = {}
    for ch, q in iter_quests(chapters):
        qid = q.get("id", "")
        graph[qid] = deps_of(q)
        for dep in deps_of(q):
            if dep not in quest_ids:
                f.append(Finding(ERROR, "Q-DEP-RESOLVES", ch.name, ch.line_of(qid),
                                 f"quest {qid} depends on {dep}, which is not a known quest id "
                                 f"(dangling dependency -> orphaned/unreachable quest)"))
            if dep == qid:
                f.append(Finding(ERROR, "Q-DEP-ACYCLIC", ch.name, ch.line_of(qid),
                                 f"quest {qid} depends on itself"))
    # cycle detection (DFS)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {k: WHITE for k in graph}

    def dfs(node, stack):
        color[node] = GRAY
        for dep in graph.get(node, []):
            if dep not in graph:
                continue
            if color[dep] == GRAY:
                cyc = " -> ".join(stack[stack.index(dep):] + [dep])
                f.append(Finding(ERROR, "Q-DEP-ACYCLIC", "(graph)", 0,
                                 f"dependency cycle: {cyc}"))
            elif color[dep] == WHITE:
                dfs(dep, stack + [dep])
        color[node] = BLACK

    for node in graph:
        if color[node] == WHITE:
            dfs(node, [node])
    return f


def check_chapter_group(chapters, ctx):
    """Q-CHAPTER-GROUP (WARN)."""
    f = []
    groups = ctx["group_ids"]
    for ch in chapters:
        g = ch.data.get("group")
        if g and g not in groups:
            f.append(Finding(WARN, "Q-CHAPTER-GROUP", ch.name, ch.line_of(str(g)),
                             f"chapter group {g} is not defined in chapter_groups.snbt"))
    return f


def check_match_components(chapters, ctx):
    """Q-MATCH-COMPONENTS (ERROR) - the tier-skip guard."""
    f = []
    valid = {"strict", "fuzzy"}
    for ch, q in iter_quests(chapters):
        qid = q.get("id", "")
        for t in item_tasks(q):
            item = t.get("item")
            if components_repr(item):  # has a component filter
                mc = t.get("match_components")
                if mc is None:
                    f.append(Finding(ERROR, "Q-MATCH-COMPONENTS", ch.name,
                                     ch.line_of(t.get("id", qid)),
                                     f"quest {qid}: item task filters on components "
                                     f"({item.get('id')}) but has no match_components - FTB "
                                     f"ignores the filter and ANY {item.get('id')} completes it "
                                     f"(tier-skip exploit). Add match_components: \"strict\"."))
                elif mc not in valid:
                    f.append(Finding(ERROR, "Q-MATCH-COMPONENTS", ch.name,
                                     ch.line_of(t.get("id", qid)),
                                     f"quest {qid}: match_components is {mc!r}, "
                                     f"expected one of {sorted(valid)}"))
    return f


def check_dup_tasks(chapters, ctx):
    """Q-NO-DUP-TASK - two quests in a chapter with an identical item task."""
    f = []
    for ch in chapters:
        seen: dict[tuple, str] = {}
        for q in ch.quests:
            qid = q.get("id", "")
            for t in item_tasks(q):
                item = t.get("item") or {}
                key = (item.get("id"), components_repr(item))
                if key in seen:
                    sev = ERROR if key[1] else WARN
                    note = ("identical discriminated task - one quest completing auto-completes "
                            "the other (copy-paste of the variant?)" if key[1]
                            else "two quests require the same bare item - picking it up may "
                                 "complete both")
                    f.append(Finding(sev, "Q-NO-DUP-TASK", ch.name, ch.line_of(t.get("id", qid)),
                                     f"quest {qid} task {key[0]} duplicates quest {seen[key]}: {note}"))
                else:
                    seen[key] = qid
    return f


def check_lang(chapters, ctx):
    """Q-LANG-INLINE (WARN) + Q-LANG-ORPHAN (WARN)."""
    f = []
    inline_keys = ("title", "subtitle", "description", "text")
    quest_ids = ctx["quest_ids"]
    chapter_ids = {ch.data.get("id") for ch in chapters if ch.data.get("id")}
    # inline text in chapters (gets extracted to lang / wiped)
    for ch, q in iter_quests(chapters):
        qid = q.get("id", "")
        for k in inline_keys:
            if k in q:
                f.append(Finding(WARN, "Q-LANG-INLINE", ch.name, ch.line_of(qid),
                                 f"quest {qid} has inline {k!r} in the chapter; FTB extracts text "
                                 f"to lang/en_us.snbt - author it there or it may be wiped"))
    # orphan lang entries
    lang = ctx["lang_ids"]
    for qid in sorted(lang["quest"] - quest_ids):
        f.append(Finding(WARN, "Q-LANG-ORPHAN", "lang/en_us.snbt", 0,
                         f"lang has quest.{qid}.* but no quest {qid} exists (dead entry)"))
    for cid in sorted(lang["chapter"] - chapter_ids):
        f.append(Finding(WARN, "Q-LANG-ORPHAN", "lang/en_us.snbt", 0,
                         f"lang has chapter.{cid}.* but no chapter {cid} exists (dead entry)"))
    return f


DASH_RE = re.compile("[—–]")


def check_dashes(chapters, ctx):
    """Q-NO-DASHES (ERROR) - house rule: ASCII punctuation only."""
    f = []
    files = [LANG_FILE] + [ch.path for ch in chapters]
    for p in files:
        if not p.exists():
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if DASH_RE.search(line):
                f.append(Finding(ERROR, "Q-NO-DASHES", p.name, i,
                                 "em-dash/en-dash present (use ASCII '-' / ':' / restructure)"))
    return f


def check_item_exists(chapters, ctx):
    """Q-ITEM-EXISTS (ERROR) - needs tools/data/item_ids.txt; skips if absent."""
    allow = ctx["item_allowlist"]
    if allow is None:
        return [Finding(INFO, "Q-ITEM-EXISTS", "-", 0,
                        "not run: no tools/data/item_ids.txt. Generate via /kubejs export in the "
                        "dev instance, then commit kubejs/exported item ids (one per line).")]
    f = []
    for ch, q in iter_quests(chapters):
        qid = q.get("id", "")
        stacks = []
        for t in item_tasks(q):
            it = t.get("item")
            if isinstance(it, dict) and it.get("id"):
                stacks.append((it["id"], t.get("id", qid)))
        for r in q.get("rewards", []) or []:
            it = r.get("item") if isinstance(r, dict) else None
            if isinstance(it, dict) and it.get("id"):
                stacks.append((it["id"], r.get("id", qid)))
        for iid, anchor in stacks:
            if iid not in allow:
                f.append(Finding(ERROR, "Q-ITEM-EXISTS", ch.name, ch.line_of(anchor),
                                 f"quest {qid} references item {iid}, not in the pack registry "
                                 f"(Missing Item)"))
    return f


VARIANT_RE = re.compile(r'"productivefrogs:slime_variant":\s*"productivefrogs:([a-z_]+)"')
BUCKET_VAR_RE = re.compile(r'Variant:\s*"productivefrogs:([a-z_]+)"')


def check_variant_made(chapters, ctx):
    """Q-VARIANT-MADE (WARN) - a froglight/slime task for a variant no recipe produces."""
    makeable = ctx["makeable_variants"]
    if not makeable:
        return [Finding(INFO, "Q-VARIANT-MADE", "-", 0,
                        "not run: no makeable variants parsed from kubejs/server_scripts")]
    f = []
    for ch, q in iter_quests(chapters):
        qid = q.get("id", "")
        for t in item_tasks(q):
            item = t.get("item") or {}
            comps = item.get("components") or {}
            variant = None
            sv = comps.get("productivefrogs:slime_variant")
            if isinstance(sv, str) and sv.startswith("productivefrogs:"):
                variant = sv.split(":", 1)[1]
            bed = comps.get("minecraft:bucket_entity_data")
            if isinstance(bed, dict) and isinstance(bed.get("Variant"), str):
                variant = bed["Variant"].split(":", 1)[1]
            if variant and variant not in makeable:
                f.append(Finding(WARN, "Q-VARIANT-MADE", ch.name, ch.line_of(t.get("id", qid)),
                                 f"quest {qid} checks variant '{variant}' but no shipped recipe "
                                 f"produces it (quest <-> recipe drift?)"))
    return f


CHECKS = [
    check_ids,
    check_dependencies,
    check_chapter_group,
    check_match_components,
    check_dup_tasks,
    check_lang,
    check_dashes,
    check_item_exists,
    check_variant_made,
]


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def run():
    chapters = load_chapters()
    ctx = {
        "quest_ids": {q.get("id") for _, q in iter_quests(chapters)},
        "group_ids": load_group_ids(),
        "lang_ids": load_lang_ids(),
        "item_allowlist": load_item_allowlist(),
        "makeable_variants": makeable_variants(),
    }
    findings: list[Finding] = []
    for check in CHECKS:
        findings.extend(check(chapters, ctx))
    n_quests = sum(len(ch.quests) for ch in chapters)
    return findings, len(chapters), n_quests


def main(argv=None):
    ap = argparse.ArgumentParser(description="Static validator for FTB Quests data.")
    ap.add_argument("--strict", action="store_true", help="exit non-zero on warnings too")
    ap.add_argument("--json", action="store_true", help="emit findings as JSON")
    args = ap.parse_args(argv)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    try:
        findings, n_chapters, n_quests = run()
    except SNBTError as e:
        print(f"PARSE ERROR: {e}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps([f.as_dict() for f in findings], indent=2))
    else:
        order = {ERROR: 0, WARN: 1, INFO: 2}
        for fnd in sorted(findings, key=lambda x: (order[x.severity], x.check, x.file, x.line)):
            loc = f"{fnd.file}:{fnd.line}" if fnd.line else fnd.file
            print(f"{fnd.severity:<5} {fnd.check:<20} {loc}\n      {fnd.message}")

    errors = sum(1 for f in findings if f.severity == ERROR)
    warns = sum(1 for f in findings if f.severity == WARN)
    infos = sum(1 for f in findings if f.severity == INFO)
    print(f"\n{errors} error(s), {warns} warning(s), {infos} info "
          f"({n_quests} quests in {n_chapters} chapters checked)", file=sys.stderr)

    if errors:
        return 1
    if warns and args.strict:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
