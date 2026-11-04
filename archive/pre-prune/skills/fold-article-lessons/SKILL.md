---
name: "fold-article-lessons"
description: "Fold the lessons from an article's drafting cycle into the Language Rules and Book Rules after it publishes. Use when Coach Gen says learn from this cycle or fold the lessons."
---

# Fold article lessons

Run this after an article publishes, or whenever Coach Gen says "learn from this cycle" or "fold the lessons". The goal: turn what he said during the drafts into a few strong rules, worded so a future thread understands them without the article in front of it, placed in the right doc, and approved in one pass.

The two rule docs are protected: `Coach_Gen_Language_Rules.md` (project only, no Mac copy) and `claude/Coach_Gen_Book_Rules.md` (master on his Mac at `5 Laws of Lasting Change/Book/Coach_Gen_Book_Rules.md`). Read `claude/Coach_Gen_Protected_Docs.md` first. Nothing is written until he says go on the exact lines.

## 1. Gather everything he said in the cycle

- Every chat message about the piece, from the first draft to publish.
- Every comment in every draft Google Doc: Drive `read_file_content` with `includeComments: true`, one call per draft.
- His silent edits: diff each draft doc's text against the draft you sent, and the published text against the last draft.

For each note, write down what it was reacting to: the exact line, and which draft. A note without its context gets misread.

When his note quotes your own reply, find what in your reply he objected to before you decide what the lesson is. Twice in one cycle a quoted reply was misread, and rules were built on the misreading.

## 2. Sort the notes

- **Rule candidate:** he gave a reason, a complaint or a verdict, and it would change how a different piece on a different topic gets written.
- **His explicit rule:** he said "rule", "general rule", "this can be a strong rule". Always a candidate.
- **Observation:** an edit with no reason, a word swap, a fix that only fits this article. Never a rule. List these in one line at the end.
- **Already covered:** an existing rule already says it. Not new. At most add the example under the old rule, and only if it makes the old rule clearer.
- **Rejected before:** anything he struck in an earlier round. Do not bring it back.

Overfitting test, for every candidate: would this rule still make sense, and still matter, for an article about something else entirely? If not, it is an observation. Fewer, stronger rules beat many small ones.

## 3. Word each rule

- **Title:** bold, plain, and says the principle. No clever names. "End a list of three on the callback", not a label only you understand.
- **Body:** 1 to 3 plain sentences that state the general principle. Never in the article's details (no berries, no named study, no "step 4").
- **His words:** quote only what makes sense on its own. If a quote needs the doc to be understood ("[]", "this", "step 4"), cut that part with "..." or give the context in plain words first. A quote out of context confuses every future reader of the rule.
- **Example:** add one only if it makes the rule clearer without the article.
- **Mechanics:** no em dashes, no semicolons, British spelling, Oxford comma. Date it ("Annotated 16 Oct 2026" or "(Added 16 Oct 2026.)").

## 4. Place each rule

- **Language Rules:** his voice, word choice, tone, how he talks to the reader, and article conventions (tag `[article]` when it only applies to articles). Pick the section by topic.
- **Book Rules:** how sentences, paragraphs, arguments and stories are built. New rules get the next R number.
- **Group related rules** under one heading instead of scattering them (for example, a "Scientific explanations" heading holding three rules).
- **Correcting or extending an old rule:** annotate under it and keep the old line. Both docs are add and annotate, never condense.
- **Anchor:** name the exact existing line each addition goes after.

## 5. Show it once

One message:

1. Every proposed addition in its full final wording, each with doc, section, and the exact line it goes after.
2. One line of observations, with no rules attached.
3. "Go?"

Never summarise instead of showing the text. "Wording stays the same" or "goes in section 3" without the lines is vague, and he has to ask twice. If he corrects some items, show only the changed lines again, then ask once more.

## 6. Write, on his go

Write exactly the approved text. Nothing else in either doc changes.

**Book Rules:**
1. Back up the Mac master to `$HOME` with a dated name.
2. Insert by Python at the anchor, then assert the diff against the backup is insertions only, and that the added text has no em dash or semicolon.
3. Check the blank lines around each insertion.
4. `device_stage_files` the master, copy it to `/home/claude/upload/claude/Coach_Gen_Book_Rules.md`, and `project_write` with `local_path`.

**Language Rules:**
1. Fresh `project_read`.
2. Take the content bytes by script from that tool result in the session transcript (`/root/.claude/projects/-home-claude/<session>.jsonl`). Never retype the doc.
3. Insert by script at each anchor, assert insertions only and no em dash or semicolon in the added text.
4. `project_write` with `local_path`.

Then report in a short list: which lines went into which doc and section.

## 7. Process lessons and memory

- Lessons about how to run the drafts (not about the writing itself) go into the `coach-gen-writer` skill: propose the complete updated SKILL.md with `propose_skills`.
- Save his stated preferences from the cycle to project memory.

## What went wrong before (16 Oct 2026, Law 1 Part 2)

- A quoted reply was misread twice, and rules were built on the misreadings.
- Simple edits were turned into rules. He called it overfitting.
- Rules were worded in the article's details, so they read awkwardly.
- Related rules were scattered instead of grouped.
- Placements were given without the text, which was vague.
- His words were quoted out of context.
- It took five rounds to land nine lines. Following this skill, it should take one, or two at most.