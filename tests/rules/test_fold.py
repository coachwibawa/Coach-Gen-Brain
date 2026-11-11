#!/usr/bin/env python3
"""Self-test for tools/cg_fold.py (step 16). Runs the whole fold path in a throwaway
copy of the repo, with made-up rule text and made-up checker answers. Nothing here
touches rules/folds, the brain or the real test runs.

It covers: build (a change, two new rules, a retire, the card rows that follow),
the gate (touched checkers only, an origin draft, a kept answer, a failing gate),
decline, approve, stored (md5 check, live files, cards, checkers, the next base).

Usage: python3 tests/rules/test_fold.py [--keep]   (--keep leaves the copy and prints its path)
       python3 tests/rules/test_fold.py --emit FILE writes the approved sample fold to FILE,
                                                    for the dry run inside the brain
"""
import json, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = {
    "slug": "selftest", "date": "2026-11-11", "source": "tests/rules/test_fold.py: made-up lessons, never stored",
    "lessons": [
        {"action": "change", "target": "R1.7",
         "add": [{"line": "SELFTEST added line about one story.", "after": "One arc, told forward. You can say in one sentence which story you are telling."}],
         "reword": [{"old": "- No return trips to a story already told, and no new pieces of it later.",
                     "new": "SELFTEST reworded: no return trips to a story already told."}],
         "why": "self-test",
         "his_words": [{"on": "11 Nov 2026", "about": "a made-up draft", "quote": "made-up words"}]},
        {"action": "new", "tier": 1, "heading": "Selftest rule one", "after": "R1.7",
         "lines": ["SELFTEST the goal of this made-up rule.", "SELFTEST its test."], "why": "self-test"},
        {"action": "new", "tier": 1, "heading": "Selftest rule two", "after": "R1.7",
         "lines": ["SELFTEST second new rule after the same rule."], "why": "self-test"},
        {"action": "new", "tier": 2, "heading": "Selftest polish, in full", "short": "Selftest polish", "after": "R2.6",
         "cards": ["article", "chapter"], "lines": ["SELFTEST a polish line."], "why": "self-test"},
        {"action": "retire", "target": "R2.5", "why": "self-test: raw emotion leaves"},
        {"action": "change", "target": "card:case-study", "add": [{"line": "SELFTEST a new card line."}], "why": "self-test"},
        {"action": "new", "tier": 0, "heading": "Selftest hard line", "check_type": "checker",
         "lines": ["SELFTEST never this."], "why": "self-test, declined below"},
    ],
}


def run(tmp, *args, ok=True):
    p = subprocess.run([sys.executable] + list(args), cwd=tmp, capture_output=True, text=True)
    out = p.stdout + p.stderr
    if ok and p.returncode:
        sys.exit(f"FAILED: {' '.join(args)}\n{out}")
    if not ok and not p.returncode:
        sys.exit(f"SHOULD HAVE FAILED: {' '.join(args)}\n{out}")
    return out


def answers(run_dir, code, ids, failing=()):
    res = [{"id": i, "verdict": "fail" if i in failing else "pass",
            "breaks": [{"quote": "made up", "why": "made up"}] if i in failing else []} for i in ids]
    (run_dir / f"{code}.json").write_text(json.dumps({"rule": code, "results": res}), encoding="utf-8")


def check(cond, what):
    print(("ok   " if cond else "WRONG") + " " + what)
    if not cond:
        sys.exit(1)


def main():
    tmp = Path(tempfile.mkdtemp(prefix="cg_fold_test_"))
    for d in ("tools", "rules", "tests"):
        shutil.copytree(ROOT / d, tmp / d, ignore=shutil.ignore_patterns("__pycache__", "folds", "rules_live.json", "rulebook_live.txt", "BASE"))
    sys.path.insert(0, str(tmp / "tools"))
    import cg_rules
    v3 = cg_rules.load_rows(tmp / "rules/table/rules_v3.json")
    v3_md5 = cg_rules.all_md5(v3)
    spec = tmp / "spec.json"
    spec.write_text(json.dumps(SPEC), encoding="utf-8")
    fold = tmp / "rules/folds/2026-11-11_selftest.json"
    rd = tmp / "tests/rules/runs/selftest"

    out = run(tmp, "tools/cg_fold.py", "build", str(spec))
    f = json.loads(fold.read_text(encoding="utf-8"))
    by = {r["target"] or r["code"]: r for r in f["rows"]}
    check(set(by) == {"R1.7", "R1.21", "R1.22", "R2.12", "R2.5", "R0.9", "card:article", "card:letter", "card:chapter",
                      "card:key-moments", "card:case-study"}, "build: 7 lessons give 11 rows, cards included")
    check(by["R1.21"]["sort"] < by["R1.22"]["sort"] and 180 < by["R1.21"]["sort"] < 190, "two new rules after R1.7 keep their order, before R1.8")
    check("R2.5" not in by["card:article"]["loads"] and "R2.12" in by["card:article"]["loads"], "the article card drops R2.5 and loads R2.12")
    check("Raw emotion" not in by["card:article"]["body"] and by["card:article"]["body"].endswith("Selftest polish, Callbacks and staying close, Moves that work."),
          "the article card's Tier 2 line was rebuilt, in rulebook order")
    check(by["card:letter"]["body"] == next(r["body"] for r in v3 if r["code"] == "card:letter") and "R2.5" not in by["card:letter"]["loads"],
          "the letter card keeps its text and follows the article card's loads")
    check(by["card:case-study"]["body"].split("\n")[-2] == "- SELFTEST a new card line.", "a card line is added above the Tier 2 line")
    check("Checkers this fold touches: R1.7, R1.21, R1.22" in out, "build names the touched checkers")
    run(tmp, "tools/cg_fold.py", "approve", str(fold), ok=False)
    check(True, "approve refuses a fold that is not gated")

    # decline lesson 7 (the Tier 0 rule): codes of the others stay
    run(tmp, "tools/cg_fold.py", "decline", str(fold), "7", "--note", "self-test: he said no")
    f2 = json.loads(fold.read_text(encoding="utf-8"))
    check([r["code"] for r in f2["rows"]] == [r["code"] for r in f["rows"] if r["code"] != "R0.9"] and f2["declined"][0]["code"] == "R0.9",
          "decline removes that lesson, keeps every other code, and keeps the declined row on file")

    # gate: touched checkers only, with an origin draft
    origin = tmp / "origin.md"
    origin.write_text("A made-up draft the lesson came from.\n", encoding="utf-8")
    out = run(tmp, "tools/cg_fold.py", "gate", str(fold), "--dir", str(rd), "--origin", str(origin), "--origin-output", "chapter")
    prompts = sorted(p.name for p in rd.glob("*.prompt.md"))
    check(prompts == ["R1.21.prompt.md", "R1.22.prompt.md", "R1.7.prompt.md"], "gate writes prompts for the 3 touched checkers only")
    p7 = (rd / "R1.7.prompt.md").read_text(encoding="utf-8")
    check("SELFTEST added line about one story." in p7 and "No return trips to a story already told, and no new pieces" not in p7,
          "the R1.7 prompt carries the candidate rule text")
    check('<draft id="ORIGIN"' in p7 and "SELFTEST a new card line." in p7, "the prompt carries the origin draft and the candidate card")
    ids = [m["id"] for m in json.loads((rd / "manifest_in.json").read_text(encoding="utf-8"))]
    run(tmp, "tools/cg_fold.py", "result", str(fold), "--dir", str(rd), ok=False)
    check(True, "result refuses while answers are missing")
    answers(rd, "R1.7", ids, failing=("ORIGIN", "F2"))
    answers(rd, "R1.21", ids)
    answers(rd, "R1.22", ids, failing=("P3",))
    out = run(tmp, "tools/cg_fold.py", "result", str(fold), "--dir", str(rd), ok=False)
    check("GATE FAILED" in out and "P3      pass      fail        WRONG  R1.22 Selftest rule two" in out, "a false fail on an approved passage fails the gate")
    answers(rd, "R1.22", ids)
    out = run(tmp, "tools/cg_fold.py", "result", str(fold), "--dir", str(rd))
    check("15 of 15 cases as expected" in out and "ORIGIN  fail      fail        ok     R1.7" in out, "the gate passes: 5 fails, 9 passes and the origin draft")
    check("F1      fail      fail        ok     R1.16" in out, "untouched checkers come from the last full run (F1 still caught by R1.16)")
    f3 = json.loads(fold.read_text(encoding="utf-8"))
    check(all(r["fold_stage"] == "gated" and r["test_gate"]["fails_caught"] == "5 of 5" and r["test_gate"]["passes_kept"] == "9 of 9" for r in f3["rows"]),
          "the gate result is written into every row")
    out = run(tmp, "tools/cg_fold.py", "gate", str(fold), "--dir", str(rd), "--origin", str(origin), "--origin-output", "chapter")
    check("none (all answers kept)" in out, "a second gate on the same text keeps the answers")

    # approve and store
    run(tmp, "tools/cg_fold.py", "approve", str(fold), "--on", "2026-11-11")
    if "--emit" in sys.argv:
        shutil.copyfile(fold, sys.argv[sys.argv.index("--emit") + 1])
    f4 = json.loads(fold.read_text(encoding="utf-8"))
    import cg_fold
    cand = cg_fold.apply_fold(v3, f4)
    want = cg_rules.all_md5(cand)
    keys = {"rulebook": "rulebook", "article": "article", "letter": "letter", "chapter": "chapter", "key_moments": "key moments", "case_study": "case study"}
    wrong = [f"{k}={'0' * 32 if k == 'chapter' else want[v]}" for k, v in keys.items()]
    run(tmp, "tools/cg_fold.py", "stored", str(fold), "--md5", *wrong, ok=False)
    check(not json.loads(fold.read_text(encoding="utf-8"))["stored_on"] and not (tmp / "rules/table/rules_live.json").exists(),
          "stored refuses when one md5 differs from the brain's, and marks nothing")
    out = run(tmp, "tools/cg_fold.py", "stored", str(fold), "--md5", *[f"{k}={want[v]}" for k, v in keys.items()])
    live = cg_rules.load_rows(tmp / "rules/table/rules_live.json")
    check(cg_rules.all_md5(live) == want and want != v3_md5, "the live file is v3 plus the fold")
    codes = [r["code"] for r in live]
    check("R2.5" not in codes and codes.index("R1.7") < codes.index("R1.21") < codes.index("R1.22") < codes.index("R1.8"), "live order: R1.7, R1.21, R1.22, R1.8, and R2.5 is gone")
    check((tmp / "rules/checkers/R1.21.md").exists() and len(list((tmp / "rules/checkers").glob("R1.*.md"))) == 22, "the checkers were rebuilt: 22 templates")
    card = (tmp / "rules/table/cards/Card_Article.md").read_text(encoding="utf-8")
    check("SELFTEST a polish line." in card and "Show raw emotions" not in card, "the article card was recompiled")
    check((tmp / "tests/rules/runs/BASE").read_text().strip() == "selftest", "the gate run is the base for the next fold")
    txt = (tmp / "rules/rulebook/rulebook_live.txt").read_text(encoding="utf-8")
    check("SELFTEST reworded: no return trips to a story already told." in txt, "rulebook_live.txt holds the new wording")
    out = run(tmp, "tools/cg_fold.py", "build", str(fold), ok=False)
    check("approved" in out, "an approved fold cannot be rebuilt")
    # a second fold builds on the first
    spec2 = dict(SPEC, slug="selftest-two", lessons=[{"action": "change", "target": "R1.21", "add": [{"line": "SELFTEST second fold."}], "why": "self-test"}])
    spec.write_text(json.dumps(spec2), encoding="utf-8")
    out = run(tmp, "tools/cg_fold.py", "build", str(spec))
    check("CHANGE R1.21" in out, "a second fold can change a rule the first one added")
    print("\nself-test: every check passed")
    if "--keep" in sys.argv:
        print(tmp)
    else:
        shutil.rmtree(tmp)


main()
