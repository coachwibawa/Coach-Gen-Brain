# Icebreaker Brand Restyle Log (addendum to Icebreaker_Build_Log.md, which stays as written)

## Brand restyle, 30 Oct 2026 (applied to all five finals)
Restyled to the new brand docs (`brand/00_START-HERE`, `01_CORE`, `10_VIDEO`). Cuts and corrected caption wording unchanged. Finals in `1 Final` are re-exported and loudnormed to -14 LUFS.
- Captions: Montserrat 800, caps, white, black stroke, no shadow, centre line at about 60% of the height.
- Question box (Reels): Montserrat 800 caps, Abyss text on Aqua plate, square corners, top of the safe zone, 8 s.
- Mark: white watermark PNG from the logo kit (72 px wide, top right, inside the safe zone) replaces the text mark "COACH GEN" on all five. The Full Talk shows it from 3 s.
- Full Talk title card: Charcoal plate, gold mark (160 px), gold eyebrow "LASTING CHANGE", Ivory Montserrat title "Icebreaker speech". Gold family chosen because it is a stage piece. A black strip at the top of the card was fixed with a plate text clip (c245) with large background padding.
- Bebas Neue is retired from all five.

## Method correction (supersedes "direct edits to concat.json are ignored")
With the project CLOSED, direct edits to `concat.json` work. Edit `timelines[0].clips` (the app reads this) and the top-level `clips` too. Then `project_open`. Backups of the pre-restyle files: `concat.json.bak_oct30` in each project folder. `clip_transform` takes `offsetX`, `offsetY`, `scale` directly (no `patch`). `export_start` needs `output`.

## Still open
- One highlight word per caption chunk (Aqua on Reels, Gold on the Full Talk) is not done.
- Lower third "Genison Wibawa" on first appearance (4 s) and the end card are not done.
- The mark PNG is linked from the Documents logo kit path. If that folder moves, relink or copy the PNG into `_media`.

## 30 Oct 2026: phrase re-chunk applied to all five videos

- Captions in all five Concat projects were rewritten by phrase using a dynamic-programming script (rechunk.py on the Mac, in $HOME/refocr). Word times were interpolated inside the old chunks.
- Chunks now: R1 38, R2 32, R3 32, R4 43, Full Talk 246. Mean about 3.5 words, median about 3 words per second.
- About 6 to 16 percent of chunks still run over 20 characters per second. Ending on a small word: 0 to 4 percent.
- Known imperfect breaks: R1 "WHEN REALLY,", "KNOW IS THERE IT'S PREVENTING"; R2 "FINISHING IT WHY IS IT", "HARDER IT'S NOT ABOUT MAKING"; R3 "YOU ARE AT THE FINISH / LINE YOU ARE A SUPPORTER". Some 35-character chunks wrap to two lines. Breaks are heuristic, not true syntax, and can be hand-tuned in Concat.
- Backups: concat.json.bak_chunk (before re-chunk) and concat.json.bak_oct30 (before brand restyle).
- All five re-exported at CRF 18 and loudnormed to -14 LUFS into 1 Final.
- Brand guide rule in brand/10_VIDEO.md ("2 to 4 words per chunk") not changed. Needs Gen's approval.
- Still open: highlight word per chunk, lower third, end card.

## 31 Oct 2026: pipeline rebuild (highlights, heading D, name tag, pop, blue family)

- All five videos re-rendered with the new pipeline (`claude/Video_Pipeline.md`, code `claude/cg_video_build.py`), not Concat. The Concat projects are unchanged and no longer match the finals.
- Captions hand-edited by phrase. Bad breaks fixed (for example "FEET ON YOUR RIGHT FOOT", "FINISHING IT WHY IS IT", "YOU ARE AT THE FINISH / LINE"). Small wording fixes by context: "I DIDN'T SAY, HEY, YOU NEED TO DO THIS" (Whisper had "SHE"), "TO START A NEW CAREER", "FOR SIX YEARS", "WHAT THEY START?".
- Chunks: R1 39, R2 33, R3 34, R4 45, Full Talk 244. 6 to 15 percent over 20 characters per second, 0 to 4 percent end on a small word (sentence ends excluded).
- Highlight words in Aqua only where a word carries the meaning (R1 18, R2 18, R3 16, R4 16, Full Talk 93).
- Heading: style D (Gen picked D over A, B, C on 31 Oct 2026). R1 "MOVING FORWARD?", R2 "FINISH", R3 "FINISH LINE?", R4 "BACK?" in Aqua.
- Name tag "Genison Wibawa / International Coach & Author", top left at y 300: Reels 8.5 to 12.5 s, Full Talk 3.5 to 7.5 s.
- Caption pop entrance, 0.1 s.
- Colour family: blue on all five, because Gen wears a white shirt and navy trousers in the first frame (Gen's rule, 31 Oct 2026). The Full Talk title card moved from gold to blue (Abyss plate, blue mark, Aqua eyebrow, Mist title).
- R1 to R4 finals are in `1 Final`. The Full Talk was rendered in the cloud workspace and sent in chat. The Mac copy in `1 Final` is still the 30 Oct Concat version until the Mac shell works again (it broke with EIO after its disk filled with render segments).
- Still open: end card (needs Gen's call to action pick). Brand guide `brand/10_VIDEO.md` not yet updated for heading D, name tag position, colour-by-outfit rule and "highlight only where needed".
