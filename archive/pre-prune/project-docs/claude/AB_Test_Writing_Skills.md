# A/B Test: Writing Skills (current vs. mixed)

Set up 2026-10-19. Run this in the writing thread. Coach Gen's call: test "current" against "mixed" only. A version built entirely on the new method, or entirely new with his writing only as context, is out.

## The two versions

- **A, current:** the `inside-the-introvert` skill exactly as it is.
- **B, mixed:** the same skill, the same rule docs and the same material, plus these two steps (adapted from Matt Pocock's writing-fragments, writing-shape and writing-beats skills, github.com/mattpocock/skills, MIT licence):
  1. **Leading word.** After settling the blank and before drafting, find or coin the one term the piece hangs on (the way "Momentum Engine" carries Law 4). Prefer a word from his own material. Build the piece's transitions and closing around it.
  2. **Grounding check.** Before drafting, list the ideas the reader already brings (a reader with English as a second language who has not read his other pieces). While drafting and again in the review pass, check every paragraph leans only on ideas the reader brought or met earlier in the piece. If a paragraph needs an idea not yet grounded, ground it first or cut the move.
- **Left out of round 1:** the fragments interview. It changes the input, not the method, so both versions must start from the same pile. It can be its own test later.

## How to run a round

1. Coach Gen gives one piece of raw material. Save it word for word to one file.
2. Launch two agents at the same time with the Agent tool. Each starts with no memory of the chat. Both prompts are identical except for one block:
   - Both: "Run the inside-the-introvert skill on the material in <file>. Read the rule docs it names. Return Insight 1, 2 and 3 as plain text, plus the built-detail list. Do not publish."
   - B only: add the two steps above, word for word.
   - Do not pass either agent any earlier draft, comment or note from this chat.
3. The main thread writes neither draft and does not edit either one.
4. Label the drafts X and Y in random order (flip a coin by script) and record the key in this file.
5. Show both to Coach Gen. He scores each "x% as a book" and comments as usual. Reveal the key only after he has scored both.
6. Log the round below. Do not fold anything into a skill until at least 2 rounds are in, ideally 3, on different material.

**Annotated after round 1 (19 Oct 2026):**
- **Chronicle.** Each round keeps its full record on his Mac, in `Book/Research/ab_tests/roundN/`: the material, both exact prompts, both full outputs (process notes included), the blind doc source, a log (setup, raw results, incidents, his scores) and the key. His words: "make sure to chronicle these tests so I can assess the ab test fully."
- **The key.** Step 4 says record the key in this file. Round 1 keeps it sealed in `key.json` on the Mac until he has scored both, so it cannot be seen by accident here. It goes into the table below once he has scored.
- **The input.** Round 1 gave both writers a curated pile copied word for word from the worksheet, at his go, so the method is the only thing that differs. Both prompts also carried the same test conditions (use only the material file, no questions, the blank as the first line, stop after the skill's step 6, no writes).
- **Scratch folders.** In round 1 both writers shared one scratch folder, and writer A read writer B's draft when B's file overwrote A's. From round 2, each prompt names a scratch folder of its own.

**Annotated before round 2 (20 Oct 2026):**
- **A new pair.** After the redo, his call widened the test: "Let's do another ab test. but now, the mixed vs a total pocock." His answers: "Pocock on autopilot" and "can we redo foot on brake. same input and all?" This newer call replaces the line at the top that put an all-new-method version out of the test.
- **M, mixed:** version B above, the redo's prompt word for word, with only its paths changed.
- **P, Pocock on autopilot:** Matt Pocock's writing-shape and writing-beats method, with the writer making every choice the method hands to the user (openings, each next beat) and logging why. No inside-the-introvert skill, no Language Rules, no Book Rules. Only the mechanical house rules (no em dashes, no semicolons, digits, British spelling, no emojis, never "my clients", David and Melina, no invented biography) and the Insight 1, 2 and 3 format. Exact prompt: `round2/prompt_P.txt`.
- **Limit: a described method.** Pocock's SKILL.md files could not be fetched word for word (GitHub is blocked for Claude's fetch tool). P ran on the method as its public pages describe it. If he pastes the files, a later round can run the exact text.
- **Limit: the project block.** Every agent launched in this project receives the project instructions (Core philosophy, content formats, Strunk and White style rules) and his saved preferences. So P was Pocock's method plus that short block, not voice-free. The redo writers had the same block.

## Rounds

| Round | Date | Material | X was | Y was | Score X | Score Y | His notes |
|---|---|---|---|---|---|---|---|
| 1 | 2026-10-19 | Law 2, the brakes (curated pile, `round1/material.md`). Blind doc: "A/B Test Round 1, Law 2 Brakes (Drafts X and Y)" | sealed (`round1/key.json`) | sealed | pending | pending | pending |
| 1 redo | 2026-10-20 | The same pile (`round1b/material.md`), each writer in its own scratch folder. Blind doc: "A/B Test Round 1 Redo, Law 2 Brakes (Drafts X and Y)" | B (mixed) | A (current) | about 8.1 (sections: 10, 6, 8) | about 4.3 (sections: 4, 5, 4) | Scored by section. X opening "10/10". X David's session "6/10. the quoted words are discombobulated. yes, they are verbatim. but as I mentioned, readers have no context and are expecting full sentences." X turn to the reader "8/10. it's digestible. but not wow like reading dweck or the opening of this passage". X Insight 2 "actually like this approach to insight 2. even though this barely matters for the current goal (book worthy writing)". Y opening "mediocre, flow feels choppy. storytelling worse. 4/10". Y David's session "conversation is hard to follow. 5/10". Y turn to the reader "feels lectury, not as impactful. 4/10". Totals are word-weighted averages of his section scores, by Claude. Full log: `round1b/log.md`. |
| 2 | 2026-10-20 | The same pile (`round2/material.md`). M (mixed) vs P (Pocock on autopilot). Blind doc: "A/B Test Round 2, Law 2 Brakes (Drafts X and Y)" | P (Pocock on autopilot) | M (mixed) | about 5.9 (sections: 7.5, 4, ending not scored) | about 7.3 (sections: 8, David's session not scored, 7) | Scored by section. X opening "conversation still awkward. but the flow of ideas is surprisingly reasonable. 7.5/10". X explanation "explanation feels like scattered thoughts. feels like repeating points even though nothing is repeated. 4/10". X ending "conclusion feels weak, and not how I would love it. david concluding himself, without any help from the writer to make a better payoff feel empty." Y opening "cool opening, segwayed well into david. 8/10". Y David's session "idk, feel mediocre." Y turn to the reader and ending "feels lectury, but does get the point across and serves its purpose. 7/10". Totals are word-weighted averages of the scored sections only, by Claude. Both unscored sections drew negative comments, so both true totals are likely a little lower. Full log: `round2/log.md`. |

Round 1 (19 Oct) is void: writer A's transcript shows it read a scratch file writer B had just written. It is not scored. The 35 shared phrases first shown as evidence are not proof: the two isolated writers of the redo share 62. Details in `round1/log.md` and `round1b/log.md`.

## Decision rule

Whichever wins gets folded into `inside-the-introvert` (and `write-book-from-material` if it helps there too). If B wins on only one of the two steps, fold in only that step. Rules that come out of the test go to the Book Rules, which are protected: show him the exact lines and wait for his go.

**Annotated after round 2 (20 Oct 2026):** his call: "I am confident enough that mix is the choice here." This newer call settles the winner after 2 rounds, both on the brake material, where step 6 would ideally want a third round on different material. Nothing is folded into a skill yet: that waits for his go, as above.

Cost per writer run, as the Agent tool reports it (tokens, time): round 1 void, A 177,472 and 9.4 min, B 197,609 and 11.9 min. Redo, current 191,837 and 10.8 min, mixed 190,139 and 11.3 min. Round 2, mixed 192,798 and 11.7 min, Pocock on autopilot 151,498 and 11.1 min. The two mixed steps add no measurable cost. Most of each run goes on reading the skill and the 3 rule docs, which Pocock on autopilot did not read.

**Correction (20 Oct 2026):** the token numbers in the line above are each writer's memory size at its last step, as the Agent tool reports it. They are not the total. Every step re-reads the writer's whole memory, mostly at the cheaper repeat-read rate. Total read per run, from the writers' own logs: round 1 void, A 1.85 million (13 steps), B 2.15 million (14 steps). Redo, current 2.63 million (17 steps), mixed 1.75 million (12 steps). Round 2, mixed 2.28 million (15 steps), Pocock on autopilot 5.34 million (52 steps). So Pocock on autopilot cost the most, because it wrote one beat per step. The skill and the 3 rule docs are about 32,000 tokens, read once per run, a small share of the total. The aborted first launch of round 2 used 0.24 million (M) and 0.19 million (P) before the limit stopped it. Mixed and current stay level with each other.

**Annotated 20 Oct 2026, the fold:** at his go ("blocked is to yes mixed steps and everything from 2 turns ago"), the leading word and the grounding check went into a new merged skill, `coach-gen-writer`, as steps 4 and 5, word for word from section "The two versions" above. Proposed to him on a review card. It replaces `inside-the-introvert`, `lasting-change-letters` and `write-book-from-material` once he saves it.
