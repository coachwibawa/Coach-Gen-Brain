# 13 Web (rules for any page or Antigravity brief)

Version 1.1, 30 Oct 2026. Load with 01_CORE.md and tokens.json. These are surface rules, not a site plan. Page structure and content are decided per project with Gen.

## 1. Every brief to Antigravity starts with
"Use the attached tokens.css and tokens.json only. Fonts: Montserrat and Libre Baskerville from Google Fonts, nothing else. Square corners (0, or 4 px on buttons and inputs). No gradients, glows or shadows. Voice in first person 'I'."
Attach `tokens.css` and the logo files the page needs.

## 2. Type scale (size/line height px)
| Role | Desktop | Mobile |
|---|---|---|
| Display | 56/64 Montserrat 700 | 36/44 |
| H1 | 44/52 | 32/40 |
| H2 | 32/40 | 26/34 |
| H3 | 24/32 | 20/28 |
| Eyebrow | 13/16 Montserrat 600 caps | 12/16 |
| Body (UI) | 17/28 Montserrat 400 | 16/26 |
| Body (articles) | 19/32 Libre Baskerville | 18/30 |
| Quote | 28/40 Libre Baskerville italic | 22/32 |

## 3. Layout
Max content width 1200 px, 12 columns, 24 px gutters, 24 px side padding on mobile. Section spacing 96 px desktop, 64 px mobile.

## 4. Components
- Header: horizontal Coach Gen logo (blue family), menu, one button.
- Button primary: Deep Water background, White text, Montserrat 600 caps +0.06 em, radius 4 px. On dark: Aqua background, Abyss text.
- Offer card (every offer, no exceptions): name (Montserrat 700), one-line promise, who it is for, one button. 2 px rule on top in the family color. Square corners.
  - ADDED (30 Oct 2026): the card also holds the offer's sub-brand mark (next to the name) and a photo slot on top. No real photo yet: the mark large on a brand color. A Reel may play in the slot as a short silent loop.
- Testimonial card: quote in Libre Baskerville italic, real name and role in Montserrat 600. Real clients only.
- Section dividers: the maze line.
- Book section: the one place a gold section may sit inside a blue page (full-width background change).
- Interactive tools (calculators, diagnostics): allowed and liked. Any figure they use shows its source.
  - CORRECTION (30 Oct 2026): Gen scored the ROI calculator low ("probably kinda trash, or can be in a submodule"). Tools live on track pages, not the home page. The 5 Laws diagnostic is the one tool on the home page.
- ADDED (30 Oct 2026): the method section on any page is the 5 Laws, not a separate set of keys. Introvert statistics live on the Introverts track page, sourced.

## 5. Meta
- Page title: "<Page name> | Coach Gen". Author: Genison Wibawa.
- Share image: 1200 x 628 from `CoachGen-Logo-Kit/05_Website`, or a page-specific one in the same template.
- Favicon: micro mark from the kit.

## 6. Checklist for any page
1. Only the two fonts load.
2. No gradient, glow or shadow in the CSS.
3. "I", never "we".
4. Every menu link works (no 404s).
5. Testimonials are real, statistics sourced.
6. Title line on the page matches the audience (01_CORE section 2).
