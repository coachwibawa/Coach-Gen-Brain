-- 013 (2026-10-27): brain.health() for the daily silent-failure alert.
-- Returns one row per check: check, ok, detail. A daily scheduled task reads it and notifies Coach Gen when any row is not ok.
-- The key check calls OpenAI once (a few words, cost close to zero).

create or replace function brain.health()
returns table(check_name text, ok boolean, detail text)
language plpgsql security definer
set search_path to 'brain', 'extensions', 'public'
as $$
declare
  v_active boolean; v_last_ok timestamptz; v_failed int; v_missing_e int; v_missing_c int; v_vec extensions.vector; v_err text;
begin
  select bool_or(active) into v_active from cron.job where jobname = 'brain-embed';
  check_name := 'embed job is on'; ok := coalesce(v_active, false);
  detail := case when v_active is null then 'job brain-embed is missing' when v_active then 'active' else 'job brain-embed is switched off' end;
  return next;

  select max(d.end_time) into v_last_ok from cron.job_run_details d join cron.job j on j.jobid = d.jobid
   where j.jobname = 'brain-embed' and d.status = 'succeeded';
  check_name := 'embed job ran in the last 15 minutes'; ok := v_last_ok > now() - interval '15 minutes';
  ok := coalesce(ok, false);
  detail := 'last good run: ' || coalesce(to_char(v_last_ok at time zone 'Asia/Jakarta', 'YYYY-MM-DD HH24:MI') || ' Jakarta', 'never');
  return next;

  select count(*) into v_failed from cron.job_run_details d join cron.job j on j.jobid = d.jobid
   where j.jobname = 'brain-embed' and d.status = 'failed' and d.start_time > now() - interval '24 hours';
  check_name := 'no failed embed runs in 24 hours'; ok := v_failed = 0; detail := v_failed || ' failed runs';
  return next;

  select count(*) into v_missing_e from brain.entries e
   where e.added_at < now() - interval '30 minutes'
     and not exists (select 1 from brain.entry_vectors v where v.entry_id = e.id);
  check_name := 'every entry is searchable'; ok := v_missing_e = 0; detail := v_missing_e || ' entries older than 30 minutes have no vector';
  return next;

  select count(*) into v_missing_c from brain.chunks c join brain.documents d on d.id = c.document_id
   where c.embedding is null and d.added_at < now() - interval '30 minutes';
  check_name := 'every chunk is searchable'; ok := v_missing_c = 0; detail := v_missing_c || ' chunks older than 30 minutes have no vector';
  return next;

  begin
    v_vec := brain.embed_text('health check');
    check_name := 'OpenAI key works'; ok := v_vec is not null;
    detail := case when v_vec is null then 'embed_text returned nothing' else 'test embed succeeded' end;
  exception when others then
    get stacked diagnostics v_err = message_text;
    check_name := 'OpenAI key works'; ok := false; detail := 'embed_text failed: ' || left(v_err, 200);
  end;
  return next;
end $$;

revoke execute on function brain.health() from public, anon, authenticated;
