# The two thin margins, full gate (16 Nov 2026)

Why: F1 was caught only by R1.16 and F3 only by R1.11, each for a reason narrower than his own. This run tests how much "5 of 5" rests on.

How it ran: Sonnet helpers, one per rule, each judging all 14 drafts (`cg_check.py batch`). All 20 checkers once, then R1.2, R1.5, R1.11 and R1.16 a second time, then R1.2, R1.5 and R1.16 twice more with new notes. 30 helper runs, about 105,000 tokens each, about 3.1 million in all. Drafts written by script from `test_set.json`.

1. **Before any change: 13 of 14. F1 passed.** No checker failed it. R1.16 missed the "the" and "you" switch in both runs. On 11 Nov it caught it. So the F1 catch was luck, not a margin.
2. R1.5 passed F1 in both runs. Its ground is his own note on F1: "too many differing concepts that were unexplored".
3. R1.2 passed F3 in both runs, though it carried a note taken from F3. His ground on F3: "did I just miss several paragraphs".
4. R1.11 failed F3 in both runs, for the reason he never raised (no turn to the reader).
5. All 9 approved passages passed every checker in every run.

The fix: three notes in `rules/checkers/calibration.json`, each naming its case. No rule text changed.
6. R1.16, from F1: the subject line is a hard line. A run that starts on "the" and switches to "you" is a break.
7. R1.5, from F1: the end of a passage gets no pass. Two or more new ideas in the closing lines, none explained, is a break.
8. R1.2, from F3: a link back must bring the question back in words the reader will know. A passing mention after a paragraph on something else is not a link.

After the notes, each of the three checkers was run twice (the rule from 11 Nov): F1 failed R1.5 and R1.16 both times, F3 failed R1.2 both times, and all 9 approved passages passed both times.

What it does not prove: the three notes quote words from F1 and F3. So the test set now shows the checkers catch these two drafts on his grounds. It shows less about a new draft with the same fault in other words. The blind A/B in step 20 is the test for that.

Files: `before_notes/` holds the answers of R1.2, R1.5, R1.11 and R1.16 from before the notes. `notes_a/` and `notes_b/` hold the two runs after. The table below joins the first full run with `notes_a` for the three changed checkers. The last column is the 11 Nov run.

Result: 14 of 14 cases as expected (5 fail cases, 9 approved passages).

| Case | What it is | Expected | Got | Caught by | Caught by, before |
| --- | --- | --- | --- | --- | --- |
| F1 | Taste test round 3, passage 1: "Why Pushing Harder Fails", p | fail | fail | R1.5 Nothing arrives bare, R1.16 Parallels that truly match | R1.16 Parallels that truly match |
| F2 | Taste test round 3, passages 2 and 3: Melina, with invented  | fail | fail | R1.6 Images from the reader's life, R1.7 One story, told once, R1.11 Bring it to the reader's life | R1.6 Images from the reader's life, R1.7 One story, told once, R1.10 A quote earns its marks, R1.11 Bring it to the reader's life |
| F3 | Chapter 3 (Law 1) epoch 4: the ditch paragraph, with the par | fail | fail | R1.2 Joins answer the reader's question, R1.11 Bring it to the reader's life | R1.11 Bring it to the reader's life |
| F6 | Law 2 chimpanzee piece, v7 | fail | fail | lint, R1.1 One thread, R1.2 Joins answer the reader's question, R1.3 Links are real, R1.4 Few names, one each, R1.5 Nothing arrives bare, R1.7 One story, told once, R1.12 Research backs, never interrupts, R1.13 Built details serve the reader, R1.14 No meta-narration | lint, R1.1 One thread, R1.2 Joins answer the reader's question, R1.3 Links are real, R1.4 Few names, one each, R1.5 Nothing arrives bare, R1.7 One story, told once, R1.12 Research backs, never interrupts, R1.13 Built details serve the reader, R1.14 No meta-narration |
| F8 | Case Study Test round 1, passage 2: Aiman | fail | fail | R1.5 Nothing arrives bare, R1.7 One story, told once, R1.8 Stakes, not more story, R1.9 Warm the water, R1.15 Rhythm without choppiness, R1.20 AI tells | R1.5 Nothing arrives bare, R1.8 Stakes, not more story, R1.9 Warm the water, R1.13 Built details serve the reader, R1.15 Rhythm without choppiness |
| P2 | Lasting Change Letters #1: Never Split The Difference (full, | pass | pass | - | - |
| P3 | Introduction, as merged into the master draft | pass | pass | - | - |
| P4 | Chapter 1, "Staying Who You Are", as merged into the master  | pass | pass | - | - |
| P5 | Article: "3 Stages of Consistency" (published) | pass | pass | - | - |
| P6 | Article: "How can you be busy but lazy?" (published) | pass | pass | - | - |
| P7 | Chapter 3 epoch 4: the parent paragraph | pass | pass | - | - |
| P8 | Chapter 3 epoch 4: the reader's-week paragraph | pass | pass | - | - |
| P9 | Chapter 3 epoch 5: David's points system, your rewrite | pass | pass | - | - |
| P10 | Case Study Test round 1, passage 6: your door-to-door story | pass | pass | - | - |

## F1: Taste test round 3, passage 1: "Why Pushing Harder Fails", patched rewrite

- R1.5 Nothing arrives bare: "And it doesn’t start from zero. Somewhere in your life, you have already changed something without noticing.". The closing lines drop in new ideas with no example, reason or step, so the reader is left holding claims they cannot use.
- R1.5 Nothing arrives bare: "Lasting Change works with the part of you that wants to stay the same, one step at a time, in an order it can accept.". The idea is named and asserted but never shown, so the reader cannot picture what working with that part looks like.
- R1.16 Parallels that truly match: "If the diet slips, make it stricter. If you miss a morning run, set 2 alarms.". The side-by-side examples start on 'the diet', switch to 'you' in the second, then go back to 'the plan', so the run does not match and feels off.

## F2: Taste test round 3, passages 2 and 3: Melina, with invented "health" and "nutritionist"

- R1.6 Images from the reader's life: "a plan so big it never left the page". A made-up metaphor the reader has to decode, not an image from their own life.
- R1.6 Images from the reader's life: "it closes the case on her: if she just can’t, there is nothing left to try". A courtroom image (verdict, closing and opening the case) is a second image system the reader must decode.
- R1.7 One story, told once: "Even her nutritionist once told her that if she were really consistent she would see results every week". After Melina's story is told whole, the second half returns to it and adds a new scene, which breaks 'no new pieces of it later'.
- R1.7 One story, told once: "For years, that sentence ended every attempt Melina made at getting healthier.". This retells her story a second time after the divider instead of giving a short callback in the same words.
- R1.11 Bring it to the reader's life: "A verdict is something you can only accept. A cause is something you can work on.". The passage stays with Melina's health case and the writer's own 20s, and never shows how this sentence-as-verdict pattern reaches the reader's work, money, relationships or other areas.

## F3: Chapter 3 (Law 1) epoch 4: the ditch paragraph, with the paragraphs around it

- R1.2 Joins answer the reader's question: "He had already answered his own question about clarity, in a picture of his own.". The clarity question was asked a full paragraph earlier and is only mentioned in passing here, so the reader has to hunt for what was asked and the picture seems to come from nowhere.
- R1.11 Bring it to the reader's life: "He didn't need more options. He needed the focus to stick with what he picked.". The passage ends inside David's story and never turns to the reader's own life or shows the pattern in other areas, so the reader is left to translate it alone.

## F6: Law 2 chimpanzee piece, v7

- lint, T0 no em dashes: em dash. Use a full stop, comma, colon or brackets
- lint, T0 no em dashes: em dash. Use a full stop, comma, colon or brackets
- lint, T0 no em dashes: em dash. Use a full stop, comma, colon or brackets
- lint, article card headers: missing the header line "Insights from me, to you." on a line of its own
- lint, article card headers: missing the header line "Insights from other experts." on a line of its own
- lint, article card headers: missing the header line "Insight from within you." on a line of its own
- R1.1 One thread: "Two lessons, 10 years apart. Most of us only ever learn the first one.". The second lesson (Melvin earns his place by taking risk) is set up and then never used for the human reader, so the chimp thread is dropped.
- R1.1 One thread: "So why does it still shout at you at 2am, 20 years later?". The piece suddenly turns from a 15-year-old's written rule to regret and its lesson, a new idea the chimp story did not set up, so the reader loses what the piece is about.
- R1.1 One thread: "tell it as a story about somebody else and find the moral. That is why there is a chimpanzee in my notes.". The stated reason for the chimp does not match how the chimp story was told, so the reader has to guess the link.
- R1.2 Joins answer the reader's question: "Then one day Melvin makes the mistake that costs him.". It follows a paragraph that said the hazing ends when they let him in and that he did nothing wrong, so the reader cannot tell how this fits or when it happens.
- R1.2 Joins answer the reader's question: "I have watched a load come off someone's chest for the first time in 20 years, in a single afternoon". It lands after the closing question with no link to it, so the reader does not know what it answers or why it comes here.
- R1.3 Links are real: "Then one day Melvin makes the mistake that costs him.". The false 'Then' puts a punishment-causing mistake after he was let in, and it contradicts the line 'He did nothing wrong', so the reader loses the timeline.
- R1.3 Links are real: "So why does it still shout at you at 2am, 20 years later?". 'It' has no clear referent, since the reader must guess whether it means the written sentence, the memory or the regret.
- R1.3 Links are real: "Because it is not finished with you.". The far 'it' is left unnamed, and the answer only becomes clear when 'Regret' appears a line later.
- R1.4 Few names, one each: "Reddy calls it close to hazing, and it runs for 10 years". The researcher is named again and again in Insight 1 (primatologist, Reddy twice more) when she should appear once with a role or not at all, which adds names the reader must carry.
- R1.4 Few names, one each: "Because it is not finished with you. It still has a lesson to teach". The same thing is called a sentence, a memory, a lesson and regret, so the reader cannot tell what 'it' that shouts at 2am refers to.
- R1.4 Few names, one each: "Regret is not punishment, it is there to stop you repeating something.". 'Regret' appears here as a new name for the thing earlier called 'that one sentence' and 'memory', so the reader has to guess it is the same thing.
- R1.5 Nothing arrives bare: "Because it is not finished with you. It still has a lesson to teach, and you have not learned it yet. Regret is not punishment, it is there to stop you repeating something.". A surprising claim about regret is stated flat with no example, reason or premise, so the reader must take it on trust.
- R1.5 Nothing arrives bare: "And when you cannot answer, tell it as a story about somebody else and find the moral.". A new technique is handed over with no reason or step, and the jump from chimpanzees to the reader's own regret is not bridged.
- R1.7 One story, told once: "Then one day Melvin makes the mistake that costs him. He reaches for a female who belongs to a male above him". A new scene is dropped in after the 10 years of hazing and 'He did nothing wrong', so the reader cannot tell when it happened or why the hazing began.
- R1.7 One story, told once: "it runs for 10 years, until the day they finally let him in.". The ending is announced early, before the story tells how he gets in.
- R1.7 One story, told once: "I have watched a load come off someone's chest for the first time in 20 years, in a single afternoon". A new unnamed mini story appears after the closing question, with no setup or arc.
- R1.12 Research backs, never interrupts: "In Kibale National Park, Uganda, a primatologist named Rachna Reddy spent years watching one thing". The study opens the piece and runs for many paragraphs with two findings, before his idea is stated, so the research carries the piece instead of backing it.
- R1.12 Research backs, never interrupts: "One honest note. Her research does not claim to measure regret as a feeling inside a chimpanzee.". This caveat marks what the study does not prove instead of what the frame did to him, and it makes the reader doubt the chimp story they just followed.
- R1.12 Research backs, never interrupts: "Then one day Melvin makes the mistake that costs him.". The dramatised, named chimp story goes well past the facts of the study, so the reader cannot tell what the researcher found and what was added.
- R1.13 Built details serve the reader: "He reaches for a female who belongs to a male above him, and the older males make sure he never forgets it.". This is a built, staged event that contradicts the line just before it ("He did nothing wrong"), is not in the expert layer's account of Reddy's findings, and exists only to set up the "do not reach above your standing" lesson, so the reader cannot tell what is science and what is invented.
- R1.14 No meta-narration: "Two lessons, 10 years apart. Most of us only ever learn the first one.". The writer explains the piece's own shape (two lessons, 10 years apart) instead of letting the story carry it.

## F8: Case Study Test round 1, passage 2: Aiman

- R1.5 Nothing arrives bare: "He tried out his opening line on his morning customers. Before December, he was confident.". Steps are missing between avoiding his own voice and being confident, so the reader has to guess how the change happened.
- R1.7 One story, told once: "Before December, he was confident.". The ending is announced with no steps carried forward, so the reader is not told how Aiman got from a deadline to confidence.
- R1.8 Stakes, not more story: "he came to me with a deadline: the December meeting, in his own voice.". The deadline is named but nothing shows what Aiman stands to lose if he misses it, so the beat has no stakes and the reader has no reason to care.
- R1.8 Stakes, not more story: "He tried out his opening line on his morning customers.". A weak beat is filled with an extra scene instead of a concrete risk, so the story moves but nothing is on the line.
- R1.9 Warm the water: "Before December, he was confident.". The reader gets no steps between trying one line on customers and being confident, so they must guess how he got there.
- R1.9 Warm the water: "for years he sent his assistant to present for him, even in his own boardroom". A cafe owner with a boardroom, and no reason given for sending an assistant, leaves the reader guessing the background.
- R1.9 Warm the water: "In late October, he came to me with a deadline: the December meeting, in his own voice.". It does not say what made him come now or what his own voice means, so a leap is left unserved.
- R1.15 Rhythm without choppiness: "Before December, he was confident.". A short closing sentence brings a new fact (his confidence) that no step in the story earned, so the reader has to guess how he got there.
- R1.20 AI tells: "He tried out his opening line on his morning customers. Before December, he was confident.". The whole case is a clipped summary that jumps from a trial run to 'confident' with no scene, line or step, so the reader has to take the result on trust.
