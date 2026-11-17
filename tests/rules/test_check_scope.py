#!/usr/bin/env python3
"""A Tier 1 rule scoped to some outputs is checked only on those outputs (17 Nov 2026).

Runs in a throwaway folder with a made-up rules file. Checks prepare, batch and split.
Usage: python3 tests/rules/test_check_scope.py
"""
import json, os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ok = True


def check(cond, what):
    global ok
    print(("ok    " if cond else "FAIL  ") + what)
    ok = ok and cond


with tempfile.TemporaryDirectory(dir=ROOT / "tests/rules/runs", prefix="_scope_test_") as t:
    t = Path(t)
    live = json.loads((ROOT / "rules/table/rules_v3.json").read_text(encoding="utf-8"))
    rows = live["rows"]
    last = max(r["sort"] for r in rows if r["kind"] == "rule" and r["tier"] == 1)
    rows.append({"sort": last + 1, "body": "### Made-up scoped rule\n- A line.\n", "code": "R1.99", "kind": "rule", "tier": 1,
                 "heading": "Made-up scoped rule", "outputs": ["chapter", "key moments"], "check_type": "checker",
                 "extends": None, "loads": [], "evidence": None, "beats": None, "v3_first": None, "v3_last": None})
    (t / "rules.json").write_text(json.dumps(live), encoding="utf-8")
    env = dict(os.environ, CG_RULES=str(t / "rules.json"), CG_CHECKERS=str(t / "checkers"))
    run = lambda *a: subprocess.run([sys.executable, str(ROOT / "tools/cg_check.py"), *a], cwd=ROOT, env=env, capture_output=True, text=True)
    r = run("build")
    check(r.returncode == 0, "build with a scoped Tier 1 rule: " + (r.stdout + r.stderr).strip().splitlines()[-1])
    (t / "a.md").write_text("A short letter.\n", encoding="utf-8")
    (t / "c.md").write_text("A short chapter passage.\n", encoding="utf-8")
    r = run("prepare", str(t / "a.md"), "--output", "letter", "--dir", str(t / "p_letter"))
    check(not (t / "p_letter/R1.99.prompt.md").exists(), "prepare: no prompt for a letter")
    v = json.loads((t / "p_letter/R1.99.json").read_text()) if (t / "p_letter/R1.99.json").exists() else {}
    check(v.get("verdict") == "pass" and "out of scope" in v.get("note", ""), "prepare: a letter passes the scoped rule without a call")
    check((t / "p_letter/R1.1.prompt.md").exists(), "prepare: unscoped rules still get a prompt")
    r = run("prepare", str(t / "c.md"), "--output", "chapter-excerpt", "--dir", str(t / "p_ch"))
    check((t / "p_ch/R1.99.prompt.md").exists(), "prepare: a chapter excerpt gets the scoped rule")
    r = run("prepare", str(t / "a.md"), "--output", "letter", "--dir", str(t / "p_ch"))
    check(not (t / "p_ch/R1.99.prompt.md").exists(), "re-prepare as a letter: the old chapter prompt is gone")
    r = run("prepare", str(t / "c.md"), "--output", "chapter", "--dir", str(t / "p_letter"))
    check(not (t / "p_letter/R1.99.json").exists() and (t / "p_letter/R1.99.prompt.md").exists(),
          "re-prepare as a chapter: the old out-of-scope pass is gone, the prompt is there")
    man = [{"id": "A", "output": "letter", "draft": str(t / "a.md")}, {"id": "C", "output": "chapter", "draft": str(t / "c.md")}]
    (t / "man.json").write_text(json.dumps(man), encoding="utf-8")
    r = run("batch", str(t / "man.json"), "--dir", str(t / "b"), "--only", "R1.99")
    prompt = (t / "b/R1.99.prompt.md").read_text() if (t / "b/R1.99.prompt.md").exists() else ""
    check('<draft id="C"' in prompt and '<draft id="A"' not in prompt, "batch: only the chapter goes into the scoped rule's prompt")
    (t / "b/R1.99.json").write_text(json.dumps({"rule": "R1.99", "results": [{"id": "C", "verdict": "fail", "breaks": []}]}))
    r = run("split", str(t / "b"))
    a = json.loads((t / "b/A/R1.99.json").read_text())
    c = json.loads((t / "b/C/R1.99.json").read_text())
    check(a["verdict"] == "pass" and "out of scope" in a.get("note", ""), "split: the letter passes, marked out of scope")
    check(c["verdict"] == "fail", "split: the chapter keeps its answer")

print("\nscope test: " + ("every check passed" if ok else "FAILED"))
sys.exit(0 if ok else 1)
