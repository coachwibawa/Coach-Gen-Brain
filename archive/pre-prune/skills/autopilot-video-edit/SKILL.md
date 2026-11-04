---
name: "autopilot-video-edit"
description: "Turn Coach Gen's raw talking-head video into a full cut plus Sinek-style Reels with captions, via the build.py pipeline. Use when he gives a raw speech or talk video to edit."
---

# Autopilot video edit (Coach Gen)

He gives a raw video. You build finished cuts. He can still finish by feel in Concat or CapCut.

## Arguments (all optional)
- `keywords:` words he says that a model could mishear (names, places, his terms), for example `Melina, Toastmasters, Lasting Change, 6C`. Always add the standing list: Coach Gen, Genison Wibawa, Lasting Change, 5 Laws, Marathon, Toastmasters, HR, Singapore, Jakarta.
- `script:` the speech script, outline or notes, pasted or as a file path. Used to prime transcription and to settle flagged words. Captions still follow what he SAID, not the script.
- `deliverables:` full, reels or both. If missing, put it on the review page.

## Read first
Project docs `claude/Video_Pipeline.md` (the render pipeline and its code `claude/cg_video_build.py`), `brand/00_START-HERE.md`, `brand/01_CORE.md`, `brand/10_VIDEO.md` (v1.2 has Gen's 31 Oct and 1 Nov picks), `claude/Reel_Style_Guide.md` (structure and pacing only), `claude/Toastmasters_Speech_Handoff.md` (NEVER USE rules), `claude/Caption_Chunking_Research.md`, and the project's own edit plan. Brand docs win over older style notes. Where Video_Pipeline.md has a newer dated correction, it wins.

## Model and effort (Gen, 31 Oct 2026)
Farsight is cheaper than trial and error. Plan a new kind of build on Opus at high or xhigh. Running this workflow on a new video from an approved plan is Sonnet or Opus at medium.

## Content rules (set by Gen, 27 Oct 2026)
- Assume everything in his own video has consent. Never cut a line because it names or involves another person, or because it is a sensitive personal story. Powerful stories go in.
- One moment may appear in more than one Reel. Do not avoid overlap between Reels.
- Cut repeated phrases, whether said on purpose or as a stumble. Use judgment. Keep the last take. Applies to Reels and the full talk.
- Reels: remove um/uh fillers and long pauses. Full talk: keep natural pauses, trim dead air over about 0.5 s.
- Replace a named member's name with a generic phrase.

## Caption wording: verbatim by default (Gen, 1 Nov 2026; replaces the 27 Oct "assume context" rule)
- Clean-up may only REMOVE fillers, restarts and repeats, and fix small grammar (an article, a verb tense, a plural).
- Never swap one real word for another (noun, name, number, adjective, verb) unless the review step settled it. Reason: "national marathon" became "actual marathon". Both read fine in context, so context cannot decide. Only the audio can.
- His natural style (pauses, fillers, restarts, unrehearsed) is fine for the audience. The system absorbs it. Do not lecture him about it.

## Workflow (one stop for him, before cutting; everything after runs without stopping)
1. **Probe.** ffprobe the file.
2. **Transcribe twice.** faster-whisper large-v3 with word timestamps and word probabilities, force English, initial prompt = keywords plus the first part of the script. Then a second model (different size or family) on the same audio. Decode audio with ffmpeg to 16 kHz mono. Whisper hides fillers, stretches word times over pauses and hallucinates over silence.
3. **Flag.** Words where the two models disagree, and words under about 0.5 probability in either. Where the script settles a flag clearly, note it but still show it.
4. **Plan.** Find cut points with audio-energy pause detection (smoothed level under -36 dB for 0.30 s or more) plus filler and restart times. Last-take rule: when a sentence is said more than once, the last take is correct, including a restart inside a take. Propose the Reels (time ranges and the heading question for each) and the colour family (from what he wears in the first frame).
5. **Review page (artifact), then STOP once for his picks.** This is the ONLY stop, placed before cutting, so every decision is batched and nothing after it waits on him. Build one HTML artifact titled "Video review: <video>":
   - Top: flagged words only, each a card with timestamp, a 3 s inline audio clip (mp3, base64), model A text, model B text, pick buttons (A, B, or type his own).
   - Then: the proposed cuts (what repeats and restarts go, as short text lines with timestamps), the proposed Reels with their heading questions, deliverables if not given, and the colour family.
   - Then: the full caption draft in a scrollable table: time, caption as it will look (caps, one line, highlight word in the accent colour), a speed badge over 20 characters per second, a length badge over 24 characters, and a marker on every line that differs from the transcript (transcript on hover).
   - Summary line: flags, cuts, Reels, chunk stats.
   - A "Copy my picks" button that gives one short line (for example `3:A 7:B 9:national R2:ok`) to paste back. Also accept picks typed in chat. Silence on an item means accept the proposal.
   - Plain and fast to scan. If there are no flags and nothing uncertain, skip the stop and say so.
6. **Execute without stopping.** Apply his picks. Cut and join with ffmpeg into `<name> cut.mp4` in `2 Concat projects/_media/` (close shot scale 1.4, offsetX -0.2; wide default; alternate at sentence breaks every 5 to 20 s). Write the spec with captions from the real word times mapped through the cut list (output time = running total of kept pieces minus source start), `*word*` for highlights. `build.py SPEC check`, `build.py SPEC` (resumes by segment; call again until DONE), `build.py SPEC cover` for each Reel, `build.py SPEC sheet <times>` and look once.
7. **Deliver.** Stage the finals and covers and send them. Log to project docs (add only, no em dashes).

First run note: steps 2 to 5 are planned but not yet scripted. On the next raw video, write them as scripts beside build.py (transcribe, flags, cut plan, review page builder), test them on that video, and save them to the project.

## Caption rules
- Cut by PHRASE, never by a fixed word count. Usually 2 to 5 words, range 1 to 6. Break at a clause boundary or punctuation.
- ONE LINE ONLY, like Sinek (Gen, 1 Nov 2026). Keep each chunk to 24 characters or fewer. build.py never wraps and shrinks a longer chunk to fit (down to 80 percent), and the check line counts them. Aim for 0.
- Never end a chunk on a small word (a, an, the, to, of, and, or, but, is, in, on, at, for, with, your, my, our, I, it, that) unless it ends a sentence.
- Speed ceiling about 20 characters per second. At least 0.33 s per word, never under 0.5 s.
- No word-by-word flashing, no moving highlight.
- Highlight one word (or one meaning unit such as FINISH LINE) only where it carries the meaning, not on every chunk (Gen, 31 Oct 2026).
- Effect: very subtle (Gen, 1 Nov 2026, after a blind test where bounce, slide and bigger-highlight felt excessive). Default `cap_fx: subtle` = fade in 0.08 s, fade out 0.04 s, no scale or movement.

## Look (brand/10_VIDEO.md v1.2)
- 1080x1920, 30 fps.
- Colour family by what Gen wears in the first frame: cool clothes (white, blue, grey, black) blue family, Aqua #72CCD0 accent, Abyss #01131C plates. Warm clothes (beige, brown, cream, gold, earth) gold family, Gold #C8B796 accent, Charcoal #2B2B2B plates. One family per video, title card included. Check the accent stands out from the background.
- Captions: Montserrat ExtraBold caps, white, black outline, centre line y 1152.
- Heading on Reels: style D. Big Montserrat Black white text with black outline, payoff word in the accent, short accent rule, small pop in, 0 to 8 s. It is the provoking question. No end card on Sinek-style Reels: the question sits in frame 1 and goes in the post caption or comment.
- Name tag: "Genison Wibawa" plus the title line from 01_CORE section 2 (default International Coach & Author), top left at y 300, 4 s. Reels 8.5 s (after the heading), full talks 3.5 s.
- Corner mark: white PNG `5 Laws of Lasting Change/Brand/CoachGen-Logo-Kit/04_Video-watermark/coachgen_watermark-mark_white_60pct.png`, 72 px, top right (x 944, y 281), full length.
- Full talk title card (3 s, video shifts +3 s): family plate, family mark 160 px (`01_Logo/Mark-only/PNG/coachgen_mark_blue_on-dark_2x.png` or `coachgen_mark_gold_on-dark_2x.png`), accent eyebrow "LASTING CHANGE", title in Mist #EAF5F6 or Ivory #F6F2EA.
- Grid cover for each Reel: `build.py SPEC cover`.
- Keep all text and the mark between y 270 and y 1250.
- Thought-style Reels use Libre Baskerville 400 captions instead (not yet in the pipeline).

## Audio
- Loudness -14 LUFS (done by build.py).
- Voice: `voice: radio_deep` (radio polish plus 1 semitone lower, formants kept). Gen picked it in a blind test (1 Nov 2026).
- Music (planned): `music` track plus `music_db` about -22 dB under the voice, ducked under speech, 1 s fade in, 2 s fade out. Calm cinematic piano or pads. Tracks must carry commercial rights. Gen may generate them on his own GPU with an open model that allows commercial use (for example ACE-Step, Apache 2.0) or a paid Suno plan, and puts the files in a Brand Music folder. Set the level by a blind test on a phone speaker.

## Blind tests (how Gen decides looks and sounds)
Make 2 or 3 versions that differ in one thing only, match loudness within 0.2 LU, label them randomly (A, B, C or X, Y, Z), put them in a new folder under `Desktop/ClaudeConcat/` with `answer key (open after you pick).txt`, send them, and never reveal the key until he picks.

## Concat (only when he wants to hand-finish)
- Concat 0.2.8 MCP tools (deferred, load with ToolSearch). Project path = the project folder under `2 Concat projects/`. Edits stay in memory until project_save. project_close when done (an open project blocks the GUI).
- Every call returns the whole timeline JSON (token heavy). edit_apply does not work from this link. Concat cannot colour one word inside a caption.
- Cut method: one raw clip c2 at start 0, split in DESCENDING time order, then clips_remove with ripple true.
- `clip_update` takes `clipId` and `patch` (a text patch must carry the full style). `clip_transform` takes `offsetX`, `offsetY`, `scale` directly.
- `export_start` takes `path`, `output` and `crf` 18. Poll `export_status`. Then project_close, sleep 3, then loudnorm with ffmpeg.
- Bulk edits: with the project CLOSED, edit `concat.json` directly (both `timelines[0].clips` and the top-level `clips`). Back up first.

## Machines and files
- Mac shell is device_bash (ffmpeg with libass and rubberband, 4 cores, folders under $HOME/mnt/). Each call stops at about 175 s and background jobs die between calls. The pipeline resumes segment by segment.
- The Mac shell disk is small (about 10 GB). Delete each work folder in $HOME/cgr after its final is copied. On 31 Oct 2026 a full disk broke the shell (EIO on every command) until the desktop app restarted. A segment written while the disk filled was corrupt and truncated the next final: after any disk error, delete all segments and re-render.
- device_commit_files: 30 MB per file and 100 MB per call, and a repeated file name can keep the old copy, so use a new name each push. device_stage_files only from connected folders (Desktop, Downloads, Documents/5 Laws of Lasting Change).
- Fonts: libass needs static Montserrat files in ~/cgfonts on the Mac (from github.com/JulietaUla/Montserrat). In the cloud make them from `Brand/Fonts/Montserrat.ttf` with fontTools (see Video_Pipeline.md).
- All video work lives under `Desktop/ClaudeConcat/<Video name>/` with `1 Final/`, `2 Concat projects/` (cut files in `_media/`), `3 Work files (safe to delete)/`. Never loose on the Desktop.
- Send him a clickable preview after big edits.

## Finishing
Report: what was built and where, which flags he settled, what repeats were cut, and that he should preview. Add a build log to project docs (add only, no em dashes).