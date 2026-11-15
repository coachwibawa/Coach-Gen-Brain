-- 022_rule_folds_guards.sql (Rules Refactor Plan, step 16, after the fresh review of 16 Nov 2026)
-- Replaces the two inner fold functions of migration 021 with guarded versions. Nothing else changes.
--   1. A change or retire fold is tied to the exact text of its target (base_md5, set by cg_fold.py build).
--      brain.fold_store refuses when the live target has changed since: without this, a second fold on
--      the same rule could silently wipe a line the first fold added.
--   2. brain.fold_load refuses to overwrite an open fold that came from another file (two chats that
--      gave the same code to different lessons).
--   3. brain.fold_store also compares tier, check type and, for a new rule, its sort with the approved file.
--   4. The fold row's evidence now records why and base_md5.

create or replace function brain._fold_load(f jsonb, p_path text)
returns table(fold_code text, fold_action text, fold_target text, stage text, body_md5 text)
language plpgsql security definer
set search_path to 'brain','extensions','vault','public'
as $fn$
declare r jsonb; act text; tgt text; st text; c text; srt int; ev jsonb; gate jsonb;
        t brain.rules%rowtype; cur brain.rules%rowtype;
begin
  if coalesce(f->>'source','') = '' then
    raise exception 'the fold file needs a source: where the rule came from';
  end if;
  for r in select x from jsonb_array_elements(f->'rows') with ordinality a(x, o) order by o loop
    c := r->>'code'; act := r->>'action'; tgt := r->>'target'; st := r->>'fold_stage';
    gate := nullif(r->'test_gate', 'null'::jsonb);
    if act is null or act not in ('new','change','retire') then
      raise exception '%: action must be new, change or retire', c;
    end if;
    if st is null or st not in ('captured','judged','merged','gated') then
      raise exception '%: fold_load takes stages up to gated. His go and the storing go through brain.fold_store', c;
    end if;
    if st = 'gated' and gate is null then
      raise exception '%: a gated fold carries its test_gate result', c;
    end if;
    if act = 'new' then
      if r->>'kind' <> 'rule' or c !~ '^R[0-2]\.[0-9]+$' or tgt is not null then
        raise exception '%: a new fold is a rule with a code like R1.21 and no target', c;
      end if;
    else
      if c !~ '^fold:' then
        raise exception '%: a change or retire fold has a code like fold:R1.7:2026-11-12a', c;
      end if;
      select * into t from brain.rules x where x.code = tgt and x.status = 'active' and x.fold_stage = 'stored';
      if not found then
        raise exception '%: target % is not a live row', c, tgt;
      end if;
      if t.kind = 'frame' or t.kind <> r->>'kind' or t.tier is distinct from (r->>'tier')::smallint then
        raise exception '%: a fold keeps the kind and tier of %. To move a rule to another tier, retire it and add a new one', c, tgt;
      end if;
      if act = 'retire' and t.kind <> 'rule' then
        raise exception '%: only a rule can be retired', c;
      end if;
    end if;
    ev := coalesce(r->'evidence', '{}'::jsonb)
          || jsonb_build_object('fold', jsonb_build_object('action', act, 'target', tgt, 'file', p_path,
               'why', coalesce(r->>'why', r->'evidence'->>'why'), 'base_md5', r->>'base_md5'));
    select * into cur from brain.rules x where x.code = c;
    if not found then
      if act = 'new' then
        srt := (r->>'sort')::int;
        if srt is null or exists (select 1 from brain.rules x where x.sort = srt) then
          raise exception '%: sort % is missing or taken', c, r->>'sort';
        end if;
      else
        select greatest(coalesce(max(x.sort), 0), 100000) + 1 into srt from brain.rules x;
      end if;
      insert into brain.rules(code, kind, tier, heading, body, sort, outputs, check_type, extends, loads,
                              evidence, beats, source, added_on, fold_stage, test_gate, added_by)
      values (c, r->>'kind', (r->>'tier')::smallint, r->>'heading', r->>'body', srt,
              array(select jsonb_array_elements_text(r->'outputs')), r->>'check_type', r->>'extends',
              array(select jsonb_array_elements_text(r->'loads')), ev,
              array(select jsonb_array_elements_text(r->'beats')), f->>'source',
              coalesce((f->>'added_on')::date, current_date), st, gate, f->>'added_by');
    else
      if cur.status <> 'active' or cur.fold_stage not in ('captured','judged','merged','gated') then
        raise exception '%: already approved, stored or retired. Its text is frozen. A further change is a new fold', c;
      end if;
      if cur.evidence->'fold'->>'file' is distinct from p_path then
        raise exception '%: this code is already an open fold from another file (%). Pull the repo and build again, so this fold gets its own code', c, cur.evidence->'fold'->>'file';
      end if;
      update brain.rules x set
        heading = r->>'heading', body = r->>'body',
        outputs = array(select jsonb_array_elements_text(r->'outputs')), check_type = r->>'check_type',
        extends = r->>'extends', loads = array(select jsonb_array_elements_text(r->'loads')),
        evidence = ev, beats = array(select jsonb_array_elements_text(r->'beats')),
        source = f->>'source', fold_stage = st, test_gate = gate,
        sort = case when act = 'new' then (r->>'sort')::int else x.sort end
      where x.id = cur.id;
    end if;
    fold_code := c; fold_action := act; fold_target := tgt; stage := st; body_md5 := md5(r->>'body');
    return next;
  end loop;
end $fn$;

create or replace function brain._fold_store(f jsonb)
returns table(what text, hash text)
language plpgsql security definer
set search_path to 'brain','extensions','vault','public'
as $fn$
declare r jsonb; act text; tgt text; c text; d date; n int; bad text; cur brain.rules%rowtype;
begin
  d := (f->>'approved_on')::date;
  if d is null then
    raise exception 'no approved_on in the fold file. Nothing is stored without his go';
  end if;
  if d > current_date then
    raise exception 'approved_on % is in the future', d;
  end if;
  for r in select x from jsonb_array_elements(f->'rows') with ordinality a(x, o) order by o loop
    c := r->>'code'; act := r->>'action'; tgt := r->>'target';
    select * into cur from brain.rules x where x.code = c;
    if not found then
      raise exception '%: not in brain.rules. Run brain.fold_load on the gated file first', c;
    end if;
    if cur.status <> 'active' or cur.fold_stage <> 'gated' or cur.test_gate is null then
      raise exception '%: stage %, status %. Only a gated fold can be stored', c, cur.fold_stage, cur.status;
    end if;
    if md5(cur.body) <> md5(r->>'body') or cur.heading <> r->>'heading'
       or cur.loads <> array(select jsonb_array_elements_text(r->'loads'))
       or cur.outputs <> array(select jsonb_array_elements_text(r->'outputs'))
       or cur.tier is distinct from (r->>'tier')::smallint or cur.check_type is distinct from r->>'check_type'
       or (act = 'new' and cur.sort is distinct from (r->>'sort')::int) then
      raise exception '%: the row in the table is not the one in the approved file. Load and gate the final text first', c;
    end if;
    if act <> 'new' and not exists (select 1 from brain.rules x where x.code = tgt and x.status = 'active'
         and x.fold_stage = 'stored' and md5(x.body) = r->>'base_md5') then
      raise exception '%: % has changed since this fold was built, or is no longer live. Build the fold again on the live text, then gate it again', c, tgt;
    end if;
    if act = 'new' then
      update brain.rules x set fold_stage = 'stored', approved_on = d where x.id = cur.id;
    elsif act = 'change' then
      update brain.rules x set
        heading = cur.heading, body = cur.body, outputs = cur.outputs, check_type = cur.check_type,
        extends = cur.extends, loads = cur.loads,
        evidence = jsonb_set(x.evidence, '{folds}', coalesce(x.evidence->'folds', '[]'::jsonb)
                   || jsonb_build_array(jsonb_build_object('fold', c, 'on', d, 'source', cur.source)))
      where x.code = tgt and x.status = 'active' and x.fold_stage = 'stored';
      get diagnostics n = row_count;
      if n <> 1 then raise exception '%: target % is not a live row', c, tgt; end if;
      update brain.rules x set fold_stage = 'stored', approved_on = d, status = 'retired',
        retired_note = format('Fold record. Applied to %s on %s.', tgt, d) where x.id = cur.id;
    elsif act = 'retire' then
      update brain.rules x set status = 'retired',
        retired_note = format('Retired on %s by %s: %s', d, c, coalesce(r->>'why', 'no reason given'))
      where x.code = tgt and x.status = 'active' and x.fold_stage = 'stored' and x.kind = 'rule';
      get diagnostics n = row_count;
      if n <> 1 then raise exception '%: target % is not a live rule', c, tgt; end if;
      update brain.rules x set fold_stage = 'stored', approved_on = d, status = 'retired',
        retired_note = format('Fold record. Retired %s on %s.', tgt, d) where x.id = cur.id;
    else
      raise exception '%: action must be new, change or retire', c;
    end if;
  end loop;
  -- The cards must still add up.
  select string_agg(k.code || ' loads ' || l, ', ') into bad
    from brain.rules k, unnest(k.loads) l
   where k.kind = 'card' and k.status = 'active' and k.fold_stage = 'stored'
     and not exists (select 1 from brain.rules t where t.code = l and t.status = 'active'
                     and t.fold_stage = 'stored' and t.kind = 'rule' and t.tier = 2);
  if bad is not null then
    raise exception 'a card loads a rule that is not live: %', bad;
  end if;
  select string_agg(t.code, ', ') into bad
    from brain.rules t
   where t.kind = 'rule' and t.tier = 2 and t.status = 'active' and t.fold_stage = 'stored'
     and not exists (select 1 from brain.rules k where k.kind = 'card' and k.status = 'active'
                     and k.fold_stage = 'stored' and t.code = any(k.loads));
  if bad is not null then
    raise exception 'Tier 2 rule on no card, so nothing would load it: %', bad;
  end if;
  what := 'rulebook'; hash := md5(brain.rulebook_text()); return next;
  for what in select unnest(array['article','letter','chapter','key moments','case study']) loop
    hash := md5(brain.card_text(what)); return next;
  end loop;
end $fn$;
