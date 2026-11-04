# Main Brain Input: Handoff (2026-10-26)

## Start here
This chat is the main brain input for the 5 Laws project. It takes in new raw material (Fathom calls, podcasts, articles, his voice dumps and chat thoughts) and routes each piece to its right home. It does not draft the book or articles (that is the `coach-gen-writer` chats) and it does not do company admin (that is `claude/Company_Docs_and_Tax_Handoff.md`).

## Where things live
- **The worksheet (SSOT):** `build_worksheet.js` on his Mac, in `/Users/coachwibawa/Documents/5 Laws of Lasting Change/` (`$HOME/mnt/5 Laws of Lasting Change/` in device_bash). The `/extract-fathom` skill holds the field map, the `callNoteOn` helper, the tag formats and the build command. Older backup copies sit in `Book/build/archive/` on the Mac.
- **What has been mined:** `claude/Fathom_Mined_Log.md`. Two tables: worksheet passes, and book material passes (21 Oct onward). Plus the "not mined on purpose" lines.
- **Book material bank:** `claude/New_Material_21Oct.md`. IDs A- (his articles), L- (Lasting Change Letters), N- (Notion notes), B- (reference books), F- (Fathom, latest F-144), W- (Wayan). Also the "original sources for outside voices" table and the consent updates.
  - (Update 27 Oct: latest F- is now F-150. The file name is only the date it was started. It is the book material bank.)
- **Book map:** `claude/Book_Map_Continuity.md` and the Book Map vault on the Mac, where new pieces get status "new".
- **Printable quotes:** `claude/Testimony_Mastertext_Collection.md` (mirror of the Mac copy). Cast: Sri prints as Melina, Kin prints as David, Dan Sato is built. Section 5 is the NEVER USE list.
- **To-dos from calls:** `Master_Project_Status.md`.
- **Facts about him:** project memory (for example the naming rule in brand-identity).

## Where each kind of material goes
1. Explains or sharpens a Law, its exercise, misconception, misexecution, sequence or skip cost: a tagged note in the worksheet.
2. A story, line or image the book could use: a new F- (or A-, B-, W-) entry in `New_Material_21Oct.md`, verbatim with a timestamp link, so any persona or chapter can use it.
3. A client or coach line fit to print: the Testimony collection, add-only, with print name and placement.
4. A to-do or decision: `Master_Project_Status.md`.
5. A durable fact or preference about him: memory.

One piece can go to more than one home (the 26 Oct Kin call went to both the F- bank and the worksheet).

**How the writing chats find it (27 Oct).** It is a pull system: a writing chat reads only the files its skill lists. Before 27 Oct, `coach-gen-writer` and `write-book-from-material` did not list the bank, so bank entries never reached a chapter unless someone pointed a chat at them. On 27 Oct he asked for a system where mined material reaches the writing chats with no one notifying them. Three skill updates were proposed: `coach-gen-writer` and `write-book-from-material` now read the whole bank for every piece and take the entries for that Law, and `extract-fathom` now writes every printable story or line to the bank (step 6b). So the rule for this chat: anything that might be printed goes in the bank, even if it also went to the worksheet. If the skill cards were not saved, the writing chats still cannot see the bank. Check that first.

## Done
- Every Fathom call up to and including 26 Oct 2026 is mined. See the log for which passes each call got.
- Huberman / Alpha School podcast folded into the worksheet (14 Oct).
- Consent: Sri is okay with her material being kept and used (asked 20 Oct, despite her completion form). Wayan, the cafe owner, the tech lead and the CEO who wanted out gave consent on 22 Oct. Wayan still needs a print name, and workplace details change in print.
- (27 Oct) Next step 1 done: no Fathom calls after 26 Oct. Next step 2 done: the origin story is F-145 to F-150 in the bank, logged in the mined log. Not yet set to "new" in the Book Map vault (no Mac folder was connected).

## In progress
Nothing is half-done. The 26 Oct Kin call had both a book pass (F-109 to F-144) and a worksheet pass (25 notes).

## Next, in order
1. Run `/extract-fathom recent` for any call after 26 Oct.
2. The 5 Laws origin story from the 19 Oct sprint (https://fathom.video/calls/866194711?timestamp=2575, 42:55 to 46:53: Pak Jeffrey's USP questions, "I help people on rock bottom", making it 5 steps, the alliteration) is not in the F- bank yet. Add it as F- entries for the book Introduction.
   - (Done 27 Oct as F-145 to F-150. Still open: Book Map vault status "new" when the Mac is connected, and how Pak Jeffrey is named in print.)
3. Calls left out on purpose stay out unless he says so: Stefanie Toner (ask him first), ACC group mentoring calls, Gen and Genio sprints before August, the 24 Aug finance call.
4. When he pastes a podcast, article or voice dump, route it by the list above and report what went where.

## Rules for this work
- Add-only, everywhere. Never condense, retype or delete existing text. Read the current worksheet file before every edit, because other chats edit it too.
- If the Mac is offline, write nothing anywhere else. Print the notes in chat as ready-to-insert and say they are not written yet.
- Never quote a call from memory. Pull the transcript first.
- Check the NEVER USE list before anything is marked printable: no money figures, health details, religious lines, organisation or club names, or a third person's private story.
- Report in the `/extract-fathom` format: one line per note, with its field, the exact text, the timestamp link and a one-line reason. No PDF. No reflective commentary.
- His documents: no em dashes, no semicolons, simple English.
- (27 Oct) Use his doc names, never nicknames. Say "the book material bank (`New_Material_21Oct.md`)", not "F-bank". He was lost when a made-up label was used.

## Suggested skills
- `extract-fathom`: every Fathom call, by name, date, "recent" or topic.
- `grilling`: when he brings a rough idea and wants it pinned down before it goes into the worksheet.
- `wait-what`: when a report did not land.
- `handoff`: to update this doc when the chat gets long.
- Not here: `coach-gen-writer` (drafting), `merge-epoch-to-book` (book draft), `fold-article-lessons` (rule docs). Point him to the writing chat for those.
