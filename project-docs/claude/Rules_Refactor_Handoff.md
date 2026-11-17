# Rules Refactor Handoff

## Start here

This chat runs **Phase 4 of the Rules Refactor Plan: steps 14 to 19** (skills and pruning). Set the model each step's row in the plan names: step 14 Opus high, step 15 Sonnet high, step 16 Opus high, step 17 Opus high, step 18 Sonnet medium, step 19 Opus high. Read the plan doc first, then this note.

(11 Nov, first Phase 4 chat: the fresh checker pass, step 14 and step 15 are done. See "Added 11 Nov, from the first Phase 4 chat". The next chat starts at the first "Next, in order" list below, step 16.)

**Autopilot until 18 Nov 2026 (his request, 11 Nov):** he wants Claude on autopilot and does not want to think for a while. Draft everything, decide what Claude can decide, and log every bigger call in the Decisions log of the doc "Autopilot, 11 to 18 Nov 2026" (https://claude.ai/artifact/KF6g1UUcANJhXVn97n82QL). Park his parts (saving skill cards, pasting project instructions, a go on a list) for 18 Nov. Tick the task board in that doc as items finish.

(11 Nov: Phase 3, steps 9 to 13, is done. 6 Nov: this note opened Phase 3, steps 9 to 13. 6 Nov: Phase 2, steps 6 to 8, is done and the rulebook v3 is approved. 5 Nov: this note opened Phase 2, steps 6, 7 and 8, on Opus, effort extra high.)

## Where things live

- **The plan:** Claude Doc "Rules Refactor Plan", https://claude.ai/artifact/3E4W9WNRdKoCLG2qXGvWTp. 22 steps in 6 phases, with the model, effort and Gen's part for each step. Steps 1 to 5 are marked done in it.
- **Repo:** GitHub `coachwibawa/Coach-Gen-Brain` (the old name `coach-gen-brain` redirects). Clone it, then attach it with push access.
  - `archive/pre-prune/` holds a byte-for-byte snapshot of every rule doc, project doc, skill and memory file as they stood on 4 Nov, with `MANIFEST.md5`. Tags `pre-prune` (Gen's tag on GitHub is `Pre-prune`) and `mb` mark it. Restore from it if a cut hurts.
  - `tests/rules/test_set.json` and `README.md` hold the rule test set (step 5). Read the README before using it.
  - A repo hook asks for every change to be committed and pushed before the chat ends.
- **Rule sources to inventory (step 6):**
  - Project: `Coach_Gen_Language_Rules.md`, `claude/Coach_Gen_Book_Rules.md` (a mirror only), `Guardrails.md`, `claude/Coach_Gen_Protected_Docs.md`, `claude/Coach_Gen_Content_Rules.md`, `claude/Coach_Gen_Social_Posting_Rules.md`, `claude/Reel_Style_Guide.md`, `brand/02_VOICE.md`, `brand/90_TASTE.md`.
  - Gen's Mac, folder `5 Laws of Lasting Change`: `Book/Coach_Gen_Book_Rules.md` is the Book Rules master. `Book/Book_Status.md` is the ownership ledger.
  - Skills: `coach-gen-writer`, `propose-language-rule`, `fold-article-lessons`. The archive also has copies.
  - Project instructions (in project settings) and memory: account level `/preferences.md` and the project's `preferences.md` and `ways-of-working.md`.
- **Review page from step 5:** https://claude.ai/artifact/FkgsaFt77Dmn29Z42Awdtf. Gen's picks are in its `verdicts` collection. They are already copied into the test set, so it is for reference only.

Added 6 Nov, from Phase 2:

- **The approved rulebook (step 8):** `rules/rulebook/rulebook_v3.txt` is the text to load in step 9. Its Google Doc is "Coach Gen Writing Rulebook, v3" (id 1tIfyVrZn34JMATZHWJ72Cc9OvojNzuIlU-g2BOEQPvk), approved 6 Nov. 215 lines numbered straight through: Tier 0 has 8 rules (37 lines), Tier 1 has 20 rules (86 lines), Tier 2 has 11 rules (44 lines), and 5 cards (48 lines). `build_rulebook.py` renders it. `README.md` there says what changed in v1, v2 and v3. The v1 and v2 docs are superseded.
- **The inventory (step 6):** `rules/inventory/`. `inventory.psv` has 447 rows, every old rule with its tier, outputs, check type, action, target and note. Every row now has a decision, none open. `targets.psv` (the step 6 grouping, T0.1 to T2.12, plus skill destinations such as `skill:writer` and `skill:propose`), `clashes.psv` (C1 to C21 and O1, all settled), `flags.psv` (30 flagged rules, all decided). `build_inventory.py` validates and renders `INVENTORY.md`. The v3 headings are the final rules. The inventory is the trail of which old rules each one came from, and the source for the evidence column.
- **Evidence:** the rulebook intro promises his quotes and the evidence behind each rule stay with the rule in the rules table. The inventory rows (source doc and line) and `archive/pre-prune/` hold them. Quotes stay out of the rule line itself (flag 7).
- **Decision page (step 7):** https://claude.ai/artifact/GMy4eBgCtFPBWSMLFbHncD. His 24 picks are in `rules/step7/picks_2026-11-05/`. Generator: `tools/decision_page/build.py`, now also the `decision-page` skill.
- **The rule shape he wants:** `claude/Case_Study_Quotes_Report_2026-11-05.md`, and v3's "A quote earns its marks" (lines 74 to 83). A rule gives a goal, a test to judge by, an allowed zone and hard lines, instead of a freeze that protects words at the cost of the goal.
- **The brain:** Supabase project "Coach Gen Brain" in his existing org, reached through the Supabase connector. Get its ref with `list_projects`.

Added 11 Nov, from Phase 3:

- **The rules table (step 9):** `brain.rules` (migration `019_rules_table.sql`), 49 rows: 5 frame rows, 39 rules (`R0.1` to `R0.8`, `R1.1` to `R1.20`, `R2.1` to `R2.11`, in v3 order) and 5 cards (`card:article`, `card:letter`, `card:chapter`, `card:key-moments`, `card:case-study`). Read with `brain.get_card('chapter')` (rows) or `brain.card_text('chapter')` (one text). `brain.rulebook_text()` equals `rulebook_v3.txt` byte for byte (md5 `a80b78c1b69fc97be58cdbad021f8138`). Add-only: delete and truncate are refused, a rule leaves by `status = 'retired'` with a note, and every insert and update goes to `brain.change_log`. Fold fields: `beats`, `source`, `added_on`, `fold_stage` (captured, judged, merged, gated, approved, stored), `test_gate`, `approved_on`. Only active and stored rows are served. Load file `rules/table/rules_v3.json`, built by `rules/table/build_rules_load.py`, loaded with `brain.load_rules(path)` straight from the repo. Details: `rules/table/README.md` and `SCHEMA.md`.
- **The mining change columns:** migration `020_entry_quote_context.sql` adds `answers`, `context` and `owned_words` to `brain.entries` (and to the end of `entries_full`). They are empty. The `mine` skill starts filling them in Phase 4.
- **The cards (step 10):** `rules/table/compile_cards.py` builds them from the table data and checks each against the live brain. Copies: project `claude/cards/Card_*.md`, Mac `Book/Rule Cards/`. A chapter loads about 5,850 rule tokens (the plan said 4,800, and v3 grew with his additions).
- **The lint (step 11):** `tools/cg_lint.py`. Runner `tests/rules/run_lint_on_testset.py`, notes `tests/rules/README_LINT.md`.
- **The checkers (steps 12 and 13):** `tools/cg_check.py` and `rules/checkers/` (one template per Tier 1 rule, `checkers.json`, `calibration.json`, `README.md`). Rebuild the templates with `cg_check.py build` after any rule or note change. Calibration report: `tests/rules/runs/calibration_2026-11-11/REPORT.md`.
- **Cost of the checkers:** no Anthropic API key exists (none in the workspace, none in the Supabase Vault). In a chat each Sonnet helper carries about 75,000 to 90,000 tokens of overhead, so one draft checked by 20 helpers costs about 1.5 million tokens. For test runs, use batch mode (one helper per rule, all drafts at once). Through the API the same check would be about 30,000 tokens. A key is his call (open in the Decisions log).
- **Autopilot doc:** "Autopilot, 11 to 18 Nov 2026", https://claude.ai/artifact/KF6g1UUcANJhXVn97n82QL. Task board (31 items, tick boxes) and the Decisions log.

Added 11 Nov, from the first Phase 4 chat:

- **The fresh checker pass:** `tests/rules/runs/fresh_2026-11-11/REPORT.md`, 14 of 14 from one fresh run of all 20 checkers. `tests/rules/report_run.py RUN --compare OLD` prints any run as a report (each case, expected, got, who caught it). The manifest the run used is `manifest_in.json` there (built from `test_set.json`). Two new calibration notes under R1.19 name P6 and P10.
- **The new coach-gen-writer (step 14):** repo `skills/coach-gen-writer/SKILL.md` holds the exact text proposed with `propose_skills`, about 2,000 words. `skills/README.md` says why it is longer than 1,500. The card was shown in the 11 Nov chat and is not saved yet. If that card is lost, propose again from the repo file.
- **The doc build in one command (step 15):** `Book/source/epoch_build.py` on his Mac, beside `make_review_doc.py` (md5 `61013936ca228afb7fd6fa150f650177`). It keeps its state in a work folder and, run again after each step, does the next stage and prints the one connector call to make (create_file with a file reference, read_doc, update_doc, the PDF export, the pages to look at). Not in the repo.
- **The Mac folder** `/Users/coachwibawa/Documents/5 Laws of Lasting Change` was connected again in this chat (folder access granted 11 Nov). A new chat may need to ask again with `device_request_folder_access`.

## Done

1. Phase 0: his decisions, the Mac folder connected, the repo attached.
2. Step 4: archive committed (`65bdaba`), tagged and pushed. Gaps: the 4 project `.docx` uploads exist only as text extracts. `write-book-from-material` was already gone from disk, so its copy comes from an earlier read.
3. Step 5: test set locked on 5 Nov at 15 cases, 6 fail and 9 pass. Gen re-judged every case by book standard. Dropped and kept on file: Melvin (P1), chimp v5 and v6 (F4, F5).
4. Step 6 (5 Nov): 447 rules inventoried and 30 flagged as counterproductive, outdated, badly made or noise. Commits `38d1ac6`, `7c64cf8`, `f278273`.
5. Step 7 (5 Nov): every clash and flag settled by his 24 picks on the decision page. Commits `94f2127`, `eb707d5`.
6. Step 8 (6 Nov): rulebook v1, then v2 (his comments and the quote rule), then v3 (his 7 comments on v2). v3 approved, line 192 included. Commit `f133364`. Card 39 confirmed on 6 Nov: the "" markup rule and the older brief line both go, and BR-0.3 with them.
7. Skills saved from this phase: `decision-page` and `rule-audit` (new), `rhyme-this` (no pick from Claude).
8. Step 9 (6 Nov): migrations 019 and 020 applied after a dry run inside the live brain that undid itself. 49 rows loaded, the rulebook md5 equals the file, all five card md5 values equal the script, 49 log rows, delete and truncate refused (tested live). Commits `cdd6187`, `2aee439`.
9. Step 10 (6 Nov): the five cards, every line word for word from v3, md5 equal to the live brain, written to the project and the Mac. Commit `bc94072`.
10. Step 11 (6 Nov): `cg_lint.py`. All 9 approved passages clean, F6 and F7 flagged, F1, F2, F3 and F8 left to the checkers (quality, no mechanical break). Letters with no Insight headers get a note, not a break, because his approved letter has none. Commit `cc122de`.
11. Step 12 (6 Nov): `cg_check.py` and 20 templates built from the table data. Smoke test: F8 failed 8 of 20. Commit `1a3b41d`.
12. Step 13 (6 to 11 Nov): three rounds. Final: 5 of 5 fail cases fail, 9 of 9 approved passages pass. Thin margins: F1 is caught only by R1.16 and F3 only by R1.11. Commits `d64d43e`, `318dbfb`. Plan rows 9 to 13 marked done.
13. Fresh full checker pass (11 Nov): all 20 checkers in one fresh run, 14 of 14. On the way, R1.19 falsely failed P6, then P10 on a rerun. A note for each (naming the case) fixed it, and two final reruns of R1.19 came back 14 of 14. Thin margins unchanged: F1 only by R1.16, F3 only by R1.11. About 2.1 million tokens. Commit `e958d92`.
14. Step 14 (11 Nov): coach-gen-writer rewritten from 6,400 words to about 2,000 (load the card, draft, lint, review file, check once, deliver, markup). All 40 `skill:writer` inventory rows landed. A fresh reviewer compared it with the old skill and the cards and found 9 gaps and 2 errors, all fixed. Proposed with `propose_skills`. Commit `85cb459`. His part: save the card (parked for 18 Nov).
15. Step 15 (11 Nov): `epoch_build.py` on his Mac. Tested read-only on Chapter 3 epoch 5: the html step, the stage 1 guard (it refuses a doc already on the 6x9 page), the word-for-word check (it stopped at his own typed edit, as it should), stage 2 (124 requests, one 49 KB part) and the PDF step (18 pages, figure pages found by caption). Not run live: create_file and the two update_doc writes. Their stage code is unchanged from the 3 Nov build. First real use: the next chapter epoch.

## In progress

Nothing half built. One open check: the step 13 result rests on a mixed run (5 checkers from round 3, 15 from round 2). Run a fresh full pass before daily use leans on it (Next, step 1). (6 Nov: Phase 3 had not started. 5 Nov: Phase 2 had not started.)

(11 Nov: that open check is closed. The fresh pass held 14 of 14, Done 13. Nothing is half built.)

## Next, in order (from 11 Nov, the second Phase 4 chat)

1. **Step 16, merge `fold-article-lessons` into `propose-language-rule`.** A new rule goes into `brain.rules` through the fold stages, records what it beats, its source and its date, and must keep 5 of 5 fails and 9 of 9 passes. Fold in the inventory rows with target `skill:propose`. Also propose the `mine` skill change: fill `answers`, `context` and `owned_words`. Read both skills' current SKILL.md in full first (`propose_skills` refuses an improvement until the current text is in the chat). The new coach-gen-writer already points rule asks to propose-language-rule, so keep that name. Test gate: `cg_check.py batch` on `tests/rules/runs/fresh_2026-11-11/manifest_in.json`, but run only the checkers the new rule touches, not all 20. His part: save the cards, delete `write-book-from-material` and `fold-article-lessons` in settings (parked).
2. **Step 17, new project instructions, about 10 lines,** pointing at the cards, the lint and the checkers. Replace the opening "Coach Wibawa (Coach Gen)" (drift report). His part: paste them into project settings (parked).
3. **Step 18, the stale project docs list** (about 30, already archived), each with its load cost. This also covers the 2 Nov sprint item "phase out project docs" and carried item 10. His part: a go on the list, and he removes the .docx uploads himself (parked).
4. **Step 19, project memory dedupe:** writing rules leave, working style stays. Carried items 10 and 11. His part: a go on the list, and he fixes the semicolon line in account-level preferences (parked).
5. End with /handoff for Phase 5 (steps 20 to 22). Step 20 needs his blind scores, so it waits until after 18 Nov. Fold check at the handoff.

Parked for 18 Nov from the first Phase 4 chat: save the coach-gen-writer card (in the 11 Nov chat, or proposed again from `skills/coach-gen-writer/SKILL.md`).

## Next, in order (as written 11 Nov, at the end of Phase 3)

1. **Fresh full checker pass.** All 20 checkers on the 14 drafts, Sonnet helpers, batch mode: build the manifest from `test_set.json` (F3 as `chapter`, P7, P8 and P9 as `chapter-excerpt`, the rest as in `REPORT.md`), `cg_check.py batch`, one helper per `R1.x.prompt.md`, then `split` and `collect`. If a case flips, add a calibration note that names the case and rerun only that checker. About 1.8 million tokens, so run it when tokens allow. (Done 11 Nov, Done 13.)
2. **Step 14, rewrite `coach-gen-writer` at about 1,500 words:** load the card (`brain.card_text` or `claude/cards/`), draft, lint (`cg_lint.py`), check (`cg_check.py`), deliver as a Google Doc epoch. Fold in the inventory rows with target `skill:writer` (BR-0.1, the [] markup rule, among them). Mind the helper cost: check the final draft once, not every pass. Read the current SKILL.md in full, then propose it with `propose_skills`. His part: save the card (parked for 18 Nov). (Done 11 Nov, Done 14. About 2,000 words.)
3. **Step 15, one script command for the Google Doc build.** (Done 11 Nov, Done 15.)
4. **Step 16, merge `fold-article-lessons` into `propose-language-rule`.** A new rule goes into `brain.rules` through the fold stages, records what it beats, its source and its date, and must keep 5 of 5 fails and 9 of 9 passes. Fold in the inventory rows with target `skill:propose`. Also propose the `mine` skill change: fill `answers`, `context` and `owned_words`. His part: save them, delete `write-book-from-material` and `fold-article-lessons` in settings (parked). (Moved to the list above, step 1.)
5. **Step 17, new project instructions, about 10 lines,** pointing at the cards, the lint and the checkers. Replace the opening "Coach Wibawa (Coach Gen)" (drift report). His part: paste them into project settings (parked).
6. **Step 18, the stale project docs list** (about 30, already archived), each with its load cost. This also covers the 2 Nov sprint item "phase out project docs" and carried item 10. His part: a go on the list, and he removes the .docx uploads himself (parked).
7. **Step 19, project memory dedupe:** writing rules leave, working style stays. Carried items 10 and 11. His part: a go on the list, and he fixes the semicolon line in account-level preferences (parked).
8. End with /handoff for Phase 5 (steps 20 to 22). Step 20 needs his blind scores, so it waits until after 18 Nov.

Carried to later phases, so nothing is lost:

9. (was 7) **Mining change (agreed 5 Nov):** "never reword" becomes a storage rule only. Each stored line also keeps what it answered, one line of session context, and the words the person owns, and each person's records stay linked. Not built. It touches the brain's entries and the `mine` skill: build it with step 9 if the schema change is small, otherwise in Phase 4.
   - 11 Nov: the schema part was built in step 9 (migration 020, columns only, records already linked through `speaker_id` and `about_id`). The `mine` skill part is in Next, step 4.
10. (was 8) **The old locked line:** `brand/02_VOICE.md`, `claude/Coach_Gen_Social_Posting_Rules.md` and project memory still hold the old wording. The master draft (`Book/source/chapters/chapter-1.js`, lines 116 and 143) and v3 line 10 hold the new one: "Every time you fail to make change, you succeed at staying who you are." Fix in steps 18 and 19.
11. (was 9) **Memory lines for step 19:** the "" markup line in project `preferences.md` (card 39), the semicolon line in account `/preferences.md` (decision 1), the memory lines MA-03 and MW-10 (semicolon as an em dash substitute), MW-01 (planning agent only, C19) and MW-05 (the brief line, card 39).
12. (was 10) **Rules routed to skills:** inventory rows with target `skill:writer` go into the step 14 rewrite (the [] markup rule, BR-0.1, among them). Rows with `skill:propose` go into step 16.
   - 11 Nov: the `skill:writer` rows are in the step 14 draft. The `skill:propose` rows wait for step 16.

Phase 3 steps, as written on 6 Nov (all done):

1. **Step 9, the rules table in the brain.** Write the migration: one rules table, a never-delete trigger, a change log, and a card function that returns Tier 0, Tier 1, one card and the Tier 2 rules that card names. Load rulebook v3 into it as written, each rule with its tier, outputs, heading, v3 line numbers and evidence. Add the fold fields below. Batch every write, finish the rest of the work, then ask him for one go and run the batch right after.
   - **The fold pipeline (agreed 5 Nov, built in steps 9, 10 and 16):** capture, judge, merge before adding, gate on the test set, his approval, store, compile. Each new rule records the rules it beats, its source and its date. A fold check runs at every /handoff: each rule he asked for in the chat is in the table or was declined.
2. **Step 10, the card compiler.** From the table, write the five cards (article, letter, chapter, key moments, case study) to the project and to his Mac. Diff the compiled text against `rulebook_v3.txt`: it must match word for word. A chapter should load about 4,800 rule tokens.
3. **Step 11, `cg_lint.py`.** Mechanical checks per output: Tier 0 marks and words (em dash, semicolon, emoji, "my clients", the business "we"), locked names and lines spelled exactly, and the Tier 2 mechanics. Word count and reading grade are reported, never failed. It must flag every test-set failure a script can see and pass all 9 approved passages.
4. **Step 12, one-rule checkers.** One short prompt per Tier 1 rule (20 in v3), run in parallel. Each reads the whole passage against its one rule and returns pass or fail, with the line that breaks it.
5. **Step 13, calibrate on the test set.** Between the linter and the checkers, all 6 fail cases fail and all 9 pass cases pass. Print each case with what was expected and what came back, plain and readable. Daily runs use Sonnet.
6. End with /handoff for Phase 4 (steps 14 to 19).

Phase 2 steps, as written on 5 Nov (all done):

1. **Step 6, inventory.** List every rule from every source above. For each, record its tier (0, 1 or 2), the outputs it applies to (article, letter, chapter, key moments, case study), its check type (mechanical, one-rule checker, or judgment), and keep, merge or cut. Mark duplicates (the em dash rule sits in 12 docs) and the history that lives in rule files (logs, the abandoned v1 Book Rules). Gen's part: none.
2. **Step 7, settle every clash.** Show Gen a short numbered list of each clash and how his decisions settle it. Wait for his go.
3. **Step 8, write the merged rulebook.** Tiers 0, 1 and 2, plus one card per output: article, letter, chapter, key moments, case study. Put it in a Google Doc for him to mark up, then wait for his go.
4. End with /handoff for Phase 3 (steps 9 to 13, the machinery).

## Rules for this work

- **His decisions (4 Nov):** semicolons are banned everywhere. Research in articles follows Book Rules R28 (story first, no year, at most one name), not Language Rules section 11. `write-book-from-material` goes (he deletes it in settings). He gave permission to condense, merge and delete old rules for performance and efficiency, now that the archive exists.
- **What the tiers mean, in his words (5 Nov):** a passing passage can still need "some t2 edits, but pass t1 t0". So a Tier 2 rule is polish and must never fail a draft. A failing draft breaks Tier 0 or Tier 1. Place each rule with this in mind.
- **The test set:** the checker judges the whole passage. The flagged lines are reminders of what went wrong, not the whole test. Every new rule must fail all 6 fail cases between them, and pass all 9 pass cases.
- **Protected docs:** the Language Rules and Book Rules are only ever written after Gen says go on the exact text. The Book Rules master lives on his Mac, and the project copy is a mirror. Never retype a doc: copy text by script from tool results.
- **Showing him things:** use short numbered lines he can take in at a glance. When he must choose, give options without steering him to one. Never quote him out of context in a rule (the cold-read test in `propose-language-rule`).
- **One chat per phase.** Each phase ends with /handoff.

Added 6 Nov:

- **His "fine" or "ok" is a go.** Act on it. Never ask him to confirm the same thing again (6 Nov, after being asked twice).
- **v3 is approved text.** Load it as written. His typed lines (v3 lines 4 and 139) stay word for word, including the curly apostrophe in "we’re".
- **Numbering runs straight through** in anything he reads, never restarting at 1.
  - CORRECTION (6 Nov, his words: "just don't continue numbers though hunders over a conversation"): in chat replies, each message starts again at 1. Straight-through numbering is for documents.
- **No pick from Claude wherever he chooses** (card 41).
- **Supabase writes:** batch them, finish the rest, ask for one go, run right after.
  - 11 Nov, during autopilot (until 18 Nov): writes that only add and can be undone go ahead and are logged in the Decisions log. Anything destructive, public, paid, or a skill save waits for him.
- **New or reworded rules** take the shape in "Where things live": goal, test, allowed zone, hard lines.

Added 11 Nov, from Phase 3:

- **Pick and log (6 Nov, his words: "just pick something dude and continue"):** when a call is low risk and can be undone, pick it, say which in one line, and log it. Do not stop for it.
- **Retry a failed check (6 Nov):** when a check fails for a tool reason (a confirmation timed out), retry it at once. Never leave a check undone and call the step finished.
- **Calibration notes:** a note in `rules/checkers/calibration.json` may say where a rule's line is, taken from his verdict on a test case, and names that case. A note never changes rule text.

Added 11 Nov, from the first Phase 4 chat:

- **A checker can be noisy at its line.** R1.19 flipped on a different approved passage in each rerun. When a note fixes a flip, rerun that checker twice, not once, before calling it held.
- **Big tool results land in files.** A full `read_doc` or a PDF export is saved by the app to a file whose path the result gives. Point the script at that path. Never copy the JSON through the chat.

## Suggested skills

- `pick-model`: at the start, if he asks which model or effort to use.
- `propose-language-rule`: for the rule format (bold title, short numbered lines) and the cold-read test, when wording the rulebook in step 8.
- `grilling`: in step 7, if a clash needs his thinking rather than a yes or no.
- `google-workspace`: before building the step 8 Google Doc.
- `handoff`: at the end of the phase.

For Phase 3 (added 6 Nov):

- `pick-model`: at the start of each step, if he asks.
- `decision-page`: if a step raises several calls for him.
- `propose-language-rule`: when designing the fold fields in step 9, since step 16 merges into it.
- `handoff`: at the end of Phase 3, with the fold check.

For Phase 4 (added 11 Nov):

- `coach-gen-writer`: read its SKILL.md in full before the step 14 rewrite.
- `skill-creator` and `propose-language-rule`: for steps 14 and 16. Propose with `propose_skills`.
- `rule-audit`: for steps 18 and 19.
- `decision-page`: to serve the step 18 and 19 lists to him on 18 Nov.
- `pick-model`: at the start of each step, if he asks.
- `handoff`: at the end of Phase 4, with the fold check.

## Log

- 5 Nov 2026: written at the end of Phase 1 (steps 4 and 5).
- 6 Nov 2026: updated at the end of Phase 2 (steps 6 to 8). Rulebook v3 approved. Fold check: every rule he asked for in the Phase 2 chat is in v3, a skill or project memory (numbering, vulnerability, the decision page, no pick, the quote rule), except the mining change, which is carried in Next, item 7.
- 11 Nov 2026: updated at the end of Phase 3 (steps 9 to 13). Fold check: he asked for no new writing rule in the Phase 3 chat. His working-style asks (chat numbering restarts each message, pick and log, retry a failed check, autopilot until 18 Nov) are in Rules for this work and Start here.
- 11 Nov 2026: updated mid Phase 4, after the first Phase 4 chat (fresh checker pass, steps 14 and 15). Fold check: he asked for no new rule in that chat. The new "Next, in order" list starts at step 16.

## Added 16 Nov 2026: Phase 4 is done, Phase 5 has started

Everything above is background and the rules for this work. Its "Next, in order" lists are history. The live record is in the repo `coachwibawa/Coach-Gen-Brain`:

- `rules/PHASE5_HANDOFF.md`: read this first. It is the newest note and says what is next.
- `rules/PHASE4_STATE.md`: how steps 16 to 19 ended.

State on 16 Nov:

1. Steps 14 to 19 are done. All skill cards are saved, the 10 project instruction lines are pasted, and `fold-article-lessons` and `write-book-from-material` are deleted.
2. Migrations 021 and 022 are applied (the fold path). The brain's rules are unchanged: 49 rows, rulebook md5 `a80b78c1b69fc97be58cdbad021f8138`.
3. The thin margins are closed with three calibration notes: 14 of 14, each note held twice.
4. Phase 5, step 1 is done: 23 stale docs left the project after a sha256 compare with the archive (88 docs to 65), Guardrails and the pointer docs are updated, the locked line has one wording everywhere, and project memory is cleaned up.
5. Next: step 20, the blind A/B (old stack against the new card, lint and checkers, on one chapter section, labelled X and Y, scored by him at the end). Then steps 21 and 22, and /handoff.

Added to the rules for this work on 16 Nov:

- **He handed the calls to Claude.** When a decision has an obvious better call, make it and log it. Whatever he must do himself, say it again in the current reply. Never ask twice for something he has done.
- **A catch by one checker is not a margin.** Count a fail case as held only when a checker fails it on his own ground, twice.
- **Comparing a project doc with a file:** `project_read` returns text into the chat, never a file. For a byte compare, sign-in to claude.ai in the browser pane lets one script take the sha256 of every doc. `project_write` returns the sha256 of what it wrote as `version`.

## Log, continued

- 16 Nov 2026: updated at the start of Phase 5, after step 1. This copy was rebuilt and matched the live doc's sha256 before the section was added. Fold check: he asked for no new writing rule in the 16 Nov chats.

## Added 16 Nov 2026, evening: steps 20 and 21 done, step 22 under way

Read `rules/PHASE5_HANDOFF.md` in the repo first. It has the newest state.

1. **Step 20, the blind A/B, ran** on Chapter 5 (Law 3), the pruning section, from 8 brain entries. Old stack against the new one (skill, chapter card, lint, 20 checkers). Both drafts pass the lint and all 20 checkers. The new draft needed 2 checker fix rounds first.
2. **His scores, given before the key was opened:** X 7 (old stack), Y 8.25 (new stack), a hunch, low confidence. Record, words and cost: `tests/rules/runs/ab_2026-11-16/log.md` in the repo.
3. **Step 21:** the new stack wins, so it stays the default. Nothing restored. One round only, so the next real chapter is the true test.
4. **His reason, for both drafts:** the recommendation (pruning) was not argued, built up or delivered powerfully, which a book that gives specific advice must do. It is solved by length and thought, and storytelling sometimes, and research. No rule yet. It goes through `propose-language-rule` (Next, step 1 in the repo note).
5. **Still open:** the one-line coach-gen-writer card is his to save. `AB_Test_Writing_Skills` stays in the project: its byte compare with the archive was not possible in the 16 Nov evening chat (the browser route was blocked), so it leaves only after a compare.
6. **Rules added:** read the blind-test prompts for stray lines before launch. Run the checkers once on the final draft. After a fix rerun only the checkers that failed. Log his scores and words before opening the key.

## Log, continued again

- 16 Nov 2026, evening: updated after steps 20 and 21. Fold check: he gave a reason for the verdict (a recommendation must be argued, built up and delivered powerfully, solved by length and thought, storytelling sometimes, research). It is not in the rules table yet. It is Next, step 1 in the repo note, so it is not lost, and it was not declined.

## Added 17 Nov 2026: the refactor is closed

All 22 steps are done. This note is history now. No handoff follows.

1. Report: Claude Doc "Rules Refactor: close-out report", https://claude.ai/artifact/Tx5Z8zkebihtmmrP2DDWgT.
2. His last calls and one save: https://claude.ai/artifact/EHAQER2geMeTK5Ka5D5AxQ. What each pick means is in the repo, `rules/closeout_2026-11-17/README.md`.
3. The rule from his A/B reason, R1.21, waits there (card 1). It is in the brain as a draft and not served.
4. The final state is the last section of `rules/PHASE5_HANDOFF.md` in the repo.

## Log, closed

- 17 Nov 2026: refactor closed. Fold check: the one rule he asked for (his A/B reason) is R1.21, waiting at stage merged for his pick. Nothing else was asked for.
- 17 Nov 2026, 11:20: his picks. R1.21 is stored (Tier 1, chapters). The A/B record left the project. He is back, so the autopilot period is over.
