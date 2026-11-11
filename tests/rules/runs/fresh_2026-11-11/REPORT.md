# Fresh full checker pass (11 Nov 2026)

Result: all 5 fail cases fail and all 9 approved passages pass, between the lint and the 20 one-rule checkers, all from one fresh run. This confirms the step 13 result, which rested on a mixed run (5 checkers from round 3, 15 from round 2). F7 (his typed phrase) is caught by the lint and is not a checker case.

How it ran: Sonnet helpers, one per rule, each judging all 14 drafts (`cg_check.py batch`). Manifest: `manifest_in.json`, built from `test_set.json` (F1, F2, F3, P3 and P4 as `chapter`, P7, P8 and P9 as `chapter-excerpt`, F8 and P10 as `case-study`, the rest as their own kind).

One case flipped, and two notes fixed it:
1. First pass: 13 of 14. P6 (approved article) failed R1.19 Turns and endings, which wanted the way out spelled out after Insight 1's closing question.
2. Note added to R1.19, naming P6: the possibility can come in Insight 2, in the line that turns the story around. R1.19 rerun twice: P6 passed both times, but one rerun failed P10 (approved case study) for stopping at the low point.
3. Note added to R1.19, naming P10: a case study may stop at the low point, because the turn comes in the prose around it. R1.19 rerun twice: 14 of 14 both times.
R1.19 catches none of the fail cases, so neither note can let a failure through. The earlier R1.19 answers are kept in `r19_round2/`.

Thin margins, unchanged: F1 is caught by one checker (R1.16) and F3 by one (R1.11). Both held in this fresh run, by the same checkers as before. F2 and F8 each gained catchers.

Cost: 24 Sonnet helpers (20, then 4 for R1.19), about 86,000 to 94,000 tokens each, about 2.1 million tokens in all.

The last column shows who caught each case in the step 13 report.

Result: 14 of 14 cases as expected (5 fail cases, 9 approved passages).

| Case | What it is | Expected | Got | Caught by | Caught by, before |
| --- | --- | --- | --- | --- | --- |
| F1 | Taste test round 3, passage 1: "Why Pushing Harder Fails", p | fail | fail | R1.16 Parallels that truly match | R1.16 Parallels that truly match |
| F2 | Taste test round 3, passages 2 and 3: Melina, with invented  | fail | fail | R1.6 Images from the reader's life, R1.7 One story, told once, R1.10 A quote earns its marks, R1.11 Bring it to the reader's life | R1.6 Images from the reader's life, R1.7 One story, told once |
| F3 | Chapter 3 (Law 1) epoch 4: the ditch paragraph, with the par | fail | fail | R1.11 Bring it to the reader's life | R1.11 Bring it to the reader's life |
| F6 | Law 2 chimpanzee piece, v7 | fail | fail | lint, R1.1 One thread, R1.2 Joins answer the reader's question, R1.3 Links are real, R1.4 Few names, one each, R1.5 Nothing arrives bare, R1.7 One story, told once, R1.12 Research backs, never interrupts, R1.13 Built details serve the reader, R1.14 No meta-narration | lint, R1.1 One thread, R1.2 Joins answer the reader's question, R1.3 Links are real, R1.5 Nothing arrives bare, R1.7 One story, told once, R1.8 Stakes, not more story, R1.9 Warm the water, R1.12 Research backs, never interrupts, R1.13 Built details serve the reader, R1.14 No meta-narration |
| F8 | Case Study Test round 1, passage 2: Aiman | fail | fail | R1.5 Nothing arrives bare, R1.8 Stakes, not more story, R1.9 Warm the water, R1.13 Built details serve the reader, R1.15 Rhythm without choppiness | R1.5 Nothing arrives bare, R1.8 Stakes, not more story, R1.9 Warm the water |
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

- R1.16 Parallels that truly match: "If the diet slips, make it stricter. If you miss a morning run, set 2 alarms. If the plan falls apart in week 2". The subject flips between 'the diet', 'you' and 'the plan' inside one parallel run, so the three cases do not line up as a matching set.

## F2: Taste test round 3, passages 2 and 3: Melina, with invented "health" and "nutritionist"

- R1.6 Images from the reader's life: "with a plan so big it never left the page". A made-up metaphor the reader has to decode instead of a plain statement of what happened to her plans.
- R1.7 One story, told once: "For years, that sentence ended every attempt Melina made at getting healthier.". Melina's story was already told whole in the first half, and this section returns to it with new scenes instead of a callback, so the reader meets her story twice.
- R1.7 One story, told once: "Even her nutritionist once told her that if she were really consistent she would see results every week". This is a brand new scene added after the story was finished, which the reader never saw in the first telling.
- R1.10 A quote earns its marks: "So what I realised is, that's why I almost never finish anything.". Thinking out loud kept as said: the stumbling "So what I realised is" opener, and as the passage's first line "that's why" points to nothing, so the reader has to guess.
- R1.10 A quote earns its marks: ""That's always been my mindset," she said. "Can you picture it?"". "Can you picture it?" has nothing to picture and reads as a stray spoken fragment, so the reader has to guess what she means.
- R1.11 Bring it to the reader's life: "Melina saw through hers in 3 sessions. It took me years to see through mine.". The passage stays with Melina's health story and his own 20s, and never shows the reader how a verdict sentence like this shows up in the reader's own work, money, relationships or other areas.

## F3: Chapter 3 (Law 1) epoch 4: the ditch paragraph, with the paragraphs around it

- R1.11 Bring it to the reader's life: "He didn't need more options. He needed the focus to stick with what he picked.". The case ends inside David's business and projects, with no turn to the reader and no quick examples of where else the reader's own life works this way.

## F6: Law 2 chimpanzee piece, v7

- lint, T0 no em dashes: em dash. Use a full stop, comma, colon or brackets
- lint, T0 no em dashes: em dash. Use a full stop, comma, colon or brackets
- lint, T0 no em dashes: em dash. Use a full stop, comma, colon or brackets
- lint, article card headers: missing the header line "Insights from me, to you." on a line of its own
- lint, article card headers: missing the header line "Insights from other experts." on a line of its own
- lint, article card headers: missing the header line "Insight from within you." on a line of its own
- R1.1 One thread: "Two lessons, 10 years apart. Most of us only ever learn the first one.". The chimp story sets up two lessons (stay small, then take a risk to get in), but the piece drops the second and never turns it into anything the reader can use.
- R1.1 One thread: "Because it is not finished with you. It still has a lesson to teach, and you have not learned it yet.". The thread swerves from an old sentence written at 15 that still governs us to regret as a teacher, so the reader no longer knows which one the piece is about.
- R1.1 One thread: "Then one day Melvin makes the mistake that costs him.". This reopens a punishment the paragraph above already described and adds an event the piece never uses, so the reader has to guess how it fits.
- R1.2 Joins answer the reader's question: "Then one day Melvin makes the mistake that costs him.". The paragraph before said he did nothing wrong and was let in after 10 years, so this new mistake has no link and the reader has to guess how the story fits.
- R1.2 Joins answer the reader's question: "In humans, we sometimes make that mistake at 15.". The switch from chimpanzees to people has no bridge, and the reader cannot tell which mistake is meant or why the story turns here.
- R1.2 Joins answer the reader's question: "I have watched a load come off someone's chest for the first time in 20 years". This paragraph follows the closing question with no link to it, so the reader does not know why the piece goes back to a claim after asking.
- R1.3 Links are real: "So why does it still shout at you at 2am, 20 years later?". "it" has no clear referent (the three stories were listed, not a single thing), so the reader must guess what is shouting.
- R1.3 Links are real: "Then one day Melvin makes the mistake that costs him.". The text just said he did nothing wrong and the hazing began because he turned 10, so this "then" and "mistake" contradict the order and cause already given.
- R1.3 Links are real: "Because it is not finished with you. It still has a lesson to teach". "it" again floats free of any named noun until "Regret" appears a sentence later, so the reader has to recall and guess.
- R1.4 Few names, one each: "a primatologist named Rachna Reddy spent years watching one thing". A researcher who need not be kept is named in Insight 1, then repeated as 'Reddy calls it' and 'what Reddy watched', so the reader carries a name they did not need.
- R1.4 Few names, one each: "Call him Melvin.". An invented chimp name is added on top of the researcher, the park and the group, so the reader holds several names for a story they only need for its lesson.
- R1.5 Nothing arrives bare: "Because it is not finished with you. It still has a lesson to teach, and you have not learned it yet.". The reader is told that a memory that shouts at 2am holds an unlearned lesson, with no example or reason to accept it, so they must take it on faith.
- R1.5 Nothing arrives bare: "tell it as a story about somebody else and find the moral. That is why there is a chimpanzee in my notes.". The step from the chimp story to this technique is never explained, so the reader has to guess how a story about someone else unlocks the lesson.
- R1.5 Nothing arrives bare: "Two lessons, 10 years apart. Most of us only ever learn the first one.". The human second lesson is never stated, so the reader cannot see what the missing half is for people before the piece asks them to apply it.
- R1.7 One story, told once: "Reddy calls it close to hazing, and it runs for 10 years, until the day they finally let him in.". The ending of Melvin's arc is announced early, then the story is reopened later, so the timeline is not carried forward.
- R1.7 One story, told once: "Then one day Melvin makes the mistake that costs him.". A new scene is added to a story already told (he 'did nothing wrong'), so the reader has to guess how it fits the arc.
- R1.7 One story, told once: "That is only half of what Reddy watched.". This is a return trip to the chimp story to add new scenes after it seemed finished.
- R1.12 Research backs, never interrupts: "Her research does not claim to measure regret as a feeling inside a chimpanzee.". A protective caveat about what the study does not prove, which the rule bans, and it makes the reader doubt the piece's own frame.
- R1.12 Research backs, never interrupts: "That is only half of what Reddy watched.". The study runs across many paragraphs with two findings and comes before the idea, so the research leads instead of backing his point.
- R1.13 Built details serve the reader: "Then one day Melvin makes the mistake that costs him. He reaches for a female who belongs to a male above him". This built chimp event contradicts the line just before it ("He did nothing wrong"), is not in the expert note, and leaves the reader unsure what actually happened to the young male.
- R1.14 No meta-narration: "Two lessons, 10 years apart. Most of us only ever learn the first one.". The writer labels the shape of the story he just told instead of letting the reader see it, which is the exact meta-narration the rule bans.

## F8: Case Study Test round 1, passage 2: Aiman

- R1.5 Nothing arrives bare: "He tried out his opening line on his morning customers. Before December, he was confident.". The change from sending an assistant to being confident is given as an outcome with no steps between, so the reader has to guess how it happened.
- R1.8 Stakes, not more story: "he came to me with a deadline: the December meeting, in his own voice.". The deadline is the only pressure, and nothing shows what Aiman stands to lose if he misses it, so the reader cannot feel why the beat matters.
- R1.9 Warm the water: "Before December, he was confident.". The reader gets no step between the deadline and his confidence, so they must guess how he got from avoiding the boardroom to feeling ready.
- R1.13 Built details serve the reader: "He tried out his opening line on his morning customers.". A staged action built from nothing the person said, which proves the point and which the reader has to take on trust.
- R1.13 Built details serve the reader: "Before December, he was confident.". A feeling stated as fact with no words from Aiman to earn it, so the reader cannot trust the case.
- R1.15 Rhythm without choppiness: "Before December, he was confident.". A short closing sentence carries the whole outcome as a new fact, so the reader gets the result without the steps that led to it.
