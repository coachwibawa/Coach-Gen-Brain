# The linter and the test set (step 11)

`tools/cg_lint.py` is the mechanical half of the checks. `python3 tests/rules/run_lint_on_testset.py` runs it on every case in `test_set.json` and on `lint_bad_sample.txt`. Add `--verbose` to see the Tier 2 notes.

## What it checks

- **FAIL (Tier 0):** em dash (and a spaced hyphen or en dash standing in for one), semicolon, emoji, "my clients", the business "we" (our team, we offer, at Coach Gen and similar), a locked name or locked line not spelled exactly, a malformed [MATERIAL NEEDED], and, with `--keep`, a phrase he typed that is missing, changed or turned into a heading.
- **FORM (from the output's card):** article header lines, order and the "Coach Gen" sign-off. Letter name "Lasting Change Letters #N". Chapter figure labels (Figure 3.1).
- **NOTE (Tier 2, never fails):** American spelling, a missing Oxford comma, small counts written as digits, "everyday" as an adverb.
- **Reported only:** word count, sentence count, reading grade.

Not checked here: print names against `brain.personas` (needs the brain), bare "Lasting Change" (also ordinary English), the shared human "we". Everything about quality, joins, invented facts and quotes is left to the one-rule checkers (step 12). A clean lint is not a pass.

## Result on the test set (6 Nov 2026)

- All 9 approved passages (P2 to P10) come out with no FAIL or FORM.
- F6 is flagged (three em dashes, and the Insight headings are not the exact header lines).
- F7 is flagged: all three failed renderings of his typed phrase. The approved rendering is clean.
- F1, F2, F3 and F8 are quality failures with no mechanical break. The lint stays clean on them, as it should. They are for step 12 and step 13.
- A deliberately broken sample trips every check.

## Open question for him

The letter card says "Everything on the article card", which includes the three Insight header lines. His approved letter (P2, the Never Split The Difference letter, 90%) has one field, no Insight headers, and ends with "Coach Gen" and a question. So for letters the lint reports the missing headers as a note, not a break. If letters should carry the three headers, the card line stays and the lint turns that note into a break. If they should not, the letter card line needs rewording in a later pass.
