"""Universal book parser: PDF -> turns.json for tools/build_load.py.

Two stages.
  python3 tools/parse_book.py book.pdf --profile
      Prints a page map, a style table (font + size, with sample lines), header/footer
      candidates and the contents page. No settings needed. Read it, then write books/<name>.json.
  python3 tools/parse_book.py book.pdf books/<name>.json turns.json
      Parses with the settings, writes turns.json and prints the checks and the pages to look at.

Roles come from the font and size of each line, not from spaces. Settings keys (all optional except
keep_pages and styles) are listed in books/README.md and in Universal_Parser_Plan.md.
turns.json shape: [{"s": PDF page, "t": text, "ch": chapter, "sec": section, "k": kind, "sp": speaker?}]
"""
import json, re, sys, collections, hashlib
import pdfplumber

SPACE_GAP = 0.25  # gap (in font sizes) that counts as a space when the PDF has no space char


def parse_ranges(s, n):
    out = set()
    for part in str(s).split(','):
        part = part.strip()
        if not part: continue
        if '-' in part:
            a, b = part.split('-'); out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return {p for p in out if 1 <= p <= n}


def style_key(font, size):
    return f"{re.sub(r'^[A-Z]{6}\+', '', font)} {size:.1f}"


def read_lines(page):
    """Group characters into lines. Returns list of dicts with text, x0, x1, top, bottom, size, style."""
    chars = [c for c in page.chars]
    if not chars: return []
    chars.sort(key=lambda c: (round(c['top'], 0), c['x0']))
    groups, cur = [], []
    for c in sorted(chars, key=lambda c: c['top']):
        if cur and abs(c['top'] - cur[0]['top']) > 0.45 * max(c['size'], cur[0]['size']):
            groups.append(cur); cur = []
        cur.append(c)
    if cur: groups.append(cur)
    lines = []
    for g in groups:
        g.sort(key=lambda c: c['x0'])
        text, prev = '', None
        for c in g:
            ch = c['text']
            if ch in ('\t', '\xa0'): ch = ' '
            if prev is not None and ch != ' ' and not text.endswith(' ') and c['x0'] - prev['x1'] > SPACE_GAP * c['size']:
                text += ' '
            text += ch; prev = c
        text = re.sub(r'\s+', ' ', text).strip()
        if not text: continue
        vis = [c for c in g if c['text'].strip()]
        dom = collections.Counter(style_key(c['fontname'], c['size']) for c in vis).most_common(1)[0][0]
        lines.append({'text': text, 'x0': min(c['x0'] for c in vis), 'x1': max(c['x1'] for c in vis),
                      'top': min(c['top'] for c in g), 'bottom': max(c['bottom'] for c in g),
                      'size': max(c['size'] for c in vis), 'style': dom, 'nchars': len(vis)})
    lines.sort(key=lambda l: (l['top'], l['x0']))
    return lines


def norm_digits(t):
    return re.sub(r'\d+', '#', t)


def find_running(all_lines, npages):
    """Lines in the top or bottom band that repeat on many pages (running headers, footers, page numbers)."""
    cnt = collections.Counter()
    for pno, (lines, h) in all_lines.items():
        seen = set()
        for l in lines:
            if l['top'] < 60 or l['bottom'] > h - 55:
                seen.add(norm_digits(l['text']))
        cnt.update(seen)
    return {t for t, n in cnt.items() if n >= max(5, 0.08 * npages)}


# ---------------------------------------------------------------- profile

def profile(path):
    with pdfplumber.open(path) as pdf:
        n = len(pdf.pages)
        data = {}
        for i, pg in enumerate(pdf.pages, start=1):
            data[i] = (read_lines(pg), pg.height)
    print(f"FILE {path}\nPAGES {n}")
    empty = [p for p, (ls, _) in data.items() if len(ls) == 0]
    if len(empty) > 0.5 * n:
        print("WARNING: most pages have no text. This is a scanned PDF. Needs OCR. Stop."); return
    # page signatures
    sig = {}
    for p, (ls, h) in data.items():
        if len(ls) == 0: sig[p] = 'empty'; continue
        txt = [l['text'] for l in ls]
        endnum = sum(bool(re.search(r'(\d+|\d+[-–]\d+)$', t)) for t in txt) / len(txt)
        startnum = sum(bool(re.match(r'^\d{1,3}[.\s]', t)) for t in txt) / len(txt)
        commas = sum(t.count(',') for t in txt) / len(txt)
        if len(ls) < 10: sig[p] = 'sparse'
        elif endnum > 0.5 and commas > 1: sig[p] = 'index-like'
        elif startnum > 0.35: sig[p] = 'notes-like'
        elif endnum > 0.4 and len(ls) > 15: sig[p] = 'contents-like'
        else: sig[p] = 'text'
    runs, start = [], 1
    for p in range(2, n + 2):
        if p > n or sig[p] != sig[start]:
            runs.append((start, p - 1, sig[start])); start = p
    print("\nPAGE MAP (guess)")
    for a, b, k in runs:
        print(f"  p{a}" + (f"-{b}" if b != a else '') + f"  {k}")
    # style table
    styles = collections.Counter(); samples = collections.defaultdict(list); firstp = {}
    for p, (ls, h) in data.items():
        for l in ls:
            styles[l['style']] += 1
            if len(samples[l['style']]) < 3 and l['text'] not in samples[l['style']]:
                samples[l['style']].append(l['text'][:60])
            firstp.setdefault(l['style'], p)
    print("\nSTYLES (font size, lines, first page, samples). Map the ones you need in settings.styles")
    for k, c in styles.most_common(14):
        print(f"  {k!r}: {c} lines, first p{firstp[k]}, e.g. {samples[k]}")
    # left margin
    x0s = collections.Counter(round(l['x0']) for _, (ls, _) in data.items() for l in ls)
    print("\nLEFT EDGES (x, lines):", x0s.most_common(6))
    # running lines
    run = find_running(data, n)
    print("\nRUNNING HEADER/FOOTER patterns (dropped automatically):", sorted(run)[:8])
    # chapter candidates: sparse or early-in-page non-body lines
    body = styles.most_common(1)[0][0]
    print(f"\nBODY STYLE GUESS: {body!r}")
    print("\nCHAPTER CANDIDATES (page, first lines when the page starts with a non-body style or is sparse)")
    c = 0
    for p, (ls, h) in data.items():
        if not ls: continue
        first = ls[0]
        key = re.match(r'^(chapter|part|introduction|conclusion|appendix|prologue|epilogue|\d{1,2}$|[ivxl]+$)', first['text'], re.I)
        if (first['style'] != body and sig[p] in ('sparse', 'text') and first['top'] > 40 and (key or sig[p] == 'sparse')):
            print(f"  p{p}: {[l['text'][:50] for l in ls[:3]]}"); c += 1
            if c >= 70: print("  ..."); break
    # contents
    cands = sorted(((p, sum(bool(re.search(r'\d+$', l['text'])) for l in ls)) for p, (ls, _) in data.items() if p <= 20 and len(ls) > 8),
                   key=lambda x: -x[1])[:2]
    for p, _ in sorted(cands):
        print(f"\nCONTENTS-LIKE PAGE p{p}")
        for l in data[p][0][:45]: print("  ", l['text'][:90])


# ---------------------------------------------------------------- parse

def parse(path, cfg, out):
    with pdfplumber.open(path) as pdf:
        n = len(pdf.pages)
        data = {i: (read_lines(pg), pg.height) for i, pg in enumerate(pdf.pages, start=1)}
    keep = parse_ranges(cfg['keep_pages'], n) - parse_ranges(','.join(map(str, cfg.get('skip_pages', []))) or '', n)
    styles = cfg['styles']
    chapters = sorted((int(p), lab) for p, lab in cfg.get('chapters', []))
    parts = {int(p) for p in cfg.get('parts', [])}
    drop_re = [re.compile(r) for r in cfg.get('drop_lines', [])]
    speakers = cfg.get('speakers', {})
    chap_re = re.compile(cfg['chapter_line_re']) if cfg.get('chapter_line_re') else None
    running = set() if cfg.get('keep_running') else find_running({p: data[p] for p in keep}, len(keep))
    # margins from body lines
    body_lines = [l for p in keep for l in data[p][0] if styles.get(l['style'], styles.get(re.sub(r'-(Italic|Oblique)', '', l['style']), 'body')) == 'body']
    margin = collections.Counter(round(l['x0']) for l in body_lines).most_common(1)[0][0]
    xr = sorted(l['x1'] for l in body_lines); right = xr[int(0.9 * len(xr))]
    indent = cfg.get('indent', 4)
    frac_ind = sum(l['x0'] > margin + indent for l in body_lines) / max(1, len(body_lines))
    by_indent = cfg.get('paragraph_by', 'auto')
    if by_indent == 'auto': by_indent = 'indent' if 0.03 < frac_ind < 0.45 else 'gap'
    print(f"PARAGRAPH RULE {by_indent} (margin x={margin}, share of indented lines {frac_ind:.0%})")

    def role_of(l):
        s = l['style']
        if s in styles: return styles[s]
        s2 = re.sub(r'-(Italic|Oblique)(?=\s)', '', s)
        if s2 in styles: return styles[s2]
        unmapped[s] += 1
        return 'body'

    unmapped = collections.Counter(); dropped = collections.Counter()
    turns = []; src_chars = []; src_page_end = []  # source text (no whitespace) in order, per page end offset
    cur = None  # current paragraph
    cur_head = None
    chapter = cfg.get('front_label', 'Front'); section = chapter
    chap_idx = 0
    prev_line = None

    def flush():
        nonlocal cur
        if cur and cur['t'].strip():
            cur['t'] = re.sub(r'\s+', ' ', cur['t']).strip(); turns.append(cur)
        cur = None

    def flush_head():
        nonlocal cur_head, section
        if cur_head:
            t = re.sub(r'\s+', ' ', cur_head['t']).strip(); cur_head['t'] = t
            section = t; cur_head['sec'] = t; turns.append(cur_head)
        cur_head = None

    def add_text(t, pno, kind, new):
        nonlocal cur
        if new or cur is None:
            flush(); cur = {'s': pno, 't': t, 'ch': chapter, 'sec': section, 'k': kind}; return
        prev = cur['t']
        if (prev.endswith('-') and not prev.endswith(' -')) or prev.endswith('—') or t.startswith('—'):
            cur['t'] = prev + t
        else:
            cur['t'] = prev + ' ' + t

    list_re = re.compile(r'^(\d+(\.\d+)?[.:)] |[•▪◦] |[—–-] )')
    for pno in sorted(keep):
        while chap_idx < len(chapters) and chapters[chap_idx][0] <= pno:
            if chapters[chap_idx][0] == pno:
                flush(); flush_head(); chapter = chapters[chap_idx][1]; section = chapter
            chap_idx += 1
        lines, h = data[pno]
        kept = []
        for l in lines:
            if norm_digits(l['text']) in running or any(r.search(l['text']) for r in drop_re) or role_of(l) == 'skip':
                dropped[norm_digits(l['text'])[:40]] += 1; continue
            kept.append(l)
        is_chapter_page = any(c[0] == pno for c in chapters)
        if pno in parts:
            flush(); flush_head()
            t = ' '.join(l['text'] for l in kept)
            src_chars.append(re.sub(r'\s', '', t))
            if t: turns.append({'s': pno, 't': t, 'ch': chapter, 'sec': t, 'k': 'part'}); section = t
            src_page_end.append((pno, sum(map(len, src_chars)))); continue
        lead = is_chapter_page
        if is_chapter_page or pno in parts: prev_line = None
        for l in kept:
            role = role_of(l); t = l['text']
            src_chars.append(re.sub(r'\s', '', t))
            if lead and (role in ('chapter', 'part') or (chap_re and chap_re.match(t))):
                # chapter title lines at the top of a chapter page: one heading turn
                if cur_head is None: cur_head = {'s': pno, 't': t, 'ch': chapter, 'sec': chapter, 'k': 'chapter'}
                else: cur_head['t'] += ' ' + t
                prev_line = l; continue
            if lead and role == 'body' and not (chap_re and chap_re.match(t)): flush_head(); lead = False
            if role in ('heading', 'chapter', 'part'):
                gap = (l['top'] - prev_line['bottom']) if prev_line else 99
                if cur_head is not None and prev_line is not None and prev_line.get('_head') and gap < 1.0 * l['size']:
                    cur_head['t'] += ' ' + t
                else:
                    flush(); flush_head()
                    cur_head = {'s': pno, 't': t, 'ch': chapter, 'sec': section, 'k': 'heading'}
                l['_head'] = True; prev_line = l; continue
            if cur_head is not None: flush_head()
            if role == 'figure':
                gap = (l['top'] - prev_line['bottom']) if prev_line else 99
                if cur and cur['k'] == 'figure' and gap < 1.2 * l['size']: add_text(t, pno, 'figure', False)
                else: add_text(t, pno, 'figure', True)
                prev_line = l; continue
            # body line: decide new paragraph
            new = False
            if cur is None or cur['k'] != 'body': new = True
            elif prev_line is not None:
                gap = l['top'] - prev_line['bottom']
                was_indented = prev_line['x0'] > margin + indent
                is_indented = l['x0'] > margin + indent
                short_prev = prev_line['x1'] < right - 0.12 * (h * 0.6) and re.search(r'[.!?:"”’)]$', cur['t'])
                if gap > 0.6 * l['size'] or (is_indented and not was_indented and gap >= 0) or (short_prev and gap >= -2 and by_indent == 'gap') or list_re.match(t): new = True
                if pno != cur['s'] and prev_line.get('_page') != pno: new = new  # page break: continue unless a rule above fired
            elif list_re.match(t): new = True
            # drop cap: a single large letter on its own line glues to the next line
            if prev_line is not None and prev_line.get('_dropcap'):
                cur['t'] += t if not cur['t'].endswith(' ') else t; l['_page'] = pno; prev_line = l; continue
            if len(t) == 1 and t.isalpha() and l['size'] > 1.25 * (body_lines[0]['size'] if body_lines else 12):
                add_text(t, pno, 'body', True); l['_dropcap'] = True; l['_page'] = pno; prev_line = l; continue
            if any(t.startswith(pre) for pre in speakers): new = True
            add_text(t, pno, 'body', new); l['_page'] = pno; prev_line = l
        flush_head()
        src_page_end.append((pno, sum(map(len, src_chars))))
    flush(); flush_head()
    # drop cap + small caps fixes, speakers
    for t in turns:
        t['t'] = re.sub(r'^([A-Z]) (?=[A-Z]{2})', r'\1', t['t']) if t['k'] == 'body' else t['t']
        for pre, name in speakers.items():
            if t['t'].startswith(pre): t['t'] = t['t'][len(pre):].strip(); t['sp'] = name; break
    # part turns take the next chapter's label so no tiny documents appear
    for i, t in enumerate(turns):
        if t['k'] == 'part':
            nxt = next((u['ch'] for u in turns[i + 1:] if u['k'] != 'part'), t['ch']); t['ch'] = nxt
    json.dump(turns, open(out, 'w'), ensure_ascii=False)
    report(turns, src_chars, src_page_end, cfg, unmapped, dropped, speakers)


def report(turns, src_chars, src_page_end, cfg, unmapped, dropped, speakers):
    src = ''.join(src_chars)
    tt = ''.join(re.sub(r'\s', '', t['t']) for t in turns)
    if speakers:  # labels are stripped from turns, strip them from the source count too
        for pre in speakers: src = src.replace(re.sub(r'\s', '', pre), '')
    bad_pages = set()
    ok = src == tt
    if not ok:
        i = next((k for k in range(min(len(src), len(tt))) if src[k] != tt[k]), min(len(src), len(tt)))
        pg = next((p for p, end in src_page_end if end > i), src_page_end[-1][0])
        bad_pages.add(pg)
    print(f"\nTURNS {len(turns)}  WORDS {sum(len(t['t'].split()) for t in turns)}  CHARS {len(tt)}")
    print(f"NO TEXT LOST: {'OK' if ok else 'FAIL'}  source {len(src)} vs turns {len(tt)}" + ('' if ok else f"  first difference near p{sorted(bad_pages)}"))
    if unmapped: print("UNMAPPED STYLES (treated as body):", dict(unmapped.most_common(5)))
    print("DROPPED lines (running headers, skips):", sum(dropped.values()), dict(dropped.most_common(5)))
    kinds = collections.Counter(t['k'] for t in turns); print("KINDS", dict(kinds))
    heads = [t for t in turns if t['k'] in ('heading', 'chapter', 'part')]
    print(f"\nHEADINGS {len(heads)}")
    flags = []
    for t in heads:
        w = len(t['t'].split())
        if w > 12 or t['t'].endswith('.') or t['t'][:1].islower(): flags.append(('head', t))
    paras = [t for t in turns if t['k'] == 'body']
    for t in paras:
        w = len(t['t'].split())
        if w > 400 or t['t'][:1].islower() or (w < 4 and not speakers): flags.append(('para', t))
    print(f"FLAGS {len(flags)}")
    for kind, t in flags[:25]:
        print(f"  [{kind}] p{t['s']} {len(t['t'].split())}w: {t['t'][:70]!r}")
    chs = collections.Counter(t['ch'] for t in turns)
    print("\nCHAPTERS", len(chs), "smallest:", chs.most_common()[-3:])
    look = sorted(bad_pages | {t['s'] for _, t in flags})
    print("\nPAGES TO LOOK AT:", look[:40], '...' if len(look) > 40 else '')
    print("all_md5", hashlib.md5('\n'.join(t['t'] for t in turns).encode()).hexdigest())


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[2] == '--profile':
        profile(sys.argv[1])
    elif len(sys.argv) == 4:
        parse(sys.argv[1], json.load(open(sys.argv[2])), sys.argv[3])
    else:
        print(__doc__)
