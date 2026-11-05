# Step 7: the decision page

`decisions.json` is the spec for the review page "Rulebook Decisions" (https://claude.ai/artifact/GMy4eBgCtFPBWSMLFbHncD). `rulebook_decisions.html` is the built page. Build with `python3 tools/decision_page/build.py rules/step7/decisions.json rules/step7/rulebook_decisions.html`, then publish the same file path so the link and the saved picks stay.

His picks save to the page's db collection `picks`, one doc per card (doc id = the card's number or range, fields `call` and `why`). Read them with ArtifactData `list`.

Cards: 1 to 7 requirements, 8 to 13 his calls (business changes), 14 to 38 proposed cuts and changes (flags.psv), 39 to 41 open clashes, 42 to 56 settled clashes (clashes.psv).
