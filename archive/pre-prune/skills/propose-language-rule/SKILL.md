---
name: "propose-language-rule"
description: "Propose additions to any of Coach Gen's rule docs (Language Rules, Book Rules, Content, Social Posting, style guides) from what worked and didn't in a drafting turn. Use for /propose-language-rule or \"make this a rule\"."
---

# Propose a language rule

His words (30 Oct 2026): "make this a skill /propose-language-rule. but by language rule I am referring to any rule doc that we improve by going through turns and seeing what did and didn't work."

Run this whenever a round of his feedback holds a lesson that should outlive the piece: after a markup round, before the next epoch, when he says "make this a rule", or when he types /propose-language-rule. It turns what he said into a few strong rules, placed in the right doc, shown once in full, and written only on his go.

`fold-article-lessons` is this same job run once at the end of an article cycle. This skill works at any turn, on any rule doc.

## 0. The rule docs

Read `claude/Coach_Gen_Protected_Docs.md` first. Then find the doc the lesson belongs to. Each doc carries its own maintenance rule at the top, and that rule governs the write.

| Doc | What it holds | Protection | Where the master lives |
|---|---|---|---|
| `Coach_Gen_Language_Rules.md` | His voice: words, tone, how he talks to the reader, article conventions | Read-only, write only on his named go | Project only |
| Book Rules (`claude/Coach_Gen_Book_Rules.md`) | Book craft: sentences, paragraphs, arguments, stories, chapter shape | Read-only, write only on his named go | His Mac, `Book/Coach_Gen_Book_Rules.md`. The project copy is a mirror |
| `claude/Coach_Gen_Social_Posting_Rules.md` | Packaging per platform | Append-only | Project |
| `claude/Coach_Gen_Content_Rules.md` | Short-form content from articles | Add and annotate | Project |
| Style guides (`claude/Reel_Style_Guide.md`, `brand/90_TASTE.md`, and any new one) | Video, brand taste | Follow the doc's own top rule | Project |
| A skill's SKILL.md | How a job is run, not how the writing reads | Changed only through `propose_skills` | Skill store |

A lesson about the writing goes in a rule doc. A lesson about the process (which step, which file, when to ask) goes in the skill that runs that process, through `propose_skills`, with the complete updated SKILL.md.

## 1. Gather what he said

- Every chat message since the last time rules were folded for this piece, word for word.
- Every comment in the latest draft Google Doc: Drive `read_file_content` with `includeComments: true`.
- His silent edits: diff the doc's text against what you delivered.
- What each note sits on: the exact line, and which draft. A note without its context gets misread. When his note quotes your reply, find what in your reply he objected to before you decide the lesson.

Log all of it word for word in the piece's markup log first (for a chapter, `Book/build/<chapter>/markup_log.md`), so nothing depends on the chat surviving.

## 2. Measure before you claim

When he asks "can you quantify this", or a rule will say what other authors do, measure it. Never claim from memory what the books do.

- His reference shelf is on his Mac as text: `Book/Research/reference_texts/` (atomic_habits, mindset, courage, elements, zinsser). Count with a short script in device_bash. Name the line numbers you looked at.
- Measure the draft the same way, so the rule can say "the books do X times, the draft did Y times".
- Say plainly when the books do something sometimes, not never.

## 3. Sort the notes

- **Rule candidate:** he gave a reason, a complaint or a verdict, and it would change how a different piece on a different topic gets written.
- **His explicit rule:** he said "rule", "make this a rule", "general rule". Always a candidate.
- **Praise with a reason:** "I like X" with the thing named. A candidate, worded as "a pattern to reach for" with the count of confirmed instances, not as a required shape.
- **Observation:** an edit with no reason, a word swap, a fact decision for one piece ("this money figure is approved"). Never a rule. It goes in the piece's fact sheet or markup log. List these in one line at the end.
- **Already covered:** an existing rule already says it. At most annotate the old rule with his new words or a clearer example.
- **Rejected before:** anything he struck in an earlier round. Do not bring it back.

Overfitting test for every candidate: would it still make sense, and still matter, for a different piece on a different topic? If not, it is an observation. Fewer, stronger rules beat many small ones.

## 4. Word each rule

- **Title:** bold, plain, says the principle. New rules in a numbered doc get the next number (the Book Rules run R1 upward).
- **Body:** the general principle in 1 to 3 short lines, not the piece's details.
- **Format:** a bold title, then short numbered lines, one idea per line, so he understands each line in one glance. Never a dense paragraph. The rule's own lines come first, then his words, then support. His words (30 Oct): "why does 7 and others not have things I can understand in one glance like 8. I would really prefer that". Then: "much better. keep this as rule."
- **His words:** quote what makes sense on its own, with the date and what it was about. Cut anything that needs the doc to understand ("this", "[]") or give the context first.
- **Cold-read test, for every quote of his:** read it as an AI that has never seen this chat. Could it be taken as a command he never gave, or as wider than he meant? Then either put the context in front of it in a few words ("on a draft where every heading was a question:") or cut it.
  1. His observation about how Claude writes is labelled as context, never worded as the rule. Example: "quality drops when quotes are involved" was a note on Claude's drafts, not a ban on quotes.
  2. A word he used loosely is pinned down. Example: he wrote "following chapter" and meant a later section of the same chapter.
  3. The rule's own lines must stand without the quote. The quote is evidence, not the instruction.
  His words (30 Oct): "I notice that you quote me in a rule that might or will be taken ooc by the ai reading this without context."
- **Things he offered to do himself:** word them as something to try, not something to leave to him. His words (30 Oct), on headings he reworks: "you can do yourself or try to; I just dont mind doing it myself".
- **His options:** when he offered several ways out and has not picked one, list them in his words and mark any default as your proposal, so he chooses.
- **Support:** the measurement from step 2, with line numbers.
- **Your diagnosis:** if the rule rests on your reading of why something failed, say so ("Claude's reading, to confirm on the next draft"). Annotate it as confirmed or wrong once he reacts.
- **Review pass:** if the doc has a checklist (the Book Rules section I, the Language Rules section 12), add one test line per new rule. The writer skills run only that checklist after drafting, so a rule with no line there never gets checked.
- **Mechanics:** no em dashes, no semicolons, British spelling, Oxford comma. Date every addition ("(Added 30 Oct 2026.)" or "Annotated 30 Oct 2026:").

## 5. Place each rule

- Pick the doc by what the rule governs (step 0), then the section by topic.
- A correction or extension of an old rule is an annotation under it. The old line stays. Every rule doc is add and annotate, never condense.
- Group related rules under one heading instead of scattering them.
- **Anchor:** name the exact existing line each addition goes after.

## 6. Show it once

One message:

1. Every proposed addition in its full final wording, in the glanceable format from step 4, each with its doc, section and anchor line.
2. The review-pass lines, if any.
3. One line of observations, with no rules attached.
4. "Go?"

Never summarise instead of showing the text. If he corrects some items, show only the changed ones again, then ask once more. Nothing is written until he says go on the exact lines.

## 7. Write, on his go

Write exactly the approved text. Nothing else in the doc changes. Never retype a doc.

**Book Rules (Mac master, then mirror):**
1. Back up the Mac master to `$HOME` with a dated name.
2. Insert by Python at each anchor. Assert the diff against the backup is insertions only, and the added text has no em dash or semicolon.
3. Check the blank lines around each insertion.
4. `device_stage_files` the master, copy it into the working directory, and `project_write` the mirror with `local_path`.
5. If the Mac is not reachable, wait. Never write the mirror alone.

**Language Rules, and any project-only doc:**
1. Fresh `project_read`.
2. Take the content bytes by script from that tool result in the session transcript (`/root/.claude/projects/-home-claude/<session>.jsonl`). Never retype the doc.
3. Insert by script at each anchor. Assert insertions only, and every old line still present.
4. `project_write` with `local_path`.

**Append-only docs:** the same as project-only, and corrections go in as CORRECTION lines under the old line.

Then report in a short list which lines went into which doc and section, and add one line to the piece's calibration log: rules folded, with their numbers.

## What went wrong before

- A quoted reply was misread twice, and rules were built on the misreadings (16 Oct).
- Simple edits were turned into rules. He called it overfitting.
- Rules were worded in the piece's details, so they read awkwardly later.
- Placements were given without the text, which was vague.
- His words were quoted out of context.
- Claims about what Clear and Dweck do were made from memory. Measure them.
- It took five rounds to land nine lines (16 Oct). Following this skill, it should take one, or two at most.
- Rules were shown as dense paragraphs he could not take in at a glance (30 Oct).
- Three quotes failed the cold-read test (30 Oct): an observation about Claude's quotes read as a ban on quotes, a question read without what it asked about, and "following chapter" meant a section.