---
name: "handoff"
description: "Write a handoff note so a new chat can pick up this work, saved to the project with the skills the next chat should use. Use when Coach Gen asks for a handoff or says he will continue this in another chat."
---

# Handoff

Adapted from Matt Pocock's handoff skill (github.com/mattpocock/skills, MIT licence).

Write a note that lets a fresh chat continue this work with no other context. If he named what the next chat is for, shape the note around that.

## Where it goes

The project, so any chat finds it: `claude/<Topic>_Handoff.md` (for example `claude/Company_Docs_and_Tax_Handoff.md`, `claude/Book_Writing_Handoff.md`). Write it locally first, then `project_write` with `local_path`.

If a handoff for this topic already exists, read it first. Update its status lines and add a dated section for what changed. Never condense or drop earlier content. Handoff docs are working docs: add and annotate only.

## What it holds

1. **Start here:** one line on what the next chat is for.
2. **Where things live:** links and paths (Drive folder ids, Mac paths, Notion pages, project docs). Point to them. Never copy content that already lives in a doc, spec, log or file.
3. **Done:** short list.
4. **In progress:** the exact state, including anything waiting on him.
5. **Next, in order:** numbered steps.
6. **Rules for this work:** only the ones specific to it (for example "never type passwords for him", "tax-facing text in Indonesian").
7. **Suggested skills:** which installed skills the next chat should call, and when.

## Never include

Passwords, passphrases, API keys, ID numbers, bank account numbers, or private details about his clients beyond what the project docs already hold.

## Finish

Reply with one line naming the doc, plus the exact sentence he can paste to open the next chat (for example: "Read claude/Company_Docs_and_Tax_Handoff.md and continue from Next, step 1."). No em dashes.