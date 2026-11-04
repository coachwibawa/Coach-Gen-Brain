# Brain Mining: Handoff (2026-10-27)

This replaces `claude/Main_Brain_Input_Handoff.md` for mining. That doc is kept as history and is not updated.

## Start here
This chat is where Coach Gen drops raw material to mine: Fathom calls, videos, podcasts, articles, voice dumps, chat thoughts. Everything goes into one place, the Coach Gen Brain (Supabase project `zjedqjiuxkoncwsmylls`, schema `brain`). He never has to say where it goes. Every writing chat reads the brain, so nothing needs routing. The full rule is `claude/Brain_Rule.md`. Read it first.

This chat does not draft (that is `coach-gen-writer`) and does not do company admin (`claude/Company_Docs_and_Tax_Handoff.md`).

## What is in the brain (27 Oct 2026)
- 867 entries: worksheet 403, Testimony collection 114, book material bank 217 (A-, B-, E-, L-, N-, F-01 to F-150, W-01 to W-19), Obsidian vault 68, Brainstorm Log 65 (BL-01 to BL-65).
- 49 sources (every Fathom call mined so far, with its passes and what was left out on purpose), 11 people with consent.
- 2 works (the book, the client workbook), 22 personas (the Cast cards), 307 "used in" rows, 39 connections.
- Every row was checked word for word against the original files.

## Frozen (history, never add to them)
`build_worksheet.js`, `Testimony_Mastertext_Collection.md`, `claude/New_Material_21Oct.md`, `claude/Fathom_Mined_Log.md`, `claude/Brainstorm_Log.md`, `claude/Main_Brain_Input_Handoff.md`, both Obsidian vaults.

## How to mine
Follow `claude/Brain_Rule.md` section 4: source first (check `passes`), people, no duplicates, the entry verbatim with its timestamp link, connections, close the source's `passes`, fill `added_by`. Report one line per entry: law, type, the exact text, the link, and one plain reason.

Rules carried over from the old handoff:
- Never quote a call from memory. Pull the transcript first.
- Mine verbatim. Turning it into writing is the writing chats' job.
- Mark anything on the old NEVER USE list with status `never use` (money figures, health details, religious lines, organisation or club names, a third person's private story). It is stored, never printed.
- Calls left out on purpose stay out unless he says so: Stefanie Toner (ask him first), ACC group mentoring calls, Gen and Genio sprints before August, the 24 Aug finance call.
- To-dos from calls still go to `Master_Project_Status.md`. Durable facts about him go to memory.
- His documents: no em dashes, no semicolons, simple English. Use his doc names, never nicknames.

## Open items
- No Fathom calls after 26 Oct have been mined yet.
- Wayan still needs a print name. How Pak Jeffrey is named in print is still open.
- Pending his approval (the destructive batch, 27 Oct): drop the temporary `staging` schema in the brain, add a one-line frozen notice to the top of three Mac files, save the skill updates, paste the Project instructions rule.

## Suggested skills
- `extract-fathom` (updated to write to the brain once he saves the card).
- `grilling`, `wait-what`, `handoff`.

---

## Update, 27 Oct 2026 (later the same day): the raw layer and the intake decision

Added after the 27 Oct sprint with Genio. Nothing above this line changed, except that the destructive batch below is now done.

**Done since the text above**
- The destructive batch was approved and run: the temporary `staging` schema is dropped.
- The vector layer is live. All 867 curated entries have vectors. A job embeds anything new every minute.
- The raw layer is live: `brain.documents` and `brain.chunks`. Search across both layers is `brain.search_all`. The rules for it are in `claude/Brain_Rule.md` section 7.
- Cleanup tags now hide non-content rows from search: 5 headings, 17 duplicates, 1 table dump, 12 labels. The words did not change.
- One raw document exists: "Gen and Genio sprint, 27 Oct 2026" (document 1, source 51). No gold was mined from it. Coach Gen judged it to be tech talk with no 5 Laws insight, so it was retired the same day (`status = 'retired'`). Its words are kept and it no longer shows in search.
- Removal test, rolled back: chunks can be deleted, documents and sources cannot (add-only lock). Retire with the new `status` column.

**Intake decision (Coach Gen, 27 Oct 2026).** Calls keep coming through this chat. Claude reads the call, removes the dirt (filler and junk sections such as family, money, shopping, unrelated talk), and stores only the kept sections as a document. Then it mines gold from them. A direct Fathom fetch that stores whole calls was rejected for now, because code cannot tell a Law 5 story from a shopping order, and the raw layer would fill with junk and private talk. It can come back only if a keep or drop sorting step is tested on a call Coach Gen knows well.

**Mining steps with the raw layer (to follow until the skill is saved)**
1. Source row first, as in Brain_Rule section 4.
2. Clean the transcript. Keep each chunk's start time and link.
3. Cut out junk sections. Write what was cut in `left_out` and the document's `notes`.
4. Store the kept sections in `brain.documents`, then call `brain.chunk_document(<document id>)`. The embed job does the rest.
5. Mine the gold from the kept text into `brain.entries`, as in section 4.
6. Close the source's `passes`.

**To-dos from sprints.** The `extract-fathom` card now includes a rule: every to-do or "I want to" Coach Gen says in a sprint with Genio goes straight onto the task list and into `Master_Project_Status.md` under that sprint, with 1 to 3 suggested next steps. The card was shown to him and is not yet saved. It does not yet include the raw layer steps above.

**Still open**
- Save the `extract-fathom` card, then add the raw layer steps to it.
- Skill cards not yet proposed: `coach-gen-writer`, `inside-the-introvert`, `lasting-change-letters`. `write-book-from-material` was shown and is not yet saved.
- Tuning: chunk size and overlap, a one-line context for each chunk, a golden set of 10 to 20 of his real questions, small against large embedding model.
- Phone video: he will use Google Drive and Cowork. ffmpeg exists on his Mac. Whisper is not installed, and the Mac shell had no internet, so the transcription route is undecided.
- A Fathom API key is only needed if the direct fetch comes back.
- The full pipeline, with built and not built marked, is in `Brain_Pipeline_Manifesto.md` (sent to him in chat, not yet in the project).

---

## Handoff, 27 Oct 2026, 16:50: for the next chat

**Start here.** Continue the brain build from the blockers below. Coach Gen is frustrated by long answers and by options. Answer his question first, in plain words, with no unasked options. He is the expert on his own material. Do not assume what he wants. When he asks for understanding, explain before acting.

**Where things live**
- Rule for all chats: `claude/Brain_Rule.md` (section 7 is the raw layer and search).
- Plan and status: `claude/Brain_RAG_Plan.md` (status update at the bottom).
- Full pipeline with built and not built marked, the decision of 27 Oct 16:46, and 18 risks: `Brain_Pipeline_Manifesto.md`. It is a chat file only. It was not added to the project because Guardrails says to ask before creating a new project doc. Ask him if it should go in.
- Schema, migrations 004 to 008: GitHub `coachwibawa/Coach-Gen-Brain` (`SCHEMA.md`, `migrations/`). Pushed 27 Oct.
- Supabase project `zjedqjiuxkoncwsmylls`. OpenAI key is in Supabase Vault as `openai_api_key`.
- Mac folder (when linked): `/Users/coachwibawa/Documents/5 Laws of Lasting Change`.

**Done today (beyond the sections above)**
- Migration 008: `documents.status` and `retired_note`; `search_all` skips retired documents; document 1 retired.
- Updated additively: `Brain_Rule.md` (new section 7), `Brain_Mining_Handoff.md`, `Brain_RAG_Plan.md`.
- `extract-fathom` card with the sprint to-do rule shown to him, not saved.

**Blockers**
1. Mac link is down. The linked computer failed to connect (error 502) in the last turn. Until it returns, nothing can run on his Mac. This blocks: the frozen notice on three Mac files (`build_worksheet.js`, `Testimony_Mastertext_Collection.md`, `Book/build/book-map/new_material.md`), the phone video, ffmpeg audio extraction and any Whisper install. He says he will use Google Drive and Cowork for the video. Ask him to reopen this task in the Claude desktop app.
2. He has not saved the skill cards. Only he can save them from the card. Pending: `extract-fathom`, `write-book-from-material`. Not yet proposed: `coach-gen-writer` (edited copy exists in the old session scratchpad and may be gone), `inside-the-introvert`, `lasting-change-letters`. A proposal needs the original SKILL.md read in full first.
3. Tuning needs his 10 to 20 real questions for the golden set.
4. Phone video transcription route is undecided: local Whisper, OpenAI transcription (about 25 MB file limit), or a Mac app.
5. A direct Fathom fetch needs his Fathom API key. It is off by his decision, so this is not a blocker unless he reopens it.

**Next, in order**
1. Check the Mac link. If it is back, add the frozen notice to the three Mac files and, if the video is in Drive or the folder, extract the audio with ffmpeg.
2. Ask him to save the `extract-fathom` card. Then propose a revised card that adds the raw layer steps from the update above. Then do the remaining cards, up to 3 per proposal.
3. Collect his 10 to 20 real questions. Run them through `search_all` with `layers = 'gold'` and with `'both'`. Show results as a table of question, top hits, and whether he judges them right.
4. Test a one-line context for each chunk, chunk size, and small against large embedding model on that set.
5. Mine the next unmined Fathom calls (none after 26 Oct yet) with the intake rule: Claude cuts the junk, stores kept sections, mines gold.
6. Build the `retrieve` and `check-said` skills after the tuning. Writing chats search gold only (Claude proposal, ask him to confirm).
7. Open naming: Wayan's print name, Pak Jeffrey.
8. Missing risk fixes, if he wants them: a check that each entry's text appears word for word in the stored document, progress tracking in `passes`, an alert if the embed job stops.

**Rules for this work**
- Calls come through Claude. No direct Fathom fetch and no storing of whole calls unfiltered.
- Never delete. Documents and sources are add-only. Retire with `status`.
- Never touch the Project Rebirth Supabase projects.
- Never print anything with status `never use`.
- No em dashes and no semicolons in his documents.
- Destructive actions go last and need his approval.

**Suggested skills**
- `extract-fathom` for any Fathom call.
- `wait-what` only when he types it.
- `grilling` if he wants a decision stress-tested.
- `handoff` at the end of each session.

---

## CORRECTION, 27 Oct 2026, 16:58 (Coach Gen challenged the blockers above, and he was right)

The Blockers and Next list in the 16:50 handoff contained claims I had not checked. Wrong lines are kept above on purpose. This block replaces them.

1. WRONG: "He has not saved the skill cards." Checked the installed skills. `extract-fathom` already has the Supabase brain steps and section 8 "To-dos from sprints", so that card is saved. `write-book-from-material` already reads and writes the brain, so that card is saved too. The same wrong claim appears in "Still open" and "Done today" above. It is not a blocker.
2. WRONG: "frozen notice on three Mac files" as pending. The earlier session record says those notices were added. The Mac link is down, so this was not re-checked.
3. NOT A BLOCKER: the Mac link. It dropped during this session (502), and nothing he asked for in the last hour needs it. It only matters again for the phone video.
4. NOT A BLOCKER: phone video transcription route. He said he will use Google Drive and Cowork. The route question comes up only when he has the video ready.
5. NOT A BLOCKER: the golden-set questions. Tuning is optional work, not something he is waiting on.
6. REAL, small: `coach-gen-writer`, `inside-the-introvert` and `lasting-change-letters` still have no brain steps (checked: they do not mention the brain). That is Claude's job to propose. He did not ignore anything.
7. STILL TRUE: the revised `extract-fathom` card should add the raw layer steps (store kept sections in `brain.documents`, then `chunk_document`). Not done yet.

So the real state: nothing is blocked on Coach Gen. What remains is Claude's work: the three skill cards, the raw layer steps in `extract-fathom`, and the tuning.
