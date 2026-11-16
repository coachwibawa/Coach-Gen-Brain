# Rules Refactor: Phase 5 handoff (16 Nov 2026)

## Start here

This chat carries out Claude's calls from the decision page (the cleanup of project docs and memory), then runs Phase 5, step 20: the blind A/B. Read `claude/Rules_Refactor_Handoff.md` in the project for the background and the rules for this work, then `rules/PHASE4_STATE.md` here for Phase 4. This note is the newest of the three.

## Where things live

- The plan: Claude Doc "Rules Refactor Plan", https://claude.ai/artifact/3E4W9WNRdKoCLG2qXGvWTp
- Autopilot doc (task board and Decisions log): https://claude.ai/artifact/KF6g1UUcANJhXVn97n82QL
- Decision page: https://claude.ai/artifact/GJfsX6ro5pfMh1jdgSjCCf. Spec: `rules/phase4_decisions/`. Claude's calls on it: `rules/PHASE4_STATE.md`, section "16 Nov, 01:40".
- The lists behind the calls: `rules/step18/stale_docs.md` (34 docs), `rules/step19/memory_dedupe.md` (62 memory lines), `project-docs/Guardrails.md` (the prepared new Guardrails).
- The archive to compare with before any doc leaves: `archive/pre-prune/` with `MANIFEST.md5`.
- Checkers, notes and the last full run: `rules/checkers/README.md`, `rules/checkers/calibration.json`, `tests/rules/runs/margins_2026-11-16/REPORT.md`.
- The fold path: `rules/folds/README.md`, `tools/cg_fold.py`, migrations 021 and 022 (applied).
- Step 20 material: project doc `AB_Test_Writing_Skills` (kept until step 20 is done), `archive/pre-prune/` for the old stack, `skills/coach-gen-writer/SKILL.md` for the new one.
- His Mac folder: `/Users/coachwibawa/Documents/5 Laws of Lasting Change`. Ask for it with `device_request_folder_access`. `Book/Book_Status.md` is needed for cards 28 to 34.

## Done

1. Phase 4, steps 14 to 19: built, tested, drafted or served. Detail in `rules/PHASE4_STATE.md`.
2. All 4 skill cards are saved, the writer's one-line addition included (checked 16 Nov against the installed skills).
3. He has pasted the 10 project instruction lines and removed the 4 Word uploads (seen 16 Nov: new instructions, 88 docs).
4. The thin margins: closed with three calibration notes. 14 of 14, each note held twice. F1 is caught by R1.5 and R1.16, F3 by R1.2 and R1.11.
5. The brain is unchanged by all of this: 49 rows in `brain.rules`, rulebook md5 `a80b78c1b69fc97be58cdbad021f8138`, no fold stored.

## In progress

Nothing half built. Waiting on him: delete `fold-article-lessons` and `write-book-from-material` in Settings if they still show. The semicolon ban is now in his account preferences (seen 16 Nov), so that one is done.

## Next, in order

1. **Carry out the calls** (cards 4 to 41, as listed in `rules/PHASE4_STATE.md`). Read each doc fresh and compare it with its archive copy before it leaves. Archive any newer version first. Write `Guardrails.md` from `project-docs/Guardrails.md` by `local_path`, never retyped. Keep `AB_Test_Writing_Skills` and `Raw_Take_Edit_Plan_Jikoshoukai`.
2. **Bring `claude/Rules_Refactor_Handoff.md` up to date.** It still lists step 16 as next. Only do it when `project_read` hands the doc over as a file, or copy it by script from a tool result. Add a dated section. Never retype it.
3. **Step 20, the blind A/B:** one chapter section written twice, by the old stack and by the new card, lint and checkers. Label them X and Y. He scores both at the end without knowing which is which.
4. Steps 21 and 22, as the plan says.
5. End with /handoff. Fold check: every rule he asked for in the chat is in the table or was declined.

## Rules for this work

Those in `claude/Rules_Refactor_Handoff.md` still hold. Added 16 Nov:

1. **He handed the calls to Claude.** When a decision has an obvious better call, make it and log it in the Decisions log. Whatever he must do himself, say it again in the current reply.
2. **A catch by one checker is not a margin.** F1 was "caught" on 11 Nov and passed clean on 16 Nov with nothing changed. Count a fail case as held only when a checker fails it on his own ground, twice.
3. **Autopilot ends about 18 Nov.** After that, bigger calls go back to him.

## Suggested skills

- `rule-audit`: for the docs and memory cleanup in step 1.
- `decision-page`: only if a new call needs him.
- `coach-gen-writer`: for the new-stack side of step 20.
- `pick-model`: at the start of step 20, if he asks.
- `handoff`: at the end.

## Fold check for the 16 Nov chats

He asked for no new writing rule. His working-style ask (make the obvious calls, repeat what is his to do) is in project memory and in the rules above.

## 16 Nov, 08:35 to 09:15: step 1, first pass

Done:

1. `Guardrails.md` written to the project by `local_path` (sha256 `fa83a3fb0cf0935035d7673b308dc7fc8af1e08cd5ba24f9a041a2bb641b0289`, equal to `project-docs/Guardrails.md`).
2. Card 41, the memory cleanup: done in `preferences.md` (83 lines to 31) and `ways-of-working.md` (21 lines to 10). The autopilot line stays until 18 Nov. The lines newer than the archive are in `rules/step19/removed_newer_lines.md`.
3. Card 4, memory part: `overview.md` now holds the newer locked line.
4. Cards 28 to 34 checked against `Book/Book_Status.md` on his Mac: `rules/step18/book_notes_check_2026-11-16.md`. 2 are covered. 5 hold live items and stay for now (Claude's call).

NOT done, and why:

5. **No doc has been removed.** `project_read` hands every doc over as chat text (even 182 KB), so no script can compare it with the archive. Helper agents have no Projects tool. The browser pane (claude.ai is allowed there now) is not signed in to claude.ai. Once he signs in there, one script can fingerprint all docs: fetch `/api/organizations/<org>/projects/01a004af-f98d-75a0-82ee-b053384bfff1/docs` in the page, sha256 each `content`, and compare with `sha256sum` of the archive copies. `project_write` also returns the sha256 of what it wrote as `version`.
6. The pointer fixes that depend on the removals (Protected Docs rows, Toastmasters handoff, Content Rules) and the exact-byte edits need the same compare first.
7. Card 4, the CORRECTION lines in the brand docs, `cg_render.py` and the Social Posting Rules: he sees the exact lines first (the docs' own rule).
8. Only read so far in this chat: Full_Read_Notes_1 and 4 (inline, not compared by script).

Leaving list once the compare passes (26 docs): groups A, B, C of `rules/step18/stale_docs.md`, the 5 Full Read Notes, Brand_Direction_Phase1, Brain_RAG_Plan, Overnight_Book_Run_Ledger, Experimental_Book_Branch_Handoff.
