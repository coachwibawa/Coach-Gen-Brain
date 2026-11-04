# Brand drift report, November 2026

Run: 1 Nov 2026, 14:20 UTC (21:20 Jakarta), monthly scheduled check. Read only. Nothing was changed on the site, Instagram, or any account.
Read: brand/00_START-HERE.md, 01_CORE.md, 13_WEB.md, 99_CHANGELOG.md (project master), plus 19_LINKS.md and 20_BRAND-AUDIT.md for the known-issue baseline.
Checked: coachwibawa.com home, every page in the five menu dropdowns (About, Paths, Articles, Resources, Coaching), every footer page, and instagram.com/coachgenofficial logged out.

Short version: since the 30 and 31 Oct baseline, nothing on the site or Instagram has changed. Both still show the old brand in full. Every finding below was expected before rollout Phase 2 (Instagram) and Phase 5 (site), so none is a new break. Each one is still live, though, and the top three are the ones visitors see first.

## Top 3

1. The site still shows "Coach Wibawa" on every page: header logo, footer, copyright, page titles ("The Official Website of Coach Wibawa: The Introvert's Executive Coach"), meta author "Coach Wibawa Team", About h1 "The story behind Coach Wibawa", and testimonials. Breaks 01_CORE s1 and s9.8, 13_WEB s5. Fix: rollout Phase 5 rebuild, with titles set to "<Page name> | Coach Gen" and author Genison Wibawa.
2. The site loads the wrong fonts and colors. It loads Oswald, Outfit and Libre Baskerville from Google Fonts. Body text is set in Manrope, which is never loaded, so it falls back to the system font. Montserrat is not loaded at all. Main colors are teal #2B9CAB, navy #1D3658, #1D2530, grey #627084 and #E0E6EB, none of them in the palette. The home page also has 13 gradient layers, 22 shadows or glows, and 67 elements rounded over 4 px. Breaks 01_CORE s4, s5 and s6, 13_WEB s1 and s6.1 to s6.2. Fix: Antigravity rebuild with tokens.css and the 13_WEB s1 brief line.
3. Instagram is not rebranded yet. Name field: "Coach Gen 源 Official". No bridge line, no title line, and the bio link is bit.ly/officialcoachgen plus 2 more, not a coachwibawa.com hub path. Highlight covers are white circles with black line icons, not the template. The last 9 posts (newest 24 Aug 2026) use a typewriter font, a Trajan-style serif, red "MYTH" and "LIE" labels, rounded cards, glow streaks and gradients, with no corner mark. Breaks 01_CORE s1, s4, s5, s6 and s9, and 19_LINKS s1 rule 1. Fix: rollout Phase 2. Bio from 18_COPY-KITS with "Coach Gen (Genison Wibawa)" and "International Coach & Author", covers from the highlight_covers template (17_TEMPLATES), link to coachwibawa.com once LIVE in 19_LINKS. New posts only from the 11_SOCIAL templates. Old posts can stay as an archive.

## All findings

### Website, coachwibawa.com

- Every page, names: "Coach Wibawa" in header logo, footer brand line, "Connect Coach Wibawa", "© 2026 Coach Wibawa". Rule: 01_CORE s1, s9.8. Fix: Coach Gen logo (blue family) and "© 2026 PT Gapai Bangkit Wibawa" or "Coach Gen" per 14_DOCS.
- Page titles: home "The Introvert's Executive Coach | Coach Wibawa | Executive Coach for Introverts". Start Here, ILA and ROI calculator end in "| Coach Wibawa". Every other page uses the same generic "The Official Website of Coach Wibawa: The Introvert's Executive Coach". Rule: 13_WEB s5. Fix: "<Page name> | Coach Gen" on every page.
- Home meta: author "Coach Wibawa Team". Description says "Public speaking coaching team". Rule: 13_WEB s5, 01_CORE s3 voice. Fix: author "Genison Wibawa", description in "I" voice about the 5 Laws.
- Fonts, whole site: Oswald, Outfit and Libre Baskerville are loaded. Manrope is used but not loaded. Montserrat is missing. Rule: 01_CORE s5, 13_WEB s6.1. Fix: load only Montserrat (400, 600, 700, 800) and Libre Baskerville.
- Colors, whole site: teal #2B9CAB, navy #1D3658, dark #1D2530, grey #627084, light grey #E0E6EB. Rule: 01_CORE s4.3. Fix: map to Deep Water, Abyss, Aqua and Mist via tokens.css.
- Gradients, glows, shadows, radius: hero and path cards use linear gradients. Buttons and cards have drop shadows. A pulse glow sits on the "Now accepting" dot. Rounded corners appear well over 4 px. Rule: 01_CORE s6 and s9.3, 13_WEB s6.2. Fix: flat panels, radius 0 (4 px on buttons and inputs).
- "We" voice on home ("What our clients say", "We don't teach acting. We engineer..."), /about ("our founder", "The Engineers Behind The Coach"), /about/story, /about/system, /about/science (9 uses), /coaching/executive-coaching (8), /coaching/life-journey-mastery, /resources/assessments, /resources/citations, /resources/roi-calculator, and the path pages for Inside The Introvert, 3 Keys, 6C and Podcast. Rule: 01_CORE s3 and s9.4, 13_WEB s6.3. Fix: rewrite in "I". The legal pages (/terms, /privacy, /refund) also say "we". They can stay formal but should name PT Gapai Bangkit Wibawa.
- Title line under his name on home: "Genison Wibawa, B.Eng., CPC / Public Speaking Coach for Introverts". This line is not in the approved list. Rule: 01_CORE s2. Fix: "Certified Professional Coach (CPC)" on coaching pages or "International Coach & Author" as the default.
- Menu and footer links that land on a 404 screen: /paths (home "Choose your path" link), /framework (footer), /products (footer, plus contact "Book a Call" and About "View Our Services"). Rule: 13_WEB s6.4, 19_LINKS s1 rule 4. Fix: the PLANNED redirects in 19_LINKS s3. Every menu dropdown link (27 pages) opens a real page.
- Footer external links: linkedin.com/in/genison-wibawa (DEAD), instagram.com/coachwibawa (OLD, released handle), linktr.ee/coachwibawa (LIVE, OLD). Rule: 19_LINKS s1 rules 1 and 2. Fix: hub paths /linkedin and /instagram once built. Until then use linkedin.com/in/coachwibawa and instagram.com/coachgenofficial.
- Home statistics: "% of engineers deemed unemployable", "% salary increase", "$B annual US cost" carry a single line, "Source: International Journal of Management and Humanities", with no paper, author or year. The counters also read 0% until scrolled. Rule: 01_CORE s3 proof, 13_WEB s4 and s6.5. Fix: full citation in the same view, or move them to a track page, sourced.
- ROI calculator on the home page ("Calculate your lost potential", "Based on US-based research", no source shown). Rule: 13_WEB s4 CORRECTION (tools live on track pages, the 5 Laws diagnostic is the one home tool). Fix: remove it from home and keep /resources/roi-calculator as a track tool with sources.
- Method section on home is "The Three Transformation Keys", not the 5 Laws. Rule: 13_WEB s4 ADDED, 01_CORE s3. Fix: 5 Laws method section with the maze-line progress motif.
- Home positioning: hero "The Introvert's Executive Coach" and paths led by introvert offers. Rule: 01_CORE s3 CORRECTION (Lasting Change is the flagship, Introverts is one track). Fix: lead with the 5 Laws promise line.
- Testimonials: Dan Sato, Mira K. and Gurun P. (home carousel), alongside Wayan Perdana and Julie. Not confirmed in this run. Rule: 01_CORE s3 and s9.5, 13_WEB s6.5. Fix: Gen confirms each one is a real client who gave permission. Drop any that is not.
- Article category pages /introverts-public-speaking and /introverts-energy-management are almost empty: one teaser each, the first with a placeholder quote ("one small step for man"). Rule: 90_TASTE (judgment). Fix: hide empty categories from the menu until they hold articles.
- /resources/citations lists entries as "External Research Paper [1]" with no visible titles in the first screen. Rule: 01_CORE s3. Fix: check that each entry names the paper. Not read in full this run.
- /privacy shows "Last updated: November 1, 2026", today's date, so the field is probably generated live. Low priority. Fix: set a fixed date.

### Instagram, instagram.com/coachgenofficial (logged out)

- Name field: "Coach Gen 源 Official". The kanji is not in the naming rule, and there is no bridge line. Rule: 01_CORE s1, 02_VOICE bios. Fix: name per 18_COPY-KITS Instagram, with "Coach Gen (Genison Wibawa)" until about Feb 2027.
- Bio: "I liberate those who always start but never finish. If you're tired of following others's plan, Let's do it your way. 👇 Freedom is free." It has no title line, a typo ("others's"), a capital "Let's" mid-sentence, and an emoji. Rule: 01_CORE s2, 18_COPY-KITS, Language Rules. Fix: the 18_COPY-KITS Instagram bio.
- Bio link: bit.ly/officialcoachgen plus 2 more. Rule: 19_LINKS s1 rules 1 and 2 (not LIVE in s2). Fix: coachwibawa.com or the start-here hub once LIVE.
- Highlight covers (CEOs Testimonies, Author, The Stage, TheAnti・Coach, WorstAdviceEver) are white circles with black icons, and two use badge logos with their own fonts. Rule: 17_TEMPLATES highlight covers, 01_CORE s4. Fix: render covers with cg_render.py.
- Last 9 posts (pinned 3-tile "Liberate Yourself" set from 3 Jul plus reels from 10 to 24 Aug): typewriter monospace and Trajan-style serif type, white glow streaks on black, red-coral MYTH and LIE labels, rounded translucent cards, gradient backgrounds, no Coach Gen corner mark. Old yellow or orange captions were not seen in the grid thumbnails. Rule: 01_CORE s4, s5, s6 and s9, 11_SOCIAL. Fix: new posts from 11_SOCIAL templates only. No post has gone up since 24 Aug, so nothing new has drifted.

### Guide health

- Every project file named in 00_START-HERE exists: 01_CORE, 02_VOICE, 10_VIDEO to 18_COPY-KITS, 19_LINKS, 20_BRAND-AUDIT, 90_TASTE, 99_CHANGELOG, BRIEF-HEADER, ANTIGRAVITY-RULES, tokens.json, tokens.css, templates/cg_render.py, Coach_Gen_Language_Rules.md, claude/Coach_Gen_Book_Rules.md, claude/Coach_Gen_Social_Posting_Rules.md, claude/Reel_Style_Guide.md, claude/Brand_Direction_Phase1.md.
- Not checked: Brand/CoachGen-Logo-Kit/, LOGO-USAGE.md and the Brand/Guide mirror on the Mac. No Mac folder was connected to this run. Fix: connect the "5 Laws of Lasting Change" folder to the scheduled task, or check by hand.
- Changelog has lines for v1.0, v1.1, v1.2, v1.3 and v1.4. Clean.
- 00_START-HERE header still says "Version 1.1, 30 Oct 2026" while its sections and the changelog reach v1.4. Rule: 00_START-HERE "Changing the guide" (version bump). Fix: add a line under the header, "Current version 1.4, 31 Oct 2026", keeping the old line.
- Drift protection item 1: the coach-gen-brand skill did not appear in this run's skill list. Rule: 00_START-HERE "Drift protection" 1. Fix: check that the skill is saved to Gen's account and switched on.
- Project instructions still open with "Coach Wibawa (Coach Gen), ICF-certified coach". Rule: 01_CORE s1. Fix: "Genison Wibawa (Coach Gen), ICF Associate Certified Coach (ACC)". Gen edits this in the project settings.

## What is clean

- All 27 pages in the five menu dropdowns open real pages. No menu link lands on a 404. Only /paths, /framework and /products do, as logged on 30 Oct.
- The site loads no Bebas Neue, Anton or Geist.
- The contact email genison@coachwibawa.com and the wa.me/6582509098 and tinyurl WhatsApp links are the LIVE targets in 19_LINKS.
- The Instagram handle is @coachgenofficial as decided, and the profile photo is a real headshot.
- No new drift since the baseline: no new posts, pages or links in old styling have appeared since 31 Oct.
- Guide files and changelog are complete, apart from the version header noted above.

Next run: 1 Dec 2026. Compare against this report and the Drive snapshot texts.
