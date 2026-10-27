-- 012 (2026-10-27): default meaning cutoff raised from 0.30 to 0.32.
-- Fixed test Q20 (an unrelated entry at 0.305). No test question lost its expected ref.
do $mig$
declare def text;
begin
  def := pg_get_functiondef('brain.search_all(text,integer,integer,text,double precision,text)'::regprocedure);
  def := replace(def, 'p_min_sim double precision DEFAULT 0.30', 'p_min_sim double precision DEFAULT 0.32');
  execute def;
end $mig$;
