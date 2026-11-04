# Experimental Book Branch: Handoff (21 Oct 2026)

## Start here
Build a second, separate copy of the book: the real master draft (Introduction and Chapter 1, both merged) with the experimental Chapters 2 to 7 from the overnight run added after them. It is a different, less serious branch. The real master draft stays untouched.

## His words (21 Oct)
"create the book with the experimental material on top of what already exist ... no need to put it in the page, just the title and clear that this is a different less serious branch"

So: no red banners, headers, footers or watermarks inside the pages. Only the title (and file name) says it is the experimental branch.

## Where things live
- Mac, connected folder: `/Users/coachwibawa/Documents/5 Laws of Lasting Change/Book/`. In device_bash the same folder is under the session's `mnt/5 Laws of Lasting Change/` (run `find / -maxdepth 4 -name "5 Laws*"` to locate it).
- Master draft (do not overwrite): `Book/5_Laws_of_Lasting_Change_Draft.docx` and `.pdf`, plus `5_Laws_of_Lasting_Change_Print_Booklet_A4.pdf`.
- Build system: `Book/source/make_book.py` from `source/build.js`. Chapters in `source/chapters/` (`introduction.js`, `chapter-1.js`), order from `BOOK` in build.js. `source/merge_epoch.py` writes a chapter file from an epoch Google Doc. Full description: the "The master book draft" section of `Book/Book_Status.md`.
- Experimental chapter text, one folder each, in `Book/build/`: `chapter-2`, `law-1` (Chapter 3 is `epoch2_chapter.md` and `epoch2.json`), `law-2` (Ch 4), `law-3` (Ch 5), `law-4` (Ch 6), `law-5` (Ch 7). Each has `chapter.md` (markers: `@LABEL`, `#`, `##`, `@PULL`, `@SUMMARY`, `@WITHIN`) and `endnote.txt`.
- The same chapters as Google Docs: ids in project doc `claude/Overnight_Book_Run_Ledger.md`.
- Map, continuity fixes and all open questions: project doc `claude/Book_Map_Continuity.md`.
- Already made (heavily branded, every page): `Book/build/EXPERIMENTAL_NOT_APPROVED_5_Laws_Chapters_2-7.docx` and `.pdf`. Chapters 2 to 7 only. Not the book build. Leave it as it is.
- New Google Doc drafts folder (his call, 21 Oct): "5 Laws Manuscript Drafts", id 1rmgnWP9AHkgZjDnk6yvv-9SDaMx5Aq1K.

## Done
- Chapter 3 (Law 1) epoch 2 from the 20 Oct grilling. Chapters 2, 4, 5, 6, 7 epoch 1 written overnight without him. None marked up or scored by him.
- All files on the Mac, Book_Status.md updated (rows annotated, ownership section "Overnight run").
- One merged, heavily branded docx/pdf of Chapters 2 to 7.

## In progress
Nothing. The branch build has not started.

## Next, in order
1. Read `Book/Book_Status.md` (the master draft section) and `source/build.js`, `source/make_book.py` to see how a build runs and where it writes.
2. Make the branch without touching the master: copy `source/` to `Book/experimental/source/` (or add an output-name switch), so its output never lands on `5_Laws_of_Lasting_Change_Draft.*` and never triggers the master's archive step.
3. Turn each experimental `chapter.md` into a chapter file in the format of `source/chapters/chapter-1.js` (Chapter 2, then Chapters 3 to 7). Keep Summary and From Within You boxes as the existing chapters do. Leave out the grey end notes ("From Claude, ..."). Use no `notes` unless the format needs an empty list.
4. Title: on the cover and title page, mark it as the experimental branch, for example "5 Laws of Lasting Change, Experimental Branch". File names: `5_Laws_Experimental_Branch.docx`, `.pdf` and the A4 booklet, in `Book/experimental/`. Nothing else in the pages says experimental.
5. Build, open the PDF, check page order (chapters start on right-hand pages), Contents, and that no em dashes or "my clients" slipped in.
6. Send him the PDF. Add one line to Book_Status.md (add only): where the branch lives and that it is not the master.

## Rules for this work
- The real master draft and its archive stay untouched. Merges into the master only through /merge-epoch-to-book, at his word, per approved epoch.
- No content changes to the chapters in this build. The continuity fixes in Book_Map_Continuity.md are for the next epochs, not this build.
- Never retype files. Move bytes (stage, md5 check, mv). Deleting on the Mac needs his permission.
- Book_Status.md, handoffs and logs: add and annotate only. Protected docs (Language Rules, Book Rules) are never written.
- No em dashes, no semicolons, British spelling, never "my clients".
- Concise replies, no reflective commentary, no "what's next" unless he asks.

## Suggested skills
- `anthropic-skills:merge-epoch-to-book` for how the build system works. Read it, but don't run its merge into the master.
- `anthropic-skills:book-draft-to-booklet` if he asks to print the branch.
- `anthropic-skills:docx` and `anthropic-skills:pdf` only if the build system needs help.
