-- Coach Gen Brain, migration 002: pin search_path on every brain function
-- (Supabase security advisor: function_search_path_mutable).

alter function brain.check_tags() set search_path = brain, pg_catalog;
alter function brain.freeze_entry_columns() set search_path = brain, pg_catalog;
alter function brain.check_minor_once() set search_path = brain, pg_catalog;
alter function brain.check_persona_work() set search_path = brain, pg_catalog;
alter function brain.log_change() set search_path = brain, pg_catalog;
alter function brain.block_delete() set search_path = brain, pg_catalog;
alter function brain.block_truncate() set search_path = brain, pg_catalog;
alter function brain.block_update() set search_path = brain, pg_catalog;
