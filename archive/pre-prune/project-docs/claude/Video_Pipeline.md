# Coach Gen Video Pipeline (v1, 31 Oct 2026)

One script renders a finished video from a cut file and a small spec. No Concat in the loop, so no timeline JSON in the chat. Code: `claude/cg_video_build.py` (copy it to the machine that renders as `build.py`).

## What it does in one pass
- Captions: Montserrat ExtraBold caps, white, black outline, centre line at y 1152 (60%), max width 86%, phrase chunks you write by hand in the spec.
- Highlight: wrap a word in `*stars*` and it turns Aqua (blue family) or Gold (gold family). Only where a word carries the meaning, not on every chunk (Gen, 31 Oct 2026).
- Caption entrance: "pop", 85% to 100% in 0.1 s. Set `cap_fx` to `none` to turn it off. Gen asked for it (31 Oct 2026). No study backs a gain in attention, it is a common creator preset. Kept short so reading is not delayed.
- Heading (Reels): style D, picked by Gen 31 Oct 2026. Big Montserrat Black white text with black outline, payoff word in the accent colour, short accent rule under it, small pop in, 0 to 8 s.
- Name tag: "Genison Wibawa" plus title line from 01_CORE section 2, plate panel at 85%, 4 px accent rule on the left, square corners. Top left at y 300 (clean wall, clear of the face and the captions). Reels: 8.5 to 12.5 s, after the heading. Full talk: 3.5 to 7.5 s.
- Corner mark: white watermark PNG, 72 px, top left corner at x 944, y 281.
- Title card (full talks, optional): 3 s plate, family mark 160 px, accent eyebrow caps, title Montserrat Bold. Video shifts by +3 s.
- Audio: loudnorm to -14 LUFS, AAC 192k, 48 kHz.
- Quality line printed before render: chunk count, share over 20 characters per second, share ending on a small word (sentence ends with . ? ! do not count), max words, highlight count.

## Colour family rule (Gen, 31 Oct 2026)
Pick the family from what Gen wears in the first frame. Cool clothes (white, blue, grey, black): blue family, Aqua accent, Abyss plates. Warm clothes (beige, brown, cream, gold, earth): gold family, Gold accent, Charcoal plates. Check the accent also stands out from the background. One family per video, title card included. This overrides the older "gold for stage pieces" default.

## How to run
```
python3 build.py SPEC.json          # check line, render segments, finish (concat + loudnorm)
python3 build.py SPEC.json check    # quality line only
python3 build.py SPEC.json sheet 1.0 9 34.5   # frame sheet at chosen times
```
Env: `CG_FONTS` (folder with the static Montserrat files), `CG_BUDGET` (seconds per call, default 120 for the Mac shell limit; use a large value in the cloud). It renders 30 s segments and skips finished ones, so on the Mac shell just call it again until it prints DONE.

Speed: on the Mac shell (4 cores) a 45 s Reel takes 16 to 37 s. Concat exports took minutes.

## Spec format (JSON)
```
{ "name": "R1 Gas and Brake", "family": "blue",
  "src": ".../_media/R1 cut.mp4", "out": ".../1 Final/R1 Gas and Brake.mp4", "work": "~/cgr/R1",
  "mark": ".../coachgen_watermark-mark_white_60pct.png",
  "heading": {"lines": ["WHY ARE YOU NOT", "MOVING *FORWARD?*"], "start": 0, "end": 8},
  "lower_third": {"start": 8.5, "dur": 4, "name": "Genison Wibawa", "line": "International Coach & Author", "w": 540},
  "title_card": {"eyebrow": "LASTING CHANGE", "title": "Icebreaker speech", "mark_png": ".../coachgen_mark_blue_on-dark_2x.png"},
  "cap_fx": "pop",
  "captions": [[0.0, 1.31, "IMAGINE YOU GET INTO A *CAR*."], ...] }
```
Caption times are final output times (for a full talk with a title card they already include the +3 s).

## Fonts
Libass needs static font files. Make them once from `Brand/Fonts/Montserrat.ttf` (variable) with fontTools `instancer` at weights 400, 600, 700, 800, 900, and set the family names to "Montserrat" (Regular, Bold), "Montserrat SemiBold", "Montserrat ExtraBold", "Montserrat Black". GitHub font downloads work from the Mac shell but are blocked in the cloud workspace.

## Size calibration (libass versus CSS px)
Libass font size is about 1.5 times the CSS px size for Montserrat. Caption 80 matches the old Concat caption (fontSize 0.028). Name 60 is about 40 px CSS, title line 42 is about 28 px CSS.

## Known limits
- The Mac shell disk is small. Full-talk segments filled it on 31 Oct 2026 and the shell stopped (EIO on every command) until the desktop app restarts. Delete each work folder after its final is copied, and render long videos in the cloud workspace.
- device_commit_files takes 30 MB per file at most, so a full-talk final made in the cloud must be split into parts and joined on the Mac with `cat`, or rendered on the Mac.
- device_commit_files can keep an old copy when the same file name is committed again. Use a new file name for each push.

## Voice (added 1 Nov 2026)
Spec key `voice`: `none`, `radio` (high-pass, low-shelf warmth +4 dB at 120 Hz, -2 dB at 300 Hz, +2 dB at 3.5 kHz, de-esser, gentle compression) or `radio_deep` (the same plus a 1 semitone drop with formants kept, rubberband). Blind test on R3, loudness matched: Gen picked `radio_deep` over the original and `radio`. First used on the Icebreaker Full Talk. The Reels are still the original voice until he confirms.

## Caption effects and cover (added 1 Nov 2026)
- `cap_fx`: `pop` (85 to 100 percent in 0.1 s, default), `bounce` (70 to 105 to 100 percent in 0.15 s, fade out 0.06 s), `slide` (rise 15 px and fade in 0.1 s, fade out 0.06 s), `bounce_hl` (bounce, highlight word stays 110 percent), `none`. Blind test X, Y, Z sent to Gen 1 Nov 2026 in `Desktop/ClaudeConcat/Caption FX Test` (key in that folder). Set the winner as default.
- `build.py SPEC cover`: grid cover still (heading plus mark on a clean frame, no caption, no name tag) saved as `<name> cover.jpg` beside the final. `cover_t` picks the frame (default 1.0 s).
- No end card on Sinek-style Reels (Gen, 1 Nov 2026). The provoking question is the heading in frame 1 and goes in the post caption or comment.

## Transcription and caption review (planned 1 Nov 2026, build on the next raw video)
Problem: "national marathon" became "actual marathon". Whisper medium misheard, then correcting "by context" made it read well instead of making it right. Both versions are valid in context, so text alone cannot decide. Timing was fine.
1. Inputs: raw video, plus optional keywords and optional script, outline or notes (skill arguments).
2. Transcribe twice: faster-whisper large-v3 with word timestamps and word probabilities, primed with the keywords and script as the initial prompt, plus a second model (a different family or size) on the same audio.
3. Flag: words where the two models disagree, and words under about 0.5 probability in either.
4. Captions verbatim by default. Clean-up may only remove fillers, restarts and repeats and fix small grammar. Never swap one real word for another without a flag decision.
5. Caption review page (artifact) before render: flagged spots first, each with timestamp, a 3 s audio clip (inline mp3), model A text, model B text and a pick button, then the full caption list with highlight words coloured, speed warnings, and every change from the transcript marked. A "Copy my picks" button gives a short line Gen pastes back. Expect 5 to 15 flags on a 5 minute talk.
6. Render only after the picks.

## Background music (planned 1 Nov 2026)
Spec keys `music` (track file) and `music_db` (level, start about -22 dB under the voice). Sidechain ducking under speech, 1 s fade in, 2 s fade out, loop if short. Mood: calm cinematic piano or pads. Tracks must carry commercial rights (Suno paid plan or a licensed library). Gen's workspace cannot download from music sites, so Gen supplies tracks into a Brand Music folder. Level set by a blind test on a phone speaker.

## Corrections (1 Nov 2026, later)
- Caption effect: Gen saw the X, Y, Z test and wants it very subtle ("feels excessive"). New default `cap_fx: subtle` = fade in 0.08 s, fade out 0.04 s, no scale or movement.
- One line only, like Sinek. WrapStyle 2 (no wrap). Chunks over 24 characters shrink to fit (down to 80 percent) and the check line counts them. Write chunks to 24 characters or fewer so the count stays 0.
- Review placement: one stop BEFORE cutting, not before render. Transcription and flags come first, and every decision (flagged words, proposed cuts, Reel picks, heading questions) goes on one review page. After his picks, cutting, captions and render run without stopping.
