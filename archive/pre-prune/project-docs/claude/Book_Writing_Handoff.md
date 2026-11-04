# Book Writing Handoff (19 Oct 2026)

From the book thread to the article thread. Read this before writing any book chapter, or any article written to book standard.

His words (19 Oct): "specifications has changed, and now I want the article thread next door to write like a book, so that means getting all your context, especially the references and your exploration of it. your scope will be book formatting and stuff, not writing."

## 1. Who does what from now on

- **Article thread: all writing.** Articles written to book standard, and the book chapters themselves: story options, key moments, epochs, and redrafts from his markup. Skill: `write-book-from-material`.
  - *Annotated 20 Oct 2026:* writing now runs on one merged skill, `coach-gen-writer` (articles, Lasting Change Letters and chapters, all to book standard, with the leading word and grounding check from the A/B test). It replaces `inside-the-introvert`, `lasting-change-letters` and `write-book-from-material` once he saves it and removes the old three. One chat per piece, opened with the skill, closed with /handoff.
- **Book thread: formatting only.** The master draft build (`source/build.js`, `source/make_book.py`), merging an approved epoch into it (skill `merge-epoch-to-book`), the Notes page, page order and empty pages, the print booklet (skill `book-draft-to-booklet`), and layout. It touches a chapter only when he says the chapter is ready to merge.

## 2. Read first, in this order

1. **Book Rules.** Master on his Mac: `Book/Coach_Gen_Book_Rules.md` (project mirror `claude/Coach_Gen_Book_Rules.md`). Protected. Section 0 is his markup code, A to G are the rules (R1 to R37), H is where the books and the Language Rules disagree and what he decided, I is the review pass.
2. `Coach_Gen_Language_Rules.md` (protected), `Guardrails.md`, `claude/Coach_Gen_Protected_Docs.md`.
3. `claude/Coach_Gen_Book_Calibration_Log.md`. Every reaction of his, word for word, add-only. Read the sections for the Introduction, Chapter 1, the taste tests, and Law 1.
4. `Book/Book_Status.md` on his Mac. The book map (epoch, Google Doc id and score per chapter) and the ownership ledger (which chapter owns which story, idea and quote). Update it after every epoch.
5. Project memory (`preferences.md`) holds his working preferences for the book.

## 3. The references

His shelf, and why (his words, from memory): **Atomic Habits** (the presenting and layering of ideas, confident authoring that makes readers trust the book), **Mindset** (relatability, presentation, the structure of case studies), **The Courage to Be Disliked** in English, on purpose (conversation and book structure, and the narrator's perspective, though he found its dialogue "all or nothing" and tiring). Plus the two writing guides he follows because they mimic him: **The Elements of Style** (2018 Classic Edition, Strunk's text without E. B. White) and **On Writing Well** (6th edition). In taste test round 1 he rated Mindset and Atomic Habits highest.

**All of it is now in one folder on his Mac: `Book/Research/`.** Start with `Book/Research/README.md`, which lists every file. Nothing in it lives only in the book thread's cloud workspace any more.

- `Book/Research/reference_texts/`: the five books in full, as text. **Every line reference in the Book Rules, the Findings and the Notes points into these files**: "AH 449" is line 449 of `atomic_habits.txt`, "MS 61" is `mindset.txt`, "CG 2147" is `courage.txt`. Checked by md5 on 19 Oct: byte for byte the files the full read used. Count lines with `grep -n` or `sed -n`. The `*_pypdf.txt` copies have page markers, and `zinsser_pypdf.txt` is the one to quote On Writing Well from. The PDFs are in `Book/References/`.
- `Book/Research/full_read/`: the full read of all five books (also in the project, see section 4).
- `Book/Research/taste_tests/`: the passages he marked blind, the tests as he saw them, and the scripts. **`Taste_Test_Passages.md`** puts each reference passage next to his mark, flow score and reason word for word, with its line range in the text files. Also in the project as `claude/Taste_Test_Passages.md`.
- `Book/Research/measurements/`: the scripts and outputs behind every number in the notes, and the readability numbers below.
- Some notes name paths in the book thread's cloud workspace (`/home/claude/refs/ah_raw.txt`, `/home/claude/taste/passages.json`, `.../scratchpad/ah_measure.py`). Section 5 of the README maps each one to its file in `Book/Research/`.

## 4. The exploration

The full read (4 to 5 Oct), in the project and in `Book/Research/full_read/`:

- `claude/Full_Read_Agent_Brief.md`: what each book was read for: his reactions, what he hates in Claude's drafts, the 13 questions.
- `claude/Full_Read_Notes_1_Elements.md`: Strunk's 18 rules, the ones that explain his taste-test reactions, and where Strunk clashes with the Language Rules.
- `claude/Full_Read_Notes_2_Zinsser.md`: On Writing Well part by part, with warnings.
- `claude/Full_Read_Notes_3_Atomic_Habits.md`, `_4_Mindset.md`, `_5_Courage.md`: each has a book map with line ranges, chapter by chapter notes, answers to the 13 questions, the taste-test passages explained sentence by sentence, **15 testable moves to reproduce** (Atomic Habits section 5, Mindset section 5, Courage section 6), what not to copy, and measured mechanics.
- `claude/Findings_Guides.md`: the 16 findings from the two guides, and the warnings.
- `claude/Findings_Books.md`: the moves all five sources share, measured mechanics, and section F (how Clear and Dweck bring in research, quotes, headings, and how many terms a reader must hold).
- `claude/Full_Read_Progress.md`: the read log and the lessons it produced.
- `claude/Taste_Test_Passages.md`: the reference passages he marked, with his words and the text.

The Book Rules (R1 to R37) are built from these notes plus his reactions. A rule that cites "AH 572 to 607" is explained in the notes, and the text sits at those lines in `Book/Research/reference_texts/atomic_habits.txt`.

**Readability, measured 19 Oct** (standard Flesch formulas, body text only, front matter, notes, appendix and index left out). Grade is Flesch-Kincaid Grade Level. Ease is Flesch Reading Ease, 0 to 100, higher is easier.

| Book | Whole book | Introduction | Chapter 1 | Words per sentence |
|---|---|---|---|---|
| Atomic Habits | grade 6.9, ease 72.8 | grade 7.8, ease 70.5 | grade 7.0, ease 72.7 | 15.4 |
| Mindset | grade 6.5, ease 73.9 | grade 7.5, ease 71.2 | grade 6.8, ease 73.1 | 14.3 |
| The Courage to Be Disliked | grade 6.4, ease 74.3 | grade 5.1, ease 82.8 | grade 5.9, ease 75.4 | 13.9 |
| On Writing Well | grade 8.0, ease 69.9 | grade 7.8, ease 70.6 | grade 5.2, ease 82.5 | 18.2 |
| The Elements of Style | grade 8.4, ease 63.6 | grade 8.4, ease 68.9 | grade 9.2, ease 61.6 | 16.1 |

His six true pieces: grade 3 to 6, ease 75 to 93 (recorded in the Language Rules). The book so far, same method: Introduction grade 6.3, ease 79.9. Chapter 1 grade 4.8, ease 89.0. Law 1 Epoch 1 grade 3.8, ease 91.7.

## 5. The method that works (the lean method, his choice on 6 Oct)

1. Gather the chapter's material from the worksheet (`build_worksheet.js`), Obsidian, the Testimony collection and his articles. Sort it first: earlier agents filed material under the wrong Law (his warning, 7 Oct). Facts and keeper lines go in `Book/build/<chapter>/fact_sheet.md`.
2. Story options or key moments: each one written 3 ways, built differently, not reworded. He picks or mixes.
3. The epoch: the whole chapter written forward from the fact sheet around his picks, never by patching the last draft. One new Google Doc per epoch.
4. His markup: read with comments, log every word of it in the calibration log, then the next epoch.
5. When he says a chapter is ready, the book thread merges it.

**Google Doc layout, so the book thread can merge it without retyping** (`merge_epoch.py` reads the doc's structure):

- One grey line at the top asking for "x% as a book".
- A short label line ("Chapter 2") directly above the title. The title is Heading 1.
- Headings inside the chapter are Heading 2. The opening story has no heading (R31).
- The line the chapter is built to deliver (R35) is its own centred, italic paragraph.
- The Chapter Summary is a single-cell table whose first line is "Chapter Summary", then one bullet per line. The From Within You box is a single-cell table: title, one intro line, then one question per line.
- After the boxes: a horizontal rule, then the grey end note, starting "From Claude,". The merge stops there.
- Visible space after every paragraph (his rule, 15 Oct).
  - *Annotated 3 Nov 2026:* chapter epoch docs now follow the printed book's layout, his pick "a": a first-line indent and no gap, as in the book. Key moments docs and article drafts keep the visible gap. Built by `Book/source/make_review_doc.py` (html, then stage1 and stage2 through the Docs API, then check): 6 by 9 page, Georgia 10.5, centred small-caps headings, drop letters, figures nested in a borderless table so they never split, the end note on its own page after a page break. The merge still stops at "From Claude,". The label line is italic now, so run merge_epoch.py with `--label "Chapter N"`. Page numbers stay off (he adds them with Insert > Page numbers).
- Research: for every study or book cited, give the exact phrase in the chapter it belongs to, and the full source. The book thread turns that into the Notes page (Penguin style: page number, phrase in italics, source).

## 6. Where the book stands (19 Oct)

*Annotated 20 Oct 2026: the newest state of Chapter 2 is in section 8.*

- **In the master draft:** Introduction (epoch 4) and Chapter 1, Staying Who You Are (epoch 3). `Book/5_Laws_of_Lasting_Change_Draft.pdf` and the print booklet beside it.
- **Chapter 2, Law 1, Reset My Course: Epoch 1 is waiting for his markup** (Google Doc "5 Laws Manuscript, Law 1 Epoch 1", id 1k2w2CLAkdSHRzSURMXKHS7pj38DAHAYvBYcjot0XFGg, untouched since 7 Oct). Working files: `Book/build/law-1/` (fact_sheet.md, outline.md, epoch1.json, epoch1_chapter.md). Built from his picks in "5 Laws Manuscript, Law 1 Story Options" (id 13ceHYWQssrnse9qGiI3wehSHgBQyv1GC0tkuUQD-Auo).
- **Open questions to him, from the Law 1 Epoch 1 end note:** (1) a name for [NAME B], who now holds David's planned trip, (2) whether the reason given for quitting his writing course is true ("An unfinished manuscript can't be judged. A finished one can."), (3) whether the breakdown of all 5 Laws stays at the start of Law 1 or gets a short chapter of its own. Also unanswered: should "If I don't try and fail, I'm lazy, not incompetent" (live coaching, 22 Sep, filed under Law 3) move to Law 1's hidden reward.
- **His Law 1 notes still to apply (7 Oct):** split David's story across several people with different names and scatter them through the chapters (ask him for names), and his worry that a chapter built only from its stories would be too short. His "remember this" on unpacking every leap of logic is now Book Rule R37.
- **Laws 2 to 5:** not started. The ownership ledger in `Book_Status.md` lists the material each one already owns.

## 7. Working on his files

- His Mac is the master. Working files go in `Book/build/<chapter>/`, never in the project.
- Never re-type a file. Edit in place with a short script on the Mac. To write a file from the cloud, stage it under a new name, commit it to `Book/build/incoming/`, check the md5 on the Mac, then `mv` it into place. A commit once wrote a stale cached copy over the master.
- The Book Rules and the Language Rules are protected: show him the exact lines, and write only when he names the change. The calibration log and other working docs are add-only.

## 8. Handoff, 20 Oct 2026: Chapter 2 starts with a grilling

**Start here:** the next chat works on Chapter 2 (Law 1, Reset My Course). First a grilling on what Chapter 2 really needs to accomplish, then the plan. No writing yet.

His words (20 Oct): "I think one big thing I needed was a grilling(not specific to the skill) on "the big thing or things or theme" that needs to happen in chapter 2. Like how I imagine shakespeare might've written a complicated first act, but once there are too many ideas he had to ask himself "what does this first act REALLY mean and NEED to accomplish?", only then the masterpiece can be born."

### Where things live

- **Skill:** `coach-gen-writer` (saved 20 Oct). It replaces inside-the-introvert, lasting-change-letters and write-book-from-material. He keeps the old three until the new workflow is confirmed. His words: "I will delete once I confirm the new workflow works." Use coach-gen-writer.
- **Law 1 material and what it owns:** `Book/Book_Status.md`, sections "Law 1 (epoch 1, 7 Oct)" and "Law 1 (article series, newest layer, 19 Oct)".
- **The article series "How can you be busy but lazy?":** Parts 1 and 2 published on the Inside The Introvert board in Notion. Part 3 draft 2 is Google Doc 1AjvghqVm5Xk6BOCHcsCpZI0q5VhDfwGsO47u4OVyoIA (the doc is the only copy now). His markup of draft 1 and his reaction to draft 2 are in the calibration log, sections "Law 1 Part 3 draft 1, his markup (18 and 19 Oct)" and "Law 1 Part 3 draft 2 (19 Oct)".
- **Law 1 Epoch 1** (7 Oct, never marked up): Google Doc 1k2w2CLAkdSHRzSURMXKHS7pj38DAHAYvBYcjot0XFGg, working files in `Book/build/law-1/`.
- **The Energy Audit** (coined 19 Oct) is written into the worksheet, `build_worksheet.js`, TRACKER_ROWS, Law 1 Core Exercise.
- **The A/B test** that produced coach-gen-writer's steps 4 and 5: `claude/AB_Test_Writing_Skills.md`, and `Book/Research/ab_tests/` on his Mac.

### Done (19 and 20 Oct)

- Part 3 draft 2 was written. His reaction (19 Oct): "I actually really like that the piece is full of ideas, every paragraph is quotable and seems brilliant on its own with fresh ideas. What is not right for me though, is that we already have 2 parts published, so having this new fuller paradigm seems like a commitment. How about you try finishing the chapter first(aka, the whole chapter 2, and the flow of chapter 2. using the published parts as material but not as strict black boxes). then we'll see how part 3 and next can be sliced"
- Then: "don't write yet, plan first." A Chapter 2 plan was given in chat, and he parked it: "ask me again later for chapter plan." That plan was never saved to a file and was lost when the chat was summarised. Its decisions survive, below.
- The A/B test ran 2 valid rounds. The mixed method won both, and it is now in coach-gen-writer.

### In progress, waiting on him

- **Chapter 2 plan, decisions that survive:** the opening is the diet pair (he gave no preference, so the default stands). All Epoch 1 material is kept (no preference, so keep). Still open: does the full breakdown of the 5 Laws open Law 1, or get a short chapter of its own?
- **Older open questions** from Epoch 1's end note (section 6): the writing-course reason, and whether the 22 Sep line "if I don't try and fail, I'm lazy, not incompetent" moves to Law 1. [NAME B] does not apply in the articles, where David keeps the trip. His 7 Oct notes: split David's story across several people, and his worry that a chapter built only from stories is too short.
- **Part 3** is parked until the chapter's flow is settled. Then decide how Part 3 onward is sliced.
- **A stray line**, "CLAUDE EDITED THIS AGAIN", sits at the top of the project copy of `Coach_Gen_Language_Rules.md`. The doc is protected. Remove it only if he says "delete that line".

### Next, in order

1. Open with coach-gen-writer, chapter ending, Law 1. Load as its step 2 says (rules, research, state). Read the Law 1 material: the two Law 1 sections of the ledger, Parts 1 and 2 on Notion, Part 3 draft 2, and Epoch 1.
2. Grill him with the grilling skill (rounds, a recommended answer on every question) on what Chapter 2 really needs to accomplish: the one thing the reader must leave with, the chapter's job in the book (Chapter 1 promises that the first Law turns you around), which ideas carry it, and which belong to another chapter or go. Build the recommended answers from his material. No plan and no writing during the grilling.
3. Write down what he settles: the blank and the one thought (coach-gen-writer step 3), and the leading word (step 4), in a new outline file in `Book/build/law-1/`. Log his answers word for word in the calibration log.
4. Then the plan: the key moments, and where Parts 1, 2 and 3 sit in them. Show it. No writing until he says.
5. Then decide how Part 3 onward is sliced.

### Rules for this work

- Newer context wins in a conflict (his rule, 19 Oct). The article series beats Epoch 1.
- Parts 1 and 2 are material, not fixed blocks.
- Plan before writing. The skill's chapter ending says not to stop for an outline, but for this chapter he asked for a plan first, so stop after the plan.

### Suggested skills

- coach-gen-writer, chapter ending, for the whole piece.
- grilling, for step 2.
- handoff, before leaving the chat.
- merge-epoch-to-book, only when he says the chapter is ready (the book thread).

## 9. Handoff, 4 Nov 2026: client case studies (a grilling), then Chapter 3 epoch 5 review and epoch 6

*Annotated 4 Nov 2026: the newest state is in section 10. R41 and review item 3d, named below, were removed the same day.*

**Start here:** the next chat learns how Dweck writes client case studies and what makes his own way of writing a client his, grills him on combining the two, then reads his markup of Chapter 3 (Law 1) epoch 5 and writes epoch 6.

His words (4 Nov): "I actually think we should learn how to write client case studies like dweck, first and foremost" "while at the same time extracting to an essence what is it that makes my style of writing client essence my style, so that we can combine the two." "will need another grilling session about the above". Asked whether the epoch review and epoch 6 go in the same chat: yes.

### Where things live

- **Book Rules**, new on 3 and 4 Nov (Mac master `Book/Coach_Gen_Book_Rules.md`, mirror `claude/Coach_Gen_Book_Rules.md`): /privileged in section 0, the R38 annotation, the layout annotation under "Paragraphs look separate" (3 Nov). R3 annotated (money and health), R3b annotated (built details: what is allowed and what is not, 40 lines), new R41 (search the brain before you build), review pass 3c and 3d (4 Nov).
  - *Annotated 4 Nov 2026:* removed the same day at his order: R41, line 7 of the R3b annotation ("Search the brain first (R41).") and review item 3d. The R3b annotation now has 39 lines. See section 10.
- **Built Detail Test:** Google Doc "5 Laws, Built Detail Test (20 questions)" (id 12X8BsIL9Wk2f4E6ggacLbUbB0f3v23NOMDNYriAZ7T0). His marks and every why: `Book/Research/taste_tests/built_detail_test_marks_full_2026-11-04.md`. Summary in the calibration log, "Built Detail Test, and the rules it produced (3 and 4 Nov)".
- **Chapter 3 epoch 5:** Google Doc "5 Laws Manuscript, Chapter 3 (Law 1) Epoch 5" (id 1WPWfz9vmjxd2aeNZJRTXkkV6vNBPG5tEEYvpBAoOv2c, Drafts folder 1rmgnWP9AHkgZjDnk6yvv-9SDaMx5Aq1K), the first draft in the book's layout. Text as delivered: `Book/build/law-1/epoch5_chapter.md` and `epoch5.json`. Written review pass: `review_e5.md`. Claude's scores: `scores_e5.md` (7.3, an upper bound). His notes so far: `markup_log.md` (his 3 Nov rewrite of the points-system paragraph, and the $200 decision).
- **Review doc builder:** `Book/source/make_review_doc.py` (html, stage1, stage2, check), `Book/source/nest_fig.py`, `Book/source/review_scorecard.html`. The coach-gen-writer skill's "Deliver the chapter" step (saved 3 Nov) says how to run them.
- **Dweck's cases:** `Book/Research/reference_texts/mindset.txt`. Read so far (4 Nov): the note on changed names (lines 68 to 74), five cases (1203 to 1222, 1806 to 1815, 1885 to 1905, 2249 to 2255, 7257 to 7270), and three where a person's past is told (674, 1568, 5947). His ratings of Mindset passages: `claude/Taste_Test_Passages.md` and the calibration log's taste tests.
- **His own client writing he praised or rewrote:** the calibration log (the Melina scene notes in taste test round 2, the Chapter 1 and Introduction epochs, the Law 1 story options), and `Book/build/law-1/markup_log.md` (the epoch 4 and 5 notes).

### Done (3 and 4 Nov)

- Chapter 3 epoch 5 written whole, with a written review pass (87 joins), built in the book's layout, scored.
- The book-layout delivery is now in coach-gen-writer (he saved it).
- Built Detail Test made and marked (59 OK, 38 No, 3 open). The rules above folded on his go.
- $200 stays in Chapter 3: money may show a struggle.

### In progress, waiting on him

- **His markup of epoch 5.** He has rewritten the points-system paragraph and may mark more. Open in the end note: plough and cow, or farms and barns, goats and oats, wheat and sheep. "Business" as Figure 3.2's first column. Who the 168-hour project is credited to. Claude's two flags on his rewrite, not changed: "and so begins" (the rest is past tense), and "the pattern he's so familiar with" sitting three paragraphs before "three patterns of his own" (R32).
- **One brain fix:** F-141 reads "stand at the front". In the call (2026-10-26, at 1:20:02) it is "stand in front", his Naruto image of standing in front to protect the village. Correct it the way `claude/Brain_Rule.md` says.

### Next, in order

1. Open with coach-gen-writer, chapter ending, Law 1. Load as its step 2 says, including the new R3, R3b and R41 lines.
2. Measure before the grilling (facts are the chat's job): every client case in Mindset (length in lines, how the person is named and tagged, what surface is given, where their own words sit, how the result is told, where Dweck's own line sits, how background is marked). Then the same for his own client writing that he praised. Save both to `Book/Research/case_studies/`.
3. Grill him with the grilling skill on how to write a client case study: what to take from Dweck, what is his, and how the two combine. Recommended answers built from the measurements.
4. Fold what he settles into the Book Rules with propose-language-rule, on his go.
5. Read his epoch 5 markup (`read_file_content` with `includeComments: true`, diffed against `epoch5_chapter.md`). Log it word for word in `markup_log.md` and the calibration log.
6. Epoch 6: write whole from the material (R4) with the new rules, run the written review pass (step 9), score it, build it with make_review_doc.py, deliver.

### Rules for this work

- Never print a real client name. Composite names only. Never print "purple bird": it is David's camp story and published speech (F-70), so it identifies him.
- The built-detail lines say what is allowed. They are never a list of musts.
- Quotes of his in a rule pass the cold-read test (propose-language-rule).
- If this chat gets summarised, run /handoff again.

### Suggested skills

- coach-gen-writer, chapter ending, for the epoch work.
- grilling, for step 3.
- propose-language-rule, for step 4.
- google-workspace, before building or changing the Google Doc.
- handoff, before leaving the chat.

## 10. Handoff, 4 Nov 2026: the Case Study Test, round 2 (20 records, 5 ways each), then Chapter 3 epoch 5 review and epoch 6

**Start here:** the next chat builds round 2 of the Case Study Test from his own records: 20 records, each written 5 ways, for him to score. When the case-study lines are settled, the same chat reads his Chapter 3 epoch 5 markup and writes epoch 6. The grilling planned in section 9 is done. Do not grill again unless he asks.

### His words, so he never has to repeat them

1. The goal (4 Nov): "I actually think we should learn how to write client case studies like dweck, first and foremost" "while at the same time extracting to an essence what is it that makes my style of writing client essence my style, so that we can combine the two."
2. Where: "uh, the chat handling the handoff's grilling was way off from my expectation. let's just do the grilling of presenting case studies here. postulate first the objective, and how its best achieved"
3. His own stories: "my own stories can be in. I think it's good too to have it be short and sweet."
4. On Claude grilling him with its own picks: "uh you're just talking to yourself. how do we test now? assume I trust your researches."
5. After round 1: "I think you are missing the whole fucking point here." Then the objective, below, and: "So use my material and like expand it and compare and see how I score it. it's not about how similar are the fucking scores between dwecks passage and my fucking passage. why is this so fucking hard. If you are completely fucking lost, just ask me for directions"
6. The size: "do more records godmammit, like 20x5 from earlier." (20x5 is the Built Detail Test's shape: 20 records, 5 versions each.)
7. This handoff: "don't fucking let the last test I fucking marked to go to waste too. fuck man. give a fucking detailed handoff, I don't want to repeat these instructions again"

### The objective

Claude's words on 4 Nov, which he holds it to ("which these are your fucking words"):

1. It reads like Dweck. The reader trusts it, it moves fast, and it lands on the person's own line.
2. It sounds like you. Your stance: curious, the editor and not the hero, and the client already capable. In your simple words, with your vividness.
3. It stays inside the built-detail lines you set on 4 Nov.

### What the test is, and what it is not

1. It is his material, built out in different ways, scored by him against the three lines above. His scores are the data.
2. It is not a contest with Dweck. No Dweck passages in round 2. Never compare his scores of Dweck with his scores of his own material.
3. It is not a grilling. Do not ask him questions and answer them yourself. The test is how he gives directions.
4. If you are lost, ask him for directions in one short question. Do not guess at a new format.

### Round 1, done and marked (4 Nov)

- Google Doc "5 Laws, Case Study Test (8 passages)" (id 1xAwmGFpjozX_NZhuKM30pIPySXkb7X_lB0eY5wuRTMo). Dweck 1, 3, 5, 7 and Claude 2, 4, 6, 8 (from his material), mixed, no sources shown.
- His marks and every why, word for word: the calibration log, "Case Study Test round 1 (4 Nov)", and `Book/Research/case_studies/case_study_test_marks_2026-11-04.md`.
- The key (what each passage is, every built detail in Claude's four): `case_study_test_key_2026-11-04.md`. Dweck's moves and his essence, with evidence: `case_study_tables_2026-11-04.md`. The measurements behind them: `dweck_cases.md`, `gen_client_writing.md`, `measure_output.md`, `compare.md`. All in `Book/Research/case_studies/` on his Mac.
- Claude's four scored: Aiman 2, Bayu 7, his door-to-door story 8, Melina 6.

What round 1 says, for round 2 to apply (Claude's reading of his marks):

1. Claude's client cases were under-built. A gap between two recorded moments needs one or two reasonable bridges from the R3b Allowed list. Aiman (2): "nothing after the first sentence make any sense". Bayu (7): "Middle could use some reasonable assumptions we talked about." Melina (6): "The whole thing happened so fast? Maybe requires one more reasonable additions."
2. Length follows the story: "not all stories has to be short, and not all stories have to be long." Short works only when every step is there (his own story, 8: "Good and concise, short and sweet.").
3. The best cases carry an argument. Dweck's Loretta (8): "good example of using case study to enhance an argument". Kristina (9): the "What could they have said instead?" line.
4. No advice, no diagnosis, no know-it-all voice. Dweck's cab driver (7): "I don't like the advice and diagnosis and knowitallness". This is why the objective asks for his stance, not hers.
5. Keep: a short session line of his (Bayu: "“So you’re looking for warmth” is a nice touch."), an open story about himself, and vivid odd stories of what people do (Nicole, 8: "I don't mind this vivid and clients do crazy shit type of stories.").

### Round 2, the spec

1. 20 records, 5 versions each, 100 passages, in one new Google Doc, laid out like the Built Detail Test (id 12X8BsIL9Wk2f4E6ggacLbUbB0f3v23NOMDNYriAZ7T0): the record first, then its 5 versions.
2. The record: the brain's text, in print names, with its legacy_ref. He needs it to judge what was built.
3. The 5 ways. Each version is built a different way, not reworded:
   1. Situation first: who they are and the problem, then the session.
   2. The session as a scene: his question, a pause, what they said.
   3. Their own line first, then how they got there.
   4. The reader first: one line about the reader's own life, then the person.
   5. An argument inside the case: the case proves a point on the way, like Dweck's Loretta (the other readings) and Kristina ("What could they have said instead?").
4. Under each version, one grey "Built:" line naming every built detail and the R3b section that allows it. Nothing built goes unlisted.
5. After each version, a box for his mark: Mark (1 to 10) and Why, judged against the three lines of the objective. The doc's one-line "how to mark" says so.
6. Apply round 1's lessons in every version. Length follows the story, so the five versions of one record may differ in length.
7. Print names only. Hide the person with swaps where needed (R3b Allowed), and keep every other detail consistent with the swap.
8. Send him the link. Do not mark, predict or score it for him.

### Records to use (pick 20, mix the people)

- David: F-132, F-136, F-96, F-123, F-119, F-11, F-141, T-308, F-17, F-50. For F-141, fix the brain first (Still open, 1).
- Bayu: W-01 and W-02 (the gas stove), W-05 (the hidden agenda, with his poker line), W-06 and W-07 (anger as a defence, a cool head two weeks later), W-14 and W-15 (scolded, the white room and the wall), W-17 (the house and the toys), W-19 (the massage, "I didn't get the crack today.").
- The sales client: T-018.
- His own stories: A-01, F-85, F-104, F-892, F-43, F-90.

Read each one fresh from `brain.entries_full` (text, original_text, note, status, certainty) before building. Map names with `brain.personas`. Skip any record whose status or note says never use.

### Records to leave out

1. Aiman F-39, Bayu W-10 to W-12, Melina F-31, F-36 and F-28, Dan Sato F-40, Andi F-41. Two attempts at round 2 in the 4 Nov chat stopped mid-build on drafts from these records, and nothing was delivered. Do not rebuild them.
2. Any record with a health condition, a diagnosis, a medicine, a health reading or a body weight. Any money figure without a human side (R3).
3. Entry 879's cause, anything marked never use, and anything that names "purple bird".

### The Book Rules now (end of 4 Nov, checked on his Mac)

1. In: the R3 annotation (money and health), the R3b annotation (built details: Read this first, Never, Border, Allowed, Use very carefully, His own stories, 39 lines), review item 3c.
2. Removed at his order: R41, line 7 of the R3b annotation ("Search the brain first (R41)."), and review item 3d. His words: "just fucking remove everything related to this error from the rules first".
3. What he had meant: "me saying "first sentence can be its own rule that is prevalent and stronger". is referring to the first sentence of rule 7." That sentence was "Look in the brain first." Claude had promoted the whole line, with the read-the-source part he had turned down: "this seems like a giant waste of tokens and time, no? how big is this impact. if I can't trust what I have in brain, why have brain in the first place."
4. Open, his call only: whether a rule holding just "Look in the brain first." comes back. Claude's wording, unanswered: "**R41. Look in the brain first.** Before you write any detail of a person, a story or a quote, search the brain for it. This holds for all writing, not only built details." Write nothing to the rules without his go on the exact lines.
5. For this work, build from the brain record. Do not go back to calls or transcripts to check a record's wording unless he asks.

### Still open

1. F-141 in the brain still reads "stand at the front" (checked 4 Nov). In the call (2026-10-26, at 1:20:02) David's words are "okay lah, maybe I play one game of Dota before I go and stand in front": his Naruto image, Hinata standing in front to protect the village. Fix it the way `claude/Brain_Rule.md` says, before F-141 goes into the test.
2. Chapter 3 epoch 5: his markup, the end-note questions and Claude's two flags, all as in section 9, "In progress".

### Next, in order

1. Open with coach-gen-writer. Load the Book Rules (the R3 and R3b annotations, 3c), the calibration log entries "Built Detail Test, and the rules it produced" and "Case Study Test round 1", and the round 1 files in `Book/Research/case_studies/`.
2. Fix F-141 (Still open, 1).
3. Pick 20 records from the list and read each from the brain. Build the 100 versions to the spec. Check each "Built:" line against R3b. Read each version again as the reader would.
4. Build the doc (google-workspace skill). Check that it opens and reads clean. Send him the link with one line on how to mark.
5. When he has marked: read the doc with its comments, log every mark and why word for word in the calibration log (add-only, before "## Hold-out"), and save the marks to `Book/Research/case_studies/case_study_test_round2_marks_<date>.md`.
6. Read the marks: which ways score high, for which kinds of record and person, and why, in his words. Show him in short numbered lines. Then propose case-study lines for the Book Rules with propose-language-rule. Write only on his go on the exact lines.
7. Then section 9, steps 5 and 6: his epoch 5 markup (read with comments, diff against `epoch5_chapter.md`, log in `markup_log.md` and the calibration log), then epoch 6, written whole, reviewed, scored, built with make_review_doc.py and delivered.

### Rules for this work

1. When he says do A, do A. When lost, ask him for directions.
2. Never print a real client name. Print names come from `brain.personas`: David, Melina, Bayu, Andi, Aiman, Dan Sato. Never print "purple bird" (F-70, it identifies David).
3. No never-use material, no weights or health readings, nothing from entry 879's cause.
4. Every built detail stays inside R3b and is listed.
5. No em dashes and no semicolons in his docs.
6. Talk to him in short numbered lines he can take in at a glance.
7. Protected docs (Book Rules, Language Rules): show the exact lines, write only on his go, Mac master first, then the mirror from the same bytes. Add and annotate only.
8. Send a fresh link after every big edit.
9. Do not bring up next steps that are not part of this work.
10. Never tell him a chat was compacted or summarised. If it happens, write a new dated handoff section.

### Suggested skills

- coach-gen-writer: load first, for the voice, the rules and the epoch work.
- google-workspace: before building the test doc and the epoch 6 doc.
- propose-language-rule: Next, step 6.
- handoff: before leaving the chat.
- grilling: only if he asks for it.
