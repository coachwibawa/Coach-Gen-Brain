# 10 Video (Reels, talks, captions)

Version 1.3, 3 Nov 2026 (1.2 plus section 10 for live video, nothing removed). Load with 01_CORE.md. Structure and pacing come from `claude/Reel_Style_Guide.md`. This file overrides its fonts, colors and caption position.

## 1. Pick the style
| Post type | Style | Font | Family |
|---|---|---|---|
| A thought, belief, reframe (Myth vs Reality, Identity Shifts) | Thought (Dan Koe) | Libre Baskerville | Blue. Gold when about the book |
| Behind the scenes, events, announcements, Gen as a person | Persona (Hiro) | Montserrat 800 | Blue |
| Teaching a Law, client stories, talk and podcast clips | Professional (Sinek) | Montserrat 800 | Blue. Gold for stage and speaking clips |

- CORRECTION (31 Oct 2026): the family follows what Gen wears in the first frame, not the post type. Cool clothes (white, blue, grey, black): Blue. Warm clothes (beige, brown, cream, gold, earth): Gold. Also check the accent stands out from the background. One family per video, title card included. Gen: "you can vary the color to the brand color; the decision tree is based on what I'm wearing on the first frame."

Caption language follows the spoken language (Reel Style Guide decision, 21 Oct 2026).

## 2. Captions (all styles except the Thought hook card)
- Montserrat 800, caps, white, letter spacing +0.01 em, black stroke, no shadow. **Locked.**
- 2 to 4 words per chunk, max 2 lines, centred, max width 86%. **Locked.**
  - CORRECTION (30 to 31 Oct 2026): chunk by phrase, usually 2 to 5 words (range 1 to 6), never end on a small word unless the sentence ends, about 20 characters per second at most. Evidence in `claude/Caption_Chunking_Research.md`. Gen approved the rule ("I like that rule").
- Centre line at 60% of the height (y about 1150 at 1080 x 1920). This keeps one file usable as an organic Reel and as an ad. Replaces the older 60 to 75% band. **Locked.**
- One highlight word per chunk on the word that carries the meaning: Aqua #72CCD0 (blue pieces), Gold #C8B796 (gold pieces). **Locked.**
  - ADDED (30 Oct 2026): no A/B test. Gen: "I think the blue is fine; maybe can keep the other for options or for different series in the future". The old colors sit on the reserved series list in 01_CORE.
  - CORRECTION (31 Oct 2026): highlight only where a word carries the meaning, not on every chunk (Gen: "the highlighting of one word when necessary"). A meaning unit of two words (FINISH LINE, GIVES UP) counts as one.
  - ADDED (31 Oct 2026): captions enter with a short effect, under 0.15 s so reading is not delayed. Default pop (85% to 100% in 0.1 s). A blind test of bounce, slide and bounce-with-bigger-highlight is out with Gen (1 Nov 2026); the winner replaces the default.
  - ADDED (1 Nov 2026): caption wording is verbatim by default. Clean-up may remove fillers, restarts and repeats and fix small grammar, but never swaps one real word for another. Uncertain words (two transcription models disagree, or low confidence) go to Gen on a short review list before render. Reason: "national marathon" became "actual marathon" when context was used to correct.
- Thought style captions: Libre Baskerville 400, smaller, white or Gold, same position.
- Split screen (two speakers): speaker 1 Aqua, speaker 2 White, caption on the middle line.
- Concat starting values, **check once** then lock: fontSize 0.028, fontWeight 800, offsetY 0.10, maxWidth 0.86, strokeWidth 0.004, shadow false.
- Retired values: #FFD400 yellow, #FF6A13 orange, #3FA9F5 blue, #D4A64A old gold, Bebas Neue, Anton, Baskerville (system). Libre Baskerville replaces Baskerville.

## 3. Hook card (Thought style)
Abyss background (Charcoal for gold pieces), Libre Baskerville 400 white, left-aligned or one centred line, max width 75%, inside the safe zone. 5 to 6 s.

## 4. Question box (optional)
Montserrat 800 caps, Abyss text on an Aqua panel (Charcoal on Gold for gold pieces), square corners, top of the safe zone (y about 300), up to 8 s.
- CORRECTION (31 Oct 2026): on Reels the question uses heading style D instead of the panel, picked by Gen in a mock test of four looks ("actually, I prefer D"). Montserrat Black about 64 px CSS, white with black outline, the payoff word in the accent colour, a 300 x 10 px accent rule under it, small pop in, 0 to 8 s, centred at y 440 to 560. The panel stays available as an option.
- ADDED (1 Nov 2026): this question is also the end card. Sinek-style Reels have no end card: the provoking question sits in frame 1 and in the post caption or comment (Gen, 1 Nov 2026).
- ADDED (1 Nov 2026): grid cover. A still of the heading plus the corner mark on a clean frame (no caption, no name tag), saved as `<name> cover.jpg` next to the final.

## 5. Logo on video
Mark only, white PNG from `CoachGen-Logo-Kit/04_Video-watermark`, 72 px wide at 1080 x 1920, 70% opacity, top right at x 944, y 280, full length. Replaces the text "COACH GEN" mark. **Locked.**
- ADDED (30 Oct 2026): mark only in 9:16, because platforms already show @coachgenofficial under every Reel and the name version is 3.5 times wider. Landscape video (YouTube, LinkedIn, full talks) may use the horizontal logo with the name in the corner. The name appears in the lower third and the end card.

## 6. Cards
- Title card (full talks, 3 s): Abyss background, mark 160 px, title Montserrat 700 64 px in Mist, eyebrow in Aqua caps.
- Lower third (first appearance, 4 s): "Genison Wibawa" Montserrat 700 40 px, title line from 01_CORE section 2 in Montserrat 400 28 px, Abyss panel at 85%, 4 px Aqua rule on the left, square corners.
  - CORRECTION (31 Oct 2026): place it top left at y 300 (x 64, about 540 x 150 px), not low. Low it covered the chin in close shots and fought the captions. On Reels it shows at 8.5 to 12.5 s, after the heading. On full talks at 3.5 s, after the title card.
- End card (3 s, optional): stacked logo, one call to action, one handle or URL. Thought style has no end card.
  - CORRECTION (1 Nov 2026): Professional (Sinek) style has no end card either. See section 4.

## 7. Persona style extras
Stickers, cut-ins and B-roll keep their energy, but stickers and frames use palette colors only. No pink frames, no emoji walls. Branded shirt with the Coach Gen mark when possible.

## 8. Fixed technical values
1080 x 1920 (16:9 1920 x 1080 for full talks), 30 fps, loudness about -14 LUFS (the autopilot-video-edit skill has the ffmpeg line). Length 25 to 75 s for Reels.
- ADDED (31 Oct 2026): everything above is rendered by the pipeline in `claude/Video_Pipeline.md` (code `claude/cg_video_build.py`), not Concat.
- ADDED (1 Nov 2026): voice. Radio polish (warmth, de-ess, gentle compression) plus 1 semitone lower with formants kept (`voice: radio_deep`). Gen picked it in a blind test against the original and the polish alone ("B sounds better"). First applied to the Icebreaker Full Talk.
- PLANNED (1 Nov 2026): background music, very low (about 20 to 25 dB under the voice, ducked while he speaks), cinematic and calm. Level to be set by a blind test. Tracks must carry commercial rights.

## 9. Checklist before delivery
1. One family, no gold with Aqua.
2. Only Montserrat or Libre Baskerville on screen.
3. Captions and logo inside y 270 to 1250.
4. One highlight word per chunk, palette color.
5. Mark top right at 70%.
6. Title line matches the audience, or none.
7. ADDED (31 Oct 2026): family matches the first-frame outfit rule.
8. ADDED (1 Nov 2026): no unconfirmed word swaps in captions (review list cleared).

## 10. Live video: Meet, Zoom and workshops (added 3 Nov 2026)
Gen's words: "I think it's professional enough without the bg. And if I want a bg I want to consider a transparent bg, aka the logo just floating." This background carries most first impressions, so it is one look, not a set.

### 10.1 Decisions
1. Keep the real room. No virtual background, no green screen, no AI background removal. A fanless MacBook Air should not run background removal for a whole call.
2. A floating Coach Gen G mark sits top right of the frame, 130 px wide at 1920 x 1080, 70 px from the right edge and 60 px from the top (x 1720, y 60). It is a transparent PNG layered over the camera.
3. Two mark colours, one per backdrop. Aqua #72CCD0 when the wall or curtain behind him is dark. White when the wall is light. Pick once per room, do not switch mid-call.
4. No glow, no neon, no gradient, no outline. The neon podcast look is for the podcast only.
5. Name tag (optional, for the first minute of workshops and talks): bottom right, panel 642 x 154 px, 70 px margins, Deep Water #0D4A59, square corners. Line 1 "Genison Wibawa" Montserrat 700 46 px in Mist. Line 2 "Coach Gen  |  International Coach & Author" Montserrat 500 26 px in Aqua. Change line 2 to the audience title line from 01_CORE section 2 when needed.
6. Text on the frame always sits on the solid panel. Never loose text over the room.
7. Real photos of Gen only. The room is his own.
8. The Zoom and Meet background templates from 17_TEMPLATES stay as a fallback if a client's platform blocks virtual cameras. They are not the default.

### 10.2 Scene set (OBS)
| Scene | Use |
|---|---|
| 0 Standby | Abyss background with the aqua mark centred. Before the call starts and during breaks |
| 1 Talk | Camera full frame, G mark. The default |
| 2 Present (slides + face) | Slides on the right 1320 px, camera on the left 600 px, G mark |
| 3 Slides full | Slides full frame, G mark |
| 4 Spotlight (image + face) | One image with the camera beside it |
Name tag source is hidden by default in scenes 1 and 2. Show it for the first minute, then hide it.

### 10.3 Mac setup notes
- App: OBS Studio 33.0.1, Apple Silicon. Installed by Gen on 3 Nov 2026.
- Scene collection: Scene Collection menu, Import, `Brand/Meet/OBS/Coach_Gen.json`. Pick the camera in the Camera source and the window in the Slides source. The import file was generated from Gen's PC collections and not tested by Setsu. Gen reports OBS is operational with what he needs.
- Virtual camera: Start Virtual Camera in OBS, then in Meet go to Settings, Video, Camera, and choose OBS Virtual Camera. Turn off Meet's own effects and backgrounds.
- First run needs the OBS camera extension approved. Tahoe: System Settings, Privacy & Security, Extensions, OBS "Media Extension". macOS 15: General, Login Items & Extensions, Camera Extensions.
- Permissions granted: Camera, Microphone. Not granted: Screen Recording (needed for scenes 2 and 3) and Input Monitoring (hotkeys while OBS is in the background). Grant them in System Settings, Privacy & Security when needed.
- Slides sent through the camera lose sharpness. For text-heavy slides use Meet's own Present button and keep OBS for the face.
- Dropped from the PC setup on purpose: green screen, AI background removal, gaming and VTube scenes, the Zoom pirate scene, old "Coach Wibawa" text, the Gotham font. Not copied: Toastmasters timer cards, QR code, podcast and Spotify logos, engagement-model image. Those files remain on the PC.

### 10.4 Files (Mac, under `5 Laws of Lasting Change/Brand/Meet/`)
- `coachgen_meet_overlay_aqua_1920x1080.png` and `coachgen_meet_overlay_white_1920x1080.png`: transparent, mark only.
- `coachgen_meet_nametag_1920x1080.png`: transparent, name tag only.
- `coachgen_mark_aqua_1024.png`: mark used by the Standby scene.
- `OBS/Coach_Gen.json`, `OBS/README_OBS_Mac.md`.
- `OBS/pc/Remarkable_Presenter.json`, `OBS/pc/Zoom_slide_background.json`, `OBS/pc/Untitled.json`: Gen's PC originals, archived untouched.
Do not move or rename the PNGs. The scene collection points at these paths.

### 10.5 Open
- Wall idea: a printed or painted Coach Gen mark on the wall strip beside the curtain. Waiting on the strip width in cm from Gen. If it happens, it follows the same rules: Aqua or Deep Water on a light wall, no neon.
- Checklist for a live call: right overlay colour for the backdrop, Meet effects off, OBS Virtual Camera chosen, name tag hidden after the first minute, no loose text on the frame.
