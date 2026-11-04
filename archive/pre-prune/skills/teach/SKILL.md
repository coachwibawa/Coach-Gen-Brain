---
name: "teach"
description: "Teach Coach Gen a skill or topic over many sessions with short lessons, cheat sheets and a record of what he has learned, such as the ICF ACC exam. Use when he says teach me or wants to learn something."
---

# Teach

Adapted from Matt Pocock's teach skill (github.com/mattpocock/skills, MIT licence).

He wants to learn something over several sessions. Keep the state of his learning in files, so any thread can pick it up.

## The workspace

One folder per topic on his Mac: `/Users/coachwibawa/Documents/Learning/<Topic>/` (through the device bridge, `$HOME/mnt/Documents/Learning/<Topic>/`). Create it on the first run. If the Mac is not reachable, say so in one line and keep the files in the session until it is.

- `MISSION.md`: why he is learning this. Ground every lesson in it.
- `RESOURCES.md`: trusted sources for knowledge, and communities for practice.
- `GLOSSARY.md`: the topic's terms, once he can use them correctly.
- `learning-records/0001-<name>.md`: what he has truly learned. Used to pick the next lesson.
- `lessons/0001-<name>.html`: one short lesson per file.
- `reference/<name>.html`: cheat sheets that print well.
- `assets/`: a shared stylesheet and reusable quiz parts.
- `NOTES.md`: how he likes to be taught.

Read the whole folder before each session.

## The mission comes first

If `MISSION.md` is empty, ask him why he wants to learn this before teaching anything. Push for a concrete outcome ("pass the ACC exam this year and use the competencies in every session"), not "understand X". Write it in this shape, one screen at most:

```
# Mission: <Topic>
## Why
<1 to 3 sentences: what changes in his work or life>
## Success looks like
- <something he will be able to do, that someone could observe>
## Constraints
- <time, budget, other commitments, how he likes to learn>
## Out of scope
- <nearby topics he does not want to chase now>
```

Confirm with him before changing the mission. When it changes, add a learning record.

## Knowledge, skills, wisdom

- **Knowledge** comes from high-trust sources. Fill `RESOURCES.md` before teaching much. Never trust your own memory for facts: look them up and cite them. For the ACC exam, start from ICF's own published documents (the Core Competencies and the exam information).
- **Skills** come from practice with fast feedback: quizzes, short real-world tasks, practice on his own coaching.
- **Wisdom** comes from real people. Suggest a community where he can test the skill (a peer coaching group, his mentor coach). If he does not want one, note it in `RESOURCES.md` and stop suggesting.

Two kinds of strength. Feeling fluent in the moment is not the goal. Long-term memory is. Build it with recall from memory, spacing over days, and mixing related topics in practice.

## A lesson

One self-contained HTML file in `lessons/`, numbered in order. Each lesson:

- teaches one tightly scoped thing tied to the mission, just above what he already knows (check the learning records)
- is short and gives him one real win
- teaches only the knowledge the skill needs, then makes him practise it with feedback
- cites its claims with links, and names one best source to read or watch
- links to earlier lessons and the reference sheets
- reminds him he can ask you follow-up questions
- uses the shared stylesheet in `assets/` (build it in the first lesson) and reuses any quiz parts already there

Clean, readable layout. Simple English. No em dashes.

Quizzes: every answer option has the same number of words. Move the correct answer's position around. No clues in formatting or order.

After writing a lesson, send it to him with `SendUserFile` so he can open it.

## Reference sheets and glossary

After a lesson, put its core into a reference sheet: the compressed version he will come back to. Add a term to `GLOSSARY.md` only once he uses it correctly. One or two sentences per term. Pick one word per idea and list the others to avoid. Once a term is in the glossary, use it everywhere.

## Learning records

Write one (1 to 3 sentences, numbered in order) only when:

1. he showed real understanding of something non-trivial
2. he told you what he already knows (record how deep)
3. a wrong belief was corrected
4. the mission changed

Covering a topic is not learning. Wait for evidence. When a later record replaces an earlier one, mark the old one `Status: superseded by 000N`. Never delete.

## Languages

He learns Japanese and German through comprehensible input. For a language topic, follow his method: record it in `NOTES.md`, and use lessons for things like grammar points or nuance, never to replace his input routine.