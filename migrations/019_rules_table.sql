-- 019_rules_table.sql (Rules Refactor Plan, step 9)
-- One home for the writing rules: brain.rules.
-- 1. brain.rules: one row per block of the rulebook (frame, rule or card), with tier,
--    outputs, check type, v3 line numbers, evidence and the fold fields.
-- 2. The add-only lock: delete and truncate refused. A rule leaves by status 'retired'.
-- 3. Every insert and update is copied into brain.change_log.
-- 4. A card's links (extends, loads) must point at real rows: a card, and Tier 2 rules.
-- 5. brain.get_card(output): Tier 0, Tier 1, the card (and the card it extends),
--    and the Tier 2 rules the card names. brain.card_text(output) joins them as text.
--    brain.rulebook_text() joins every live row, for the word-for-word check against the file.
-- 6. brain.load_rules(path): loads a rules/table/*.json file made by
--    rules/table/build_rules_load.py, straight from the repo, so rule text never passes through a chat.
-- Only rows that are active and stored are served. A new rule climbs the fold stages
-- (captured, judged, merged, gated, approved, stored) before any card sees it.

create table brain.rules (
  id bigint generated always as identity primary key,
  code text not null unique,
  kind text not null check (kind in ('frame','rule','card')),
  tier smallint check (tier between 0 and 2),
  heading text not null,
  body text not null,
  sort int not null unique,
  outputs text[] not null default '{}'
    check (outputs <@ array['article','letter','chapter','key moments','case study']),
  check_type text check (check_type in ('mechanical','checker','judgment')),
  v3_first int,
  v3_last int,
  extends text references brain.rules(code),
  loads text[] not null default '{}',
  evidence jsonb not null default '{}'::jsonb,
  status text not null default 'active' check (status in ('active','retired')),
  retired_note text,
  -- the fold pipeline
  beats text[] not null default '{}',
  source text not null,
  added_on date not null default current_date,
  fold_stage text not null default 'captured'
    check (fold_stage in ('captured','judged','merged','gated','approved','stored')),
  test_gate jsonb,
  approved_on date,
  added_by text,
  added_at timestamptz not null default now(),
  constraint rules_shape check (
    (kind = 'rule' and tier is not null and check_type is not null and cardinality(outputs) > 0)
    or (kind = 'card' and tier is null and check_type is null and cardinality(outputs) > 0)
    or (kind = 'frame' and check_type is null and cardinality(outputs) = 0)),
  constraint rules_links_only_on_cards check (kind = 'card' or (extends is null and cardinality(loads) = 0)),
  constraint rules_lines check ((v3_first is null) = (v3_last is null) and (v3_first is null or v3_first <= v3_last)),
  constraint rules_stored_needs_approval check (fold_stage not in ('approved','stored') or kind = 'frame' or approved_on is not null),
  constraint rules_retired_note check (status = 'active' or retired_note is not null)
);

comment on table brain.rules is 'The writing rules (Rules Refactor Plan step 9). Add-only. Retire, never delete. Served by brain.get_card().';
comment on column brain.rules.code is 'R0.1 to R2.11 for rules, card:<output> for cards, title, tier0, tier1, tier2, cards for the frame';
comment on column brain.rules.body is 'The exact text of the block, heading line included. Joining all live bodies by sort gives the rulebook.';
comment on column brain.rules.loads is 'On a card: the Tier 2 rule codes it names. Empty means it uses the card it extends';
comment on column brain.rules.beats is 'The old rules this one replaces (inventory ids, or rule codes for later folds)';
comment on column brain.rules.test_gate is 'Result of the test-set gate: run date, fail cases caught, pass cases kept';

create function brain.check_rule_links() returns trigger language plpgsql as $$
declare bad text;
begin
  if new.extends is not null and not exists (
       select 1 from brain.rules where code = new.extends and kind = 'card') then
    raise exception 'brain.rules %: extends % is not a card', new.code, new.extends;
  end if;
  select string_agg(x, ', ') into bad from unnest(new.loads) x
   where not exists (select 1 from brain.rules r where r.code = x and r.kind = 'rule' and r.tier = 2);
  if bad is not null then
    raise exception 'brain.rules %: loads % which are not Tier 2 rules', new.code, bad;
  end if;
  return new;
end $$;

create trigger rules_check_links before insert or update of extends, loads on brain.rules
  for each row execute function brain.check_rule_links();
create trigger rules_no_delete before delete on brain.rules
  for each row execute function brain.block_delete();
create trigger rules_no_truncate before truncate on brain.rules
  for each statement execute function brain.block_truncate();
create trigger rules_log after insert or update on brain.rules
  for each row execute function brain.log_change();

alter table brain.rules enable row level security;
alter table brain.rules force row level security;
create policy rules_admin on brain.rules for all to postgres, service_role using (true) with check (true);
revoke all on brain.rules from public, anon, authenticated;

-- The rows one output loads, in rulebook order.
create function brain.get_card(p_output text)
returns table(code text, kind text, tier smallint, heading text, body text, sort int, v3_first int, v3_last int)
language sql stable set search_path = brain as $$
  with recursive live as (
    select * from brain.rules where status = 'active' and fold_stage = 'stored'
  ), card as (
    select l.code, l.extends, l.loads, 0 as depth from live l
     where l.kind = 'card' and p_output = any(l.outputs) and l.code = 'card:' || replace(p_output, ' ', '-')
    union all
    select l.code, l.extends, l.loads, c.depth + 1 from live l join card c on l.code = c.extends
  ), t2 as (
    select distinct unnest(loads) as code from card
  )
  select l.code, l.kind, l.tier, l.heading, l.body, l.sort, l.v3_first, l.v3_last
    from live l
   where (l.kind = 'frame' and l.code in ('title','tier0','tier1','cards'))
      or (l.kind = 'frame' and l.code = 'tier2' and exists (select 1 from t2))
      or (l.kind = 'rule' and l.tier in (0,1) and p_output = any(l.outputs))
      or (l.kind = 'rule' and l.tier = 2 and l.code in (select code from t2))
      or (l.kind = 'card' and l.code in (select code from card))
   order by l.sort
$$;

create function brain.card_text(p_output text) returns text
language sql stable set search_path = brain as $$
  select string_agg(body, E'\n' order by sort) || E'\n' from brain.get_card(p_output)
$$;

create function brain.rulebook_text() returns text
language sql stable set search_path = brain as $$
  select string_agg(body, E'\n' order by sort) || E'\n'
    from brain.rules where status = 'active' and fold_stage = 'stored'
$$;

-- Load a rules file from the repo. Inserts only. Refuses a file whose codes already exist.
create function brain.load_rules(p_path text, p_ref text default 'main')
returns table(rows_added int, rules int, cards int, rulebook_md5 text, source_md5 text)
language plpgsql security definer
set search_path to 'brain','extensions','vault','public'
as $fn$
declare f jsonb; r jsonb; n int := 0; dup text;
begin
  f := brain.github_fetch(p_path, p_ref)::jsonb;
  select string_agg(x->>'code', ', ') into dup
    from jsonb_array_elements(f->'rows') x where exists (select 1 from brain.rules where code = x->>'code');
  if dup is not null then raise exception 'already in brain.rules: %', dup; end if;
  for r in select x from jsonb_array_elements(f->'rows') x order by (x->>'sort')::int loop
    insert into brain.rules(code, kind, tier, heading, body, sort, outputs, check_type, v3_first, v3_last,
                            extends, loads, evidence, beats, source, added_on, fold_stage, approved_on, added_by)
    values (r->>'code', r->>'kind', (r->>'tier')::smallint, r->>'heading', r->>'body', (r->>'sort')::int,
            array(select jsonb_array_elements_text(r->'outputs')), r->>'check_type',
            (r->>'v3_first')::int, (r->>'v3_last')::int, r->>'extends',
            array(select jsonb_array_elements_text(r->'loads')), coalesce(r->'evidence','{}'::jsonb),
            array(select jsonb_array_elements_text(r->'beats')), f->>'source', (f->>'added_on')::date,
            'stored', (f->>'approved_on')::date, f->>'added_by');
    n := n + 1;
  end loop;
  return query select n,
    (select count(*)::int from brain.rules where kind = 'rule'),
    (select count(*)::int from brain.rules where kind = 'card'),
    md5(brain.rulebook_text()), f->>'source_md5';
end $fn$;

revoke all on function brain.check_rule_links(), brain.get_card(text), brain.card_text(text),
  brain.rulebook_text(), brain.load_rules(text, text) from public, anon, authenticated;
