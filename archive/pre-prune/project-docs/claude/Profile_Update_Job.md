# Profile Update Job (queued, 30 Oct 2026)

Goal: bring every live Coach Gen profile in line with the brand guide (project docs `brand/`). Copy comes from `brand/18_COPY-KITS.md`, images from the logo kit and the templates. Claude fills each platform in Gen's logged-in Chrome. Gen handles logins, codes, deletions, and payments, and says go once per platform before anything is saved.

Load first: `brand/00_START-HERE.md`, `brand/01_CORE.md`, `brand/02_VOICE.md`, `brand/18_COPY-KITS.md`, and the coach-gen-brand skill. Use the chrome-browser skill for the browser.

## Order and status
| # | Platform | What changes | Who | Status |
|---|---|---|---|---|
| 1 | Instagram @coachgenofficial | Handle (done). Name field, bio, link to start-here, highlight covers, 3 pinned posts | Claude fills, Gen says go | Handle done 30 Oct |
| 2 | LinkedIn (/in/coachwibawa) | Name "Genison Wibawa", headline v2, About, banner, URL to /in/coachgenofficial, role "Founder and Coach, Coach Gen (PT Gapai Bangkit Wibawa)" replacing "The Communication Engineer Lab", Featured | Claude fills, Gen says go | Open |
| 3 | Facebook Page (Coach Gen) | Intro, About with the Indonesian line (after his yes), cover, profile picture | Claude fills, Gen says go | Open |
| 4 | Facebook personal (Genison Bertholino) | Bio line pointing to the Page, drop "Introvert's coach" | Claude fills, Gen says go | Open |
| 5 | WhatsApp group | Phase 1 name and description, group icon (wa_icon template) | Gen (WhatsApp is on his phone) or Claude through the WhatsApp tools if allowed | Open |
| 6 | YouTube @coachwibawa | Hide the old channel (Gen said go on 30 Oct). Deleting stays Gen's own step if he wants it later | Claude hides, Gen signs in | DONE 30 Oct: Gen hid the coachwibawa@gmail.com channel (@CoachWibawa) |
| 6b | YouTube, found 30 Oct | Chrome is signed in to 5 Google accounts, each with an empty channel (0 subscribers): genison@coachwibawa.com "Coach Wibawa" @CoachWibawaOfficial, coachwibawa@gmail.com "Coach Wibawa" (the Linktree one), onewiththousandzero@gmail.com "Ano nymous", genisonwibawa@gmail.com "Genison Wibawa", wibawagenisonb@gmail.com "CoachWibawa". The hide page for the coachwibawa@gmail.com channel is open in Chrome and needs Gen's password | Gen signs in | Waiting on Gen |
| 7 | YouTube @coachgenofficial | New channel on his work email (genison@coachwibawa.com): Gen creates the channel, then Claude sets name, handle, description, banner, profile picture | Gen creates, Claude fills | Next |
| 7b | Done 30 Oct (Gen's go) | Work-email channel renamed: name "Coach Gen (Genison Wibawa)", handle @coachgenofficial (youtube.com/@coachgenofficial works, the old handle display may take a while to update), description set. Still open: banner and profile picture, which Gen uploads (the browser extension cannot upload files): Brand/CoachGen-Logo-Kit/03_Social/YouTube-banner/coachgen_youtube-banner_blue_on-dark_2560x1440.png and Profile-picture/coachgen_avatar_blue_on-dark_1080.png | Gen uploads 2 images | Mostly done |
| 6c | YouTube wibawagenisonb@gmail.com "CoachWibawa" | Possibly the old "terrible" channel. Hide it the same way (Studio, Settings, Channel, Advanced settings, Remove YouTube content, hide) | Gen | Open |
| 8 | Linktree (coachwibawa) | Retire once start-here is live. Until then: name, bio, link order | Claude fills, Gen says go | Open |
| 9 | Website (Antigravity) | Brief with ANTIGRAVITY-RULES.md: start-here page, fix the footer LinkedIn link (404) and /framework and /products (404), retire "Coach Wibawa", two fonts only, new logo, update the LinkedIn link after the URL change | Gen runs Antigravity with Claude's brief | Open |
| 10 | cal.com | Event "First Coaching Session (paid)", the free-call application, confirmation and reminder messages, brand color and avatar | Claude fills, Gen connects payment | Open |
| 11 | Gmail signature | Signature from the logo kit and copy kit | Claude fills, Gen says go | Open |

## Open answers needed from Gen
1. The Indonesian Facebook About line: "Untuk kamu yang selalu mulai, tapi nggak pernah selesai."
2. ANSWERED 30 Oct: paid first session is 60 minutes. The free call is 5 minutes. No reply time is promised.
3. Free-call criteria.

## Rules for the run
- Never type passwords or codes. Stop at every login and wait.
- Before saving each platform, show Gen what will change and wait for his go.
- Never delete anything. Never click post, publish, or pay.
- Old URLs break when a handle or URL changes: update every place that links to it the same day (site, Linktree, email signature, bios).

## Update 30 Oct 2026, 14:32 (added, nothing above changed)
- Gen reports done: YouTube banner and profile picture uploaded (row 7b). Old channels @CoachWibawa and @CoachWibawaACC hidden by Gen (rows 6, 6b, 6c). Fonts installed. Skill cards saved. Brand rule pasted in project instructions.
- Open answers 1 and 3 ANSWERED 30 Oct: Indonesian line approved. Free-call wording settled in brand/18_COPY-KITS.md section 13 (no criteria stated publicly).
- Rule change for the run, from Gen 30 Oct: be proactive on socials. Claude does the clicking and uploading. Uploads go through the Chrome extension's file_upload tool with Mac folder paths. Gen still does passwords, codes, deletions, and payments.
- The step-by-step plan for everything left now lives in claude/Brand_Rollout_Plan.md. Work from that plan and log progress there.
