-- 018: brain.load_from_github also records the pass on an existing source.
-- A load file with "source_id" may carry "pass" (text appended to sources.passes) and "left_out_add" (text appended to sources.left_out).
-- For a new source, passes and left_out go in the "source" object as before.
-- Applied 1 Nov 2026. Body otherwise identical to 015.
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
  -- 018: record the pass on an existing source, so no separate UPDATE (and no approval prompt) is needed
  if f ? 'source_id' and (f ? 'pass' or f ? 'left_out_add') then
    update brain.sources s set
      passes = s.passes || case when f ? 'pass' then array[f->>'pass'] else '{}'::text[] end,
      left_out = case when f ? 'left_out_add' then concat_ws(' ', s.left_out, f->>'left_out_add') else s.left_out end
    where s.id = src;
  end if;
end $fn$;

revoke all on function brain.load_from_github(text,text) from public, anon, authenticated;
