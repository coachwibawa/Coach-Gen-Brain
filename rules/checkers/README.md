# The one-rule checkers (step 12)

One template per Tier 1 rule (`R1.1.md` to `R1.20.md`), built by `python3 tools/cg_check.py build` from the rules table data (`rules/table/rules_live.json` once a fold is stored, else `rules/table/rules_v3.json`), the same data as `brain.rules`. Each template carries its rule word for word. `checkers.json` lists each rule's md5. Rebuild after any rule change, never edit by hand.

Each checker reads the whole draft against its one rule and answers JSON: pass or fail, with up to three exact quotes and what the reader loses at each. A draft fails if the lint (`tools/cg_lint.py`) has a break or any checker fails. Tier 2 is never checked.

## Running

- With an API key: `cg_check.py prepare DRAFT --output chapter --dir RUN`, then `cg_check.py run RUN` (20 calls in parallel, Sonnet), then `cg_check.py collect RUN`.
- In a chat with no key: `prepare`, then one Sonnet helper per `RUN/R1.x.prompt.md`, each saving its JSON as `RUN/R1.x.json`, then `collect`.
- Many drafts at once (calibration): `cg_check.py batch MANIFEST --dir RUN` makes one prompt per rule carrying every draft, then `split RUN` and `collect RUN/<id>` per draft. `--only R1.7,R1.19` keeps the run to the named checkers.
- The test-set gate for a new or changed rule (step 16): `tools/cg_fold.py gate` and `result` do the batch, the split and the join with the last full run. See `rules/folds/README.md`.

## Cost

In a chat, each helper carries about 74,000 tokens of overhead before it reads anything, so a single draft costs about 1.5 million tokens (20 helpers). Through the API the same check costs about 20 calls of 500 to 800 tokens plus the draft. For daily use an API key is the cheap route.

## Smoke test (6 Nov 2026)

F8 (Aiman, his "nothing after the first sentence make any sense"), on Sonnet: FAIL, 8 of 20 checkers fail (joins, nothing arrives bare, one story, stakes, warm the water, bring it to the reader's life, built details, AI tells). Every one names the bare ending or the missing bridges. Saved in `tests/rules/runs/smoke_F8/`.

## Calibration (step 13, 6 to 11 Nov 2026)

Done: all 5 fail cases fail and all 9 approved passages pass. Report: `tests/rules/runs/calibration_2026-11-11/REPORT.md`.
- `calibration.json` holds the notes each checker reads: how to read its rule, learned from his verdicts. Each note names the cases it came from. A note never changes a rule.
- Each prompt now carries the card for its output (context only) and says when a draft is an excerpt (`--output chapter-excerpt`).
- Thin margins: F1 is caught by one checker and F3 by one.
- Daily runs use Sonnet.

## Fresh full pass (11 Nov 2026)

Confirmed: 5 of 5 fail cases fail and 9 of 9 approved passages pass, all 20 checkers from one fresh run. Report: `tests/rules/runs/fresh_2026-11-11/REPORT.md`, printed by `tests/rules/report_run.py`.
- One flip on the way: R1.19 failed P6, then P10. Two notes for R1.19 fixed it (each names its case), and two reruns of R1.19 came back 14 of 14.
- Thin margins still: F1 only by R1.16, F3 only by R1.11, the same as before.
