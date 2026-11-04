# 11 Social static (Instagram, LinkedIn, Facebook)

Version 1.1, 30 Oct 2026. Load with 01_CORE.md. Copy rules (hooks, hashtags, sign-offs, language mix) live in `claude/Coach_Gen_Social_Posting_Rules.md`. This file covers looks only.

## 1. Per platform
| Platform | Formats | Look | Language |
|---|---|---|---|
| Instagram | 4:5 carousels and posts, 9:16 Stories | The Coachinator look: floating pictures and silhouette images over the brand background. A plain text-on-black slide is not enough on Instagram | Full English |
| LinkedIn | 1:1 image, 4:5 document carousel (PDF) | Calmer: one image or a clean document carousel. Gold family allowed for author and speaking posts | English |
| Facebook | 1:1 or 4:5 image | Minimalist: one object, lots of empty space, at most a word or two of text | English title, Indonesian tag line (see posting rules) |

## 1b. Three modes, same two fonts (added 30 Oct 2026)
| Mode | Headline font | Family | Used for |
|---|---|---|---|
| Teach | Montserrat 800 | Blue | Carousels that teach, ads, Professional and Persona Reels |
| Thought | Libre Baskerville 400 | Blue | Quotes, reframes, Thought Reels. Max about 16 words on a cover |
| Author | Libre Baskerville 400 or italic | Gold | The book, Lasting Change Letters, speaking |
The mode follows the post type. No agent picks a mode freely.

## 2. Route (cheapest first)
1. Instagram carousels: write a Coachinator Script Import script. Never drive the Slide Editor field by field. Never click Save in the Coachinator. Gen adds floating pictures and silhouettes by hand.
2. Single images: one AI image prompt (16_IMAGERY.md) or one rendered template.
3. Rendered templates (HTML to PNG) only for LinkedIn document carousels, quote cards and ads.

## 3. Coachinator setup (one time, then reuse)
Make two style presets in the Coachinator and use only these: "CG Blue" (Abyss background, Mist text, Aqua accent pill) and "CG Gold" (Charcoal background, Ivory text, Gold accent pill). Fonts Montserrat and Libre Baskerville. Scripts then name the preset instead of styling slide by slide.
  - CORRECTION (30 Oct 2026): three presets, CG Blue, CG Blue Light (Mist background, Abyss text, Deep Water pill), and CG Gold (heading in Libre Baskerville Gold). No Claude Code needed: make them by hand with the Style presets button, or paste the Antigravity prompt from the decision memo (decision 8) if the fonts are missing. Scripts may start with "preset: CG Blue" once Antigravity adds that line.
- In scripts, `==accent pill==` uses the family accent. `++green reward pill++` is not used (green is not in the palette).

## 4. Carousel template (4:5)
- Slide 1: hook only. Montserrat 700 80 px, max 8 words, eyebrow label above (series name, caps). Mark bottom left at 64 px.
- Middle slides: one idea each. Heading 64 px plus up to 30 words of body at 36 to 40 px. Slide number bottom right, "3/7".
- Last slide: one call to action, the handle, stacked logo.
- One background color for the whole carousel. Slide count follows the story, not a fixed number.

## 5. Quote card (4:5)
Libre Baskerville italic 56/76, max 30 words, maze-line rule above, name below in Montserrat 600 caps 28 px. Client quotes from real clients with permission only.

## 6. LinkedIn document carousel
Same template as section 4, exported as one PDF, 1080 x 1350 pages. Title line on the last page follows the audience (usually ICF ACC on LinkedIn).

## 7. Profile set
Profile picture: mark only or Gen's portrait, 1080 x 1080, same on every platform. Banners from `CoachGen-Logo-Kit/03_Social`. Bio title line: International Coach & Author.

## 8. Checklist before delivery
1. Right language for the platform.
2. One family, one background per carousel.
3. Headline inside the centre 1012 px on 4:5.
4. No text under 24 px.
5. Mark or logo present once.
6. No composite names as testimonials.
