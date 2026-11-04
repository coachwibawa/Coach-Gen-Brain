# Brain Function: Handoff (2026-10-27, 18:20)

## Start here
The next chat is for "the brain function". Coach Gen named it only as "for the brain function". The record does not say which function he means. Ask him in one line what it is before building anything, and write his answer into this doc. Candidates that exist in the plans are listed under "What it could mean". Do not pick one for him.

## Where things live
- Rule for all chats: `claude/Brain_Rule.md` (section 7 covers the raw layer, search and retiring).
- Plan and status: `claude/Brain_RAG_Plan.md` (status update at the bottom).
- Mining handoff and its CORRECTION block: `claude/Brain_Mining_Handoff.md`.
- Pipeline manifesto with built and not built marked, the 16:46 decision and 18 risks: `Brain_Pipeline_Manifesto.md`. It is a chat file only and is not in the project. Ask him if it should be.
- Schema and migrations 004 to 008: GitHub `coachwibawa/Coach-Gen-Brain` (`SCHEMA.md`, `migrations/`).
- Supabase project `zjedqjiuxkoncwsmylls`, schema `brain`, free plan, region ap-southeast-1. Never touch the Project Rebirth projects.
- Skills now installed: `mine` (proposed as a card at 17:03, check it is saved), `extract-fathom` (saved, has the raw layer steps), `coach-gen-writer` (saved, reads the brain), `write-book-from-material` (saved). `inside-the-introvert` and `lasting-change-letters` were deleted by him.

## What exists today (checked live at 18:20)
- Edge functions: none. `list_edge_functions` returned an empty list.
- Vault secrets: `openai_api_key` only. There is no Fathom key and no Anthropic key.
- Cron: one job, `brain-embed`, every minute, active.
- Counts: 875 entries (867 at the move-in, 8 added since by another chat, last one at 18:02 Jakarta), 51 sources, 2 documents (1 active, 1 retired), 65 chunks.
- Database functions already there: `brain.embed_text` (calls OpenAI from inside Postgres through the `http` extension), `brain.embed_pending`, `brain.embed_pending_chunks`, `brain.chunk_document(doc, target_words, overlap_turns)`, `brain.search`, `brain.search_all(query, limit, law, type, min_sim, layers)`.
- Supabase tools available for a function: `deploy_edge_function`, `create_edge_function_secret`, `get_edge_function`, `list_edge_functions`, `query_logs`, `get_advisors`.

## Done (relevant to a function)
- Vector layer and raw layer live. Hybrid search works with a similarity cutoff. Retired documents are skipped.
- `documents.status` (active or retired) added in migration 008. Documents and sources cannot be deleted by design.
- Decision of 27 Oct 2026, 16:46 (Coach Gen): calls and files come through Claude. Claude cleans, cuts junk sections and stores only the kept text. No direct Fathom fetch that stores whole calls. It may return only if a keep or drop sorting step is tested on a call he knows well, with him checking what it dropped.

## What it could mean (not decided, do not pick for him)
1. A function that fetches Fathom transcripts with an API key. Currently rejected as described above, unless it includes the sorting step.
2. A function that turns audio into text for the phone video. The route is undecided: local Whisper on his Mac, OpenAI transcription (file limit about 25 MB) or a Mac app. His Mac has ffmpeg, no Whisper, and its shell had no internet in the test.
3. A function that other tools can call to search the brain (a retrieve endpoint).
4. A function that writes a one-line context for each chunk with a cheap model, to fix loose questions missing chunks. Needs an Anthropic key in the Vault.

## In progress
Nothing is half built. No migration or function is waiting.

## Next, in order
1. Ask Coach Gen which function he means. Write the answer under "Start here".
2. Check the Supabase advisors and the project settings before building: `get_advisors` (security and performance), and whether the free plan pauses an idle project. The pause rule is believed to be about one week and is not verified.
3. Write the spec in plain words first: what goes in, what comes out, what it costs, what can fail, who sees the text. Show it to him before deploying.
4. Build it small. Store any key in the Vault or as a function secret, never in code or in a project doc.
5. Test it on a call or file he knows well, and show him what it kept and dropped.
6. Add an alert for silent failure (the embed job stopping, a key expiring, the spend cap). None exists now.
7. Record it in `SCHEMA.md` and `migrations/`, then push. Update `Brain_Rule.md` and `Brain_RAG_Plan.md` additively.

## Rules for this work
- Never delete. Documents and sources are add-only. Retire with `status`.
- Verbatim stays verbatim. A function never rewrites his words.
- A whole input is never stored unfiltered.
- Client material goes to OpenAI when it is embedded. Whether his client consent covers that is not known. Raise it before any new outside service touches client text.
- Keys never go into code, docs, chat or git.
- Never touch the Project Rebirth Supabase projects.
- Destructive actions go last and need his approval.
- Answer his question first, in plain words, no unasked options. He is the expert on his material. Do not assume what he wants. His documents: no em dashes, no semicolons, simple English.

## Suggested skills
- `mine` and `extract-fathom` for any intake test.
- `grilling` if he wants the function spec stress-tested.
- `wait-what` only when he types it.
- `handoff` at the end.
