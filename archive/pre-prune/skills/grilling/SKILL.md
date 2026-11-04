---
name: "grilling"
description: "Grill Coach Gen relentlessly about a plan, decision or idea in rounds, each question with a recommended answer. Use when he says grill me or wants to stress-test his thinking."
---

# Grilling

Adapted from Matt Pocock's grilling skill (github.com/mattpocock/skills, MIT licence).

Interview him until you both share one understanding of the plan. Picture the plan as a tree: every decision branches into the decisions that hang off it.

## How a round works

Work the tree in rounds. The **frontier** is every decision whose earlier decisions are already settled: the questions you can ask now without guessing at answers you have not heard. Ask the whole frontier in one round. Number each question and give your recommended answer. Then wait.

Format each question like this. No emojis.

```
**Q1. <short title>**
<the question, with the options if there are any>

My pick: <your recommended answer, and the reason in one line>
```

Word each question so that "yes" accepts your pick. He answers fast with "yes", "no, X", or a number list.

After each round, recompute the frontier. Settled decisions unlock the ones that depended on them. A question that depends on another question still open in this round belongs to a later round.

## Facts are your job, decisions are his

Never ask him for a fact you can look up: his files on the Mac, the project docs, memory, Notion, Drive, the web. Look it up yourself, directly, in this conversation. Do not spin up fresh agents for lookups (they cost too many tokens). While a lookup runs, the questions that depend on it wait; ask the rest now.

Every decision goes to him. Never decide one silently.

## Done

The session is done when the frontier is empty: every branch visited, nothing silently assumed. Then give the settled plan in a short list and ask "Agreed?" Do not act on the plan until he confirms.

## Style

Simple English, short questions. No em dashes. No reflective commentary at the end.