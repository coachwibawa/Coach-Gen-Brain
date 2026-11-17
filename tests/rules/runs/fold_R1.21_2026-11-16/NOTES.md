# Fold R1.21 gate, 16 to 17 Nov 2026

1. Wording 1 (16 Nov): 14 of 15. R1.21 passed draft Y (ORIGIN). Wording judged too soft, reworded (reasons argued, not named, doubt answered with a reason).
2. Wording 2: still 14 of 15. Calibration note added for R1.21, from his 16 Nov verdict on draft Y. Run 1: 15 of 15 (held/run1_note.json).
3. Run 2 (held/run2.json): 13 of 15. P2 (a letter) failed R1.21, ORIGIN passed. Noise, and the rule reached a letter he was proud of.
4. Scoped to the book: outputs chapter and key moments only (his words: "books that give a specific advice"). tools/cg_check.py now honours a Tier 1 rule's outputs (out-of-scope drafts pass it without a call). tests/rules/test_fold.py still passes.
5. Scoped runs 1, 2, 3 (held/scoped_run*.json): 15 of 15 each. The note held three times.
6. side/: R1.21 on draft X (old stack): fail. On the rewrite with the rule (side/drafts/REWRITE.md, 1,187 words, Opus high, new stack plus R1.21): pass.
7. Fresh review, 17 Nov (Opus, cold): the note was rule text in disguise and the gate circular (wordings 1 and 2 passed ORIGIN until the note was written from it). The rule was wider than his words (the four-part case, the strongest doubt, "once" were Claude's). Key moments cannot hold a whole case. Code points: silent gate pass, stale files in prepare, a KeyError on rule spellings. All code points fixed, tests extended.
8. Wording 3 (17 Nov): narrower, scoped to chapter, a [MATERIAL NEEDED] line, the note cut to how to read an excerpt. Run 1: 14 of 15. ORIGIN (draft Y) passes, and X passes alone (held/wording3_*.json). The rewrite passes.
9. Finding: the fault he named is not caught by a one-rule Sonnet checker on these drafts once the rule says only what he said. Wording 2 is kept as alt_wording2_spec.json. The choice goes to him (decision page, 17 Nov).
10. 17 Nov, 11:06, his pick on the close-out page (card 1 to 7): "use your recommendation, but I think this is essential enough to fail a draft". So Tier 1, wording 3. A second note for R1.21 from his verdict on draft Y (the way the 16 Nov notes for R1.5, R1.16 and R1.2 came from F1 and F3). Three runs: 15 of 15 each, ORIGIN fails on his ground every time (held/tier1_note2_run*.json).
11. Same note, alone: draft X fails, the rewrite passes (held/tier1_note2_X.json, held/tier1_note2_REWRITE.json). Approved on his pick and stored the same day.
