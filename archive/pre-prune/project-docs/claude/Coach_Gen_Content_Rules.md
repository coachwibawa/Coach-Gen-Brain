# Coach Gen Content Rules

The voice rules for the articles-to-content pipeline (`content-from-article` skill). Scope: short-form content pieces derived from an existing article (Inside The Introvert, Lasting Change Letters, or anything pasted in), close to the 5x5x5 shape, but any shape the run calls for.

**This is a separate rulebook from `Coach_Gen_Language_Rules.md` (article voice) and `claude/Coach_Gen_Book_Rules.md` (book voice).** Confirmed directly: content language requirements differ from both, and this subset is learned bottom-up through its own epochs, not inherited from either existing rulebook. Do not copy rules in from them. If a genuine overlap shows up through real correction, log it here in this doc's own words.

**Maintaining this document.** Add and annotate. Never condense. When a later finding corrects an earlier rule, keep the old line and mark the correction, so the reasoning survives.

**How a rule gets added.** Each run of `content-from-article` is a potential epoch. When Coach Gen reacts to or corrects an output, and a real rule falls out of that correction, propose the exact line here before writing it, then log it under Calibration Log below with the date and what prompted it. Reasoned explicitly against overfitting: never derive a rule from an edit he did not complain about, and flag if a proposed rule risks overfitting to one piece.

---

# 1. RULES

## Baseline, carried over from the 555 work (not epoch-derived, his own direct instructions)

These came from the earlier 5x5x5 brainstorm work in this project, before this doc existed. They're baseline, not calibration findings, so they're logged here rather than under Calibration Log, which is reserved for rules actually derived from a correction.

- **Strip to bare suggestions.** The highlights, formats, and headline fives are bare suggestions only, no source citations and no field labels, as long as the underlying reading/research was actually done and these rules were followed.
- **The 4th five is recommended combos.** Unordered, each one a combination of picks from the first three fives, selected by: (1) whether he's done that content before, (2) audience impact, (3) importance to the framework.
- **Combos get full storyboards, not labels.** A "do these" combo needs a full beat-by-beat storyboard with production tags up front. Never a one-line label plus a rationale.
- **Content-kitchen leads come only from him, never looked up or invented.** No Notion query, no static assumed list of his formats. Content-kitchen formats/examples enter only through what he supplies for that run (via `pointers`).
- **Default shape is the four fives.** When a run doesn't specify otherwise, produce the full 5x5x5 brainstorm (5 highlights, 5 formats, 5 headlines, 5 combos). When he asks for a single piece, a specific count, or anything else, produce exactly that instead.

---

# 2. CALIBRATION LOG

*(empty, nothing run through this skill yet. Each entry: date, source article, what he corrected, the rule drawn from it.)*
