# Phase 4 decision page (15 Nov 2026)

Everything from steps 16 to 19 that waits for him, as one review page: 11 cards, numbers 1 to 41.

- Page: https://claude.ai/artifact/GJfsX6ro5pfMh1jdgSjCCf (slug `7bf0add9-d61e-4729-9352-3e8a15ce49b0`), capabilities db and user.
- His picks: collection `picks`. Each doc id is a card id (`1`, `2`, `3`, `4`, `5`, `6-19`, `20-23`, `24-27`, `28-34`, `35-40`, `41`), with `call` and `why`.
- Spec: `decisions.json`. Rebuild with `python3 tools/decision_page/build.py rules/phase4_decisions/decisions.json rules/phase4_decisions/phase4_decisions.html`, then publish to the same slug so the link and his picks stay.
- The lists behind the cards: `rules/step17/` (project instructions), `rules/step18/stale_docs.md`, `rules/step19/memory_dedupe.md`.
