#!/usr/bin/env python3
"""Run tools/cg_lint.py on the rule test set (step 11) and print each case.

Expected, in his terms:
  P cases (pass): the lint must show no FAIL or FORM.
  F cases (fail): the lint must flag what a script can see. Quality failures
  (F1, F2, F3, F8) have no mechanical break and are left to the checkers (step 12).
Usage: python3 tests/rules/run_lint_on_testset.py [--verbose]
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from cg_lint import lint  # noqa: E402

OUTPUT = {"article": "article", "letter": "letter", "book chapter": "chapter"}
# What a script can see in each failing case.
SCRIPT_VISIBLE = {"F6": "an em dash (three in the draft)", "F7": "his typed words changed or turned into a heading"}
KEEP_F7 = "goal they kept changing"

d = json.load(open(ROOT / "tests/rules/test_set.json", encoding="utf-8"))
verbose = "--verbose" in sys.argv
bad = 0


def show(label, expect, findings, note=""):
    global bad
    breaks = [f for f in findings if f["level"] in ("FAIL", "FORM")]
    notes = [f for f in findings if f["level"] == "NOTE"]
    got = "flagged" if breaks else "clean"
    ok = (expect == "flag" and breaks) or (expect == "clean" and not breaks) or expect == "none"
    if expect != "none" and not ok:
        bad += 1
    mark = "ok  " if ok else "WRONG"
    print(f"{mark} {label:34} expected {expect:5}  got {got:7} ({len(breaks)} breaks, {len(notes)} notes) {note}")
    for f in breaks + (notes if verbose else []):
        print(f"       {f['level']:4} {f['rule']}: {f['msg']}  [{f['excerpt'][:70]}]")


for c in d["cases"]:
    cid, out = c["id"], OUTPUT.get(c["output"])
    if cid == "F7":
        for r in c["failed_renderings"]:
            f, _ = lint(r["text"], None, [KEEP_F7])
            show(f"F7 failed: {r['what']}", "flag", f, "(script-visible)")
        f, _ = lint(c["approved_rendering"], None, [KEEP_F7])
        show("F7 approved rendering", "clean", f)
        continue
    f, st = lint(c["text"], out)
    if c["verdict"] == "pass":
        show(f"{cid} {c['output']}", "clean", f)
    elif cid in SCRIPT_VISIBLE:
        show(f"{cid} {c['output']}", "flag", f, f"(sees {SCRIPT_VISIBLE[cid]})")
    else:
        show(f"{cid} {c['output']}", "none", f, "(quality failure, no mechanical break: left to step 12)")
# Self-test: a sample with every kind of break must trip every check.
f, _ = lint(open(ROOT / "tests/rules/lint_bad_sample.txt", encoding="utf-8").read(), "chapter")
rules = {x["rule"] for x in f}
need = {"T0 no em dashes", "T0 no semicolons", "T0 no emojis", 'T0 never "my clients"', 'T0 no business "we"',
        "T0 locked names", "T0 locked lines", "T0 missing material", "chapter card figures",
        "T2 British spelling", "T2 everyday", "T2 numbers"}
lacking = sorted(need - rules)
print()
print("self-test (lint_bad_sample.txt): " + ("every check fired" if not lacking else "DID NOT FIRE: " + ", ".join(lacking)))
bad += len(lacking)
print("RESULT:", "all as expected" if not bad else f"{bad} case(s) not as expected")
sys.exit(1 if bad else 0)
