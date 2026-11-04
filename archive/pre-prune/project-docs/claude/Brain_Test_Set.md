# Brain Test Set (2026-10-27)

20 questions to test brain search before and after any tuning. A test passes when an expected ref lands in the top 5 of `brain.search_all(question, 5)`. Q20 passes when nothing comes back.

Expected refs were chosen from the opening lines of entries. Correct any that are wrong. Add only. Do not remove questions, so old and new runs stay comparable.

| # | Question | Expected ref | What it tests |
|---|---|---|---|
| 1 | Does missing one day ruin a new habit? | WS-L5-F6-03, WS-L3-F6-07 | Loose question, research fact |
| 2 | What is the proof file? | WS-TR-CoreExercise-256a-L5, WS-L5-F2-14 | Coined term, thin entry |
| 3 | How do I phase out coaching check-ins over time? | WS-L5-F2-07, OBS-L5-Resources-02 | Paraphrase |
| 4 | Client thinks a motivation dip means he is sabotaging himself | WS-L3-F6-01 | Client story, loose |
| 5 | Client watched every course video but skipped the worksheets | T-301 | Client words |
| 6 | Fear of effort versus fear of the outcome | A-22 | Coach golden rule |
| 7 | Why is failing after trying hard scarier than not trying? | F-94 | Own story, loose |
| 8 | The maze dead end and retracing your steps | F-137 | Metaphor |
| 9 | Why does knowing 7 x 8 by heart help the mind? | WS-L5-F1-16 | Outside voice |
| 10 | What is a yearly misogi? | WS-L5-F2-21 | Exact term |
| 11 | How does a planned break prove the skill follows you? | WS-L5-F2-13 | Law 5 tool |
| 12 | Client keeps breaking promises to himself | WS-L4-F2-08 | Promise ladder, loose |
| 13 | Is coaching the same as seeing a psychiatrist? | WS-TR-Misconceptions-5e5f-L2 | Misconception |
| 14 | Why does scolding myself hurt my speaking? | WS-L2-F1-07 | Cross-topic |
| 15 | Teach clients to fish, not give the fish | T-032 | Coach line |
| 16 | Why do introverts feel tired after meetings? | A-19 | Introvert theory |
| 17 | High standards and high support together | WS-L4-F2-13 | Outside voice, Yeager |
| 18 | Burnout from gripping a gym habit | WS-L5-F7-03 | Kodawari, loose |
| 19 | What did Gen say about bringing notes in the icebreaker speech? | Icebreaker chunk @00:01:24 | Chunk layer |
| 20 | What does Gen think about cryptocurrency? | None | Must return nothing above the 0.30 cutoff |

## Known limits
- Q19's expected chunk is a guess from the document title.
- Q2 and Q18 point at thin or partial entries.
- No Law 0 or untagged entries yet.

## Runs
(Never overwrite a run. Add the next one below.)

### Run 1: Baseline, 2026-10-27 18:35, search_all as it stands (AND word match)
Score: 14 pass, 1 unconfirmed, 5 fail.

| # | Result | Top 5 notes |
|---|---|---|
| 1 | Pass | Both expected refs in top 5 |
| 2 | Pass | WS-L5-F2-14 found, only 3 results |
| 3 | Pass | OBS-L5-Resources-02 at rank 5, two icebreaker chunks above it |
| 4 | Pass | Rank 2, icebreaker chunk at rank 1 |
| 5 | Fail | T-301 missing. Returned W-302, WS-L3-F2-13 and others |
| 6 | Pass | A-22 at rank 2 |
| 7 | Pass | Rank 3, icebreaker chunk at rank 1 |
| 8 | Pass | Rank 2 |
| 9 | Pass | Rank 1 |
| 10 | Fail | Returned nothing. The exact word "misogi" was not matched |
| 11 | Pass | Rank 3, icebreaker chunk at rank 1 |
| 12 | Pass | Rank 2 |
| 13 | Pass | Rank 3 |
| 14 | Pass | Rank 2, icebreaker chunk at rank 1 |
| 15 | Fail | T-032 missing |
| 16 | Pass | Rank 1 |
| 17 | Pass | Rank 1 |
| 18 | Fail | WS-L5-F7-03 missing |
| 19 | Unconfirmed | Icebreaker chunks returned, timestamp cut off in the output |
| 20 | Fail | Should return nothing. Returned WS-L1-F1-09 |

Patterns:
- Q10 is the AND word match problem. "What is a yearly misogi?" needs every word in one entry, so the exact word "misogi" finds nothing.
- Icebreaker speech chunks took the top slot in 7 of 20 questions that were not about the speech (Q3, 4, 7, 11, 12, 14, 18). Chunk context lines hold only the title and timestamp.
- Q20 shows the 0.30 cutoff lets an unrelated entry through.

### Run 2: 2026-10-27, migration 009 (OR word match, filler words dropped)
Score: 16 pass, 4 fail.
- New passes: Q5 (T-301 rank 2), Q19 (icebreaker @00:01:24 rank 2, now confirmed).
- Still failing: Q10, Q15, Q18, Q20.
- Q10 cause found: WS-L5-F2-21 matched by words, but its meaning score was 0.253, under the 0.30 cutoff. A match on both meaning and words was dropped, while a weaker words-only match (F-11) passed.

### Run 3: 2026-10-27, migration 010 (any word match passes the cutoff, gold and chunks)
Score: 16 pass, 4 fail.
- Q10 now passes (WS-L5-F2-21 rank 1).
- Q13 broke. Icebreaker chunks entered the top 5 of 11 of the 18 non-speech questions. Long spoken chunks match many words.
- Rejected. Fixed in Run 4.

### Run 4: 2026-10-27, migration 011 (word match skips the cutoff for gold entries only, chunks keep the 0.30 cutoff)
Score: 17 pass, 3 fail. This is the live version.

| # | Result | Note |
|---|---|---|
| 1 | Pass | Ranks 1 and 2, no chunks |
| 2 | Pass | Both expected refs now in top 5 |
| 3 | Pass | Rank 3, two icebreaker chunks above |
| 4 | Pass | Rank 1 |
| 5 | Pass | Rank 2 (failed in baseline) |
| 6 | Pass | Rank 1 |
| 7 | Pass | Rank 2, icebreaker chunk at rank 1 |
| 8 | Pass | Rank 2 |
| 9 | Pass | Rank 1 |
| 10 | Pass | Rank 1 (failed in baseline) |
| 11 | Pass | Rank 2, no chunks |
| 12 | Pass | Rank 2, no chunks |
| 13 | Pass | Rank 4 |
| 14 | Pass | Rank 1 |
| 15 | Fail | T-032 matches all 4 words, meaning 0.326, still outside top 5 |
| 16 | Pass | Rank 1 |
| 17 | Pass | Rank 1 |
| 18 | Fail | WS-L5-F7-03 matches 2 words, meaning 0.366, outside top 5 |
| 19 | Pass | Icebreaker @00:01:24 at rank 2 |
| 20 | Fail | WS-L1-F1-09 at meaning 0.305, just over the 0.30 cutoff, no word match |

Icebreaker chunks in the top 5 of non-speech questions: 4 of 18 (baseline 7).

Open causes:
- Q15: T-032's search text carries a long call link and timestamps, which dilutes its word rank.
- Q20: cutoff 0.30 is a hair too low for pure meaning matches.

### Run 5: 2026-10-27, migration 012 (default cutoff raised from 0.30 to 0.32)
Score: 18 pass, 2 fail. This is the live version.
- Q20 now passes: returns nothing.
- No question lost its expected ref.
- Q3 and Q4 dropped one icebreaker chunk each. Icebreaker chunks still appear in the top 5 of 4 of 18 non-speech questions, now 1 chunk each in Q3, Q4 and Q7, 2 in Q14.
- Still failing: Q15 (T-032) and Q18 (WS-L5-F7-03). Both are ranking problems, not cutoff problems. Left for later, once more material is in.

### Run 6: 2026-10-28, after The War of Art went into the raw layer (documents id 3, 103 chunks, outside)
Score: 18 pass, 2 fail. Same as Run 5. The book did not push out any expected gold entry.
- War of Art chunks now appear in the top 5 of Q4, Q6, Q7 and Q12, next to his own entries. This is the wanted cross-reference behaviour.
- Still failing: Q15 and Q18 (ranking, unchanged).

## Cross-reference tests (added 2026-10-28)
Goal set by Coach Gen: when he asks about his own idea, search should also bring back the outside author who says something close, so he can cite them. Each test is his idea in plain words. It passes when his own entry is found AND a fitting outside passage comes back. Q30 and Q31 must return no outside passage.

| # | His idea (question) | His entry | Fitting War of Art section (PDF page) |
|---|---|---|---|
| 21 | Fear has two sides: fear of the effort and fear of the outcome | A-22 | Resistance and Fear (51), Fear (137) |
| 22 | Going it alone and giving up early keep the old identity safe | WS-TR-HiddenReward-57c9-L4 | Fear (137 to 138), Resistance and Isolation (55) |
| 23 | Clients think they must fix their past first, like seeing a psychiatrist, before they can change | WS-TR-Misconceptions-5e5f-L2 | Resistance and Healing (57) |
| 24 | A morning ritual that gets me into the work | F-104 | What I Do (11), What a Writer's Day Feels Like (69) |
| 25 | Clients are seeking approval to change | WS-TR-StuckSymptoms-2463-L1 | A Professional Self-Validates (93 to 94) |
| 26 | Every time you fail to change, you succeed at staying who you are | BL-65 | The Authentic Self (139), The Unlived Life (13) |
| 27 | Consistency is the effort you can give each day, not speed | F-93 | A Professional Is Patient (78) |
| 28 | Self-scolding: you can do better but you are lazy | WS-L2-F1-07 | A Professional Self-Validates (93) |
| 29 | Commando conditioning: it does not matter whether you like it, you do it | F-04 | How to Be Miserable (71) |
| 30 | Talented kid who coasted on being smart and then fell behind | F-12 | None fits. Must return no outside passage |
| 31 | How do I file my Indonesian tax return? | none | None. Must return nothing |

### Cross-reference run A: 2026-10-28, search_all as it stands (both layers, top 8, cutoff 0.32)
His own entry found: 10 of 10.
Fitting outside passage found: 4 of 9 (Q21, Q22, Q24, Q28).
Cause: for the misses the right passage is already the top or second book match, but its meaning score is 0.27 to 0.32. An idea that is close but worded differently scores lower than a direct match, so the 0.32 chunk cutoff drops it.

### Cross-reference run B: 2026-10-28, test query only (outside documents only, top 3, cutoff 0.25)
Fitting outside passage found: 9 of 9.
Q20 (cryptocurrency), Q30 and Q31 returned nothing. Pass.
Not built yet. Proposed as a separate outside search, so the main search keeps its cutoff.

## Run 7: voices search (28 Oct 2026)

Function: `brain.search_voices(p_query, p_scope, p_limit_own, p_limit_outside, p_min_sim, p_outside_min_sim)`. Migrations 014 and 014b.

How it works:
- `p_scope = 'own'`: your gold entries (including entries typed "outside voice" that you adopted into your framework) and chunks from your own documents. Cutoff 0.32 on meaning, same rules as the main search.
- `p_scope = 'outside'`: chunks from documents owned by `outside` only. Cutoff 0.25 on meaning, top 3 by similarity.
- `p_scope = 'all'` (default): both lists side by side. Each row carries `voice` (own or outside), `author`, `source`, and `place`. For books `place` reads "page 93" instead of a fake timestamp.

Original 20 questions (own scope, top 5): 18 of 20. Same result as Run 6. Q15 and Q18 still fail for the same reasons. Q9 and Q17 first dropped out because gold entries typed "outside voice" were filtered from the own list by mistake. Fixed in 014b. Q20 returns nothing, as it should.

Cross-reference questions Q21 to Q31:
- Own entry in top 5: Q21, Q22, Q23, Q24, Q26, Q27, Q28, Q29, Q30 found (9 of 10). Q25 sits at rank 9 and is found in the top 10. This is the same rank as in the main search, so the voices search did not cause it.
- Fitting outside passage in top 3: 9 of 9 (Q21 p137, Q22 p55, Q23 p57, Q24 p69, Q25 p94, Q26 p139, Q27 p78, Q28 p93, Q29 p71).
- Q30 (talented kid): outside list empty, as it should be.
- Q31 (tax return): outside list empty, as it should be. The own list still returns word matches on "file" and "return" (WS-L5-F2-14 and similar). This is the known word-match rule for gold entries, left as is.

Weak outside hits worth knowing: Q23 scores 0.27 and Q25 scores 0.26. They land just above the 0.25 cutoff. If outside material grows, watch for off-topic passages near that line.

## Correction to Run 7 and the readable log (28 Oct 2026)

Correction: the Run 7 text above says the own entry was in the top 5 for 9 of 10 cross-reference questions, with Q27 counted as found. That was wrong. F-93 (Q27) is not in the top 10 at all. Its meaning score is 0.339, which passes the 0.32 cutoff, but other entries and chunks rank higher. The right count is 8 of 10 in the top 5 (Q21, Q22, Q23, Q24, Q26, Q28, Q29, Q30). Q25 sits at rank 9 and Q27 is missing. The book side is unchanged: 9 of 9.

How to read the log: "Own" is your gold entries and your own chunks, top 5 counted. "Book" is the outside list, top 3 counted. For Q1 to Q20 no book passage was expected, so book hits there are listed but not scored. They are the first data on wrong citations.

Q1  PASS  Does missing one day ruin a new habit?
    Own: WS-L5-F6-03 #1, WS-L3-F6-07 #2. Book: none returned.
Q2  PASS  What is the proof file?
    Own: WS-L5-F2-14 #1, WS-TR-CoreExercise-256a-L5 #5. Book: none returned.
Q3  PASS  How do I phase out coaching check-ins over time?
    Own: OBS-L5-Resources-02 #1, WS-L5-F2-07 #2. Book: none returned.
Q4  PASS  Client thinks a motivation dip means he is sabotaging himself
    Own: WS-L3-F6-01 #1. Book (not scored): p31 0.39, p39 0.38, p59 0.36.
Q5  PASS  Client watched every course video but skipped the worksheets
    Own: T-301 #2. Book: none returned.
Q6  PASS  Fear of effort versus fear of the outcome
    Own: A-22 #1. Book (not scored): p137 0.50, p50 0.45, p135 0.41. All on fear, fitting.
Q7  PASS  Why is failing after trying hard scarier than not trying?
    Own: F-94 #1. Book (not scored): p137 0.41, p50 0.38, p138 0.37. Fitting.
Q8  PASS  The maze dead end and retracing your steps
    Own: F-137 #2. Book (not scored): p110 0.26 about Watergate. Off topic.
Q9  PASS  Why does knowing 7 x 8 by heart help the mind?
    Own: WS-L5-F1-16 #1. Book: none returned.
Q10 PASS  What is a yearly misogi?
    Own: WS-L5-F2-21 #1. Book: none returned.
Q11 PASS  How does a planned break prove the skill follows you?
    Own: WS-L5-F2-13 #2. Book (not scored): p84 0.29, p93 0.28, p93 0.28. Loose fit.
Q12 PASS  Client keeps breaking promises to himself
    Own: WS-L4-F2-08 #2. Book (not scored): p91 0.35, p99 0.34, p39 0.35. Loose fit.
Q13 PASS  Is coaching the same as seeing a psychiatrist?
    Own: WS-TR-Misconceptions-5e5f-L2 #4. Book (not scored): p39 0.27, p38 0.26, p87 0.25. p39 fits, the rest are weak.
Q14 PASS  Why does scolding myself hurt my speaking?
    Own: WS-L2-F1-07 #2. Book (not scored): p158 0.25, p57 0.28, p99 0.27. Weak.
Q15 FAIL  Teach clients to fish, not give the fish
    Own: T-032 at #7, outside the top 5. Book (not scored): p87 0.28, p84 0.25. Off topic.
Q16 PASS  Why do introverts feel tired after meetings?
    Own: A-19 #1. Book: none returned.
Q17 PASS  High standards and high support together
    Own: WS-L4-F2-13 #1. Book (not scored): p58 0.26, p142 0.25. Off topic.
Q18 FAIL  Burnout from gripping a gym habit
    Own: WS-L5-F7-03 at #7, outside the top 5. Book (not scored): p93 0.31, p39 0.30, p93 0.29. Loose fit.
Q19 PASS  What did Gen say about bringing notes in the icebreaker speech?
    Own: Icebreaker @00:01:24 #2. Book: none returned.
Q20 PASS  What does Gen think about cryptocurrency?
    Expected nothing. Own: nothing. Book: nothing.
Q1 to Q20: 18 of 20.

Q21 PASS  Fear has two sides: fear of the effort and fear of the outcome
    Own: A-22 #1. Book: expected p51 or p137, found p137 0.52 (also p50 0.46, p138 0.40).
Q22 PASS  Going it alone and giving up early keep the old identity safe
    Own: WS-TR-HiddenReward-57c9-L4 #1. Book: expected p137, p138 or p55, found p55 0.35 and p138 0.33 (also p31 0.34).
Q23 PASS  Clients think they must fix their past first, like seeing a psychiatrist
    Own: WS-TR-Misconceptions-5e5f-L2 #1. Book: expected p57, found p57 twice at 0.27 (also p39 0.28). Weak score.
Q24 PASS  A morning ritual that gets me into the work
    Own: F-104 #1. Book: expected p11 or p69, found p69 0.43 and p11 0.43 (also p109 0.40).
Q25 FAIL(own) PASS(book)  Clients are seeking approval to change
    Own: WS-TR-StuckSymptoms-2463-L1 at #9, outside the top 5. Book: expected p93 or p94, found p94 0.26. Weak score, only one result.
Q26 PASS  Every time you fail to change, you succeed at staying who you are
    Own: BL-65 #1. Book: expected p139 or p13, found p139 0.34 (also p89 0.34 and 0.33).
Q27 FAIL(own) PASS(book)  Consistency is the effort you can give each day, not speed
    Own: F-93 not in the top 10 (meaning score 0.339). Got WS-TR-Stories-cbb3-L3, F-04, OBS-L4-StuckSymptoms-03. Book: expected p78, found p78 0.29 (also p72 0.29, p11 0.28).
Q28 PASS  Self-scolding: you can do better but you are lazy
    Own: WS-L2-F1-07 #1. Book: expected p93, found p93 0.32 (also p89 0.31, p99 0.31).
Q29 PASS  Commando conditioning: it does not matter whether you like it, you do it
    Own: F-04 #1. Book: expected p71, found p71 0.32 (also p11 0.32, p14 0.30).
Q30 PASS  Talented kid who coasted on being smart and then fell behind
    Own: F-12 at #2 or #3 (a tie, order varies). Book: expected nothing, returned nothing.
Q31 PASS(book)  How do I file my Indonesian tax return?
    Book: expected nothing, returned nothing. Own side still returns WS-L5-F2-14, WS-TR-CoreExercise-256a-L5 and F-20 because "file" and "return" match words.
Q21 to Q31: own 8 of 10 in the top 5, book 9 of 9, empty book list correct on Q30 and Q31.

What the book hits on Q1 to Q20 show: of 11 questions that returned book passages, 4 fit (Q6, Q7, Q13 partly, Q4 partly), and 7 are loose or off topic (Q8, Q11, Q12, Q14, Q15, Q17, Q18 by my reading). Wrong citations are real. All the off-topic ones score between 0.25 and 0.31. Raising the outside cutoff from 0.25 to about 0.30 would cut most of them but would also lose the Q23, Q25 and Q27 matches that score 0.26 to 0.29. This trade-off is the main open question for the outside search.

## Run 8: five outside books (1 Nov 2026)

What changed since Run 7: Mindset (source 54), Atomic Habits (source 47) and The Courage to Be Disliked (source 45) went into the raw layer as outside books. Migration 016 changed only the label of book chunks in `search_all` (page instead of a time). Migrations 017 and 017b changed the outside list of `search_voices`: the best passage of each book comes first, then the rest by score, and the candidate pool grew from 80 to 250 chunks.

**Own side (top 5), after 017b.** Q1 to Q20: 18 of 20, same as Run 7. Q15 and Q18 still fail for the same ranking reasons. Q20 returns no own rows. Q21 to Q30: 8 of 10, same as Run 7 (Q25 and Q27 still miss). The new books did not push out any own entry.

**Outside side before 017 (three books plus Pressfield, top 3 by score).** One large book often filled all three slots. Pressfield's expected page came back only for Q21. Most new hits fit the idea (Dweck on fear of effort for Q6, Q7 and Q21, Clear on habits for Q1 and Q12, Kishimi and Koga on self-scolding for Q14).

**Outside side after 017b (one per book first).** At least one fitting passage in the top 3 (my reading of the first lines):
- Q21 PASS: Dweck p45 (trying and failing is the worst fear), Pressfield p137
- Q22 PASS: Pressfield p55 (afraid of being alone), Kishimi and Koga p45 (people choose their lifestyle)
- Q23 PASS: Kishimi and Koga p33 (staying in etiology, the past)
- Q24 PASS: Pressfield p11 (What I Do), Clear p64
- Q25 PASS: Clear p104 (behaviors that earn approval)
- Q26 PASS: Clear p36 (the story you repeat), Kishimi and Koga p45
- Q27 PASS: Clear p115 (Walk Slowly, but Never Backward), Dweck p42 (tortoise and hare), Pressfield p78
- Q28 FAIL: Kishimi and Koga p112, Dweck p175, Clear p59, all loose. Pressfield p93 (0.32) is outranked.
- Q29 FAIL: all loose. Pressfield p71 is outranked.
Score: 7 of 9 fitting. Pressfield's expected page: 4 of 9 (Q21, Q22, Q24, Q27). The expected pages in the Q21 to Q29 table were set when Pressfield was the only book, so this count is kept for comparison only.

**Questions whose expectation no longer holds.**
- Q30 (talented kid who coasted): Mindset is about exactly this, so a book passage is now right. Dweck p229, p58, p63 come back. Q30 now counts as a pass when a Mindset passage returns.
- Q20 (cryptocurrency): the outside list returns 3 rows at about 0.26 to 0.28 (Dweck p116 and p117, Kishimi and Koga p108). Off topic. The 0.25 outside cutoff is now too low for five books. Raising it to 0.30 would also drop the weak but fitting Pressfield matches. Open question, not changed in this run.
- Q31 (tax return): outside list empty. Pass.

Open items: Q15, Q18, Q25 and Q27 (own ranking), Q28 and Q29 (book ranking), and the outside cutoff (Q20).
