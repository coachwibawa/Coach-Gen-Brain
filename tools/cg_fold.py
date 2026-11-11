#!/usr/bin/env python3
"""cg_fold.py: the file side of the fold pipeline (Rules Refactor Plan, step 16).

A fold is how a new or changed rule gets into brain.rules. Its stages:
captured, judged, merged, gated (the test set), approved (his go), stored.
One fold file holds one round of feedback: one or more lessons, each of which is
a new rule, a change to a live rule or card, or a rule that leaves.

Rule codes never change. A changed rule keeps its code (R1.7 stays R1.7). The
fold row that carried the change stays in the table as the record.

Commands:
  build SPEC|FOLD            check a fold spec and write rules/folds/<date>_<slug>.json.
                             Prints the proposal (what he must see) and the checkers it touches.
                             Run it again on the fold file after editing its "spec" part
  gate FOLD --dir RUN [--all] [--origin DRAFT --origin-output OUT]
                             the test-set gate with the fold applied: the lint, and one batch
                             prompt per touched Tier 1 checker (--all: every checker).
                             --origin adds the draft the lesson came from. It must fail
  result FOLD --dir RUN      after the helpers saved RUN/<code>.json: join them with the last
                             full run, print each case (expected, got, caught by) and write
                             the gate into the fold file
  approve FOLD [--on DATE]   record his go on the exact text. Only a gated fold can be approved
  decline FOLD N --note "…"  lesson N is out (his words in the note). The rest is rebuilt
  stored FOLD --md5 rulebook=… article=… letter=… chapter=… key_moments=… case_study=…
                             after brain.fold_store: mark it stored, rebuild the live files, check
                             every md5 against the brain's, recompile the cards, rebuild the checkers
  live                       rebuild rules_live.json and rulebook_live.txt from v3 plus the
                             stored folds, and print the md5 values
  status                     every fold file with its stage, for the fold check at a handoff

The brain side (migration 021), both plain selects:
  select * from brain.fold_load('rules/folds/<file>.json');    after build, and again after result
  select * from brain.fold_store('rules/folds/<file>.json');   after approve, on his go only
"""
import argparse, contextlib, copy, datetime, hashlib, io, json, os, re, shutil, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cg_rules  # noqa: E402

ROOT = cg_rules.ROOT
RUNS = ROOT / "tests/rules/runs"
BASE_FILE = RUNS / "BASE"
TEST_SET = ROOT / "tests/rules/test_set.json"
LIVE_TXT = ROOT / "rules/rulebook/rulebook_live.txt"
STAGES = ["captured", "judged", "merged", "gated", "approved", "stored"]
T2_LINE = "- Tier 2 rules loaded:"
BASE_CARDS = {"article": ["article", "letter"], "chapter": ["chapter", "key moments"], "case study": ["case study"]}
MD5_KEYS = {"rulebook": "rulebook", "article": "article", "letter": "letter", "chapter": "chapter",
            "key_moments": "key moments", "case_study": "case study"}


def fail(m):
    sys.exit("FAIL: " + m)


def today():
    return datetime.date.today().isoformat()


def read(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def write(p, data):
    Path(p).write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except ValueError:
        return str(p)


# ---------- the rules as they stand ----------

def fold_files():
    return sorted(cg_rules.FOLDS.glob("*.json")) if cg_rules.FOLDS.exists() else []


def apply_fold(rows, fold):
    """Return the rows with one fold's rows applied (what brain.fold_store does)."""
    rows = copy.deepcopy(rows)
    by = {r["code"]: r for r in rows}
    for fr in fold["rows"]:
        if fr["action"] == "new":
            if fr["code"] in by:
                fail(f"{fr['code']} is already a live rule")
            new = {k: fr[k] for k in ("sort", "body", "code", "kind", "tier", "heading", "outputs", "check_type",
                                      "beats", "extends", "loads")}
            new.update(v3_first=None, v3_last=None, evidence=fr.get("evidence", {}))
            rows.append(new)
            by[new["code"]] = new
        else:
            t = by.get(fr["target"])
            if not t:
                fail(f"{fr['code']}: target {fr['target']} is not a live row")
            if fr["action"] == "change":
                for k in ("heading", "body", "outputs", "check_type", "extends", "loads"):
                    t[k] = copy.deepcopy(fr[k])
            else:
                rows.remove(t)
                del by[fr["target"]]
    return sorted(rows, key=lambda r: r["sort"])


def live_rows():
    """v3 plus every stored fold, in the order they were stored. Never reads rules_live.json."""
    rows = cg_rules.load_rows(cg_rules.V3)
    stored = [read(p) for p in fold_files()]
    stored = sorted((f for f in stored if f.get("stored_on")), key=lambda f: f["stored_seq"])
    for f in stored:
        rows = apply_fold(rows, f)
    return rows, stored


def check_rows(rows):
    """What brain.fold_store checks at the end, plus the text marks."""
    live = {r["code"]: r for r in rows}
    for r in rows:
        if "—" in r["body"] or ";" in r["body"]:
            fail(f"{r['code']}: em dash or semicolon in the rule text")
        if r["kind"] == "card":
            for l in r["loads"]:
                if l not in live or live[l]["tier"] != 2:
                    fail(f"{r['code']} loads {l}, which is not a live Tier 2 rule")
            t2 = [x for x in rows if x["kind"] == "rule" and x["tier"] == 2]
            for line in r["body"].split("\n"):
                if not line.startswith(T2_LINE) or "the chapter card's" in line:
                    continue
                named = []
                for name in [s.strip() for s in line.split(":", 1)[1].strip().rstrip(".").split(",")]:
                    hit = [x["code"] for x in t2 if x["heading"].startswith(name)]
                    if len(hit) != 1:
                        fail(f"{r['code']}: the Tier 2 name '{name}' matches {len(hit)} live rules")
                    named.append(hit[0])
                if named != list(r["loads"]):
                    fail(f"{r['code']}: its Tier 2 line names {named} but it loads {r['loads']}")
    loaded = {l for r in rows if r["kind"] == "card" for l in r["loads"]}
    orphans = [r["code"] for r in rows if r["kind"] == "rule" and r["tier"] == 2 and r["code"] not in loaded]
    if orphans:
        fail("Tier 2 rule on no card, so nothing would load it: " + ", ".join(orphans))
    if len({r["sort"] for r in rows}) != len(rows):
        fail("two rows share a sort value")


def cmd_live(_=None, quiet=False):
    rows, stored = live_rows()
    check_rows(rows)
    md5s = cg_rules.all_md5(rows)
    if stored:
        write(cg_rules.LIVE, {"source": "rules_v3.json plus the stored folds: " + ", ".join(f["fold"] for f in stored),
                              "built_by": "tools/cg_fold.py live", "rulebook_md5": md5s["rulebook"], "rows": rows})
        LIVE_TXT.write_text(cg_rules.rulebook_text(rows), encoding="utf-8")
    else:
        for p in (cg_rules.LIVE, LIVE_TXT):
            if p.exists():
                p.unlink()
    if not quiet:
        t1 = sum(1 for r in rows if r["kind"] == "rule" and r["tier"] == 1)
        print(f"ok: {len(rows)} live rows ({t1} Tier 1 rules), {len(stored)} stored folds"
              + (f", written to {rel(cg_rules.LIVE)}" if stored else ", so the tools read rules_v3.json"))
        for k, v in md5s.items():
            print(f"  {k:12} {v}")
    return rows, md5s


# ---------- build: spec -> fold file ----------

def clean_line(s, what):
    s = s.strip()
    if s.startswith("- "):
        s = s[2:].strip()
    if not s or "\n" in s:
        fail(f"{what}: a rule line is one line of text")
    if "—" in s or ";" in s:
        fail(f"{what}: no em dash and no semicolon in a rule line: {s[:60]}")
    if s.startswith("#"):
        fail(f"{what}: a rule line cannot start with #")
    return s


def body_lines(row):
    return row["body"].split("\n")[1:]


def find_line(lines, wanted, what):
    w = "- " + clean_line(wanted, what)
    hits = [i for i, l in enumerate(lines) if l == w]
    if len(hits) != 1:
        fail(f"{what}: \"{wanted[:60]}\" matches {len(hits)} lines of the rule. Copy the line exactly")
    return hits[0]


def used_codes(rows, skip=None):
    codes = {r["code"] for r in cg_rules.load_rows(cg_rules.V3)} | {r["code"] for r in rows}
    sorts = {r["sort"] for r in rows}
    for p in fold_files():
        f = read(p)
        mine = skip and p.resolve() == Path(skip).resolve()
        for fr in ([] if mine else f["rows"]) + f.get("declined", []):
            codes.add(fr["code"])
            if fr["action"] == "new" and fr.get("sort"):
                sorts.add(fr["sort"])
    return codes, sorts


def next_rule_code(tier, codes):
    n = max([int(c.split(".")[1]) for c in codes if re.fullmatch(rf"R{tier}\.\d+", c)] or [0]) + 1
    return f"R{tier}.{n}"


def free_sort(rows, after_code, taken):
    """A free sort value between a row and the next one. rows: live rows plus the new ones so far."""
    order = sorted(rows, key=lambda r: r["sort"])
    i = next(k for k, r in enumerate(order) if r["code"] == after_code)
    lo, hi = order[i]["sort"], order[i + 1]["sort"]
    cand = [s for s in range(lo + 1, hi) if s not in taken]
    if not cand:
        fail(f"no free place after {after_code}. The sort values there need a new migration to spread them")
    mid = (lo + hi) // 2
    return min(cand, key=lambda s: abs(s - mid))


def evidence(lesson):
    ev = {k: lesson[k] for k in ("his_words", "support", "diagnosis", "why") if lesson.get(k)}
    for q in ev.get("his_words", []):
        if not (q.get("quote") and q.get("on") and q.get("about")):
            fail("each his_words entry needs quote, on (the date) and about (what it was said about)")
    return ev


def set_t2_line(card, rows_by, loads):
    """Rewrite a base card's 'Tier 2 rules loaded' line from its loads."""
    lines = card["body"].split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith(T2_LINE)]
    if len(idx) != 1:
        fail(f"{card['code']}: expected one '{T2_LINE}' line")
    old_names = [s.strip() for s in lines[idx[0]].split(":", 1)[1].strip().rstrip(".").split(",")]
    names = []
    for code in loads:
        r = rows_by[code]
        if r.get("action") == "new":
            short = r.get("short") or r["heading"]
        else:
            short = next((n for n in old_names if r["heading"].startswith(n)), r["heading"])
        names.append(short)
    lines[idx[0]] = f"{T2_LINE} {', '.join(names)}."
    return "\n".join(lines)


def build_rows(spec, rows, path=None):
    by = {r["code"]: r for r in rows}
    cand = copy.deepcopy(by)                    # the state as lessons are applied, for companions
    codes, sorts = used_codes(rows, skip=path)
    date = spec["date"]
    out, card_loads = [], {}                    # card_loads: card code -> new loads, built up across lessons
    order_rows, chain = [{"code": r["code"], "sort": r["sort"]} for r in rows], {}

    def fold_code(target):
        for letter in "abcdefghijklmnopqrstuvwxyz":
            c = f"fold:{target}:{date}{letter}"
            if c not in codes:
                codes.add(c)
                return c
        fail("too many folds on one rule in one day")

    for n, lesson in enumerate(spec["lessons"], start=1):
        if lesson.get("declined"):
            continue
        act = lesson.get("action")
        what = f"lesson {n}"
        ev = evidence(lesson)
        if act == "new":
            tier = lesson.get("tier")
            if tier not in (0, 1, 2):
                fail(f"{what}: a new rule needs tier 0, 1 or 2")
            heading = lesson["heading"].strip()
            if heading in {r["heading"] for r in cand.values() if r["kind"] == "rule"}:
                fail(f"{what}: a live rule is already called \"{heading}\". Change that rule instead")
            lines = [clean_line(l, what) for l in lesson["lines"]]
            if not lines:
                fail(f"{what}: a rule needs at least one line")
            code = lesson.get("code") or next_rule_code(tier, codes)
            codes.add(code)
            lesson["code"] = code
            tier_rows = [r for r in rows if r["kind"] == "rule" and r["tier"] == tier]
            after = lesson.get("after") or max(tier_rows, key=lambda r: r["sort"])["code"]
            if after not in by or by[after]["kind"] != "rule" or by[after]["tier"] != tier:
                fail(f"{what}: 'after' must be a live Tier {tier} rule")
            # a second new rule after the same rule goes after the first new one
            sort = lesson.get("sort") or free_sort(order_rows, chain.get(after, after), sorts)
            chain[after] = code
            order_rows.append({"code": code, "sort": sort})
            sorts.add(sort)
            lesson["sort"] = sort
            short = lesson.get("short")
            if short and not heading.startswith(short):
                fail(f"{what}: 'short' (the name on the cards) must be the start of the heading")
            if tier == 2:
                cards = lesson.get("cards") or []
                if not cards or any(c not in BASE_CARDS for c in cards):
                    fail(f"{what}: a Tier 2 rule names the cards that load it: any of {', '.join(BASE_CARDS)}")
                outputs = [o for o in cg_rules.OUTPUTS if any(o in BASE_CARDS[c] for c in cards)]
                check = lesson.get("check_type", "judgment")
            else:
                cards, outputs = [], lesson.get("outputs") or list(cg_rules.OUTPUTS)
                check = lesson.get("check_type") or ("checker" if tier == 1 else None)
                if check not in ("mechanical", "checker", "judgment"):
                    fail(f"{what}: a Tier 0 rule says its check_type: mechanical (the lint) or checker")
            row = {"lesson": n, "code": code, "action": "new", "target": None, "kind": "rule", "tier": tier,
                   "heading": heading, "body": "### " + heading + "\n" + "\n".join("- " + l for l in lines),
                   "sort": sort, "outputs": outputs, "check_type": check, "extends": None, "loads": [],
                   "beats": lesson.get("beats", []), "evidence": ev}
            if lesson.get("short"):
                row["short"] = lesson["short"]
            out.append(row)
            cand[code] = row
            for c in cards:
                for o in BASE_CARDS[c]:
                    cc = cg_rules.card_code(o)
                    card_loads.setdefault(cc, list(cand[cc]["loads"]))
                    order = sorted(set(card_loads[cc]) | {code}, key=lambda x: cand[x]["sort"])
                    card_loads[cc] = order
        elif act in ("change", "retire"):
            target = lesson.get("target")
            t = cand.get(target)
            if not t or t["kind"] not in ("rule", "card"):
                fail(f"{what}: target {target} is not a live rule or card")
            code = lesson.get("code") or fold_code(target)
            codes.add(code)
            lesson["code"] = code
            base = {"lesson": n, "code": code, "action": act, "target": target, "kind": t["kind"], "tier": t["tier"],
                    "sort": None, "outputs": list(t["outputs"]), "check_type": t["check_type"],
                    "extends": t["extends"], "loads": list(t["loads"]), "beats": [target], "evidence": ev}
            if act == "retire":
                if t["kind"] != "rule":
                    fail(f"{what}: only a rule can be retired")
                if not lesson.get("why"):
                    fail(f"{what}: a retire needs a why")
                out.append(dict(base, heading=t["heading"], body=t["body"], why=lesson["why"]))
                del cand[target]
                if t["tier"] == 2:
                    for cc, c in cand.items():
                        if c["kind"] == "card" and target in card_loads.get(cc, c["loads"]):
                            card_loads[cc] = [x for x in card_loads.get(cc, c["loads"]) if x != target]
                continue
            lines = body_lines(t)
            changed = []
            for x in lesson.get("reword", []):
                i = find_line(lines, x["old"], what)
                if lines[i].startswith(T2_LINE):
                    fail(f"{what}: the Tier 2 line of a card is rebuilt by the tool, never edited")
                lines[i] = "- " + clean_line(x["new"], what)
                changed.append(("reword", x["old"], x["new"]))
            for x in lesson.get("remove", []):
                i = find_line(lines, x, what)
                changed.append(("remove", lines.pop(i)[2:], None))
            for x in lesson.get("add", []):
                new = "- " + clean_line(x["line"], what)
                if new in lines:
                    fail(f"{what}: the rule already has that line")
                if x.get("first"):
                    i = 0
                elif x.get("after"):
                    i = find_line(lines, x["after"], what) + 1
                else:
                    i = len(lines)
                    if t["kind"] == "card" and lines and lines[-1].startswith(T2_LINE):
                        i -= 1
                lines.insert(i, new)
                changed.append(("add", x["line"], x.get("after")))
            heading = (lesson.get("heading") or t["heading"]).strip()
            if not changed and heading == t["heading"]:
                fail(f"{what}: nothing changes. Use add, reword, remove or heading")
            if not lines:
                fail(f"{what}: a rule cannot lose every line. Retire it instead")
            row = dict(base, heading=heading, body="### " + heading + "\n" + "\n".join(lines))
            row["evidence"] = dict(ev, changed=[{"how": h, "line": a, "ref": b} for h, a, b in changed])
            out.append(row)
            cand[target] = dict(t, heading=heading, body=row["body"])
        else:
            fail(f"{what}: action must be new, change or retire")

    # Companion card rows: a Tier 2 rule that arrives or leaves changes the cards that load it.
    for cc, loads in card_loads.items():
        card = cand[cc]
        if loads == list(by[cc]["loads"]) and card["body"] == by[cc]["body"]:
            continue
        body = card["body"]
        if any(l.startswith(T2_LINE) for l in body.split("\n")) and "the chapter card's" not in body:
            body = set_t2_line(dict(card, body=body), cand, loads)
        mine = next((r for r in out if r["action"] == "change" and r["target"] == cc), None)
        if mine:
            mine.update(loads=loads, body=body)
        else:
            out.append({"lesson": 0, "code": fold_code(cc), "action": "change", "target": cc, "kind": "card",
                        "tier": None, "heading": card["heading"], "body": body, "sort": None,
                        "outputs": list(card["outputs"]), "check_type": None, "extends": card["extends"],
                        "loads": loads, "beats": [cc],
                        "evidence": {"why": "The Tier 2 rules this card loads changed in the same fold."}})
    # Rules before cards, so a card never names a rule that is not there yet.
    out.sort(key=lambda r: (r["kind"] == "card", r["lesson"]))
    return out


def touched(fold):
    """Tier 1 checkers whose rule text is new or changed."""
    codes = []
    for fr in fold["rows"]:
        if fr["kind"] == "rule" and fr["tier"] == 1 and fr["action"] in ("new", "change"):
            codes.append(fr["code"] if fr["action"] == "new" else fr["target"])
    return codes


def show(fold, rows):
    by = {r["code"]: r for r in rows}
    print(f"\nProposal: {fold['fold']} ({len([r for r in fold['rows'] if r['lesson']])} lessons). Source: {fold['source']}")
    for fr in fold["rows"]:
        where = "card" if fr["kind"] == "card" else f"Tier {fr['tier']}"
        if fr["action"] == "new":
            print(f"\n[{where}] NEW RULE {fr['code']}: {fr['heading']}")
            print("  placed after: " + next(r["heading"] for r in sorted(rows, key=lambda r: -r["sort"]) if r["sort"] < fr["sort"]))
            for l in body_lines(fr):
                print("  + " + l[2:])
        elif fr["action"] == "retire":
            print(f"\n[{where}] RETIRE {fr['target']}: {fr['heading']}\n  why: {fr['why']}")
        else:
            old = by[fr["target"]]
            print(f"\n[{where}] CHANGE {fr['target']}: {old['heading']}" + (f" -> {fr['heading']}" if fr["heading"] != old["heading"] else ""))
            ol, nl = body_lines(old), body_lines(fr)
            for l in ol:
                if l not in nl:
                    print("  - " + l[2:])
            for l in nl:
                if l not in ol:
                    print("  + " + l[2:])
            if old["loads"] != fr["loads"]:
                print(f"  loads: {', '.join(old['loads'])} -> {', '.join(fr['loads'])}")
    t = touched(fold)
    print("\nCheckers this fold touches: " + (", ".join(t) if t else "none (no Tier 1 rule text changes)"))
    t0 = [fr for fr in fold["rows"] if fr["kind"] == "rule" and fr["tier"] == 0 and fr["check_type"] == "mechanical"]
    if t0:
        print("Tier 0 mechanical rule changed: make tools/cg_lint.py match before the gate (" + ", ".join(fr["target"] or fr["code"] for fr in t0) + ").")


def cmd_build(a):
    src = read(a.spec)
    is_fold = "rows" in src and "spec" in src
    spec = src["spec"] if is_fold else src
    if is_fold and src.get("approved_on"):
        fail("this fold is approved. Its text is frozen. A further change is a new fold")
    for k in ("slug", "source", "lessons"):
        if not spec.get(k):
            fail(f"the spec needs {k}")
    if not re.fullmatch(r"[a-z0-9-]+", spec["slug"]):
        fail("slug: lower-case letters, digits and hyphens")
    spec.setdefault("date", today())
    stage = spec.get("stage", "merged")
    if stage not in STAGES[:3]:
        fail("spec stage is captured, judged or merged. The gate and his go set the later stages")
    rows, _ = live_rows()
    name = f"{spec['date']}_{spec['slug']}"
    path = cg_rules.FOLDS / f"{name}.json"
    if path.exists() and not is_fold:
        old = read(path)
        if old.get("approved_on"):
            fail(f"{rel(path)} is approved. Use a new slug for a new fold")
        # keep the codes the first build gave, so rows already in the brain keep their identity
        for new, was in zip(spec["lessons"], old["spec"]["lessons"]):
            same = all(new.get(k) == was.get(k) for k in ("action", "target", "tier")) and \
                (new.get("action") != "new" or new.get("heading") == was.get("heading"))
            for k in ("code", "sort"):
                if same and was.get(k) and not new.get(k):
                    new[k] = was[k]
    declined = src.get("declined", []) if is_fold else (read(path).get("declined", []) if path.exists() else [])
    out = build_rows(spec, rows, path)
    if not out:
        fail("no lesson left to fold")
    for r in out:
        r["fold_stage"], r["test_gate"] = stage, None
    fold = {"fold": name, "source": spec["source"], "added_on": spec["date"],
            "added_by": spec.get("added_by", "propose-language-rule"), "approved_on": None,
            "stored_on": None, "stored_seq": None, "spec": spec, "declined": declined, "rows": out}
    cand = apply_fold(rows, fold)
    check_rows(cand)
    cg_rules.FOLDS.mkdir(parents=True, exist_ok=True)
    write(path, fold)
    show(fold, rows)
    print(f"\nok: {rel(path)}, stage {stage}. Commit and push, then: select * from brain.fold_load('{rel(path)}');")


# ---------- the gate ----------

def base_dir():
    name = BASE_FILE.read_text(encoding="utf-8").strip() if BASE_FILE.exists() else "fresh_2026-11-11"
    return RUNS / name


def run_env(run):
    return dict(os.environ, CG_RULES=str(run / "rules_candidate.json"), CG_CHECKERS=str(run / "checkers"))


def sh(cmd, env=None):
    p = subprocess.run([sys.executable] + cmd, cwd=ROOT, env=env, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def cmd_gate(a):
    fold = read(a.fold)
    if fold.get("approved_on"):
        fail("this fold is already approved")
    run = Path(a.dir).resolve()
    if RUNS.resolve() not in run.parents:
        fail(f"--dir must be a folder under {rel(RUNS)}, so the run can be committed and become the next base")
    run.mkdir(parents=True, exist_ok=True)
    (run / ".gitignore").write_text("*.prompt.md\nsrc/\n*/draft.md\ncheckers/\nrules_candidate.json\n", encoding="utf-8")
    rows, _ = live_rows()
    cand = apply_fold(rows, fold)
    check_rows(cand)
    write(run / "rules_candidate.json", {"rows": cand})
    env = run_env(run)
    code, outp = sh(["tests/rules/run_lint_on_testset.py"])
    print("lint on the test set: " + outp.splitlines()[-1])
    if code:
        fail("the lint no longer gives the expected result on the test set. Fix tools/cg_lint.py first:\n" + outp)
    code, outp = sh(["tools/cg_check.py", "build"], env)
    if code:
        fail(outp)
    t1 = [r["code"] for r in cand if r["kind"] == "rule" and r["tier"] == 1]
    rerun = t1 if a.all else touched(fold)
    cases = {c["id"]: c for c in read(TEST_SET)["cases"]}
    man = [dict(m) for m in read(base_dir() / "manifest.json") if m["id"] != "ORIGIN"]
    (run / "src").mkdir(exist_ok=True)
    for m in man:
        p = run / "src" / f"{m['id']}.md"
        p.write_text(cases[m["id"]]["text"].strip() + "\n", encoding="utf-8")
        m["draft"] = str(p)
    if a.origin:
        if not a.origin_output:
            fail("--origin needs --origin-output (article, letter, chapter, chapter-excerpt, key-moments or case-study)")
        if not touched(fold):
            fail("--origin tests a Tier 1 rule. This fold changes none")
        p = run / "src" / "ORIGIN.md"
        shutil.copyfile(a.origin, p)
        man.append({"id": "ORIGIN", "output": a.origin_output, "draft": str(p)})
    write(run / "manifest_in.json", man)
    meta = {"fold": fold["fold"], "rerun": rerun, "all": bool(a.all), "base": None if a.all else base_dir().name,
            "origin": bool(a.origin), "body_md5": {r["code"]: cg_rules.md5(r["body"]) for r in fold["rows"]}}
    write(run / "gate.json", meta)
    if not rerun:
        print("No Tier 1 rule text changes, so no checker is rerun. Next: cg_fold.py result FOLD --dir " + rel(run))
        return
    # Keep an answer only when it was given to this exact prompt.
    old = {p.name: cg_rules.md5(p.read_text(encoding="utf-8")) for p in run.glob("R1.*.prompt.md")}
    code, outp = sh(["tools/cg_check.py", "batch", str(run / "manifest_in.json"), "--dir", str(run), "--only", ",".join(rerun)], env)
    if code:
        fail(outp)
    todo = []
    for c in rerun:
        p, ans = run / f"{c}.prompt.md", run / f"{c}.json"
        if ans.exists() and old.get(p.name) == cg_rules.md5(p.read_text(encoding="utf-8")):
            continue
        if ans.exists():
            ans.unlink()
        todo.append(c)
    for stale in run.glob("R1.*.json"):
        if stale.stem not in rerun:
            stale.unlink()
    print(f"ok: gate ready in {rel(run)}. {len(man)} drafts, checkers to run: {', '.join(todo) or 'none (all answers kept)'}")
    for c in todo:
        print(f"  one Sonnet helper reads {rel(run / (c + '.prompt.md'))} and saves its JSON answer as {rel(run / (c + '.json'))}")
    print(f"Then: python3 tools/cg_fold.py result {rel(a.fold)} --dir {rel(run)}")


def cmd_result(a):
    fold = read(a.fold)
    run = Path(a.dir).resolve()
    meta = read(run / "gate.json")
    if meta["body_md5"] != {r["code"]: cg_rules.md5(r["body"]) for r in fold["rows"]}:
        fail("the fold text changed after this gate was prepared. Run gate again")
    env = run_env(run)
    missing = [c for c in meta["rerun"] if not (run / f"{c}.json").exists()]
    if missing:
        fail("no answer yet from: " + ", ".join(missing))
    man = read(run / "manifest_in.json")
    for m in man:
        (run / m["id"]).mkdir(exist_ok=True)
        shutil.copyfile(m["draft"], run / m["id"] / "draft.md")
        (run / m["id"] / "output.txt").write_text(m["output"] + "\n", encoding="utf-8")
    write(run / "manifest.json", [{k: m[k] for k in ("id", "output")} for m in man])
    if meta["rerun"]:
        code, outp = sh(["tools/cg_check.py", "split", str(run)], env)
        if code:
            fail(outp)
    cand = read(run / "rules_candidate.json")["rows"]
    heads = {r["code"]: r["heading"] for r in cand if r["kind"] == "rule" and r["tier"] == 1}
    base = RUNS / meta["base"] if meta["base"] else None
    os.environ.update(CG_RULES=env["CG_RULES"], CG_CHECKERS=env["CG_CHECKERS"])
    import cg_check
    rows_out, wrong, caught_by = [], 0, {}
    for m in man:
        d = run / m["id"]
        if m["id"] == "ORIGIN":
            who = [c for c in meta["rerun"] if cg_check.parse_verdict((d / f"{c}.json").read_text(encoding="utf-8"), c)["verdict"] == "fail"]
            who = [c for c in who if c in touched(fold)]
            got, exp = ("fail" if who else "pass"), "fail"
        else:
            for c in heads:
                if c in meta["rerun"]:
                    continue
                src = base / m["id"] / f"{c}.json" if base else None
                if not src or not src.exists():
                    fail(f"no earlier answer for {c} on {m['id']}. Run the gate with --all")
                shutil.copyfile(src, d / f"{c}.json")
            for stale in d.glob("R1.*.json"):
                if stale.stem not in heads:
                    stale.unlink()
            with contextlib.redirect_stdout(io.StringIO()):
                res = cg_check.cmd_collect(argparse.Namespace(dir=str(d), draft=None, output=None))
            rep = read(d / "report.json")
            who = (["lint"] if rep["lint"] else []) + [v["rule"] for v in rep["checkers"] if v["verdict"] == "fail"]
            got, exp = res.lower(), ("fail" if m["id"].startswith("F") else "pass")
        ok = got == exp
        wrong += not ok
        caught_by[m["id"]] = who
        rows_out.append((m["id"], exp, got, "ok" if ok else "WRONG", ", ".join(w if w == "lint" else f"{w} {heads.get(w, '')}".strip() for w in who) or "-"))
    fails = sum(1 for m in man if m["id"].startswith("F"))
    passes = sum(1 for m in man if m["id"].startswith("P"))
    print(f"Gate for {fold['fold']}: {len(man) - wrong} of {len(man)} cases as expected.")
    print("Checkers rerun: " + (", ".join(meta["rerun"]) or "none") + (f". The rest from {meta['base']}." if meta["base"] else "."))
    print(f"{'Case':7} {'Expected':9} {'Got':11} {'':6} Caught by")
    for r in rows_out:
        print(f"{r[0]:7} {r[1]:9} {r[2]:11} {r[3]:6} {r[4]}")
    if wrong:
        print("\nGATE FAILED. Either the wording is wrong, or a checker misreads the rule. For a misread, add a note to "
              "rules/checkers/calibration.json that names the case and comes from his verdict on it, then run gate "
              "again and rerun that checker twice. A note never changes rule text.")
        sys.exit(1)
    gate = {"on": today(), "run": rel(run), "base": meta["base"], "rerun": meta["rerun"],
            "fails_caught": f"{fails} of {fails}", "passes_kept": f"{passes} of {passes}", "lint": "all as expected",
            "caught_by": {k: v for k, v in caught_by.items() if v}}
    for r in fold["rows"]:
        r["fold_stage"], r["test_gate"] = "gated", gate
    write(a.fold, fold)
    print(f"\nok: gated. Commit and push, then: select * from brain.fold_load('{rel(a.fold)}');")


# ---------- his go, and after ----------

def cmd_approve(a):
    fold = read(a.fold)
    if any(r["fold_stage"] != "gated" or not r["test_gate"] for r in fold["rows"]):
        fail("only a gated fold can be approved. Run gate and result first")
    fold["approved_on"] = a.on or today()
    for r in fold["rows"]:
        r["fold_stage"] = "approved"
    write(a.fold, fold)
    print(f"ok: approved on {fold['approved_on']}. Commit and push, then, on his go only:\n"
          f"  select * from brain.fold_store('{rel(a.fold)}');")


def cmd_decline(a):
    fold = read(a.fold)
    if fold.get("approved_on"):
        fail("this fold is approved. Its text is frozen")
    lessons = fold["spec"]["lessons"]
    if not 1 <= a.lesson <= len(lessons) or lessons[a.lesson - 1].get("declined"):
        fail(f"no open lesson {a.lesson}")
    lessons[a.lesson - 1]["declined"] = {"on": today(), "note": a.note}
    gone = [dict(r, declined={"on": today(), "note": a.note}) for r in fold["rows"] if r["lesson"] == a.lesson]
    fold["declined"] = fold.get("declined", []) + gone
    fold["rows"] = [r for r in fold["rows"] if r["lesson"] != a.lesson]
    write(a.fold, fold)
    print("Declined: " + ", ".join(r["code"] for r in gone))
    for r in gone:
        print(f"  in the brain, if it was loaded: select brain.fold_decline('{r['code']}', '{a.note.replace(chr(39), chr(39) * 2)}');")
    if any(not l.get("declined") for l in lessons):
        cmd_build(argparse.Namespace(spec=a.fold))
    else:
        print("No lesson left in this fold.")


def cmd_stored(a):
    fold = read(a.fold)
    if not fold.get("approved_on"):
        fail("not approved")
    if fold.get("stored_on"):
        fail("already marked stored")
    brain = {}
    for kv in a.md5:
        k, v = kv.split("=", 1)
        if k not in MD5_KEYS:
            fail(f"unknown md5 key {k}. Use: " + ", ".join(MD5_KEYS))
        brain[MD5_KEYS[k]] = v.strip()
    if set(brain) != set(MD5_KEYS.values()):
        fail("give all six md5 values that brain.fold_store returned: " + ", ".join(MD5_KEYS))
    before = Path(a.fold).read_text(encoding="utf-8")
    seqs = [read(p).get("stored_seq") or 0 for p in fold_files()]
    fold["stored_on"], fold["stored_seq"] = today(), max(seqs + [0]) + 1
    for r in fold["rows"]:
        r["fold_stage"] = "stored"
    write(a.fold, fold)
    rows, mine = cmd_live(quiet=True)
    bad = [k for k in brain if brain[k] != mine[k]]
    if bad:
        Path(a.fold).write_text(before, encoding="utf-8")
        cmd_live(quiet=True)
        fail("the repo and the brain disagree on: " + ", ".join(bad) + ". Nothing was marked stored. "
             "Compare select brain.rulebook_text() with a rebuild before going on")
    print("ok: the live files equal the brain (rulebook and all five cards, md5 for md5)")
    args = ["rules/table/compile_cards.py", "rules/table/cards", "--brain-md5"] + [f"{k}={brain[v]}" for k, v in MD5_KEYS.items() if k != "rulebook"]
    code, outp = sh(args)
    print(outp.splitlines()[-1])
    if code:
        fail(outp)
    code, outp = sh(["tools/cg_check.py", "build"])
    print(outp.splitlines()[0])
    if code:
        fail(outp)
    gate = fold["rows"][0]["test_gate"] or {}
    run = ROOT / gate["run"] if gate.get("run") else None
    if run and (run / "manifest.json").exists() and (gate.get("rerun") or gate.get("base") is None):
        BASE_FILE.write_text(run.name + "\n", encoding="utf-8")
        print(f"the next gate builds on {run.name}")
    print("Now: copy rules/table/cards/Card_*.md to the project (claude/cards/) and to his Mac (Book/Rule Cards/), "
          "then commit and push.")


def cmd_status(_):
    files = fold_files()
    if not files:
        print("no folds yet")
    for p in files:
        f = read(p)
        stage = "stored " + f["stored_on"] if f.get("stored_on") else (f["rows"][0]["fold_stage"] if f["rows"] else "all declined")
        print(f"{f['fold']:40} {stage:18} {len(f['rows'])} rows, {len(f.get('declined', []))} declined. {f['source'][:70]}")
        for r in f["rows"]:
            print(f"    {r['action']:6} {r['target'] or r['code']:16} {r['heading']}")
        for r in f.get("declined", []):
            print(f"    declined {r['target'] or r['code']:13} {r['heading']}: {r['declined']['note'][:60]}")
    print("In the brain: select code, heading, fold_stage, status, source from brain.rules "
          "where fold_stage <> 'stored' or code like 'fold:%' order by added_at;")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("spec")
    g = sub.add_parser("gate")
    g.add_argument("fold")
    g.add_argument("--dir", required=True)
    g.add_argument("--all", action="store_true")
    g.add_argument("--origin")
    g.add_argument("--origin-output")
    r = sub.add_parser("result")
    r.add_argument("fold")
    r.add_argument("--dir", required=True)
    ap_ = sub.add_parser("approve")
    ap_.add_argument("fold")
    ap_.add_argument("--on")
    d = sub.add_parser("decline")
    d.add_argument("fold")
    d.add_argument("lesson", type=int)
    d.add_argument("--note", required=True)
    s = sub.add_parser("stored")
    s.add_argument("fold")
    s.add_argument("--md5", nargs="+", required=True)
    sub.add_parser("live")
    sub.add_parser("status")
    a = ap.parse_args()
    {"build": cmd_build, "gate": cmd_gate, "result": cmd_result, "approve": cmd_approve, "decline": cmd_decline,
     "stored": cmd_stored, "live": cmd_live, "status": cmd_status}[a.cmd](a)


if __name__ == "__main__":
    main()
