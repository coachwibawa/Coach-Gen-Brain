-- 024: the private layer (17 Nov 2026, Coach Gen's go)
--
-- Why: he wants every call mined in full, sensitive parts included
-- (family, money, health, third people's private stories), without
-- those parts reaching a writing chat. Business needs may later allow
-- their use, so nothing is cut and a private row can be released later
-- by changing its status (logged in brain.change_log).
--
-- What:
-- 1. documents.status gets 'private'. search_all and search_voices only
--    serve chunks of 'active' documents, so private chunks are skipped
--    with no change to either function. Chunks are still cut and
--    embedded, so a release needs no rebuild.
-- 2. entries.status gets 'private'. brain.entries_full (what writing
--    chats and both search functions read) leaves private entries out.
-- 3. brain.entries_private: the same columns, private entries only.
--    Read it only when Coach Gen asks for private material by name.
-- Nothing is dropped. Only check constraints are replaced.

begin;

alter table brain.documents drop constraint documents_status_check;
alter table brain.documents add constraint documents_status_check
  check (status = any (array['active','retired','private']));

alter table brain.entries drop constraint entries_status_check;
alter table brain.entries add constraint entries_status_check
  check (status = any (array['raw','printable','placed','never use','retired','private']));

create or replace view brain.entries_full as
 select e.id, e.legacy_ref, e.project, e.law, e.type, e.tags, e.text,
    e.original_text, e.original_language,
    sp.real_name as speaker, ab.real_name as about,
    e.certainty, e.origin, e.said_on,
    s.title as source, s.kind as source_kind,
    e.link, e.importance, e.status, e.note, e.extra, e.corrects_id,
    e.added_by, e.added_at,
    (select count(*) from brain.used_in u where u.entry_id = e.id) as times_used,
    e.answers, e.context, e.owned_words
   from brain.entries e
     left join brain.people sp on sp.id = e.speaker_id
     left join brain.people ab on ab.id = e.about_id
     left join brain.sources s on s.id = e.source_id
  where e.status <> 'private';

create or replace view brain.entries_private as
 select e.id, e.legacy_ref, e.project, e.law, e.type, e.tags, e.text,
    e.original_text, e.original_language,
    sp.real_name as speaker, ab.real_name as about,
    e.certainty, e.origin, e.said_on,
    s.title as source, s.kind as source_kind,
    e.link, e.importance, e.status, e.note, e.extra, e.corrects_id,
    e.added_by, e.added_at,
    (select count(*) from brain.used_in u where u.entry_id = e.id) as times_used,
    e.answers, e.context, e.owned_words
   from brain.entries e
     left join brain.people sp on sp.id = e.speaker_id
     left join brain.people ab on ab.id = e.about_id
     left join brain.sources s on s.id = e.source_id
  where e.status = 'private';

comment on view brain.entries_private is
  'Private entries only (migration 024). Read only when Coach Gen asks for private material by name. Never served by search, never printed.';

commit;
