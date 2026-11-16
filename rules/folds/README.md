# Folds: how a rule gets into the rules table (step 16)

A fold is one round of feedback turned into rule changes. One file here per fold. The skill that runs it is `propose-language-rule`.

**Stages:** captured, judged, merged, gated (the test set), approved (his go), stored.

**Rule codes never change.** A changed rule keeps its code (R1.7 stays R1.7), so the checkers, the calibration notes and every report keep pointing at the same rule. In `brain.rules` a fold is one row per action:

- `new`: a new rule. The row carries its final code (R1.21) and goes live when stored.
- `change`: new wording for a live rule or card. The row is `fold:<target>:<date><letter>`. When stored, its text is copied onto the target, the old text stays in `brain.change_log`, and the fold row stays as the record (retired, with a note).
- `retire`: a live rule leaves. When stored, the target is retired with the reason.

A fold row is never served before it is stored. Nothing is deleted.

## The path

1. Write a spec (below), then `python3 tools/cg_fold.py build SPEC.json`. It writes `rules/folds/<date>_<slug>.json`, prints the proposal and names the checkers the fold touches. Commit, push, then `select * from brain.fold_load('rules/folds/<file>.json');` so the lesson is in the brain.
2. `python3 tools/cg_fold.py gate FOLD --dir tests/rules/runs/<name>`. It runs the lint on the test set and writes one batch prompt per touched Tier 1 checker (`--all` for every checker). `--origin DRAFT --origin-output chapter` adds the draft the lesson came from: a touched checker must fail it. One Sonnet helper per prompt saves its JSON answer as `<code>.json` in the run folder.
3. `python3 tools/cg_fold.py result FOLD --dir <same>`. It joins the new answers with the last full run (`tests/rules/runs/BASE`, else `fresh_2026-11-11`), prints each case with what was expected and what came back, and passes only when every fail case still fails and every approved passage still passes. It writes the gate into the fold file. Commit, push, `brain.fold_load` again.
4. Show him the exact text and the gate result. On his go: `python3 tools/cg_fold.py approve FOLD`, commit, push, then `select * from brain.fold_store('rules/folds/<file>.json');`. It returns six md5 values.
5. `python3 tools/cg_fold.py stored FOLD --md5 rulebook=… article=… letter=… chapter=… key_moments=… case_study=…`. It rebuilds `rules/table/rules_live.json` and `rules/rulebook/rulebook_live.txt`, checks all six md5 values against the brain's, recompiles the five cards and rebuilds the checkers. Then copy the cards to the project (`claude/cards/`) and his Mac (`Book/Rule Cards/`), commit and push.

If he says no to a lesson: `python3 tools/cg_fold.py decline FOLD N --note "his words"`, and in the brain `select brain.fold_decline('<code>', '<his words>');`. The file and the table keep the declined lesson, so it is never proposed again.

`python3 tools/cg_fold.py status` lists every fold and its stage. Use it for the fold check at a handoff.

## Guards, and the way back (added 16 Nov 2026, after the fresh review)

- **A fold is tied to the text it was built on.** Each change or retire row carries `base_md5`, the md5 of its target as it stood at `build`. `gate`, `approve` and `brain.fold_store` refuse when the live rule has changed since (another fold was stored first). Then: `reopen` if it was approved, `build` on the fold file, gate and load again. Without this guard a second fold could wipe a line the first one added.
- **The gate is tied to the live rules.** `approve` refuses when the live rulebook changed after the gate ran.
- **`python3 tools/cg_fold.py reopen FOLD`** undoes `approve` (never a stored fold). Use it for any refusal after `approve`.
- **`gate --fresh R1.x`** throws away that checker's saved answer, for a rerun.
- **Pull before `build`.** `brain.fold_load` refuses to overwrite an open fold that came from another file, which is what two chats that have not pulled would do.
- **After `brain.fold_store`, if the md5 values were lost:** `select 'rulebook' as what, md5(brain.rulebook_text()) union all select o, md5(brain.card_text(o)) from unnest(array['article','letter','chapter','key moments','case study']) o;`. `stored` can be run again on a stored fold to finish the cards and the checkers.
- **A line stands in one rule only.** `build` refuses a line another live rule already has.
- **Every lesson needs** a `why`, and `his_words` or `support`.
- **Known limit:** places between two rules are finite (the sort values are 10 apart). When `build` says there is no free place, the sort values need a migration to spread them. None is written yet.
- Migration: `migrations/022_rule_folds_guards.sql`.

## The spec

```json
{
 "slug": "short-name",
 "source": "12 Nov 2026, his markup on Law 2 Part 1, epoch 3 (Google Doc id)",
 "stage": "merged",
 "lessons": [
  {"action": "change", "target": "R1.7",
   "add": [{"line": "The new line.", "after": "An existing line, copied exactly."}],
   "reword": [{"old": "An existing line, copied exactly.", "new": "Its new wording."}],
   "remove": ["An existing line, copied exactly."],
   "why": "What goes wrong without it, in one line.",
   "his_words": [{"on": "12 Nov 2026", "about": "on a draft where every heading was a question", "quote": "his words"}],
   "support": ["Atomic Habits, lines 449 to 460: what was measured"],
   "diagnosis": "Claude's reading, to confirm on the next draft: ..."},
  {"action": "new", "tier": 1, "heading": "Name of the rule", "after": "R1.7",
   "lines": ["The goal.", "The test.", "The allowed zone.", "The hard lines."], "why": "..."},
  {"action": "new", "tier": 2, "heading": "Name, in full", "short": "Name", "after": "R2.6",
   "cards": ["article", "chapter"], "lines": ["..."], "why": "..."},
  {"action": "retire", "target": "R2.5", "why": "..."}
 ]
}
```

- `stage` is captured, judged or merged. The gate and his go set the later stages.
- Lines are written without the leading "- ". No em dash, no semicolon.
- `add` without `after` goes at the end of the rule (`"first": true` puts it at the top).
- A change keeps the rule's tier. To move a rule to another tier, retire it and add a new one.
- A Tier 2 rule names the cards that load it: `article`, `chapter`, `case study`. The letter card follows the article card and key moments follows the chapter card. The tool rewrites each card's "Tier 2 rules loaded" line and adds those card rows to the fold itself.
- A Tier 1 rule may name the outputs it covers: `"outputs": ["chapter", "key moments"]` (default: all five). The brain's cards already pick rules by outputs. Since 17 Nov 2026 the checkers do too: a draft of another output passes that rule without a call, marked "out of scope". Test: `tests/rules/test_check_scope.py`.
- A new Tier 0 rule says its `check_type`: `mechanical` (then `tools/cg_lint.py` must be made to match before the gate) or `checker`.
- His quote, the support and Claude's diagnosis live in the row's evidence, never in the rule's lines.
- To correct the wording before his go: edit the `spec` part of the fold file and run `build` on the fold file. The codes stay. The gate must run again, and it keeps every answer whose prompt did not change.

## What checks what

- `tools/cg_rules.py` reads the rules for every tool: `rules_live.json` when a fold is stored, else `rules_v3.json`. It picks rows the way `brain.get_card()` does, so an md5 from the repo can be compared with one from the brain.
- `tests/rules/test_fold.py` runs the whole path in a throwaway copy with made-up rules and answers (37 checks).
- `tests/rules/fixtures/fold_selftest.json` is the same made-up fold, for a dry run inside the brain that undoes itself. Run 11 Nov 2026: after the fold, the brain's rulebook and all five cards equal the repo's, md5 for md5. Nothing was kept.
- Migration: `migrations/021_rule_folds.sql`.
