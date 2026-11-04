---
name: "book-draft-to-booklet"
description: "Turn the latest master draft of Coach Gen's book 5 Laws of Lasting Change into an A4 print booklet to fold and staple, and tell him how to print it. Use when he asks to print the draft or make a booklet."
---

# Turn the latest book draft into a print booklet

His ask (7 Oct 2026): "how do I print this book draft? so that you know it flaps. also you need to plan the empty pages I assume". Then: "turn this into a skill. turning the latest book draft into a booklet."

The result is `Book/5_Laws_of_Lasting_Change_Print_Booklet_A4.pdf` on his Mac: two book pages per A4 sheet, in booklet order. He prints it on both sides, folds the stack in half, and staples it on the fold. It reads like a real book.

## Where everything lives

His Mac folder `/Users/coachwibawa/Documents/5 Laws of Lasting Change/Book/` (device bridge: `$HOME/mnt/5 Laws of Lasting Change/Book/` in device_bash). Work there with device_bash. Never re-type a file.

- `5_Laws_of_Lasting_Change_Draft.pdf`: the master draft (6 x 9 in pages), built by `source/make_book.py`.
- `source/make_booklet.py`: imposes the draft into the booklet. `python3 source/make_booklet.py .` from the Book folder. Options: `--in DRAFT.pdf`, `--out BOOKLET.pdf`. It copies the previous print file to `build/archive/<date-time>/` first.
- `source/make_book.py`: the full rebuild (docx, PDF, Contents and Notes page numbers). It calls `booklet()` from make_booklet.py at the end, so every rebuild and every chapter merge also writes a fresh booklet.
- `source/build.js`: the book page order (below).
- `Book_Status.md`: the master draft section records how the print file works.

## Book page order (already built into build.js, check it, don't redo it)

Cover page 1, empty page 2, title page 3, copyright page 4, Contents page 5, empty page 6, Introduction on page 7 (numbered 1). The title page, Contents, Introduction, every chapter and the Notes start on a right-hand (odd) page. When a part would start on a left page, an empty left page with no page number goes before it. This comes from `SectionType.ODD_PAGE` in build.js, plus LibreOffice's PDF filter option `IsSkipEmptyPages: false` in make_book.py (without it, LibreOffice drops the empty pages from the PDF). make_book.py also checks the Introduction lands on an odd page and flips `CONTENTS_PAD` if not.

## Steps

1. **Is the draft current?** Compare the newest `source/chapters/*.js` and `source/build.js` against the draft PDF's modification time. If a chapter or the build is newer, or he says the draft changed, rebuild: `python3 source/make_book.py .` (about a minute, it writes the booklet too). Otherwise run only `python3 source/make_booklet.py .`. Never merge an epoch here: merging is the merge-epoch-to-book skill, on his word.
2. **Check the page order** in the draft PDF with a pdftotext loop over every page (first words and the last line, which holds the page number). The Introduction must be on an odd page, every chapter opening and the Notes on odd pages, empty pages with no number. If any part starts on an even page, stop and fix build.js or the filter option before printing.
3. **Check the booklet.** `pdfinfo`: A4 landscape (841.89 x 595.28 pt), sheets = book pages rounded up to a multiple of 4, divided by 2 for the page count. Stage the booklet to the cloud workspace, render it with `pdftoppm -r 40 -png`, tile the sides into one contact sheet, and look at it. Sheet 1 front: empty left half, cover on the right. Sheet 1 back: the inside of the cover on the left. The middle sheet of each booklet holds two pages in reading order. Every pair on a sheet must add up to (booklet size + 1) within its booklet.
4. **Deliver.** SendUserFile the booklet (it is already in his Book folder, so no commit). Reply with the printing steps below and one line on what the print holds (which chapters are merged). Nothing else.
5. If the print order or the page order changed, add a dated line to the master draft section of `Book_Status.md` (add only).

## How the imposition works (make_booklet.py)

- Pad the book to a multiple of 4 with empty pages at the end. The last page is the back cover.
- Up to 48 book pages: one booklet. Longer: booklets of 32 pages (8 sheets), the last one smaller. He folds each booklet and stacks them in order.
- Within a booklet of size S starting at page index b, sheet k (from 0): front = left `b+S-1-2k`, right `b+2k`. Back = left `b+2k+1`, right `b+S-2-2k`.
- Each 6 x 9 page is scaled to fit half an A4 sheet (about 92%), touching the fold, centred top to bottom.

## Printing steps to give him (his Mac, Preview)

1. Open `5_Laws_of_Lasting_Change_Print_Booklet_A4.pdf` in Preview, then File, Print.
2. Paper A4, scale 100%. Two-Sided on, **Short-Edge binding**.
3. Keep the sheets in order, fold the stack in half, staple twice on the fold. With more than one booklet, fold each and stack them in order.
4. No two-sided printer: print the odd pages, put the stack back in, print the even pages. Test with one sheet first to see which way to feed it.

The pages print at about 92% of the real 6 x 9 in size.

## Rules

- His Mac is the master. Work there with device_bash. Stage only to look at the PDF. If a file has to go back to the Mac, stage it under a new name, commit to `Book/build/incoming/`, check the md5 on the Mac, then `mv` it into place (device_commit_files once wrote a stale cached copy over a master).
- Archive before overwriting. Nothing is deleted.
- No em dashes, no semicolons in anything written to his files or to him. Keep the reply short: the file, the steps, done.