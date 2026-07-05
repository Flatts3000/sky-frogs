#!/usr/bin/env python3
"""Score every quest description for mechanical AI-tells and regenerate
docs/quest_rewrite_candidates.md.

This is the tool behind the candidates doc: run it after any quest-text change
so the ranking reflects the shipped lang, not a stale hand-count. It reads the
committed lang (`pack/config/ftbquests/quests/lang/en_us.snbt`) and the chapter
files (for the quest -> chapter map), scores each described quest, and writes
the ranked markdown table.

Formula (documented so the ranking is reproducible, not a black box). A score
flags the *mechanical* tells only; a human still judges the gestalt.

  dash-as-reveal ` - `   1.5 each   spaced hyphen doing em-dash work (loudest tell)
  long body (>=100 words) 2.5        one-shot; supersedes "wordy"
  wordy body (60-99 words) 1.5       one-shot
  fragment subtitle       1.5        subtitle of <=5 words (the kicker formula)
  rhetorical opener       1.5        desc opens with a question-word clause ending "?"
  'pour' verb             1.0        names an action MC lacks (accuracy tell); human confirms metaphor vs error
  em/en-dash              2.0        hard house-rule violation (validate_quests already blocks these)

  Bands: HIGH >=8 | MED 4-7.5 | LOW 0.5-3.5 | CLEAN 0

Usage: python tools/score_quest_voice.py        # rewrites the doc
       python tools/score_quest_voice.py --check # prints summary, writes nothing
"""
from __future__ import annotations
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_quests as vq  # noqa: E402  (reuse SNBT parser + paths)

DOC = vq.REPO / "docs" / "quest_rewrite_candidates.md"
LANG = vq.LANG_FILE

STR_RE = r'"((?:[^"\\]|\\.)*)"'
RHETORICAL_RE = re.compile(
    r'^\s*(?:tired|done|want|need|ever|why|ready|sick|got|had enough|looking)\b[^"]*\?',
    re.I,
)
POUR_RE = re.compile(r"\bpour(?:s|ed|ing)?\b", re.I)
EMDASH_RE = re.compile(r"[–—]")
DASH_REVEAL_RE = re.compile(r"\S - \S")


def load_lang_text():
    """quest id -> {title, subtitle, desc} from the committed lang file."""
    text = LANG.read_text(encoding="utf-8")
    titles, subs, descs = {}, {}, {}
    for m in re.finditer(r"^\tquest\.([0-9A-F]+)\.title: " + STR_RE, text, re.M):
        titles[m.group(1)] = m.group(2)
    for m in re.finditer(r"^\tquest\.([0-9A-F]+)\.quest_subtitle: " + STR_RE, text, re.M):
        subs[m.group(1)] = m.group(2)
    # quest_desc is an array of quoted strings, written either multi-line
    # (`[\n\t\t"a"\n\t\t"b"\n\t]`) or single-line (`["a"]`). Match a run of
    # quoted strings between the brackets so both shapes parse and a `]` inside
    # a string can't end the match early.
    desc_re = re.compile(r'quest\.([0-9A-F]+)\.quest_desc: \[((?:\s*' + STR_RE + r")*\s*)\]")
    for m in desc_re.finditer(text):
        parts = re.findall(STR_RE, m.group(2))
        descs[m.group(1)] = " ".join(p for p in parts if p != "")
    return titles, subs, descs


def quest_chapter_map():
    """quest id (upper hex) -> chapter filename stem."""
    out = {}
    for ch in vq.load_chapters():
        stem = ch.name[:-5] if ch.name.endswith(".snbt") else ch.name
        for q in ch.quests:
            qid = q.get("id")
            if isinstance(qid, str) and re.fullmatch(r"[0-9A-Fa-f]{16}", qid):
                out[qid.upper()] = stem
    return out


def strip_codes(s: str) -> str:
    return re.sub(r"&[0-9a-fk-or]", "", s)


def word_count(s: str) -> int:
    return len(strip_codes(s).split())


def is_fragment(sub: str) -> bool:
    if not sub:
        return False
    return word_count(sub) <= 5


def score_quest(desc: str, sub: str):
    """Return (score, tell-strings)."""
    tells, score = [], 0.0
    plain = strip_codes(desc)

    n_dash = len(DASH_REVEAL_RE.findall(plain))
    if n_dash:
        score += 1.5 * n_dash
        tells.append(f"{n_dash}x dash-reveal")

    wc = word_count(desc)
    if wc >= 100:
        score += 2.5
        tells.append(f"long ({wc}w)")
    elif wc >= 60:
        score += 1.5
        tells.append(f"wordy ({wc}w)")

    if is_fragment(sub):
        score += 1.5
        tells.append("fragment subtitle")

    if RHETORICAL_RE.match(plain):
        score += 1.5
        tells.append("rhetorical opener")

    if POUR_RE.search(plain):
        score += 1.0
        tells.append("'pour' verb")

    if EMDASH_RE.search(desc) or EMDASH_RE.search(sub):
        score += 2.0
        tells.append("em/en-dash")

    return round(score, 2), tells


def band(score: float) -> str:
    if score >= 8:
        return "HIGH"
    if score >= 4:
        return "MED"
    if score > 0:
        return "LOW"
    return "CLEAN"


def main():
    check_only = "--check" in sys.argv
    titles, subs, descs = load_lang_text()
    chap = quest_chapter_map()

    rows = []
    for qid, desc in descs.items():
        sub = subs.get(qid, "")
        score, tells = score_quest(desc, sub)
        rows.append(
            {
                "score": score,
                "band": band(score),
                "chapter": chap.get(qid, "?"),
                "quest": titles.get(qid, qid),
                "tells": ", ".join(tells),
            }
        )

    rows.sort(key=lambda r: (-r["score"], r["chapter"], r["quest"]))
    counts = {b: sum(1 for r in rows if r["band"] == b) for b in ("HIGH", "MED", "LOW", "CLEAN")}
    total = len(rows)

    print(
        f"{total} descriptions scored. "
        f"HIGH (>=8): {counts['HIGH']} | MED (4-7): {counts['MED']} | "
        f"LOW (0.5-3.5): {counts['LOW']} | CLEAN (0): {counts['CLEAN']}"
    )
    if check_only:
        return

    lines = [
        "# Quest rewrite candidates",
        "",
        "Objective AI-tell scoring of every quest description, ranked by rewrite "
        "priority. **Generated by `python tools/score_quest_voice.py`** - rerun it "
        "after any quest-text edit so the ranking reflects the shipped lang, not a "
        "stale hand-count. A high score flags the *mechanical* tells; a human still "
        "judges the gestalt. Companion to `quest_voice_rewrite.md` (the spec + the "
        "scoring formula lives in the script header).",
        "",
        f"**{total} descriptions scored.** HIGH (>=8): {counts['HIGH']} | "
        f"MED (4-7): {counts['MED']} | LOW (0.5-3.5): {counts['LOW']} | "
        f"CLEAN (0): {counts['CLEAN']}",
        "",
        "| # | Tier | Score | Chapter | Quest | Tells |",
        "|--|--|--|--|--|--|",
    ]
    n = 0
    for r in rows:
        if r["band"] == "CLEAN":
            continue
        n += 1
        lines.append(
            f"| {n} | {r['band']} | {r['score']:g} | {r['chapter']} | "
            f"{r['quest']} | {r['tells']} |"
        )
    lines.append("")
    lines.append(
        f"*(CLEAN rows omitted: {counts['CLEAN']} descriptions show no mechanical tells.)*"
    )
    DOC.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote {DOC}")


if __name__ == "__main__":
    main()
