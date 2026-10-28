-- 015: load prepared outside material straight from this repo, so book text never passes through a chat.
-- brain.github_fetch(path, ref) reads a file from coachwibawa/Coach-Gen-Brain with the read-only token in vault secret coach_gen_brain.
-- brain.load_from_github(path, ref) loads a loads/*.json file made by tools/build_load.py: inserts only, returns doc_id, title, chunks, md5 per document.
-- Both are callable only by the service role (revoked from public, anon, authenticated).
-- Tested 28 Oct 2026: full Mindset text (583 KB, 17 documents, 408 chunks) in one call, md5 matched, rolled back.

create or replace function brain.github_fetch(p_path text, p_ref text default 'main')
returns text language plpgsql security definer
set search_path to 'brain','extensions','vault','public'
as $fn$
declare k text; r extensions.http_response;
begin
  select decrypted_secret into k from vault.decrypted_secrets where name in ('github_brain_token','coach_gen_brain') order by name = 'github_brain_token' desc limit 1;
  if k is null then raise exception 'GitHub token missing in vault (coach_gen_brain)'; end if;
  perform extensions.http_set_curlopt('CURLOPT_TIMEOUT', '120');
  r := extensions.http((
    'GET','https://api.github.com/repos/coachwibawa/Coach-Gen-Brain/contents/'||p_path||'?ref='||p_ref,
    array[extensions.http_header('Authorization','Bearer '||k),
          extensions.http_header('Accept','application/vnd.github.raw'),
          extensions.http_header('User-Agent','coach-gen-brain'),
          extensions.http_header('X-GitHub-Api-Version','2022-11-28')],
    null, null)::extensions.http_request);
  if r.status <> 200 then raise exception 'github error %: %', r.status, left(r.content,300); end if;
  return r.content;
end $fn$;

create or replace function brain.load_from_github(p_path text, p_ref text default 'main')
returns table(doc_id bigint, title text, chunks int, md5 text)
language plpgsql security definer
set search_path to 'brain','extensions','vault','public'
as $fn$
declare f jsonb; src bigint; d jsonb; did bigint; t jsonb; sp text; ctx text; n int;
begin
  f := brain.github_fetch(p_path, p_ref)::jsonb;
  sp := f->>'speaker'; ctx := f->>'context_prefix';
  if f ? 'source_id' then src := (f->>'source_id')::bigint;
  else
    insert into brain.sources(title, kind, url, participants, passes, left_out, notes, added_by)
    values (f->'source'->>'title', f->'source'->>'kind', f->'source'->>'url', f->'source'->>'participants',
            coalesce(array(select jsonb_array_elements_text(f->'source'->'passes')), '{}'),
            f->'source'->>'left_out', f->'source'->>'notes', coalesce(f->>'added_by','mine'))
    returning id into src;
  end if;
  for d in select * from jsonb_array_elements(f->'docs') loop
    select jsonb_agg(e || jsonb_build_object('sp', coalesce(e->>'sp', sp)) order by o) into t
      from jsonb_array_elements(d->'turns') with ordinality x(e,o);
    insert into brain.documents(source_id, title, kind, owner, language, turns, clean_text, notes, added_by)
    values (src, d->>'title', coalesce(d->>'kind','book'), coalesce(d->>'owner','outside'), coalesce(d->>'language','en'), t,
            (select string_agg(e->>'t', E'\n' order by o) from jsonb_array_elements(t) with ordinality x(e,o)),
            concat_ws(' ', f->>'notes', d->>'note_tail'), coalesce(f->>'added_by','mine'))
    returning id into did;
    insert into brain.chunks(document_id, position, text, context, t_start, t_end, speakers, tokens_est)
    select did, (c->>0)::int,
      (select string_agg((e->>'sp')||': '||(e->>'t'), E'\n' order by o) from jsonb_array_elements(t) with ordinality x(e,o) where o between (c->>1)::int and (c->>2)::int),
      ctx||' '||coalesce(d->>'chapter','')||'. Section: '||(c->>3)||'. PDF page '||(t->((c->>1)::int-1)->>'s')||'.',
      (t->((c->>1)::int-1)->>'s')::int, (t->((c->>2)::int-1)->>'s')::int,
      sp,
      ((select sum(array_length(regexp_split_to_array(trim(e->>'t'), '\s+'),1)) from jsonb_array_elements(t) with ordinality x(e,o) where o between (c->>1)::int and (c->>2)::int)*1.35)::int
    from jsonb_array_elements(d->'chunks') c;
    get diagnostics n = row_count;
    doc_id := did; title := d->>'title'; chunks := n;
    md5 := md5((select string_agg(e->>'t', E'\n' order by o) from jsonb_array_elements(t) with ordinality x(e,o)));
    return next;
  end loop;
end $fn$;

revoke all on function brain.github_fetch(text,text) from public, anon, authenticated;
revoke all on function brain.load_from_github(text,text) from public, anon, authenticated;
comment on function brain.load_from_github(text,text) is 'Loads a prepared outside-material JSON file (loads/*.json in coachwibawa/Coach-Gen-Brain) into documents and chunks. Inserts only. Token from vault secret coach_gen_brain.';
