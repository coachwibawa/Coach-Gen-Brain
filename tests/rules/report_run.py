#!/usr/bin/env python3
"""Print a checker run on the test set as REPORT.md: each case, what was expected, what came back.

Usage: python3 tests/rules/report_run.py RUN_DIR [--compare OLD_RUN_DIR] > RUN_DIR/REPORT.md
Needs RUN_DIR/<id>/report.json (from cg_check.py split, then collect per case).
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
heads = {m["code"]: m["heading"] for m in json.loads((ROOT / "rules/checkers/checkers.json").read_text(encoding="utf-8"))}
cases = {c["id"]: c for c in json.loads((ROOT / "tests/rules/test_set.json").read_text(encoding="utf-8"))["cases"]}
run = Path(sys.argv[1])
old = Path(sys.argv[sys.argv.index("--compare") + 1]) if "--compare" in sys.argv else None
ids = [m["id"] for m in json.loads((run / "manifest.json").read_text(encoding="utf-8"))]


def caught(d):
    r = json.loads((d / "report.json").read_text(encoding="utf-8"))
    who = (["lint"] if r["lint"] else []) + [v["rule"] for v in r["checkers"] if v["verdict"] == "fail"]
    return r, who


def label(who):
    return ", ".join(w if w == "lint" else f"{w} {heads[w]}" for w in who) or "-"


rows, detail, wrong = [], [], 0
for i in ids:
    c = cases[i]
    r, who = caught(run / i)
    got = r["result"].lower()
    exp = c["verdict"]
    ok = got == exp
    wrong += not ok
    line = f"| {i} | {c['title'][:60]} | {exp} | {got} | {label(who)} |"
    if old and (old / i / "report.json").exists():
        _, before = caught(old / i)
        line += f" {label(before)} |"
    rows.append(line)
    if who:
        detail.append(f"\n## {i}: {c['title']}\n")
        for f in r["lint"]:
            detail.append(f"- lint, {f['rule']}: {f['msg']}")
        for v in r["checkers"]:
            if v["verdict"] == "fail":
                for b in v["breaks"][:3]:
                    detail.append(f"- {v['rule']} {heads[v['rule']]}: \"{b.get('quote', '')}\". {b.get('why', '')}")
head = "| Case | What it is | Expected | Got | Caught by |" + (" Caught by, before |" if old else "")
sep = "| --- | --- | --- | --- | --- |" + (" --- |" if old else "")
fails = sum(cases[i]["verdict"] == "fail" for i in ids)
print(f"Result: {len(ids) - wrong} of {len(ids)} cases as expected ({fails} fail cases, {len(ids) - fails} approved passages).\n")
print(head)
print(sep)
print("\n".join(rows))
print("\n".join(detail))
