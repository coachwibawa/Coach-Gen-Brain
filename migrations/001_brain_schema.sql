-- Coach Gen Brain, migration 001: schema, lists, add-only lock, history, privacy.
-- Everything lives in its own schema "brain", which the public API does not expose.

create schema if not exists brain;

-- ============================================================
-- Fixed lists (add new values on purpose, never delete)
-- ============================================================

create table brain.projects (
  name text primary key,
  note text,
  added_at timestamptz not null default now()
);

create table brain.entry_types (
  name text primary key,
  note text,
  added_at timestamptz not null default now()
);

create table brain.tags (
  name text primary key,
  note text,
  added_at timestamptz not null default now()
);

insert into brain.projects (name, note) values
  ('5 Laws of Lasting Change', 'The framework, the book, the workbook'),
  ('Introverts', 'Introvert niche knowledge'),
  ('Body Language', '6 Pillars of Body Language'),
  ('General', 'Coach Gen material that fits no single project');

insert into brain.entry_types (name, note) values
  ('own story', 'Something that happened to Gen'),
  ('client story', 'Something that happened to a client'),
  ('client words', 'A client describing a step: how it felt, where they got stuck (Testimony rule 10)'),
  ('testimony', 'A client verdict on a whole Law, before and after (Testimony rule 10)'),
  ('coach line', 'Gen speaking as coach'),
  ('outside voice', 'A book, study or person outside Gen and his clients'),
  ('idea', 'A concept or argument'),
  ('metaphor', 'An image or comparison'),
  ('tool', 'An exercise or method');

insert into brain.tags (name, note) values
  ('fit', 'The person names the problem the book solves'),
  ('before-after', 'A shift, before and after'),
  ('small win', 'A checkable win with no numbers'),
  ('honest partial', 'A half-finished, honest result'),
  ('works alone', 'Used the tool without the coach'),
  ('doubt', 'A reader-style doubt'),
  ('mechanism', 'Explains why it works'),
  ('identity', 'A who-I-am shift'),
  ('stuck symptom', 'Worksheet field: Stuck Symptoms'),
  ('misconception', 'Worksheet field: Misconceptions'),
  ('misexecution', 'Worksheet field: Common Misexecutions'),
  ('hidden reward', 'Worksheet field: Hidden Reward (what the old pattern protects)'),
  ('resource', 'Worksheet field: Resources'),
  ('coined term', 'Worksheet field: Coined Term'),
  ('core exercise', 'Worksheet field: Core Exercise'),
  ('dod', 'Worksheet field: DoD'),
  ('sequence trigger', 'Worksheet field: Sequence Trigger'),
  ('why this position', 'Worksheet field: Why This Position'),
  ('opening quote', 'Worksheet field: Opening Quote'),
  ('what happens if skipped', 'Worksheet field: What Happens If Skipped'),
  ('timeframe anchor', 'Worksheet field: Timeframe Anchor'),
  ('introvert', 'Introvert-specific material');

-- ============================================================
-- People (consent lives here)
-- ============================================================

create table brain.people (
  id bigint generated always as identity primary key,
  real_name text not null unique,
  role text not null check (role in ('self','client','peer','coach','family','friend','outside author','other')),
  consent text not null default 'not asked' check (consent in ('given','pending','not asked','refused','not needed')),
  notes text,
  added_by text,
  added_at timestamptz not null default now()
);

-- ============================================================
-- Sources (one row per call, video, podcast, book, article, dump)
-- ============================================================

create table brain.sources (
  id bigint generated always as identity primary key,
  title text not null,
  kind text not null check (kind in ('fathom call','video','podcast','article','book','voice dump','own published','note','chat','other')),
  url text,
  happened_on date,
  participants text,
  passes text[] not null default '{}',
  left_out text,
  notes text,
  added_by text,
  added_at timestamptz not null default now()
);

-- ============================================================
-- Entries (one row per mined piece)
-- ============================================================

create table brain.entries (
  id bigint generated always as identity primary key,
  legacy_ref text unique,
  project text not null references brain.projects(name),
  law smallint check (law between 0 and 5),
  type text not null references brain.entry_types(name),
  tags text[] not null default '{}',
  text text not null,
  original_text text,
  original_language text,
  speaker_id bigint references brain.people(id),
  about_id bigint references brain.people(id),
  certainty text not null check (certainty in ('recorded','recounted','built')),
  origin text not null default 'verbatim' check (origin in ('verbatim','translated','joined','shortened','built')),
  said_on date,
  source_id bigint references brain.sources(id),
  link text,
  importance text not null default 'minor' check (importance in ('core','major','minor')),
  status text not null default 'raw' check (status in ('raw','printable','placed','never use','retired')),
  note text,
  extra jsonb not null default '{}'::jsonb,
  corrects_id bigint references brain.entries(id),
  added_by text,
  added_at timestamptz not null default now(),
  search tsvector generated always as (
    to_tsvector('simple', coalesce(text,'') || ' ' || coalesce(original_text,'') || ' ' || coalesce(note,''))
  ) stored
);

create index entries_search_idx on brain.entries using gin (search);
create index entries_project_law_idx on brain.entries (project, law, said_on);
create index entries_source_link_idx on brain.entries (source_id, link);
create index entries_tags_idx on brain.entries using gin (tags);

-- Tags must come from the fixed list
create function brain.check_tags() returns trigger language plpgsql as $$
declare bad text;
begin
  select t into bad from unnest(new.tags) t
  where not exists (select 1 from brain.tags g where g.name = t) limit 1;
  if bad is not null then
    raise exception 'Unknown tag "%". Add it to brain.tags on purpose first.', bad;
  end if;
  return new;
end $$;

create trigger entries_check_tags before insert or update of tags on brain.entries
  for each row execute function brain.check_tags();

-- Frozen columns: text, speaker, source, link, date said (and the technical ones)
create function brain.freeze_entry_columns() returns trigger language plpgsql as $$
begin
  if new.text is distinct from old.text
     or new.original_text is distinct from old.original_text
     or new.original_language is distinct from old.original_language
     or new.speaker_id is distinct from old.speaker_id
     or new.source_id is distinct from old.source_id
     or new.link is distinct from old.link
     or new.said_on is distinct from old.said_on
     or new.legacy_ref is distinct from old.legacy_ref
     or new.corrects_id is distinct from old.corrects_id
     or new.added_by is distinct from old.added_by
     or new.added_at is distinct from old.added_at then
    raise exception 'Add-only: text, speaker, source, link and date said can never change. Add a new entry with corrects_id pointing to entry %.', old.id;
  end if;
  return new;
end $$;

create trigger entries_freeze before update on brain.entries
  for each row execute function brain.freeze_entry_columns();

-- ============================================================
-- Connections (replaces Obsidian links)
-- ============================================================

create table brain.connections (
  id bigint generated always as identity primary key,
  from_id bigint not null references brain.entries(id),
  to_id bigint not null references brain.entries(id),
  relation text not null check (relation in ('pairs with','before after','backs up','mirrors','answers','same idea','contradicts','part of')),
  note text,
  added_by text,
  added_at timestamptz not null default now(),
  check (from_id <> to_id),
  unique (from_id, to_id, relation)
);

-- ============================================================
-- Works, personas, used in
-- ============================================================

create table brain.works (
  id bigint generated always as identity primary key,
  title text not null unique,
  kind text not null check (kind in ('book','workbook','talk','article','article series','letter','reel','reel series','course','other')),
  status text,
  notes text,
  added_by text,
  added_at timestamptz not null default now()
);

create table brain.personas (
  id bigint generated always as identity primary key,
  work_id bigint not null references brain.works(id),
  name text not null,
  profile text,
  based_on text,
  added_by text,
  added_at timestamptz not null default now(),
  unique (work_id, name)
);

create table brain.used_in (
  id bigint generated always as identity primary key,
  entry_id bigint not null references brain.entries(id),
  work_id bigint not null references brain.works(id),
  location text,
  persona_id bigint references brain.personas(id),
  used_on date not null default current_date,
  note text,
  added_by text,
  added_at timestamptz not null default now()
);

create index used_in_entry_work_idx on brain.used_in (entry_id, work_id);

-- A minor entry may be used once per work. Core and major may repeat.
create function brain.check_minor_once() returns trigger language plpgsql as $$
declare imp text;
begin
  select importance into imp from brain.entries where id = new.entry_id;
  if imp = 'minor' and exists (
    select 1 from brain.used_in u
    where u.entry_id = new.entry_id and u.work_id = new.work_id and u.id <> coalesce(new.id, -1)
  ) then
    raise exception 'Entry % is minor and is already used in this work. Minor entries are used once per work.', new.entry_id;
  end if;
  return new;
end $$;

create trigger used_in_minor_once before insert or update of entry_id, work_id on brain.used_in
  for each row execute function brain.check_minor_once();

-- Persona must belong to the same work
create function brain.check_persona_work() returns trigger language plpgsql as $$
begin
  if new.persona_id is not null and not exists (
    select 1 from brain.personas p where p.id = new.persona_id and p.work_id = new.work_id
  ) then
    raise exception 'Persona % does not belong to work %.', new.persona_id, new.work_id;
  end if;
  return new;
end $$;

create trigger used_in_persona_work before insert or update on brain.used_in
  for each row execute function brain.check_persona_work();

-- ============================================================
-- History of every change
-- ============================================================

create table brain.change_log (
  id bigint generated always as identity primary key,
  table_name text not null,
  row_id bigint,
  old_row jsonb,
  new_row jsonb,
  changed_by text not null default current_user,
  changed_at timestamptz not null default now()
);

create function brain.log_change() returns trigger language plpgsql as $$
begin
  insert into brain.change_log (table_name, row_id, old_row, new_row)
  values (tg_table_name,
          (to_jsonb(new)->>'id')::bigint,
          to_jsonb(old) - 'search',
          to_jsonb(new) - 'search');
  return new;
end $$;

-- ============================================================
-- The add-only lock: no deletes, no emptying tables, on every table
-- ============================================================

create function brain.block_delete() returns trigger language plpgsql as $$
begin
  raise exception 'Add-only: nothing is ever deleted from brain.%. Retire it with a status or note instead.', tg_table_name;
end $$;

create function brain.block_truncate() returns trigger language plpgsql as $$
begin
  raise exception 'Add-only: brain.% can never be emptied.', tg_table_name;
end $$;

do $$
declare t text;
begin
  foreach t in array array['projects','entry_types','tags','people','sources','entries','connections','works','personas','used_in','change_log'] loop
    execute format('create trigger %I before delete on brain.%I for each row execute function brain.block_delete()', t || '_no_delete', t);
    execute format('create trigger %I before truncate on brain.%I for each statement execute function brain.block_truncate()', t || '_no_truncate', t);
    execute format('alter table brain.%I enable row level security', t);
    execute format('alter table brain.%I force row level security', t);
  end loop;
  foreach t in array array['projects','entry_types','tags','people','sources','entries','connections','works','personas','used_in'] loop
    execute format('create trigger %I after update on brain.%I for each row execute function brain.log_change()', t || '_log', t);
  end loop;
end $$;

-- The change log itself can never be edited
create function brain.block_update() returns trigger language plpgsql as $$
begin
  raise exception 'brain.% can never be edited.', tg_table_name;
end $$;

create trigger change_log_no_update before update on brain.change_log
  for each row execute function brain.block_update();

-- ============================================================
-- Privacy: no public access at all
-- ============================================================

revoke all on schema brain from public, anon, authenticated;
revoke all on all tables in schema brain from public, anon, authenticated;
revoke all on all functions in schema brain from public, anon, authenticated;
alter default privileges in schema brain revoke all on tables from public, anon, authenticated;
alter default privileges in schema brain revoke all on functions from public, anon, authenticated;

-- Admin role used by Claude's connector keeps full access through RLS bypass,
-- and a policy for the postgres role keeps FORCE RLS from locking the owner out.
do $$
declare t text;
begin
  foreach t in array array['projects','entry_types','tags','people','sources','entries','connections','works','personas','used_in','change_log'] loop
    execute format('create policy %I on brain.%I for all to postgres, service_role using (true) with check (true)', t || '_admin', t);
  end loop;
end $$;

-- ============================================================
-- The fixed window chats read through
-- ============================================================

create view brain.entries_full with (security_invoker = true) as
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
  (select count(*) from brain.used_in u where u.entry_id = e.id) as times_used
from brain.entries e
left join brain.people sp on sp.id = e.speaker_id
left join brain.people ab on ab.id = e.about_id
left join brain.sources s on s.id = e.source_id;

revoke all on brain.entries_full from public, anon, authenticated;
