# L3 Link Fix Brief for Antigravity (coachwibawa.com)

Version 1.0, 1 Nov 2026. Written by Claude for Genison Wibawa. Source: brand/19_LINKS.md, the 31 Oct snapshot baseline, and the 1 Nov drift report.
How to use: open the coachwibawa.com workspace in Antigravity and paste everything below the line. When Antigravity says it has deployed, tell Claude "L3 deployed". Claude then checks every link in a browser and marks it LIVE in the link map.

---

BRAND RULES (follow exactly, do not invent a style)

- Names: Coach Gen is the company and logo. Genison Wibawa is the person. Never write "Coach Wibawa". Instagram handle: @coachgenofficial.
- Fonts: only Montserrat (headings, buttons, labels, captions) and Libre Baskerville (reading text, quotes). Both from Google Fonts.
- Colors, blue family (default for everything): Abyss #01131C, Deep Water #0D4A59, Aqua #72CCD0, Mist #EAF5F6.
- Colors, gold family (only for the book, Lasting Change Letters, speaking, and paid program documents): Charcoal #2B2B2B, Gold #C8B796, Deep Gold #9A8360, Ivory #F6F2EA.
- One family per piece. Never put Gold and Aqua in the same design. No other colors.
- Shapes: square corners (0, or 4 px on buttons and inputs). No gradients, glows, drop shadows, or diagonal elements.
- Text on photos always sits on a solid color panel. Real photos of Genison only. No stock people, no AI-made people.
- Voice: first person "I", never "we". Plain words, British spelling, numbers as digits, no em dashes, no emojis.
- Logo: use the files from the Coach Gen logo kit as they are. Do not redraw, recolor, stretch, or add effects.
- Design tokens: tokens.css and tokens.json (attached). Use their values, not your own.
- If something is not covered here, ask Genison. Do not guess.

---

## SCOPE OF THIS TASK: LINKS ONLY

This task changes links and redirects only.
Do not change any visible text, names, colors, fonts, images, or layout in this task, even where they break the brand rules above. The full rebrand is a separate task that comes later. If you see something else wrong, list it at the end of your reply. Do not fix it now.

## TASK 1. Find out how redirects work on this site

1. Tell me how the site is built and hosted (for example Vite + React on Vercel, Netlify, Firebase Hosting, Cloudflare Pages).
2. Use the host's own redirect config if it has one (vercel.json "redirects", Netlify "_redirects", firebase.json "redirects", Cloudflare "_redirects"). These are real server redirects.
3. Only if the host has no redirect config: add a client-side route for each path that calls `window.location.replace(<target>)` straight away, with no page flash.
4. Note: today every unknown path returns HTTP 200 and shows an "Oops! Page not found" screen. Keep that behaviour for unknown paths in this task. Only the paths below change.

## TASK 2. Add these redirects

Hub paths. These point to outside profiles that will change later, so use a TEMPORARY redirect (302 or 307). Do NOT use 301 here: browsers remember a 301 forever and a later change would not reach visitors.

| Path | Redirects to | Type |
|---|---|---|
| /linkedin | https://www.linkedin.com/in/coachwibawa/ | 302 |
| /instagram | https://www.instagram.com/coachgenofficial/ | 302 |
| /youtube | https://www.youtube.com/@coachgenofficial | 302 |
| /whatsapp | https://tinyurl.com/InsideTheIntrovertCircle | 302 |
| /chat | https://wa.me/6582509098 | 302 |
| /facebook | https://www.facebook.com/profile.php?id=61593414951464 | 302 |
| /book | /contact | 302 (will point to a booking page later) |

Old pages that are gone. These are permanent, so use 301.

| Path | Redirects to | Type |
|---|---|---|
| /framework | /about/system | 301 |
| /products | / | 301 |
| /paths | /#paths | 301 |

For /paths: give the "Paths that align with who you are" section on the home page the id `paths`, so /#paths scrolls to it.

## TASK 3. Change these links on the site

Search the whole codebase (components, layout, footer, data files, config) for each old value and replace it. List every file you changed.

| Where | Link text | Old target | New target |
|---|---|---|---|
| Footer, Connect icons | LinkedIn | https://www.linkedin.com/in/genison-wibawa/ | /linkedin |
| Footer, Connect icons | Instagram | https://www.instagram.com/coachwibawa/ | /instagram |
| Footer, Connect icons | WhatsApp Inner Circle | https://tinyurl.com/InsideTheIntrovertCircle | /whatsapp |
| Footer, Connect icons | WhatsApp | https://wa.me/6582509098 | /chat |
| Footer, Quick Links | Framework | /framework | /about/system |
| Footer, Quick Links | Products | /products | /coaching/executive-coaching |
| Home, paths section | Choose your path | /paths | /#paths |
| Home, bottom | Join Inner Circle | https://tinyurl.com/InsideTheIntrovertCircle | /whatsapp |
| Home, bottom | Ask on WhatsApp | https://wa.me/6582509098 | /chat |
| Home, bottom | Connect on LinkedIn | https://www.linkedin.com/in/coachwibawa/ | /linkedin |
| /about, bottom | View Our Services | /products | /coaching/executive-coaching |
| /contact, Book a Call card | View Our Services | /products | /coaching/executive-coaching |
| /contact, WhatsApp card | Chat with Advisor | https://wa.me/6582509098 | /chat |
| /contact, WhatsApp card | Join Inner Circle | https://tinyurl.com/InsideTheIntrovertCircle | /whatsapp |
| /paths/3keys-influence | Book Strategy Session | /contact | /book |
| /paths/6c-public-speaking | Book Discovery Call | /contact | /book |

Then search the codebase for any remaining copy of these strings and replace it the same way:
- `linkedin.com/in/genison-wibawa` and `linkedin.com/in/coachwibawa` to `/linkedin`
- `instagram.com/coachwibawa` to `/instagram`
- `youtube.com/@coachwibawa` and `youtube.com/@CoachWibawaACC` to `/youtube`
- `tinyurl.com/InsideTheIntrovertCircle` to `/whatsapp`
- `wa.me/6582509098` to `/chat`
- `"/products"` to `/coaching/executive-coaching`, `"/framework"` to `/about/system`, `"/paths"` (exact, not `/paths/...`) to `/#paths`

Leave these alone: the Linktree icon (linktr.ee/coachwibawa), the email address genison@coachwibawa.com, every `/paths/<name>` page link, and all other internal links.

Links that open another site (all the hub paths except /book) open in a new tab, with `rel="noopener"`. Internal links open in the same tab.

## TASK 4. Check before you finish

1. Open each path in TASK 2 on the deployed site and write down where it lands.
2. Open the home page, /about, /contact, /paths/3keys-influence and /paths/6c-public-speaking, and click every link in the TASK 3 table. Write down where each one lands.
3. Confirm no link anywhere still points to /products, /framework, /paths (exact), genison-wibawa, or instagram.com/coachwibawa.
4. Reply with: hosting type, redirect method used, files changed, and the two lists from steps 1 and 2. Also list anything else you noticed but did not fix.
