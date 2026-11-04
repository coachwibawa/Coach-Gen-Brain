---
name: "coach-gen-writer"
description: "Write, mark up, redraft or publish Coach Gen's pieces in his voice: Inside The Introvert articles, Lasting Change Letters editions and chapters of his book 5 Laws of Lasting Change."
---

# Coach Gen Writer

One writer for everything he publishes in his voice. A shared core (context, method, checks), then one of three endings:

- **Article:** Inside The Introvert, a newsletter piece in 3 fields, published to Notion.
- **Letter:** Lasting Change Letters, the same 3 fields, built from a book he has read plus what he saw in it as a coach.
- **Chapter:** a chapter of the book 5 Laws of Lasting Change, delivered as a Google Doc he marks up.

Everything is written to book standard. His words (19 Oct 2026): "specifications has changed, and now I want the article thread next door to write like a book, so that means getting all your context, especially the references and your exploration of it." On 20 Oct he extended it to Lasting Change Letters.

**Argument.** The kind of piece, then:

- **Article:** the raw material itself. A transcript, a worksheet field, a paragraph he typed while thinking out loud. Not a topic.
- **Letter:** the book plus his realisation. Never pick a book for him and never write about one he has not read.
- **Chapter:** a chapter name ("Law 3", "Introduction"), or `next` (the first chapter in the book map with no draft yet), or `all` (stop 1 for every undrafted chapter, one key-moments doc each), or `picked <chapter>` (log his picks, then build), or `marked <chapter>` (log his markup, then redraft). A chapter with no name means `next`. With picks or a marked draft waiting, do that first.

With no argument, ask what he wants to write and wait. Do not scan the worksheet or propose angles unprompted.

**This skill is a procedure, not a rulebook.** The rules live in protected docs. Never restate them here or into the chat. A second copy drifts from the protected one, and that drift is what once made one piece take 10 drafts.

---

## 0. One chat per piece

- Start a new chat for each piece: an article, a letter, a chapter, or one part of a series. Open it with this skill, for example "/coach-gen-writer article" plus the material, or "/coach-gen-writer chapter Law 2".
- Keep that chat through draft, his markup and redraft. His reasons for a mark live in the chat until they are logged.
- Start a fresh chat when the piece is approved or published, or when the chat gets summarised. A summary drops the rule docs out of memory.
- Before leaving a chat, run /handoff. It updates `claude/Book_Writing_Handoff.md`, so the next chat starts where this one stopped.
- Write in the conversation, not through fresh agents. His words (6 Oct 2026): "This new workflow is too token and time inefficient, and doesn't seem to accomplish the objective of generating creativity and new lines or constructions." A fresh agent re-reads about 80 KB of rules before it writes a word, and a beat-by-beat outline leaves it nothing to invent but the wording. Fresh agents are for blind A/B tests only. Most of the cost of a piece is the number of steps, each re-reading the chat, not the files read once.

## 1. Where everything lives

His Mac folder `/Users/coachwibawa/Documents/5 Laws of Lasting Change/` (device bridge, `$HOME/mnt/5 Laws of Lasting Change/` in device_bash):

- `Book/Coach_Gen_Book_Rules.md`: **the master Book Rules.** The project copy `claude/Coach_Gen_Book_Rules.md` is a mirror. After any change, write the mirror from the same file with `project_write` and `local_path`. Never retype it.
- `Book/Book_Status.md`: the book map (epoch, Google Doc id and his score per chapter) and the **ownership ledger** (which chapter or article series owns which idea, story and quote). Create it from `claude/Full_Read_Progress.md` and the calibration log if it does not exist.
- `Book/Research/`: the five reference books as text, the full read, the taste tests and the measurements. Start with `Book/Research/README.md`.
- `Book/build/<chapter>/`: working files per chapter (`fact_sheet.md`, `outline.md`, `key_moments_eN.md`, `epochN.json` with the exact text delivered). Working files go here, never into the project.
- **The Coach Gen Brain** (Supabase project `zjedqjiuxkoncwsmylls`, schema `brain`): the one home of all his material. It replaced the worksheet, the Obsidian vaults and the Testimony collection on 27 Oct 2026. Read `claude/Brain_Rule.md` first. Those old files are frozen history. Read them only to check something.

In the project: `Coach_Gen_Language_Rules.md` (protected, read only), `Guardrails.md`, `claude/Coach_Gen_Protected_Docs.md`, `claude/Coach_Gen_Book_Calibration_Log.md` (his reactions word for word, add-only), the research findings and notes (step 2), and `claude/Book_Writing_Handoff.md`.

In Notion: Inside The Introvert (`collection://d73333e2-807b-4aee-a4ce-0bb96ef282e7`), including the Laws of Lasting Change Acts 1 to 3 and his true-corpus pieces (My Dragon series, The Social Battery Myth, On Blind Spots, How Do You Reset?), and Lasting Change Letters (`collection://409042c2-c5a3-4ebd-a21c-10621af68452`).

In Google Drive: session transcripts (for example "Sri 3 Transcript"). **For checking a fact only. Never a source of new detail.**

**Writing to his Mac.** `device_commit_files` can write a stale cached copy when a staged path was used before. On 6 Oct it put an older Book Rules over the master for a minute. Stage under a new file name, commit to a new path, check the md5 on the Mac, then `mv` it over the target. Small text edits go in place with a short python script in device_bash.

If the Mac is not reachable, say so in one line, use the project copies, and tell him they may be stale.

## 2. Load first, draft second

Read in full before writing a sentence. Once per chat, not once per draft.

1. **Rules.** `Coach_Gen_Language_Rules.md` (his voice: the words he would say), the Book Rules (the craft: how sentences, paragraphs, client stories and warmth connect), `claude/Coach_Gen_Protected_Docs.md` (what you may not write to) and `Guardrails.md`.
2. **Research.** `claude/Findings_Books.md`, `claude/Findings_Guides.md` and `claude/Taste_Test_Passages.md`. His words (19 Oct): "the most important is the research(read through of the book)." The five Full Read Notes (`claude/Full_Read_Notes_1_Elements.md` to `_5_Courage.md`) are the chapter-by-chapter notes the findings were built from, about 130,000 tokens together. Open one only when a rule or finding cites it. A citation like "AH 449" is line 449 of `Book/Research/reference_texts/atomic_habits.txt`. Count lines with `grep -n` or `sed -n`.
3. **State.** `Book_Status.md`, the calibration log entries for this piece (for a chapter, also the Introduction's), and the handoff note when this continues earlier work.

For articles and letters, section H of the Book Rules falls back to the Language Rules: numbers as digits, simple words for readers with English as a second language. Contractions are fine in warm or spoken lines. On word count, his words (5 Oct): "for now, disregard word counts." Report the count, never cut to it. His first article drafted with the Book Rules ("3 Stages of Consistency", 5 Oct 2026) scored 90%.

Do not draft from memory of the rules. Do not summarise them back to him.

## 3. Settle the blank

Section 2 of the Language Rules and R1 of the Book Rules are the test that overrides everything else. Fill in "this piece is about ____" and give it back to him in one line before drafting. Every paragraph gets measured against it later. In a letter, the blank is his realisation, never the book's subject.

## 4. Find the leading word

After settling the blank and before drafting, find or coin the one term the piece hangs on (the way "Momentum Engine" carries Law 4). Prefer a word from his own material. Build the piece's transitions and closing around it. In a chapter, this is the thread word in the outline (R32).

## 5. Ground the reader

Before drafting, list the ideas the reader already brings (a reader with English as a second language who has not read his other pieces). While drafting and again in the review pass, check every paragraph leans only on ideas the reader brought or met earlier in the piece. If a paragraph needs an idea not yet grounded, ground it first or cut the move.

Steps 4 and 5 came from the writing-skill A/B test (`claude/AB_Test_Writing_Skills.md`, 19 to 20 Oct 2026), adapted from Matt Pocock's writing-fragments, writing-shape and writing-beats skills (github.com/mattpocock/skills, MIT licence). With them, blind drafts scored about 8.1 and 7.3. Without them, about 4.3. His call: "I am confident enough that mix is the choice here."

## 6. Take the material

- **The brain.** Query `brain.entries_full` with `execute_sql` for the Law and the types you need (the SQL examples are in `claude/Brain_Rule.md` section 3). Read all of the Law's material, not a sample. Everything in it is real, his words and his sessions, unless `certainty` says `built` (invented for a persona). `recorded` is from a recording, `recounted` is his memory of a client. Never ask him to verify it. Sort before use: earlier agents filed material under the wrong Law (his warning, 7 Oct). Old IDs (F-, T-, W-, WS-, OBS-, BL-) are in `legacy_ref`. Search gold only. Raw chunks are never printed as a quote.
- **The prescription.** Build the method, and an article's closing third, from the Law's Core Exercise, Hidden Reward, self-directed questions and DoD lines. An invention that fits well is the worst failure on record here, because it reads fine and still replaces his method. The story is yours to shape. The coaching is not.
- **Testimony lines and the cast.** They are in the brain too (types and personas, see `brain.personas` and `brain.used_in`). Use each text exactly as written. Never print anything with status `never use`: weights, health readings, money figures, health framing, third parties' private stories.
- **The ledger.** An idea, story or quote another chapter or series owns gets, at most, one callback line here.
- **A letter's material:** choose by fit, following section 8 of the Language Rules. Name the core of the book's idea, test each candidate against it, take the one that shows the core happening, and prefer a live session over an exercise.

## 7. Stories about people he coaches

Follow Book Rules R3b: true core, built surface. The core comes from the records. The surface is built so a reader can follow it and the person cannot recognise herself. List every built detail under the draft, next to what the records say, so he can strike any of them. He often picks the surface himself on the next round. Use what he gives.

Composite names in print (Melina, David, Dan Sato). Never "my clients".

## 8. Draft whole

Write the draft whole, from the material forward (Book Rules R4). A redraft starts from the material and the blank, never from patching the last draft's sentences. The ending below says what the draft holds.

## 9. Check it yourself before he sees it

**Do the review pass in writing, not in your head.** (Added 3 Nov 2026, at his go.) After the draft is whole and before the Google Doc is built, save `Book/build/<chapter>/review_eN.md` on his Mac (for an article or a letter, the same file in its build folder). It holds three lists:

1. **Every paragraph join:** the reader's one-line question, and the first words of the next paragraph that answer it (Book Rules R5). A join fails when no question fits, or when a sentence takes for granted something the reader has not read yet (Book Rules R7, step 5 above).
2. **Every thing the reader must carry:** its one name, and any other name it picked up in the draft (Book Rules R32). Two names for one thing fail.
3. **Every "so", "then", "because" and time word:** the relation it claims, checked against what actually happened (Book Rules R6). A cause or a time order that is not real fails.

Run the old core rules first (R4, R5, R6, R32), then the newest rules, so new rules do not crowd out old ones. Fix every fail by rewriting that passage from the material, never by bolting on a connector phrase. A glue phrase added to pass a check is how taste test round 3 became "robotic and repeated". Put one line in the end note: "Review pass: N joins checked, M fixed." The file stays on his Mac, out of the Google Doc.

Why: Chapter 3 epoch 4 (30 Oct) passed a review done in the head and still broke R4, R5, R6 and R32. Claude scored it 7.5. His words (3 Nov): "I didn't read all the way, I was half ready to drop the book. due to the cracks and obvious flaws." And, on the rules being skipped: "why do I have fucking rules if you can say you didn't follow it to 5 of them on fucking thinking model".

Then the rest of the review:

Run section I of the Book Rules as the review pass, then section 12 of the Language Rules, then the grounding check from step 5 again. Fix spelling and grammar silently, keeping his voice (R15). Then the mechanical checks, each of which has caught real defects:

- `pip install textstat==0.7.3 --break-system-packages`, then word count, words per sentence, Flesch-Kincaid, reading ease, and named things per 100 words. Pin that version. The current release needs an NLTK corpus this container cannot fetch.
- Diff the vocabulary against his true corpus. Watch unseen abstract nouns of 7 or more letters. If the corpus files are gone after a container reset, rebuild them from the Insight 1 fields of the six true pieces on the Notion board (Language Rules, section 1).
- A script for em dashes, semicolons, numbers, British spelling and "my clients". Do not call a draft clean until the script says so.

Check every fact against the material yourself. No checker agent. Report the numbers as one line, never as evidence the draft is good. Two drafts once scored identically and were not remotely the same piece.

## 9b. Score it before he does

For a book chapter, score the draft on the six traits in the Scorecard section below, one line of reason per trait, and save it to `Book/build/<chapter>/scores_eN.md` before delivery. Keep your scores out of the Google Doc. Articles and letters may use the same six traits when he asks for a score.

## 10. His markup

- Show the draft with no preamble and no defending choices he has not questioned.
- He marks up inline, line by line, comments in the doc, or rewrites a passage himself. Keep his rewrite word for word, except for silent grammar fixes. Read a Google Doc with `read_file_content` and `includeComments: true`, and diff it against what you delivered to find what he typed.
- Apply the codes he types in comments: [] and "" and /privileged (Book Rules section 0), and /rhyme-this, which runs the rhyme-this skill on the text the comment sits on. Nothing runs when he types a code in Docs. It is read here, in the markup round.
- Log his score, picks, comments and inline notes in the calibration log **word for word**, with the words each one sits on. Add only. Never condense.
- When he fills in the scorecard, log his six scores next to yours and follow the Calibration paragraph of the Scorecard section. Show him your scores only after he has sent his.
- Apply his notes, then re-read the whole beat around each fix. Repairing one line by announcing an ending early is how an arc got broken once.
- When he says "regurgitate", give the full piece, all fields with their header lines.

## 11. Feed what you learn back

- What he typed into the text becomes a keeper line, word for word. It is not a rule.
- Propose a rule only when his markup produces one that is not already in the Language Rules or the Book Rules, and only from something he said: a stated reason, a complaint, a verdict. Check it for overfitting first. An edit he made without explaining it is an observation. List those separately with no rule attached.
- Both rule docs are protected. Show him the exact lines and which doc they go in, and write only when he names the change in that turn. Book Rules: the Mac master first, then the project mirror from the same bytes. Never write to the Language Rules yourself. If a Book Rule clashes with the Language Rules, it goes in the warnings section with his decision.
- After a piece publishes, run fold-article-lessons.

---

## Ending A: Inside The Introvert article

**Draft** Insight 1, Insight 2 and Insight 3. Insight 3 is a question about Insight 1, aimed at a reader who was in his shoes in that piece. No title, no subtitle, no category yet. Give him the three fields as plain text.

**Publish only when he says go.** Ask once for name, subtitle and category. Then stop asking. If he does not answer, pick a category from the list, leave the subtitle empty, publish, and say what you picked so he can change it in one click. Never invent a title. If he wants candidates he will ask.

Notion data source: `collection://d73333e2-807b-4aee-a4ce-0bb96ef282e7`

Fields: Name, Subtitle, Category, Status, Published At, Insight 1, Insight 2, Insight 3. The Content property and the page body stay empty. Everything lives in the three Insight fields. Each field opens with its header line ("Insights from me, to you.", "Insights from other experts.", "Insight from within you."), then a blank line between paragraphs. Insight 1 ends with `Coach Gen`.

Category options, exact spelling: Introvert's Leadership, Introvert's Mindset, Introvert's Public Speaking, Introvert's Strength, Introvert's Life Journey, Introvert's Energy Management, Focus, Productivity.

After publishing, compare the stored fields with the approved text by sha256 and say they match.

This schema is carried here because the doc that held it was deleted. This is now the only copy.

## Ending B: Lasting Change Letters edition

A sister series to Inside The Introvert. The raw material is a book he has read, and what he saw in it as a coach that the author was not writing about.

**This is not a book review.** The piece is his realisation. The book is the setup, and it gets only the words it takes to make his point land. No summary, no chapter walk, no verdict on whether the book is good. Name the author in the first mention, as in "Never Split The Difference, by Chris Voss." It was not clear in one draft who wrote the book. After that, the author gets only what the setup needs. Edition 1 passed with the author named twice in Insight 1. The book's own detail, dates, co-authors and named tools, lives in Insight 2.

The author wrote for their own reader. He is writing for his. The translation between those two worlds is the whole piece. Edition 1: Chris Voss negotiates with criminals who are negotiating with him, and Coach Gen negotiates with people who are negotiating with themselves.

**Check the book before quoting it.** Names, terms, years and claims about what a book says get verified, not recalled. If a term is the author's, use the author's actual word for it. If something cannot be confirmed, say so and ask rather than guessing with confidence. Do not attribute his own idea to the author, and do not let the author's thesis quietly replace his.

**Draft:**

- **Insight 1**, his realisation, in his voice, with the book present only as far as it takes to introduce the point. Aim at about 320 words so it lands in range after his notes.
- **Insight 2**, the book layer. The author, the title, and what the book actually says, in its own terms. This is where anything he left out of Insight 1 belongs. It must sound different from Insight 1, not a restatement of it.
- **Insight 3**, the reader's own question, opening a new angle.

No title, no subtitle, no category yet. The target range is the article range for now. He has said to try it and adjust once a few editions exist, so if a piece wants to run longer, say so and let him decide.

**Publish only when he says go.** Name is `Lasting Change Letters #N`, numbered in order. Subtitle is the book's title. Edition 1 set this pattern. Never invent any other title. If he does not name a category, pick the Law the edition serves, publish, and say what you picked.

Notion data source: `collection://409042c2-c5a3-4ebd-a21c-10621af68452`

Fields, identical to Inside The Introvert: Name, Subtitle, Category, Status, Published At, Insight 1, Insight 2, Insight 3, Day, Slug, Content. The Content property and the page body stay empty. Same header lines and spacing, and Insight 1 ends with `Coach Gen`.

Category options, exact spelling: Reset My Course, Reframe Past Regret, Resolve Present Friction, Reap Future Habits, Relax To Results, Focus, Productivity. Tag the edition with the Law it serves.

Edition 1 had a beat where he found he was already applying the book's ideas before reading it. That is one instance, not a rule. Do not build it into later editions unless he says so.

## Ending C: Book chapter

The goal is to finish the whole book from the material that already exists: the Coach Gen Brain, his articles and his own notes. A chapter goes from raw material to a Google Doc he can mark up in two stops. Stop 1: the chapter's key moments, each written three ways, for him to pick. Stop 2: the whole chapter, built around his picks. Do every step between the stops in one go. Do not stop to ask him to approve a fact sheet or an outline.

**The book map.** The row names where material used to live (worksheet, Obsidian, Testimony). Find the same material in the brain by Law, type and `legacy_ref`. Read every source in the chapter's row in full. A skim of one part is not a read.

| Order | Chapter | Main material |
|---|---|---|
| 1 | Chapter 1, the pattern (his own story) | Laws of Lasting Change Acts 1 to 3 (Notion), the worksheet Stories row notes for the three acts, My Dragon series |
| 2 | Law 1, Reset My Course | Worksheet Law 1 page and column, Obsidian Law 1, Testimony 3B and T-110 to T-119 (David), T-022, and the Law 1 article series (Book_Status.md) |
| 3 | Law 2, Reframe Past Regret | Worksheet Law 2, Obsidian Law 2, Testimony 3C and T-018, the accepted chimpanzee piece (Language Rules section 14) |
| 4 | Law 3, Resolve Present Friction | Worksheet Law 3 (his pruning story is its Stories cell), Obsidian Law 3, Laws 3-5 Map, Testimony 3D, T-014, T-017 |
| 5 | Law 4, Reap Future Habits | Worksheet Law 4, Obsidian Law 4, Laws 3-5 Map, Testimony 3E, T-019 to T-021 |
| 6 | Law 5, Relax To Results | Worksheet Law 5, Obsidian Law 5, Testimony 3F, T-025 |
| 7 | Introduction (epoch 3 and later) | Testimony INTRO and INTRO-LETTER entries, his published pieces. **Write it last**, once the chapters exist, so it promises only what they deliver |

A conclusion is not decided. Do not write one unless he asks. An article's Insight 2 and 3 are optional (Book Rules R29).

**Fact sheet** (`build/<chapter>/fact_sheet.md`):

- Every event, detail, number and quote the chapter could use, in time order, each tagged with its source (brain `legacy_ref` and entry id, article title).
- **Keeper lines**: his own words to print word for word. His worksheet sentences, his typed edits, and lines he praised in the calibration log ("this is good", "cool sentence").
- **No article sentences.** Facts and keepers only. An article sentence that is not a keeper is rewritten as a plain fact. This is what stops the old draft from leaking in.

**Outline** (`build/<chapter>/outline.md`), three things, not a beat-by-beat plan:

- The blank, "this chapter is about ____", and the one thought the reader leaves with.
- The thread word (step 4), and the 2 or 3 things the reader must keep (R32).
- The key moments: the 5 or 6 places that carry the chapter (its opening, its turns, its payoff, its hand-off), and where the headings go (R31).

**Law chapters, default shape**, as a menu, not a sequence to fill. Skip any slot that has no material:

1. Opening story: one case or his own scene, no heading.
2. The stuck point in the reader's own life (Stuck Symptoms, self-talk inline).
3. Myth and reality (Misconceptions, Common Misexecutions).
4. The idea, shown first and then named (Concept, Coined Term, Hidden Reward).
5. The method: his Core Exercise and Resources. **Never invented.**
6. What changes (DoD lines, Testimony WHAT-CHANGED and END-CARD lines).
7. Why this Law comes here and what it opens next (Why This Position, What Happens If Skipped, Sequence Trigger).
8. A From Within You exercise box, built from his self-directed questions and Core Exercise.
9. A Chapter Summary box, with lines lifted from the chapter.

If something needs material that does not exist, do not invent it. Mark it `[MATERIAL NEEDED: what, and where it would go]`.

**Stop 1: the key moments, three ways each.** In the conversation, write each key moment three ways. **Built differently, not reworded:** for example time order, his line first, the reader first, the payoff first, a callback to an earlier line, a mirror with matching beats. Label each version with how it is built. Every fact comes from the fact sheet, and every version follows the Book Rules. Run the step 9 script. Deliver a Google Doc, "5 Laws Manuscript, <Chapter> Key Moments", with one grey line at the top asking him to pick one version per moment, or mix them, and to comment on any line. Save the text to `build/<chapter>/key_moments_eN.md`, update `Book_Status.md`, and add one line to the calibration log. Reply with 1 or 2 lines and the link.

**Stop 2: the chapter.** Write the whole chapter in the conversation, from the fact sheet forward, with his picks in place and the joins between them written fresh. Never draft by editing an earlier chapter draft. Then step 9.

**Deliver the chapter.** (Annotated 3 Nov 2026: a chapter epoch now looks like the printed book. His words: "I want to see it, and this changes everything about the feeling of reading. Don't need a pdf, just gdocs modded in a way." His picks: an indent and no gap, page numbers off, chapter epochs only. Key moments docs and article drafts keep the old layout, with a visible gap after every paragraph.)

- Stage `Book/source/make_review_doc.py` and `Book/source/review_scorecard.html` from his Mac and run the script in the session. It reads the chapter source in the @LABEL, #, ##, @PULL, @FIGURE, @SUMMARY and @WITHIN blocks, the end note and the grey top line.
- Build in five steps:
  1. `make_review_doc.py html SRC.md ENDNOTE.txt TOPLINE.txt review_scorecard.html OUT.html ROLES.json`. Create the doc with Drive `create_file` (`contentMimeType: text/html`) in the Drafts folder, titled "5 Laws Manuscript, <Chapter> Epoch N". The HTML carries structure only.
  2. `read_doc`, then `stage1 DOC.json ROLES.json OUT.json`: the 6 by 9 page and its margins, a page break in place of each imported rule (before the end note and before the scorecard), two blank write lines under each From Within You question, merged span cells. Send it with `update_doc` and the revision guard.
  3. `read_doc` again, then `check DOC.json ROLES.json SRC.md`. It compares every paragraph and box with the source word for word and stops at the first mismatch. Then `stage2`: every paragraph, run, cell and column set to the book spec. Style changes shift no indexes, so a batch too long for one call can go in two, the second guarded by the revision the first returns.
  4. If stage1 warns that a figure came in flat, nest it in a borderless 1x1 table, as `Book/source/nest_fig.py` did for Figure 3.1 in epoch 5. One outer row that cannot break keeps the figure and its caption on one page.
  5. Export the doc as a PDF (Drive `download_file_content`, `application/pdf`) and render the pages with the google-workspace `render_export.py`. Look at the chapter opening, every figure and box, the end note and the scorecard. Put the opening page next to page 7 of `Book/5_Laws_of_Lasting_Change_Draft.pdf`. Fix a split figure or box, or a scorecard that spills onto a new page, before sending the link.
- The layout: Georgia 10.5 on a 6 by 9 page, justified, paragraphs set apart by a first-line indent with no gap. The label line italic and centred, the title in bold small caps, headings centred in small caps (never typed in capitals, so the merge reads the words as written), a grey drop letter on the first paragraph after the title or a heading, the R35 line centred in italic 12, the Chapter Summary in a filled box, From Within You in a ruled box with a write line under each question. Page numbers stay off. He adds them with Insert > Page numbers.
- The merge contract in `claude/Book_Writing_Handoff.md` section 5 still holds: the label line above the Heading 1 title, Heading 2 inside, the boxes as single-cell tables, the end note starting "From Claude,". Two things changed. The end note starts on a new page after a page break. The label is italic, so merge-epoch-to-book runs `merge_epoch.py` with `--label "Chapter N"` (tested on epoch 5: title, headings, pull line, summary and questions all came through).
- The printed draft PDF was built without Georgia installed, so it fell back to DejaVu Serif, which sets fewer words per line. The doc uses real Georgia, as `build.js` asks.
- After the grey end note, on its own page, add a blank copy of the scorecard so he can fill it in the doc or copy it out. make_review_doc.py fits it to the 6 by 9 page. The template is the Google Doc "5 Laws Manuscript, Chapter Scorecard (template)" (id 1-nwGGllMVxyNqmXlhO6iRCF-kYPYv8_AMh0nfFOBP3Q). It sits after the end note, so merge-epoch-to-book never reads it.
- The grey end note holds the `[MATERIAL NEEDED]` list and at most 3 questions, only about facts, realness or missing material. For every study or book cited, give the exact phrase and the full source for the Notes page.
- Save the exact delivered text to `build/<chapter>/epochN.json`. Update `Book_Status.md`: the epoch, the doc id, and the ideas, stories and quotes this chapter now owns. Add one line to the calibration log: drafted, awaiting his markup. Write the project mirror.
- Reply in chat with 1 or 2 lines and the link. Do not recap the chapter.

---

## Scorecard (added 29 Oct 2026)

His words (29 Oct 2026): "I like this scoring framework. integrate into the skill and as a questionnaire in the google docs I can fill or copy paste." The method is analytic scoring, as exam boards use it: separate traits, each scored against written levels, fixed by anchor pieces, and checked by two raters scoring apart. His comments stay the main signal. The scores say which trait a comment belongs to.

**The six traits, scored 1 to 10.**

| Trait | 10 looks like | 7 looks like | 4 looks like | His words behind it |
|---|---|---|---|---|
| 1. The one idea | One provocative thought the whole chapter delivers. A reader can say it back in one sentence. | The idea is there but shares the stage with others. | Several ideas, none of them the point. | "doesn't build a 10/10 idea" |
| 2. Build | Every section adds a layer to the one idea. Nothing restarts, nothing repeats. Each section ends on the question the next one answers. | Most sections build, one or two stand alone. | Sections read as separate essays. | "x is not even a function of y", "the chapter breaks down on chunks larger than paragraph" |
| 3. Paragraph craft | Any paragraph could be sent to a friend, and they would ask which bestseller it is from. | Most paragraphs pass, some are flat or choppy. | Paragraphs feel assembled. | "if I were to send one paragraph to a friend, they would ask which bestselling book are you reading" |
| 4. Voice | Sounds like him. Simple words, his rhythm, spoken material rewritten as book prose. | His voice with some stiff or borrowed lines. | Reads like a transcript or like generic self-help. | "putting quote in trains like how it happened in the call doesn't help the reader" |
| 5. Proof | Real stories, research and outside voices, placed the way Clear and Dweck place them. Nothing invented where the material exists. | Proof is real but clumsy, too much, or in the wrong place. | Claims stand bare, or the proof interrupts the story. | "find how clear and dweck references other people's work or research" |
| 6. Reader pull | The reader sees their own life, feels the stakes, and wants the next chapter. | Relatable in places, flat in others. | The reader watches from outside. | "how to make the audience relate" |

**Overall score.** The average of the six, but never more than the weakest trait plus 2. A chapter with great paragraphs and a broken build cannot score high.

**Anchors.** Chapter 3 (Law 1) epoch 2 is a 5.5 overall (his score, 29 Oct). Chapter 2 epoch 3 is an 8 (his score, 28 Oct). The Clear and Dweck passages he marked in `claude/Taste_Test_Passages.md` are the 10s. Add an anchor each time he scores a new epoch. Never remove one.

**Calibration.** Score every chapter epoch on all six traits before he reads it, with one line of reason per trait. Save the scores to `Book/build/<chapter>/scores_eN.md` on his Mac. Do not put them in the Google Doc, so they do not lead his score. When he sends his scores, log them word for word in the calibration log next to yours. Where the two differ by 2 or more on a trait, say which it was: the trait's description, or your reading of the draft. A change to a description goes through propose_skills, never silently.

**Reader check (alpha readers).** Three questions per chapter: Where did you stop or skim? Which line would you send to a friend? What was this chapter about, in one sentence? If their sentence matches the blank (step 3), trait 1 passed.

## What has actually gone wrong before

Each of these happened, was diagnosed, and some happened again. Recognise them.

- **A review pass done in the head.** Chapter 3 epoch 4 (30 Oct) checked the three newest rules carefully and skimmed the rest. It broke R4 (moved sentences from epoch 3), R5 (a sentence answering a question the reader never saw), R6 (false "so" and "then") and R32 (one pattern, four names). He was "half ready to drop the book". Hence the written review file in step 9.
- **The disclaimer paragraph.** A line explaining what the research or the source does not prove. Cut four times, reinserted four times. It was never judged by the reader, because it was classified as protection rather than content. Language Rules, section 8.
- **A second story arc.** One life told as two stories, or a cut arc replaced by a different one. When a beat is weak it wants stakes, not more story. Language Rules, sections 5 and 6.
- **The invented prescription.** A payoff that fits the story but is not his coaching. His words: "everything after this, mainly the diagnosis and prescription, is not what I actually would prescribe." Language Rules, section 8. The method comes from the worksheet.
- **The half-vague client story.** Strict no-invention left a case too vague to follow and too specific to hide the person, in choppy fragments of what she said in session. Book Rules R3b.
- **A wall of context.** "my words are verbatim and records of coaching is nice. but they are in a wall of context." Give the reader the facts before a client's line.
- **The author's past in the present tense.** A line showing him at his worst, read as who he is now. Book Rules R21.
- **One area of life only.** A diet case that left readers building other habits outside the piece. Book Rules R16.
- **Meta-narration.** Lines that explain the shape of the piece instead of delivering it. Language Rules, section 5.
- **Research dropped into his story.** "the way you put things is very jarring." Book Rules R28.
- **A transcript used as a quarry.** "where the fuck did healthy come from?" Facts come from approved material only.
- **Patching an earlier draft.** "yes now it's parallel and long, but it's just making it robotic and repeated." And on a chapter's epoch 2: "the content is still held back by previous draft it feels." Hence writing from the material or fact sheet forward.
- **Too many ideas, or ideas from other chapters.** "x is not even a function of y, and is just random." Hence the ownership ledger.
- **A forced parallel or mirror.** "the parallel is still not that connected or is forced in a context that can't use that structure."
- **A made-up image.** "what is this vague metaphor no one ever uses?"
- **A heavy pipeline.** "This new workflow is too token and time inefficient, and doesn't seem to accomplish the objective of generating creativity and new lines or constructions." Hence the lean method, the key moments, and writing in the conversation.
- **Trusting the numbers.** They catch gross failure and nothing else. Language Rules, section 1.
- **Working material in the project.** Drafts, logs, measurements, fact sheets and outlines stay local or in `Book/build/` on his Mac. See `Guardrails.md`.
- **Letters only: summary creep**, where the book slowly takes over Insight 1, and **the author's thesis**, where the piece ends up arguing the book's point rather than his.

## Brain use log

When a piece goes into a chapter, talk, article or letter, add a row to `brain.used_in` (entry, work, location, persona if any). A minor entry can be used once per work. Check `brain.used_in` before choosing material so nothing is repeated. See `claude/Brain_Rule.md` section 5.