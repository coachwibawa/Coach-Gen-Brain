# Checker calibration, step 13 (11 Nov 2026)

Result: all 5 fail cases fail and all 9 approved passages pass, between the lint and the 20 one-rule checkers. F7 (his typed phrase) is caught by the lint and is not a checker case.

How it ran: Sonnet helpers, one per rule, each judging all 14 drafts (`cg_check.py batch`). Round 1 (6 Nov): every fail caught, 7 approved passages falsely failed. Round 2 (6 Nov): calibration notes, card context and excerpt framing added, 2 false fails left and F3 missed (it had wrongly been framed as an excerpt). Round 3 (11 Nov): notes added to R1.2, R1.5 and R1.13, F3 framed as the chapter opening it is, and the 5 changed checkers rerun (R1.1, R1.2, R1.5, R1.11, R1.13). The other 15 answers are from round 2.

Thin margins to watch: F1 is caught by one checker (R1.16, on a weaker reason than his own: R1.5 caught it in round 2 but not after its round 3 note) and F3 by one (R1.11). A fresh full run should confirm the result holds before daily use leans on it. A fresh full run should confirm the result holds.

| Case | What it is | Expected | Got | Caught by |
| --- | --- | --- | --- | --- |
| F1 | Taste test round 3, passage 1: "Why Pushing Harder Fails", p | fail | fail | R1.16 Parallels that truly match |
| F2 | Taste test round 3, passages 2 and 3: Melina, with invented  | fail | fail | R1.6 Images from the reader's life, R1.7 One story, told once |
| F3 | Chapter 3 (Law 1) epoch 4: the ditch paragraph, with the par | fail | fail | R1.11 Bring it to the reader's life |
| F6 | Law 2 chimpanzee piece, v7 | fail | fail | lint, R1.1 One thread, R1.2 Joins answer the reader's question, R1.3 Links are real, R1.5 Nothing arrives bare, R1.7 One story, told once, R1.8 Stakes, not more story, R1.9 Warm the water, R1.12 Research backs, never interrupts, R1.13 Built details serve the reader, R1.14 No meta-narration |
| F8 | Case Study Test round 1, passage 2: Aiman | fail | fail | R1.5 Nothing arrives bare, R1.8 Stakes, not more story, R1.9 Warm the water |
| P2 | Lasting Change Letters #1: Never Split The Difference (full, | pass | pass | - |
| P3 | Introduction, as merged into the master draft | pass | pass | - |
| P4 | Chapter 1, "Staying Who You Are", as merged into the master  | pass | pass | - |
| P5 | Article: "3 Stages of Consistency" (published) | pass | pass | - |
| P6 | Article: "How can you be busy but lazy?" (published) | pass | pass | - |
| P7 | Chapter 3 epoch 4: the parent paragraph | pass | pass | - |
| P8 | Chapter 3 epoch 4: the reader's-week paragraph | pass | pass | - |
| P9 | Chapter 3 epoch 5: David's points system, your rewrite | pass | pass | - |
| P10 | Case Study Test round 1, passage 6: your door-to-door story | pass | pass | - |

## F1: Taste test round 3, passage 1: "Why Pushing Harder Fails", patched rewrite

- R1.16 Parallels that truly match: "If the diet slips, make it stricter. If you miss a morning run, set 2 alarms.". The three parallel "if" lines switch subject from "the diet" to "you" and back to "the plan", so the list does not read as one matched set.

## F2: Taste test round 3, passages 2 and 3: Melina, with invented "health" and "nutritionist"

- R1.6 Images from the reader's life: "a plan so big it never left the page". A made-up metaphor the reader has to decode, instead of an image from their own life or Melina's words.
- R1.6 Images from the reader's life: "closes the case on her: if she just can’t, there is nothing left to try". A courtroom image (case, verdict, closes, opens again) sits in the same passage as the earlier page image, so the reader meets two image systems.
- R1.7 One story, told once: "Even her nutritionist once told her that if she were really consistent she would see results every week". Melina's story was already told whole, and this new scene arrives on a return trip after the break, so the reader gets a second telling with new pieces added.
- R1.7 One story, told once: "So what I realised is, that’s why I almost never finish anything.". The passage opens on Melina's realisation, the ending of her story, before the story earns it, then repeats it when it finally arrives.

## F3: Chapter 3 (Law 1) epoch 4: the ditch paragraph, with the paragraphs around it

- R1.11 Bring it to the reader's life: "He didn't need more options. He needed the focus to stick with what he picked.". The passage stays inside David's life and never shows how this reaches the reader's work, money, health or relationships, so the reader is left to guess how it applies to them.

## F6: Law 2 chimpanzee piece, v7

- lint, T0 no em dashes: em dash. Use a full stop, comma, colon or brackets
- lint, T0 no em dashes: em dash. Use a full stop, comma, colon or brackets
- lint, T0 no em dashes: em dash. Use a full stop, comma, colon or brackets
- R1.1 One thread: "Two lessons, 10 years apart. Most of us only ever learn the first one.". The piece sets up a second lesson (earning your way in through risk) and then never uses it, so the reader is left waiting for a payoff that does not come.
- R1.1 One thread: "Because it is not finished with you. It still has a lesson to teach, and you have not learned it yet.". The thread swaps from the chimpanzee's two lessons to regret as a messenger, so the reader no longer knows what the piece is about.
- R1.2 Joins answer the reader's question: "Then one day Melvin makes the mistake that costs him.". The story has already run to the day he is let in, so this jumps back in time with no link, and the reader cannot tell how it fits 'He did nothing wrong' or the 10 years.
- R1.2 Joins answer the reader's question: "So why does it still shout at you at 2am, 20 years later?". 'It' has no clear referent after the paragraph of three stories, so the reader has to guess what is shouting.
- R1.3 Links are real: "So why does it still shout at you at 2am, 20 years later?". "it" has no referent: the sentence before lists three painful memories, and the word "regret" only appears two sentences later, so the reader must guess what is shouting.
- R1.3 Links are real: "Then one day Melvin makes the mistake that costs him.". "Then" and "the mistake" contradict the earlier "He did nothing wrong" and the 10 years of hazing already told, so the reader cannot tell when this happens or why he is punished.
- R1.5 Nothing arrives bare: "Because it is not finished with you. It still has a lesson to teach, and you have not learned it yet.". The surprising claim that a old memory holds a lesson comes with no example or reason, and "it" has no clear referent, so the reader has to guess what is shouting.
- R1.5 Nothing arrives bare: "Then one day Melvin makes the mistake that costs him. He reaches for a female who belongs to a male above him". It contradicts the earlier "He did nothing wrong" and adds a new event with no step linking it to the hazing, so the reader loses the thread of the story.
- R1.7 One story, told once: "Reddy calls it close to hazing, and it runs for 10 years, until the day they finally let him in.". The ending of Melvin's arc is announced before the story gets there, and 'Then one day Melvin makes the mistake' is then told after the 10 years already ran, so the timeline is muddled.
- R1.7 One story, told once: "That is only half of what Reddy watched.". The chimp story is cut in two and the second half is added later, so the reader gets the arc in pieces rather than told forward once.
- R1.8 Stakes, not more story: "He reaches for a female who belongs to a male above him, and the older males make sure he never forgets it.". The danger is only claimed ("never forgets it") with no clause showing what is done to him, and the extra beat adds story while muddying the hazing timeline.
- R1.9 Warm the water: "So why does it still shout at you at 2am, 20 years later?". "It" and the regret it stands for were never introduced, so the reader cannot tell what is shouting or how the chimpanzee story led here.
- R1.9 Warm the water: "Because it is not finished with you. It still has a lesson to teach, and you have not learned it yet.". The jump from Melvin's two lessons to a person's old regret is asserted, not built, so the reader has to guess the link.
- R1.12 Research backs, never interrupts: "One honest note. Her research does not claim to measure regret as a feeling inside a chimpanzee.". A protective caveat about what the study does not prove, added for safety rather than for the reader, which the rule says to cut.
- R1.12 Research backs, never interrupts: "In Kibale National Park, Uganda, a primatologist named Rachna Reddy spent years watching one thing". The study opens Insight 1 and runs for many paragraphs with place and group detail, instead of his idea coming first and then 2 to 5 sentences of one finding.
- R1.13 Built details serve the reader: "Then one day Melvin makes the mistake that costs him. He reaches for a female who belongs to a male above him". This built scene contradicts the line just before it ("He did nothing wrong") and is not flagged as invented in Insight 2, so the reader is confused about what Reddy actually found.
- R1.14 No meta-narration: "Two lessons, 10 years apart. Most of us only ever learn the first one.". The writer stops the story to describe its own shape (two lessons, years apart) instead of letting the reader see it.
- R1.14 No meta-narration: "That is why there is a chimpanzee in my notes.". It explains the piece's own design and why the story was chosen, which pulls the reader out of the point.

## F8: Case Study Test round 1, passage 2: Aiman

- R1.5 Nothing arrives bare: "He tried out his opening line on his morning customers. Before December, he was confident.". The change from avoiding the stage to confidence is given with no steps between, so the reader must guess how a rehearsal produced it.
- R1.8 Stakes, not more story: "he came to me with a deadline: the December meeting, in his own voice.". The deadline is named but nothing shows what is at risk if he misses it, so the beat stays weak and the reader has no reason to feel the stakes.
- R1.9 Warm the water: "Before December, he was confident.". The reader gets no bridge from a customer trial to confidence, so the change is stated and not shown.
- R1.9 Warm the water: "he sent his assistant to present for him, even in his own boardroom". Why a cafe owner avoided speaking, and what the December meeting or his opening line was, is never given, so the reader must guess.
