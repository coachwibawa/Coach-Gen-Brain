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

## 16 Nov, 13:20 to 13:50: step 1 finished

He signed in to claude.ai in the browser pane and said go (also "ok" on the CORRECTION lines).

1. **Compare:** one script in the page fetched all 88 docs and took the sha256 of each. All 37 docs that mattered (the leaving ones and the ones to edit) equalled their archive copy, byte for byte. Nothing newer had to be archived.
2. **Removed, 23 docs:** groups A, B and C of `rules/step18/stale_docs.md` (14), the 5 Full Read Notes, Brand_Direction_Phase1, Brain_RAG_Plan, Overnight_Book_Run_Ledger, Experimental_Book_Branch_Handoff. The project holds 65 docs. (The note above says 26. That was a miscount.)
3. **Stay on purpose:** AB_Test_Writing_Skills (until step 20), Raw_Take_Edit_Plan_Jikoshoukai, and 5 book notes with live items (`rules/step18/book_notes_check_2026-11-16.md`).
4. **Written, each by `local_path` from the archive copy plus exact inserts** (copies in `project-docs/`, old lines all kept): Protected Docs, Toastmasters handoff, Content Rules, Social Posting Rules, brand 00_START-HERE, 01_CORE, 02_VOICE, 18_COPY-KITS, 99_CHANGELOG (v1.7), and `brand/templates/cg_render.py` (2 sample texts changed, a comment above each, compiles).
5. **Mac mirror:** the 5 brand md files were copied to `Brand/Guide/`. `cg_render.py` has no copy in `Brand/Guide/templates/` on the Mac, so it was not mirrored.
6. `project_write` refuses a doc this chat has not read with `project_read`, so each edited doc was read once first.
7. He deleted the two old skills. Do not ask again.

Still open from step 1:

- `Book/Book_Status.md` on his Mac holds the older locked line. Not changed (his ledger, a book chat's job).
- The 5 book notes leave once a book chat has merged their live items.
- The autopilot line in project memory leaves after 18 Nov.
- Two saved skills (`rhyme-this`, `merge-epoch-to-book`) still cite old rule numbers. They get rule names the next time each is edited.
- coach-gen-writer may still point at the Full Read Notes in the project. They are now in `archive/pre-prune/project-docs/claude/`.

Next: step 2 (bring `claude/Rules_Refactor_Handoff.md` up to date). The same browser route can fetch its bytes: the live sha256 on 16 Nov was `91b110c454cd...`, 26,953 bytes. Then step 3, the blind A/B.

## 16 Nov, 13:55: step 2 done

`claude/Rules_Refactor_Handoff.md` has its dated section (sha256 `91656d95717d...`). The copy in `project-docs/claude/` was rebuilt and matched the live doc's sha256 (`91b110c454cd...`, 26,953 bytes) before the section was appended, so the old text is byte for byte.

One card waits for his save: one line in coach-gen-writer that points the Full Read Notes at the repo archive (proposed 16 Nov, 13:50).

**Next: step 3 (plan step 20), the blind A/B, in a new chat.** Start it with: read `rules/PHASE5_HANDOFF.md` in the repo `coachwibawa/Coach-Gen-Brain` and continue from Next, step 3.

## 16 Nov, 19:00 to 20:00: step 20 and 21 done

1. **Step 20 ran** on Chapter 5 (Law 3), the pruning section, from 8 brain entries. Old stack: the pre-prune skill and rule docs. New stack: the skill, the chapter card, `cg_lint.py`, the 20 checkers. Record: `tests/rules/runs/ab_2026-11-16/log.md` (setup, incidents, cost, his words, the key).
2. **Result:** he scored X 7 (old stack) and Y 8.25 (new stack), before he saw the key, a hunch, low confidence. Both drafts pass the lint and all 20 checkers. The new draft needed 2 checker fix rounds first.
3. **Step 21:** the new stack wins, so it stays the default. Nothing restored. One round only. The next real chapter is the true test.
4. **His reason, for both drafts:** the recommendation (pruning) is not argued, built up or delivered powerfully, which a book that gives specific advice must do. Neither stack caught it. The checkers have no rule for it. His follow-up: it is solved by length and thought, and storytelling sometimes, and research. Word for word in the log.
5. The key is in `tests/rules/runs/ab_2026-11-16/sealed/key.json`. It is open now.

## Next, in order (from 16 Nov, 20:00)

1. **The candidate rule above:** run `propose-language-rule` on his sentence. It needs a test: write the pruning section again with the rule, check that the 5 fail and 9 pass cases hold, and that the new rule fails both A/B drafts. He sees the exact text and gives the go. Opus, high.
2. **The cost of the checkers.** The A/B used about 2.4 million Sonnet tokens on 26 helper runs. Get an API key for `cg_check.py run` (about 20 small calls). That is his part.
3. **Still his:** save the one-line coach-gen-writer card (the Full Read Notes pointer). Delete nothing else. The autopilot line in project memory leaves after 18 Nov.
4. **Left on purpose:** review item 13 (spreading the sort values), the 5 book notes with live items, the two skills that cite old rule numbers (`rhyme-this`, `merge-epoch-to-book`).
5. **The first real use:** the next chapter epoch with the new stack. Run the checkers once on the final draft only.

## Rules added 16 Nov, from the A/B

1. Writers in a blind test get the same prompt but for one block. Read the prompt for stray lines before launch.
2. Checkers run once on the final draft. After a fix, rerun only the checkers that failed, twice for a noisy one.
3. Log his scores and words before opening the key.

## 16 Nov, 20:05: step 22 done

1. `claude/Rules_Refactor_Handoff.md` in the project has its dated section (sha256 `a38e79d4d35b...`, equal to `project-docs/claude/Rules_Refactor_Handoff.md`). The old text is byte for byte.
2. Project memory points at the rules table: one line in `ways-of-working.md` ("Writing rules"), one in `areas/rules-refactor.md` (his A/B scores).
3. **`AB_Test_Writing_Skills` was NOT removed.** The byte compare with `archive/pre-prune/project-docs/claude/AB_Test_Writing_Skills.md` needs the browser route (sign-in to claude.ai, fetch the docs, sha256), and the auto mode classifier blocked that call on 16 Nov evening. The doc is the older record of the Pocock A/B rounds and is safe in the archive. It leaves once a compare is possible, or once he says to remove it without one.
4. The Phase 5 plan rows 20 to 22 and the Decisions log in the Autopilot doc are updated.

The next chat starts at "Next, in order (from 16 Nov, 20:00)" above, step 1: propose the rule from his verdict reason.
