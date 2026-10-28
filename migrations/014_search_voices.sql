-- 014: brain.search_voices. Voice-aware search so a writing chat can cite outside authors.
-- Scope own: gold entries (including adopted entries typed "outside voice") and chunks from own documents. Cutoff 0.32.
-- Scope outside: chunks from documents owned by 'outside'. Cutoff 0.25 on meaning, top 3.
-- Scope all (default): both lists. Rows carry voice, author, source and place ("page 93" for books).
-- Applied live as 014_search_voices and 014b_voices_keep_adopted_gold. This file holds the final form.
create or replace function brain.search_voices(
  p_query text,
  p_scope text default 'all',
  p_limit_own integer default 8,
  p_limit_outside integer default 3,
  p_min_sim double precision default 0.32,
  p_outside_min_sim double precision default 0.25
) returns table(voice text, kind text, ref text, author text, source text, place text, type text, text text, link text, similarity double precision, score double precision, via text)
language plpgsql security definer
set search_path to 'brain','extensions','public'
as $fn$
declare qv extensions.vector; k int := 60; tsq tsquery;
begin
  if p_scope not in ('own','outside','all') then
    raise exception 'p_scope must be own, outside or all';
  end if;
  qv := brain.embed_text(p_query);
  tsq := brain.or_tsquery(p_query);
  return query
  with g_sem as (
    select v.entry_id id, (1 - (v.embedding <=> qv)) sim, row_number() over (order by v.embedding <=> qv) rk
    from brain.entry_vectors v join brain.entries_full f on f.id = v.entry_id
    where f.status <> 'never use' and not (coalesce(f.tags,'{}') && array['heading','duplicate','table dump','label'])
    order by v.embedding <=> qv limit 50
  ), g_lex as (
    select e.id, row_number() over (order by ts_rank(e.search, tsq) desc) rk
    from brain.entries e join brain.entries_full f on f.id = e.id
    where tsq is not null and e.search @@ tsq and f.status <> 'never use' and not (coalesce(f.tags,'{}') && array['heading','duplicate','table dump','label'])
    order by ts_rank(e.search, tsq) desc limit 50
  ), g as (
    select coalesce(s.id, l.id) id, s.sim,
      coalesce(1.0/(k+s.rk),0) + coalesce(1.0/(k+l.rk),0) sc,
      case when s.id is not null and l.id is not null then 'both' when s.id is not null then 'meaning' else 'words' end via
    from g_sem s full join g_lex l on s.id = l.id
  ), c_sem as (
    select c.id, (1 - (c.embedding <=> qv)) sim, row_number() over (order by c.embedding <=> qv) rk
    from brain.chunks c join brain.documents d on d.id = c.document_id
    where c.embedding is not null and d.status = 'active'
    order by c.embedding <=> qv limit 80
  ), c_lex as (
    select c.id, row_number() over (order by ts_rank(c.search, tsq) desc) rk
    from brain.chunks c join brain.documents d on d.id = c.document_id
    where tsq is not null and c.search @@ tsq and d.status = 'active'
    order by ts_rank(c.search, tsq) desc limit 80
  ), c as (
    select coalesce(s.id, l.id) id, s.sim,
      coalesce(1.0/(k+s.rk),0) + coalesce(1.0/(k+l.rk),0) sc,
      case when s.id is not null and l.id is not null then 'both' when s.id is not null then 'meaning' else 'words' end via
    from c_sem s full join c_lex l on s.id = l.id
  ), own_rows as (
    select 'own'::text voice, 'gold'::text kind, f.legacy_ref::text ref, f.speaker::text author, 'Coach Gen brain'::text source,
           null::text place, f.type::text type, f.text::text text, f.link::text link,
           g.sim::double precision similarity, g.sc::double precision score, g.via::text via
    from g join brain.entries_full f on f.id = g.id
    where (g.via in ('both','words') or g.sim >= p_min_sim)
    union all
    select 'own', 'chunk', d.title||' @'||to_char((c2.t_start||' seconds')::interval,'HH24:MI:SS'), c2.speakers::text, d.title::text,
           null::text, d.kind::text, c2.text::text, c2.link::text, c.sim::double precision, c.sc::double precision, c.via::text
    from c join brain.chunks c2 on c2.id = c.id join brain.documents d on d.id = c2.document_id
    where d.owner::text <> 'outside' and c.sim >= p_min_sim
  ), out_rows as (
    select 'outside'::text voice, 'chunk'::text kind, d.title||' '||case when d.kind::text = 'book' then 'p'||c2.t_start else '@'||to_char((c2.t_start||' seconds')::interval,'HH24:MI:SS') end ref,
           c2.speakers::text author, d.title::text source,
           case when d.kind::text = 'book' then 'page '||c2.t_start else to_char((c2.t_start||' seconds')::interval,'HH24:MI:SS') end place,
           d.kind::text type, c2.text::text text, c2.link::text link,
           c.sim::double precision similarity, c.sc::double precision score, c.via::text via
    from c join brain.chunks c2 on c2.id = c.id join brain.documents d on d.id = c2.document_id
    where d.owner::text = 'outside' and c.sim >= p_outside_min_sim
  )
  select * from (select * from (select * from own_rows order by score desc limit p_limit_own) a where p_scope in ('own','all')
                 union all
                 select * from (select * from out_rows order by similarity desc limit p_limit_outside) b where p_scope in ('outside','all')) u
  order by (u.voice = 'own') desc, u.score desc;
end $fn$;
comment on function brain.search_voices(text,text,integer,integer,double precision,double precision) is 'Voice-aware search. scope own = Coach Gen own and adopted material, outside = other authors with cutoff 0.25 top 3, all = both lists side by side.';
