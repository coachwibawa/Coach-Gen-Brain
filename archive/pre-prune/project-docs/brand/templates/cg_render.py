#!/usr/bin/env python3
"""Coach Gen template renderer, brand guide v1.1 (30 Oct 2026).

Renders every Coach Gen master template from a small JSON file, so no agent
designs from a blank page. Values come from brand/01_CORE.md and the modules.

  python3 cg_render.py --list
  python3 cg_render.py TEMPLATE fields.json OUT.png   (or OUT.pdf for carousel)
  python3 cg_render.py --examples OUTDIR               (one sample of everything)

Needs Python 3 with playwright (Chromium). Fonts download once from the
Google Fonts repo on GitHub into ~/.cache/cg_fonts.
"""
import sys, os, json, html, pathlib, urllib.request

# ---------------------------------------------------------------- tokens
C = dict(abyss='#01131C', deep='#0D4A59', aqua='#72CCD0', mist='#EAF5F6',
         charcoal='#2B2B2B', gold='#C8B796', deepgold='#9A8360', ivory='#F6F2EA',
         white='#FFFFFF', black='#000000')
FAM = {
    'blue':       dict(bg=C['abyss'], fg=C['mist'], head='#FFFFFF', acc=C['aqua'], btn=C['aqua'], btnfg=C['abyss'], logo=C['aqua']),
    'blue-light': dict(bg=C['mist'], fg=C['abyss'], head=C['abyss'], acc=C['deep'], btn=C['deep'], btnfg=C['white'], logo=C['deep']),
    'gold':       dict(bg=C['charcoal'], fg=C['ivory'], head=C['gold'], acc=C['gold'], btn=C['gold'], btnfg=C['charcoal'], logo=C['gold']),
    'gold-light': dict(bg=C['ivory'], fg=C['charcoal'], head=C['charcoal'], acc=C['deepgold'], btn=C['charcoal'], btnfg=C['ivory'], logo=C['deepgold']),
}
TITLE_LINE = {
    'casual': 'International Coach &amp; Author',
    'corporate': 'ICF Associate Certified Coach (ACC)',
    'individual': 'Certified Professional Coach (CPC)',
}
HANDLE = '@coachgenofficial'

# ---------------------------------------------------------------- logos
MARK_D = 'M0 0 L256 0 L256 88 L224 88 L224 32 L32 32 L32 224 L224 224 L224 112 L256 112 L256 256 L0 256 Z M56 56 L200 56 L200 88 L88 88 L88 168 L168 168 L168 144 L120 144 L120 112 L200 112 L200 200 L56 200 Z'
LOGOS = {"stacked": {"vb": "0 0 256 312", "p": [{"d": "M0 0 L256 0 L256 88 L224 88 L224 32 L32 32 L32 224 L224 224 L224 112 L256 112 L256 256 L0 256 Z M56 56 L200 56 L200 88 L88 88 L88 168 L168 168 L168 144 L120 144 L120 112 L200 112 L200 200 L56 200 Z", "t": ""}, {"d": "M13 0.4Q10.2 0.4 7.82 -0.5Q5.44 -1.41 3.7 -3.08Q1.95 -4.75 0.97 -7.02Q0 -9.28 0 -12Q0 -14.72 0.97 -16.98Q1.95 -19.25 3.71 -20.92Q5.46 -22.59 7.84 -23.5Q10.22 -24.4 13.02 -24.4Q16.14 -24.4 18.67 -23.32Q21.2 -22.25 22.9 -20.16L19.34 -16.86Q18.11 -18.26 16.6 -18.98Q15.08 -19.7 13.29 -19.7Q11.6 -19.7 10.2 -19.14Q8.8 -18.58 7.78 -17.56Q6.75 -16.53 6.18 -15.12Q5.62 -13.7 5.62 -12Q5.62 -10.3 6.18 -8.88Q6.75 -7.47 7.78 -6.44Q8.8 -5.42 10.2 -4.86Q11.6 -4.3 13.29 -4.3Q15.08 -4.3 16.6 -5.02Q18.11 -5.74 19.34 -7.16L22.9 -3.86Q21.2 -1.79 18.67 -0.69Q16.14 0.4 13 0.4Z M43.06 0.4Q40.23 0.4 37.82 -0.52Q35.41 -1.45 33.65 -3.12Q31.88 -4.8 30.9 -7.06Q29.92 -9.32 29.92 -12.01Q29.92 -14.69 30.9 -16.94Q31.88 -19.19 33.65 -20.88Q35.42 -22.56 37.82 -23.48Q40.22 -24.4 43.05 -24.4Q45.9 -24.4 48.28 -23.48Q50.67 -22.57 52.43 -20.89Q54.2 -19.21 55.18 -16.96Q56.16 -14.7 56.16 -12Q56.16 -9.31 55.18 -7.05Q54.2 -4.78 52.43 -3.11Q50.67 -1.43 48.28 -0.52Q45.9 0.4 43.06 0.4ZM43.05 -4.3Q44.66 -4.3 46.02 -4.86Q47.38 -5.42 48.4 -6.45Q49.41 -7.48 49.98 -8.89Q50.54 -10.3 50.54 -12.01Q50.54 -13.72 49.98 -15.12Q49.41 -16.52 48.4 -17.55Q47.38 -18.58 46.02 -19.14Q44.66 -19.7 43.05 -19.7Q41.44 -19.7 40.08 -19.14Q38.71 -18.58 37.69 -17.55Q36.67 -16.52 36.1 -15.11Q35.54 -13.71 35.54 -12.01Q35.54 -10.3 36.1 -8.89Q36.67 -7.48 37.69 -6.45Q38.7 -5.42 40.07 -4.86Q41.44 -4.3 43.05 -4.3Z M62.29 0 72.99 -24H78.48L89.2 0H83.4L74.6 -21.17H76.8L68 0ZM67.66 -5.13 69.12 -9.35H81.48L82.96 -5.13Z M108.32 0.4Q105.52 0.4 103.14 -0.5Q100.76 -1.41 99.01 -3.08Q97.27 -4.75 96.29 -7.02Q95.32 -9.28 95.32 -12Q95.32 -14.72 96.29 -16.98Q97.27 -19.25 99.02 -20.92Q100.78 -22.59 103.16 -23.5Q105.54 -24.4 108.34 -24.4Q111.46 -24.4 113.98 -23.32Q116.51 -22.25 118.21 -20.16L114.66 -16.86Q113.43 -18.26 111.92 -18.98Q110.4 -19.7 108.6 -19.7Q106.92 -19.7 105.52 -19.14Q104.12 -18.58 103.09 -17.56Q102.07 -16.53 101.5 -15.12Q100.93 -13.7 100.93 -12Q100.93 -10.3 101.5 -8.88Q102.07 -7.47 103.09 -6.44Q104.12 -5.42 105.52 -4.86Q106.92 -4.3 108.6 -4.3Q110.4 -4.3 111.92 -5.02Q113.43 -5.74 114.66 -7.16L118.21 -3.86Q116.51 -1.79 113.98 -0.69Q111.46 0.4 108.32 0.4Z M143.19 0V-24H148.76V0ZM126.74 0V-24H132.31V0ZM131.88 -9.84V-14.52H143.6V-9.84Z M185.92 0.4Q183.09 0.4 180.7 -0.5Q178.31 -1.41 176.55 -3.08Q174.79 -4.75 173.82 -7.02Q172.84 -9.28 172.84 -12Q172.84 -14.72 173.82 -16.98Q174.79 -19.25 176.57 -20.92Q178.34 -22.59 180.74 -23.5Q183.15 -24.4 186.03 -24.4Q189.22 -24.4 191.78 -23.35Q194.33 -22.29 196.07 -20.27L192.52 -16.97Q191.21 -18.36 189.67 -19.03Q188.13 -19.7 186.29 -19.7Q184.56 -19.7 183.12 -19.14Q181.68 -18.58 180.63 -17.56Q179.59 -16.53 179.02 -15.12Q178.46 -13.72 178.46 -12Q178.46 -10.33 179.02 -8.92Q179.59 -7.5 180.63 -6.47Q181.68 -5.43 183.1 -4.87Q184.51 -4.3 186.23 -4.3Q187.89 -4.3 189.44 -4.84Q190.99 -5.37 192.49 -6.65L195.63 -2.65Q193.66 -1.15 191.08 -0.37Q188.49 0.4 185.92 0.4ZM195.63 -2.65 190.57 -3.37V-12.38H195.63Z M205.87 0V-24H224V-19.53H211.39V-4.47H224.46V0ZM210.98 -10.02V-14.34H222.55V-10.02Z M233.98 0V-24H238.56L252.73 -6.7H250.51V-24H256V0H251.42L237.25 -17.3H239.46V0Z", "t": "translate(0 312)"}]}, "horizontal": {"vb": "0 0 1002.67 256", "p": [{"d": "M0 0 L256 0 L256 88 L224 88 L224 32 L32 32 L32 224 L224 224 L224 112 L256 112 L256 256 L0 256 Z M56 56 L200 56 L200 88 L88 88 L88 168 L168 168 L168 144 L120 144 L120 112 L200 112 L200 200 L56 200 Z", "t": ""}, {"d": "M13 0.4Q10.2 0.4 7.82 -0.5Q5.44 -1.41 3.7 -3.08Q1.95 -4.75 0.97 -7.02Q0 -9.28 0 -12Q0 -14.72 0.97 -16.98Q1.95 -19.25 3.71 -20.92Q5.46 -22.59 7.84 -23.5Q10.22 -24.4 13.02 -24.4Q16.14 -24.4 18.67 -23.32Q21.2 -22.25 22.9 -20.16L19.34 -16.86Q18.11 -18.26 16.6 -18.98Q15.08 -19.7 13.29 -19.7Q11.6 -19.7 10.2 -19.14Q8.8 -18.58 7.78 -17.56Q6.75 -16.53 6.18 -15.12Q5.62 -13.7 5.62 -12Q5.62 -10.3 6.18 -8.88Q6.75 -7.47 7.78 -6.44Q8.8 -5.42 10.2 -4.86Q11.6 -4.3 13.29 -4.3Q15.08 -4.3 16.6 -5.02Q18.11 -5.74 19.34 -7.16L22.9 -3.86Q21.2 -1.79 18.67 -0.69Q16.14 0.4 13 0.4Z M43.06 0.4Q40.23 0.4 37.82 -0.52Q35.41 -1.45 33.65 -3.12Q31.88 -4.8 30.9 -7.06Q29.92 -9.32 29.92 -12.01Q29.92 -14.69 30.9 -16.94Q31.88 -19.19 33.65 -20.88Q35.42 -22.56 37.82 -23.48Q40.22 -24.4 43.05 -24.4Q45.9 -24.4 48.28 -23.48Q50.67 -22.57 52.43 -20.89Q54.2 -19.21 55.18 -16.96Q56.16 -14.7 56.16 -12Q56.16 -9.31 55.18 -7.05Q54.2 -4.78 52.43 -3.11Q50.67 -1.43 48.28 -0.52Q45.9 0.4 43.06 0.4ZM43.05 -4.3Q44.66 -4.3 46.02 -4.86Q47.38 -5.42 48.4 -6.45Q49.41 -7.48 49.98 -8.89Q50.54 -10.3 50.54 -12.01Q50.54 -13.72 49.98 -15.12Q49.41 -16.52 48.4 -17.55Q47.38 -18.58 46.02 -19.14Q44.66 -19.7 43.05 -19.7Q41.44 -19.7 40.08 -19.14Q38.71 -18.58 37.69 -17.55Q36.67 -16.52 36.1 -15.11Q35.54 -13.71 35.54 -12.01Q35.54 -10.3 36.1 -8.89Q36.67 -7.48 37.69 -6.45Q38.7 -5.42 40.07 -4.86Q41.44 -4.3 43.05 -4.3Z M62.29 0 72.99 -24H78.48L89.2 0H83.4L74.6 -21.17H76.8L68 0ZM67.66 -5.13 69.12 -9.35H81.48L82.96 -5.13Z M108.32 0.4Q105.52 0.4 103.14 -0.5Q100.76 -1.41 99.01 -3.08Q97.27 -4.75 96.29 -7.02Q95.32 -9.28 95.32 -12Q95.32 -14.72 96.29 -16.98Q97.27 -19.25 99.02 -20.92Q100.78 -22.59 103.16 -23.5Q105.54 -24.4 108.34 -24.4Q111.46 -24.4 113.98 -23.32Q116.51 -22.25 118.21 -20.16L114.66 -16.86Q113.43 -18.26 111.92 -18.98Q110.4 -19.7 108.6 -19.7Q106.92 -19.7 105.52 -19.14Q104.12 -18.58 103.09 -17.56Q102.07 -16.53 101.5 -15.12Q100.93 -13.7 100.93 -12Q100.93 -10.3 101.5 -8.88Q102.07 -7.47 103.09 -6.44Q104.12 -5.42 105.52 -4.86Q106.92 -4.3 108.6 -4.3Q110.4 -4.3 111.92 -5.02Q113.43 -5.74 114.66 -7.16L118.21 -3.86Q116.51 -1.79 113.98 -0.69Q111.46 0.4 108.32 0.4Z M143.19 0V-24H148.76V0ZM126.74 0V-24H132.31V0ZM131.88 -9.84V-14.52H143.6V-9.84Z M185.92 0.4Q183.09 0.4 180.7 -0.5Q178.31 -1.41 176.55 -3.08Q174.79 -4.75 173.82 -7.02Q172.84 -9.28 172.84 -12Q172.84 -14.72 173.82 -16.98Q174.79 -19.25 176.57 -20.92Q178.34 -22.59 180.74 -23.5Q183.15 -24.4 186.03 -24.4Q189.22 -24.4 191.78 -23.35Q194.33 -22.29 196.07 -20.27L192.52 -16.97Q191.21 -18.36 189.67 -19.03Q188.13 -19.7 186.29 -19.7Q184.56 -19.7 183.12 -19.14Q181.68 -18.58 180.63 -17.56Q179.59 -16.53 179.02 -15.12Q178.46 -13.72 178.46 -12Q178.46 -10.33 179.02 -8.92Q179.59 -7.5 180.63 -6.47Q181.68 -5.43 183.1 -4.87Q184.51 -4.3 186.23 -4.3Q187.89 -4.3 189.44 -4.84Q190.99 -5.37 192.49 -6.65L195.63 -2.65Q193.66 -1.15 191.08 -0.37Q188.49 0.4 185.92 0.4ZM195.63 -2.65 190.57 -3.37V-12.38H195.63Z M205.87 0V-24H224V-19.53H211.39V-4.47H224.46V0ZM210.98 -10.02V-14.34H222.55V-10.02Z M233.98 0V-24H238.56L252.73 -6.7H250.51V-24H256V0H251.42L237.25 -17.3H239.46V0Z", "t": "translate(320 160) scale(2.666667)"}]}}

def mark(color, w):
    return f"<svg width='{w}' height='{w}' viewBox='0 0 256 256'><path fill-rule='evenodd' fill='{color}' d='{MARK_D}'/></svg>"

def lockup(kind, color, w):
    L = LOGOS[kind]; x0, y0, vw, vh = [float(v) for v in L['vb'].split()]
    h = w * vh / vw
    paths = ''.join(f"<path fill-rule='evenodd' fill='{color}' transform='{p['t']}' d='{p['d']}'/>" for p in L['p'])
    return f"<svg width='{w:.0f}' height='{h:.0f}' viewBox='{L['vb']}'>{paths}</svg>"

# Offer marks: 32-unit grid, 4-unit strokes, square corners (decision E, 30 Oct 2026).
OFFER = {
    '5laws': "<path d='M2 30 H8 V24 H14 V18 H20 V12 H26 V6 H30' fill='none' stroke='{c}' stroke-width='4' stroke-linejoin='miter' stroke-linecap='square'/>",
    '6c': "<path d='M16 2.5 L28.5 9.5 V22.5 L16 29.5 L3.5 22.5 V9.5 Z' fill='none' stroke='{c}' stroke-width='4' stroke-linejoin='miter'/>",
    'ila': "<path d='M16 3.5 L29.5 28.5 H2.5 Z' fill='none' stroke='{c}' stroke-width='4' stroke-linejoin='miter'/>",
    'eoi': "<path d='M10 2 H2 V30 H10 M22 2 H30 V30 H22' fill='none' stroke='{c}' stroke-width='4' stroke-linejoin='miter'/><rect x='12' y='12' width='8' height='8' fill='{c}'/>",
    'iti': "<rect x='2' y='2' width='28' height='28' fill='none' stroke='{c}' stroke-width='4'/><rect x='14' y='9' width='4' height='14' fill='{c}'/>",
    'lcl': "<rect x='4' y='2' width='24' height='28' fill='none' stroke='{c}' stroke-width='4'/><rect x='10' y='10' width='12' height='3' fill='{c}'/><rect x='10' y='16' width='12' height='3' fill='{c}'/><rect x='10' y='22' width='8' height='3' fill='{c}'/>",
}
OFFER_NAMES = {'5laws': '5 Laws of Lasting Change', '6c': '6C of Public Speaking', 'ila': 'Introversion Leverage',
               'eoi': 'Engineer of Influence', 'iti': 'Inside The Introvert', 'lcl': 'Lasting Change Letters'}

def offer_mark(key, color, w):
    return f"<svg width='{w}' height='{w}' viewBox='0 0 32 32'>{OFFER[key].format(c=color)}</svg>"

# ---------------------------------------------------------------- fonts
FONT_SRC = {
    'Montserrat.ttf': 'montserrat/Montserrat%5Bwght%5D.ttf',
    'Montserrat-Italic.ttf': 'montserrat/Montserrat-Italic%5Bwght%5D.ttf',
    'LibreBaskerville.ttf': 'librebaskerville/LibreBaskerville%5Bwght%5D.ttf',
    'LibreBaskerville-Italic.ttf': 'librebaskerville/LibreBaskerville-Italic%5Bwght%5D.ttf',
}
def fonts_css():
    cache = pathlib.Path(os.environ.get('CG_FONT_DIR', pathlib.Path.home() / '.cache' / 'cg_fonts'))
    cache.mkdir(parents=True, exist_ok=True)
    for name, path in FONT_SRC.items():
        f = cache / name
        if not f.exists() or f.stat().st_size < 10000:
            urllib.request.urlretrieve('https://raw.githubusercontent.com/google/fonts/main/ofl/' + path, f)
    u = lambda n: (cache / n).as_uri()
    return (f"@font-face{{font-family:M;src:url('{u('Montserrat.ttf')}');font-weight:100 900}}"
            f"@font-face{{font-family:M;src:url('{u('Montserrat-Italic.ttf')}');font-weight:100 900;font-style:italic}}"
            f"@font-face{{font-family:B;src:url('{u('LibreBaskerville.ttf')}');font-weight:400 700}}"
            f"@font-face{{font-family:B;src:url('{u('LibreBaskerville-Italic.ttf')}');font-weight:400 700;font-style:italic}}")

def esc(t):
    return html.escape(str(t or ''), quote=False).replace('\n', '<br>')

def hl(t, color):
    """==word== marks the one highlight word (captions, ad headlines)."""
    parts = esc(t).split('==')
    return ''.join(f"<span style='color:{color}'>{p}</span>" if i % 2 else p for i, p in enumerate(parts))

# ---------------------------------------------------------------- templates
# Each returns (width, height, inner_html, transparent)

def t_carousel_slide(f, n=1, total=1):
    mode = f.get('mode', 'teach')
    fam = FAM[f.get('family') or ('gold' if mode == 'author' else 'blue')]
    kind = f.get('kind', 'body')
    W, H = 1080, 1350
    if mode == 'teach':
        hcss = "font-family:M;font-weight:800;font-size:{s}px;line-height:1.14"
    elif mode == 'thought':
        hcss = "font-family:B;font-weight:400;font-size:{s}px;line-height:1.42"
    else:
        hcss = "font-family:B;font-style:italic;font-weight:400;font-size:{s}px;line-height:1.42"
    size = {'cover': 88 if mode == 'teach' else 64, 'body': 64 if mode == 'teach' else 52, 'end': 64}[kind]
    eyebrow = f"<div style='font-family:M;font-weight:600;font-size:28px;letter-spacing:.12em;text-transform:uppercase;color:{fam['acc']}'>{esc(f.get('eyebrow'))}</div>" if f.get('eyebrow') else ''
    title = f"<div style='{hcss.format(s=size)};color:{fam['head']};margin-top:28px'>{esc(f.get('title'))}</div>"
    body = f"<div style='font-family:B;font-size:38px;line-height:1.45;color:{fam['fg']};margin-top:36px'>{esc(f.get('body'))}</div>" if f.get('body') else ''
    foot_r = f"{n}/{total}" if kind != 'end' else ''
    if kind == 'end':
        center = (f"<div style='display:flex;flex-direction:column;align-items:flex-start;gap:36px'>{lockup('stacked', fam['logo'], 260)}"
                  f"<div style='{hcss.format(s=56)};color:{fam['head']}'>{esc(f.get('title'))}</div>"
                  f"<div style='font-family:M;font-weight:600;font-size:30px;letter-spacing:.06em;background:{fam['btn']};color:{fam['btnfg']};padding:22px 30px;border-radius:4px'>{esc(f.get('cta', 'FOLLOW FOR MORE'))}</div>"
                  f"<div style='font-family:M;font-size:30px;color:{fam['fg']}'>{esc(f.get('handle', HANDLE))}</div></div>")
        inner = f"<div style='position:absolute;left:96px;right:96px;top:0;bottom:0;display:flex;align-items:center'>{center}</div>"
    else:
        inner = f"<div style='position:absolute;left:96px;right:96px;top:0;bottom:170px;display:flex;flex-direction:column;justify-content:center'>{eyebrow}{title}{body}</div>"
        inner += f"<div style='position:absolute;left:96px;bottom:84px'>{mark(fam['logo'], 64)}</div>"
        inner += f"<div style='position:absolute;right:96px;bottom:98px;font-family:M;font-weight:600;font-size:28px;color:{fam['acc']}'>{foot_r}</div>"
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative;overflow:hidden'>{inner}</div>", False

def t_quote(f):
    fam = FAM[f.get('family', 'blue')]
    W, H = 1080, 1350
    rule = f"<svg width='420' height='34' viewBox='0 0 420 34'><path d='M0 30 H90 V4 H190 V30 H290 V4 H420' fill='none' stroke='{fam['acc']}' stroke-width='4'/></svg>"
    inner = (f"<div style='position:absolute;left:96px;right:96px;top:0;bottom:120px;display:flex;flex-direction:column;justify-content:center;gap:44px'>{rule}"
             f"<div style='font-family:B;font-style:italic;font-size:56px;line-height:76px;color:{fam['head']}'>{esc(f.get('quote'))}</div>"
             f"<div style='font-family:M;font-weight:600;font-size:28px;letter-spacing:.12em;text-transform:uppercase;color:{fam['acc']}'>{esc(f.get('name'))}</div>"
             + (f"<div style='font-family:M;font-size:26px;color:{fam['fg']};margin-top:-30px'>{esc(f.get('role'))}</div>" if f.get('role') else '') +
             f"</div><div style='position:absolute;left:96px;bottom:84px'>{mark(fam['logo'], 64)}</div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative'>{inner}</div>", False

def t_reel_title(f):
    fam = FAM[f.get('family', 'blue')]
    W, H = 1080, 1920
    inner = (f"<div style='position:absolute;left:96px;right:96px;top:270px;bottom:670px;display:flex;flex-direction:column;justify-content:center;gap:40px'>{mark(fam['logo'], 160)}"
             f"<div style='font-family:M;font-weight:600;font-size:30px;letter-spacing:.12em;text-transform:uppercase;color:{fam['acc']}'>{esc(f.get('eyebrow'))}</div>"
             f"<div style='font-family:M;font-weight:700;font-size:72px;line-height:84px;color:{fam['head']}'>{esc(f.get('title'))}</div></div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative'>{inner}</div>", False

def t_lower_third(f):
    fam = FAM[f.get('family', 'blue')]
    W, H = 1080, 1920
    line = TITLE_LINE.get(f.get('audience', 'casual'), f.get('line', TITLE_LINE['casual']))
    bar = (f"<div style='position:absolute;left:64px;top:1030px;background:rgba(1,19,28,.85);border-left:8px solid {fam['acc']};padding:26px 36px'>"
           f"<div style='font-family:M;font-weight:700;font-size:48px;color:#FFFFFF'>{esc(f.get('name', 'Genison Wibawa'))}</div>"
           f"<div style='font-family:M;font-size:32px;color:{C['mist']};margin-top:6px'>{line}</div></div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;position:relative'>{bar}</div>", True

def t_end_card(f):
    fam = FAM[f.get('family', 'blue')]
    W, H = 1080, 1920
    line = TITLE_LINE.get(f.get('audience', 'casual'))
    inner = (f"<div style='position:absolute;left:96px;right:96px;top:270px;bottom:670px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px'>"
             f"{lockup('stacked', fam['logo'], 360)}<div style='font-family:M;font-size:34px;color:{fam['fg']}'>{line}</div>"
             f"<div style='font-family:M;font-weight:700;font-size:34px;letter-spacing:.06em;background:{fam['btn']};color:{fam['btnfg']};padding:26px 36px;border-radius:4px;text-align:center'>{esc(f.get('cta'))}</div>"
             f"<div style='font-family:M;font-size:34px;color:{fam['fg']}'>{esc(f.get('handle', HANDLE))}</div></div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative'>{inner}</div>", False

AD_SIZES = {'9x16': (1080, 1920), '4x5': (1080, 1350), '1x1': (1080, 1080)}
def t_ad(f):
    fam = FAM[f.get('family', 'blue')]
    W, H = AD_SIZES[f.get('size', '9x16')]
    # Everything sits in the central 9:16-safe band so all three crops share one layout.
    top, bottom = {'9x16': (270, 670), '4x5': (110, 110), '1x1': (80, 80)}[f.get('size', '9x16')]
    line = TITLE_LINE.get(f.get('audience', 'individual'))
    photo = ''
    if f.get('photo'):
        photo = f"<div style='position:absolute;inset:0;background:url({pathlib.Path(f['photo']).resolve().as_uri()}) center/cover'></div>"
    panel_bg = fam['bg'] if not f.get('photo') else 'transparent'
    inner = (photo + f"<div style='position:absolute;left:64px;right:64px;top:{top}px;bottom:{bottom}px;display:flex;flex-direction:column;justify-content:flex-end'>"
             f"<div style='background:{fam['bg']};padding:44px 48px;display:flex;flex-direction:column;gap:22px'>"
             f"<div style='display:flex;justify-content:space-between;align-items:center'><div style='font-family:M;font-weight:600;font-size:26px;letter-spacing:.12em;text-transform:uppercase;color:{fam['acc']}'>{esc(f.get('eyebrow'))}</div>{mark(fam['logo'], 56)}</div>"
             f"<div style='font-family:M;font-weight:800;font-size:66px;line-height:74px;color:{fam['head']}'>{hl(f.get('headline'), fam['acc'])}</div>"
             f"<div style='font-family:M;font-size:28px;color:{fam['fg']}'>Genison Wibawa · {line}</div>"
             f"<div style='font-family:M;font-weight:700;font-size:30px;letter-spacing:.06em;background:{fam['btn']};color:{fam['btnfg']};padding:22px 30px;border-radius:4px;align-self:flex-start'>{esc(f.get('cta'))}</div>"
             f"</div></div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{panel_bg if f.get('photo') else fam['bg']};position:relative;overflow:hidden'>{inner}</div>", False

def t_offer_card(f):
    fam = FAM[f.get('family', 'blue')]
    W, H = 720, 1080
    key = f.get('mark', '5laws')
    if f.get('photo'):
        top = f"<div style='height:440px;background:url({pathlib.Path(f['photo']).resolve().as_uri()}) center/cover'></div>"
    else:
        top = f"<div style='height:440px;background:{C['deep'] if fam['bg'] == C['abyss'] else '#3A3A3A'};display:flex;align-items:center;justify-content:center'>{offer_mark(key, fam['acc'], 200)}</div>"
    inner = (top + f"<div style='padding:40px 44px;display:flex;flex-direction:column;gap:18px;height:640px;box-sizing:border-box'>"
             f"<div style='font-family:M;font-weight:600;font-size:22px;letter-spacing:.12em;text-transform:uppercase;color:{fam['acc']}'>{esc(f.get('tag', 'PROGRAM'))}</div>"
             f"<div style='display:flex;align-items:center;gap:18px'>{offer_mark(key, fam['acc'], 56)}<div style='font-family:M;font-weight:700;font-size:40px;line-height:46px;color:{fam['head']}'>{esc(f.get('name', OFFER_NAMES.get(key)))}</div></div>"
             f"<div style='font-family:B;font-size:30px;line-height:44px;color:{fam['fg']}'>{esc(f.get('promise'))}</div>"
             f"<div style='font-family:M;font-size:24px;color:{fam['fg']};opacity:.72'>{esc(f.get('who'))}</div>"
             f"<div style='margin-top:auto;font-family:M;font-weight:700;font-size:24px;letter-spacing:.06em;background:{fam['btn']};color:{fam['btnfg']};padding:18px 26px;border-radius:4px;align-self:flex-start'>{esc(f.get('cta', 'SEE MORE'))}</div></div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};border-top:6px solid {fam['acc']};box-sizing:border-box'>{inner}</div>", False

def t_article_header(f):
    fam = FAM[f.get('family', 'blue')]
    W, H = 1200, 628
    series = f.get('series', 'Inside The Introvert')
    key = 'lcl' if 'Letters' in series else 'iti'
    tfont = "font-family:M;font-weight:700" if f.get('family', 'blue').startswith('blue') else "font-family:B;font-weight:400"
    inner = (f"<div style='position:absolute;left:80px;right:80px;top:70px;bottom:70px;display:flex;flex-direction:column;justify-content:space-between'>"
             f"<div style='display:flex;align-items:center;gap:18px'>{offer_mark(key, fam['acc'], 44)}<div style='font-family:M;font-weight:600;font-size:22px;letter-spacing:.12em;text-transform:uppercase;color:{fam['acc']}'>{esc(series)}</div></div>"
             f"<div style='{tfont};font-size:58px;line-height:70px;color:{fam['head']}'>{esc(f.get('title'))}</div>"
             f"<div style='display:flex;justify-content:space-between;align-items:center'><div style='font-family:M;font-size:22px;color:{fam['fg']}'>{esc(f.get('date'))}</div>{lockup('horizontal', fam['logo'], 230)}</div></div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative'>{inner}</div>", False

def t_wa_icon(f):
    fam = FAM[f.get('family', 'blue')]
    W = H = 1080
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};display:flex;align-items:center;justify-content:center'>{mark(fam['logo'], 560)}</div>", False

def t_offer_mark(f):
    fam = FAM[f.get('family', 'blue')]
    W = H = 512
    bg = 'transparent' if f.get('transparent', True) else fam['bg']
    color = f.get('color') or fam['acc']
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{bg};display:flex;align-items:center;justify-content:center'>{offer_mark(f.get('mark', '5laws'), color, 448)}</div>", f.get('transparent', True)

def t_video_bg(f):
    """Zoom, Google Meet, and Teams background. The head sits in the centre, so marks stay on the edges.
    Self-view may show it mirrored. Other people see it the right way round."""
    fam = FAM[f.get('family', 'blue')]
    W, H = 1920, 1080
    maze = f"<svg width='1920' height='60' viewBox='0 0 1920 60' style='position:absolute;left:0;bottom:120px;opacity:.35'><path d='M0 50 H360 V10 H760 V50 H1160 V10 H1560 V50 H1920' fill='none' stroke='{fam['acc']}' stroke-width='4'/></svg>"
    name = ''
    if f.get('show_name', True):
        line = TITLE_LINE.get(f.get('audience', 'casual'))
        name = (f"<div style='position:absolute;right:96px;top:96px;text-align:right'>"
                f"<div style='font-family:M;font-weight:700;font-size:40px;color:{fam['head']}'>Genison Wibawa</div>"
                f"<div style='font-family:M;font-size:26px;color:{fam['fg']};margin-top:6px'>{line}</div></div>")
    inner = (maze + f"<div style='position:absolute;left:96px;top:96px'>{lockup('horizontal', fam['logo'], 360)}</div>" + name)
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative;overflow:hidden'>{inner}</div>", False

def t_linkedin_banner(f):
    """LinkedIn personal banner 1584x396. The profile photo covers the lower left, so text sits right."""
    fam = FAM[f.get('family', 'blue')]
    W, H = 1584, 396
    line = TITLE_LINE.get(f.get('audience', 'corporate'))
    inner = (f"<div style='position:absolute;right:96px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;align-items:flex-end;gap:14px;text-align:right'>"
             f"<div style='font-family:B;font-size:44px;line-height:58px;color:{fam['head']};max-width:1100px'>{esc(f.get('promise', 'If you keep trying, but never finish, this is why.'))}</div>"
             f"<div style='font-family:M;font-weight:600;font-size:22px;letter-spacing:.12em;text-transform:uppercase;color:{fam['acc']}'>{line} · {esc(f.get('site', 'coachwibawa.com'))}</div></div>"
             f"<div style='position:absolute;right:96px;top:56px'>{lockup('horizontal', fam['logo'], 250)}</div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative'>{inner}</div>", False

def t_highlight_cover(f):
    """Instagram Story highlight cover. Only the centre circle shows, so the mark sits there."""
    fam = FAM[f.get('family', 'blue')]
    W, H = 1080, 1920
    key = f.get('mark')
    icon = offer_mark(key, fam['acc'], 300) if key else mark(fam['logo'], 300)
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};display:flex;align-items:center;justify-content:center'>{icon}</div>", False

def t_youtube_thumb(f):
    fam = FAM[f.get('family', 'blue')]
    W, H = 1280, 720
    photo = ''
    if f.get('photo'):
        photo = f"<div style='position:absolute;right:0;top:0;bottom:0;width:560px;background:url({pathlib.Path(f['photo']).resolve().as_uri()}) center/cover'></div>"
    inner = (photo + f"<div style='position:absolute;left:64px;top:64px;bottom:64px;width:{'620' if f.get('photo') else '1150'}px;display:flex;flex-direction:column;justify-content:center;gap:20px'>"
             f"<div style='font-family:M;font-weight:600;font-size:24px;letter-spacing:.12em;text-transform:uppercase;color:{fam['acc']}'>{esc(f.get('eyebrow'))}</div>"
             f"<div style='font-family:M;font-weight:800;font-size:76px;line-height:84px;color:{fam['head']}'>{hl(f.get('headline'), fam['acc'])}</div></div>"
             f"<div style='position:absolute;left:64px;bottom:48px'>{mark(fam['logo'], 52)}</div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative;overflow:hidden'>{inner}</div>", False

def t_podcast_cover(f):
    """Podcast cover art. Rendered at 1500 and upscaled is not allowed: platforms want 3000x3000, so render at 3000."""
    fam = FAM[f.get('family', 'blue')]
    W = H = 3000
    key = f.get('mark', 'iti')
    inner = (f"<div style='position:absolute;inset:240px;display:flex;flex-direction:column;justify-content:space-between'>"
             f"{offer_mark(key, fam['acc'], 520)}"
             f"<div style='font-family:M;font-weight:800;font-size:300px;line-height:310px;color:{fam['head']}'>{esc(f.get('title', 'Inside The Introvert'))}</div>"
             f"<div style='display:flex;justify-content:space-between;align-items:flex-end'><div style='font-family:M;font-size:96px;color:{fam['fg']}'>{esc(f.get('host', 'with Genison Wibawa'))}</div>{mark(fam['logo'], 240)}</div></div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative'>{inner}</div>", False

def t_newsletter_header(f):
    fam = FAM[f.get('family', 'blue')]
    W, H = 1200, 360
    series = f.get('series', 'Inside The Introvert')
    key = 'lcl' if 'Letters' in series else 'iti'
    inner = (f"<div style='position:absolute;inset:0 72px;display:flex;align-items:center;justify-content:space-between'>"
             f"<div style='display:flex;align-items:center;gap:28px'>{offer_mark(key, fam['acc'], 96)}<div><div style='font-family:M;font-weight:700;font-size:52px;color:{fam['head']}'>{esc(series)}</div>"
             f"<div style='font-family:M;font-size:26px;color:{fam['fg']};margin-top:8px'>{esc(f.get('edition', ''))}</div></div></div>{lockup('horizontal', fam['logo'], 300)}</div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative'>{inner}</div>", False

A4_PORTRAIT, A4_LANDSCAPE = (794, 1123), (1123, 794)   # px at 96 dpi = 210 x 297 mm

def t_certificate(f):
    """A4 landscape certificate for paid programs (gold family by default, paid program documents)."""
    fam = FAM[f.get('family', 'gold-light')]
    W, H = A4_LANDSCAPE
    # Added 3 Nov 2026: optional signature image (transparent PNG) sits on the signature line, right side.
    sig = (f"<img src='{pathlib.Path(f['signature']).resolve().as_uri()}' style='display:block;height:96px;margin:0 24px -14px auto'>"
           if f.get('signature') else "")
    inner = (f"<div style='position:absolute;inset:38px;border:2px solid {fam['acc']}'></div>"
             f"<div style='position:absolute;inset:46px;border:1px solid {fam['acc']};opacity:.5'></div>"
             f"<div style='position:absolute;inset:90px 110px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:14px'>"
             f"{lockup('horizontal', fam['logo'], 230)}"
             f"<div style='font-family:M;font-weight:600;font-size:14px;letter-spacing:.2em;text-transform:uppercase;color:{fam['acc']};margin-top:26px'>Certificate of completion</div>"
             f"<div style='font-family:B;font-size:46px;line-height:58px;color:{fam['head']};margin-top:6px'>{esc(f.get('name', 'Participant Name'))}</div>"
             f"<div style='font-family:B;font-size:16px;line-height:26px;color:{fam['fg']};max-width:620px'>has completed the <b>{esc(f.get('program', '90-Day Lifetime Change'))}</b>, a coaching program built on the 5&nbsp;Laws of Lasting Change.</div>"
             f"<div style='display:flex;justify-content:space-between;align-items:flex-end;width:100%;margin-top:auto;font-family:M;font-size:13px;color:{fam['fg']}'>"
             f"<div style='text-align:left'><div style='border-top:1px solid {fam['fg']};padding-top:8px;width:240px'>{esc(f.get('date', ''))}<br>Date</div></div>"
             f"<div style='text-align:right'>{sig}<div style='border-top:1px solid {fam['fg']};padding-top:8px;width:280px'>Genison Wibawa<br>ICF Associate Certified Coach (ACC)</div></div></div></div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative'>{inner}</div>", False

def t_speaker_kit(f):
    """A4 portrait one-pager for event organisers: photo, bio, talks, proof, contact."""
    fam = FAM[f.get('family', 'blue')]
    W, H = A4_PORTRAIT
    line = TITLE_LINE.get(f.get('audience', 'casual'))
    photo = (f"<div style='width:250px;height:330px;flex:none;background:url({pathlib.Path(f['photo']).resolve().as_uri()}) 50% 35%/cover'></div>"
             if f.get('photo') else f"<div style='width:250px;height:330px;flex:none;background:{C['deep']};display:flex;align-items:center;justify-content:center'>{mark(fam['logo'], 120)}</div>")
    talks = ''.join(f"<div style='padding:12px 0;border-top:1px solid rgba(114,204,208,.25)'><div style='font-family:M;font-weight:700;font-size:15px;color:{fam['head']}'>{esc(t.get('title'))}</div><div style='font-family:B;font-size:12.5px;line-height:19px;color:{fam['fg']};margin-top:4px'>{esc(t.get('desc'))}</div></div>" for t in f.get('talks', []))
    proof = ''.join(f"<div style='flex:1;border-top:3px solid {fam['acc']};padding-top:8px'><div style='font-family:M;font-weight:700;font-size:22px;color:{fam['head']}'>{esc(a)}</div><div style='font-family:M;font-size:11px;color:{fam['fg']};opacity:.8'>{esc(b)}</div></div>" for a, b in f.get('proof', []))
    inner = (f"<div style='position:absolute;inset:48px 52px;display:flex;flex-direction:column;gap:22px'>"
             f"<div style='display:flex;justify-content:space-between;align-items:center'>{lockup('horizontal', fam['logo'], 190)}<div style='font-family:M;font-weight:600;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:{fam['acc']}'>Speaker kit</div></div>"
             f"<div style='display:flex;gap:26px'>{photo}<div style='display:flex;flex-direction:column;gap:10px'>"
             f"<div style='font-family:M;font-weight:700;font-size:30px;color:{fam['head']}'>Genison Wibawa</div><div style='font-family:M;font-size:14px;color:{fam['acc']}'>{line}</div>"
             f"<div style='font-family:B;font-size:13px;line-height:21px;color:{fam['fg']}'>{esc(f.get('bio'))}</div></div></div>"
             f"<div style='display:flex;gap:18px'>{proof}</div>"
             f"<div><div style='font-family:M;font-weight:600;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:{fam['acc']};margin-bottom:4px'>Talks and workshops</div>{talks}</div>"
             f"<div style='margin-top:auto;display:flex;justify-content:space-between;font-family:M;font-size:12px;color:{fam['fg']};border-top:1px solid rgba(114,204,208,.25);padding-top:12px'>"
             f"<div>{esc(f.get('formats', ''))}</div><div>{esc(f.get('contact', 'coachwibawa.com · @coachgenofficial'))}</div></div></div>")
    return W, H, f"<div style='width:{W}px;height:{H}px;background:{fam['bg']};position:relative'>{inner}</div>", False

def t_qr(f):
    """QR code in brand colors, square modules, optional mark in the centre (high error correction)."""
    import qrcode
    # Scanners need dark modules on a light background, so dark families switch to their light twin.
    fam = FAM[{'blue': 'blue-light', 'gold': 'gold-light'}.get(f.get('family', 'blue-light'), f.get('family', 'blue-light'))]
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=4)
    q.add_data(f.get('url', 'https://coachwibawa.com')); q.make(fit=True)
    m = q.get_matrix(); n = len(m)
    W = H = 1080
    s = W / n
    dark = C['abyss'] if fam['bg'] == C['mist'] else C['charcoal']
    rects = ''.join(f"<rect x='{x*s:.2f}' y='{y*s:.2f}' width='{s+0.6:.2f}' height='{s+0.6:.2f}'/>" for y in range(n) for x in range(n) if m[y][x])
    centre = ''
    if f.get('with_mark', True):
        c = W * 0.15
        centre = (f"<rect x='{(W-c)/2-s*0.6:.1f}' y='{(H-c)/2-s*0.6:.1f}' width='{c+1.2*s:.1f}' height='{c+1.2*s:.1f}' fill='{fam['bg']}'/>"
                  f"<svg x='{(W-c)/2:.1f}' y='{(H-c)/2:.1f}' width='{c:.1f}' height='{c:.1f}' viewBox='0 0 256 256'><path fill-rule='evenodd' fill='{dark}' d='{MARK_D}'/></svg>")
    svg = f"<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}'><rect width='{W}' height='{H}' fill='{fam['bg']}'/><g fill='{dark}'>{rects}</g>{centre}</svg>"
    return W, H, svg, False

PDF_TEMPLATES = {'certificate': ('297mm', '210mm'), 'speaker_kit': ('210mm', '297mm')}

TEMPLATES = {
    'certificate': ('A4 landscape certificate (PNG, or PDF for print). fields: name, program, date, signature? (transparent PNG path), family (gold-light)', t_certificate),
    'speaker_kit': ('A4 speaker one-pager (PNG, or PDF for print). fields: bio, talks [{title, desc}], proof [[big, small]], formats, contact, photo?, audience, family', t_speaker_kit),
    'qr': ('1080 QR code with the mark in the centre. fields: url, family (blue-light), with_mark (true)', t_qr),
    'video_bg': ('1920x1080 Zoom, Google Meet, and Teams background. fields: family, show_name (true), audience', t_video_bg),
    'linkedin_banner': ('1584x396 LinkedIn personal banner. fields: promise?, audience (corporate), site?, family', t_linkedin_banner),
    'highlight_cover': ('1080x1920 Instagram Story highlight cover. fields: mark? (offer mark, or the logo mark), family', t_highlight_cover),
    'youtube_thumb': ('1280x720 YouTube thumbnail. fields: eyebrow, headline (==word==), photo?, family', t_youtube_thumb),
    'podcast_cover': ('3000x3000 podcast cover. fields: title, host, mark, family', t_podcast_cover),
    'newsletter_header': ('1200x360 email newsletter header (shown at 600 wide). fields: series, edition, family', t_newsletter_header),
    'carousel': ('4:5 carousel or LinkedIn PDF. fields: mode teach|thought|author, family?, slides:[{kind cover|body|end, eyebrow, title, body, cta, handle}]', None),
    'quote': ('4:5 quote card. fields: quote, name, role?, family', t_quote),
    'reel_title': ('9:16 title card for full talks. fields: eyebrow, title, family', t_reel_title),
    'lower_third': ('9:16 transparent overlay. fields: name?, audience casual|corporate|individual, family', t_lower_third),
    'end_card': ('9:16 end card. fields: cta, handle?, audience?, family', t_end_card),
    'ad': ('Ad in 9x16, 4x5 or 1x1 (size, or "all"). fields: eyebrow, headline (==word== highlights), cta, audience, photo?, family', t_ad),
    'offer_card': ('720x1080 offer card. fields: mark 5laws|6c|ila|eoi|iti|lcl, name?, promise, who, tag?, cta?, photo?, family', t_offer_card),
    'article_header': ('1200x628 article header and share image. fields: series, title, date, family (blue for Inside The Introvert, gold for Letters)', t_article_header),
    'wa_icon': ('1080 WhatsApp group icon. fields: family', t_wa_icon),
    'offer_mark': ('512 offer mark PNG. fields: mark, family or color, transparent?', t_offer_mark),
}

# ---------------------------------------------------------------- render
def _page_html(inner):
    return f"<html><head><style>{fonts_css()}*{{margin:0;padding:0;box-sizing:border-box}}body{{background:transparent}}</style></head><body><div id='r' style='display:inline-block'>{inner}</div></body></html>"

def render(name, fields, out):
    from playwright.sync_api import sync_playwright
    out = pathlib.Path(out).resolve(); out.parent.mkdir(parents=True, exist_ok=True)
    jobs = []
    if name == 'carousel':
        slides = fields.get('slides', [])
        for i, s in enumerate(slides, 1):
            jobs.append((t_carousel_slide({**fields, **s}, i, len(slides)), out.with_name(f"{out.stem}_{i:02d}.png")))
    elif name == 'ad' and fields.get('size') == 'all':
        for sz in AD_SIZES:
            jobs.append((t_ad({**fields, 'size': sz}), out.with_name(f"{out.stem}_{sz}.png")))
    else:
        jobs.append((TEMPLATES[name][1](fields), out))
    made = []
    if name in PDF_TEMPLATES and out.suffix == '.pdf':
        from playwright.sync_api import sync_playwright as _sp
        (W, H, inner, transparent), path = jobs[0]
        with _sp() as p:
            b = p.chromium.launch(); pg = b.new_page()
            tmp = path.with_suffix('.html'); tmp.write_text(_page_html(inner).replace("<style>", "<style>@page{margin:0}", 1))
            pg.goto(tmp.as_uri()); pg.wait_for_timeout(300)
            pw, ph = PDF_TEMPLATES[name]
            pg.pdf(path=str(path), width=pw, height=ph, print_background=True, margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'})
            tmp.unlink(); b.close()
        return [path]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        for (W, H, inner, transparent), path in jobs:
            pg.set_viewport_size({'width': W, 'height': H})
            tmp = path.with_suffix('.html'); tmp.write_text(_page_html(inner))
            pg.goto(tmp.as_uri()); pg.wait_for_timeout(200)
            pg.locator('#r').screenshot(path=str(path), omit_background=transparent)
            tmp.unlink(); made.append(path)
        b.close()
    if name == 'carousel' and out.suffix == '.pdf':
        from PIL import Image
        ims = [Image.open(m).convert('RGB') for m in made]
        ims[0].save(out, save_all=True, append_images=ims[1:], resolution=144)
        made.append(out)
    return made

EXAMPLES = {
    'carousel_teach': ('carousel', {'mode': 'teach', 'slides': [
        {'kind': 'cover', 'eyebrow': 'Law 3 · Resolve Present Friction', 'title': '3 reasons you restart every Monday'},
        {'kind': 'body', 'title': 'You plan for the person you want to be', 'body': 'Placeholder body copy, up to 30 words, one idea per slide.'},
        {'kind': 'end', 'title': 'Find the Law that keeps you restarting.', 'cta': 'TAKE THE FREE DIAGNOSTIC'}]}),
    'carousel_thought': ('carousel', {'mode': 'thought', 'slides': [
        {'kind': 'cover', 'eyebrow': 'Inside The Introvert', 'title': 'You do not fail to make lasting change. You succeed at staying who you are.'}]}),
    'carousel_author': ('carousel', {'mode': 'author', 'slides': [
        {'kind': 'cover', 'eyebrow': 'Lasting Change Letters', 'title': 'If you keep trying, but never finish, this is why.'}]}),
    'quote_blue': ('quote', {'quote': 'Placeholder client quote, real clients with permission only, up to 30 words.', 'name': 'Client name', 'role': 'Role, City', 'family': 'blue'}),
    'quote_gold': ('quote', {'quote': 'You do not fail to make lasting change. You succeed at staying who you are.', 'name': 'Genison Wibawa', 'role': '5 Laws of Lasting Change', 'family': 'gold'}),
    'reel_title': ('reel_title', {'eyebrow': 'Toastmasters talk', 'title': 'Why you keep restarting', 'family': 'blue'}),
    'lower_third_casual': ('lower_third', {'audience': 'casual'}),
    'lower_third_corporate': ('lower_third', {'audience': 'corporate'}),
    'lower_third_individual': ('lower_third', {'audience': 'individual'}),
    'end_card_blue': ('end_card', {'cta': 'TAKE THE 5 LAWS DIAGNOSTIC', 'family': 'blue'}),
    'end_card_gold': ('end_card', {'cta': 'READ THE FIRST CHAPTER', 'family': 'gold'}),
    'ad': ('ad', {'size': 'all', 'eyebrow': 'Free diagnostic', 'headline': 'Keep trying but never ==finish==?', 'cta': 'FIND YOUR LAW', 'audience': 'individual', 'family': 'blue'}),
    'offer_card_5laws': ('offer_card', {'mark': '5laws', 'tag': 'START HERE', 'promise': 'Placeholder promise for the offer.', 'who': 'Placeholder audience', 'cta': 'TAKE IT FREE'}),
    'offer_card_lcl': ('offer_card', {'mark': 'lcl', 'tag': 'AUTHOR', 'promise': 'Placeholder promise for the Letters.', 'who': 'For readers', 'family': 'gold'}),
    'article_header_iti': ('article_header', {'series': 'Inside The Introvert', 'title': 'How can you be busy but lazy?', 'date': 'October 12, 2026', 'family': 'blue'}),
    'article_header_lcl': ('article_header', {'series': 'Lasting Change Letters', 'title': 'Never Split the Difference', 'date': 'Edition 1, September 2026', 'family': 'gold'}),
    'wa_icon': ('wa_icon', {'family': 'blue'}),
    'video_bg_blue': ('video_bg', {'family': 'blue', 'audience': 'casual'}),
    'video_bg_light_corporate': ('video_bg', {'family': 'blue-light', 'audience': 'corporate'}),
    'video_bg_gold_plain': ('video_bg', {'family': 'gold', 'show_name': False}),
    'linkedin_banner': ('linkedin_banner', {'family': 'blue'}),
    'highlight_cover_6c': ('highlight_cover', {'mark': '6c', 'family': 'blue'}),
    'youtube_thumb': ('youtube_thumb', {'eyebrow': 'Law 1 · Reset My Course', 'headline': 'Why you ==never== finish', 'family': 'blue'}),
    'podcast_cover': ('podcast_cover', {'title': 'Inside The Introvert', 'host': 'with Genison Wibawa', 'mark': 'iti', 'family': 'blue'}),
    'certificate': ('certificate', {'name': 'Participant Name', 'program': '90-Day Lifetime Change', 'date': '30 October 2026'}),
    'qr_site': ('qr', {'url': 'https://coachwibawa.com', 'family': 'blue-light'}),
    'speaker_kit': ('speaker_kit', {'bio': 'Genison Wibawa, known as Coach Gen, helps people who keep trying, but never finish. He is an ICF Associate Certified Coach and the creator of the 5 Laws of Lasting Change, a coaching system built from hundreds of hours with people in Indonesia, Malaysia, Singapore, Japan, and America. Before coaching, he worked in engineering in Jakarta and Singapore, where he watched brilliant people go unheard. Today he coaches in English, Indonesian, and Japanese, writes Inside The Introvert and Lasting Change Letters, and is writing his first book, 5 Laws of Lasting Change.',
        'talks': [{'title': 'Why you keep restarting: the 5 Laws of Lasting Change', 'desc': 'For any audience. Why change fades after the first push, and the 5 Laws that make it last.'},
                  {'title': 'Speak with structure, not performance', 'desc': 'For teams that present. The 6C of Public Speaking for analytical minds.'},
                  {'title': 'Use the way you think: introverts at work', 'desc': 'For introverts and their leaders. Introversion Leverage in meetings, pitches, and promotions.'},
                  {'title': 'Get your ideas heard: influence for engineers', 'desc': 'For technical teams. How to move the people who decide.'}],
        'proof': [['ICF ACC', 'Associate Certified Coach'], ['Hundreds', 'of coaching hours'], ['5', 'countries'], ['3', 'coaching languages']],
        'formats': 'Keynote · Workshop · Fireside chat · English, Indonesian, Japanese',
        'contact': 'coachwibawa.com · @coachgenofficial'}),
    'newsletter_header_lcl': ('newsletter_header', {'series': 'Lasting Change Letters', 'edition': 'Edition 2', 'family': 'gold'}),
}

def main(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__); return
    if argv[0] == '--list':
        for k, (d, _) in TEMPLATES.items():
            print(f"{k:16} {d}")
        return
    if argv[0] == '--examples':
        outdir = pathlib.Path(argv[1] if len(argv) > 1 else 'examples')
        for k, (name, fields) in EXAMPLES.items():
            for m in render(name, fields, outdir / f"{k}.png"):
                print('made', m)
        return
    name, fjson, out = argv[0], argv[1], argv[2]
    fields = json.loads(pathlib.Path(fjson).read_text()) if os.path.exists(fjson) else json.loads(fjson)
    for m in render(name, fields, out):
        print('made', m)

if __name__ == '__main__':
    main(sys.argv[1:])
