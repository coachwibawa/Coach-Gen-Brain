# Universal Book Parser: Plan

Written 31 Oct 2026. Status: plan, not built yet.

## 1. Why

Loading a book into the brain is now cheap. The GitHub route takes one SQL call and about 15,000 tokens.

Cleaning is the expensive part. Mindset and Atomic Habits each got their own hand-made parser (`/home/claude/mindset/parse.py`, `/home/claude/ah/parse.py`). Claude read many pages of layout text, fixed a rule, ran it again, and repeated. For Atomic Habits that cost an estimated 100,000 to 200,000 tokens.

Goal: one parser for every book. A new book needs only a short settings file. Claude reads only the pages the checks flag.

Target per book: cleaning under 30,000 tokens, the whole mine under 50,000 tokens and under 30 minutes, plus the embedding wait.

## 2. What the probe found (31 Oct 2026)

The two old parsers guess structure from spaces in `pdftotext -layout` output: how far a line is indented, whether it is in capitals, whether it is centered. That breaks on every new layout.

The PDFs also store the font and size of every letter. I checked three books:

| Book | Body text | Section heading | Other styles |
|---|---|---|---|
| Atomic Habits | Georgia 14.4 | Arial Bold 14.4 | Figure labels in Arial 10.8, part pages in Arial 23.8 and 28.8 |
| Mindset | Liberation Serif 14.4 | Liberation Serif Bold Italic 14.4 | Italic for emphasis inside paragraphs |
| The War of Art | Times 11.5 | Times 14.0 | Drop cap in Times 14.0, a line of underscores under each heading |

Each book marks headings differently, but always with a style that differs from the body. The left edge of each line is also exact (for example 90 for a new paragraph and 72 for a running line in Atomic Habits). That beats counting spaces.

## 3. How it works

The tool is `tools/parse_book.py`. It reads the PDF with pdfplumber, which is already installed.

**Stage 1, profile (no settings needed).** It prints a short report:
- Page map: a guess for each page range (front matter, contents, body, notes, index, ads), based on simple signals. Index pages are lines ending in page numbers. Notes pages are lines starting with numbers.
- Style table: every font and size used in the body pages, how many lines use it, and 3 sample lines for each.
- The contents page text, so chapter titles can be copied.

Claude reads this report (about 2,000 tokens) and writes the settings file. This replaces reading pages one by one.

**Stage 2, parse (with settings).**
1. Remove running headers, footers and page numbers: lines that repeat across many pages at the same height.
2. Give each line a role from the style table: body, heading, chapter title, part title, figure, drop cap, or skip.
3. Join lines into paragraphs. A new paragraph starts when the first line is indented, when the gap above it is bigger than normal, or when the role changes.
4. Fix the known joins: hyphen at line end, a dash between lines, a drop cap joined to its word (T HE becomes THE).
5. List items (starting with a number, a bullet or a dash) start a new paragraph each.
6. Label every paragraph with its chapter and section.
7. Write `turns.json`, the same shape `tools/build_load.py` reads today: `{"s": PDF page, "t": text, "ch": chapter, "sec": section}`. One small addition: `"k"` for the kind of turn (body, heading, figure, list, quote). It does no harm and lets a later search skip headings and figure scraps.

## 4. The settings file

One small JSON file per book in `books/<name>.json`. It holds no book text, so it is safe to keep in the repo.

```json
{
  "title": "The Courage to Be Disliked",
  "keep_pages": "12-280",
  "skip_pages": ["150"],
  "styles": {
    "Georgia 14.4": "body",
    "Arial-Bold 14.4": "heading",
    "Arial 23.8": "part",
    "Arial 10.8": "figure"
  },
  "chapter_start": "a page whose first line is a number alone",
  "chapter_titles_from_page": 6,
  "speakers": {"PHILOSOPHER:": "Philosopher", "YOUTH:": "Youth"},
  "drop_lines": ["^_{5,}$"]
}
```

Every key is optional except `keep_pages` and `styles`. When a new book needs a new trick, it becomes a new optional key in the shared parser. Book-specific code never goes back into the parser.

## 5. Checks, and the only pages Claude reads

Every run prints these checks:
- **No text lost, per page.** The page text and the turns from that page match with all spaces removed. A failed page is listed by number.
- **Headings.** The full list of headings, numbered. Flags: longer than 12 words, ends with a full stop, or starts in lowercase.
- **Paragraphs.** Flags: longer than 400 words (likely two paragraphs joined), starts in lowercase (likely a broken join), shorter than 4 words in the middle of body text.
- **Speakers** (dialogue books only). Every turn has a speaker. Turns without one are listed.
- **Pages to look at.** One list of page numbers from all the flags above.

Claude reads only the pages on that list, changes the settings, and runs again. When the list is empty or every flag is explained, the text is ready for `build_load.py`.

## 6. Dialogue books

The Courage to Be Disliked is written as a talk between the Philosopher and the Youth. With the `speakers` setting, each turn gets its real speaker in `"sp"`. A chunk then reads "Philosopher: ..." and "Youth: ...". This is the same shape the brain uses for calls, so search and citations work the same way. `build_load.py` already keeps a per-turn `sp` when it differs from the book's main speaker.

## 7. Tests on the three books already loaded

Before the parser is trusted, it runs on Mindset, Atomic Habits and The War of Art.

- For Mindset and Atomic Habits, the hand parsers' output is the answer key. Pass: headings are the same, or each difference is listed and is better. At least 98% of paragraph breaks are the same. No text lost.
- The War of Art has no local answer key, so it passes on the checks in section 5 alone.
- The answer keys go into `tests/expected/<name>.json` as counts and one md5 per paragraph, never the text itself. A later chat can re-run a test when Gen attaches the PDF again.

The brain is not touched. Mindset and Atomic Habits stay as loaded. These are tests only.

## 8. Where it lives

Repo `coachwibawa/Coach-Gen-Brain`:
- `tools/parse_book.py`: the parser
- `books/mindset.json`, `books/atomic_habits.json`, `books/war_of_art.json`: settings for the test books
- `tests/expected/`: answer keys, hashes only
- `SCHEMA.md`: a short section on how to use it

## 9. The new flow for a book (replaces /mine step 5b.1)

1. Gen attaches the PDF and says /mine.
2. `python3 tools/parse_book.py book.pdf --profile`. Claude reads the report.
3. Claude writes `books/<name>.json`.
4. `python3 tools/parse_book.py book.pdf books/<name>.json turns.json`. Claude reads the checks and only the flagged pages, and adjusts the settings if needed.
5. Then the GitHub route as today: `build_load.py`, push, `load_from_github`, compare md5, remove the load file, check embeddings.
6. Write `passes` and `left_out` in the load file the first time, so no UPDATE (and no approval prompt) is needed after.

The /mine skill gets this as an added step. Nothing in it is removed.

## 10. Build steps

0. Fix the small search label bug: book chunks show a time like "@00:03:13" where the page should be. Book chunks should show "p39". `search_voices` already shows the page correctly.
1. Write the profile stage. Run it on all three books and check the style tables by eye.
2. Write the parse stage and the checks.
3. Write the three settings files and the answer keys.
4. Run the tests until all three pass.
5. Commit, update `SCHEMA.md`, and propose the added step for the /mine skill.
6. First real use: The Courage to Be Disliked.

Model for the build: Sonnet, medium effort. It follows this plan, and every step has a check. If it fails twice on the same step, move to Opus.

Estimated build cost: one session, about 60,000 to 100,000 tokens. It pays for itself on the first new book.

## 11. Not in this version

- Scanned PDFs with no text inside. The profile stage spots them and stops. Those would need OCR.
- EPUB files. They are easier, because the chapters and headings are already marked inside the file. A separate reader can be added later, and it would write the same `turns.json`.
- Notes and index text. They stay cut, as with Mindset and Atomic Habits.
- Transcripts, such as the Huberman episode. They already have their own route.

## 12. Built (31 Oct 2026, added after the plan)

Built by Sonnet in one session. In the repo `coachwibawa/Coach-Gen-Brain`: `tools/parse_book.py`, `books/` (settings and README), `tests/` (compare and regression keys), `SCHEMA.md` section, migration 016.

Results:
- Atomic Habits: 1,278 turns, 61,666 words. Mindset: 1,675 turns, 91,143 words. The War of Art: 640 turns, 23,888 words. All three lose no text.
- Against the old hand parsers, the text is the same except credit lines, section-break dashes and periods the hand parser added. Atomic Habits has 1,278 turns where the hand parser had 1,444, because the hand parser cut every paragraph at a page break and the new one joins them. 56 joins happen at page breaks. The rest are figure text grouped into one turn and chapter titles joined into one heading line.
- The new parser splits 58 paragraphs the hand parser kept whole (for example the "Problem #1:" run-in heads in Atomic Habits chapter 1), because the book indents the first line of each.
- Profile run: about 35 seconds and about 3,000 tokens to read. The parse run takes about 35 seconds.
- Book chunks in `brain.search_all` now show the page ("p39") instead of a time.

Not yet done: the first real book (The Courage to Be Disliked) will show what settings keys are still missing. Dialogue speakers (`speakers`) are built but untested on a real dialogue book. The `/mine` skill step is proposed, not saved.

## 13. First real use and loop closed (1 Nov 2026, added)

- The Courage to Be Disliked went in on 31 Oct 2026 with the parser on Sonnet: 1,573 turns, 727 Youth and 727 Philosopher turns, no text lost, no flags, 15 documents, 237 chunks. One parser change was needed: a speaker label starts a new paragraph.
- Cost came in well under the Atomic Habits cleaning. I read only the profile report and a few spot pages.
- Regression keys now cover four books. All pass.
- Loop closed on 1 Nov 2026: the load records its own pass (no approval prompt), push and drop scripts, one passage per book in the outside search, and Run 8 of the test set. Details in `claude/Brain_Rule.md` section 10.
