# Handoff note from Setsu to Reina

From: Setsu (Gen's Claude Cowork chats in the claude.ai project "5 Laws of Lasting Change")
To: Reina (Claude Code in VS Code, working on the coachwibawa.com repo)
Date: 1 Nov 2026
Only what you cannot see from the repo. Anything you can check in the code yourself is left out.

## 1. Where the plan lives
- Master: the claude.ai project (you cannot see it). Mirror on this Mac, kept in sync by Setsu:
  `/Users/coachwibawa/Documents/5 Laws of Lasting Change/Brand/Brand_Rollout_Plan.md`
  Read section 11 (the website moves from Antigravity to Claude Code, Track A and Track B) and the newest status lines at the very end of the file.
- The brand guide that `.cursorrules` points to as `.agent/rules/brand_guide.md` does not exist in the repo. The real guide is in `/Users/coachwibawa/Documents/5 Laws of Lasting Change/Brand/Guide/`. For the website: `00_START-HERE.md`, `01_CORE.md`, `13_WEB.md`, `ANTIGRAVITY-RULES.md`, `BRIEF-HEADER.md`, `19_LINKS.md`, `tokens.css`, `tokens.json`.
- Your task list for now is section 4 of `/Users/coachwibawa/Documents/5 Laws of Lasting Change/Brand/Website/CLAUDE_CODE_START.md` (B0 setup), with the changes in section 4 below.

## 2. The plan in one screen
- The live site is still the OLD brand ("Coach Wibawa", teal logo, Oswald, Outfit and Manrope fonts, gradients, "we" voice). The new brand is Coach Gen. A full rebrand comes later (plan Phase 5).
- Gen's order: first every social profile and site outside the website gets updated (Setsu does this in Chrome). Setsu then builds one "Afters board" showing all of them. Gen reviews it. Only then does website work go live.
- So for now: **B0 setup only.** Add `CLAUDE.md` and `docs/HANDOFF.md`, mirror the brand files into `docs/brand/`. No link fixes, no design or text changes on live pages.
- After that, in order: B1 link fixes (`Brand/Website/L3_Link_Fix_Brief.md`, written for Antigravity, still the exact task list), B2 LinkedIn address change, B3 a new start-here page, B4 the rebrand, B5 /book to cal.com, B6 new features.

## 3. Who does what
- **Reina:** code, branches, the repo, the build, Supabase reads.
- **Setsu:** opening the live site in Chrome to check every link after a deploy, the social profiles, the snapshot library (Google Drive folder "Coach Gen Brand Snapshots"), and the master plan and brand guide.
- So the no-browser rule in `.agents/rules/no-browser.md` fits: you never need the browser. Setsu checks the live result.
- To report to Setsu: add one dated line at the end of section 11.5 in the Mac plan file (add-only, never edit earlier lines). Gen can also paste your reply into Setsu's chat.

## 4. Changes to the B0 task in CLAUDE_CODE_START.md (Gen's existing rules win)
- **Pull requests:** Gen opens PRs himself (the old rules say so). Push your branch and give him the compare link. Do not merge.
- **Checks:** if the no-verify rule stands, skip local `npm run build`. The GitHub check (`verify.yml`: lint, tests, link check) runs on every push. Report its result.
- **Supabase:** you have the Supabase connection. Read only. No migrations, no edge function deploys, no data changes without Gen's go in the chat.

## 5. Things found from outside the repo (1 Nov 2026)
1. **`/admin/worksheet` is public on the live site.** Setsu opened https://coachwibawa.com/admin/worksheet logged out: it shows the 6C worksheet ("Print to PDF..."). `src/App.tsx` on main has no guard on that route. When the workbook branch merges, the full 5 Laws workbook (with the David case study) would be public too. Before that branch merges, Gen decides: protect `/admin/*`, or accept it as public. Flag it, do not change it yet.
2. **Which branch is live?** The remote has `main`, `production`, `standardize-development-on-multiple-devices`, and the Sales-Deck branch. Find out from the code or Gen whether Lovable publishes from `main` or `production`. Merging into the live branch may publish the site, which needs Gen's go.
3. **A password sits in a committed file.** `DEPLOY_CHECKLIST.md` lines 8 and 31 hold the proposal page password in plain text. The repo is private. Mention it to Gen once. Do not print it in any reply.
4. **The site answers HTTP 200 for every path**, even missing ones (it renders an "Oops! Page not found" screen). Any link check must read the page content, not the status code. The repo's `scripts/check-links.ts` may already handle internal routes. Check how it treats unknown paths.
5. **Pages that show the not-found screen today:** `/paths`, `/framework`, `/products`. Footer has a dead LinkedIn link (`/in/genison-wibawa`) and the old Instagram handle (`instagram.com/coachwibawa`). The contact page "Book a Call" and the About page "View Our Services" both go to `/products`. All of this is fixed in B1, not now.
6. **Worksheets outside the repo:** Gen's coaching worksheets also exist as Word and PDF files built by a script in `/Users/coachwibawa/Documents/5 Laws of Lasting Change/` (`build_worksheet.js`, `5_Laws_Signature_Program_Worksheet.docx`, `Law1_Client_Worksheet.docx`, `Law3_Client_Worksheet.docx`). The web workbook at `/admin/worksheet` may duplicate them. In `docs/HANDOFF.md`, note which one is the source for each Law. Do not merge them.
7. **Client stories:** public pages may only use real clients with permission, or the composite names from the book draft. The "David" case in `caseStudies.ts` is also told in Gen's public LinkedIn post of 12 Oct 2026, so it is public already. Any other client name: ask Gen.

## 6. Writing rules for anything you write (docs, commit messages, replies)
No em dashes anywhere. No emojis. Plain words, short sentences. British spelling. Never "Coach Wibawa" in new text. Reference documents are add-only: add and annotate, never shorten.
