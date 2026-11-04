# 17 Templates (load for any visual made from a template)

Version 1.1, 30 Oct 2026. Load with 01_CORE.md. The renderer is `brand/templates/cg_render.py` in the project (mirror: Mac `Brand/Templates/cg_render.py`).

## 1. Rule
Every visual starts from one of these templates. No blank-page design. A new kind of visual needs a new template, approved by Gen, before it ships.

## 2. How an agent uses it
1. Get `cg_render.py` (project_read it into the working directory, or use the Mac copy).
2. Write the fields as JSON (see the table). Put `==word==` around the one highlight word where a headline allows it.
3. Run `python3 cg_render.py TEMPLATE fields.json out.png`. Carousels write one PNG per slide, or a PDF when the output ends in `.pdf` (LinkedIn document posts).
4. `python3 cg_render.py --list` prints every template. `--examples DIR` renders one of each.
5. Needs Python 3 with Playwright and Pillow. Fonts download once from the Google Fonts repo.
6. Look at the result once before delivering.

## 3. Templates
| Template | Size | Fields | Used for |
|---|---|---|---|
| carousel | 1080 x 1350 per slide, or PDF | mode teach, thought, or author; slides of kind cover, body, end with eyebrow, title, body, cta | Instagram carousels when not using the Coachinator, LinkedIn document posts |
| quote | 1080 x 1350 | quote, name, role, family | Quote cards, client quotes (real clients with permission) |
| reel_title | 1080 x 1920 | eyebrow, title, family | Title card of full talks |
| lower_third | 1080 x 1920, transparent | audience casual, corporate, or individual | Name and title line on first appearance in a video |
| end_card | 1080 x 1920 | cta, audience, family | Last 3 seconds of a Reel |
| ad | 9x16, 4x5, 1x1, or all | eyebrow, headline, cta, audience, photo, family | Meta and LinkedIn ads, one layout in three sizes |
| offer_card | 720 x 1080 | mark, name, promise, who, tag, cta, photo, family | Website catalog, offer posts |
| article_header | 1200 x 628 | series, title, date, family | Article header and share image |
| newsletter_header | 1200 x 360 | series, edition, family | Email newsletter header, shown 600 wide |
| video_bg | 1920 x 1080 | family, show_name, audience | Zoom, Google Meet, and Teams backgrounds |
| linkedin_banner | 1584 x 396 | promise, audience, site, family | LinkedIn personal banner |
| highlight_cover | 1080 x 1920 | mark, family | Instagram Story highlight covers |
| youtube_thumb | 1280 x 720 | eyebrow, headline, photo, family | YouTube thumbnails |
| podcast_cover | 3000 x 3000 | title, host, mark, family | Inside the Introvert podcast cover |
| wa_icon | 1080 x 1080 | family | WhatsApp group icon |
| offer_mark | 512 x 512, transparent | mark, family or color | Single offer mark |
| certificate | A4 landscape, PNG or PDF | name, program, date, family (gold-light) | Completion certificates for paid programs |
| speaker_kit | A4 portrait, PNG or PDF | bio, talks, proof, formats, contact, photo, audience | One-pager for event organisers |
| qr | 1080 x 1080 | url, family, with_mark | QR codes for cards, slides, and print |

Families: blue, blue-light, gold, gold-light. Mode decides the family in carousels: teach and thought are blue, author is gold.

## 4. Offer marks
| Key | Offer | Shape |
|---|---|---|
| 5laws | 5 Laws of Lasting Change (flagship) | Five steps, right angles |
| 6c | 6C of Public Speaking | Hexagon (named exception to the no-diagonals rule) |
| ila | Introversion Leverage | Triangle (named exception) |
| eoi | Engineer of Influence | Brackets around a square |
| iti | Inside The Introvert | An I inside a square |
| lcl | Lasting Change Letters | A page with lines |
All drawn on a 32-unit grid with 4-unit strokes and square corners, like the logo. Files: Mac `Brand/Offer-Marks/` (SVG and PNG in aqua, deep-water, gold, deep-gold, white, black).

## 4b. Rules for the new templates (added 30 Oct 2026)
- QR codes are always dark modules on a light background. Dark families switch to their light twin automatically, because many phone scanners cannot read light-on-dark codes. Test every new QR code with a phone before printing.
- Certificates use the gold family (paid program documents). Print from the PDF.
- The speaker kit needs the original portrait file for print. The screenshot copy is too small.

## 4c. Other ready files (Mac)
- `Brand/Merch/`: print files of the mark for shirts (SVG and 4000 px PNG), with sizes in its README.
- `Brand/Website/start-here.html`: the link-in-bio page that replaces Linktree. Links marked VERIFY need Gen's check. Give it to Antigravity with ANTIGRAVITY-RULES.md.

## 5. Video call backgrounds
- The head sits in the middle, so the logo goes top left and the name top right. Nothing sits behind the face.
- Self-view may show the background mirrored. Other people see it the right way round. Do not flip the file.
- Use show_name true with the audience line for client and corporate calls. Use show_name false (logo only) for casual calls.
- Ready files: Mac `Brand/Templates/examples/video_bg_*.png`.

## 6. Fonts
Montserrat and Libre Baskerville files sit in Mac `Brand/Fonts/`. Double-click each file and press Install so Concat, Word, Pages, and Keynote can use them.

## 7. Checklist
1. Started from a template, not a blank page.
2. Family matches the content (01_CORE section 4).
3. One highlight word at most.
4. Title line matches the audience.
5. Looked at the render once.

## 4d. Signature (added 3 Nov 2026)
- Gen's handwritten signature, cleaned from his photo of 3 Nov 2026: Mac `Brand/Signature/`. Transparent PNGs: `genison_signature_ink.png` (near black, for light backgrounds and print), `genison_signature_abyss.png` (Abyss), `genison_signature_white.png` (for dark backgrounds). The original photo is kept next to them.
- The certificate template takes an optional field `signature` (path to the transparent PNG). It sits on the signature line, right side, above "Genison Wibawa, ICF Associate Certified Coach (ACC)". The left line is the date, now labelled "Date" under it.
- Use the signature only on documents Gen issues himself (certificates, letters, proposals he has approved). Never on anything sent without his go.
- CORRECTION to the table in section 3 (3 Nov 2026): certificate fields are name, program, date, signature (optional), family (gold-light).
