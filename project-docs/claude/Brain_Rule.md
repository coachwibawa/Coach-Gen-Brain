# The Brain: the one rule for all Coach Gen material

Every chat in this project follows this file. If a skill or an older doc says something different, this file wins.

## 1. One place

All of Coach Gen's original material lives in one database: the Supabase project **Coach Gen Brain** (project id `zjedqjiuxkoncwsmylls`), schema `brain`. Calls, videos, podcasts, voice dumps, his published pieces, book notes, recounted client stories, testimony lines, worksheet notes: all of it.

Read and write it with the Supabase connector (`execute_sql` with project id `zjedqjiuxkoncwsmylls`). Never touch the Project Rebirth projects.

If the Supabase connector is not available in a chat, say so in one line. Do not mine into any file instead.

## 2. The old files are frozen

These are history now. Read them only to check something. Never add to them:

- `build_worksheet.js` and the worksheet PDF/docx
- `Testimony_Mastertext_Collection.md` (Mac and project copy)
- `claude/New_Material_21Oct.md` and `Book/build/book-map/new_material.md`
- `claude/Fathom_Mined_Log.md` (replaced by `brain.sources.passes`)
- The Obsidian vaults `5 Laws of Lasting Change` and `5 Laws Book Map`
- `claude/Brainstorm_Log.md` and the vault's `Brainstorm Log.md`
- `claude/Main_Brain_Input_Handoff.md` (the mining chat now uses `claude/Brain_Mining_Handoff.md`)

Everything in them was moved into the brain on 27 Oct 2026 and checked word for word. Old IDs (F-132, T-306, W-07, WS-L3-F6-01, OBS-..., BL-...) are kept in `legacy_ref`, so an old ID can still be looked up.

When a skill says "write to the worksheet", "add to the Testimony collection", "log in the mined log" or "read the vault", do the same thing in the brain instead.

## 3. Reading

Read through the view `brain.entries_full`. It has: id, legacy_ref, project, law, type, tags, text, original_text, original_language, speaker, about, certainty, origin, said_on, source, source_kind, link, importance, status, note, extra, corrects_id, added_by, added_at, times_used.

```sql
-- Law 3 material, newest first
select id, legacy_ref, type, text, speaker, about, certainty, said_on, source, link, importance, status, note
from brain.entries_full
where project = '5 Laws of Lasting Change' and law = 3 and status <> 'never use'
order by said_on desc nulls last;

-- Word search
select f.* from brain.entries_full f join brain.entries e using (id)
where e.search @@ plainto_tsquery('simple', 'boulder');

-- Unused strong material
select * from brain.entries_full where times_used = 0 and importance in ('core','major') and status <> 'never use';

-- What a work already uses, and where
select e.legacy_ref, e.text, u.location, p.name persona
from brain.used_in u join brain.entries e on e.id = u.entry_id
join brain.works w on w.id = u.work_id left join brain.personas p on p.id = u.persona_id
where w.title = '5 Laws of Lasting Change';

-- Links between pieces
select a.legacy_ref, c.relation, b.legacy_ref, c.note
from brain.connections c join brain.entries a on a.id = c.from_id join brain.entries b on b.id = c.to_id;
```

Other tables: `brain.people` (real people, role, consent), `brain.sources` (every call, video, book, file, with `passes` = what was mined from it), `brain.works` (the book, the workbook, talks, series), `brain.personas` (cast cards, one per work), `brain.used_in`, `brain.connections`, `brain.change_log` (history of every change).

Rules for reading:
- Never print anything with status `never use`.
- `certainty`: `recorded` = from a recording, person certain. `recounted` = Coach Gen's memory of a client, the struggle is real but the person may not match. `built` = invented for a persona.
- `speaker` is who said the words. `about` is who the story is about. They can differ.
- A persona belongs to a work, not to the material.

## 4. Mining (adding material)

When Coach Gen drops anything to mine, put it in the brain. He does not need to say where.

1. **Source first.** Look for it in `brain.sources` (by title or url). If it exists, read `passes` so nothing is mined twice. If not, insert it (title, kind, url, happened_on, participants).
2. **People.** Look up `brain.people` by real name. Add anyone new with role and consent.
3. **No duplicates.** Before each entry, check `brain.entries` for the same `source_id` and `link`, or the same text.
4. **The entry, verbatim.** `text` holds the words as said. Remove nothing but filler that changes no meaning, and never reword. For Indonesian, put the original in `original_text` with `original_language = 'id'`, the English in `text`, and `origin = 'translated'`. Set project, law (0 = whole book or Intro, blank if not 5 Laws), type, tags, speaker_id, about_id, certainty, said_on, source_id, link (timestamp link), importance, note (why it matters, where it fits).
5. **Connections.** Add a row to `brain.connections` when a piece pairs with, mirrors, answers or backs up another.
6. **Close the source.** Append to the source's `passes` what this pass covered and the date. Put anything left out on purpose in `left_out`.
7. **Always fill `added_by`** with the chat or skill that added the row.

Turning verbatim material into writing is each writing chat's job. The brain stores words as they were said.

Lists are fixed. Projects, types and tags come from `brain.projects`, `brain.entry_types` and `brain.tags`. An unknown value is refused. Add a new value to the list on purpose first, and only when Coach Gen agrees.

## 5. Using material in a work

When a piece goes into a book chapter, talk, article or letter, add a row to `brain.used_in` (entry, work, location, persona if any). A minor entry can be used once per work. Core and major entries can repeat. A new work gets a row in `brain.works` first.

## 6. Never delete

- Delete, truncate and drop are refused or forbidden. Never run `drop`, `truncate`, `alter table ... drop column` or `disable trigger`.
- The words of an entry never change. To fix one, add a new entry with `corrects_id` pointing to the old one, and set the old one's status to `retired`.
- Status, law, tags, importance, note and extra can change. Every change is logged in `brain.change_log`.

The full schema and the migration files are in the GitHub repo `coachwibawa/Coach-Gen-Brain` (`SCHEMA.md`, `migrations/`).

## 7. The raw layer and search (added 2026-10-27, later the same day)

This section adds to sections 3, 4 and 6. Nothing above it changed.

**What the raw layer is.** Besides curated entries (gold), the brain has a second layer for text that was cleaned but not picked as gold.
- `brain.documents`: one row per cleaned input (a call, a monologue, later a PDF or a post). Columns include `title`, `kind`, `owner` (`own` for his own words), `happened_on`, `turns` (the cleaned speaker turns), `source_id`, `notes`, `status` and `retired_note`.
- `brain.chunks`: the same text cut into pieces, with a start time, a timestamp link and a vector. Chunks and vectors are derived data. They can be rebuilt without touching a word.
- `brain.entry_vectors`: one vector per curated entry, embedded with its context (Law, Type, Speaker, About, Note, Text).
- A job embeds anything new every minute. Do not embed by hand.

**Intake rule (decided with Coach Gen, 27 Oct 2026).** Material still comes in through the mining chat, and Claude reads it. Claude removes the dirt: timestamps, filler, and whole sections that are not his knowledge (family and money talk, shopping, bookings, unrelated chat). Only the kept sections go into `brain.documents`. Do not store a whole call unfiltered. Anything cut on purpose is written in the source's `left_out` and the document's `notes`. There is no direct Fathom fetch. It stays off until a keep or drop sorting step is tested on a call Coach Gen knows well.

**Search.** `brain.search_all(query, limit, law, type, min_sim, layers)` searches by meaning and by exact words together. `layers` is `'gold'`, `'chunks'` or `'both'`. Weak matches under `min_sim` (default 0.30) are dropped. Chunks of retired documents are skipped. Law and type filters apply to gold only.

**Which layer to search (Claude proposal, 27 Oct 2026, not yet confirmed by Coach Gen).** Writing chats search gold only (`layers = 'gold'`). Search the raw chunks only to answer "have I said this before" or to recall. A raw chunk is never printed as a quote in a work unless it is first promoted to a gold entry with all its tags.

**Retiring a document.** Documents and sources cannot be deleted. To take a document out of search, set `status = 'retired'` and fill `retired_note`. Its words stay. Chunks can be removed and rebuilt, but retiring is enough.

## 8. Search tuning, the test set and the health check (added 2026-10-27, evening)

This section adds to section 7. Nothing above it changed. Where it differs from section 7, this section is current.

**How search works now (migrations 009 to 012).**
- Word match uses any meaningful word of the question, not every word. Filler words (what, is, why, how and others) are dropped by `brain.or_tsquery()`. Entries that match more words rank higher.
- A gold entry that matches by words always passes the cutoff. A chunk must still reach the cutoff on meaning, because long spoken chunks match many words.
- The default `min_sim` is now 0.32 (was 0.30).

**The test set.** `claude/Brain_Test_Set.md` holds 20 fixed questions with expected entries, and every run. Before and after any change to search, run all 20 and add a new run to the file. Never overwrite a run or remove a question. Add a question each time search misses something real. Score on 27 Oct 2026: 14 of 20 at baseline, 18 of 20 now.

**The health check.** `select * from brain.health();` returns 6 checks: the embed job is on, it ran in the last 15 minutes, no failed runs in 24 hours, every entry has a vector, every chunk has a vector, the OpenAI key works. A daily scheduled task "Brain health check" (07:41 Jakarta) runs it and notifies Coach Gen by push and email only when a check fails. When he says "fix the brain health alert", start with `brain.health()`.

## 9. Voices: own ideas and outside authors (added 2026-10-28)

This section adds to sections 7 and 8. Nothing above it changed.

**Why.** Coach Gen wants to search his own idea and see, next to it, what other authors wrote on the same idea, so he can cite them. Outside authors (for example Steven Pressfield, The War of Art, `brain.documents` id 3, owner `outside`) are stored raw in the chunks layer and never mixed up with his own words.

**The function.** `brain.search_voices(query, scope, limit_own, limit_outside, min_sim, outside_min_sim)` (migration 014). Every row has `voice` (own or outside), `author`, `source`, `place` (for a book, "page 93"), `type`, `text`, `similarity`.
- `scope = 'own'`: his gold entries and chunks from his own documents. Entries typed "outside voice" that he adopted into his framework count as his own here. Cutoff 0.32.
- `scope = 'outside'`: chunks from documents owned by `outside` only. Cutoff 0.25 on meaning, top 3. An unrelated question returns nothing.
- `scope = 'all'` (default): both lists side by side.

**How a writing chat uses it.** Run `scope = 'all'` when a piece could use a citation. Use the own list as the material. Use the outside list only as a named citation: author, book, page, exact words. An outside passage is never presented as his idea and never mixed into his voice. `brain.search_all` stays for plain recall and is unchanged.

**Test record.** Run 7 in `claude/Brain_Test_Set.md`: the original 20 questions score 18 of 20 as before, and 9 of 9 fitting Pressfield passages come back in the top 3. Rerun all 31 questions after any change to either search function, and add a new run. Never overwrite a run.

## 10. Books from PDF (added 2026-11-01)

This section adds to sections 7 to 9. Nothing above it changed.

**One route for every book PDF.** Use `tools/parse_book.py` in the repo, never a hand-made parser. It reads fonts, not spaces. Steps and settings keys are in the repo: `books/README.md` and `SCHEMA.md` (Book load route, final shape). The `/mine` skill follows the same steps.

**No approval prompt.** The load call `brain.load_from_github` inserts the documents and chunks and, for a source that already exists, appends the pass and the cut pages to the source (migration 018). Put `pass` and `left_out_add` in the load file. No separate UPDATE and no "say go" step.

**Load files.** They hold book text, so they are committed to main only for the load and removed right after with `tools/drop_load.sh`. Branch deletion and force-push are blocked from the Claude workspace.

**Dialogue books.** The `speakers` setting puts the character in each turn (Youth, Philosopher). Headings get the speaker "Section title".

**Outside search with many books.** `search_voices` takes the best passage of each book first (migrations 017 and 017b), so one large book cannot fill the citation list. Test record: Run 8 in `claude/Brain_Test_Set.md`. Rerun the 31 questions after a new book or any search change, and add a run.

**Books in the raw layer (1 Nov 2026):** The War of Art, Mindset, Atomic Habits, The Courage to Be Disliked. All outside voice, raw layer only. Gold from them only when Coach Gen asks.

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
