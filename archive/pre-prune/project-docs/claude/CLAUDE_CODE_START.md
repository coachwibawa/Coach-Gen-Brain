# Claude Code start file: coachwibawa.com

Written 1 Nov 2026 by Claude (Opus) in the claude.ai project "5 Laws of Lasting Change", for a Claude Code session on Gen's Mac. You cannot see that project or its memory. This file and the files it points to are your context. Read them before you touch code.

## 1. Who and how
- Owner and only approver: Genison Wibawa (Gen). Brand: Coach Gen. Legal company: PT Gapai Bangkit Wibawa. Never write "Coach Wibawa" in anything new.
- Gen likes short, direct answers. Plain words. No em dashes in anything you write, ever. British spelling.
- Reference documents are add-only: add and annotate, never shorten or rewrite them smaller.
- Never merge into main, never publish or deploy the live site, never send or post anything, without Gen's "go" in the chat. One go per release.
- Never type, print, or commit secrets (Supabase keys, Resend key, passwords, .env files).

## 2. Read these first (on this Mac)
Base folder: `/Users/coachwibawa/Documents/5 Laws of Lasting Change/Brand/`
1. `Brand_Rollout_Plan.md`: the plan. Read section 0.3 (rules), section 10 (link work order), section 11 (this website takeover, Track B), and the newest status lines.
2. `Guide/00_START-HERE.md`, `Guide/01_CORE.md`, `Guide/13_WEB.md`: brand rules for the website.
3. `Guide/ANTIGRAVITY-RULES.md` and `Guide/BRIEF-HEADER.md`: the website rules Antigravity followed. They now apply to you.
4. `Guide/19_LINKS.md`: the link registry. Every link you add must point to a target marked LIVE there.
5. `Guide/20_BRAND-AUDIT.md`: the snapshot library (Google Drive folder "Coach Gen Brand Snapshots").
6. `Website/L3_Link_Fix_Brief.md`: your first real coding task (later, not now).
If a file is missing, say so and continue with the rest.

## 3. Facts about the code
- Repo: github.com/coachwibawa/coachwibawa, private. A Lovable project (Vite, React, TypeScript, shadcn, Tailwind) synced both ways with GitHub. Supabase runs the newsletter (edge functions, tables).
- `npm run build` also runs `scripts/check-links.ts`. GitHub Actions `.github/workflows/verify.yml` runs lint, tests and links on every push.
- Old agent rules live in `.antigravity/rules.md`, `.agent/rules/`, `.cursorrules`. Some say "Coach Wibawa". Where they differ from the brand guide, the guide wins.
- Branch `5-Laws-of-Lasting-Change-Sales-Deck` holds Gen's unfinished worksheet work (21 files, committed 1 Nov as "WIP"). Do not merge it. Do not delete any branch.
- The live site answers HTTP 200 for every path, even missing ones (it shows an "Oops! Page not found" screen). Check a page by its text, never by status code.

## 4. Your task now: B0 setup only
Do these on a new branch `claude/setup` off main:
1. `git fetch --all`. List every branch: what it does in one line, ahead of main or not, merged or not.
2. Read the code and write `docs/HANDOFF.md`: how the site is built and published (Lovable or other, step by step), where content comes from (articles, newsletter, assessments), Supabase tables and functions, environment variable NAMES only and where each is set, unmerged branches and what is left in each, known bugs and half-done features. Mark anything you could not confirm as "unconfirmed, ask Gen".
3. Create `CLAUDE.md` at the repo root, so every future session starts with the rules. Include: the rules in section 1 of this file, the brand rules (copy from BRIEF-HEADER and ANTIGRAVITY-RULES, keep them as written), the link rules (19_LINKS section 1, plus: hub paths use 302, retired pages use 301), the "check text, not status" rule, the branch and pull request flow, and a pointer to `docs/brand/` and `docs/HANDOFF.md`.
4. Copy into `docs/brand/`: 01_CORE.md, 13_WEB.md, 19_LINKS.md, ANTIGRAVITY-RULES.md, BRIEF-HEADER.md, tokens.css, tokens.json (from `Brand/Guide/` and the project files on this Mac; if tokens files are not on the Mac, list them as missing). Add `docs/brand/README.md`: "Mirror of the Coach Gen brand guide. The master is the claude.ai project 5 Laws of Lasting Change. Refresh this folder when the guide changes."
5. Run `npm ci` and `npm run build`. Report errors, do not fix unrelated ones.
6. Commit, push the branch, open a pull request into main. Do NOT merge.
7. Add one status line at the end of section 11.5 in `/Users/coachwibawa/Documents/5 Laws of Lasting Change/Brand/Brand_Rollout_Plan.md` (add-only): date, "B0 done in Claude Code", the pull request link, and open questions.
8. Reply to Gen with: the branch table, the pull request link, what you could not confirm, and questions. Keep it short.

Do not start L3 (the link fixes) or any design change. Gen gives the go for those after he reviews the Afters board.
