-- 011 (2026-10-27): chunks keep the meaning cutoff. Long spoken chunks match many words,
-- so letting them skip the cutoff flooded results (11 of 18 non-speech test questions).
-- Gold entries keep the skip from 010.
do $mig$
declare def text;
begin
  def := pg_get_functiondef('brain.search_all(text,integer,integer,text,double precision,text)'::regprocedure);
  def := replace(def, '(c.via in (''both'',''words'') or c.sim >= p_min_sim)', '(c.sim >= p_min_sim)');
  execute def;
end $mig$;
