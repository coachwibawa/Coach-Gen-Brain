# Phase 4 state, saved 15 Nov 2026, 18:35 Jakarta

Saved in a hurry, on his word ("save before hitting limit"). This file is NEWER than `claude/Rules_Refactor_Handoff.md` in the project, which still says step 16 is next. Read that note for the background and the rules for this work, then continue from "Open, in order" below.

## Done and pushed

1. **Step 16, built and tested.** `tools/cg_fold.py` (build, gate, result, approve, decline, stored, live, status), `tools/cg_rules.py`, `tools/cg_check.py` (`--only`, `CG_RULES`, `CG_CHECKERS`, reads the live rules), `rules/table/compile_cards.py` (reads the live rules), `tests/rules/test_fold.py` (27 checks, all pass), `tests/rules/fixtures/`, `rules/folds/README.md` (the path and the spec format).
2. **Migration 021 is APPLIED to the brain** (11 Nov): `brain.fold_load`, `brain.fold_store`, `brain.fold_decline` and two inner functions. Applied from the repo file pinned to commit `194d432`. Tested before and after in a dry run that undid itself: after a made-up fold, the brain's rulebook and all five cards equalled the repo's, md5 for md5. The brain is unchanged: 49 rows in `brain.rules`, rulebook md5 `a80b78c1b69fc97be58cdbad021f8138`, no fold stored yet.
3. **Design call:** rule codes never change. A changed rule is updated in place when its fold is stored, the old text stays in `brain.change_log`, and the fold row stays in the table as the record.
4. **Skill drafts in the repo, NOT yet proposed with `propose_skills`:** `skills/propose-language-rule/SKILL.md` (merged with fold-article-lessons, about 2,100 words), `skills/mine/EDITS.md`, `skills/extract-fathom/EDITS.md` (two exact replacements each, checked to occur once in the installed skills).
5. **The mining change:** section 11 of `claude/Brain_Rule.md` was written to the project on 11 Nov (`answers`, `context`, `owned_words`). Copy: `project-docs/claude/Brain_Rule.md`.
6. **Step 17, drafted:** `rules/step17/project_instructions.txt` (10 lines, his to paste) and `project-docs/Guardrails.md` (prepared, NOT written to the project: it goes in when he pastes the instructions).
7. **Step 18, drafted:** `rules/step18/stale_docs.md`. 34 of the 92 project docs can leave, about 260,500 tokens, in 6 groups, with the pointers that must move with them.
8. **Step 19, drafted:** `rules/step19/memory_dedupe.md`. 62 memory lines leave, about 30 stay. Each leaving line was checked against its new home. Nothing removed.
9. **Decision page published:** https://claude.ai/artifact/GJfsX6ro5pfMh1jdgSjCCf (slug `7bf0add9-d61e-4729-9352-3e8a15ce49b0`, collection `picks`, 11 cards, numbers 1 to 41). Spec in `rules/phase4_decisions/`.
10. **Docs updated on 15 Nov:** the Rules Refactor Plan (rows 16 to 19), and the Autopilot doc (a "Paste text for the project instructions" section, a link under task 2, a note on task 12).

## Done on 16 Nov (after the save above)

11. **The fresh review came in** (it ran the path cold, about 30 wrong inputs, and both migrations on a local Postgres): 36 points, verdict "not safe as it stands", first fix: a fold must refuse to store when its target changed after it was built. Fixed: every ERROR (1 to 6) and GAPs 7 to 12, 14 to 19, 21 to 24, plus NITs 25 to 27, 29 (in part), 30 to 36. `tests/rules/test_fold.py` now runs 37 checks, all pass.
12. **Migration 022 is APPLIED to the brain** (16 Nov): guarded versions of the two inner fold functions (a fold is tied to its target's text by `base_md5`, a load cannot overwrite another file's open fold, the store compares tier, check type and sort). Applied from the repo file pinned to commit `6f1ebb3`, after a dry run that undid itself (md5 equal, both guards refused as they should). The brain is still unchanged: 49 rows, same rulebook md5.
13. **The 3 skill cards were proposed** in the chat on 16 Nov: propose-language-rule (about 2,600 words), mine, extract-fathom. They wait for his save. Repo copies: `skills/`.
14. **Brain Rule section 11** was written again with two lines made exact (which entries are empty, and never empty a filled field).
15. **Decisions log** in the Autopilot doc: rows added for migrations 021 and 022, the code design, section 11, the gate default, the skill's length and the two things held back.

## Open, in order

1. **`claude/Rules_Refactor_Handoff.md` in the project is NOT updated.** It still says step 16 is next. This file is the newer record. A chat with room should add a dated section to that note (add-only, never retyped: start from a fresh `project_read`) and run /handoff for Phase 5. Fold check for this chat: he asked for no new writing rule.
2. **Left from the review, on purpose:**
   - Item 13: places between two rules can run out (sort values are 10 apart). A new rule at the end of a tier now takes the next value, which gives 9 appends. A migration to spread the values is not written.
   - Item 20: the new coach-gen-writer never names `answers`, `context` and `owned_words`. Add one line pointing at section 11 of the Brain Rule the next time that skill is proposed. Its card from 11 Nov is not saved yet, so it can go into a re-proposal from `skills/coach-gen-writer/SKILL.md`.
   - Item 28: the gate-failed text talks about wording even when the fold only retires a rule.
   - Two inventory rows landed in part: BR-00c ("weaker support says so" is now one line under Support) and PL-06 (the anchor line is shown by `build`).
3. **The two thin margins (found 15 Nov, not acted on).** F1 is caught only by R1.16, on a narrower reason than his own ("too many differing concepts that were unexplored", which is R1.5's ground). F3 is caught only by R1.11, for a reason he never raised. His real complaint on F3 is continuity ("did I just miss several paragraphs"). R1.2 already carries a calibration note taken from F3, and its checker still passed F3 in the fresh run. So "5 of 5" is thinner than it looks. Next: rerun R1.2 and R1.5 on all 14 drafts, twice each (`cg_check.py batch tests/rules/runs/fresh_2026-11-11/manifest_in.json --dir <new run> --only R1.2,R1.5`, after writing the drafts from `test_set.json`), and see what they say about F3 and F1. Then decide on notes. No rule text changes without him.
4. **Phase 5, step 20:** the blind A/B (old stack against the new card, lint and checkers on one chapter section). A new chat. It needs him only at the end, to score X and Y.

## What waits for him

Everything is on the decision page: save 4 skill cards, paste the 10 lines, fix the semicolon line in his account-level preferences, 2 calls (the locked line, the Full Read Notes), the go on the docs list and the go on the memory list.

## 16 Nov, 01:40: he handed the calls to Claude

His words: "seems everything is arbitrary decisions with obvious calls on what is better. if it's something I have to do, like skill cards etc, say it again or propose it again so I never have to dig old turns." Saved to project memory.

All 4 skill cards are SAVED (checked against the installed skills on 16 Nov): coach-gen-writer, propose-language-rule, mine, extract-fathom. One small card is open: one line added to coach-gen-writer on how to read `answers`, `context` and `owned_words` (proposed 16 Nov).

Claude's calls on the decision page, to carry out in the next chat (each doc read fresh and compared with its archive copy before it is removed, newer versions archived first):

1. Card 4, the locked line: the newer wording everywhere. He approved it as the locked line in rulebook v3. Add the dated CORRECTION lines to the brand docs and the Social Posting Rules, and fix `overview.md` in project memory.
2. Card 5, the Full Read Notes: move out. The writer skill then points at the repo archive.
3. Cards 6 to 19: remove all 14.
4. Cards 24 to 27: move Brand_Direction_Phase1 and Brain_RAG_Plan. Keep AB_Test_Writing_Skills until step 20 is done, and keep Raw_Take_Edit_Plan_Jikoshoukai (that idea is parked, not dropped).
5. Cards 28 to 34: check each against Book_Status.md on his Mac, then move.
6. Cards 35 to 40: all pointer fixes, with Guardrails written once he has pasted the instructions.
7. Card 41: the memory cleanup as listed. The cards are saved, so group A can go too.

Still his, because only he can: paste the 10 lines into the project settings, take "semicolon" out of his account-level preference, remove the 4 Word uploads, delete fold-article-lessons and write-book-from-material in Settings if they still show, save the one-line writer card.
