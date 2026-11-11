# mine: the edits proposed on 11 Nov 2026 (step 16, the mining change)

Two exact replacements on the installed SKILL.md (proposed with propose_skills as `edits`). The reason: migration 020 added `answers`, `context` and `owned_words` to `brain.entries`, and section 11 of `claude/Brain_Rule.md` says how to fill them.

## Edit 1 (section 6, Pick the gold)

Old:

- Entries are verbatim. Follow section 4 of `claude/Brain_Rule.md`. Fill `added_by` with `mine`. Mark anything on the NEVER USE list with status `never use`. Never delete or reword. To fix an entry, add a new one with `corrects_id`.

New:

- Entries are verbatim. Follow section 4 of `claude/Brain_Rule.md`. Fill `added_by` with `mine`. Mark anything on the NEVER USE list with status `never use`. Never delete or reword. To fix an entry, add a new one with `corrects_id`.
- With every entry, in the same insert, also fill `answers`, `context` and `owned_words` (section 11 of `claude/Brain_Rule.md`): what the line answered, one line of session context a cold reader would need (facts, never the meaning), and the words the person owns, copied exactly from the text. Write them from the transcript while it is on the page. Leave `answers` empty when the line answered nothing.

## Edit 2 (Rules that do not change)

Old:

- Verbatim stays verbatim. Turning it into writing is the writing chats' job.

New:

- Verbatim stays verbatim. "Never reword" is a storage rule: the brain keeps the words as said, and turning them into writing is the writing chats' job.
