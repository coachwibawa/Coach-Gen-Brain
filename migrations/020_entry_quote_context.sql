-- 020_entry_quote_context.sql (Rules Refactor Plan, the mining change agreed 5 Nov 2026)
-- "Never reword" becomes a storage rule only: entries.text keeps the exact words (already frozen).
-- So a quote can be rebuilt later under "A quote earns its marks", each entry may also keep:
--   answers      what the line answered (the question or prompt it responds to)
--   context      one line of session context a cold reader would need
--   owned_words  the words the person owns (their image, their signature phrase), never dropped
-- Each person's records are already linked through speaker_id and about_id (brain.people).
-- New columns only. Nothing is dropped or rewritten. Changes are logged by the existing entries_log trigger.
-- The mine skill starts filling these in Phase 4.

alter table brain.entries
  add column answers text,
  add column context text,
  add column owned_words text[] not null default '{}';

comment on column brain.entries.answers is 'What the line answered: the question or prompt it responds to';
comment on column brain.entries.context is 'One line of session context a cold reader would need';
comment on column brain.entries.owned_words is 'Words the person owns (their image, their signature phrase). Never dropped from a quote';

create or replace view brain.entries_full with (security_invoker = true) as
select
  e.id,
  e.legacy_ref,
  e.project,
  e.law,
  e.type,
  e.tags,
  e.text,
  e.original_text,
  e.original_language,
  sp.real_name as speaker,
  ab.real_name as about,
  e.certainty,
  e.origin,
  e.said_on,
  s.title as source,
  s.kind as source_kind,
  e.link,
  e.importance,
  e.status,
  e.note,
  e.extra,
  e.corrects_id,
  e.added_by,
  e.added_at,
  (select count(*) from brain.used_in u where u.entry_id = e.id) as times_used,
  e.answers,
  e.context,
  e.owned_words
from brain.entries e
left join brain.people sp on sp.id = e.speaker_id
left join brain.people ab on ab.id = e.about_id
left join brain.sources s on s.id = e.source_id;

revoke all on brain.entries_full from public, anon, authenticated;
