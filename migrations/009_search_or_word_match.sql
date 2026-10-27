-- 009 (2026-10-27): word match uses OR instead of AND, with filler words dropped.
-- Before: plainto_tsquery needed every word of the question in one entry, so loose questions
-- got zero word matches. Now any meaningful word counts, and ts_rank ranks entries matching more words higher.

create or replace function brain.or_tsquery(p_query text)
returns tsquery language sql immutable set search_path to 'brain','public' as $$
  select case when count(*) = 0 then null
         else to_tsquery('simple', string_agg(w, ' | ')) end
  from (
    select distinct w from regexp_split_to_table(regexp_replace(lower(p_query), '[^a-z0-9 ]', ' ', 'g'), '\s+') w
    where length(w) > 1 and w !~ '^(the|a|an|and|or|but|of|to|in|on|at|for|with|by|from|about|as|is|are|was|were|be|been|being|do|does|did|doing|done|have|has|had|i|me|my|myself|you|your|he|him|his|she|her|it|its|we|our|they|them|their|this|that|these|those|what|which|who|whom|why|how|when|where|not|no|so|than|too|very|can|will|just|should|would|could|gen|say|said|think|thinks|after|before|over|into|out|up|down|then|there|here|all|any|some|more|most|other|such|only|own|same|if|because|until|while|feel|feels|means|keep|keeps|new)$'
  ) t;
$$;

create or replace function brain.search_all(p_query text, p_limit integer default 10, p_law integer default null::integer, p_type text default null::text, p_min_sim double precision default 0.30, p_layers text default 'both'::text)
 returns table(kind text, ref text, law integer, type text, speaker text, text text, link text, similarity double precision, score double precision, via text)
 language plpgsql security definer
 set search_path to 'brain', 'extensions', 'public'
as $function$
declare qv extensions.vector; k int := 60; tsq tsquery;
begin
  qv := brain.embed_text(p_query);
  tsq := brain.or_tsquery(p_query);
  return query
  with g_sem as (
    select v.entry_id id, (1 - (v.embedding <=> qv)) sim, row_number() over (order by v.embedding <=> qv) rk
    from brain.entry_vectors v join brain.entries_full f on f.id = v.entry_id
    where f.status <> 'never use' and not (coalesce(f.tags,'{}') && array['heading','duplicate','table dump','label'])
      and (p_law is null or f.law = p_law) and (p_type is null or f.type::text = p_type)
    order by v.embedding <=> qv limit 50
  ), g_lex as (
    select e.id, row_number() over (order by ts_rank(e.search, tsq) desc) rk
    from brain.entries e join brain.entries_full f on f.id = e.id
    where tsq is not null and e.search @@ tsq and f.status <> 'never use' and not (coalesce(f.tags,'{}') && array['heading','duplicate','table dump','label'])
      and (p_law is null or f.law = p_law) and (p_type is null or f.type::text = p_type)
    order by ts_rank(e.search, tsq) desc limit 50
  ), g as (
    select coalesce(s.id, l.id) id, s.sim,
      coalesce(1.0/(k+s.rk),0) + coalesce(1.0/(k+l.rk),0) sc,
      case when s.id is not null and l.id is not null then 'both' when s.id is not null then 'meaning' else 'words' end via
    from g_sem s full join g_lex l on s.id = l.id
  ), c_sem as (
    select c.id, (1 - (c.embedding <=> qv)) sim, row_number() over (order by c.embedding <=> qv) rk
    from brain.chunks c join brain.documents d on d.id = c.document_id
    where c.embedding is not null and d.status = 'active' and p_law is null and p_type is null
    order by c.embedding <=> qv limit 50
  ), c_lex as (
    select c.id, row_number() over (order by ts_rank(c.search, tsq) desc) rk
    from brain.chunks c join brain.documents d on d.id = c.document_id
    where tsq is not null and c.search @@ tsq and d.status = 'active' and p_law is null and p_type is null
    order by ts_rank(c.search, tsq) desc limit 50
  ), c as (
    select coalesce(s.id, l.id) id, s.sim,
      coalesce(1.0/(k+s.rk),0) + coalesce(1.0/(k+l.rk),0) sc,
      case when s.id is not null and l.id is not null then 'both' when s.id is not null then 'meaning' else 'words' end via
    from c_sem s full join c_lex l on s.id = l.id
  )
  select * from (
    select 'gold'::text, f.legacy_ref::text, f.law::int, f.type::text, f.speaker::text, f.text::text, f.link::text,
           g.sim::double precision, g.sc::double precision, g.via::text
    from g join brain.entries_full f on f.id = g.id
    where p_layers in ('both','gold') and (g.sim is null or g.sim >= p_min_sim) and (g.sim is not null or g.via = 'words')
    union all
    select 'chunk', d.title||' @'||to_char((c2.t_start||' seconds')::interval,'HH24:MI:SS'), null::int, d.kind::text, c2.speakers::text, c2.text::text, c2.link::text,
           c.sim::double precision, c.sc::double precision, c.via::text
    from c join brain.chunks c2 on c2.id = c.id join brain.documents d on d.id = c2.document_id
    where p_layers in ('both','chunks') and (c.sim is null or c.sim >= p_min_sim)
  ) u order by 9 desc limit p_limit;
end $function$;
