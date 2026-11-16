# Step 20, the blind A/B: log (16 Nov 2026)

## Setup

1. The piece: one section of Chapter 5 (Law 3), the pruning section, from his own pruning story. Claude's call. Reason: no test case and no calibration note comes from Law 3, and the earlier A/B rounds all used the Law 2 brake pile.
2. The material: `material.md`, 8 gold entries (406, 549, 580, 622, 548, 120, 121, 122). Each entry's md5 equals the brain's (`material_parts/`). Entry 406 is cut where a pasted article on another subject begins inside it.
3. Old stack (folder `/tmp/ab20/a7k`): the skill from `archive/pre-prune/skills/coach-gen-writer/` (6,369 words), the Language Rules, the Book Rules, Protected Docs, Guardrails, both Findings files, the Taste Test Passages, the calibration log, the Book Writing Handoff, Book Map Continuity and the Brain Rule, all from `archive/pre-prune/`. No lint, no checkers.
4. New stack (folder `/tmp/ab20/q3m`): `skills/coach-gen-writer/SKILL.md`, the chapter, case study and key moments cards (md5 equal to `brain.card_text`), `tools/cg_lint.py`, the same Findings, Taste Test and calibration log files, the Brain Rule. The checkers run after its reply, by Sonnet helpers started from the main chat. Fails go back to the same writer once.
5. Both prompts are the same but for one block and the folder name: `prompt_old.txt`, `prompt_new.txt`. Both writers: Opus, high effort, each a fresh agent in its own folder, not told the other exists. The main chat writes and edits neither draft.
6. Same test conditions for both: only the material file, no questions, no key moments stop, no doc build, the blank as the first line of the notes.
7. His Mac is not reachable from this chat (no folder connected, and the tool that asks for one is gone). So the whole record is here in the repo, not in `Book/Research/ab_tests/`.

## Incidents

1. The first launch of the old-stack writer carried a stray first line that named this run folder and the file name `prompt_old.txt`. It was stopped within a minute, before it wrote anything (its scratch folder was empty), and launched again with the exact prompt. The new-stack writer was not touched.
2. The new-stack writer's first draft failed 4 checkers (R1.4, R1.5, R1.9, R1.17): `check1/D1/`. Fix round 1 cleared three, R1.4 still failed (`check2/`). Fix round 2 cleared R1.4, held twice (`check3/R1.4.json`, `R1.4_b.json`). Per the skill only the failed checkers were rerun, not all 20.
3. The old-stack draft passed all 20 checkers in one run (`check1/D2/`). It got no checker feedback, because the old skill has no checker step.
4. The Google Doc create call was stopped by him mid-run (19:24), to switch the model. It had already run. The doc was read back whole and checked: complete, nothing missing.

## Results so far

| Stack | Writer rounds | Lint | Checkers | Words |
| --- | --- | --- | --- | --- |
| old | 1 (5 passes) | clean | 20 of 20 pass | 723 |
| new | 3 (5 passes) | clean | 20 of 20 pass after 2 fix rounds | 664 |

Drafts: `final_old.md`, `final_new.md`. Checker folders: `check1` (D1 new first draft, D2 old), `check2` (D3 new after fix 1), `check3` (D4 new after fix 2).

## Cost, as the Agent tool reports it (memory size at the last step, not the total)

- Old writer: 256,581 tokens, 33 tool calls, 9.3 min. Its first launch was stopped at once.
- New writer: 198,761 (8.6 min), then 207,877 (fix 1, 1.4 min), then 211,790 (fix 2, 2.5 min).
- Checkers, Sonnet: 20 runs at about 92,000, then 4 and 2 more at about 91,000. 26 runs, about 2.4 million.

## The blind doc

- Google Doc "Step 20 Blind A/B, Law 3 Pruning (Drafts X and Y)", id `1vM7UWV7ASuWrBG2KYxKGNpmz5_qjkWEgkLmd8BuRw-A`, built from `blind_doc.html`.
- X and Y set by `secrets.randbelow(2)`. The key is in `sealed/key.json` (sha256 starts `fe3e5407caa6ebac`). Do not open it, and do not show it to him, until he has scored both.

## His scores

Logged at 19:40 (16 Nov), before the key was opened. His words, as typed.

- In chat: "marked. I am not sure though, just a hunch that B is better but I can't pinpoint". B is the second draft, so Y.
- On X (comment on its last word): "feels ok. a good article and a good read. but since it's isolated by nature, this doesn't feel like it was taken from a book chapter (which is not a negative thing per se)."
- On Y (comment on its last word): "I think after reading both, I like the second one better. it is more book-y, like reading a penguin self help book. even though it both shares flaws due to the material and some approaches I no longer agree with, I like B better. but I still can't say for sure."
- No numbers. His call: Y over X, low confidence.

## The key (opened 19:41, after his verdict was logged)

X = old | Y = new. He preferred the new stack: the new skill, the card, the lint and the checkers.
