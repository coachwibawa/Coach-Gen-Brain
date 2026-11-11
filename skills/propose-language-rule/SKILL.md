---
name: propose-language-rule
description: "Turn a lesson from Coach Gen's feedback into a rule: tested on his test set, shown once, stored in the rules table on his go. Use for /propose-language-rule, \"make this a rule\", \"fold the lessons\" or \"learn from this cycle\"."
---

# Propose a language rule

By "language rule" he means any rule that gets better by going through drafting turns and seeing what did and did not work (30 Oct 2026). Run this when a round of his feedback holds a lesson that should outlive the piece: after a markup round, before the next epoch, after a piece publishes ("fold the lessons", "learn from this cycle"), when he says "make this a rule", or for /propose-language-rule.

A lesson climbs six stages: **captured, judged, merged, gated, approved, stored.** It ends as a few strong lines in the right place, shown to him once in full, and stored only on his go.

## 0. Where rules live

- **The writing rules** (everything written in his voice: articles, letters, chapters, key moments, case studies) live in one table, `brain.rules`, in the Coach Gen Brain (Supabase, ref from `list_projects`). Tier 0 and Tier 1 fail a draft. Tier 2 is polish and never fails one. Five cards hold what belongs to one output. The card files in the project (`claude/cards/`) and on his Mac (`Book/Rule Cards/`) are compiled copies, never edited by hand.
- The old Language Rules and Book Rules are frozen history (repo `archive/pre-prune/`). Never add a rule there.
- **Other rule docs** (Social Posting Rules, Content Rules, Reel Style Guide, the `brand/` docs): section 9.
- **A lesson about process** (which step, which file, when to ask) is not a rule. It goes into the skill that runs that process, through `propose_skills`. How he wants Claude to work with him goes to project memory.
- **Tools:** clone `coachwibawa/Coach-Gen-Brain` with push access (add_repo). `tools/cg_fold.py` runs the file side. Read `rules/folds/README.md` before the first fold of a chat: it has every command and the spec format.

## 1. Capture

- Every chat message since rules were last folded for this piece, word for word.
- Every comment in the latest draft Google Doc: `read_file_content` with `includeComments: true`. After a publish, every draft of the cycle.
- His silent edits: diff the doc's text against what you delivered, and the published text against the last draft.
- What each note sits on: the exact line, and which draft. A note without its context gets misread. When his note quotes your reply, find what in your reply he objected to before you decide the lesson.
- Log all of it word for word in the piece's markup log first (for a chapter, `Book/build/<chapter>/markup_log.md`), so nothing depends on the chat surviving.

## 2. Judge

Sort every note:

- **Rule candidate:** he gave a reason, a complaint or a verdict, and it would change how a different piece on a different topic gets written.
- **His explicit rule:** he said "rule", "make this a rule", "general rule". Always a candidate.
- **Praise with a reason:** "I like X", with the thing named. A candidate, worded as a pattern to reach for (Tier 2), never a required shape.
- **Observation:** an edit with no reason, a word swap, a fact decided for one piece. Never a rule. What he typed is a keeper line for that piece, word for word. List the observations in one line at the end.
- **Declined before:** `select heading, body, retired_note from brain.rules where retired_note like 'Declined%';`. Never bring one back.

Three tests for every candidate:

- **Overfitting:** would it still make sense, and still matter, for a different piece on a different topic? If not, it is an observation. Fewer, stronger rules beat many small ones.
- **It rests on something he said.** Never on an edit he did not explain.
- **Measure before you claim.** When a rule says what good books do, or he asks "can you quantify this", count it in `Book/Research/reference_texts/` on his Mac (atomic_habits, mindset, courage, elements, zinsser) with a short script, and name the lines you looked at. Measure the draft the same way. Say plainly when the books do something sometimes, not never.

## 3. Merge before adding

Read the live rules: `select brain.rulebook_text();`. For each candidate, take the first that fits:

- **Already covered:** a live rule says it. No fold. If a draft broke that rule and its checker missed it, that is a calibration note (section 5), not a new rule.
- **A line in a live rule:** add, reword or remove a line there.
- **A line on a card:** when it holds for one output only.
- **A new rule:** only when no live rule can hold it.
- **A rule that should leave:** retire it, with the reason.

Place it by tier. Tier 0: a hard line never crossed in a delivered draft. Tier 1: craft whose break makes him fail a passage. Tier 2: polish he would edit and still pass (his words, 5 Nov: "some t2 edits, but pass t1 t0"). When unsure between 1 and 2, ask what he did with the passage: failed it, or fixed a line.

**A clash** with a live rule, or between his rule and the writing guides (The Elements of Style, On Writing Well): show both sides and let him decide, case by case. Never pick the winner for him.

## 4. Word it

- **Shape:** a rule gives a goal, a test to judge by, an allowed zone and hard lines ("A quote earns its marks" is the model). Never a freeze that protects words at the cost of the goal.
- **Lines:** short, one idea each, plain words, read in one glance. The general principle, never the piece's details.
- **Title:** plain, and it says the principle. No clever names.
- **His words never go in a rule line.** They go in the fold's `his_words`, each with its date and what it was said about.
- **Cold-read test, for every quote of his:** read it as an AI that has never seen this chat. Could it be taken as a command he never gave, or as wider than he meant? Then put the context in `about`, or cut the quote.
  - His remark about how Claude writes is context, never the rule. "Quality drops when quotes are involved" was a note on Claude's drafts, not a ban on quotes.
  - A word he used loosely is pinned down. He wrote "following chapter" and meant a later section.
  - The rule's lines stand without the quote.
- **Something he offered to do himself** is worded as something to try, not left to him.
- **His options:** when he gave several ways out and has not picked, list them in his words. No pick from Claude.
- **Your diagnosis:** when the rule rests on your reading of why something failed, say so in `diagnosis` ("Claude's reading, to confirm on the next draft").
- **Mechanics:** no em dashes, no semicolons, British spelling, Oxford comma.

## 5. Gate on the test set

A fold must leave every fail case failing and every approved passage passing (`tests/rules/test_set.json`, his verdicts).

1. Write the spec, one lesson per entry, then `python3 tools/cg_fold.py build SPEC.json`. Commit, push, and run `select * from brain.fold_load('rules/folds/<file>.json');` so the lesson is in the brain even if the chat ends here. (A chat that must stop before the wording is final builds with `"stage": "captured"`.)
2. `python3 tools/cg_fold.py gate FOLD --dir tests/rules/runs/<name>`. When the lesson came from a draft he failed, add `--origin DRAFT --origin-output chapter`: the changed rule must fail that draft.
3. One Sonnet helper per prompt the gate names, each saving its JSON answer where the gate says. Only the checkers the fold touches run, at about 90,000 tokens each in a chat. Add `--all` only when he says tokens are no concern.
4. `python3 tools/cg_fold.py result FOLD --dir <same>`. Show him the table it prints: each case, expected, got, caught by.
5. **If the gate fails:** the wording is wrong, or the checker misreads the rule. For a misread, add a note to `rules/checkers/calibration.json` that names the case and comes from his verdict on it, run `gate` again, and rerun that checker twice before calling it held. A note never changes rule text.
6. A Tier 2 rule or a card line reruns no checker. A Tier 0 rule the script can see needs `tools/cg_lint.py` changed to match first. Every gate runs the lint on the whole test set.
7. Commit, push, and run `brain.fold_load` again, so the table holds the gated text.

## 6. Show it once

One message he can take in at a glance: short numbered lines, never a dense paragraph. Each chat reply starts its numbers at 1.

1. Each lesson: the rule's name and tier, then its new or changed lines in full final wording. For a reworded line, the old line beside the new one.
2. The gate in one line: fails caught, approved passages kept, checkers rerun.
3. One line of observations, with no rules attached.
4. "Go?"

Never summarise instead of showing the text. If he corrects a line, edit the `spec` part of the fold file, run `build` on the fold file, gate again (answers to unchanged prompts are kept) and show only the changed lines. When he has many calls to make, use the decision-page skill.

## 7. Store, on his go

His "ok" or "fine" on the shown text is a go. Never ask twice. A no to one lesson: `python3 tools/cg_fold.py decline FOLD N --note "his words"`, then the `brain.fold_decline` line it prints.

1. `python3 tools/cg_fold.py approve FOLD`. Commit and push.
2. `select * from brain.fold_store('rules/folds/<file>.json');`. It returns six md5 values.
3. `python3 tools/cg_fold.py stored FOLD --md5 rulebook=… article=… letter=… chapter=… key_moments=… case_study=…`. It checks the repo against the brain, recompiles the five cards and rebuilds the checkers. If an md5 differs, stop and find out why before anything else.
4. Copy the five cards from `rules/table/cards/` to the project (`project_write` with `local_path`, `claude/cards/Card_*.md`) and to his Mac (`Book/Rule Cards/`). Mac not reachable: say so, and do it the next time it is.
5. Commit and push.
6. Report in a short list which lines went into which rule, and add one line to the piece's calibration log: rules folded, with their codes.

## 8. The fold check, at every handoff

`python3 tools/cg_fold.py status`, and `select code, heading, fold_stage from brain.rules where status = 'active' and fold_stage <> 'stored';`. Every rule he asked for in the chat is stored, waiting at a named stage, or declined. Name each open one in the handoff.

## 9. Other rule docs

For the Social Posting Rules, the Content Rules, the Reel Style Guide and the brand docs, sections 1, 2, 4 and 6 apply as written. There is no test set for them. Then:

- Read `claude/Coach_Gen_Protected_Docs.md` and the doc's own top rule. That rule governs the write. An append-only doc takes a CORRECTION line under the old line, never an edit.
- Name the exact existing line each addition goes after, and group related rules under one heading.
- Write only on his go on the exact lines, and never retype a doc. Take its bytes by script: from the file path a fresh `project_read` gives, or, when the read comes back as text, from the doc's last committed copy in the repo (`project-docs/`, else `archive/pre-prune/project-docs/`), checked against that read. Insert at each anchor by script, assert insertions only and every old line still present, `project_write` with `local_path`, and commit the new copy to `project-docs/`.
- Date every addition, for example "(Added 12 Nov 2026.)".

## What went wrong before

- A quoted reply was misread twice, and rules were built on the misreadings.
- Simple edits were turned into rules. He called it overfitting.
- Rules were worded in the piece's details, so they read awkwardly later.
- His words were quoted out of context, and three quotes failed the cold-read test.
- Claims about what Clear and Dweck do were made from memory.
- Placements were shown without the text, and rules as dense paragraphs he could not take in at a glance.
- It took five rounds to land nine lines. Following this skill, it should take one, or two at most.
- A freeze ("keep the record as said") protected words at the cost of the goal, and every quote read as broken.
