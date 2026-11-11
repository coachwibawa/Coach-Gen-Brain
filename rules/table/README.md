# The rules table (step 9)

`brain.rules` is the one home of the writing rules. Rulebook v3 (approved 6 Nov 2026) is its first load.

- `build_rules_load.py` cuts `rules/rulebook/rulebook_v3.txt` into 49 rows: 5 frame rows (title and intro, the three tier headings, the cards heading), 39 rules (8 in Tier 0, 20 in Tier 1, 11 in Tier 2) and 5 cards. It writes `rules_v3.json`.
- Each row's `body` is its exact block of the file, heading line included. Joined by `sort`, the bodies give the file back byte for byte (md5 `a80b78c1b69fc97be58cdbad021f8138`).
- Rule codes: `R0.1` to `R0.8`, `R1.1` to `R1.20`, `R2.1` to `R2.11`, in v3 order. Cards: `card:article`, `card:letter`, `card:chapter`, `card:key-moments`, `card:case-study`. These are new codes. The step 6 groups (`T0.1` and so on in `rules/inventory/targets.psv`) are kept in each row's `evidence.step6_groups`.
- Evidence: every kept or merged inventory row is placed under exactly one rule or card (`evidence.inventory`, with source, line, summary and note). `beats` lists the same ids: the old rules this one replaces. The script fails if a row is left out. One row moved: `BR-R16a` went to "Bring it to the reader's life". The old group T2.11 (reading his raw material) lives in "A quote earns its marks".
- Cards: the letter card extends the article card, and key moments extends the chapter card. A card's `loads` lists its Tier 2 rule codes. Empty means it takes the loads of the card it extends.
- Checks the script runs: 215 numbered lines, each in exactly one row. Counts 8, 20, 11 and 5. His typed v3 lines 4 and 139 in place, with the curly apostrophe in "we’re". The rows rejoin to the file. It prints each card's size and md5.

## Load

1. `python3 rules/table/build_rules_load.py`, then push.
2. `select * from brain.load_rules('rules/table/rules_v3.json');` Inserts only. It refuses any code already in the table. `rulebook_md5` must equal `source_md5`.
3. `select o, md5(brain.card_text(o)) from unnest(array['article','letter','chapter','key moments','case study']) o;` must equal the md5 values the script printed.

## Reading

- `brain.get_card('chapter')`: the rows the chapter writer loads, in rulebook order.
- `brain.card_text('chapter')`: the same as one text.
- `brain.rulebook_text()`: every live row, for the word-for-word check against the file.
- Only rows with `status = 'active'` and `fold_stage = 'stored'` are served.

## Changing a rule

- Never delete. Retire with `status = 'retired'` and a `retired_note`. Every insert and update is copied into `brain.change_log`.
- A new rule climbs the fold stages: captured, judged, merged, gated (the test set), approved (his go), stored. It records what it beats, its source and its date. It cannot reach `approved` or `stored` without `approved_on`.
- The fold path (step 16, 11 Nov 2026): `tools/cg_fold.py` and `brain.fold_load`, `brain.fold_store`, `brain.fold_decline` (migration 021). Steps and the spec format: `rules/folds/README.md`. Rule codes never change: a changed rule is updated in place when its fold is stored, and the fold row stays as the record.
- After the first stored fold, the rules as they stand are `rules/table/rules_live.json` and `rules/rulebook/rulebook_live.txt` (v3 plus the stored folds, rebuilt by `cg_fold.py live`). `rules_v3.json` and `rulebook_v3.txt` stay as the first load and are never edited.

Size per card at about 4 characters a token: article 5,050, letter 5,360, chapter 5,850, key moments 6,010, case study 4,970.

## The card compiler (step 10)

- `python3 rules/table/compile_cards.py rules/table/cards --brain-md5 article=... letter=... chapter=... key_moments=... case_study=...` builds the five cards from `rules_v3.json` (the file loaded into `brain.rules`), picking rows the way `brain.get_card()` does.
- It fails the run if any card line is not a line of `rulebook_v3.txt` word for word and in the same order, if a card's md5 differs from the md5 of `brain.card_text()` read from the live brain, or if any rule or card row is never served.
- Output: `rules/table/cards/Card_Article.md`, `Card_Letter.md`, `Card_Chapter.md`, `Card_Key_Moments.md`, `Card_Case_Study.md` and `MANIFEST.md5`.
- Copies: the project (`claude/cards/`) and his Mac (`Book/Rule Cards/` in the 5 Laws of Lasting Change folder). Both are overwritten by a rebuild, never edited by hand.
- Run 6 Nov 2026: all five equal the live brain. Chapter card about 5,846 tokens.
