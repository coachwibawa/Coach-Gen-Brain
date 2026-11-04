# Sprint To-dos Handoff (2 Nov 2026)

## Start here

This chat is for ticking off the to-dos from the Genison Sprint of 2 Nov 2026, one by one, starting with the ones Claude can do without him.

## Where things live

- The to-do list: `Master_Project_Status.md`, section "To-do list (from Genison Sprint, 2 Nov 2026)". It holds each item, its Fathom timestamp and its suggested next steps. Read it there. Do not copy it.
- The call: [Genison Sprint, 2 Nov 2026](https://fathom.video/calls/883936268). In the brain: source 57, cleaned transcript in `brain.documents` id 110 (search it with `brain.search_all`, layer `chunks`).
- Gold from that call: `brain.entries` 893 to 898.
- Brand material for the website work: `brand/00_START-HERE.md`, `brand/13_WEB.md`, `brand/tokens.css`, `brand/tokens.json`, `claude/Brand_Rollout_Plan.md`, `claude/Brand_Drift_Report_2026-11.md`, `claude/L3_Link_Fix_Brief.md`.
- Earlier website item and payment research: `Master_Project_Status.md`, section "To-do list (from Genison Sprint, 12 Oct 2026)".
- Brain rules: `claude/Brain_Rule.md`. Supabase project `zjedqjiuxkoncwsmylls`, schema `brain`. Repo `coachwibawa/Coach-Gen-Brain`.

## Done (2 Nov 2026)

- Kin's call of 2 Nov mined: source 56, document 109, entries 883 to 892.
- Genison Sprint of 2 Nov mined: source 57, document 110, entries 893 to 898.
- The 8 to-dos written into `Master_Project_Status.md`.

## In progress, waiting on him

- He has to save the corrected `/extract-fathom` skill card (the second one: Genio calls get the raw layer like every other call). The first card from that chat is out of date.
- He has to say go for one update. The Kin call's source note says 9 entries, but 10 were written: `update brain.sources set passes = array['2026-11-02 extract-fathom: whole call read. Cleaned transcript into the raw layer, gold picked (10 entries, 883 to 892).'] where id = 56;`

## Next, in order

Do the ones Claude can start alone first, report each in a few lines, then tick it in `Master_Project_Status.md` (add a "[Done 2026-11-xx]" note, never remove the item).

1. Facebook "Page not found" link: check every Facebook link on his Linktree, LinkedIn and coachwibawa.com against the new Facebook page. Report which links are wrong and what each should point to.
2. Graphify and the skills Genio shared: research what Graphify does, how it cuts token cost, and whether it fits a Claude Code setup. Ask him for the repo link Genio sent if it is not in the call.
3. Phasing out project docs: list the project docs the brain has replaced (start with the frozen list in `claude/Brain_Rule.md` section 2), with what each costs to load. He decides. Nothing is deleted.
4. AI music for the video pipeline: find music sources cleared for both Facebook and Instagram, so videos are not demonetized. See `claude/Video_Pipeline.md` for how the pipeline works.
5. Website rebrand: Claude Design pass on the homepage from the `brand/` docs, then a Claude Code plan in phases, each with a milestone. Lock decisions with `/grilling` before building. The payment part stays blocked on the NIB.
6. Website warnings: in Claude Code, ask for the highest-ROI warnings first and fix those.
7. Receiving USD before the book launches: pick a route from the 14 Oct payment research and write the steps.
8. Screen Time hours: at the next sprint, compare his Screen Time total with his guess of 20 to 25 hours a week.

## Rules for this work

- `Master_Project_Status.md` is add-only. To edit it, take the exact text from `project_read`, change it in code, and write it back from a file in the working directory with `local_path`. Never retype it.
- Never delete a doc (`Guardrails.md`). Phasing out means he decides and it is marked, not removed.
- Family and money items from the call stay out of project docs.
- In the brain, an UPDATE needs his go: batch it, say in one line what it does, wait for "go".
- No em dashes and no semicolons in anything written for him. Simple English. Answer first.

## Suggested skills

- `/grilling` before the website rebrand plan, to lock the decisions.
- `/pick-model` at the start of each item: research items fit Sonnet, the website plan fits Opus.
- `built-in-browser` or `chrome-browser` skill before checking Linktree, LinkedIn and Facebook pages in a browser.
- `/handoff` when this chat runs long, to update this doc.
