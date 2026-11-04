---
name: "extract-fathom"
description: "Mine Coach Gen's Fathom calls for 5 Laws material and write it into the Coach Gen Brain (Supabase). Use for /extract-fathom with a client name, date, 'recent', 'everything', a link or a topic."
---

# /extract-fathom

Pull one or more Fathom calls, pick only the gold for the 5 Laws of Lasting Change, write it into the Coach Gen Brain (Supabase project `zjedqjiuxkoncwsmylls`, schema `brain`) as verbatim entries, then print in chat what was written and why. No PDF is sent. Coach Gen does not read it.

Do not ask for confirmation of anything Coach Gen already approved. Do not yap. Only stop and ask when the arguments are truly ambiguous (for example, two clients with the same first name).

## 1. Read the arguments (flexible)

The argument is free text. Resolve it with the Fathom connector tools (load them with ToolSearch "+Fathom" if deferred):

- A Fathom link: `get_recording_by_url`.
- A bare number: `get_recording_by_call_id`. If not found, try it as a recording_id.
- A client or person name (Kin, Sri, Asep, Wayan, Genio, "my brother"): `list_meetings` and match titles first ("Kin 3rd Session", "Genison Sprint" = brother call). Fall back to `find_person` with recorded_by "anyone".
- A date, range or relative date ("Oct 5", "last week", "September"): `list_meetings` with created_after / created_before.
- "recent", "latest" or no argument: the newest calls that are not yet in `brain.sources`.
- "everything" / "all": every call not yet in `brain.sources`, oldest first, at most 3 transcripts per turn. Say how many are left and continue next turn.
- A topic or phrase ("fish", "Law 5", "gave up"): `find_relevant_meetings` with recorded_by "anyone" and the user's request as user_question, then pull only the matching parts.
- Mixed ("Sri, September"): combine filters.

If the user's wording is loose, pick the best match, name it in one line, and go.

## 2. Skip what is already done

Read `claude/Brain_Rule.md` first. It is the one rule for all material. Then look the call up in `brain.sources` (by url or title) and read its `passes`. Skip calls already mined unless the user named that call directly or asked for a re-mine. Check `brain.entries` for the same `source_id` and `link` before adding anything, so nothing is added twice. To check whether an idea is already in the brain, search gold only: `select * from brain.search_all('<the idea in plain words>', 10, null, null, 0.3, 'gold');`.

## 3. Pull and read

`get_meeting_transcript` with the recording_id AND the url, so every segment has a timestamp link. Max 3 transcripts per turn. Never quote or summarise a call from memory. Ground every line in the transcript. A long transcript is saved to a file: parse it in code into a compact read file (number, time, full speaker name, text) and read that, not the raw tool output.

## 3b. Clean it and store the kept text (the raw layer)

Coach Gen decided this on 27 Oct 2026: calls come through Claude, Claude cuts the junk, and only the kept text is stored. A whole call is never stored unfiltered. There is no direct Fathom fetch. Every call gets this step, Genio sprints included (confirmed 2 Nov 2026: consistency matters more than the token cost).

1. Clean the transcript. Take the timestamps out of the text but keep each turn's start time, so every chunk still links to the exact second. Remove filler that changes no meaning. Join consecutive turns by the same speaker. Never reword.
2. Cut the junk sections: family and money talk, shopping, bookings, unrelated chat, and anything that is not his knowledge. Write what was cut, with the time ranges, in the source's `left_out` and in the document's `notes`.
3. Insert one row in `brain.documents`: `source_id`, `title`, `kind`, `owner` (`own` for his own words), `language`, `happened_on`, `url`, `turns`, `clean_text`, `notes`, `added_by` (`extract-fathom`). Copy the exact shape of the `turns` column of document 1. If a document for this source already exists, do not add another. After the insert, compare the md5 of the stored turn texts with the md5 of the local file.
4. Run `select brain.chunk_document(<document id>);`. A job embeds the new chunks within a minute. Check that the chunk count is more than 0.
5. Skip steps 1 to 4 only if Coach Gen says gold only for this call.
6. If Coach Gen later says a document is junk, retire it: `update brain.documents set status = 'retired', retired_note = '<why and when>' where id = <id>;`. Documents and sources are never deleted.

Then pick the gold from the kept text only.

## 4. Pick the gold

Keep only:
- Framework material: anything that explains, illustrates or sharpens a Law, its exercise, its misconceptions, misexecutions, sequence, or what happens if skipped.
- Coach Gen's own metaphors, stories and examples (fish, Shinkansen, kodawari, hunter-gatherer vs farmer, misogi).
- Client moments: a client's own words showing a stuck point, a shift or proof.
- In Genio calls: Genio's analogies and metaphors too (he is a software engineer). Store them as type `metaphor`, speaker Genio, and say in the note that they suit writing and stories for software engineers (added 2 Nov 2026).

Skip: small talk, games, family, health details, money figures, tools and pricing chat, plans that are not about the framework. If Coach Gen says "everything else is garbage", trust it.

Bar for gold: vivid, in his or the client's own words, maps cleanly to one Law and type, and is not already in the brain. Fewer strong notes beat many weak ones. Do not overfit a set of notes to one aspect. If a call has no gold, write no entries. This often happens in Genio calls. The raw layer and the to-dos still go in.

## 5. Tag each piece

Each entry gets: project, law (0 = whole book or Intro), type, tags, speaker, about, certainty, said_on, importance, note (why it matters and where it fits). Lists are fixed: projects, types and tags come from `brain.projects`, `brain.entry_types` and `brain.tags`. An unknown value is refused. Law terms: 1 Reset (True Desire), 2 Reframe (New Possibilities), 3 Resolve (Consistent Effort), 4 Reap (Momentum Engine), 5 Relax (Effortless Result). Law 3/4/5 = do it / tune it / trust it.

## 6. Write to the brain (add-only)

Use `execute_sql` on project `zjedqjiuxkoncwsmylls`. Follow section 4 of `claude/Brain_Rule.md`:

1. Source first: insert the call into `brain.sources` if it is not there (title, kind, url, happened_on, participants). Pick the gold before this insert, so `passes` (with the final entry count) and `left_out` can go in the same insert and no UPDATE is needed later.
2. People: look up `brain.people` by real name. Add anyone new with role and consent.
3. The entry, verbatim: `text` holds the words as said. Remove only filler that changes no meaning, never reword. For Indonesian, put the original in `original_text` with `original_language = 'id'`, the English in `text`, `origin = 'translated'`. `link` is the timestamp link. Never invent a quote. Fathom speaker labels are often wrong: check who said a line by its content before you set `speaker_id`.
4. Connections: add a row to `brain.connections` when a piece pairs with, mirrors, answers or backs up another.
5. Mark anything on the NEVER USE list (money figures, health details, religious lines, organisation or club names, a third person's private story) with status `never use`. It is stored, never printed.
6. Fill `added_by` with `extract-fathom`.
7. Never delete, truncate or drop. To fix an entry, add a new one with `corrects_id`.

Wording stays his. Turning verbatim into writing is the writing chats' job. No em dashes and no semicolons in anything you write for him.

If the Supabase connector is not available, say so in one line. Do not mine into any file instead.

## 7. Close the source

Append to the source's `passes` what this pass covered and today's date. Put anything left out on purpose in `left_out`. For a new source this is already in the insert (section 6.1).

## 8. To-dos from sprints (Genison Sprint and any call with Genio)

In sprint calls Coach Gen often says things that are to-dos, or hints that he wants to do something ("I should", "I want to", "let's try", "can you put that on the list", "I need to look into"). Catch every one while reading the transcript. Do not wait to be asked.

- Put each one straight onto the to-do list. Add it to the chat task list and append it, add-only, to `Master_Project_Status.md` under a heading for that sprint (title, date, link). Do not condense or remove earlier items. To edit that doc without retyping it, take the exact text from the `project_read` result, insert the new section in code, and write it back from a file in the working directory with `local_path`.
- Each item: the action in one plain line, the timestamp link, and the exact words he said when they are short.
- Under each item add 1 to 3 suggested next steps. Make them concrete and doable, for example "research X and report back", "draft the spec for Y", "ask Z". Mark anything Claude can start right now.
- Keep family and personal items, health and money figures out of the project doc. Mention them in chat only if he asked.
- If an item is already on the list, do not add it twice. Tell him it is already there.
- Do not mix this with the gold entries. To-dos are not brain entries.

## 9. Report in chat

One short block per call: title, date, link. One line on the raw layer: document id, number of chunks, and what was cut. Then one line per entry:

**Law N, type:** "the exact text written" ([mm:ss](timestamp link)). Why: one plain sentence.

Then, for sprints, a short numbered list of the to-dos found, each with its suggested next steps.

End with one line on anything good you deliberately left out, only if it fits better somewhere else (book, article, sales page). No reflective commentary.