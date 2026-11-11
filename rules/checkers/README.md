# The one-rule checkers (step 12)

One template per Tier 1 rule (`R1.1.md` to `R1.20.md`), built by `python3 tools/cg_check.py build` from `rules/table/rules_v3.json`, the same data as `brain.rules`. Each template carries its rule word for word. `checkers.json` lists each rule's md5. Rebuild after any rule change, never edit by hand.

Each checker reads the whole draft against its one rule and answers JSON: pass or fail, with up to three exact quotes and what the reader loses at each. A draft fails if the lint (`tools/cg_lint.py`) has a break or any checker fails. Tier 2 is never checked.

## Running

- With an API key: `cg_check.py prepare DRAFT --output chapter --dir RUN`, then `cg_check.py run RUN` (20 calls in parallel, Sonnet), then `cg_check.py collect RUN`.
- In a chat with no key: `prepare`, then one Sonnet helper per `RUN/R1.x.prompt.md`, each saving its JSON as `RUN/R1.x.json`, then `collect`.
- Many drafts at once (calibration): `cg_check.py batch MANIFEST --dir RUN` makes one prompt per rule carrying every draft, then `split RUN` and `collect RUN/<id>` per draft.

## Cost

In a chat, each helper carries about 74,000 tokens of overhead before it reads anything, so a single draft costs about 1.5 million tokens (20 helpers). Through the API the same check costs about 20 calls of 500 to 800 tokens plus the draft. For daily use an API key is the cheap route.

## Smoke test (6 Nov 2026)

F8 (Aiman, his "nothing after the first sentence make any sense"), on Sonnet: FAIL, 8 of 20 checkers fail (joins, nothing arrives bare, one story, stakes, warm the water, bring it to the reader's life, built details, AI tells). Every one names the bare ending or the missing bridges. Saved in `tests/rules/runs/smoke_F8/`.

## Calibration (step 13, 6 to 11 Nov 2026)

Done: all 5 fail cases fail and all 9 approved passages pass. Report: `tests/rules/runs/calibration_2026-11-11/REPORT.md`.
- `calibration.json` holds the notes each checker reads: how to read its rule, learned from his verdicts. Each note names the cases it came from. A note never changes a rule.
- Each prompt now carries the card for its output (context only) and says when a draft is an excerpt (`--output chapter-excerpt`).
- Thin margins: F1 is caught by one checker and F3 by one. Run a fresh full pass before daily use leans on it.
- Daily runs use Sonnet.
