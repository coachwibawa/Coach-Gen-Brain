---
name: coach-gen-writer
description: "Write, mark up, redraft, or publish Coach Gen's pieces in his voice: Inside The Introvert articles, Lasting Change Letters editions and chapters of his book 5 Laws of Lasting Change."
---

# Coach Gen Writer

One writer for everything in his voice, all to book standard (his call, 19 Oct 2026). Three endings: an **article** (Inside The Introvert), a **letter** (Lasting Change Letters), or a **chapter** of 5 Laws of Lasting Change, with its key moments and case studies.

**Argument.** Article: the raw material itself, not a topic. Letter: the book plus his realisation (never pick a book for him). Chapter: a chapter name, `next` (the first chapter in the book map with no draft yet, also what no name means), `all` (stop 1 for every undrafted chapter), `picked <chapter>` or `marked <chapter>`. Waiting picks or markup go first. No argument: ask what he wants to write, and wait.

**The rules are not in this skill.** They live in the brain's rules table and reach you as a card. Never restate them here or in chat. A second copy drifts.

## 1. One chat per piece

- A new chat per piece, kept through draft, markup, and redraft. Start fresh once it is approved or published, or when the chat gets summarised. Run /handoff before leaving.
- Write in the conversation. Helpers are only for the checkers and blind A/B tests.

## 2. Where things live

- **The brain:** Supabase "Coach Gen Brain" (ref from `list_projects`), schema `brain`: all his material and the rules. Read `claude/Brain_Rule.md` first. The worksheet, Obsidian, and Testimony files are frozen history.
- **His Mac:** `/Users/coachwibawa/Documents/5 Laws of Lasting Change/` (`$HOME/mnt/5 Laws of Lasting Change/` in device_bash): `Book/Book_Status.md` (book map and ownership ledger), `Book/Research/`, `Book/build/<piece>/` (working files, never in the project), `Book/source/` (the doc build). Mac not reachable: say so in one line and use the project copies.
- **Writing to the Mac:** `device_commit_files` can write a stale cached copy. Stage under a new file name, commit to a new path, check the md5, then `mv` it over. Small edits: a short python script in device_bash.
- **The repo** `coachwibawa/Coach-Gen-Brain` (add_repo, read access): clone it for `tools/cg_lint.py` and `tools/cg_check.py`.

## 3. Load first, once per chat

- **The card:** `select brain.card_text('chapter')` with `execute_sql` (or `article`, `letter`, `key moments`, `case study`). A chapter also loads `case study`, and `key moments` at stop 1. Brain down: `claude/cards/`.
- **The research,** the most important context for book standard: `claude/Findings_Books.md`, `claude/Findings_Guides.md`, `claude/Taste_Test_Passages.md`. Open a Full Read Notes file only when a finding cites it ("AH 449" is line 449 of `Book/Research/reference_texts/atomic_habits.txt`).
- **The state:** `Book_Status.md`, the piece's build files, its entries in `claude/Coach_Gen_Book_Calibration_Log.md`, the handoff note, and the published articles on the same Law. Where an article series and a chapter disagree, the newer context wins.

## 4. Before drafting

- **The blank:** "this piece is about ____", given to him in one line. In a letter it is his realisation, not the book's subject.
- **The leading word:** the one term the piece hangs on, from his material where you can (as "Momentum Engine" carries Law 4). Joins and the close are built around it.
- **The reader's starting point:** the ideas the reader already brings. Every paragraph leans only on those, or on what the piece has given them.
- **The moves:** list the Tier 2 moves on the card that fit this piece, not only the numbers.
- **Science or a mechanism:** lay the reasoning out in steps, one leap each, and talk it through with him before drafting.

## 5. Take the material

- Query `brain.entries_full` for the Law and the types you need (SQL in `Brain_Rule.md` section 3). Read all of it, and any source you choose from in full. Sort before use: some material sits under the wrong Law. Gold only. A raw chunk is never printed as a quote.
- Check `brain.used_in` first, so nothing repeats across works. A minor entry is used once per work.
- An idea, story, or quote another chapter or series owns (the ledger) gets one callback line at most.

## 6. Draft whole

- Write from the material forward. A redraft starts from the material and the blank, never from patching the last draft.
- After 3 rewrites of one passage, or when drafts start to look alike, use different material.
- A line that survived into an accepted draft is not proven good.

## 7. Check, then score

- **Lint every pass:** `python3 tools/cg_lint.py DRAFT --output chapter` (or `article`, `letter`, `key-moments`, `case-study`), with `--keep "phrase"` for each phrase he typed. Fix every FAIL and FORM. A clean lint is not a pass.
- **The review file, every pass:** `Book/build/<piece>/review_eN.md` lists every paragraph join (the reader's question, and the words that answer it), every carried thing with its one name, and every "so", "then", "because" and time word against what happened. Fix a fail by rewriting from the material, never with a bolted-on connector.
- **The checkers, once, on the final draft:** `cg_check.py prepare DRAFT --output chapter --dir RUN` (`chapter-excerpt` for a cut passage). With an API key, `cg_check.py run RUN`. Without one, one Sonnet helper per `RUN/R1.x.prompt.md` saves `RUN/R1.x.json`, then `cg_check.py collect RUN`. In a chat that costs about 1.5 million tokens, so never every pass. After a fix, rerun the checkers that failed.
- Check every fact against the material yourself.
- **Score a chapter** on the six traits before delivery, one line of reason each, in `Book/build/<chapter>/scores_eN.md`, never in the doc.

## 8. Deliver

- A new Google Doc per epoch, for him to mark up inline. Articles, letters, and key moments keep a visible gap after every paragraph. A chapter is set like the printed book (Ending C).
- An article or a letter keeps its built details and open questions in a grey note under the draft in the doc, never in Notion.
- No preamble, no defence of choices he has not questioned. Reply with 1 or 2 lines and the link.

## 9. His markup

- Read the doc with `read_file_content` and `includeComments: true`, and diff it against what you delivered.
- His rewrite stays word for word. A fix to his text is a proposal.
- Codes in his comments, read here: `[text]` is a suggestion (about half of that sentence or flow may be rewritten). `/privileged`: keep the fact, make it acceptable, say where it was a privilege. `/rhyme-this`: run the rhyme-this skill on that text.
- Lines he did not comment on are not approved. Anything weird in a draft is Claude's: own the fix, never ask him to explain it.
- Log his score, picks, comments, and inline edits (from the diff) in the calibration log word for word, with the words each sits on. Add only.
- Apply each note, then re-read the whole beat. Resolve a comment only when 100% sure it is fixed.
- "Regurgitate" means the full piece, every field with its header line.
- When he sends his scorecard, log it beside yours. Show yours only then.

## 10. Feed back

- His typed lines become keeper lines, word for word, not rules.
- A rule he asks for, or that his stated reason points to, goes through propose-language-rule into the rules table. An unexplained edit is an observation only.
- Every epoch: update `Book_Status.md` (epoch, doc id, what the piece now owns, never removing silently) and add one line to the calibration log (drafted, awaiting his markup).
- Log a use in `brain.used_in` once per work, the first time the piece uses it. When checking before you choose, this work's own rows do not count.

## Ending A: article

- Draft the three Insights as the article card says.
- **Publish only on his go.** Notion `collection://d73333e2-807b-4aee-a4ce-0bb96ef282e7`. Fields: Name, Subtitle, Category, Status, Published At, Insight 1, Insight 2, Insight 3. Content and the page body stay empty. Each field opens with its header line, a blank line between paragraphs, and Insight 1 ends with `Coach Gen`.
- Categories, spelled exactly: Introvert's Leadership, Introvert's Mindset, Introvert's Public Speaking, Introvert's Strength, Introvert's Life Journey, Introvert's Energy Management, Focus, Productivity.
- After publishing, compare the stored fields with the approved text by sha256. This schema lives only here.

## Ending B: letter

- Draft as the letter card says.
- **Publish only on his go.** Notion `collection://409042c2-c5a3-4ebd-a21c-10621af68452`. The article's fields plus Day, Slug, and Content, laid out the same way. Category: the Law it serves unless he names one, from Reset My Course, Reframe Past Regret, Resolve Present Friction, Reap Future Habits, Relax To Results, Focus, Productivity.

## Ending C: chapter

Two stops. Everything between them runs in one go, with no approvals of a fact sheet or an outline.

- **Book map:** Chapter 1 (his own story, the Acts 1 to 3 pieces, My Dragon), then Law 1 (David, legacy T-110 to T-119, T-022), Law 2 (T-018, the chimpanzee piece), Law 3 (his pruning story, T-014, T-017), Law 4 (T-019 to T-021), Law 5 (T-025). The Introduction last (law 0 entries and his published pieces). Find material by Law, type, and `legacy_ref`. No conclusion unless he asks.
- **Fact sheet** (`build/<chapter>/fact_sheet.md`): every usable event, detail, number, and quote in time order, each with its source. Keeper lines word for word, including lines he praised in the calibration log. No article sentences: one that is not a keeper becomes a plain fact.
- **Outline:** the blank and the one thought, the thread word, the two or three things the reader keeps, the five or six key moments, and where headings go.
- **Stop 1:** each key moment three ways (key moments card), linted, in "5 Laws Manuscript, <Chapter> Key Moments". Text saved to `build/<chapter>/key_moments_eN.md`.
- **Stop 2:** the whole chapter fresh around his picks, never edited from an earlier draft. Then section 7.
- **Build the doc:** put `src.md` (blocks marked `@LABEL`, which is required, `#`, `##`, `@PULL`, `@FIGURE`, `@SUMMARY`, `@WITHIN`), `endnote.txt`, `topline.txt` (the grey line at the top on how to mark it up), and `epoch.txt` in a work folder, stage `Book/source/epoch_build.py`, `make_review_doc.py`, and `review_scorecard.html` beside each other, and run `python3 epoch_build.py WORK`. Each run does the next step and prints the one connector call to make, then how to run it again: create, stage 1, the word-for-word check, stage 2, the PDF, and the pages to look at. Fix any split figure or box before sending the link. Copy `WORK/epochN.json` to `build/<chapter>/`.
- The merge contract is in `claude/Book_Writing_Handoff.md` section 5 (merge-epoch-to-book runs with `--label "Chapter N"`). Page numbers stay off.

## Scorecard (chapters)

Six traits, 1 to 10, each with what a 10, a 7, and a 4 look like:

1. **The one idea:** 10, one thought the chapter delivers, sayable back in one sentence. 7, it shares the stage. 4, several ideas, none the point.
2. **Build:** 10, every section adds a layer, nothing restarts or repeats, and each ends on the question the next answers. 7, one or two sections stand alone. 4, separate essays.
3. **Paragraph craft:** 10, a friend sent any paragraph would ask which bestseller it is from. 7, some are flat or choppy. 4, paragraphs feel assembled.
4. **Voice:** 10, him: simple words, his rhythm, spoken material rewritten as book prose. 7, some stiff or borrowed lines. 4, a transcript or generic self-help.
5. **Proof:** 10, real stories, research, and outside voices, placed the way Clear and Dweck place them. 7, real but clumsy or misplaced. 4, bare claims, or proof that interrupts.
6. **Reader pull:** 10, the reader sees their own life, feels the stakes, and wants the next chapter. 7, relatable in places. 4, the reader watches from outside.

Overall: the average, capped at the weakest trait plus 2. Anchors: Chapter 3 epoch 2 is 5.5, Chapter 2 epoch 3 is 8, the Clear and Dweck passages he marked are 10s. Add an anchor at each epoch he scores, never remove one. Where his score and yours differ by 2 or more, say whether the description or your reading was off. A change to a description goes to him as a skill proposal (propose_skills), never silently. Alpha readers: where did you stop or skim, which line would you send a friend, and what was this chapter about in one sentence (it should match the blank)?
