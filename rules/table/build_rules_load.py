#!/usr/bin/env python3
"""Step 9: cut the approved rulebook into rows for brain.rules.

Reads rules/rulebook/rulebook_v3.txt and the step 6 inventory, writes
rules/table/rules_v3.json for brain.load_rules(). The rulebook text is copied
by script, never retyped. Every row's body is its exact block of the file, so
joining the bodies in order gives the file back byte for byte.

Usage: python3 rules/table/build_rules_load.py
"""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "rules/rulebook/rulebook_v3.txt"
INV = ROOT / "rules/inventory/inventory.psv"
TGT = ROOT / "rules/inventory/targets.psv"
OUT = ROOT / "rules/table/rules_v3.json"

OUTPUTS = ["article", "letter", "chapter", "key moments", "case study"]
CARD_CODE = {"Article": "card:article", "Letter": "card:letter", "Chapter": "card:chapter",
             "Key moments": "card:key-moments", "Case study": "card:case-study"}
CARD_OUTPUT = {"card:article": "article", "card:letter": "letter", "card:chapter": "chapter",
               "card:key-moments": "key moments", "card:case-study": "case study"}
CARD_GROUP = {"card:article": "card-A", "card:letter": "card-L", "card:chapter": "card-C",
              "card:key-moments": "card-K", "card:case-study": "card-S"}

# v3 heading -> the step 6 groups (targets.psv) its old rules were folded from.
GROUPS = {
    "Banned marks and words": ["T0.1"], "His words stay his": ["T0.2"],
    "True material only": ["T0.3"], "His method and his thesis": ["T0.4"],
    "Built details: the hard lines": ["T0.5"], "Quotes: the hard lines": ["T0.5"],
    "Print names and hidden people": ["T0.6"], "His stance": ["T0.7"],
    "One thread": ["T1.1"], "Joins answer the reader's question": ["T1.2"],
    "Links are real": ["T1.3"], "Few names, one each": ["T1.4"],
    "Nothing arrives bare": ["T1.5"], "Images from the reader's life": ["T1.6"],
    "One story, told once": ["T1.7"], "Stakes, not more story": ["T1.8"],
    "Warm the water": ["T1.9"], "A quote earns its marks": ["T2.11"],
    "Bring it to the reader's life": [], "Research backs, never interrupts": ["T1.10"],
    "Built details serve the reader": ["T1.11"], "No meta-narration": ["T1.12"],
    "Rhythm without choppiness": ["T1.13"], "Parallels that truly match": ["T1.14"],
    "Plain words he would say": ["T1.15"], "Protect the author": ["T1.16"],
    "Turns and endings": ["T1.17"], "AI tells": ["T1.18"],
    "Mechanics, fixed silently": ["T2.1"], "Length and numbers are guardrails": ["T2.2"],
    "Specific detail": ["T2.3"], "Quoted self-talk": ["T2.4"], "Raw emotion": ["T2.5"],
    "Lists of three": ["T2.6"], "Author presence": ["T2.7"],
    "Callbacks and staying close": ["T2.8"], "People on the page": ["T2.9"],
    "Moves that work": ["T2.10"], "Built details you may use": ["T2.12"],
}
# Single rows that moved to a different v3 heading than their step 6 group.
MOVED = {"BR-R16a": "Bring it to the reader's life"}
# Evidence outside the inventory, for rules written new in v2 and v3.
EXTRA_DOCS = {
    "Quotes: the hard lines": ["claude/Case_Study_Quotes_Report_2026-11-05.md"],
    "A quote earns its marks": ["claude/Case_Study_Quotes_Report_2026-11-05.md",
                                "rules/rulebook/README.md (v2, v3 line 75)"],
}
CHECK_NEW = {"Quotes: the hard lines": "checker", "A quote earns its marks": "checker",
             "Bring it to the reader's life": "checker"}
CHECK_NAME = {"mech": "mechanical", "checker": "checker", "judge": "judgment"}


def psv(p):
    rows = [l.rstrip("\n").split("|") for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    head = rows[0]
    return [dict(zip(head, r)) for r in rows[1:]]


def fail(msg):
    sys.exit("FAIL: " + msg)


raw = SRC.read_bytes()
text = raw.decode("utf-8")
if not text.endswith("\n") or "\r" in text:
    fail("source must end in one newline and use LF")
lines = text[:-1].split("\n")
if any(not l.strip() for l in lines):
    fail("blank line in source")
if any("—" in l or ";" in l for l in lines):
    fail("em dash or semicolon in source")

# Cut into blocks: every heading line opens one.
blocks, n = [], 0
for i, l in enumerate(lines, start=1):
    if l.startswith("#"):
        blocks.append({"file_first": i, "lines": [l], "num": []})
    else:
        if not blocks:
            fail("text before the title")
        blocks[-1]["lines"].append(l)
        if l.startswith("- "):
            n += 1
            blocks[-1]["num"].append(n)
if n != 215:
    fail(f"expected 215 numbered lines, found {n}")

tgt = {r["id"]: r for r in psv(TGT)}
inv = psv(INV)

rows, tier, sort = [], None, 0
for b in blocks:
    sort += 10
    h = b["lines"][0]
    row = {"sort": sort, "body": "\n".join(b["lines"]),
           "v3_first": b["num"][0] if b["num"] else None,
           "v3_last": b["num"][-1] if b["num"] else None}
    if h.startswith("# "):
        row.update(code="title", kind="frame", tier=None, heading=h[2:])
    elif h.startswith("## "):
        name = h[3:]
        m = re.match(r"Tier (\d):", name)
        if m:
            tier = int(m.group(1))
            row.update(code=f"tier{tier}", kind="frame", tier=tier, heading=name)
        elif name == "Cards":
            tier = "card"
            row.update(code="cards", kind="frame", tier=None, heading=name)
        else:
            fail("unknown section " + name)
    else:
        name = h[4:]
        if tier == "card":
            code = CARD_CODE.get(name.split(" (")[0])
            if not code:
                fail("unknown card " + name)
            row.update(code=code, kind="card", tier=None, heading=name)
        else:
            k = sum(1 for r in rows if r["kind"] == "rule" and r["tier"] == tier) + 1
            row.update(code=f"R{tier}.{k}", kind="rule", tier=tier, heading=name)
        if not b["num"]:
            fail("heading with no numbered lines: " + name)
    rows.append(row)

by_head = {r["heading"]: r for r in rows if r["kind"] == "rule"}
cards = {r["code"]: r for r in rows if r["kind"] == "card"}
t2 = [r for r in rows if r["kind"] == "rule" and r["tier"] == 2]

# Cards: what each extends and which Tier 2 rules it loads.
for code, c in cards.items():
    c["extends"] = None
    c["loads"] = []
    for l in c["body"].split("\n")[1:]:
        if l.startswith("- Everything on the article card"):
            c["extends"] = "card:article"
        if l.startswith("- Tier 2 rules loaded:"):
            val = l.split(":", 1)[1].strip().rstrip(".")
            if val == "the chapter card's":
                c["extends"] = "card:chapter"
                continue
            for short in [s.strip() for s in val.split(",")]:
                hit = [r for r in t2 if r["heading"].startswith(short)]
                if len(hit) != 1:
                    fail(f"{code}: Tier 2 name '{short}' matches {len(hit)} rules")
                c["loads"].append(hit[0]["code"])
    if code == "card:letter" and c["extends"] != "card:article":
        fail("letter card should extend the article card")


def effective_loads(code):
    c = cards[code]
    own = list(c["loads"])
    if c["extends"]:
        own = effective_loads(c["extends"]) + [x for x in own if x not in effective_loads(c["extends"])]
    return own


# Outputs, check type, evidence and fold fields.
used = set()
for r in rows:
    if r["kind"] == "frame":
        r.update(outputs=[], check_type=None, evidence={}, beats=[])
        continue
    if r["kind"] == "card":
        out = [CARD_OUTPUT[r["code"]]] + [CARD_OUTPUT[k] for k in cards if cards[k]["extends"] == r["code"]]
        r["outputs"] = [o for o in OUTPUTS if o in out]
        r["check_type"] = None
        groups = [CARD_GROUP[r["code"]]]
    else:
        if r["heading"] not in GROUPS:
            fail("no step 6 group for " + r["heading"])
        groups = GROUPS[r["heading"]]
        if r["tier"] == 2:
            r["outputs"] = [o for o in OUTPUTS if any(r["code"] in effective_loads(k) and CARD_OUTPUT[k] == o for k in cards)]
            if not r["outputs"]:
                fail("Tier 2 rule on no card: " + r["heading"])
        else:
            r["outputs"] = list(OUTPUTS)
        r["check_type"] = CHECK_NEW.get(r["heading"]) or CHECK_NAME[tgt[groups[0]]["check"]]
    ev = []
    for i in inv:
        if i["action"] not in ("keep", "merge"):
            continue
        moved = MOVED.get(i["id"])
        if (moved and moved == r["heading"]) or (not moved and i["target"] in groups):
            ev.append({k: i[k] for k in ("id", "src", "loc", "rule", "action", "note")})
            used.add(i["id"])
    r["beats"] = [e["id"] for e in ev]
    r["evidence"] = {"step6_groups": groups, "inventory": ev}
    if r["heading"] in EXTRA_DOCS:
        r["evidence"]["docs"] = EXTRA_DOCS[r["heading"]]

for c in cards.values():
    c["loads"] = effective_loads(c["code"]) if not c["loads"] and c["extends"] else c["loads"]

# Every kept or merged inventory row that points at a rule or card is used.
want = {i["id"] for i in inv if i["action"] in ("keep", "merge") and re.match(r"(T\d\.\d+|card-[ALCKS])$", i["target"])}
missing = sorted(want - used)
if missing:
    fail("inventory rows not placed: " + ", ".join(missing))

for r in rows:
    r.setdefault("extends", None)
    r.setdefault("loads", [])

# Checks on the cut.
rule_counts = {t: sum(1 for r in rows if r["kind"] == "rule" and r["tier"] == t) for t in (0, 1, 2)}
line_counts = {t: sum(r["v3_last"] - r["v3_first"] + 1 for r in rows if r["kind"] == "rule" and r["tier"] == t) for t in (0, 1, 2)}
card_lines = sum(r["v3_last"] - r["v3_first"] + 1 for r in rows if r["kind"] == "card")
if rule_counts != {0: 8, 1: 20, 2: 11}:
    fail(f"rule counts {rule_counts}")
if line_counts != {0: 37, 1: 86, 2: 44} or card_lines != 48 or len(cards) != 5:
    fail(f"line counts {line_counts}, cards {len(cards)} with {card_lines} lines")
covered = sorted(x for r in rows if r["v3_first"] for x in range(r["v3_first"], r["v3_last"] + 1))
if covered != list(range(1, 216)):
    fail("numbered lines not covered exactly once")
rejoined = ("\n".join(r["body"] for r in sorted(rows, key=lambda r: r["sort"])) + "\n").encode("utf-8")
if rejoined != raw:
    fail("rows do not rejoin to the source")
numbered = [l for l in lines if l.startswith("- ")]
typed = {4: "- Never \"my clients\".", 139: "- Vary the counts. Twos and fours work too. Sometimes even fives when we\u2019re"}
for k, start in typed.items():
    if not numbered[k - 1].startswith(start):
        fail(f"v3 line {k} is not his typed line")
if "we’re" not in text:
    fail("curly apostrophe in \"we’re\" lost")


def card_text(code):
    c = cards[code]
    pick = {"title", "tier0", "tier1", "cards"} | {r["code"] for r in rows if r["kind"] == "rule" and r["tier"] in (0, 1)}
    loads = effective_loads(code) if c["extends"] else c["loads"]
    if loads:
        pick |= {"tier2"} | set(loads)
    chain, k = [], code
    while k:
        chain.append(k)
        k = cards[k]["extends"]
    pick |= set(chain)
    return "\n".join(r["body"] for r in sorted(rows, key=lambda r: r["sort"]) if r["code"] in pick) + "\n"


md5 = hashlib.md5(raw).hexdigest()
load = {"source": "Coach Gen Writing Rulebook, v3 (Google Doc 1tIfyVrZn34JMATZHWJ72Cc9OvojNzuIlU-g2BOEQPvk), approved 6 Nov 2026",
        "source_file": "rules/rulebook/rulebook_v3.txt", "source_md5": md5,
        "added_on": "2026-11-06", "approved_on": "2026-11-06", "added_by": "rules refactor step 9",
        "rows": rows}
OUT.write_text(json.dumps(load, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

print(f"ok: {len(rows)} rows ({sum(1 for r in rows if r['kind']=='frame')} frame, "
      f"{sum(rule_counts.values())} rules, {len(cards)} cards), 215 lines, rejoins byte for byte")
print(f"source md5 {md5}")
for code in cards:
    t = card_text(code)
    print(f"{code:18} loads {', '.join(effective_loads(code) if cards[code]['extends'] else cards[code]['loads']):60} "
          f"~{round(len(t)/4):,} tokens  md5 {hashlib.md5(t.encode()).hexdigest()}")
print(f"-> {OUT.relative_to(ROOT)}")
