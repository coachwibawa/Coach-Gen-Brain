#!/usr/bin/env python3
"""Step 10: the card compiler.

Builds the five writing cards (article, letter, chapter, key moments, case study)
from the rules table data (rules/table/rules_v3.json, the exact file loaded into
brain.rules), the same way brain.get_card() picks rows: Tier 0, Tier 1, the card
and the card it extends, and the Tier 2 rules the card names, in rulebook order.

Checks, each of which fails the run:
 1. Every card line is a line of rulebook_v3.txt, word for word, in the same order.
 2. Each card's md5 equals the md5 of brain.card_text(output) read from the live
    brain (pass them in with --brain-md5 output=md5, or the script uses the
    values recorded in rules/table/cards/MANIFEST.md5).
 3. The five cards together use every rule and card row of the table.

Usage: python3 rules/table/compile_cards.py OUTDIR [--brain-md5 article=... ...]
"""
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "rules/rulebook/rulebook_v3.txt"
LOAD = ROOT / "rules/table/rules_v3.json"
OUTPUTS = ["article", "letter", "chapter", "key moments", "case study"]
FILES = {"article": "Card_Article.md", "letter": "Card_Letter.md", "chapter": "Card_Chapter.md",
         "key moments": "Card_Key_Moments.md", "case study": "Card_Case_Study.md"}


def fail(m):
    sys.exit("FAIL: " + m)


def pick(rows, out):
    by = {r["code"]: r for r in rows}
    code = "card:" + out.replace(" ", "-")
    chain, k = [], code
    while k:
        chain.append(k)
        k = by[k]["extends"]
    t2 = {x for c in chain for x in by[c]["loads"]}
    keep = []
    for r in rows:
        c = r["code"]
        if (r["kind"] == "frame" and c in ("title", "tier0", "tier1", "cards")) \
           or (r["kind"] == "frame" and c == "tier2" and t2) \
           or (r["kind"] == "rule" and r["tier"] in (0, 1) and out in r["outputs"]) \
           or (r["kind"] == "rule" and r["tier"] == 2 and c in t2) \
           or (r["kind"] == "card" and c in chain):
            keep.append(r)
    return sorted(keep, key=lambda r: r["sort"])


def main():
    args = sys.argv[1:]
    if not args:
        fail("usage: compile_cards.py OUTDIR [--brain-md5 output=md5 ...]")
    outdir = Path(args[0])
    brain = {}
    if "--brain-md5" in args:
        for kv in args[args.index("--brain-md5") + 1:]:
            k, v = kv.split("=", 1)
            brain[k.replace("_", " ")] = v
    rows = json.loads(LOAD.read_text(encoding="utf-8"))["rows"]
    src_lines = SRC.read_text(encoding="utf-8").split("\n")[:-1]
    pos = {l: i for i, l in enumerate(src_lines)}
    outdir.mkdir(parents=True, exist_ok=True)
    used, manifest = set(), []
    for out in OUTPUTS:
        sel = pick(rows, out)
        used |= {r["code"] for r in sel if r["kind"] != "frame"}
        text = "\n".join(r["body"] for r in sel) + "\n"
        lines = text.split("\n")[:-1]
        last = -1
        for n, l in enumerate(lines, 1):
            if l not in pos:
                fail(f"{out}: line {n} is not a line of the rulebook: {l[:60]}")
            if pos[l] <= last:
                fail(f"{out}: line {n} is out of rulebook order")
            last = pos[l]
        md5 = hashlib.md5(text.encode("utf-8")).hexdigest()
        if out in brain and brain[out] != md5:
            fail(f"{out}: md5 {md5} differs from the brain's {brain[out]}")
        (outdir / FILES[out]).write_text(text, encoding="utf-8")
        manifest.append(f"{md5}  {FILES[out]}")
        rule_lines = sum(1 for l in lines if l.startswith("- "))
        print(f"{out:12} {len(lines):3} lines  {rule_lines:3} rule lines  ~{round(len(text)/4):,} tokens  {md5}"
              + ("  = brain" if out in brain else ""))
    every = {r["code"] for r in rows if r["kind"] != "frame"}
    if used != every:
        fail("rows never served by any card: " + ", ".join(sorted(every - used)))
    (outdir / "MANIFEST.md5").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(f"ok: 5 cards in {outdir}, every line word for word from rulebook_v3.txt, every rule and card used")


main()
