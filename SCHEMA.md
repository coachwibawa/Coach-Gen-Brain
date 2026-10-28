# Coach Gen Brain: schema

Read this before reading from or writing to the brain. It is the plain-words description of every table and column. If this file and the database ever disagree, the database is right and this file must be updated.

- Supabase project: **Coach Gen Brain** (id `zjedqjiuxkoncwsmylls`, coachwibawa's Org, Singapore)
- Everything lives in the schema `brain`. The public API cannot reach it.
- Brain work touches this project only. Never the Project Rebirth projects.

## The rules (enforced by the database)

1. **Nothing is ever deleted.** Delete and truncate are refused on every table.
2. **On entries, these never change:** text, original text, original language, speaker, source, link, date said, legacy ref, corrects, added by, added at. To fix a mistake, add a new entry with `corrects_id` pointing to the old one.
3. **Everything else can change** (status, importance, law, tags, note, about, extra, and so on). Every change is copied into `brain.change_log`, which itself can never be edited.
4. **Tags, types and projects come from fixed lists** (`brain.tags`, `brain.entry_types`, `brain.projects`). An unknown value is refused. To add one, insert it into the list on purpose first.
5. **A minor entry is used once per work.** Core and major entries may repeat. Using a minor entry in a different work is fine.
6. **A persona in `used_in` must belong to the same work.**
7. **Columns are never dropped.** A column that is no longer needed is renamed and retired.
8. **Never run** `drop`, `truncate`, `alter table ... drop column`, or `disable trigger` on the brain. The lock stops accidents. It cannot stop a deliberate admin command, so this rule matters.

## How to read

Read through the window **`brain.entries_full`**. It shows every entry with speaker, about and source as names, plus `times_used`. Chats should read this view, not the raw table, so the table can change underneath without breaking anyone.

Examples:
- Law 3 material, newest first: `select * from brain.entries_full where project = '5 Laws of Lasting Change' and law = 3 order by said_on desc nulls last;`
- Word search: `select * from brain.entries_full e join brain.entries x using (id) where x.search @@ plainto_tsquery('simple', 'lazy');`
- Unused gold: `... where times_used = 0 and importance in ('core','major') and status <> 'never use'`
- Never print anything with status `never use`.

## How to add

1. **Check the source first.** Look in `brain.sources` by title or url. If it exists, read its `passes` so you do not mine it twice. If not, add it.
2. **Check the people.** Look up `brain.people` by real name. Add anyone new, with role and consent.
3. **Check for duplicates.** Before adding an entry, check `brain.entries` for the same `source_id` and `link`.
4. **Add the entry.** Exact words in `text`. For Indonesian sessions, the original words go in `original_text` with `original_language = 'id'`, and the English translation in `text` with `origin = 'translated'`.
5. **Add connections** where an entry pairs with, mirrors, answers or backs up another.
6. **Update the source's `passes`** with what this pass covered.
7. Always fill `added_by` with the chat or session that added the row.

## Tables

### brain.entries: one row per mined piece
| Column | Meaning |
|---|---|
| id | Running number. This is the entry's number from now on (#1, #2...) |
| legacy_ref | Old ID from before the brain (T-306, F-132, W-07). Blank for new entries |
| project | From `brain.projects` |
| law | 1 to 5. 0 for Intro or whole book. Blank if not 5 Laws |
| type | From `brain.entry_types` |
| tags | Any number, each from `brain.tags` |
| text | The exact words (English) |
| original_text | The original words, if not English |
| original_language | Language code of the original, for example `id` |
| speaker_id | Who said the words (`brain.people`) |
| about_id | Who the story is about (`brain.people`). May differ from the speaker |
| certainty | `recorded` (from a recording, person certain), `recounted` (Gen's memory, struggle real, person may not match), `built` (invented for a persona) |
| origin | `verbatim`, `translated`, `joined`, `shortened`, `built` |
| said_on | Date the words were said |
| source_id | Where it came from (`brain.sources`) |
| link | Timestamp link |
| importance | `core`, `major`, `minor` (default `minor`) |
| status | `raw` (default), `printable`, `placed`, `never use`, `retired` |
| note | Why it matters, where it fits |
| extra | Box for one-off details (JSON). If a key gets used a lot, it becomes a real column |
| corrects_id | The entry this one corrects |
| added_by, added_at | Who added it and when |
| search | Built automatically for word search |

### brain.sources: one row per call, video, podcast, book, article or dump
title, kind (`fathom call`, `video`, `podcast`, `article`, `book`, `voice dump`, `own published`, `note`, `chat`, `other`), url, happened_on, participants, passes (which mining passes it got), left_out (what was left out on purpose), notes.

### brain.people: one row per person
real_name, role (`self`, `client`, `peer`, `coach`, `family`, `friend`, `outside author`, `other`), consent (`given`, `pending`, `not asked`, `refused`, `not needed`), notes.

### brain.connections: links between entries
from_id, to_id, relation (`pairs with`, `before after`, `backs up`, `mirrors`, `answers`, `same idea`, `contradicts`, `part of`), note.

### brain.works: each book, talk, article, series
title, kind (`book`, `workbook`, `talk`, `article`, `article series`, `letter`, `reel`, `reel series`, `course`, `other`), status, notes.

### brain.personas: a persona's profile inside one work
work_id, name, profile, based_on. The persona belongs to the work, not to the material.

### brain.used_in: an entry used in a work
entry_id, work_id, location (chapter, page, slide), persona_id (optional, same work), used_on, note.

### brain.change_log: history of every change
table_name, row_id, old_row, new_row, changed_by, changed_at. Read only.

## Migrations
Every change to the shape of the brain is a numbered file in `migrations/`, applied in order.
- `001_brain_schema.sql`: tables, lists, lock, history, privacy, window
- `002_pin_function_search_path.sql`: security fix from the Supabase advisor
- `003_certainty_optional_and_staging.sql`: certainty may be blank (ideas, framework text, outside voices); a private `staging` schema for the one-time move-in

## Move-in record (2026-10-27)
802 entries, 47 sources and 11 people moved in from the worksheet (403), the Testimony collection (114), the New Material bank F-01 to F-150 and W-01 to W-19 (217) and the Obsidian Book Map vault (68). `added_by` on these rows is `move-in 2026-10-27 (mining chat)`. Every field was checked against the original files by hash and matched exactly. Old IDs live in `legacy_ref`.

Second pass, same day, from the Obsidian Book Map vault:
- 2 works: the book "5 Laws of Lasting Change" (its `notes` hold the Persona Map, verbatim) and "5 Laws client workbook".
- 22 personas: the 18 Cast cards for the book (each `profile` is the full card, verbatim, including "Your corrections") and 4 for the workbook.
- 307 `used_in` rows: 296 book rows from the vault's Concepts and "Closest match" scan (snapshot of 22 Oct; locations keep the vault's flags such as REPEAT and CONTRADICTION), 11 workbook rows for lines marked PLACED.
- 39 connections: 24 "pairs with" (Testimony "Pair with" and notes that name a pair), 15 "same idea" (pieces under one Book Map concept).
- 58 entries BL-01 to BL-58: every quoted line of the vault's Brainstorm Log, with the decision that followed in `note`. Lines about a cast member are `client story`, `recounted`, with the cast name in `extra.persona`. The whole log is kept verbatim in the source's `notes`.
- The vault's piece "T-110" was a stray note about the Testimony file, not material, so it was skipped. 222 vault worksheet IDs used an older numbering and were matched to the brain by exact text.

## Vector layer (2026-10-27)
- `entry_vectors` (one 1536-number vector per gold entry, model text-embedding-3-small, key in Supabase Vault as `openai_api_key`).
- `documents` (full cleaned text of calls, videos, PDFs, posts. Add-only. `owner` = own, client, peer, outside) and `chunks` (derived and rebuildable, with vectors).
- `brain.search_all()` searches both layers. A cron job embeds anything new every minute.
- First raw document: Gen and Genio sprint 27 Oct 2026 (documents id 1, source row added). Personal and money talk left out (see `left_out`).
- Cleanup tags on old rows: heading 5, table dump 1, duplicate 17, label 12.

## Retire a document (2026-10-27, later)
- `documents.status` is `active` or `retired`, plus `retired_note`. Documents and sources cannot be deleted (delete trigger). Retire instead. `search_all()` skips chunks of retired documents.
- Document 1 (the 27 Oct sprint) is retired. Coach Gen judged it tech talk with no 5 Laws insight. The words are kept.
- Removal test (rolled back): chunks can be deleted, documents and sources are refused.
- Intake rule: calls come in through the mining chat. Claude cuts junk sections before a document is stored. No direct Fathom fetch for now. See `Brain_Rule.md` section 7 in the project.
- Not yet in this file from earlier: BL-59 to BL-65 (the Brainstorm Log entries added after BL-58), so counts above may be short by those.

## Search tuning and health check (2026-10-27, evening)
Tested against a fixed 20-question set (`claude/Brain_Test_Set.md` in the project, with every run recorded). Baseline 14 of 20, now 18 of 20.
- `009_search_or_word_match.sql`: new `brain.or_tsquery()`. Word match now uses any meaningful word of the question (filler words dropped) instead of every word. Run 2: 16 of 20.
- `010_search_word_match_passes_cutoff.sql`: a match on words always passes the meaning cutoff. Fixed "yearly misogi", which matched by words but scored 0.253 on meaning.
- `011_chunks_keep_cutoff.sql`: takes 010 back for chunks only. Long spoken chunks match many words and flooded results. Gold entries keep the skip. Run 4: 17 of 20.
- `012_search_cutoff_032.sql`: default `p_min_sim` raised from 0.30 to 0.32. Run 5: 18 of 20.
- `013_health_check.sql`: `brain.health()` returns 6 checks (embed job on, ran in last 15 minutes, no failed runs in 24 hours, every entry searchable, every chunk searchable, OpenAI key works). Not callable by anon or authenticated. A daily scheduled task "Brain health check" (07:41 Jakarta) reads it and notifies Coach Gen by push and email when a check fails.
- Still failing: Q15 (T-032, its search text carries a call link and timestamps) and Q18 (WS-L5-F7-03). Both are ranking problems, left until more material is in.
- Migrations 010 to 012 edit the live function text with `replace()`, so they must run in order after 009.

### Voices search (28 Oct 2026)

- `014_search_voices.sql`: `brain.search_voices(query, scope, limit_own, limit_outside, min_sim, outside_min_sim)`. Scope `own` returns Coach Gen's gold entries (including adopted entries typed "outside voice") and chunks from his own documents, cutoff 0.32. Scope `outside` returns chunks from documents owned by `outside`, cutoff 0.25 on meaning, top 3. Scope `all` (default) returns both lists. Each row has `voice`, `author`, `source`, `place` ("page 93" for books). The main `brain.search_all` stays unchanged.
- The War of Art (Steven Pressfield, 2002) is loaded as `brain.sources` 53 and `brain.documents` 3 (owner `outside`, 591 turns from PDF pages 6 to 158, 103 chunks). Data only, no migration.

### Loading long outside texts from GitHub (28 Oct 2026)

- `015_load_from_github.sql`: `brain.github_fetch(path)` and `brain.load_from_github(path)`. The token is a read-only fine-grained GitHub token for this repo, stored in the Supabase Vault as `coach_gen_brain`.
- Flow for a book: clean the PDF in code into `turns.json`, run `python3 tools/build_load.py turns.json loads/<name>.json meta.json`, push, then run `select * from brain.load_from_github('loads/<name>.json');` and compare the md5 values with the ones the script printed. Load files hold copyrighted book text, so remove them from `loads/` after the load. The repo is private.
- Mindset (Carol S. Dweck) is source 54, 28 documents (ids 4 to 31), 1,735 paragraphs, 411 chunks. It was loaded the slow way, through the chat, before this route existed.
