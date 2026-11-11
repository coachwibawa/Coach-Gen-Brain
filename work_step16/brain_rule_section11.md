
## 11. What a line answered, its context, and the words a person owns (added 2026-11-11)

This section adds to sections 3, 4 and 6. Nothing above it changed.

**Why.** His records were said inside hours of shared context. A line that worked in the session can read as a broken fragment on the page (the case study quotes, 4 to 5 Nov 2026: `claude/Case_Study_Quotes_Report_2026-11-05.md`). So "never reword" is a storage rule only. The brain keeps the words as they were said. How a line is quoted on the page follows the writing rule "A quote earns its marks", which each writing chat loads with its card. To quote a line well, a writing chat needs three more things from the session, so mining stores them with each entry (migration 020).

**Three more fields on every new entry** (agreed 5 Nov 2026):
- `answers`: what the line answered. The question or prompt it responds to, in one line, close to the words used. Empty when the line answered nothing (a monologue, a voice dump).
- `context`: one line of session context a cold reader would need: who is speaking to whom, what "it" or "he" points to, what had just happened. Facts only, never what the line means.
- `owned_words`: the words the person owns, such as their image or their signature phrase ("gas stove", "bridge", "triggered"). A list of short strings, each copied exactly from `text` or `original_text`. A writing chat never drops them from a quote.

**Filling them (mining).**
- Fill them in the same insert as the entry, from the transcript, while the session is on the page. Never from memory and never by guessing. If the transcript does not show what a line answered, leave `answers` empty.
- `text` stays exactly as said. `answers` and `context` are Claude's notes about the line. They are not the person's words and are never printed as a quote.
- The never-use lines apply to them too: no health detail, no money figure and no third person's private story in `answers` or `context`.
- A person's records stay linked through `speaker_id` and `about_id`, so a writing chat can borrow a person's own words from any of their records.

**Reading them (writing).**
- `brain.entries_full` ends with `answers`, `context` and `owned_words`.
- Entries mined before 11 Nov 2026 have them empty. For those, the session around the line is in the raw layer: the source's document in `brain.documents`, at the entry's timestamp.
- The text of an entry is frozen, but these three fields are not. They can be added to an older entry later with an update, which is logged in `brain.change_log`.
