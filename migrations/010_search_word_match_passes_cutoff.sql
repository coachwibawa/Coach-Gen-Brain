-- 010 (2026-10-27): an entry or chunk with a word match passes the meaning cutoff.
-- Fixed: WS-L5-F2-21 ("yearly misogi") matched by words but scored 0.253 on meaning and was dropped.
-- The chunk half of this change was taken back in 011.
do $mig$
declare def text;
begin
  def := pg_get_functiondef('brain.search_all(text,integer,integer,text,double precision,text)'::regprocedure);
  def := replace(def, '(g.sim is null or g.sim >= p_min_sim) and (g.sim is not null or g.via = ''words'')', '(g.via in (''both'',''words'') or g.sim >= p_min_sim)');
  def := replace(def, '(c.sim is null or c.sim >= p_min_sim)', '(c.via in (''both'',''words'') or c.sim >= p_min_sim)');
  execute def;
end $mig$;
