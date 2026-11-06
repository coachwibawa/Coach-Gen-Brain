#!/usr/bin/env python3
"""cg_check.py: the one-rule checkers (Rules Refactor Plan, step 12).

One short prompt per Tier 1 rule (20 in v3). Each checker reads the whole draft
against its one rule and returns pass or fail, with the lines that break it.
The rule text comes from the rules table data (rules/table/rules_v3.json, the
file loaded into brain.rules), so a checker never drifts from the rulebook.

Commands:
  build                          write rules/checkers/<code>.md, one template per Tier 1 rule
  prepare DRAFT --output OUT --dir DIR
                                 fill the 20 templates with one draft, ready to run
  run DIR [--model M]            run them in parallel through the Anthropic API
                                 (needs ANTHROPIC_API_KEY). Writes DIR/<code>.json
  batch MANIFEST --dir DIR       one prompt per rule carrying many drafts (calibration).
                                 MANIFEST is JSON: [{"id", "output", "draft" (path)}]
  split DIR                      split DIR/<code>.json batch answers into DIR/<id>/<code>.json
  collect DIR [--draft DRAFT --output OUT]
                                 read DIR/<code>.json (from run, or from helpers in a chat),
                                 add the lint (tools/cg_lint.py), print one report
Without an API key, a chat runs each DIR/<code>.prompt.md with a Sonnet helper and saves
the JSON it returns as DIR/<code>.json, then calls collect.

Verdict of the draft: FAIL if the lint has a break or any checker fails, else PASS.
Tier 2 is never checked here.
"""
import argparse, concurrent.futures, hashlib, json, os, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOAD = ROOT / "rules/table/rules_v3.json"
TPL_DIR = ROOT / "rules/checkers"
OUTPUTS = {"article": "an article (Inside The Introvert)", "letter": "a letter (Lasting Change Letters)",
           "chapter": "a passage from a chapter of his book, 5 Laws of Lasting Change",
           "key-moments": "a key moment from a chapter of his book", "case-study": "a case study for his book"}

TEMPLATE = """You check one draft against ONE rule from Coach Gen's writing rulebook. Check nothing else. Other checkers cover the other rules, the marks and the spelling.

Coach Gen is a coach for introverts. He writes in plain, vivid English for readers who were not in the room, many of whom read English as a second language. The draft below is {{OUTPUT}}.

What fail means. This rule is Tier 1: a real break of it fails the whole draft. A real break is a place where a careful reader loses something because of this rule: they are confused, lose the thread, have to guess, stop trusting the writer, or feel the writing is off. Do not fail the draft for polish, for taste, for a line you would only phrase differently, for grammar or spelling slips, or for something a different rule covers. Fail when you can point to the words and say what the reader loses there.

How to judge.
- Read the whole draft first. Judge the draft as a whole, not one line at a time. A rule can break across paragraphs.
- Judge only what is on the page. Some lines of the rule are about how the writer works or about parts this draft may not include (a grey line at the top, an end note, a list made before drafting). If the draft does not include that part, skip those lines and judge the prose.
- Lines in bold with "Insight" are field headings, not prose. Skip them.
- Quote the draft's own words exactly.

The rule ({{CODE}}):
<rule>
{{RULE}}
</rule>

Answer with JSON only, no other text:
{"rule": "{{CODE}}", "verdict": "pass" or "fail", "breaks": [{"quote": "exact words from the draft, at most 25", "why": "one plain sentence: what the reader loses here"}]}
"breaks" is empty for a pass. For a fail, give at most 3, the worst first.

<draft>
{{DRAFT}}
</draft>
"""


def fail(m):
    sys.exit("FAIL: " + m)


def tier1():
    rows = json.loads(LOAD.read_text(encoding="utf-8"))["rows"]
    t1 = [r for r in rows if r["kind"] == "rule" and r["tier"] == 1]
    if len(t1) != 20:
        fail(f"expected 20 Tier 1 rules, found {len(t1)}")
    return t1


def cmd_build(_):
    TPL_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []
    for r in tier1():
        body = r["body"]
        tpl = TEMPLATE.replace("{{CODE}}", r["code"]).replace("{{RULE}}", body)
        if body not in tpl:
            fail(r["code"] + ": rule text not carried word for word")
        if "—" in tpl or ";" in TEMPLATE:
            fail("em dash or semicolon in the template")
        (TPL_DIR / f"{r['code']}.md").write_text(tpl, encoding="utf-8")
        manifest.append({"code": r["code"], "heading": r["heading"], "v3_lines": [r["v3_first"], r["v3_last"]],
                         "rule_md5": hashlib.md5(body.encode()).hexdigest(), "tokens_est": round(len(tpl) / 4)})
    (TPL_DIR / "checkers.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"ok: {len(manifest)} checker templates in {TPL_DIR.relative_to(ROOT)}, each carries its rule word for word")
    for m in manifest:
        print(f"  {m['code']:6} {m['heading']:38} ~{m['tokens_est']} tokens before the draft")


def cmd_prepare(a):
    draft = Path(a.draft).read_text(encoding="utf-8").strip()
    out = Path(a.dir)
    out.mkdir(parents=True, exist_ok=True)
    for f in sorted(TPL_DIR.glob("R1.*.md"), key=lambda p: int(p.stem.split(".")[1])):
        text = f.read_text(encoding="utf-8").replace("{{OUTPUT}}", OUTPUTS[a.output]).replace("{{DRAFT}}", draft)
        (out / f"{f.stem}.prompt.md").write_text(text, encoding="utf-8")
    (out / "draft.md").write_text(draft + "\n", encoding="utf-8")
    (out / "output.txt").write_text(a.output + "\n", encoding="utf-8")
    print(f"ok: 20 prompts in {out}")


def parse_verdict(raw, code):
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        return {"rule": code, "verdict": "error", "breaks": [], "raw": raw[:300]}
    try:
        v = json.loads(m.group(0))
    except json.JSONDecodeError:
        return {"rule": code, "verdict": "error", "breaks": [], "raw": raw[:300]}
    v["rule"] = code
    if v.get("verdict") not in ("pass", "fail"):
        v["verdict"] = "error"
    v.setdefault("breaks", [])
    return v


def cmd_run(a):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        fail("no ANTHROPIC_API_KEY. In a chat, run each .prompt.md with a Sonnet helper instead")
    d = Path(a.dir)
    prompts = sorted(d.glob("R1.*.prompt.md"))

    def one(p):
        code = p.name.split(".prompt")[0]
        body = json.dumps({"model": a.model, "max_tokens": 800, "temperature": 0,
                           "messages": [{"role": "user", "content": p.read_text(encoding="utf-8")}]}).encode()
        req = urllib.request.Request(os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com") + "/v1/messages", body,
                                     {"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
        with urllib.request.urlopen(req, timeout=180) as r:
            raw = "".join(c.get("text", "") for c in json.load(r)["content"])
        v = parse_verdict(raw, code)
        (d / f"{code}.json").write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
        return code, v["verdict"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
        for code, verdict in ex.map(one, prompts):
            print(f"  {code}: {verdict}")


BATCH_HEAD = """You check several drafts against ONE rule from Coach Gen's writing rulebook. Check nothing else. Other checkers cover the other rules, the marks and the spelling.

Judge each draft on its own, as if it were the only one you had seen. Never compare drafts with each other, and never let one draft change your bar for another.

Coach Gen is a coach for introverts. He writes in plain, vivid English for readers who were not in the room, many of whom read English as a second language. Each draft says what it is (an article, a letter, a book passage or a case study).
"""


def batch_prompt(code, body, drafts):
    one = TEMPLATE.split("What fail means.", 1)[1].split("Answer with JSON only", 1)[0]
    parts = [BATCH_HEAD, "What fail means." + one.replace("({{CODE}})", f"({code})").replace("{{RULE}}", body)]
    parts.append("""Answer with JSON only, no other text:
{"rule": "%s", "results": [{"id": "the draft's id", "verdict": "pass" or "fail", "breaks": [{"quote": "exact words from that draft, at most 25", "why": "one plain sentence: what the reader loses here"}]}]}
One result per draft, in the order given. "breaks" is empty for a pass. For a fail, give at most 3, the worst first.
""" % code)
    for d in drafts:
        parts.append(f'<draft id="{d["id"]}" kind="{OUTPUTS[d["output"]]}">\n{d["text"]}\n</draft>\n')
    return "\n".join(parts)


def cmd_batch(a):
    man = json.loads(Path(a.manifest).read_text(encoding="utf-8"))
    for d in man:
        d["text"] = Path(d["draft"]).read_text(encoding="utf-8").strip()
    out = Path(a.dir)
    out.mkdir(parents=True, exist_ok=True)
    for r in tier1():
        (out / f"{r['code']}.prompt.md").write_text(batch_prompt(r["code"], r["body"], man), encoding="utf-8")
    for d in man:
        sub = out / d["id"]
        sub.mkdir(exist_ok=True)
        (sub / "draft.md").write_text(d["text"] + "\n", encoding="utf-8")
        (sub / "output.txt").write_text(d["output"] + "\n", encoding="utf-8")
    (out / "manifest.json").write_text(json.dumps([{k: d[k] for k in ("id", "output")} for d in man], indent=1), encoding="utf-8")
    print(f"ok: 20 batch prompts for {len(man)} drafts in {out}")


def cmd_split(a):
    d = Path(a.dir)
    ids = [m["id"] for m in json.loads((d / "manifest.json").read_text(encoding="utf-8"))]
    for r in tier1():
        p = d / f"{r['code']}.json"
        if not p.exists():
            print(f"  missing {p.name}")
            continue
        raw = p.read_text(encoding="utf-8")
        m = re.search(r"\{.*\}", raw, re.S)
        got = {x.get("id"): x for x in json.loads(m.group(0)).get("results", [])} if m else {}
        for i in ids:
            v = got.get(i, {"verdict": "error", "breaks": [], "raw": "no result for this draft"})
            v = dict(v, rule=r["code"])
            (d / i / f"{r['code']}.json").write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"ok: split into {len(ids)} draft folders")


def cmd_collect(a):
    d = Path(a.dir)
    heads = {m["code"]: m["heading"] for m in json.loads((TPL_DIR / "checkers.json").read_text(encoding="utf-8"))}
    draft = Path(a.draft) if a.draft else d / "draft.md"
    output = a.output or ((d / "output.txt").read_text().strip() if (d / "output.txt").exists() else None)
    sys.path.insert(0, str(ROOT / "tools"))
    from cg_lint import lint
    findings, st = lint(draft.read_text(encoding="utf-8"), output)
    lint_breaks = [f for f in findings if f["level"] in ("FAIL", "FORM")]
    verdicts, missing = [], []
    for code in heads:
        p = d / f"{code}.json"
        if not p.exists():
            missing.append(code)
            continue
        verdicts.append(parse_verdict(p.read_text(encoding="utf-8"), code))
    fails = [v for v in verdicts if v["verdict"] == "fail"]
    errors = [v for v in verdicts if v["verdict"] == "error"]
    result = "FAIL" if (lint_breaks or fails) else ("INCOMPLETE" if (missing or errors) else "PASS")
    print(f"{result}: lint {len(lint_breaks)} breaks, checkers {len(fails)} of {len(verdicts)} fail"
          + (f", {len(missing)} missing" if missing else "") + (f", {len(errors)} unreadable" if errors else "")
          + f". {st['words']} words, reading grade {st['reading_grade']}")
    for f in lint_breaks:
        print(f"  lint  {f['rule']}: {f['msg']}  [{f['excerpt'][:70]}]")
    for v in fails:
        print(f"  {v['rule']:6} {heads[v['rule']]}")
        for b in v["breaks"][:3]:
            print(f"         \"{b.get('quote', '')[:110]}\"\n         {b.get('why', '')}")
    if missing:
        print("  missing: " + ", ".join(missing))
    report = {"result": result, "stats": st, "lint": lint_breaks, "checkers": verdicts, "missing": missing}
    (d / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    p = sub.add_parser("prepare")
    p.add_argument("draft")
    p.add_argument("--output", required=True, choices=list(OUTPUTS))
    p.add_argument("--dir", required=True)
    r = sub.add_parser("run")
    r.add_argument("dir")
    r.add_argument("--model", default="claude-sonnet-5-5")
    b = sub.add_parser("batch")
    b.add_argument("manifest")
    b.add_argument("--dir", required=True)
    sp = sub.add_parser("split")
    sp.add_argument("dir")
    c = sub.add_parser("collect")
    c.add_argument("dir")
    c.add_argument("--draft")
    c.add_argument("--output")
    a = ap.parse_args()
    {"build": cmd_build, "prepare": cmd_prepare, "run": cmd_run, "batch": cmd_batch, "split": cmd_split,
     "collect": cmd_collect}[a.cmd](a)


if __name__ == "__main__":
    main()
