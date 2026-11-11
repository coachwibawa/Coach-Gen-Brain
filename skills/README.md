# Skill drafts (Rules Refactor Plan, Phase 4)

Each folder holds the SKILL.md proposed to him with propose_skills. The live skill is the one he saves from the card. These files are the record of what was proposed and why.

- `coach-gen-writer/` (step 14, 11 Nov 2026): rewritten from 6,400 words to about 2,000. It loads the card from the brain (`brain.card_text`), drafts, lints (`tools/cg_lint.py`), checks once with the one-rule checkers (`tools/cg_check.py`), and builds the chapter doc with one command. The plan aimed at 1,500 words. The extra 500 are the two Notion schemas (this is their only copy), the scorecard levels, and the doc-build inputs, which no card holds. All 40 inventory rows with target `skill:writer` landed (checked by a fresh reviewer, whose 9 finds were added).
- The one command for the doc build (step 15) is `Book/source/epoch_build.py` on his Mac, beside `make_review_doc.py`. It is not in this repo.
