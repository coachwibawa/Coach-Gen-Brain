# Full read: progress checkpoint

Started 4 Oct 2026, on Coach Gen's word: "let's start with the 2 writing rules first. deep analysis as planned. then you can generate back the taste test pieces to see if things improved. also you can annotate things you changed and why you changed (what you learned)"

Resume rule: a new session reads this file, then the notes file for the book in progress, and continues from the first unchecked line. Source texts: Mac folder Book/References (the 5 files). Calibration data: claude/Coach_Gen_Book_Calibration_Log.md.

## Order
- [x] 1. The Elements of Style, 2018 Classic Edition (full). Notes: claude/Full_Read_Notes_1_Elements.md
- [x] 2. On Writing Well, 6th edition (full). Notes: claude/Full_Read_Notes_2_Zinsser.md
- [x] 3. Distil the 2 guides. Done: claude/Findings_Guides.md (16 findings, warnings W1 to W8)
- [x] 4. Round 3 rewrites, annotated. Google Doc "5 Laws Taste Test, Round 3" (id 1N4-iVrELa8bae0sij58gPH59RJKyH5w4Qlovx-Tmg0M). Builder: /home/claude/taste/r3/round3.py. Awaiting his marks, 3 realness questions, and decisions W2 (numbers) and W7 (contractions).
- [x] 5. Atomic Habits, Mindset, Courage read in full (his go, 4 Oct: "let's just proceed with the full reading."). Notes: claude/Full_Read_Notes_3_Atomic_Habits.md, _4_Mindset.md, _5_Courage.md. Findings: claude/Findings_Books.md. Brief: claude/Full_Read_Agent_Brief.md
- [x] 6. Book Rules v2 written 5 Oct on his "execute": claude/Coach_Gen_Book_Rules.md (v2 on top, v1 archived below, word for word).
- [x] 7. Epoch 2 of the Introduction, 5 Oct. Builder: /home/claude/book/v3/epoch2_intro.py (local). Google Doc "5 Laws Manuscript, Introduction Epoch 2" (id 1Nngx_iInjemkUt3bIfTzHnRvE30fTn23opKyT5Dg5XQ). Awaiting his markup and score.
- [x] 8. Epoch 2 scored 5 Oct: sentence construction "maybe 75", content "still held back by previous draft". Logged.
- [x] 9. Calibrate on Chapter 1 from the raw material. Done 5 Oct with the /write-book-from-material skill: Chapter 1 Epoch 1 (Google Doc id 1YZltWO8_iPaujgcgQomZb9xjUFU0V_to3nQGzsCjfX8). From here on, the build state lives in Book/Book_Status.md on his Mac, and working files in Book/build/<chapter>/.

## For the Chapter 1 redraft (found while checking epoch 2)
- "The 5 Laws started as my story" now closes the Introduction. The round 3 Chapter 1 says "They started as my story." Change Chapter 1's line.
- The Introduction names Lasting Change. Chapter 1 ("I started focusing on Lasting Change instead") must read as a callback, not a first mention.
- The Introduction's reader list has "a language app". Chapter 1's Sunday list has "The language you were going to learn". Pick a different example in Chapter 1.

## Update 5 Oct
- Checked after his token cap: all 3 book notes complete (each ends with its status or summary), and every full-read file is in the project.
- Decided: small counts as words, digits for measures (Claude's reading, open to his correction). Contractions allowed. Grammar rule covers fragments ("fragments was the word I was looking for").
- Warning for Book Rules v2: all 3 books use deliberate fragments that hang off a full sentence ("Mostly horrified.", "Tiny changes. Remarkable results."). Default: fix fragments. Ask him case by case about amplifier fragments.

## Questions to read for
1. What makes one sentence lead into the next (his "x=y graph")?
2. How long does a beat get before the writer moves on, and what fills it?
3. Where do short sentences go, and what do they do?
4. How does the writer show warmth and confident authorship at the same time?
5. How do they handle a person's quoted words, so a reader without the backstory still feels them?
6. When do they use a parallel, and when does it fail?
7. What do they cut, and what do they keep that looks cuttable?
8. Where do the guides clash with the Language Rules? (warning, case by case)

## Update 4 Oct, after round 3
- Round 3 judged a failure by him (see calibration log). Round 4: one fresh passage from his pruning story, Google Doc "5 Laws Taste Test, Round 4" (id 129pXV7-OF6J1qdTKngJT1hJO8VrOs_ulM59vi6PZqho). Builder: /home/claude/taste/r4/round4.py. Awaiting marks.
- Lesson for every later draft: use a transcript only to check a fact, never as a source of new detail. Write whole drafts from the material forward, never patch line by line against notes.
