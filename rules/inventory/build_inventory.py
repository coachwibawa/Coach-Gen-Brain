#!/usr/bin/env python3
"""Step 6 of the Rules Refactor Plan: validate the rule inventory and render it.

Reads inventory.psv, targets.psv and clashes.psv (pipe-separated, first row is
the header). Checks every row, then writes inventory.json and INVENTORY.md.
Source hashes are read from archive/pre-prune so the inventory names the exact
bytes it was built from. Run from anywhere: python3 rules/inventory/build_inventory.py
"""
import hashlib, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
ARCH = REPO / "archive" / "pre-prune"

SOURCES = {
    "LR": ("Coach_Gen_Language_Rules.md (project)", "project-docs/Coach_Gen_Language_Rules.md"),
    "BR": ("Book Rules: Mac master Book/Coach_Gen_Book_Rules.md = project mirror", "project-docs/claude/Coach_Gen_Book_Rules.md"),
    "GR": ("Guardrails.md (project)", "project-docs/Guardrails.md"),
    "PD": ("claude/Coach_Gen_Protected_Docs.md", "project-docs/claude/Coach_Gen_Protected_Docs.md"),
    "CR": ("claude/Coach_Gen_Content_Rules.md", "project-docs/claude/Coach_Gen_Content_Rules.md"),
    "SP": ("claude/Coach_Gen_Social_Posting_Rules.md", "project-docs/claude/Coach_Gen_Social_Posting_Rules.md"),
    "RS": ("claude/Reel_Style_Guide.md", "project-docs/claude/Reel_Style_Guide.md"),
    "BV": ("brand/02_VOICE.md", "project-docs/brand/02_VOICE.md"),
    "BT": ("brand/90_TASTE.md", "project-docs/brand/90_TASTE.md"),
    "BS": ("Book/Book_Status.md (Mac, ownership ledger)", None),
    "WS": ("skill coach-gen-writer", "skills/coach-gen-writer/SKILL.md"),
    "PL": ("skill propose-language-rule", "skills/propose-language-rule/SKILL.md"),
    "FL": ("skill fold-article-lessons (already uninstalled)", "skills/fold-article-lessons/SKILL.md"),
    "WB": ("skill write-book-from-material (decision 3: goes)", "skills/write-book-from-material_SKILL.md.from-transcript"),
    "PI": ("project instructions (project settings)", None),
    "MA": ("memory /preferences.md (account)", "memory/preferences.md"),
    "MP": ("memory preferences.md (project)", "memory/projects/01a004af-f98d-75a0-82ee-b053384bfff1/preferences.md"),
    "MW": ("memory ways-of-working.md (project)", "memory/projects/01a004af-f98d-75a0-82ee-b053384bfff1/ways-of-working.md"),
    "MF": ("memory framework-principles.md (project)", "memory/projects/01a004af-f98d-75a0-82ee-b053384bfff1/framework-principles.md"),
    "OS": ("other skills that restate rules", None),
    "Book_Writing_Handoff": ("claude/Book_Writing_Handoff.md (case study objective, open R41)", "project-docs/claude/Book_Writing_Handoff.md"),
}
KINDS = {"rule", "process", "ref", "meta", "history", "open"}
TIERS = {"0", "1", "2", "-"}
CHECKS = {"mech", "checker", "judge", "-"}
ACTIONS = {"keep", "merge", "cut", "move", "out", "open"}
OUT_LABELS = {"social", "reel", "brand", "content", "other", "-"}
OUT_NAMES = {"A": "article", "L": "letter", "C": "chapter", "K": "key moments", "S": "case study"}


def read_psv(name):
    lines = (HERE / name).read_text(encoding="utf-8").splitlines()
    head = lines[0].split("|")
    rows = []
    for n, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        cells = line.split("|")
        if len(cells) != len(head):
            sys.exit(f"{name} line {n}: {len(cells)} fields, expected {len(head)}: {line[:80]}")
        rows.append(dict(zip(head, cells)))
    return rows


def main():
    rows = read_psv("inventory.psv")
    targets = read_psv("targets.psv")
    clashes = read_psv("clashes.psv")
    tids = {t["id"] for t in targets}
    errors = []
    seen = set()
    for r in rows:
        rid = r["id"]
        if rid in seen:
            errors.append(f"duplicate id {rid}")
        seen.add(rid)
        if r["src"] not in SOURCES:
            errors.append(f"{rid}: unknown source {r['src']}")
        if r["kind"] not in KINDS:
            errors.append(f"{rid}: kind {r['kind']}")
        if r["tier"] not in TIERS:
            errors.append(f"{rid}: tier {r['tier']}")
        if r["check"] not in CHECKS:
            errors.append(f"{rid}: check {r['check']}")
        if r["action"] not in ACTIONS:
            errors.append(f"{rid}: action {r['action']}")
        out = r["out"]
        if out not in OUT_LABELS and not re.fullmatch(r"[ALCKS]+", out):
            errors.append(f"{rid}: outputs {out}")
        if r["target"] != "-" and r["target"] not in tids:
            errors.append(f"{rid}: target {r['target']} not in targets.psv")
        # a row placed in a tiered rule must carry a tier and a check type
        if r["target"].startswith("T") and r["action"] in ("keep", "merge"):
            if r["tier"] == "-" or r["check"] == "-":
                errors.append(f"{rid}: placed in {r['target']} without tier or check")
            if r["tier"] != "-" and r["target"][1] != r["tier"]:
                errors.append(f"{rid}: tier {r['tier']} placed in {r['target']}")
        if r["action"] in ("keep", "merge") and r["target"] == "-":
            errors.append(f"{rid}: {r['action']} with no target")
        if r["action"] == "out" and not r["target"].startswith("out:"):
            errors.append(f"{rid}: out of scope but target {r['target']}")
        if "—" in "".join(r.values()) or ";" in "".join(r.values()):
            errors.append(f"{rid}: em dash or semicolon in the row")
    for c in clashes:
        for ref in re.findall(r"\b([A-Z]{2,3}-[\w.]+)", c["one side"] + " " + c["other side"]):
            ref = ref.rstrip(".,")
            if ref not in seen and not ref.startswith(("BR-R3b", "BR-R3m")):
                errors.append(f"clash {c['id']}: unknown row {ref}")
    # every tiered target must be fed by at least one row
    fed = Counter(r["target"] for r in rows if r["action"] in ("keep", "merge"))
    for t in targets:
        if t["tier"] in ("0", "1", "2", "card") and fed[t["id"]] == 0:
            errors.append(f"target {t['id']} has no source rows")
    for t in targets:
        for f in t.values():
            if "—" in f or ";" in f:
                errors.append(f"target {t['id']}: em dash or semicolon")
    if errors:
        print("\n".join(errors))
        sys.exit(1)

    # source metadata
    meta = {}
    for code, (label, rel) in SOURCES.items():
        info = {"label": label}
        if rel:
            p = ARCH / rel
            b = p.read_bytes()
            info.update(path=f"archive/pre-prune/{rel}", bytes=len(b), lines=b.count(b"\n") + 1,
                        md5=hashlib.md5(b).hexdigest())
        meta[code] = info

    by_target = defaultdict(list)
    for r in rows:
        by_target[r["target"]].append(r)

    (HERE / "inventory.json").write_text(json.dumps(
        {"built": "2026-11-05", "step": 6, "sources": meta, "targets": targets,
         "rows": rows, "clashes": clashes}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    md = []
    w = md.append
    w("# Rule inventory (step 6 of the Rules Refactor Plan)")
    w("")
    w("Built 5 Nov 2026 from the pre-prune archive (4 Nov). Every rule from every source, with its tier, the outputs it applies to, how it is checked, and whether it is kept, merged, cut or moved. Generated by `build_inventory.py` from `inventory.psv`, `targets.psv` and `clashes.psv`. Edit those, never this file.")
    w("")
    w("## How to read it")
    w("")
    w("- **Tiers.** Tier 0 and Tier 1 fail a draft. Tier 2 never does (his words, 5 Nov: \"some t2 edits, but pass t1 t0\").")
    w("  - **Tier 0:** truth and hard mechanics. Never in a delivered draft. Checked by script, or against the material.")
    w("  - **Tier 1:** core craft. Judged on the whole passage, one checker per rule (step 12).")
    w("  - **Tier 2:** polish. The writer applies it. Lint fixes the mechanical ones silently.")
    w("- **Outputs:** A article, L letter, C chapter, K key moments, S case study. `social`, `reel`, `brand`, `content` are out of scope for the five cards.")
    w("- **Check:** `mech` script (cg_lint, step 11), `checker` one-rule checker (step 12), `judge` the writer's judgment, never fails.")
    w("- **Action:** `keep` this row is the main line of its target. `merge` folded into the target. `cut` dropped (duplicate, stale, superseded, or history). `move` goes to a home outside the rulebook. `out` stays in its own doc, untouched. `open` waits on his call.")
    w("- **Target:** a rule in the proposed rulebook (T0.x, T1.x, T2.x), a card, or a destination. The wording of each target is written in step 8.")
    w("- **Loc:** line numbers in the archived copy, so step 8 can copy exact text by script.")
    w("")
    w("## Sources")
    w("")
    w("| Code | Source | Lines | Bytes | md5 (archive) |")
    w("|---|---|---|---|---|")
    for code, info in meta.items():
        w(f"| {code} | {info['label']} | {info.get('lines', '')} | {info.get('bytes', '')} | {info.get('md5', '')[:12]} |")
    w("")
    w("Checks done on 5 Nov: the Mac Book Rules master and the project mirror have the same md5 (6625cc1b). The live Language Rules, Social Posting Rules and both skills match the archive. Book_Status.md was read on the Mac (30,290 bytes, 3 Nov). Project instructions were read from this chat's context.")
    w("")

    w("## Counts")
    w("")
    src_count = Counter(r["src"] for r in rows)
    act = Counter(r["action"] for r in rows)
    tier = Counter(r["tier"] for r in rows if r["action"] in ("keep", "merge") and r["target"].startswith("T"))
    w(f"- **{len(rows)} rows** from {len(src_count)} sources. Big sources are listed rule by rule. Out-of-scope docs (social, reel, brand, content) are listed by section.")
    w("- By action: " + ", ".join(f"{k} {act[k]}" for k in ("keep", "merge", "cut", "move", "out", "open")) + ".")
    placed = sum(1 for r in rows if r["action"] in ("keep", "merge") and r["target"].startswith("T"))
    cards = sum(1 for r in rows if r["action"] in ("keep", "merge") and r["target"].startswith("card"))
    w(f"- **{placed} rows fold into {sum(1 for t in targets if t['tier'] in '012')} rules** (Tier 0: {sum(1 for t in targets if t['tier']=='0')}, Tier 1: {sum(1 for t in targets if t['tier']=='1')}, Tier 2: {sum(1 for t in targets if t['tier']=='2')}). {cards} rows go to the 5 output cards.")
    w("- By source: " + ", ".join(f"{k} {v}" for k, v in sorted(src_count.items(), key=lambda x: -x[1])) + ".")
    w("")

    w("## The proposed rulebook (merge targets)")
    w("")
    w("A skeleton for step 8, not the final wording. Each line lists the rows that feed it.")
    w("")
    for tier_name, tier_key in (("Tier 0", "0"), ("Tier 1", "1"), ("Tier 2", "2"), ("Cards", "card")):
        w(f"### {tier_name}")
        w("")
        w("| Rule | Outputs | Check | Holds | Fed by |")
        w("|---|---|---|---|---|")
        for t in targets:
            if t["tier"] != tier_key:
                continue
            feeders = [r["id"] for r in by_target[t["id"]] if r["action"] in ("keep", "merge")]
            w(f"| **{t['id']} {t['title']}** | {t['outputs']} | {t['check']} | {t['what it will hold (proposed for step 8, not final wording)']} | {', '.join(feeders)} |")
        w("")
    w("### Other homes")
    w("")
    w("| Destination | What goes there | Rows |")
    w("|---|---|---|")
    for t in targets:
        if t["tier"] == "dest":
            ids = [r["id"] for r in by_target[t["id"]]]
            w(f"| {t['id']} | {t['what it will hold (proposed for step 8, not final wording)']} | {len(ids)}: {', '.join(ids)} |")
    w("")

    w("## Test set cover (a first look, proven in steps 12 and 13)")
    w("")
    w("Every fail case should break at least one Tier 0 or Tier 1 rule, and no pass case should. Pass cases P2 to P10 were linted on 5 Nov: no em dash, semicolon or \"my clients\" in any of them, so T0.1 passes them all.")
    w("")
    w("| Case | What he marked | Rules it breaks |")
    w("|---|---|---|")
    w("| F1 round 3 patched rewrite | \"robotic and repeated\", \"wtf is this?\", \"too many differing concepts\", the/you not parallel | T1.3, T1.5, T1.13, T1.14 |")
    w("| F2 Melina with \"health\" and \"nutritionist\" | invented surface, \"vague metaphor no one ever uses\" | T0.3, T0.5, T1.6 |")
    w("| F3 Chapter 3 epoch 4, the ditch paragraph | a question answered with no link back, the metaphor \"very off\" | T1.2, T1.6 |")
    w("| F6 chimp piece v7 | two arcs, the ending announced early, two lines narrating the structure, literature-review habits | T1.7, T1.12, T1.10 |")
    w("| F7 \"The goal they kept changing\" | his typed phrase changed | T0.2 |")
    w("| F8 Aiman case study | \"nothing after the first sentence make any sense\" | T1.9, T1.11 |")
    w("")
    w("## Duplicates")
    w("")
    w("- **The em dash ban** is stated in 43 files: 23 project docs, 18 skills and 2 memory files (counted by script on the archive, statements only, research notes left out). Plus the project instructions. It becomes one line in T0.1, checked by lint.")
    w("- **The semicolon ban** is stated in 25 files (15 project docs, 10 skills). Two memory lines (account preferences, ways-of-working) offer the semicolon as the em dash substitute (clash C1).")
    w("- **Files that mention** British spelling 15, digits 17, \"my clients\" 9, the Oxford comma 8, the sign-off 13, emojis 15.")
    dupcount = Counter()
    for r in rows:
        for ref in re.findall(r"Dup ([A-Z0-9 ,.\-a-z]+)", r["note"]):
            dupcount[r["id"]] += len(re.findall(r"[A-Z]{2,3}-[\w.]+|T\d\.\d+|PI-\d+", ref))
    w("- **Review checklists repeat the rules:** Book Rules section I (30 items) and Language Rules section 12 (18 items) restate rules already listed. Both become the checker set and lint, not text the writer loads.")
    w("- **Memory repeats the rule docs:** " + str(sum(1 for r in rows if r['src'] in ('MP', 'MA', 'MW') and r['action'] == 'cut')) + " memory lines are cut as duplicates or stale (step 19). Working style stays.")
    top = [r for r in rows if dupcount[r["id"]] >= 3]
    w("- **Most-copied rules** (3 or more copies named in the row's note): " + ", ".join(f"{r['id']} ({dupcount[r['id']]})" for r in sorted(top, key=lambda r: -dupcount[r['id']])) + ".")
    w("")

    w("## History inside rule files")
    w("")
    w("| Where | What | Share of the file | Action |")
    w("|---|---|---|---|")
    w("| LR §13 to §15 (L419 to L649) | Calibration logs: Law 1 rounds, the chimp piece v1 to v10, Lasting Change Letters #1 | 20,535 of 64,888 bytes (32%) | Move to the calibration log. The chimp rewrite joins the corpus |")
    w("| LR annotations (\"Updated\", \"Retired\", \"Corrected\", \"Supersedes\") | Old lines kept beside their corrections | about 10 places | Keep only the final rule |")
    w("| BR v1 (L397 to L538) | The abandoned Book Rules v1 and its epoch 0 log | 10,016 of 61,578 bytes (16%) | Cut. It is in the archive and git |")
    w("| BR \"His words\" and \"Support\" under each rule | Evidence: quotes, measurements, line numbers | most of sections A to G | Evidence column in the rules table (step 9). Not loaded with the card |")
    w("| BR section H | Warnings between the two rule docs | 23 lines | Settled into the cards. The two-doc split ends |")
    w("| WS \"What has actually gone wrong\" | 17 failures, each pointing at a rule | 23 lines | Cut from the skill. Two letter-only lines go to card-L |")
    w("| Social Posting, Reel, Content logs | Calibration logs and approved posts | most of each file | Out of scope, untouched |")
    w("")

    w("## Clashes (seed for step 7)")
    w("")
    w("| # | Topic | One side | Other side | Status | How it settles, or his options |")
    w("|---|---|---|---|---|---|")
    for c in clashes:
        w(f"| {c['id']} | {c['topic']} | {c['one side']} | {c['other side']} | {c['status']} | {c['how it settles, or his options']} |")
    w("")

    w("## Every row, by source")
    w("")
    for code in SOURCES:
        rs = [r for r in rows if r["src"] == code]
        if not rs:
            continue
        w(f"### {code}: {SOURCES[code][0]}")
        w("")
        w("| ID | Loc | Kind | Rule | Tier | Out | Check | Action | Target | Note |")
        w("|---|---|---|---|---|---|---|---|---|---|")
        for r in rs:
            w(f"| {r['id']} | {r['loc']} | {r['kind']} | {r['rule']} | {r['tier']} | {r['out']} | {r['check']} | {r['action']} | {r['target']} | {r['note']} |")
        w("")
    text = "\n".join(md) + "\n"
    if "—" in text or ";" in text:
        bad = [l for l in text.splitlines() if "—" in l or ";" in l]
        sys.exit("em dash or semicolon in INVENTORY.md:\n" + "\n".join(bad[:5]))
    (HERE / "INVENTORY.md").write_text(text, encoding="utf-8")
    print(f"ok: {len(rows)} rows, {len(targets)} targets, {len(clashes)} clashes")
    print("actions:", dict(act))
    print("placed in tiered rules:", placed, "| to cards:", cards)
    print("tier of placed rows:", dict(tier))


if __name__ == "__main__":
    main()
