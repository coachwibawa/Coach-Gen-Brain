---
name: "to-questionnaire"
description: "Turn a decision Coach Gen can't answer alone into a fill-in questionnaire for one expert, such as a lawyer, accountant, tax consultant or partner. Use when he needs answers from someone else."
---

# To questionnaire

Adapted from Matt Pocock's to-questionnaire skill (github.com/mattpocock/skills, MIT licence).

Turn something he cannot answer alone into a **questionnaire**: a document he hands to one person to fill in on their own time, or to go through together in a meeting. The other person knows what he does not. The questionnaire pulls it out of them.

**Ask him about the send, not the subject.** He can always answer who it goes to and what he needs back. The questions in the document then aim at the gap between what the recipient knows and what he needs.

## Steps

1. **Who is it going to?** In one message, ask the recipient's role, what they know that he does not, how he knows them, and the language (English or Indonesian). Before asking, check the project docs and memory: the answer may already be there (for example the coaching contract's open clauses, or the company docs handoff). Done when you know who they are and what they know.

2. **What does he need back?** In one message, ask which decisions or facts he must walk away with. Offer the list you already found in his docs as the starting point. Done when you have a concrete list.

3. **Write it.** Draft questions aimed at the gap, using the structure below. Done when every item from step 2 is covered by at least one question.

4. **Deliver it** as a Google Doc in his Drive (Drive `create_file` with HTML content, which converts to a Doc), so he can share one link and the recipient can type answers under each question. Put it in the matching Drive folder if one exists (for example the company documents folder for legal and tax). Reply with one line and the link.

## Language

- Anything going to a tax office, notary, lawyer or government body in Indonesia: write it in Indonesian, using the exact terms officials use (for example "SPT Tahunan", "NPWP badan", "KBLI").
- Otherwise use the language he named in step 1.
- Simple words. No em dashes, no semicolons.

## Structure

Put the most important questions first, because an async reply may only get one pass. Group questions under headings by theme once there are more than a handful.

```
# <Title>

**Purpose:** why this exists and the decision riding on it.
**From:** Genison Wibawa (Coach Gen). **To:** <recipient>. **How your answers will be used:** <where they go>

## Context
One short paragraph, enough for someone outside his head to answer well.

## How to answer
Deadline and rough effort. Partial answers and "I don't know" are useful. Flag anything you are unsure of rather than skipping it.

## <Theme>
### <One question, one idea, never two in one>
_Why this matters: <only where the question could be misread or invite a throwaway answer>_

Answer:

## Anything else?
Anything we did not ask that we should know?
```

Never put passwords, ID numbers or bank account numbers into the document.