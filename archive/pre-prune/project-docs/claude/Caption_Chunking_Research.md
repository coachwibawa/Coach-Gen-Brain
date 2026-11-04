# Caption Chunking Research (30 Oct 2026)

Question: what is the ideal amount of words on screen at one time? Compared: published studies, Gen's 13 saved reference Reels, vendor guides for auto-caption tools, and our own five Icebreaker videos.

## Answer
No study gives one ideal word count. The studies give a speed ceiling and a way to break the text.
- Speed: keep each chunk at or under about 20 characters per second (about 3 words per second). At 28 characters per second viewers skip words and miss the end of the caption (Szarkowska et al. 2024, 12 / 20 / 28 cps eye-tracking test).
- Break: cut at a phrase boundary. Phrase-by-phrase chunks were the easiest on the eye; word-by-word needed the most gaze switching between picture and text (Rajendran et al. 2013, 24 viewers, no audio, uncorrected tests, so weak but consistent).
- Time-synced highlights helped learners but 49 test viewers found them too distracting for everyday viewing (Draxler et al. 2023).

## Our captions as built (measured from concat.json)
- 73% of Full Talk chunks are exactly 4 words (176 of 241). Mean 3.3 to 3.8 words.
- Median chunk 0.8 to 1.2 s, median 3.0 to 3.5 words per second. The slowest tenth runs 4.4 to 6.3 words per second (23 to 28 characters per second, over the 20 limit).
- 25 to 33% of chunks end on a small word (a, the, to, and, is, your). Example: "SO HARD? IS A / QUESTION THAT'S BEEN ON". The break follows the word count, not the grammar.

## Gen's references (looked at closely: R02 Koe, R09 Hiro, R10 and R13 Sinek; the others rely on the Reel Style Guide notes)
- Chunks follow the clause, not a count: "you go," / "the accounts" / "you follow, the information" / "that you consume," (Koe). "SINI NIH" / "FUNBARUZU YANG ADA" / "DI RUMAHKU" (Hiro). "EITHER YOU'LL QUIT," / "RETIRE," / "OR GET FIRED," / "BUT IT'S GONNA END, RIGHT?" (Sinek).
- Length varies from 1 to 6 words. Short chunks flash, long chunks stay about 1.5 to 2 s. None ends on a small word. A line break only when a chunk is long.
- OCR on the reference frames failed, so no averages are claimed.

## Auto-caption "slop" sea
- Tools and templates (Hormozi style, Submagic, OpusClip type) default to word-by-word or 1 to 4 words, cut by count and timing, not grammar. Vendor guides say 3 to 4 words (viralday) or 3 to 7 (OpusClip). None of their retention numbers cite a study ("double the retention" is unsourced; one guide says its own figures are pending verification).
- No actual slop accounts were sampled. This is vendor claims only.

## Decision for review
Replace the "2 to 4 words per chunk" rule with: one phrase per chunk, usually 2 to 5 words, never end on a small word, at least 0.33 s per word (about 3 words per second), 2 lines only when the phrase needs it. Not applied to the videos yet.

Sources: Szarkowska et al. 2024 (jatjournal.org, wrap.warwick.ac.uk); Rajendran et al. 2013 (andrewd.ces.clemson.edu); Draxler et al. 2023 (arxiv.org/abs/2307.05870); Mark Studios caption speed study (markstudios.com); OpusClip and viralday caption guides.
