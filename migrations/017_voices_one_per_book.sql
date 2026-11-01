-- 017 and 017b: brain.search_voices outside list takes the best passage of each book first, then fills by score.
-- Before, one large book could fill all three outside slots. The candidate pool grew from 80 to 250 chunks,
-- because with five books the weaker but fitting passages fell outside the top 80.
-- Applied 1 Nov 2026. Test record: Run 8 in claude/Brain_Test_Set.md.
do $m$
declare d text; d2 text;
begin
  d := pg_get_functiondef('brain.search_voices(text,text,integer,integer,double precision,double precision)'::regprocedure);
  d2 := replace(d, 'select * from (select * from out_rows order by similarity desc limit p_limit_outside) b',
    'select * from (select o2.voice, o2.kind, o2.ref, o2.author, o2.source, o2.place, o2.type, o2.text, o2.link, o2.similarity, o2.score, o2.via from (select o.*, row_number() over (partition by o.author order by o.similarity desc) brk from out_rows o) o2 order by o2.brk, o2.similarity desc limit p_limit_outside) b');
  if d2 = d then raise exception 'search_voices outside expression not found'; end if;
  execute d2;
end $m$;
-- 017b
do $m$
declare d text; d2 text;
begin
  d := pg_get_functiondef('brain.search_voices(text,text,integer,integer,double precision,double precision)'::regprocedure);
  d2 := replace(d, 'order by c.embedding <=> qv limit 80', 'order by c.embedding <=> qv limit 250');
  d2 := replace(d2, 'order by ts_rank(c.search, tsq) desc limit 80', 'order by ts_rank(c.search, tsq) desc limit 250');
  if d2 = d then raise exception 'pool limits not found'; end if;
  execute d2;
end $m$;
