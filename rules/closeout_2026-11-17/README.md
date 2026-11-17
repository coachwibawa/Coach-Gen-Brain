# Rules Refactor close-out page (17 Nov 2026)

The last calls and the one save that wait for him, as one review page: 4 cards, numbers 1 to 10.

- Page: https://claude.ai/artifact/EHAQER2geMeTK5Ka5D5AxQ (slug `6b887f06-2e31-4289-bb9c-0e37cf7871f1`), capabilities db and user.
- His picks: collection `picks`. Doc ids: `1-7` (R1.21), `8` (API key), `9` (AB_Test_Writing_Skills), `10` (the 3 skill cards), each with `call` and `why`.
- Spec: `decisions.json`. Rebuild with `python3 tools/decision_page/build.py rules/closeout_2026-11-17/decisions.json rules/closeout_2026-11-17/decisions.html`, then publish to the same slug.

## What each pick means for the chat that reads it

1. `1-7`, `t1`: store R1.21 as it stands in `rules/folds/2026-11-16_recommendation-argued.json` (propose-language-rule, section 7). The gate is 14 of 15 (ORIGIN passes). `approve` refuses a fold whose gate did not pass, so first take his pick as the go and record it in the fold file, or ask the skill's way.
2. `1-7`, `t2`: change the spec to `"tier": 2`, `"cards": ["chapter"]`, drop `outputs`, build, gate (no checker reruns for Tier 2), load, approve, store.
3. `1-7`, `wide`: copy `lessons` from `tests/rules/runs/fold_R1.21_2026-11-16/alt_wording2_spec.json` into the fold's spec, put its note under R1.21 in `rules/checkers/calibration.json`, build, gate, load, approve, store.
4. `1-7`, `hold`: `cg_fold.py decline FOLD 1 --note "his words"` and `brain.fold_decline`. The lesson stays on file as declined for now, and comes back only with a second case from a real chapter.
5. `8`, `yes`: he makes the key and puts it in the cloud environment as `CG_CHECK_API_KEY`. Then `cg_check.py run RUN` works in any chat.
6. `9`, `remove`: delete `claude/AB_Test_Writing_Skills.md` from the project (his go). Its copy stays in `archive/pre-prune/project-docs/claude/`.
7. `10`: the cards were proposed at the end of the 17 Nov chat. Lost cards are proposed again from the edits in `rules/closeout_2026-11-17/skill_edits.json`.
