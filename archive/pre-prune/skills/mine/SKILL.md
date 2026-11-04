---
name: "mine"
description: "Put anything Coach Gen gives (pasted text, voice dump, video, mp3, pdf, link, Fathom call) into the Coach Gen Brain. Use for /mine plus the material."
---

# /mine

Coach Gen gives you anything. You put it in the Coach Gen Brain (Supabase project `zjedqjiuxkoncwsmylls`, schema `brain`). He never says where it goes. Every writing chat reads the brain, so nothing needs routing.

Do not ask for confirmation of anything he already approved. Do not yap. Do not offer options when one route works. Stop and ask only when the input is truly ambiguous, or when every route for a step has failed.

Read `claude/Brain_Rule.md` first. It is the one rule for all material. If this skill and that file differ, that file wins.

## 0. Route by what he gave

- A Fathom link, a Fathom call, a client or date that points to a Fathom call: run `/extract-fathom` with the same argument. It has the Fathom steps. Do not copy them here.
- Pasted text, a chat thought, a voice dump already as text: go to step 1.
- A file on his Mac (video, mp3, m4a, wav, pdf, docx, txt, md): find it yourself. If the folder is not connected, request access with `device_request_folder_access` right away (Downloads, Desktop and Documents all need a grant). Do not ask him first. Then go to step 1 and step 2.
- A Google Drive file or doc: read it with the Drive connector (`read_file_content`), then go to step 3. A large video cannot be downloaded this way. Look for the same file in his Mac folders instead.
- A web link: `WebFetch` for the text, then go to step 3. A video page usually gives no transcript. Say so in one line and ask for the file.
- A Notion page: read it with the Notion connector, then go to step 3.
- Nothing attached: ask what to mine and wait.

## 1. Source first, no repeats

Look for it in `brain.sources` (by title or url) and `brain.documents`. If it is there, read `passes` and say what was already mined. Skip it unless he asked for a re-mine. If it is new, insert the source row (title, kind, url, happened_on, participants). Look up people in `brain.people` by real name. Add anyone new with role and consent.

Also search the project docs (`project_search` with the file name or topic). A video may already have an edit plan with a known transcript, Whisper fixes and third parties to cut. Use it.

## 2. Get text out of audio and video

Only for audio and video files. Do these steps in order and do not ask him to choose a route.

1. If a transcript or captions file already exists for it, or the project docs hold one, use that and skip the rest of this step.
2. Pull the audio with ffmpeg through `device_bash`, mono, 16 kHz, 32k mp3, and write it next to the source file in the connected folder. The video itself is never uploaded. Check duration with ffprobe.
3. Bring the mp3 into the cloud workspace with `device_stage_files`. It lands in `/mnt/user-data/uploads/<folder>/`.
4. Transcribe in the cloud workspace, not on his Mac. His Mac shell has no internet and no Whisper, so never ask him to install anything there. The cloud workspace reaches pip and huggingface.co. Run `pip install --break-system-packages faster-whisper`, then use the `medium` model with `compute_type='int8'`. Decode the audio with `ffmpeg -f f32le -ac 1 -ar 16000` into a numpy float32 array and pass the array to `transcribe`. Opening the mp3 path directly fails on a library version mismatch. Force the language when you know it (`language='en'`). For mixed Indonesian and Japanese takes, transcribe once, split by pauses, and re-run each piece with its language forced. Use `vad_filter=True`. Keep each segment's start time. A 8 minute file takes about 2 to 3 minutes.
5. Whisper invents words over silence and garbles names. Check names against the project docs and `brain.people`. Apply confident fixes and write every fix, and every doubt, in the document's `notes`.
6. Only if the cloud workspace truly cannot run Whisper (install or model download refused), say so in one line, name what failed, and then ask for a transcript from another source.
7. Leave the extracted mp3 where it is and tell him its name so he can delete it.

## 3. Clean it with a script, not by reading

Do the mechanical work in code (python in Bash), not in the chat. This keeps tokens low.

- Take the timestamps out of the text. Keep each turn's start time so every chunk still links to the exact second.
- Remove filler that changes no meaning. Join consecutive turns by the same speaker. For PDFs, remove headers, footers and page numbers. Never reword.
- Flag cut candidates by keyword and by section: family, money, shopping, bookings, health details, unrelated chat, other people's speeches, moderators and hosts.

## 4. Cut the junk

Read only the flagged parts and short previews of the rest, not the whole text. Cut whole sections that are not his knowledge. A whole input is never stored unfiltered. Write what was cut, with the time or page ranges, in the source's `left_out` and the document's `notes`.

If you cannot tell whether a section is junk, keep it and list it in the document's `notes` for him.

A client's health or mental-health detail stays in the raw layer only, is noted in `notes` as never use in print and Reels, and is never picked as gold.

## 5. Store the kept text (raw layer)

1. Check the values already in use: `select distinct kind, owner from brain.documents;`.
2. Insert one row in `brain.documents`: `source_id`, `title`, `kind`, `owner`, `language`, `happened_on`, `url`, `turns`, `clean_text`, `notes`, `added_by` (`mine`). `owner` is `own` for his own words, `client` for a client, `peer` for a peer, `outside` for another author or creator. `turns` is a JSON list of objects shaped `{"s": seconds, "t": text, "sp": speaker}`. For text with no speakers, use one turn per paragraph. Use dollar quoting for long text.
3. Run `select brain.chunk_document(<document id>);`. A job embeds the new chunks within a minute. Check that the chunk count is more than 0.
4. If he later says a document is junk, retire it: `update brain.documents set status = 'retired', retired_note = '<why and when>' where id = <id>;`. Documents and sources are never deleted.

### 5b. Long texts (books, long PDFs, anything over about 20,000 words): load through GitHub, never through the chat

Typing a whole book into `execute_sql` costs about 350,000 tokens and two hours. Supabase can pull the file itself (migration 015). Use this route:

1. Parse the PDF with the universal parser in the repo clone (`coachwibawa/Coach-Gen-Brain`), not a hand-made one (added 31 Oct 2026):
   a. `python3 tools/parse_book.py book.pdf --profile`. Read the report (page map, style table with samples, chapter candidates, contents page). If it says the PDF is scanned, stop and tell him.
   b. Write `books/<name>.json` from the report: `keep_pages`, `styles` (map each font and size to body, heading, chapter, part, figure or skip), `chapters` (list of `[pdf page, label]`), `parts`, and any of `chapter_line_re`, `drop_lines`, `speakers`, `front_label`. The keys are in `books/README.md`. Dialogue books use `speakers`.
   c. `python3 tools/parse_book.py book.pdf books/<name>.json turns.json`. Read the printed checks: NO TEXT LOST must say OK, then the flags, unmapped styles and PAGES TO LOOK AT. Read only those pages (layout text of that page, `pdftotext -layout -f N -l N`). Change the settings and run again until the flags are empty or each one is explained. If a book needs a trick the parser lacks, add it to the parser as a new optional settings key, never as book-specific code. If you changed the parser, run `tests/check_expected.py` on every test book whose PDF is attached (keys in `tests/expected/`), and add a key for the new book.
   d. Cut what is not the author's text (front matter, notes, index, ads) with `keep_pages`, and write what was cut in `left_out`.
   The output is `turns.json`: a list of `{"s": PDF page, "t": paragraph, "ch": chapter label, "sec": section label, "k": kind}`. Section headings are their own turns.
2. Write `meta.json`: `context_prefix` ("<Book> by <Author> (<year>), outside voice."), `speaker`, `title_prefix`, `notes` (what each turn is, what was cut), `added_by` `mine`. If the source already exists (books often do, from an earlier full read), use `source_id` and add `"pass"` (what this pass covered, with the date) and `"left_out_add"` (the cut pages). The load appends both to the source itself (migration 018), so no UPDATE and no "say go" step is needed. For a new source, use a `source` object with title, kind, participants, passes, left_out, notes.
3. In the repo clone: `mkdir -p loads && python3 tools/build_load.py turns.json loads/<name>.json meta.json`. Keep the printed md5 values.
4. `tools/push_load.sh loads/<name>.json`. It commits and pushes the load file to main and prints the SQL.
5. Run the printed `select * from brain.load_from_github('loads/<name>.json');` once. It inserts every document and chunk and records the pass, and returns an md5 per document. Compare them with the printed ones.
6. `tools/drop_load.sh <name>`. It removes the load file from main (it holds copyrighted text) and pushes. Do not try a throwaway branch: branch deletion and force-push are blocked from the Claude workspace.
7. Check that all chunks get embedded (about 25 a minute, `count(*) where embedding is null` for that source). Wait with a background sleep, not by polling.
8. Spot-check `brain.search_voices('<a core idea of the book>', 'outside', 0, 3)` with 3 or 4 of the book's main ideas. Then rerun the 31 test questions in `claude/Brain_Test_Set.md` and add a run (Brain_Rule section 10). Run them in batches of about 15 per SQL call, or the call times out.

The slow way (typing text into `execute_sql`) is only for short inputs, such as a call section, a voice dump or a post.

Pick the model by `/pick-model`: cleaning and checking need judgment, the load itself is one SQL call.

## 6. Pick the gold

Only from the kept text, and only from his own words or his clients' words.

- Outside material (another author, a talk, a creator): store it in the raw layer with `owner = 'outside'` and stop there. Pick lines into `brain.entries` only if he asks. Then use type `outside voice`, the real speaker, and never let it be mistaken for his.
- Own material: follow the gold bar and the tagging in `/extract-fathom` sections 4 and 5. Vivid, in his or the client's words, maps cleanly to one Law and type, not already in the brain. Check first with `select * from brain.search_all('<the idea in plain words>', 10, null, null, 0.3, 'gold');` and skip what is already there. Fewer strong notes beat many weak ones.
- Entries are verbatim. Follow section 4 of `claude/Brain_Rule.md`. Fill `added_by` with `mine`. Mark anything on the NEVER USE list with status `never use`. Never delete or reword. To fix an entry, add a new one with `corrects_id`.
- Use only values from `brain.entry_types`, `brain.projects` and `brain.tags`. Law 0 is the whole book or Intro.
- For long input such as a book, work in windows and append the range done to `passes` after each window, so a stop halfway never means mining it twice.

## 7. Close the source

Append to the source's `passes` (a text array, so use `passes || array['...']`) what this pass covered and today's date. Put anything left out on purpose in `left_out`.

An `update` triggers a Supabase approval prompt that times out if he is away. Batch all updates into one statement, tell him in one line what it does, ask him to say go, and run it the moment he says go. For a new source, write `passes` and `left_out` in the insert instead, so no update is needed. For a book loaded through 5b, the load already recorded the pass, so skip this step.

## 8. To-dos

If he is talking about plans, to-dos or things he wants to do (a sprint, a voice dump, a walk-and-talk), follow section 8 of `/extract-fathom`: straight onto the task list and into `Master_Project_Status.md`, add-only, with 1 to 3 suggested next steps. To-dos are not brain entries.

## 9. Report in chat

Short. One line on the raw layer: document id, number of chunks, what was cut. Then one line per entry:

**Law N, type:** "the exact text written" (link or timestamp). Why: one plain sentence.

Then what was left out of gold and why, then anything unchecked (doubtful Whisper words, approximate times), then the numbered to-dos with next steps, if there were any. End with one line on anything good you left out that fits better elsewhere. No reflective commentary.

## Rules that do not change

- Calls and files come through you. There is no direct Fathom fetch and no storing of whole inputs unfiltered.
- Verbatim stays verbatim. Turning it into writing is the writing chats' job.
- Nothing is deleted. Retire or correct by adding.
- Never touch the Project Rebirth Supabase projects.
- If the Supabase connector is not available, say so in one line. Do not mine into a file instead.
- `execute_sql` returns only the result of the last statement. Run checks as separate calls.
- No em dashes and no semicolons in anything you write for him.