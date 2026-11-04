---
name: "merge-epoch-to-book"
description: "Write the latest approved epoch of a chapter of Coach Gen's book 5 Laws of Lasting Change into the master book draft (docx and PDF on his Mac). Use when he says a chapter is ready to merge, or for /merge-epoch-to-book."
---

# Merge a chapter's last epoch into the master book draft

When he says a chapter is ready ("ready to merge with the real book"), its latest epoch Google Doc, with his final edits, goes into the master draft. The text comes out of the doc by script. It is never re-typed.

**Argument.** A chapter name ("Chapter 1", "Law 3"). With none, use the chapter whose latest epoch he just approved.

## Where everything lives

His Mac, `Book/` inside "5 Laws of Lasting Change" (`$HOME/mnt/5 Laws of Lasting Change/Book` in device_bash):

- `5_Laws_of_Lasting_Change_Draft.docx` and `.pdf`: the master draft.
- `source/build.js`: renders the book. Its `BOOK` list sets the order and the Contents. A part with no chapter file shows in Contents with no page number.
- `source/content.js`: the Introduction (an old version, rewritten last) and the archived old Chapter 1.
- `source/chapters/<key>.js`: one file per merged chapter. Keys: `chapter-1`, `law-1` to `law-5`, `closing`.
- `source/merge_epoch.py`: turns the Google Doc JSON into a chapter file. `source/make_book.py`: two-pass build with Contents page numbers, and it copies the previous draft to `build/archive/<date-time>/`.
- `Book_Status.md`: the latest epoch doc id per chapter, and the table "The master book draft".
- `build/<chapter>/`: the merge inputs (fixes and notes JSON).

**Writing to the Mac.** Stage under a new file name, commit to `Book/build/incoming/`, check the md5 on the Mac, then `mv` into place. `device_commit_files` can write a stale cached copy when a staged path was used before.

## Steps

1. **Find the doc.** Take the chapter's latest epoch Google Doc id from `Book_Status.md`.
2. **Log his final pass.** Read the doc with Drive `read_file_content` and `includeComments: true`. Copy his score, comments and typed edits word for word into `claude/Coach_Gen_Book_Calibration_Log.md` (add only). Comments about layout (a special line, box style, bullets) are handled in this merge. Comments that ask for new writing are not: list them in the reply for the next epoch.
3. **Get the doc as JSON.** Call Docs `read_doc` on the doc id. The result is saved to a file. Never paste it.
4. **Decide three things, then run the script.**
   - **Special lines** (`--pull`): the few lines he wants set apart, centred and italic. His words: "this is a very special line that deserves a new line or its own paragraph or box. only some select lines will have this." A chapter's locked line is one. Pass the exact text.
   - **Grammar fixes** (`--fixes`, a JSON list of `[old, new]`): only clear errors in his last edits (comma splices, fragments, tense slips), fixed in his words, plus ALL-CAPS emphasis set as `*italic*`. Each must match exactly once. Save as `build/<chapter>/merge_epochN_fixes.json`.
   - **Notes** (`--notes`, a JSON list of strings): the full citation for every study the chapter still names, for the Notes section. Book Rules R28 keeps years and journals out of the text. Save as `build/<chapter>/merge_epochN_notes.json`.

   Stage `source/merge_epoch.py` from the Mac and run it in the session:
   `python3 merge_epoch.py <saved read_doc file> --key <key> --epoch N --out <key>.js --pull "..." --fixes fixes.json --notes notes.json`

   It reads from the doc's Heading 1 (the title) to Claude's grey note. Heading 2 becomes a section heading. The first paragraph after the title or a heading gets the opening style. A soft line break starts a new paragraph. Italics become `*text*`. The Chapter Summary table becomes the shaded summary, and any other table becomes a bordered exercise box with numbered questions and write-in lines (his words: "bullet these. also make from within you differently boxed than summary"). Read its report: block count, headings, special lines, boxes, and warnings (dashes, semicolons, ALL-CAPS words, odd quote marks). Fix and rerun until there are no warnings.
5. **Put it in place.** Commit `<key>.js` and the two JSON files to the Mac and check the md5. Copy any existing chapter file to `build/archive/`, then move the new one into `source/chapters/`. If the chapter is new to the book, check its row in `BOOK` in build.js (key, number, Contents title).
6. **Build.** On the Mac, from `Book/`: `python3 source/make_book.py .` It prints the page each part starts on and where the previous draft was archived.
7. **Check the pages.** Stage the PDF, render the chapter's pages with pdftoppm at low resolution into one contact sheet, and look at it: headings, special lines, boxes whole on one page, Contents numbers, Notes. A box split across pages, or a heading alone at the bottom of a page, is fixed in build.js, never by editing the text.
8. **Record.** In `Book_Status.md`, update the chapter row (merged, epoch, date) and add a row to "The master book draft". Add one line to the calibration log and write its project mirror.
9. **Deliver.** Send the PDF with SendUserFile so he can see the layout. Reply in 1 or 2 lines: what went in, the grammar fixes in one line, and any writing comments left for the next epoch.

## Rules

- The doc is the source. Never re-type the chapter, and never edit the merged text by hand. A change after the merge comes from a new epoch doc, merged again.
- Merge only what he has approved as ready, and log his score and words before the merge.
- Never delete. The previous draft and replaced source files go to `build/archive/`.
- No em dashes and no semicolons. The script warns about both.