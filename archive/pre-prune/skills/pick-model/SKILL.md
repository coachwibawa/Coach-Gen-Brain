---
name: "pick-model"
description: "Recommend Opus, Sonnet or Haiku and an effort level for a Coach Gen task, with the reason. Use when he asks which model or effort to use for mining, writing, editing, admin or any job."
---

# Pick the model for a job

Coach Gen asks which model to use. Answer in the first line with one model name. Then give the reason in one to three short bullets. Plain, simple English. No em dashes, no semicolons.

You cannot switch the model yourself. Tell him which model to pick in the chat's model menu before he starts the job.

**Added 28 Oct 2026:** always give the effort level too. The first line is the model and the effort, for example "Opus, high effort." You cannot set the effort yourself either. Tell him to set it in the chat before he starts.

## The main rule

The more a job needs his judgment, his voice or his trust, the stronger the model.

- Anything that writes to the Coach Gen Brain lives there forever. The brain is add-only. A wrong tag, a reworded quote or a missed gold line costs more to find and fix later than a stronger model costs now. Lean stronger for these jobs.
- Anything printed in his voice (book, articles, letters, posts) is judged against his taste. Lean stronger.
- Jobs with one clear right answer, or that only follow fixed steps, can go to a cheaper model.

## By job

| Job | Model | Why |
|---|---|---|
| Mining his calls, monologues, voice dumps, client sessions | Opus | Picking gold, keeping words verbatim, tagging the Law, cutting private and junk sections. All judgment. |
| Mining an outside book, talk or post (tagged outside) | Opus | Still picking what fits the 5 Laws, and quotes must be exact. |
| Cleaning a PDF (page numbers, headers), splitting text, inserting rows he already approved | Sonnet | Mechanical steps with clear rules. |
| Loading a whole outside book PDF into the raw layer, no gold (parser, settings file, load) | Sonnet | Tested 31 Oct 2026: Sonnet built the parser and loaded The Courage to Be Disliked with no text lost and no flags. Opus only if the parser needs a new kind of rule. |
| Writing or redrafting the book, articles, Lasting Change Letters | Opus | His voice and taste. |
| Planning, specs, stress-testing a plan, brain or system design | Opus | Hard reasoning. A wrong plan wastes days. |
| Building from a plan he approved: code, migrations, skill files, scripts | Sonnet | Clear spec, checkable result. Move up to Opus if Sonnet fails twice. |
| Video edits in Concat from a clear plan | Sonnet | Following steps. |
| Social captions, short posts from material he already picked | Sonnet | Short, low risk. Use Opus if it must sound exactly like him. |
| Tax and company documents, invoices, kwitansi | Opus for anything sent to an authority, Sonnet for routine invoices and receipts | Mistakes with officials are costly. |
| Health checks, renaming files, simple lookups, scheduled routine checks | Haiku | One clear right answer. |
| Cleaning a call transcript of junk sections | Opus | Telling a Law 5 story from a shopping chat is judgment, not keyword matching. Never Haiku. |

When a job is not in the table, place it with the main rule.

## Effort level (added 28 Oct 2026)

Effort is how long the model thinks before it acts. The levels are low, medium, high, xhigh and max. More effort is slower and uses more tokens. It helps with hard reasoning: many steps, plans, catching its own mistakes. It does not give a weaker model better taste or a better feel for his voice. That comes from the model.

So pick the model by the kind of judgment the job needs. Pick the effort by how hard and how long the thinking is.

| Job | Effort | Why |
|---|---|---|
| Mining his calls, monologues, voice dumps, client sessions | high | Many small judgments in a row: what is gold, which Law, what to cut. |
| Mining an outside book, talk or post | high | Same judgments over a long text. Use medium for the storing step only, when no gold is picked. |
| Cleaning a PDF, splitting text, inserting approved rows | low | Fixed steps, done in code. |
| Loading a whole outside book PDF, no gold | medium | Writing the settings file and reading flagged pages need some judgment. |
| Writing or redrafting the book, articles, letters | high | Taste and structure. Use xhigh for a hard chapter or a full rewrite. |
| Planning, specs, stress-testing a plan, system design | xhigh | Many moving parts. Use max only for a big one-time decision that is hard to undo. |
| Building from an approved plan | medium | Clear spec. Use high for anything that changes the brain's search or rules. |
| Video edits in Concat from a clear plan | medium | Many steps, little judgment. |
| Social captions, short posts | low | Short. Use medium if it must sound exactly like him. |
| Tax and company documents for an authority | high | Exact words matter. Routine invoices and receipts: low. |
| Health checks, renaming, simple lookups | low | One right answer. |
| Cleaning a call transcript of junk sections | high | Section by section judgment. |

If the chat does not offer an effort setting for the chosen model, say "default effort".

**When a job goes wrong, which to raise first:**
- It made a reasoning mistake (missed a step, wrong logic, did not check its work): raise the effort first.
- It sounds wrong, has poor taste, or picks weak material: raise the model first.

## When unsure

If the choice is close and the job repeats often, offer one test. Run the same small piece (one call section, one page) on both models. Show him both results side by side. He picks. Record the result in this skill's table by adding a row, never removing one.

The same test works for effort: run one small piece at two effort levels and let him pick.

## Cost note

Mention cost only when it changes the answer. For example, a very long repeated job on Opus may be worth splitting: Opus for the judgment step, Sonnet for the mechanical steps.

Effort also costs. A long job at xhigh or max uses many more tokens than at high. Suggest xhigh or max only when a wrong answer would cost days or cannot be undone.