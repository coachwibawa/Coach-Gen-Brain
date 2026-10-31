-- 016: book chunks show the PDF page ("p39") in brain.search_all, not a time ("@00:00:39").
-- For documents of kind 'book' the stored t_start is a PDF page number, so the old label read the page as seconds.
-- Rewrites the label expression inside the existing function. Calls and videos keep the @HH:MM:SS label.
-- Applied 31 Oct 2026. brain.search_voices already showed the page.
do $m$
declare d text; d2 text;
begin
  d := pg_get_functiondef('brain.search_all(text,integer,integer,text,double precision,text)'::regprocedure);
  d2 := replace(d, 'd.title||'' @''||to_char((c2.t_start||'' seconds'')::interval,''HH24:MI:SS'')',
    'case when d.kind = ''book'' then d.title||'' p''||c2.t_start else d.title||'' @''||to_char((c2.t_start||'' seconds'')::interval,''HH24:MI:SS'') end');
  if d2 = d then raise exception 'search_all label expression not found'; end if;
  execute d2;
end $m$;
