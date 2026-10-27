-- Coach Gen Brain, migration 003
-- 1) certainty only applies to stories about people. Ideas, framework text and outside voices leave it blank.
alter table brain.entries alter column certainty drop not null;

-- 2) A private staging area for the one-time move-in. Rows are checked here before they enter the locked tables.
create schema if not exists staging;
create table staging.load (
  id bigint generated always as identity primary key,
  chunk int not null,
  rows jsonb not null,
  loaded_at timestamptz not null default now()
);
alter table staging.load enable row level security;
revoke all on schema staging from public, anon, authenticated;
revoke all on all tables in schema staging from public, anon, authenticated;
