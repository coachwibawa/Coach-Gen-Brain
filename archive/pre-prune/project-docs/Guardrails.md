# Guardrails

How Claude works inside this project. `Coach_Gen_Language_Rules.md` governs the writing. This governs the working.

---

## Check the protected list before any write

`claude/Coach_Gen_Protected_Docs.md` says which docs are read-only. Read it before calling `project_write` on anything here.

**On the list:** do not write. Not to fix a typo, not to reformat, not to make it comply with a rule it contains. If it should change, say so in chat, show the exact lines, and let Coach Gen decide. He can override in the moment, but he has to name the specific change in his own words that turn. "Update the language rules" is not enough.

**Not on the list:** normal edits. Condensing is allowed. Restructuring is allowed. Just read the current version first and never write from a stale read.

**Either way:** `project_write` replaces the whole file. There is no patch, no diff and no version history. A line dropped in transit is gone silently.

*Earned:* the voice-translation guide was rewritten 5 times in one session. The fifth condensed it and dropped the "courage to do the hard things" revision, the extended-metaphor rules, the structural voice patterns and most of the AI-slop explanations. They survived only because they happened to still be in that session's context.

## Never copy a file by re-typing it

To copy a file, move the bytes. `project_write` takes `local_path`. `device_stage_files` and `device_commit_files` move whole files. Reading a file into context and writing it out again produces a new file that resembles the old one, and the differences are exactly the small ones nobody checks.

*Earned:* `build_worksheet.js` was copied into the project on 2026-09-02 by re-typing. One argument, `italics: true`, went missing inside an otherwise perfect 44KB reproduction. The sibling script, uploaded as bytes, came through identical. The loss sat undetected for 12 days and surfaced only from a diff against the Mac.

## A project doc that also lives on his Mac is a mirror, not a master

Before answering "give me the latest X" for anything that also exists in a folder on his machine, list that folder and diff. If the Mac is not linked, say the project copy may be stale rather than calling it current.

*Earned:* asked for the latest build scripts, this session served the project copy as current. It was the wrong master, and nothing in the project said so.

## One artifact, one home

Code lives where it runs. Content lives where it is read. When the same file needs both, split it rather than mirroring it. A file kept in two places with no named master will drift, and the drift surfaces as a bug in something downstream, never as a conflict.

## Local by default, project by request

Scratch, logs, intermediate drafts, verification scripts, plans and measurements stay in the container. They cost nothing there.

The project gets finished deliverables, once, when he says it is finished. Anything in the project loads into every future thread, so a working file written there costs him twice: once in tokens, once in clutter when he is trying to think.

If something durable seems worth keeping, ask before writing it.

*Earned:* one session wrote tens of thousands of words of working material into project docs, most of it superseded within the hour.

## Verify, do not assert

Do not call a document clean, complete or correct until a script says so. Reading it back does not count.

*Earned:* a guardrail document that forbids em dashes and semicolons shipped with 24 em dashes and a semicolon in it. A coverage script caught them. A careful read had not.

Do not claim a protection exists until it has been tested. Read-only was assumed, then disproved by writing to the file.

## Read the whole source before choosing from it

A skim of one part is not a read.

*Earned:* for Lasting Change Letters #1, only the worksheet's tracker table was parsed. The 22 Sep live-session notes on the Law 3 page were missed, and two drafts were built on weaker material.

## Never delete a doc, flag it

Do not delete a project doc or empty one on your own judgment. Name what would go with it and let him decide.

## Read the guardrails first, then extend

Before starting work here, read `Coach_Gen_Language_Rules.md` and this file. Do not re-derive a rule that is already logged. Extend it, or correct it in place with the old line kept and the correction marked.

## Response shape

Answer the question asked, first, directly.

No reflective commentary at the end. No recap of what he just watched happen. When he asks for a thing, produce the thing, and keep the explanation to what he needs in order to judge it.

When he says do A, do A. Do not suggest B, do not skip A, do not redirect.

## Never without asking

- Publishing anything to Inside The Introvert
- Creating a new project doc
- Deleting a doc
- Writing to anything on the protected list
- Inventing a title, subtitle or citation
- Adding a fact under his name that he has not confirmed
