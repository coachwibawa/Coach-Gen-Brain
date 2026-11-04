# Alpha Book Handoff

Written 27 Oct 2026. Add-only: update status lines and add dated sections, never condense.

## Start here

Opener to paste in a new chat: "/coach-gen-writer chapter Law 1. Read claude/Book_Alpha_Handoff.md and continue from Next, step 1."

Goal: an alpha-reader booklet of Introduction to Chapter 3, and an article slice from the finished Chapter 3. He chose the slower, full path (developmental edit, his markup, epochs, merge).

## Rules that bit in the last chat

1. Every chapter or redraft goes to him as a Google Doc epoch, never a bare .md or a file in the side panel. Load the coach-gen-writer skill first, and again after any summary. The skill now says so.
2. Read the latest Drive doc WITH comments before saying anything is "waiting for markup".
3. Where the draft looks odd and Claude wrote it, Claude fixes it and decides. Do not turn it into a question for him.
4. No em dashes, no semicolons, simple English. Options as a numbered list. "ok" means act.
5. Mac is master. Never retype files. Logs and handoffs are add-only.
6. Print names only. NEVER USE list: no health details, money figures, legal matters, family history, third parties' private stories, organisation or school names, religious lines, identifying hobby details.

## State

| Piece | State |
|---|---|
| Introduction | In the master draft. 250 hours, disclaimer (two paragraphs, languages), done. Needs one warm parent line (not done). |
| Chapter 1 | In the master draft. Mike renamed. New flagship line in. Still says "hundreds of hours": change to "about 250" (not done). |
| Chapter 2 | Epoch 2 drafted (about 2,870 words) at `Book/build/chapter-2/epoch2_chapter.md` on the Mac. NOT in Drive as an epoch. A stray doc "ch2_epoch2.md" (id 1qa74OwMjvS50meQuYcwTatJn6TP8Af8sarU9vUbyHc8) sits in Drive from the side-panel render. Ask him before trashing it. Epoch 1 doc id 17wMwmVYjuWFFSa-JnvRCgCCfv_D03DAAwgz41kVmk9o. |
| Chapter 3 | Epoch 2 doc (id 1g7YmazrTbMeNAXkAbMg6z36wWaLcOoCmfLc65jtYWl8) holds his two comments from 21 Oct: next to "he owed a friend" he wrote "200 dollars", next to "The direction was missing" he wrote "maybe good place to subchapter". No score seen. Redraft not started. The "200 dollars" is a money figure: leave it out of print unless he says otherwise. |
| Master draft | PDF rebuilt 26 Oct and again 27 Oct with the new flagship line (17 pages, Intro and Ch1 only). |
| make_book.py | Needs the experimental branch's label fix before Chapter 2 can merge (a heading per Law). |

## Decisions (his, logged in claude/Brainstorm_Log.md and claude/Persona_Impact_Notes.md)

- Flagship line: "Every time you fail to make change, you succeed at staying who you are." It gets a callback in each Law.
- Villain: the Keeper. It keeps whatever is current: hard to move when still, hard to stop when moving. It changes sides once the new habit is the current thing.
- Five Keeps: Keep Their Course, Keep Past Regret, Keep Present Friction, Keep Old Habits, Keep Worrying. They go in Chapter 2 and make the Laws feel complete.
- The brake (a foot) and the Keeper (the weight of the car) are two separate points. Both stay.
- Show the Keeper misbehaving while moving. Readers can name their own Keeper later.
- Claude's calls for Chapter 3 (he said to decide): swap made-up people for cast. Michael (borrowed goal, parents), Putri (exam story, "grades should speak for her") and Andi (a direction can take a year) go in. Setsu moves to Law 2, Aiman to Law 3. The camps line becomes whose reason, not who paid. One warm parent line each in Intro, Ch2, Ch3. Joe Liemandt once only. Replace the From Within You question that repeats the body ("Whose permission..."). Keep the length near 5,600 words.

## Next, in order

1. Load /coach-gen-writer and its rules (once). Read claude/Persona_Impact_Notes.md and the last sections of claude/Brainstorm_Log.md.
2. Chapter 2: build "5 Laws Manuscript, Chapter 2 (The 5 Laws) Epoch 2" as a Google Doc from `Book/build/chapter-2/epoch2_chapter.md`, laid out per Book_Writing_Handoff section 5 (HTML, create_file). Update Book_Status.md and the calibration log.
3. Chapter 3: read Epoch 2 in Drive with comments, log his two comments word for word, redraft whole as Epoch 3 from the fact sheet (`Book/build/law-1/fact_sheet_ch3.md`) and the decisions above. Deliver as a Google Doc. Callback to the flagship line in "What Do You Get From Not Trying?".
4. His markup on both. Apply. Line edit.
5. Fix make_book.py (label fix), then merge Ch2 and Ch3 with merge-epoch-to-book.
6. Add the parent line to the Introduction. Change Ch1 "hundreds of hours" to "about 250".
7. Alpha booklet with the book-draft-to-booklet skill: a beta cover and a five-question feedback sheet.
8. Article slice from the finished Chapter 3.

## Not blocking the alpha

Laws 4 to 7 and the Keeper callbacks in them. The Brain (Supabase) migration. Website fixes to the Dragon articles. Eurich's figure in "On Blind Spots" (10 to 15%). Stefanie calls (ask first).
