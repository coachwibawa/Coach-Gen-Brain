# Icebreaker Build Log (addendum to Icebreaker_Video_Edit_Plan.md)

Built 27 Oct 2026. Source: `Downloads/20261024_101740.mp4`. All versions 1080 x 1920, 30 fps.

## Delivered on the Mac Desktop
- `Icebreaker R1 Gas and Brake.mp4` (47.0 s)
- `Icebreaker R2 Why Cant We Finish.mp4` (38.9 s)
- `Icebreaker R3 The Marathon.mp4` (42.2 s)
- `Icebreaker Full Talk.mp4` (5 min 37 s: 3 s title card, then the speech)
- Concat project for the full talk: `Desktop/Icebreaker Full Talk` (closed, editable)

## Decisions
- Social Reels: um/uh fillers and long pauses removed (Gen's request). Full talk keeps natural pauses over 0.5 s trimmed to a short beat, fillers removed.
- Melina's trauma line stays in the full talk only.
- The named member's speech reference (about 436 to 438 s) is cut in every version.
- R2: a hidden restart ("we can figure out, we can we all can solve") was cut at the first "we can".
- Corner mark is a text mark "COACH GEN". The brand kit folder was not reachable. Swap when Gen points to the logo file.
- Shots: wide as filmed, close = scale 1.4, offsetX -0.2. Captions Bebas Neue 0.034, white with black stroke.

## Method notes
- Cuts: one raw clip, split in descending time order, then ripple remove. Concat edit_apply batch does not work from this link.
- Whisper hides fillers and restarts, so cut points came from audio-energy pause detection plus hand-verified filler times. Always verify an export with a transcript and a frame sheet.
- Loudness: Concat export is about -26 LUFS. Mac ffmpeg `loudnorm=I=-14:TP=-1.5:LRA=11`, video copied. Results: R1 -14.6, R2 and R3 about -15.3, full talk -15.1 LUFS.

## Caption wording to check (Whisper)
- "a national marathon" (maybe "an actual marathon")
- "You are in the finish line"
- "He's breath" / "almost done breath"
- "I was from Singapore" (maybe "in Singapore")
- "her own solution" and "my icebreaker" were corrected by hand from "her son's" and "ex-breaker"
- Gen says "Imagine you get into a car" twice and "on your right foot" twice in the full talk. Left in as spoken.

## Cleanup
- Safe to delete: `Desktop/Icebreaker R1 Gas and Brake raw.mp4` (stale, doubled opening) and `Downloads/_claude_work/`.
- Folders moved on 27 Oct to `Desktop/ClaudeConcat/Icebreaker Speech/{1 Final, 2 Concat projects, 3 Work files (safe to delete)}`.

## Rules updated by Gen, 27 Oct (18:39 Jakarta), supersede the Decisions above
- Consent: assume everything Gen puts in his own video has consent. Do not cut a line because it names or involves another person.
- Melina's line is now allowed in a Reel. It is a very powerful story. Include it.
- One moment may appear in more than one Reel. Do not avoid overlap between Reels.
- Cut repeated phrases, whether said on purpose or as a stumble. Use judgment. This applies to the full talk too ("Imagine you get into a car", "on your right foot").

## Rebuild under the new rules, 27 Oct (applied)
Finals are in `Desktop/ClaudeConcat/Icebreaker Speech/1 Final`:
- `R1 Gas and Brake.mp4` (46.4 s), question box "WHY ARE YOU NOT MOVING FORWARD?"
- `R2 Why Cant We Finish.mp4` (38.7 s), box "WHY CAN'T WE FINISH WHAT WE START?"
- `R3 The Marathon.mp4` (42.2 s), box "WHY DO WE STOP AT THE FINISH LINE?"
- `R4 Melina.mp4` (51.9 s, new), box "WHAT WAS REALLY HOLDING HER BACK?"
- `Icebreaker Full Talk.mp4` (5 min 30 s: 3 s title card, then the speech, repeats cut, named-member reference restored)
Concat projects (captions, titles and mark editable) are in `2 Concat projects`, sharing `_media/`. Do not delete `_media`. Camera shots are burned into the `_media` cuts.
Repeats cut (source seconds): 89.53-91.77, 229.11-230.21, 238.51-238.73, 283.57-286.07, 296.79-297.97, 363.91-364.89, 375.03-375.43, 433.83-434.5.
Reel method now: ffmpeg cut from the 4K source on the Mac (cut list, 12 ms audio fades), then captions and titles in Concat, then loudnorm.
Caption words for Gen to check: "SWILLING'S SPEECH" (member name spelling), "I WAS FROM SINGAPORE", "A NATIONAL MARATHON", "ALMOST DONE BREATH", "WAS NOT TEACH HER", "TASKED/ASKED", "LIFT OUR FOOT OFF THE BRAKE" (audio unclear).
Logo is still the text mark "COACH GEN". Old projects and finals sit in `3 Work files (safe to delete)`.

## Caption correction pass, 27 Oct (applied to all five finals)
Rule from Gen: fix caption wording and grammar by contextual assumption. A mismatch with the spoken words is fine.
- Fixed in the Full Talk (28 clips) and the Reels, for example: "YOU ARE AT THE FINISH LINE", "I WAS IN SINGAPORE", "I DID NOT TEACH HER", "A CERTIFIED PUBLIC SPEAKING TRAINER", "CHANGE THAT LASTS", "HARDER INSTEAD OF CHECKING IF THE ENGINE IS WORKING".
- The named member's name in a caption was replaced by the generic "JUST LIKE THE EARLIER SPEECH".
- Still uncertain: "SAME TASKED/ASKED", "LIFT OUR FOOT OFF THE BRAKE" (kept).
- Method: direct edits to `concat.json` are ignored by the app. Use in-app `clip_update` with `path`, `clipId` (not `clip`) and the full caption style in the patch (font, size, weight, color, stroke, align, maxWidth), or the style resets. Then project_save, export_start, project_close, and loudnorm.
- All five finals re-exported and re-normalized to -14 LUFS.
