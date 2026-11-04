# 20 Brand Audit (snapshot library of every page and profile)

Version 1.0, 31 Oct 2026 (Opus). Owner and only approver: Genison Wibawa. Add-only like every brand file.
Load with `brand/19_LINKS.md`. Same keys, same places. 19_LINKS says where links go. This file records what each place looked like and said, on a date.

Gen's ask (31 Oct): "a library of screenshots of my pages and socials ... for reference for future ai and myself. should also be synergistic with the link map."

## 1. What it is for
1. **Before and after record of the rebrand.** The old brand is being replaced now. Once a page changes, its old state is gone unless it was captured.
2. **Proof for the link map.** When a row in 19_LINKS moves to LIVE, the snapshot taken that day shows what the page looked like when it was verified.
3. **Reference without a browser.** A later chat (or Gen) reads the text file to answer "what does the Instagram bio say" or "what is in the site footer" without opening anything.
4. **Drift check.** The monthly check compares new text with the last text. Only pages that changed need new screenshots.

Not for: every post, every story, every article. Profiles and pages only.

## 2. Where it lives
- **Library:** Google Drive folder **Coach Gen Brand Snapshots** (owner genison@coachwibawa.com).
  - Folder ID: `1c82sI6UQ5p-eptG-O5kI4pR2GowcfIs-`
  - Link: https://drive.google.com/drive/folders/1c82sI6UQ5p-eptG-O5kI4pR2GowcfIs-
- **Index:** `brand/19_LINKS.md` section 7 (one row per key, latest snapshot date). Never a second index anywhere else.
- Why Drive and not the Mac: the browser can drop a screenshot straight into a Drive folder. Getting an image onto the Mac would mean passing the whole file through the chat each time, which costs many tokens per image. Gen sees Drive on his phone and Mac.
- Do NOT write snapshot text into the project. Project writes reset the cache for every chat in the project.

## 3. File names
`<key>_<YYYY-MM-DD>_desktop_<nn>.jpg` for screenshots, numbered from the top of the page: 01, 02, 03.
`<key>_<YYYY-MM-DD>.txt` for the text file. One text file per key per date.
- `<key>` is the key from 19_LINKS section 2 (site, start-here, linkedin, instagram, youtube, linktree, facebook) or a site path key from section 4 below (about, contact, path-6c, and so on).
- Lowercase, hyphens only, no spaces.
- Example: `site_2026-10-31_desktop_01.jpg`, `site_2026-10-31.txt`.
- First test file already in the folder: `site_2026-10-31_desktop_01.jpg` (home page, first screen, old brand). Counts as the baseline's first image.

## 4. What to capture (the checklist)
Shots = how many screens to capture, from the top. Text = the text file (section 5).

| Key | Address | Shots | Notes |
|---|---|---|---|
| site | coachwibawa.com | full page, max 8 | Home. Headline animates: wait 6 seconds before the first shot |
| start-here | coachwibawa.com/start-here | 3 | |
| about | coachwibawa.com/about | 3 | |
| contact | coachwibawa.com/contact | 2 | |
| path-itt | coachwibawa.com/paths/inside-the-introvert | 2 | |
| path-3keys | coachwibawa.com/paths/3keys-influence | 2 | |
| path-6c | coachwibawa.com/paths/6c-public-speaking | 2 | |
| path-eoi | coachwibawa.com/paths/engineer-of-influence | 2 | |
| path-mindset | coachwibawa.com/paths/mindset-mastery | 2 | |
| path-podcast | coachwibawa.com/paths/podcast | 2 | |
| ila | coachwibawa.com/introversion-leverage-assessment | 2 | |
| assessments | coachwibawa.com/resources/assessments | 2 | |
| assessment | coachwibawa.com/assessment | 1 | |
| newsletter | coachwibawa.com/inside-the-introvert-newsletter | 1 | |
| articles | coachwibawa.com/inside-the-introvert-articles | 1 | |
| footer | (bottom of coachwibawa.com) | 1 | The footer holds the dead links. Its own shot, scrolled to the very bottom |
| linkedin | linkedin.com/in/coachwibawa | 3 | Top card, About, Experience. Owner view. Stop before "People also viewed" |
| instagram | instagram.com/coachgenofficial | 1 | Profile header, bio, highlights, first row of posts. get_page_text is blocked on Instagram: type the bio, name, link and highlight names into the text file from the screenshot (zoom in) |
| youtube | youtube.com/@coachgenofficial | 2 | Channel home, then the About panel (description and links) |
| linktree | linktr.ee/coachwibawa | 1 | Public page, not the admin |
| facebook | Coach Gen Page | 2 | Page URL is VERIFY in 19_LINKS. Find it from Gen's profile, record the URL in the text file, tell Gen. Do not edit anything |
| facebook-personal | Gen's personal profile | 1 | Intro box only. Nothing else from his personal profile |
| wa-group | WhatsApp group | 0 | Optional. Phone only. Skip unless Gen sends a screenshot himself |

Privacy: capture only Gen's own pages and profiles. Never open or capture messages, inboxes, notifications, or other people's profiles. If a sidebar shows other people (LinkedIn "People you may know"), keep it out of the shot by stopping above it.

## 5. How to capture (tested 31 Oct 2026 in Claude in Chrome)
Use **Claude in Chrome** (the extension). Load the tools in one ToolSearch call: tabs_context_mcp, tabs_create_mcp, navigate, computer, javascript_tool, get_page_text, upload_image, browser_batch, plus the Google Drive tools search_files and create_file.

Setup, once per session:
1. Open two tabs: tab A for the page, tab B for the Drive folder link in section 2.

Screenshots, per key:
1. Tab A: navigate to the address. Wait 3 seconds (6 for the home page).
2. Scroll to the top: javascript_tool `window.scrollTo(0,0)`.
3. `computer` screenshot of tab A (full scale, not 0.6). Note the screenshot ID.
4. Straight away: `upload_image` with that ID, `tabId` = tab B, `coordinate` [700, 450], `filename` per section 3. Screenshot IDs expire after a few minutes, so upload each one right after taking it.
5. Next screen: javascript_tool `window.scrollBy(0, Math.round(innerHeight*0.9))`, wait 2 seconds, repeat steps 3 and 4 with the next number. Stop at the Shots count or at the page bottom.
6. Batch steps 1 to 5 with browser_batch where possible.

Text file, per key:
1. `get_page_text` on tab A (gives the main content, but skips header and footer).
2. javascript_tool for title, description and every link. The tool cuts output at about 1,000 characters, so read links in pages of 10:
   `const u=[...new Set([...document.querySelectorAll('a[href]')].map(a=>((a.innerText||a.getAttribute('aria-label')||'').trim().replace(/\s+/g,' ').slice(0,40))+' -> '+a.href))]; 'TOTAL '+u.length+'\n'+u.slice(0,10).join('\n')` then `slice(10,20)` and so on.
   First call only: add `'TITLE: '+document.title+'\nDESC: '+(document.querySelector('meta[name=description]')?.content||'')`.
3. Google Drive `create_file`: title `<key>_<date>.txt`, parentId the folder ID, contentMimeType `text/plain`, disableConversionToGoogleType true, textContent in this layout:

```
KEY: <key>
ADDRESS: <address>
CAPTURED: <YYYY-MM-DD HH:MM> Asia/Jakarta, by <model>
VIEW: desktop, logged in as owner | logged out
SHOTS: <key>_<date>_desktop_01.jpg to _0N.jpg
TITLE: ...
DESC: ...

TEXT:
<get_page_text output, or typed from the screenshot for Instagram>

LINKS (<n>):
<text -> href, one per line>

NOTES:
<anything odd: old brand names, dead links, wrong numbers, mid-animation text>
```

Checks before moving on: `search_files` with `parentId = '<folder ID>'` shows the new files. Open one image in tab B once per session to see it is the right page.

Known limits (31 Oct 2026):
- Desktop view only. `resize_window` reported success but the window stayed 1280 wide. Phone view: skip until a method works.
- Screenshots are one screen each, not one long page image.
- The workspace shell and Gen's Mac shell cannot open his site (network blocked), so no Playwright route.
- Instagram blocks get_page_text: type the text from the screenshot.

## 6. When to capture
| Moment | What | Who |
|---|---|---|
| Baseline (now, before L3 changes the site) | Every key in section 4 | Sonnet, medium (rollout plan step S1) |
| After any rollout step | The keys that step touched. Part of verifying the step | The model doing the step |
| Monthly drift check | Text files only, every key. Compare with the last text file. New screenshots only for keys whose text changed | The monthly check |
| Gen asks | Whatever he names | Any |

Old snapshots are never deleted or overwritten. A new date means a new file.

## 7. Comparing two dates
1. Read the two text files for the key (Drive `read_file_content` or `download_file_content`).
2. List what changed: title, description, bio lines, links (added, removed, changed target), and any old brand words ("Coach Wibawa", "we", old handles).
3. Any link change is checked against 19_LINKS section 2. A link to a target that is not LIVE goes in the report as a problem.
4. Report in plain lines. Do not fix anything without Gen's go.

## 8. Change log (add lines only)
- 31 Oct 2026: file created (Opus). Method tested: Chrome screenshot dropped into the Drive folder with upload_image works. Copying images from Drive to the Mac was not used: it passes each whole image through the chat, too many tokens per image, so Drive is the library. get_page_text skips header and footer, so links come from a short script. Window resize did not work. First file: site_2026-10-31_desktop_01.jpg.
- 31 Oct 2026 (Sonnet), baseline S1 mostly done. Deviations: (1) text files are combined for some keys (paths_ holds the six path pages, site-other-pages_ holds five) to save calls. (2) One or two screens per page, not full pages, so shots show the top only. (3) LinkedIn has 1 shot only, because the sidebar shows other people. (4) site home has 2 shots of about 10 screens, text holds the rest. (5) Every page returns HTTP 200, even missing ones: judge a page by its text, never by status. (6) The page-text tool skips header and footer: links come from javascript_tool. NOT DONE: facebook Page, facebook personal, /terms /privacy /refund, mobile views.
- 31 Oct 2026, Gen's motivation (his words): "to have 1 place to see the afters; and still one place if in the future I create more pages etc." So: (a) the Drive folder is that one place. (b) NEW PAGE RULE: every new page, profile, or link a chat creates gets (i) a row in 19_LINKS section 2 and section 7, (ii) a row in section 4 of this file, (iii) a snapshot in the folder the same day, taken after it is live. (c) TO BUILD: a one-page index Gen can open ("Afters board"), listing each key with its latest shot and date, so he need not browse files. Not built yet.
- 1 Nov 2026 (Opus): S1 leftovers done: facebook (Page) and terms, privacy, refund (legal-pages_ text file). Still not captured: facebook-personal (needs switching from the Page to Gen's personal profile, do it in plan step 2.4) and the 9 extra site pages found by the drift check (see 19_LINKS change log, 1 Nov), which get their first snapshot when L3 or Phase 5 touches them. Add those 9 as rows in section 4 when captured.
- 1 Nov 2026: the monthly drift check (claude/Brand_Drift_Report_2026-11.md) read the same pages on its own. Next month it should compare against the Drive text files (section 7) instead of re-reading everything.
