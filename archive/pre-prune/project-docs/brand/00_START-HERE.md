# Coach Gen Brand Guide: Start Here

Version 1.1, 30 Oct 2026. Owner and only approver: Genison Wibawa.
Every AI agent reads this file first, then only the files its task needs.

## Why this guide exists
1. **Corporate-level consistency.** Every piece looks like it came from one company, whichever agent or tool made it.
2. **Lower token cost.** Agents load a small set of files, use fixed values, and never ask Gen a question this guide already answers.

## Load map (load the row, nothing else)
| Task | Load |
|---|---|
| Anything visible (always) | 01_CORE.md |
| Reel, video, captions, Concat, ffmpeg | + 10_VIDEO.md |
| Instagram, LinkedIn or Facebook image, carousel, Coachinator script | + 11_SOCIAL.md |
| Paid ad (Meta, LinkedIn) | + 12_ADS.md, plus 10 or 11 for the format |
| Website, landing page, brief for Antigravity | + 13_WEB.md and tokens.json |
| Document, worksheet, proposal, slide deck, invoice, print | + 14_DOCS.md |
| WhatsApp group, email, newsletter | + 15_MESSAGING.md |
| Photo direction, AI image prompt (Nano Banana, Gemini) | + 16_IMAGERY.md |
| Code that only needs colors, fonts or sizes | tokens.json only |
| Any visual made from a template (added 30 Oct 2026, v1.1) | + 17_TEMPLATES.md and templates/cg_render.py |
| Public copy: bios, profiles, captions, ads, page text, inquiry replies (added 30 Oct 2026) | + 02_VOICE.md and 18_COPY-KITS.md, then the Language Rules for sentence-level checks |
| A brief for a tool or person outside Claude (added 30 Oct 2026) | BRIEF-HEADER.md, pasted at the top. For the website in Antigravity, also ANTIGRAVITY-RULES.md |
| A judgment call no file covers | + 90_TASTE.md |

Not in this guide, load only when writing words:
- Voice and wording: `Coach_Gen_Language_Rules.md` (and the Book Rules for the book).
  - ADDED (30 Oct 2026): 02_VOICE.md holds what to say (platform, messages, tone by channel, vocabulary, bios). The Language Rules still win on how sentences are written.
- Platform copy (hooks, hashtags, sign-offs, Indonesian mix): `claude/Coach_Gen_Social_Posting_Rules.md`.
- Reel structure and pacing references: `claude/Reel_Style_Guide.md` (10_VIDEO.md overrides its fonts and colors).
- Logo files and logo rules: `Brand/CoachGen-Logo-Kit/` and its `LOGO-USAGE.md`.
- Why each decision was made: `claude/Brand_Direction_Phase1.md`. Agents never need to load it.

## Precedence (resolve conflicts without asking)
1. Gen's instruction in the current chat.
2. The protected writing docs, for words.
3. This guide, for looks.
4. Skill defaults and older style docs.

## Token rules for agents
1. Load only the files in your load-map row.
2. Values marked **locked** are used as written, with no test renders. Values marked **check once** get one preview on first use, then the agent proposes locking them.
3. Never ask Gen something this guide answers.
4. Prefer scripts and files over driving a GUI. Proof (16 Oct 2026): a Coachinator carousel driven field by field cost about 28,000 tokens for 4 slides. The Script Import route did the whole carousel in one paste.
5. A gap in the guide: build with the nearest rule, finish the task, then list the gap and one proposed line in the reply. Stop mid-task only for something that cannot be undone.
6. Run the module's checklist before delivering. A self-check costs less than a review round with Gen.

## Where the files live
- Master copy: the project docs under `brand/`. Mirror: Mac `5 Laws of Lasting Change/Brand/Guide/`.
- Edit the master first, then mirror. If the two differ, the master wins.

## Drift protection (added 30 Oct 2026)
1. The coach-gen-brand skill loads this guide in any chat that makes a Coach Gen visual or public copy.
2. The project instructions carry a short brand rule.
3. Workflow skills (video, posting) load their modules.
4. Memory records where the guide lives.
5. Outside tools get BRIEF-HEADER.md and ANTIGRAVITY-RULES.md.
6. A monthly scheduled drift check reads the live site and Instagram and saves claude/Brand_Drift_Report_YYYY-MM.md.
Any agent that finds old material (Coach Wibawa, Bebas Neue, yellow captions, gradients) lists it as a drift finding in its reply.

## Changing the guide
- Only Gen approves changes. Add and annotate, never condense or delete. When a rule changes, keep the old line and add a CORRECTION line under it with the date and his words.
- Every change gets a line in 99_CHANGELOG.md and a version bump.

## Links (added 30 Oct 2026, v1.3)
| Task | Load |
|---|---|
| Adding, changing, or publishing any link, handle, or URL (bios, buttons, signatures, QR codes, website) | + 19_LINKS.md |
Rule: publish a link only when 19_LINKS shows it LIVE with a verified date. Everything public points to coachwibawa.com or a hub path on it.

## Brand audit (added 31 Oct 2026, v1.4)
| Task | Load |
|---|---|
| Taking or reading snapshots of Gen's pages and profiles, a before and after record, or the monthly drift compare | + 20_BRAND-AUDIT.md and 19_LINKS.md |
The snapshot library is the Google Drive folder "Coach Gen Brand Snapshots". The index is 19_LINKS section 7. Read the text files there before opening a browser to answer "what does page X say".
