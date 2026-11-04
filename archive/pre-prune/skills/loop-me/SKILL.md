---
name: "loop-me"
description: "Grill Coach Gen to find the routines that repeat in his work and turn each into a workflow spec an agent can build. Use when he says loop me or wants to automate or delegate a recurring task."
---

# Loop me

Adapted from Matt Pocock's loop-me skill (github.com/mattpocock/skills, MIT licence).

Run a grilling session (the `grilling` skill: rounds, a recommended answer on every question) whose only output is **workflow specs**. Create, edit and retire specs as the answers settle things.

## The loop lens

A **loop** is something that repeats in his life or work: a weekly sprint call, every coaching session, every paid invoice, every new article. Seeing work as loops inside loops shows how predictable much of it is, and the predictable parts are the ones worth handing to an agent. Use the lens to find loops worth a spec, and suggest loops he has not noticed.

A **workflow** is the written spec of one loop. The loop is what happens each time the workflow runs.

## Words to use when they fit

Tools, not a checklist. A workflow needs no AI, no checkpoint and no schedule unless the grilling shows it does.

- **Trigger:** what starts each run. An **event** (a call ends in Fathom, an invoice is paid, an article is published) or a **schedule** (every Monday). Events are usually better.
- **Checkpoint:** a point where he checks or decides. Some workflows have none.
- **Push right:** move the checkpoint as late as it will go. Do all the work first, then ask him once, with everything ready.
- **Brief:** what a checkpoint shows him. A short, decision-ready summary (what was made, why, and a link to it), never the raw output. He reads a brief, not a draft. Example of his own rule: for Fathom mining, "just print in chat what you wrote and why".

## Before any new spec

Check what already exists so you never spec a loop twice: his installed skills (for example extract-fathom, coach-gen-billing, post-to-socials, coach-gen-writer), `Master_Project_Status.md`, and the existing workflow files. If a loop is already covered by a skill, the spec improves that skill instead.

## Where specs live

On his Mac: `/Users/coachwibawa/Documents/5 Laws of Lasting Change/Workflows/` (through the device bridge). Create it on first run.

- `Workflows/<name>.md`: one spec per workflow. This is the source of truth.
- `Workflows/NOTES.md`: raw notes on his world: the tools he uses (Notion, Fathom, Gmail, Drive, WhatsApp, his website), the channels he handles, and his own words for things. If it is empty or thin, interview him about his world before writing any spec. When a fuzzy word comes up, settle one name for it and record it here.

## Each spec covers

Trigger, inputs, the steps, every checkpoint and its brief, outputs and where they land, what must never happen (for example: never send a message, post or pay without his yes), and how to tell a run worked.

## Done

A spec is done when an agent could build it without asking a single question. Keep grilling until then. When a spec is done, say which form fits it best: a skill, a scheduled task, or a manual checklist.

## Style

Simple English. No em dashes. No reflective commentary.