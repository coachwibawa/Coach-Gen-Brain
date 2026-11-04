# Brain plan: from database to retrieval (27 Oct 2026)

Built from the 27 Oct sprint with Genio (https://fathom.video/calls/877109209, 05:00 to 56:30) and the brain as it stands. Draft for Coach Gen and Genio to check.

## 1. What this is for

The brain is for his whole career, not one book. He mines everything without deciding where it goes: his own monologues and calls, client sessions, books he liked (whole PDFs), other people's talks, posts he admires. A week or a year later, any chat recalls the right piece.

The test of success: output that is his, not AI slop. His original thoughts, the problems he met, and how coaching helped people with them. Knowledge compounds, and that is where authority comes from: he can talk about one topic, deeper and deeper, for three hours.

Why it comes first: the book ran out of ideas and started recycling. More material fixed that but made every chat bloated and expensive, and nobody could tell what had already been said. A database fixes tracking. Retrieval fixes cost and scale.

## 2. What exists today

- Supabase project "Coach Gen Brain", schema `brain`, locked (no deletes, words never edited, every change logged).
- 867 curated entries: his and his clients' verbatim lines, each tagged with Law, type, speaker, source, link and date.
- Sources, people, works, personas, used_in, connections.
- Plain word search (Postgres full-text). No vectors yet.

## 3. Two kinds of material

| | Curated entries (have) | Raw documents (new) |
|---|---|---|
| What | One idea, story or line, picked as gold | Everything: full transcripts, monologues, book PDFs, talks, posts |
| Size | A sentence to a paragraph | Minutes to hundreds of pages |
| Use | Exact quotes for the book. Must stay verbatim | Inspiration, recall, "have I said this?", style of others |
| Chunking | None, each entry is already one piece | Cut into chunks |

Both are kept. Curated entries are what gets printed. Raw documents mean nothing said is ever lost, even if it was not picked as gold.

## 4. Layer 1: data (the part every agent reuses)

**New tables**
- `documents`: one row per transcript, PDF, talk or post. Source, date, link, and the **owner**: his own words, a client, a peer, or outside (another author or creator). The owner tag is what keeps other people's material from ever being printed as his.
- `chunks`: one row per piece of a document. Position, text, start and end timestamp (for calls), embedding.
- `entry_vectors`: one vector per curated entry.

The vector tables hold derived data. They can be rebuilt any time without touching a word, so the lock on entries stays as it is.

**Cleaning, by kind of source**
- Calls and monologues: remove timestamps and filler noise from the text, keep who is speaking, and keep each chunk's start time so it still links to the moment in the recording.
- PDFs: remove headers, footers and page numbers.
- Posts: caption plus spoken transcript.

**Chunking** (the hard part, settled by testing, not guessing)
- Start with the common practice: about 500 to 1,000 tokens per chunk, with overlap (about 200 tokens) so a key sentence is never cut away from its context.
- Calls: cut at speaker turns, never mid-thought.
- Books: cut at paragraphs and sections.
- Curated entries: not chunked. A short line is embedded together with its context (Law, type, note, speaker, source), so "Don't think I can do, so I don't do." still lands near the right questions. This answers Genio's worry that very short entries never get hit.

**Embedding**
- One model for everything, because the question is turned into a vector by the same function as the material.
- Runs inside Supabase (an edge function), triggered on every new row, plus one backfill for what is already there.
- Model choice is open (section 8).

**Retrieval: one search function, hybrid**
- Meaning (vector) and exact words (full-text) together, merged into one ranked list.
- Filters: owner (his own only, or include outside), project, Law, kind of source, date range.
- Returns the top 5 to 10 pieces with the exact text, the source and the link.
- Two modes, as discussed in the sprint: exact (book quotes, verbatim, from curated entries) and loose (inspiration, can drift).

**Getting material in without burning tokens**
Today every transcript passes through a chat to reach the database. A 77-minute call is about 65,000 characters, read in and written out again. The cheaper path is to let Supabase fetch it directly:
- Fathom: an edge function pulls the transcript with a Fathom API key. The chat only says "mine call X".
- PDFs and audio: upload to Supabase Storage, and an edge function extracts the text.
Chats then spend tokens only on judgment (picking gold for curated entries), not on copying text.

## 5. Layer 2: application (agents that use the data)

Skills, each small, each reused:
- **mine**: drop anything (link, file, voice note, pasted text). It goes into documents and chunks automatically. A judgment pass picks gold into curated entries.
- **retrieve**: any chat asks the brain a question and gets the top pieces back.
- **check said**: before printing, "have I already used this in this work?" (used_in plus search).

Agents per job, each using retrieve instead of reading large project docs:
- book, article and letters, social media (IG script, LinkedIn post), editor, brand kit, company admin.

Rules (Language Rules, Book Rules, Guardrails) stay inside the skills and are read in full. A rule pulled in pieces gets half-applied. His published pieces go in as writing samples, so agents can retrieve his style by example.

Where the token saving comes from: a chat pulls 10 relevant pieces instead of reading the whole project knowledge every time. Model routing as Genio said: Opus to plan, Sonnet to build and execute, Haiku for cleaning and routine skill runs.

## 6. Layer 3: autonomous (later)

Agents acting on the brain by themselves. The dream pipeline: open a chat, get an IG script or LinkedIn post built from his own thoughts, do one take, Concat edits, the AI posts. Posting to LinkedIn and Facebook already exists. This layer only works once layers 1 and 2 return good material, so it comes last.

## 7. Milestones

| | Milestone | Done when |
|---|---|---|
| M0 | Finish the cutover | Destructive batch approved and run, Project instructions pasted, skill cards saved |
| M1 | Prototype on what exists | 867 entries embedded with context, hybrid search works, 10 of his real questions return sensible results |
| M2 | Calls as documents | Every Fathom call fetched by Supabase itself, cleaned, chunked, embedded. "What have I said about X" works across all calls |
| M3 | Outside material | One book PDF and one creator's posts in, tagged outside, never mixed with his own |
| M4 | Skills | mine, retrieve and check said. Writing skills switched to retrieve |
| M5 | Tune | Chunk size, overlap and the meaning/exact balance adjusted from real use |
| M6 | Autonomous | The dream pipeline, one agent at a time |

M1 is small and shows quickly whether this works for him before anything bigger is built.

## 8. Decisions still open (for later, not now)

1. Embedding model: OpenAI (about $1 a month, strong on mixed Indonesian and English, needs an API key) or Supabase built-in (free, weaker on Indonesian).
2. Fathom API key for direct fetching.
3. What goes in first after the prototype.
4. Genio's role: review only, access to the Supabase org, or checking the plan before each milestone.
5. Order against the book: alpha readers for Ch1 to 3 and the next article can run in their own chats in parallel, because the brain as it stands already serves the book.

## 9. Risks

- Chunking settings are a guess until tested.
- Mixed Indonesian and English weakens a weak model.
- Outside material must never be printed as his: the owner tag and the filter are the guard.
- Edge functions are one more thing to keep deployed and patched (Genio's point about maintenance).

---

## Status update, 27 Oct 2026 (later the same day)

Added after the plan was built into the brain. Nothing above this line changed, so the text above still shows the plan as it was written.

**Milestones**
- M0 done: destructive batch run, `staging` schema dropped. The skill cards are shown to Coach Gen and not all saved yet.
- M1 done: all 867 curated entries have vectors (OpenAI text-embedding-3-small, 1536 numbers, embedded with their context). Hybrid search works, with a similarity cutoff. A few test questions ran. His 10 to 20 real questions have not been tested yet.
- M2 changed. As written, "every Fathom call fetched by Supabase itself" is on hold. The raw layer is built (`documents`, `chunks`, `search_all`, an embed job every minute, `status` for retiring). Calls still come in through the mining chat. Reason below.
- M3 to M6 not started.

**Why M2 is on hold (Coach Gen's concern, 27 Oct 2026).** Cleaning means more than removing filler words and timestamps. It also means cutting whole sections that are not his knowledge: family and money talk, shopping, bookings, unrelated chat. Code can only match keywords. It cannot tell a Law 5 story from a shopping order. A direct fetch would fill the raw layer with junk that matches searches, and private talk would be sent to OpenAI for vectors. Intake therefore stays with Claude reading the call and keeping only the sections that are his. A direct fetch can come back only after a keep or drop sorting step (for example, a cheap model marks each section and Coach Gen checks what it dropped) is tested on a call he knows well.

**Real numbers from the build**
- A 77-minute call through the Fathom connector costs about 30,000 tokens.
- The 27 Oct sprint became 280 cleaned turns and 62 chunks at 150 words each, with one turn of overlap. 150 words is a test value, not a decision.
- Tuning finding: loose, abstract questions miss chunks that use other words, because mixed-topic chunks blur the vector. Planned fix: a one-line context for each chunk written by a cheap model. Not built.
- Document 1 (the sprint) was judged to be tech talk with no 5 Laws insight and was retired. Documents and sources cannot be deleted, by design. Chunks can.

**Rules decided or proposed today**
- Raw documents are cleaned and cut of junk sections before storing (decided).
- Writing chats search gold only. Raw chunks are for "have I said this" and recall, and are never printed as a quote without first becoming a gold entry (Claude proposal, not yet confirmed by Coach Gen).

**Next, in order**
1. Coach Gen saves the `extract-fathom` card. Add the raw layer steps to it.
2. Collect 10 to 20 of his real questions for the golden set.
3. Test chunk size, the one-line chunk context, and the small against the large embedding model on that set.
4. Phone video: Google Drive and Cowork, ffmpeg for the audio, a transcription route still to choose.
5. Write the `retrieve` and `check-said` skills after the tuning.

The full pipeline, with built and not built marked and a list of 17 risks, is in `Brain_Pipeline_Manifesto.md`.

---

## Status update, 27 Oct 2026 (evening)

Added after the first tuning pass. Nothing above this line changed.

**M5 started (tuning).**
- A 20-question test set is in `claude/Brain_Test_Set.md`, with every run kept. The questions were proposed by Claude from the brain and approved by Coach Gen. They are not yet his own real questions, so "next" item 2 above is only partly done.
- Score: 14 of 20 at baseline, 18 of 20 after migrations 009 to 012.
- What changed: word match uses any meaningful word, not every word. Gold entries that match by words always pass the cutoff. Chunks keep the cutoff. The default cutoff is 0.32.
- Still failing: two ranking problems (T-032 and WS-L5-F7-03). Left until more material is in, so search is not tuned to 20 questions and one speech.
- Raw icebreaker chunks still crowd the top 5 on 4 of 18 unrelated questions. All 65 chunks come from one speech, so this waits for more documents.

**Silent failure alert built.** `brain.health()` (migration 013) checks the embed job, missing vectors and the OpenAI key. A daily scheduled task at 07:41 Jakarta notifies Coach Gen by push and email when a check fails. Risk "a key expiring or the job stopping with nobody noticing" is now covered. The OpenAI spend cap itself is not checked directly. A cap that blocks the key shows up as the key check failing.

**Saved.** Migrations 009 to 013 and `SCHEMA.md` are pushed to GitHub `coachwibawa/Coach-Gen-Brain`.
