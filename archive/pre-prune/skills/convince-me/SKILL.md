---
name: "convince-me"
description: "Make the full corporate-style case for a decision Claude proposed to Coach Gen: details, evidence, options, pros, cons, and old vs new prototypes. Use when he says convince me or /convince-me."
---

# Convince me

When Gen says "convince me" about something Claude proposed (a design, a rule, a plan, a tool, a workflow), he wants the full case, the way a hired director presents to a CEO: the details and why it is better. Make the strongest honest case, show the real trade-offs, then let him decide. Never pressure.

## The case, per decision (always in this order)

1. **Recommendation.** One sentence, the conclusion first.
2. **Today.** What exists now, with evidence: a screenshot, a file, a measured value, or his own words with the date.
3. **Proposal.** Exactly what changes, with concrete values (hex codes, sizes, names, steps).
4. **Why it is better.** Numbered reasons. Each one is a fact or a mechanism, tied to his goals: consistency, token cost, credibility, and his stated taste.
5. **Options considered.** A table of 3 to 4 options with what each gains and costs. Mark the recommended one.
6. **Cons and risks.** Honest ones, each with its mitigation.
7. **What a yes commits him to.** The concrete next steps, and what does not change.
8. **Prototype.** When the decision is visual, show old and new side by side. Number every image by its decision (Image 1.2 belongs to decision 1).

## Where it goes

- One decision, no images: answer in chat with the 7 parts, short.
- Several decisions or any images: a Claude Doc decision memo.
  - Executive summary first: the conclusion, then a table of every decision with a Status dropdown (Approved, Needs approval, Needs input, Go-ahead needed, Change requested).
  - Already-approved decisions sit in their own section, apart from the ones that need approval.
  - Inputs only he can give (names, handles, his likes) get fill-in tables.
- Google Docs only when he asks for it. Google Docs can only insert images from a public URL, so a Claude Doc is the default for anything with images.

## Evidence rules

- His own words, files, and screenshots beat general claims. When citing his taste, quote him and give the date.
- Never invent data. Mark placeholder copy and numbers as placeholders.
- An old version rebuilt from live code, not screenshotted, is labelled as rebuilt.
- Claims about outside facts (contrast ratios, platform safe zones, font licenses) are checked or computed, not guessed.

## Prototype recipe (cheap and repeatable)

1. Old versions: screenshots with the built-in browser. Scroll-reveal animations can leave blank frames: then rebuild the old piece in HTML from the site's live CSS values and text.
2. New versions: one HTML board per image, rendered with Playwright at 1600 px wide. Title "Image <n>" plus a short label, a TODAY tag on the left, a PROPOSED tag on the right, one plain sentence under each side.
3. Fonts come from the Google Fonts repo (raw.githubusercontent.com/google/fonts/main/ofl/...). In inline style attributes, write font names with &quot; quotes, because single quotes break a single-quoted style attribute.
4. Look at every image (a contact sheet with ImageMagick montage saves tokens) before uploading.
5. Upload all images in one Artifact asset call to the doc's link, create all blobs in one docs batch, then embed them section by section.

## Writing rules

- Plain words his clients would understand. No em dashes. Oxford comma.
- Short sentences, specific numbers, no adjectives standing in for facts.
- Keep the chat reply to one line once the memo is ready.