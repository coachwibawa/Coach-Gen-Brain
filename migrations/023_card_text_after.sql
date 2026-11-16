-- 023: brain.card_text(output, after): one card without what another card already holds (17 Nov 2026).
--
-- Why: a chapter loads the chapter card, then the case study card, then the key moments card at stop 1.
-- Each card repeats Tier 0 and Tier 1 in full, so about 10,600 of the 16,800 card tokens a chapter read
-- were the same lines twice. The second card now comes as its own rows only.
-- Adds one function. Changes no row and no other function. To undo:
--   drop function brain.card_text(text, text);

create function brain.card_text(p_output text, p_after text) returns text
language sql stable set search_path = brain as $$
  select '# The ' || p_output || ' card, past the ' || p_after || E' card (only what that card does not hold)\n\n'
         || coalesce(string_agg(b.body, E'\n' order by b.sort), '') || E'\n'
    from brain.get_card(p_output) b
   where b.code not in (select a.code from brain.get_card(p_after) a)
$$;

revoke all on function brain.card_text(text, text) from public, anon, authenticated;
