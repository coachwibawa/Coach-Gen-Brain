#!/usr/bin/env python3
"""cg_rules.py: one place to read the writing rules from the repo (step 16).

The rules as they stand now are rulebook v3 plus every stored fold:
  rules/table/rules_v3.json     the first load (approved 6 Nov 2026), never edited
  rules/folds/*.json            one file per fold, built by tools/cg_fold.py
  rules/table/rules_live.json   v3 with the stored folds applied, written by `cg_fold.py live`
Every tool reads the live file when it exists, else v3. A gate run points the tools at
its own candidate file with the CG_RULES environment variable.

pick(), card_text() and rulebook_text() choose rows the way brain.get_card(),
brain.card_text() and brain.rulebook_text() do, so an md5 from here can be compared
with one from the brain.
"""
import hashlib, json, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V3 = ROOT / "rules/table/rules_v3.json"
LIVE = ROOT / "rules/table/rules_live.json"
FOLDS = ROOT / "rules/folds"
OUTPUTS = ["article", "letter", "chapter", "key moments", "case study"]


def rules_path():
    env = os.environ.get("CG_RULES")
    if env:
        return Path(env)
    return LIVE if LIVE.exists() else V3


def load_rows(path=None):
    return json.loads(Path(path or rules_path()).read_text(encoding="utf-8"))["rows"]


def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def card_code(output):
    return "card:" + output.replace(" ", "-")


def pick(rows, output):
    """The rows one output loads, in rulebook order (same choice as brain.get_card)."""
    by = {r["code"]: r for r in rows}
    chain, k = [], card_code(output)
    while k:
        chain.append(k)
        k = by[k]["extends"]
    t2 = {x for c in chain for x in by[c]["loads"]}
    keep = []
    for r in rows:
        c = r["code"]
        if (r["kind"] == "frame" and c in ("title", "tier0", "tier1", "cards")) \
           or (r["kind"] == "frame" and c == "tier2" and t2) \
           or (r["kind"] == "rule" and r["tier"] in (0, 1) and output in r["outputs"]) \
           or (r["kind"] == "rule" and r["tier"] == 2 and c in t2) \
           or (r["kind"] == "card" and c in chain):
            keep.append(r)
    return sorted(keep, key=lambda r: r["sort"])


def card_text(rows, output):
    return "\n".join(r["body"] for r in pick(rows, output)) + "\n"


def rulebook_text(rows):
    return "\n".join(r["body"] for r in sorted(rows, key=lambda r: r["sort"])) + "\n"


def all_md5(rows):
    """{'rulebook': md5, 'article': md5, ...}: the values brain.fold_store returns."""
    out = {"rulebook": md5(rulebook_text(rows))}
    for o in OUTPUTS:
        out[o] = md5(card_text(rows, o))
    return out
