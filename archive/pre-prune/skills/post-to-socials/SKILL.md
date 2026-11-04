---
name: "post-to-socials"
description: "Manual only, invoke with /post-to-socials. Never trigger automatically from conversation; only run when Coach Gen explicitly types the command."
---

# Post to socials (browser-assist)

**Manual invocation only.** This skill runs only when Coach Gen explicitly types `/post-to-socials`. Do not invoke it on your own judgment because a message mentions posting, sharing, or publishing content, even content that sounds ready to go out. He has to type the command himself, every time. If a message of his sounds like it wants this done but doesn't invoke the command, say what you'd do and ask him to run `/post-to-socials` rather than just doing it. This skill controls his actual logged-in browser; starting it without being asked is exactly the kind of thing he does not want.

Turns one of his articles into platform-ready posts, lets him pick or approve the version, makes the image, then fills the post composer in his own logged-in Chrome and stops. He reviews and presses post himself. This never logs in anywhere, never clicks post, publish, share, send, next, or schedule, and never runs unattended.

## Arguments

- **What to post.** "latest", an article title, a Notion link, or pasted text. If a finished post was already picked or approved earlier in the same conversation, use that and skip to Step 5.
- **Platforms.** LinkedIn, Facebook, or both. Default is LinkedIn. A platform is ready only when it has its own section in `claude/Coach_Gen_Social_Posting_Rules.md`. If he names a platform without a section yet, say so and offer to build its section with him first (the way LinkedIn and Facebook were built), rather than guessing its rules. Instagram's web composer is unreliable for feed posts (it's built mobile-first); say so plainly if he asks for it.
- **Facebook part.** Facebook turns one article into 3 posts on 3 days. If he doesn't say which part (1/3, 2/3, 3/3), ask.

## Step 1: Find the article

His articles live in Notion:

- Inside The Introvert: data source `collection://d73333e2-807b-4aee-a4ce-0bb96ef282e7`
- Lasting Change Letters: data source `collection://409042c2-c5a3-4ebd-a21c-10621af68452`

"Latest" means the row with Status "Published" and the most recent Published At date across both boards. Pull the title, Insight 1 (the story), Insight 2 (the research), and Insight 3 (the question). Drop Insight 1's header line ("Insights from me, to you."). Insights 2 and 3 are raw material (for a flex, a later Facebook part, or a closing question), not text to paste in.

Work out the live URL in case a post needs a link. Use the Slug field if it's filled. If it's empty, Inside The Introvert pages default to `https://coachwibawa.com/inside-the-introvert-articles/<month>-<day>-<year>` from the Published At date, all lowercase (e.g. `october-12-2026`). The empty-slug pattern for Lasting Change Letters isn't known yet: ask him if that post needs a link.

## Step 2: Load the rules, fresh every run

Read `claude/Coach_Gen_Social_Posting_Rules.md` from the project every run, never from memory. It grows with every run. Apply the Shared section plus each target platform's section in full: confirmed rules (every CORRECTION line overrides the line above it), flex menu, mechanics, the Indonesian log for Facebook, and the Approved posts, which set the bar for shape and tone (never templates to copy).

Do not pull voice rules from `Coach_Gen_Language_Rules.md` (article voice) or `claude/Coach_Gen_Book_Rules.md` (book voice); they govern other pipelines. The project style still holds: simple words his less-fluent clients can read, active voice, no em dashes, no semicolons, Oxford comma, spelling and grammar fixed silently in his voice. Every claim must be true and on record, never invented.

**Looks come from the brand guide (added 30 Oct 2026).** For anything visual (the image, its colors, any text on it), load these project docs: `brand/00_START-HERE.md`, `brand/01_CORE.md`, `brand/11_SOCIAL.md`, and `brand/16_IMAGERY.md`. The guide covers looks only. Words still follow the Posting Rules above. Inside The Introvert and free content use the blue family. The book and Lasting Change Letters use the gold family.

## Step 3: Draft

The rules doc wins wherever it has moved on from the summaries below.

**LinkedIn: exactly 3 finished options.**

- Link or not: decide per post, and ask if the goal (reach or clicks) isn't clear. A link, when used, goes in the post body, never the first comment.
- Shape: the title, then the series and date line directly under it (e.g. "Inside The Introvert, October 12, 2026"), then the story. Ends with "Coach Gen".
- The title is the hook (the first 140-210 characters are all most people see before "see more").
- Story about 75-85% of the post. Keep the client story and stop before it settles into the client's private low point, or into the open loop the article sets up for its next part. On LinkedIn the turn comes from Coach Gen.
- Flex end about 15-25%: any number of flexes from the flex menu, varied between options, with at least one explicit callback to the story inside the flex sentence itself, played the way a good author calls back to an earlier line.
- Close with a question that pulls comments (it can carry the callback too), then up to 3 tightly relevant hashtags picked fresh. Type a space after the last hashtag before the line break (stops LinkedIn's suggestion from swapping it).
- Show the 3 options in chat. If they share the story, show it once, then each ending with its flex mix and callback named. Give a character count and the story share for each.

**Facebook: the 3-part plan, then the requested part.**

- First show a one-line plan for all 3 parts (one story beat per day, each able to stand alone for a cold scroller). Then draft the requested part.
- Line 1: the English title. Line 2: an Indonesian tag with the part label and the article's original date, the same date on all 3 parts, e.g. "Cerita klien (1/3): 12 October 2026". English and Indonesian both inside the first 2 sentences or 15 words.
- His story and personal voice in English. The reader's inner voice and the coaching close in Indonesian, in everyday register ("kamu", "nggak"), following the Indonesian log.
- Warm and bite-sized, no word-count target. Light flex at most. Ends with "Coach Gen" only, no series line.
- Hashtags and links: follow the doc's current state. If they're still open there, ask.

**Image prompt (any platform that gets an image).** Write one Nano Banana prompt from the template in `brand/16_IMAGERY.md`: minimalist, one object, lots of empty space on a flat dark background (Abyss #01131C with Aqua #72CCD0 as the only accent, or Charcoal #2B2B2B with Gold #C8B796 for the book and Lasting Change Letters), no people, at most a word or two of text, since every extra detail is another chance for AI artifacts. Show it with the draft. Keep a no-text fallback ready in case the lettering comes out wrong.

Don't open the browser until he picks or approves a version and the prompt.

## Step 4: Every run is an epoch (append-only doc)

`claude/Coach_Gen_Social_Posting_Rules.md` is append-only (see its no-delete rule and `claude/Coach_Gen_Protected_Docs.md`).

- When he corrects a draft or states a preference and a real rule falls out of it, propose the exact line. Once he agrees, add it to the right site section with the date and his words, plus a Calibration log entry with an overfitting check. Never derive a rule from an edit he didn't complain about. No comment is not a confirmation.
- If you misread him, keep the wrong line and add a CORRECTION line under it. Never delete, condense, merge, reorder, or rewrite a line.
- Add any post he picks or approves to that site's Approved posts.
- Never retype the doc. Edit a local copy with exact find-and-insert edits (the Edit tool), confirm every old line is still there, then upload those bytes with `project_write` and `local_path` (the file must sit inside the working directory). If this session has no local copy yet, read the doc and save it locally exactly as returned; after the upload, read it back and check every section heading and the latest log entries survived.
- A rule about looks (colors, fonts, image style) goes to the brand guide's change log for his approval, not into the Posting Rules.

## Step 5: Make the image, fill the composer, nothing else

Load the `chrome-browser` skill if it isn't loaded this session. Then load the tools in one `ToolSearch` call: `tabs_context_mcp`, `navigate`, `computer`, `read_page`, `find`, `browser_batch`, `get_page_text`, `tabs_create_mcp`, `tabs_close_mcp`. Batch predictable steps with `browser_batch`.

What the browser can and can't do (learned in live runs):

- Call `tabs_context_mcp` first. If the extension isn't connected, say so and stop. Don't retry, and don't fall back to the built-in browser pane without asking (it's a separate profile without his sign-ins).
- The extension only drives tabs inside its own tab group. It can't reach a tab he opened himself unless he moves it into the group. If the group is gone, a standalone `navigate` with no tabId creates a new one.
- "Permission denied" on navigation is the extension's site permission. Ask him to allow the site in the extension, then retry. Never work around it.
- If a site shows him logged out, stop and ask him to log in himself. Never type credentials.
- If a tool says it "couldn't determine which page", call `tabs_context_mcp` again and retry once.
- `file_upload` can't attach images here: it rejected files in the session's outputs folder and in his connected Mac folder. Use copy and paste instead (below).

### Image: prompt Gemini, then copy and paste (he okayed Claude prompting Gemini)

Use the Gemini tab in the group, or open `https://gemini.google.com/app` in the group's tab.

1. Start a new chat, choose the "Images" tool and the 1:1 ratio, type the approved prompt into "Describe your image", and press Enter. (Prompting steps not yet run live: verify with screenshots.)
2. Wait for the image (take a screenshot every few seconds, up to about a minute). Check it for AI slop: garbled letters, extra objects, odd edges. If the lettering is wrong, run the no-text fallback and tell him the word needs adding in Photopea.
3. Click the image to open its full view. It opens an editor with a sketch tool, so don't click on the image again there (that draws on it).
4. Click "Copy image" (top right, between the share and download icons; hover shows the label).
5. In the composer, click at the end of the post text and press `cmd+v` (his Mac). The image lands under "Uploaded media" on Facebook. Screenshot to confirm. On LinkedIn this paste route hasn't been tried yet: verify it, and if it fails, tell him the image is on his clipboard to paste himself.

Be accurate about metadata if he asks: Chrome re-encodes clipboard images, which most likely drops the file's metadata (including the C2PA tag), but that isn't verified from here. Gemini's invisible SynthID watermark lives in the pixels and survives screenshots and copies either way.

Fallback if paste fails: zoom-capture the image square from the full view with `save_to_disk: true`, copy it to `/mnt/user-data/outputs/`, send it to him with `SendUserFile`, and ask him to drag it into the composer.

### LinkedIn

1. Navigate to `https://www.linkedin.com/feed/` and take a screenshot.
2. Click "Start a post". The modal first loads as a grey skeleton, so wait about 2 seconds and screenshot again.
3. Click the "Share your thoughts..." box and type the whole post in one `type` action.
4. Paste the image if there is one (see Image above).
5. Verify: scroll the box to the top and bottom and screenshot both. It must start with the title, end where the post ends, have no leftover text, and no hashtag swapped.

If the composer already holds text: Ctrl+A and Delete don't clear LinkedIn's editor (it selects only one block and leaves a mix of old and new text). Close the modal with the X instead. The in-page "Save this post as a draft?" box is safe to click (it's not a browser dialog). Pick Discard only if the text is a draft Claude typed this session; if it could be his own draft, ask first. Then reopen "Start a post".

### Facebook (live-tested 2026-10-15)

1. Use the Facebook tab in the group, or navigate to `https://www.facebook.com/`.
2. Check the identity. The home composer must read "What's on your mind, Coach Gen?". If it shows his personal profile (Genison Bertholino), switch: click the top-right avatar, click "Coach Gen" in the menu, wait, and check the composer again. He approved this switch.
3. Click the "What's on your mind, Coach Gen?" box. The composer opens as a full page at `facebook.com/post/create`, with the text box top left and a live preview on the right. Wait about 2 seconds and screenshot.
4. Click into the text box and type the whole post in one `type` action.
5. Paste the image (see Image above). It appears under "Uploaded media" and in the preview.
6. Verify the text top and bottom, the tag line, and the image against the preview.
7. Point out, without touching them: the "Add AI label" toggle (Meta says it requires labels on certain realistic AI-made content; whether to switch it on is his call), and the "links left" counter if the post has a link.

**Never click Post, Publish, Share, Send, Next, Boost, or a schedule button, and never switch the AI label toggle.** Allowed: opening tabs, navigating, prompting Gemini, copying the image, switching to the Coach Gen identity, opening the composer, clicking into the text box, typing, pasting the image, scrolling, and closing or discarding a draft Claude typed. If a permission prompt appears, wait for him. If an element can't be found or a click doesn't land after 2 or 3 tries, stop and say what happened rather than guessing at coordinates.

## Step 6: Hand back

Tell him which platforms are ready for review and which failed or were skipped, and why. Paste the final text in chat too. Leave the tabs open, since he needs to act on them (the one case where tabs stay open on purpose).

Never prompt him to go post, confirm he's posted, or treat the run as done once the text is typed. The posting decision and action are entirely his.