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

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pf_jar  # noqa: E402  (shared PF-jar access; see #101)

REPO = Path(__file__).resolve().parent.parent
QUESTS = REPO / "pack" / "config" / "ftbquests" / "quests"
CHAPTERS_DIR = QUESTS / "chapters"
TABLES_DIR = QUESTS / "reward_tables"
LANG_FILE = QUESTS / "lang" / "en_us.snbt"
GROUPS_FILE = QUESTS / "chapter_groups.snbt"
RECIPE_DIR = REPO / "pack" / "kubejs" / "server_scripts"
ITEM_ALLOWLIST = REPO / "tools" / "data" / "item_ids.txt"

ERROR, WARN, INFO = "ERROR", "WARN", "INFO"
HEX_POSITIVE = set("01234567")

# FTB Quests "filter" task items: the item id is a virtual filter, and matching is driven
# by the embedded filter expression (e.g. components."ftbfiltersystem:filter":
# "item_tag(c:ingots/steel)"), NOT by item-id/component equality. Verified from the FTB
# Quests bytecode: ItemTask.test -> ItemMatchingSystem.doesItemMatch checks getFilterAdapter
# first and delegates to the adapter's filter test, never consulting match_components for a
# filter stack; only NON-filter items fall through to the component-equality path. So filter
# items are exempt from Q-MATCH-COMPONENTS (the filter expression IS the matcher;
# match_components is N/A and ignored at runtime).
#
# They are NOT exempt from Q-ITEM-EXISTS: a filter item is a *real* registered item once the
# FTB Filter System mod (ftbfiltersystem) ships in the pack, so it must appear in
# item_ids.txt like anything else. (Exempting it once masked a Missing Item - a smart_filter
# task authored while the mod was not installed rendered as "Missing Item" in-game but passed
# the validator. Keep the registry check live so a filter item from an absent mod is caught.)
#
# The Q-MATCH-COMPONENTS exemption also requires the filter-expression component to be present
# and non-empty - a smart_filter with no expression is an authoring mistake and must NOT be
# exempted (it should fall through to the normal checks and get flagged).
FILTER_ITEMS = {"ftbfiltersystem:smart_filter"}
FILTER_EXPR_COMPONENT = "ftbfiltersystem:filter"


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


class RewardTable:
    """A reward_tables/<hexid>.snbt file. `table_id` references it as the signed-long
    decimal of the hex id (same id space as quests), e.g. id 7F00D00000000001 is
    referenced as table_id: 9151543141235425281L."""

    def __init__(self, path: Path):
        self.path = path
        self.name = path.name
        self.raw = path.read_text(encoding="utf-8")
        self.data = SNBT(self.raw).parse()
        self.id = self.data.get("id", "")
        self.rewards = self.data.get("rewards", []) or []

    def line_of(self, token: str) -> int:
        idx = self.raw.find(token)
        return self.raw.count("\n", 0, idx) + 1 if idx >= 0 else 0


def load_reward_tables() -> list[RewardTable]:
    if not TABLES_DIR.exists():
        return []
    return [RewardTable(p) for p in sorted(TABLES_DIR.glob("*.snbt"))]


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
    # MODDED_SELF_KEYED rows (PR #106) are 5-element: [CATEGORY, filler, variant, resource, mod]
    modded_row = re.compile(r"\[\s*'[A-Z_]+'\s*,\s*'[^']+'\s*,\s*'([a-z_]+)'\s*,")
    for js in RECIPE_DIR.glob("*.js"):
        text = js.read_text(encoding="utf-8")
        variants.update(out_stamp.findall(text))
        if js.name == "dissolution_slime_recipes.js":
            variants.update(tier_row.findall(text))
            variants.update(modded_row.findall(text))
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


def is_filter_item(item) -> bool:
    """True if the task item is a well-formed FTB Quests filter item.

    Requires both the filter item id AND a non-empty filter-expression component. A
    smart_filter with no expression is an authoring mistake, so it is NOT treated as a
    filter item - it falls through to Q-ITEM-EXISTS / Q-MATCH-COMPONENTS and gets flagged.
    """
    if not isinstance(item, dict) or item.get("id") not in FILTER_ITEMS:
        return False
    comps = item.get("components")
    expr = comps.get(FILTER_EXPR_COMPONENT) if isinstance(comps, dict) else None
    return isinstance(expr, str) and expr.strip() != ""


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
    # reward tables share the same 64-bit id space; a collision with a quest id breaks both
    for tbl in ctx["reward_tables"]:
        if tbl.id:
            _check_one_id(tbl.id, "reward-table", tbl, tbl.id, seen, f, HEXID)
        for e in tbl.rewards:
            if isinstance(e, dict) and "id" in e:
                _check_one_id(e["id"], "reward-table entry", tbl, e["id"], seen, f, HEXID)
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
            if is_filter_item(item):  # filter expression is the matcher; match_components N/A
                continue
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


COLOR_CODE_RE = re.compile(r"&[0-9a-fk-or]")
DESC_ARRAY_RE = re.compile(r"quest\.[0-9A-F]+\.quest_desc: \[(.*?)\n\t\]", re.S)
DESC_ELEM_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def check_desc_midbreak(chapters, ctx):
    """Q-DESC-MIDBREAK (ERROR ,/- | WARN no punctuation) - a quest_desc element that
    ends mid-sentence followed by "" renders as a blank line splitting the sentence
    in-game (each array element is its own line; FTB auto-wraps within an element).
    Author whole paragraphs per element; keep "" only between true paragraphs."""
    if not LANG_FILE.exists():
        return []
    f = []
    text = LANG_FILE.read_text(encoding="utf-8")
    for m in DESC_ARRAY_RE.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        elems = DESC_ELEM_RE.findall(m.group(1))
        for i, elem in enumerate(elems[:-2]):
            if not (elem and elems[i + 1] == "" and elems[i + 2]):
                continue
            stripped = COLOR_CODE_RE.sub("", elem).rstrip()
            if stripped.endswith((",", "-")):
                f.append(Finding(ERROR, "Q-DESC-MIDBREAK", LANG_FILE.name, line_no,
                                 f"desc element ends mid-sentence ({stripped[-25:]!r}) before a "
                                 f"blank line - join the fragments into one paragraph element"))
            elif not re.search(r"[.!?:)\]}\"']$", stripped):
                f.append(Finding(WARN, "Q-DESC-MIDBREAK", LANG_FILE.name, line_no,
                                 f"desc element ends without punctuation ({stripped[-25:]!r}) "
                                 f"before a blank line - mid-sentence break? join if so"))
    return f


DASH_RE = re.compile("[—–]")


def check_dashes(chapters, ctx):
    """Q-NO-DASHES (ERROR) - house rule: ASCII punctuation only."""
    f = []
    files = [LANG_FILE] + [ch.path for ch in chapters] + [t.path for t in ctx["reward_tables"]]
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
            # NOTE: filter items (ftbfiltersystem:smart_filter) are NOT exempt here. They
            # are real registered items once the FTB Filter System mod ships in the pack, so
            # they MUST appear in item_ids.txt - exempting them once masked a Missing Item
            # (a smart_filter task while the mod wasn't installed). Let the registry check run.
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
    for tbl in ctx["reward_tables"]:
        for e in tbl.rewards:
            it = e.get("item") if isinstance(e, dict) else None
            if isinstance(it, dict) and it.get("id") and it["id"] not in allow:
                f.append(Finding(ERROR, "Q-ITEM-EXISTS", tbl.name, tbl.line_of(e.get("id", "")),
                                 f"reward table {tbl.id} grants item {it['id']}, not in the pack "
                                 f"registry (Missing Item)"))
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


SINGULARITY_DIR = REPO / "pack" / "config" / "extendedcrafting" / "singularities"


def check_singularity_coverage(chapters, ctx):
    """Q-SINGULARITY-COVERAGE - every singularity the Ultimate demands must be farmable.

    The Ultimate Singularity auto-includes every singularity JSON with
    inUltimateSingularity: true, so each one's variant needs (a) a recipe that
    produces its slime (ERROR - without it the Ultimate is uncraftable, the #79
    class) and (b) a froglight quest somewhere (WARN - the one-quest-per-resource
    design law). Guards against a future PF variant addition silently reopening
    the gap.
    """
    if not SINGULARITY_DIR.exists():
        return [Finding(INFO, "Q-SINGULARITY-COVERAGE", "-", 0,
                        "not run: no extendedcrafting/singularities directory")]
    makeable = ctx["makeable_variants"]
    quested: set[str] = set()
    for ch, q in iter_quests(chapters):
        for t in item_tasks(q):
            comps = (t.get("item") or {}).get("components") or {}
            sv = comps.get("productivefrogs:slime_variant")
            if isinstance(sv, str) and sv.startswith("productivefrogs:"):
                quested.add(sv.split(":", 1)[1])
    f = []
    for p in sorted(SINGULARITY_DIR.glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not data.get("inUltimateSingularity"):
            continue
        variant = p.stem
        if makeable and variant not in makeable:
            f.append(Finding(ERROR, "Q-SINGULARITY-COVERAGE", p.name, 0,
                             f"the Ultimate Singularity demands '{variant}' but no shipped "
                             f"recipe produces its slime - the Ultimate is uncraftable (#79)"))
        if variant not in quested:
            f.append(Finding(WARN, "Q-SINGULARITY-COVERAGE", p.name, 0,
                             f"singularity variant '{variant}' has no froglight quest in any "
                             f"chapter (one-quest-per-resource law)"))
    return f


def check_singularity_ingredient(chapters, ctx):
    """Q-SINGULARITY-INGREDIENT (ERROR) - the #101 / blaze-rod drift class.

    Every committed singularity's `ingredient.item` must equal its variant's
    `primer_item` in the PINNED PF jar (the Froglight smelt output - the resource
    the Quantum Compressor is supposed to demand). PF 1.11 changed blaze's primer
    powder -> rod and the singularity had to be re-generated by hand-audit; this
    check makes the next such change a validator ERROR instead of a memory test.
    Skips with INFO when no jar is locatable (e.g. CI without the dev instance).
    """
    variants = ctx["pf_variants"]
    if variants is None:
        return []  # Q-PF-JAR (emitted by the loader) already says why
    if not SINGULARITY_DIR.exists():
        return []
    f = []
    for p in sorted(SINGULARITY_DIR.glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            f.append(Finding(ERROR, "Q-SINGULARITY-INGREDIENT", p.name, 0,
                             "unparseable singularity JSON"))
            continue
        variant = p.stem
        ingredient = (data.get("ingredient") or {}).get("item")
        vdata = variants.get(variant)
        if vdata is None:
            f.append(Finding(ERROR, "Q-SINGULARITY-INGREDIENT", p.name, 0,
                             f"singularity '{variant}' has no slime_variant in the pinned PF jar "
                             f"(removed upstream? regenerate via tools/gen_singularities.py)"))
            continue
        primer = vdata.get("primer_item")
        if ingredient != primer:
            f.append(Finding(ERROR, "Q-SINGULARITY-INGREDIENT", p.name, 0,
                             f"singularity '{variant}' ingredient is {ingredient!r} but the "
                             f"pinned PF jar's primer_item is {primer!r} - stale after a PF "
                             f"resource change (the blaze-rod class). Re-run "
                             f"tools/gen_singularities.py."))
    return f


DISSOLUTION_JS = RECIPE_DIR / "dissolution_slime_recipes.js"
# A vanilla-chain row: ['variant', 'ns:item']  (2 elements)
CHAIN_ROW_RE = re.compile(r"\[\s*'([a-z_]+)'\s*,\s*'([a-z0-9_:.]+)'\s*\]")
# A tier header: ['CATEGORY', 'ns:filler', [
TIER_HEAD_RE = re.compile(r"\[\s*'([A-Z_]+)'\s*,\s*'([a-z0-9_:.]+)'\s*,\s*\[")
# A modded self-keyed row: ['CATEGORY', 'filler', 'variant', 'ns:item', 'mod']  (5 elements)
MODDED_ROW_RE = re.compile(
    r"\[\s*'([A-Z_]+)'\s*,\s*'[a-z0-9_:.]+'\s*,\s*'([a-z_]+)'\s*,\s*'(#?[a-z0-9_:./]+)'\s*,\s*'([a-z_]+)'\s*\]")
# Threading exceptions: variants whose chamber input deliberately breaks the
# prior-resource law. iron has nothing pre-Cave to thread off (bone meal mirrors
# the table bootstrap).
THREADING_EXCEPTIONS = {"iron": "minecraft:bone_meal"}
# Self-keyed rows whose input deliberately is NOT the variant's primer_item: the
# fluid pair takes the FLUID BUCKETS (day-one obtainable; the primers kelp /
# pointed_dripstone are frog-only). Maintainer ruling on the PF 1.13 sweep.
SELF_KEYED_EXCEPTIONS = {"water": "minecraft:water_bucket", "lava": "minecraft:lava_bucket"}


def check_dissolution_threading(chapters, ctx):
    """Q-DISSOLUTION-THREADING (ERROR) - the other half of #101.

    Two laws over dissolution_slime_recipes.js, diffed against the pinned PF jar:
      - SLIME_TIERS (vanilla chains): row N's input == row N-1's variant primer_item;
        each tier's first row bridges off the PRIOR tier's last variant's primer.
      - MODDED_SELF_KEYED: each row's input == that variant's OWN primer_item
        (the make-it-yourself-first law, PR #106).
    Skips with INFO when no jar is locatable.
    """
    variants = ctx["pf_variants"]
    if variants is None:
        return []  # Q-PF-JAR (emitted by the loader) already says why
    if not DISSOLUTION_JS.exists():
        return [Finding(INFO, "Q-DISSOLUTION-THREADING", "-", 0,
                        "not run: dissolution_slime_recipes.js not found")]
    text = DISSOLUTION_JS.read_text(encoding="utf-8")
    fname = DISSOLUTION_JS.name

    def line_of(pos):
        return text.count("\n", 0, pos) + 1

    reported_missing: set[str] = set()

    def primer(variant, pos, f):
        vdata = variants.get(variant)
        if vdata is None:
            if variant not in reported_missing:  # one finding per missing variant, not per use
                reported_missing.add(variant)
                f.append(Finding(ERROR, "Q-DISSOLUTION-THREADING", fname, line_of(pos),
                                 f"row for '{variant}': no such slime_variant in the pinned "
                                 f"PF jar"))
            return None
        return vdata.get("primer_item")

    f = []
    # Split the file at the MODDED_SELF_KEYED table so the 2-element row regex
    # only runs over the vanilla SLIME_TIERS region.
    modded_at = text.find("MODDED_SELF_KEYED")
    tiers_region_end = modded_at if modded_at >= 0 else len(text)

    # --- vanilla chains: group rows under their tier header, in file order
    heads = [(m.start(), m.group(1)) for m in TIER_HEAD_RE.finditer(text, 0, tiers_region_end)]

    # Parser sanity guard (review finding on PR #110): a source-format change that
    # the regexes no longer match would otherwise parse ZERO rows and pass green
    # vacuously. Today's counts: 6 tiers, 55 chain rows, 36 modded rows (PF 1.15) -
    # assert a conservative minimum so format drift is a loud ERROR, not a silent skip.
    n_chain_rows = len(CHAIN_ROW_RE.findall(text, 0, tiers_region_end))
    n_modded_rows = len(MODDED_ROW_RE.findall(text, tiers_region_end))
    if len(heads) < 6 or n_chain_rows < 35 or (modded_at >= 0 and n_modded_rows < 1):
        return [Finding(ERROR, "Q-DISSOLUTION-THREADING", fname, 0,
                        f"parser found only {len(heads)} tier heads / {n_chain_rows} chain rows "
                        f"/ {n_modded_rows} modded rows (expected >=6 / >=35 / >=1) - the file "
                        f"format drifted away from the regexes; update the parser in "
                        f"tools/validate_quests.py before trusting this check")]
    prev_tier_last_variant = None
    for hi, (hpos, tier) in enumerate(heads):
        hend = heads[hi + 1][0] if hi + 1 < len(heads) else tiers_region_end
        rows = [(m.start(), m.group(1), m.group(2))
                for m in CHAIN_ROW_RE.finditer(text, hpos, hend)]
        prev_variant = prev_tier_last_variant
        for pos, variant, inp in rows:
            if variant in THREADING_EXCEPTIONS:
                if inp != THREADING_EXCEPTIONS[variant]:
                    f.append(Finding(ERROR, "Q-DISSOLUTION-THREADING", fname, line_of(pos),
                                     f"'{variant}' is the documented exception and must take "
                                     f"{THREADING_EXCEPTIONS[variant]!r}, found {inp!r}"))
            elif prev_variant is None:
                pass  # first row of the first tier with no bridge defined
            else:
                expect = primer(prev_variant, pos, f)
                if expect is not None and inp != expect:
                    f.append(Finding(ERROR, "Q-DISSOLUTION-THREADING", fname, line_of(pos),
                                     f"[{tier}] '{variant}' input is {inp!r} but the prior "
                                     f"variant '{prev_variant}' has primer_item {expect!r} - "
                                     f"threading broken (stale after a PF resource change?)"))
            primer(variant, pos, f)  # also flags rows for variants PF no longer ships
            prev_variant = variant
        if rows:
            prev_tier_last_variant = rows[-1][1]

    # --- modded self-keyed rows: input must equal the variant's own primer
    for m in MODDED_ROW_RE.finditer(text, tiers_region_end):
        pos, variant, inp = m.start(), m.group(2), m.group(3)
        if variant in SELF_KEYED_EXCEPTIONS:
            if inp != SELF_KEYED_EXCEPTIONS[variant]:
                f.append(Finding(ERROR, "Q-DISSOLUTION-THREADING", fname, line_of(pos),
                                 f"[self-keyed] '{variant}' is the documented fluid-bucket "
                                 f"exception and must take {SELF_KEYED_EXCEPTIONS[variant]!r}, "
                                 f"found {inp!r}"))
            primer(variant, pos, f)  # still flags variants PF no longer ships
            continue
        vdata = variants.get(variant)
        if vdata is None:
            primer(variant, pos, f)  # reports the missing variant once
            continue
        # tag-primed variants (PF primer_tag) expect '#<tag>'; item-primed, primer_item
        expect = vdata.get("primer_item") or (
            "#" + vdata["primer_tag"] if vdata.get("primer_tag") else None)
        if expect is not None and inp != expect:
            f.append(Finding(ERROR, "Q-DISSOLUTION-THREADING", fname, line_of(pos),
                             f"[self-keyed] '{variant}' input is {inp!r} but its own "
                             f"primer is {expect!r} - the make-it-first law (PR #106) "
                             f"requires the variant's own resource"))
    return f



# The crafting-table seed chains that must MIRROR the chamber chains (#125 - the
# breeze-slime gap: a variant added to SLIME_TIERS but not to its tier's table
# chain ships with a chamber recipe and no crafting recipe). Cave/Geode/Bog only:
# Tide and later are chamber-only by design law.
TABLE_CHAINS = {
    "cave_slime_chain.js": "CAVE",
    "geode_slime_chain.js": "GEODE",
    "bog_slime_chain.js": "BOG",
}
TABLE_PAIR_RE = re.compile(r"\[\s*'([a-z_]+)'\s*,\s*'([a-z_]+)'\s*\]")


def check_table_chain_mirror(chapters, ctx):
    """Q-TABLE-CHAIN-MIRROR (ERROR) - no jar needed (pack file vs pack file).

    Every [from, to] step in a *_slime_chain.js must be an ADJACENT pair in the
    same tier's SLIME_TIERS block (or a bridge from the previous tier's last
    variant into the tier's first). A step that skips variants means someone
    extended the chamber chain and forgot the table chain - exactly the breeze
    gap. Partial coverage at the ends is allowed (bootstraps live elsewhere).
    """
    if not DISSOLUTION_JS.exists():
        return []
    diss = DISSOLUTION_JS.read_text(encoding="utf-8")
    modded_at = diss.find("MODDED_SELF_KEYED")
    end = modded_at if modded_at >= 0 else len(diss)
    heads = [(m.start(), m.group(1)) for m in TIER_HEAD_RE.finditer(diss, 0, end)]
    tier_seq: dict[str, list[str]] = {}
    tier_order: list[str] = []
    for hi, (hpos, tier) in enumerate(heads):
        hend = heads[hi + 1][0] if hi + 1 < len(heads) else end
        tier_seq[tier] = [m.group(1) for m in CHAIN_ROW_RE.finditer(diss, hpos, hend)]
        tier_order.append(tier)
    if not tier_seq:
        return []  # the threading check's parser guard already screams

    f = []
    for fname, tier in TABLE_CHAINS.items():
        path = RECIPE_DIR / fname
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        pairs = TABLE_PAIR_RE.findall(text)
        if not pairs:
            f.append(Finding(ERROR, "Q-TABLE-CHAIN-MIRROR", fname, 0,
                             "parser found no [from, to] chain pairs - format drift? "
                             "update TABLE_PAIR_RE before trusting this check"))
            continue
        seq = tier_seq.get(tier, [])
        prev_last = None
        ti = tier_order.index(tier) if tier in tier_order else -1
        if ti > 0:
            prev = tier_seq[tier_order[ti - 1]]
            prev_last = prev[-1] if prev else None
        for frm, to in pairs:
            if to not in seq:
                f.append(Finding(ERROR, "Q-TABLE-CHAIN-MIRROR", fname, 0,
                                 f"table step '{frm}' -> '{to}': output variant is not in the "
                                 f"{tier} chamber chain"))
                continue
            if frm in seq:
                fi, ti2 = seq.index(frm), seq.index(to)
                if ti2 != fi + 1:
                    skipped = seq[fi + 1:ti2] if ti2 > fi else []
                    detail = (f"skips {', '.join(skipped)}" if skipped
                              else "is out of order vs the chamber chain")
                    f.append(Finding(ERROR, "Q-TABLE-CHAIN-MIRROR", fname, 0,
                                     f"table step '{frm}' -> '{to}' {detail} - the chamber "
                                     f"chain ({tier}) and the table chain disagree (the "
                                     f"breeze-slime gap, #125)"))
            elif frm == prev_last:
                if seq and to != seq[0]:
                    f.append(Finding(ERROR, "Q-TABLE-CHAIN-MIRROR", fname, 0,
                                     f"bridge step '{frm}' -> '{to}' should land on the "
                                     f"{tier} chain's first variant ('{seq[0]}')"))
            else:
                f.append(Finding(ERROR, "Q-TABLE-CHAIN-MIRROR", fname, 0,
                                 f"table step '{frm}' -> '{to}': '{frm}' is neither in the "
                                 f"{tier} chamber chain nor the previous tier's last variant"))
    return f


# The ATO seed chain mirrors the chamber's MODDED_SELF_KEYED alltheores rows the
# same way the tier table chains mirror SLIME_TIERS (the #125 drift class,
# re-opened by the PR #126 review): a metal added to one surface but not the
# other ships a census quest with no bootstrap, or a chain step with no scaling
# row, and nothing else screams. Osmium is the chain ROOT - bootstrapped by
# osmium_slime_bucket.js, never a chain output - so it is exempt from the
# output-coverage direction but must still hold a chamber row.
ATO_CHAIN_JS = "ato_slime_chain.js"
ATO_CHAIN_ROOT = "osmium"


def check_ato_chain_mirror(chapters, ctx):
    """Q-ATO-CHAIN-MIRROR (ERROR) - no jar needed (pack file vs pack file).

    The [from, to] steps in ato_slime_chain.js must form ONE connected chain
    rooted at osmium, and the set of chain outputs must equal the chamber's
    alltheores self-keyed rows minus the root. Either direction of drift is the
    breeze-slime gap (#125) transplanted to the modded table.
    """
    path = RECIPE_DIR / ATO_CHAIN_JS
    if not path.exists() or not DISSOLUTION_JS.exists():
        return []
    diss = DISSOLUTION_JS.read_text(encoding="utf-8")
    modded_at = diss.find("MODDED_SELF_KEYED")
    ato_rows = [m.group(2) for m in MODDED_ROW_RE.finditer(diss, max(modded_at, 0))
                if m.group(4) == "alltheores"]
    pairs = TABLE_PAIR_RE.findall(path.read_text(encoding="utf-8"))
    if not pairs or not ato_rows:
        return [Finding(ERROR, "Q-ATO-CHAIN-MIRROR", ATO_CHAIN_JS, 0,
                        f"parser found {len(pairs)} chain pairs / {len(ato_rows)} alltheores "
                        f"chamber rows (expected >=1 each) - format drift; update the parser "
                        f"in tools/validate_quests.py before trusting this check")]

    f = []
    if pairs[0][0] != ATO_CHAIN_ROOT:
        f.append(Finding(ERROR, "Q-ATO-CHAIN-MIRROR", ATO_CHAIN_JS, 0,
                         f"chain starts at '{pairs[0][0]}' but the root must be "
                         f"'{ATO_CHAIN_ROOT}' (the osmium_slime_bucket.js bootstrap)"))
    for i in range(1, len(pairs)):
        if pairs[i][0] != pairs[i - 1][1]:
            f.append(Finding(ERROR, "Q-ATO-CHAIN-MIRROR", ATO_CHAIN_JS, 0,
                             f"chain breaks between '{pairs[i - 1][1]}' and step "
                             f"'{pairs[i][0]}' -> '{pairs[i][1]}' - each step must take the "
                             f"prior step's output milk"))
    outputs = {to for _, to in pairs}
    if ATO_CHAIN_ROOT not in ato_rows:
        f.append(Finding(ERROR, "Q-ATO-CHAIN-MIRROR", "dissolution_slime_recipes.js", 0,
                         f"'{ATO_CHAIN_ROOT}' has no alltheores self-keyed chamber row - the "
                         f"chain root scales in the chamber like every census variant"))
    for v in ato_rows:
        if v != ATO_CHAIN_ROOT and v not in outputs:
            f.append(Finding(ERROR, "Q-ATO-CHAIN-MIRROR", ATO_CHAIN_JS, 0,
                             f"'{v}' has an alltheores chamber row but no chain step crafts "
                             f"its slime - a census quest with no bootstrap (the #125 gap)"))
    for v in sorted(outputs - set(ato_rows)):
        f.append(Finding(ERROR, "Q-ATO-CHAIN-MIRROR", ATO_CHAIN_JS, 0,
                         f"chain step outputs '{v}' but it has no alltheores self-keyed "
                         f"chamber row - no scaling path once the first frog exists"))
    return f


TABLE_REWARD_TYPES = {"loot", "random", "choice"}


def check_reward_tables(chapters, ctx):
    """Q-REWARD-TABLE-RESOLVES (ERROR) + Q-REWARD-TABLE-ORPHAN (WARN).

    A loot/random/choice reward points at a reward_tables/<hexid>.snbt via
    `table_id: <signed-long-decimal>L`. Verify it carries a table_id and that the id
    resolves to a real table (the decimal is int(hexid, 16)). Encodes the new
    reward-crate feature so a typo'd table_id can't ship a silently-empty reward.
    """
    f = []
    tables = ctx["reward_tables"]
    by_long = {}
    for tbl in tables:
        if isinstance(tbl.id, str) and re.fullmatch(r"[0-9A-Fa-f]{16}", tbl.id):
            by_long[int(tbl.id, 16)] = tbl
    for tbl in tables:
        if not tbl.rewards:
            f.append(Finding(ERROR, "Q-REWARD-TABLE-EMPTY", tbl.name, tbl.line_of(tbl.id or ""),
                             f"reward table {tbl.id} has no entries - any loot crate pointing at "
                             f"it grants nothing"))
    referenced = set()
    for ch, q in iter_quests(chapters):
        qid = q.get("id", "")
        for r in q.get("rewards", []) or []:
            if not isinstance(r, dict) or r.get("type") not in TABLE_REWARD_TYPES:
                continue
            raw_tid = r.get("table_id")
            if raw_tid is None:
                f.append(Finding(ERROR, "Q-REWARD-TABLE-RESOLVES", ch.name,
                                 ch.line_of(r.get("id", qid)),
                                 f"quest {qid}: {r.get('type')} reward has no table_id "
                                 f"(empty reward - nothing is granted)"))
                continue
            tid = str(raw_tid)
            tid = tid[:-1] if tid.endswith(("L", "l")) else tid
            try:
                val = int(tid)
            except ValueError:
                f.append(Finding(ERROR, "Q-REWARD-TABLE-RESOLVES", ch.name,
                                 ch.line_of(r.get("id", qid)),
                                 f"quest {qid}: table_id {raw_tid!r} is not a long"))
                continue
            if val in by_long:
                referenced.add(val)
            else:
                f.append(Finding(ERROR, "Q-REWARD-TABLE-RESOLVES", ch.name,
                                 ch.line_of(r.get("id", qid)),
                                 f"quest {qid}: table_id {raw_tid} resolves to no reward table "
                                 f"in reward_tables/ (hex {val & 0xFFFFFFFFFFFFFFFF:016X})"))
    for val, tbl in by_long.items():
        if val not in referenced:
            f.append(Finding(WARN, "Q-REWARD-TABLE-ORPHAN", tbl.name, tbl.line_of(tbl.id),
                             f"reward table {tbl.id} is referenced by no quest (dead table)"))
    return f


def check_hide_until(chapters, ctx):
    """Q-HIDE-UNTIL-NOOP (WARN) - hide_until_deps_complete on a quest with no dependencies.

    The flag hides a quest until its dependencies complete; with no deps the condition is
    vacuously true, so the flag does nothing. Encodes the P0 reveal-pacing work: catches a
    hide flag dropped on a chapter-root (or copy-paste) where it has no effect.
    """
    f = []
    for ch, q in iter_quests(chapters):
        flag = q.get("hide_until_deps_complete")
        if flag in (True, "true", "1b", "1") and not deps_of(q):
            f.append(Finding(WARN, "Q-HIDE-UNTIL-NOOP", ch.name, ch.line_of(q.get("id", "")),
                             f"quest {q.get('id')} sets hide_until_deps_complete but has no "
                             f"dependencies - the flag has no effect"))
    return f


CHECKS = [
    check_ids,
    check_dependencies,
    check_chapter_group,
    check_match_components,
    check_dup_tasks,
    check_lang,
    check_desc_midbreak,
    check_dashes,
    check_item_exists,
    check_variant_made,
    check_singularity_coverage,
    check_singularity_ingredient,
    check_dissolution_threading,
    check_table_chain_mirror,
    check_ato_chain_mirror,
    check_reward_tables,
    check_hide_until,
]


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def load_pf_variants(explicit_jar: str | None) -> tuple[dict | None, list[Finding]]:
    """(variant data from the PF jar, findings about how it was loaded).

    None variants => the jar-dependent checks skip; the findings say WHY, and the
    distinctions matter (code-review findings on PR #110):
      - no jar at all          -> INFO  (CI without the dev instance; by design)
      - jar present, unreadable -> WARN (corrupt/partial download is NOT a clean skip)
      - jar != the pinned filename -> WARN + skip (validating against the WRONG PF
        version produces false greens AND false reds; run sync_instance.py first).
    An explicit --pf-jar bypasses the staleness comparison (a deliberate override,
    e.g. validating against a CDN download before syncing).
    """
    jar = pf_jar.find_jar(explicit_jar)
    if jar is None:
        return None, [Finding(INFO, "Q-PF-JAR", "-", 0,
                              "jar checks not run: no productivefrogs jar found "
                              "(tools/sync_instance.py populates the dev instance; "
                              "or pass --pf-jar PATH)")]
    if not explicit_jar:
        pinned = pf_jar.pinned_filename()
        actual = Path(jar).name
        if pinned and actual != pinned:
            return None, [Finding(WARN, "Q-PF-JAR", actual, 0,
                                  f"jar on disk is {actual} but the pack pins {pinned} - "
                                  f"STALE jar would make the jar checks lie in both "
                                  f"directions; run tools/sync_instance.py (MC closed). "
                                  f"Jar checks skipped.")]
    try:
        return pf_jar.load_variants(jar), []
    except Exception as e:
        return None, [Finding(WARN, "Q-PF-JAR", Path(jar).name, 0,
                              f"jar exists but is unreadable ({type(e).__name__}: {e}) - "
                              f"corrupt or partial download? Jar checks skipped.")]


def run(pf_jar_path: str | None = None):
    chapters = load_chapters()
    pf_variants, jar_findings = load_pf_variants(pf_jar_path)
    ctx = {
        "quest_ids": {q.get("id") for _, q in iter_quests(chapters)},
        "group_ids": load_group_ids(),
        "lang_ids": load_lang_ids(),
        "item_allowlist": load_item_allowlist(),
        "makeable_variants": makeable_variants(),
        "reward_tables": load_reward_tables(),
        "pf_variants": pf_variants,
    }
    findings: list[Finding] = list(jar_findings)
    for check in CHECKS:
        findings.extend(check(chapters, ctx))
    n_quests = sum(len(ch.quests) for ch in chapters)
    return findings, len(chapters), n_quests


def main(argv=None):
    ap = argparse.ArgumentParser(description="Static validator for FTB Quests data.")
    ap.add_argument("--strict", action="store_true", help="exit non-zero on warnings too")
    ap.add_argument("--json", action="store_true", help="emit findings as JSON")
    ap.add_argument("--pf-jar", help="path to the pinned productivefrogs jar (default: the "
                                     "dev instance's mods folder; absent = jar checks skip)")
    args = ap.parse_args(argv)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    try:
        findings, n_chapters, n_quests = run(args.pf_jar)
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
