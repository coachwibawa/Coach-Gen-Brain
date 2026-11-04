#!/usr/bin/env python3
"""Coach Gen video build pipeline (v1, 31 Oct 2026).

Usage:  python3 build.py SPEC.json            render missing segments (stops at ~140 s), then finish
        python3 build.py SPEC.json sheet      frame sheet of key moments (jpg in work dir)
        python3 build.py SPEC.json check      caption stats only

Spec (JSON):
  name, src (cut video), out (final mp4), work (scratch dir, no spaces),
  family: blue|gold (pick from what Gen wears in the first frame: cool clothes blue, warm clothes gold),
  mark: corner mark png, title_card: {eyebrow, title, mark_png} (optional, 3 s, shifts video by +3 s),
  heading: {lines:[...], start, end}  (style D: big white text, *word* in accent, short accent rule),
  lower_third: {start, dur, name, line} (optional),
  captions: [[start, end, "TEXT with *highlight*"], ...]  times are FINAL output times.
  cap_fx: subtle (default, fade in 0.08 s) | pop | bounce | slide | bounce_hl | none. Gen 1 Nov 2026: very subtle; bounce, slide and bounce_hl felt excessive.
  voice: none | radio | radio_deep.  cover_t: frame time for the grid cover (build.py SPEC cover).
"""
import json, sys, os, re, subprocess, time, math, glob

FONTS = os.environ.get('CG_FONTS', os.path.expanduser('~/cgfonts'))
BUDGET = float(os.environ.get('CG_BUDGET', 120))  # seconds per call before stopping (Mac shell limit ~175 s)
FAM = {
    'blue': {'acc': '72CCD0', 'plate': '01131C', 'head': 'EAF5F6', 'text': 'FFFFFF'},
    'gold': {'acc': 'C8B796', 'plate': '2B2B2B', 'head': 'F6F2EA', 'text': 'F6F2EA'},
}
W, H, FPS, SEG = 1080, 1920, 30, 30
RADIO = 'highpass=f=70,bass=g=4:f=120,equalizer=f=300:t=q:w=1:g=-2,equalizer=f=3500:t=q:w=1.2:g=2,deesser,acompressor=threshold=-20dB:ratio=3:attack=5:release=80:makeup=2'  # voice: none | radio | radio_deep (Gen picked radio_deep in a blind test, 1 Nov 2026)
CAP_Y = 1152          # caption centre line, 60% of height
ONE_LINE = 24         # max caption characters on one line at full size (Sinek style: always one line)
SMALL = set('A AN THE TO OF AND OR BUT IS ARE WAS IN ON AT FOR WITH YOUR MY OUR I IT THAT THIS AS SO IF BY FROM'.split())


def bgr(hexrgb):
    return (hexrgb[4:6] + hexrgb[2:4] + hexrgb[0:2]).upper()


def col(hexrgb, alpha='00'):
    return f'&H{alpha}{bgr(hexrgb)}'


def ts(t):
    t = max(0, t)
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'


def hl(text, acc, base='FFFFFF'):
    return re.sub(r'\*([^*]+)\*', lambda m: '{\\c&H' + bgr(acc) + '&}' + m.group(1) + '{\\c&H' + bgr(base) + '&}', text)


def plain(text):
    return text.replace('*', '')


def ass_header(fam):
    f = FAM[fam]
    return f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat ExtraBold,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,6,0,5,75,75,0,1
Style: Head,Montserrat Black,96,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,6,0,5,60,60,0,1
Style: Box,Montserrat,10,{col(f['acc'])},&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: LName,Montserrat,60,{col(f['head'])},&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: LLine,Montserrat,42,{col(f['text'])},&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: TEye,Montserrat SemiBold,44,{col(f['acc'])},&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,6,0,1,0,0,5,0,0,0,1
Style: TTitle,Montserrat,96,{col(f['head'])},&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def rect(x, y, w, h, color, alpha='00', layer=0, t0=0, t1=0, fade=''):
    return (f"Dialogue: {layer},{ts(t0)},{ts(t1)},Box,,0,0,0,,{{\\an7\\pos({x},{y})\\bord0\\shad0"
            f"\\1c&H{bgr(color)}&\\1a&H{alpha}&{fade}\\p1}}m 0 0 l {w} 0 {w} {h} 0 {h}{{\\p0}}")


BOUNCE = r'\fscx70\fscy70\t(0,100,\fscx105\fscy105)\t(100,150,\fscx100\fscy100)'
BIGHL = r'\fscx74\fscy74\t(0,100,\fscx116\fscy116)\t(100,150,\fscx110\fscy110)'


def cap_line(s, e, text, acc, fx):
    """Caption entrance/exit effects. pop: 85->100% in 0.1 s. bounce: 70->105->100% in 0.15 s, fade out 0.06 s.
    slide: rise 15 px and fade in over 0.1 s, fade out 0.06 s. bounce_hl: bounce, highlight word stays 110%. none."""
    pre = f'Dialogue: 1,{ts(s)},{ts(e)},Cap,,0,0,0,,'
    if fx == 'slide':
        return pre + f'{{\\move(540,{CAP_Y + 15},540,{CAP_Y},0,100)\\fad(100,60)}}' + hl(text, acc)
    if fx == 'bounce_hl':
        body = re.sub(r'\*([^*]+)\*', lambda m: '{\\c&H' + bgr(acc) + '&' + BIGHL + '}' + m.group(1) + '{\\c&HFFFFFF&' + BOUNCE + '}', text)
        return pre + f'{{\\pos(540,{CAP_Y})\\fad(0,60){BOUNCE}}}' + body
    tags = {'subtle': r'\fad(80,40)', 'pop': r'\fscx85\fscy85\t(0,100,\fscx100\fscy100)', 'bounce': r'\fad(0,60)' + BOUNCE, 'none': ''}[fx]
    n = len(plain(text))
    if n > ONE_LINE:  # one line only (Gen, 1 Nov 2026): shrink long chunks instead of wrapping
        k = max(80, int(100 * ONE_LINE / n)); tags += f'\\fscx{k}\\fscy{k}'
    return pre + f'{{\\pos(540,{CAP_Y}){tags}}}' + hl(text, acc)


def build_ass(spec):
    fam = spec.get('family', 'blue'); f = FAM[fam]; acc = f['acc']
    out = [ass_header(fam)]
    hd = spec.get('heading')
    if hd:
        t0, t1 = hd['start'], hd['end']; n = len(hd['lines'])
        y0 = 440 if n == 2 else 500
        pop = r'\fad(120,200)\fscx88\fscy88\t(0,160,\fscx100\fscy100)'
        for i, line in enumerate(hd['lines']):
            out.append(f"Dialogue: 2,{ts(t0)},{ts(t1)},Head,,0,0,0,,{{\\pos(540,{y0 + i * 120}){pop}}}{hl(line, acc)}")
        ry = y0 + (n - 1) * 120 + 68
        out.append(f"Dialogue: 2,{ts(t0)},{ts(t1)},Box,,0,0,0,,{{\\an8\\pos(540,{ry})\\bord0\\shad0\\1c&H{bgr(acc)}&\\fad(120,200)\\p1}}m 0 0 l 300 0 300 10 0 10{{\\p0}}")
    lt = spec.get('lower_third')
    if lt:
        t0 = lt['start']; t1 = t0 + lt.get('dur', 4); y = lt.get('y', 300); x = 64; w = lt.get('w', 540); h = 150
        fade = r'\fad(200,200)'
        out.append(rect(x, y, w, h, f['plate'], '26', 3, t0, t1, fade))
        out.append(rect(x, y, 4, h, acc, '00', 4, t0, t1, fade))
        out.append(f"Dialogue: 4,{ts(t0)},{ts(t1)},LName,,0,0,0,,{{\\pos({x + 32},{y + 22}){fade}}}{lt['name']}")
        out.append(f"Dialogue: 4,{ts(t0)},{ts(t1)},LLine,,0,0,0,,{{\\pos({x + 32},{y + 92}){fade}}}{lt['line']}")
    for s, e, text in spec['captions']:
        out.append(cap_line(s, e, text, acc, spec.get('cap_fx', 'subtle')))
    return '\n'.join(out) + '\n'


def title_ass(spec):
    tc = spec['title_card']; fam = spec.get('family', 'blue')
    out = [ass_header(fam)]
    out.append(f"Dialogue: 0,{ts(0)},{ts(3)},TEye,,0,0,0,,{{\\pos(540,922)\\fad(200,0)}}{tc['eyebrow']}")
    out.append(f"Dialogue: 0,{ts(0)},{ts(3)},TTitle,,0,0,0,,{{\\pos(540,1037)\\fad(200,0)}}{tc['title']}")
    return '\n'.join(out) + '\n'


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print('ERR', ' '.join(cmd)[:300], r.stderr[-800:]); sys.exit(1)
    return r.stdout


def probe(src):
    o = run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_packets', '-show_entries',
             'stream=nb_read_packets:format=duration', '-of', 'json', src])
    j = json.loads(o)
    return int(j['streams'][0]['nb_read_packets']), float(j['format']['duration'])


def check(spec):
    caps = spec['captions']; n = len(caps); fast = small = 0; mx = 0
    for s, e, t in caps:
        p = plain(t); words = p.split(); mx = max(mx, len(words))
        if len(p) / max(e - s, 0.01) > 20: fast += 1
        if words[-1][-1] not in '.?!' and words[-1].strip(',').upper() in SMALL: small += 1
    hlc = sum(1 for c in caps if '*' in c[2])
    longc = sum(1 for c in caps if len(plain(c[2])) > ONE_LINE)
    print(f"{spec['name']}: {n} chunks, {100*fast/n:.0f}% over 20 cps, {100*small/n:.0f}% end on small word, max {mx} words, {hlc} highlighted, {longc} over {ONE_LINE} chars (shrunk to fit one line, aim for 0)")


def render(spec):
    wd = spec['work']; os.makedirs(wd, exist_ok=True)
    ass = os.path.join(wd, 'subs.ass'); open(ass, 'w').write(build_ass(spec))
    nfr, dur = spec.get('_probe') or probe(spec['src'])
    vstart = 3.0 if spec.get('title_card') else 0.0
    nseg = math.ceil(nfr / (SEG * FPS))
    t_start = time.time()
    if spec.get('title_card') and not os.path.exists(os.path.join(wd, 'seg_tc.mp4')):
        tass = os.path.join(wd, 'title.ass'); open(tass, 'w').write(title_ass(spec))
        plate = FAM[spec.get('family', 'blue')]['plate']
        run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', f'color=c=0x{plate}:s={W}x{H}:r={FPS}:d=3',
             '-loop', '1', '-i', spec['title_card']['mark_png'],
             '-filter_complex', f"[1]scale=160:-1[m];[0][m]overlay=(W-w)/2:730-h/2:shortest=1,ass={tass}:fontsdir={FONTS}[v]",
             '-map', '[v]', '-frames:v', str(3 * FPS), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
             '-pix_fmt', 'yuv420p', os.path.join(wd, 'seg_tc.mp4')])
    for k in range(nseg):
        seg = os.path.join(wd, f'seg_{k:03d}.mp4')
        if os.path.exists(seg):
            continue
        if time.time() - t_start > BUDGET:
            print(f'PARTIAL {k}/{nseg} segments, call again'); return False
        frames = min(SEG * FPS, nfr - k * SEG * FPS)
        off = vstart + k * SEG
        fc = (f"[0:v]setpts=PTS-STARTPTS+{off}/TB[v0];[1]scale=72:-1,format=rgba[m];"
              f"[v0][m]overlay=944:281:shortest=1[v1];[v1]ass={ass}:fontsdir={FONTS},setpts=PTS-STARTPTS[v]")
        run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(k * SEG), '-i', spec['src'], '-loop', '1', '-i', spec['mark'],
             '-filter_complex', fc, '-map', '[v]', '-frames:v', str(frames), '-an', '-c:v', 'libx264', '-preset', 'veryfast',
             '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), seg + '.tmp.mp4'])
        os.rename(seg + '.tmp.mp4', seg)
    # finish: concat video, loudnorm audio
    lst = os.path.join(wd, 'list.txt')
    with open(lst, 'w') as fh:
        if spec.get('title_card'):
            fh.write(f"file '{os.path.join(wd, 'seg_tc.mp4')}'\n")
        for k in range(nseg):
            fh.write(f"file '{os.path.join(wd, f'seg_{k:03d}.mp4')}'\n")
    VOICE = {'none': '', 'radio': RADIO + ',', 'radio_deep': 'rubberband=pitch=0.94387:formant=preserved,' + RADIO + ','}[spec.get('voice', 'none')]
    af = (f"[1:a]{VOICE}adelay={int(vstart*1000)}:all=1," if vstart else f"[1:a]{VOICE}") + "loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    tmp = os.path.join(wd, 'final.mp4')
    run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-i', spec['src'],
         '-filter_complex', af, '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
         '-shortest', '-movflags', '+faststart', tmp])
    run(['cp', tmp, spec['out']])
    print('DONE', spec['out'], f'{time.time() - t_start:.0f}s')
    return True


def sheet(spec, times=None):
    wd = spec['work']
    if not times:
        times = [1.0]
        if spec.get('lower_third'): times.append(spec['lower_third']['start'] + 1.5)
        caps = spec['captions']; times += [ (caps[i][0] + caps[i][1]) / 2 for i in range(0, len(caps), max(1, len(caps) // 6))][:6]
    outs = []
    for i, t in enumerate(times[:8]):
        o = os.path.join(wd, f'sh_{i}.png')
        run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{t:.2f}', '-i', spec['out'], '-frames:v', '1', '-vf', 'scale=360:-1', o])
        outs.append(o)
    args = []
    for o in outs: args += ['-i', o]
    n = len(outs)
    fc = ''.join(f'[{i}]' for i in range(n)) + f'hstack={n}' if n > 1 else 'null'
    dst = os.path.join(spec.get('sheet_dir') or os.path.dirname(spec['out']).replace('1 Final', '3 Work files (safe to delete)'), spec['name'] + ' sheet.jpg')
    run(['ffmpeg', '-y', '-loglevel', 'error'] + args + ['-filter_complex', fc, '-q:v', '3', dst])
    print('SHEET', dst, [round(t, 1) for t in times[:8]])


def cover(spec):
    """Grid cover: heading + corner mark on a clean frame (no caption, no name tag). Saved next to the final as '<name> cover.jpg'."""
    wd = spec['work']; os.makedirs(wd, exist_ok=True)
    sp = dict(spec, captions=[], lower_third=None)
    ass = os.path.join(wd, 'cover.ass'); open(ass, 'w').write(build_ass(sp))
    t = spec.get('cover_t', 1.0)
    dst = os.path.splitext(spec['out'])[0] + ' cover.jpg'
    fc = (f"[0:v]setpts=PTS-STARTPTS+{t}/TB[v0];[1]scale=72:-1,format=rgba[m];[v0][m]overlay=944:281[v1];"
          f"[v1]ass={ass}:fontsdir={FONTS}[v]")
    run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(t), '-i', spec['src'], '-i', spec['mark'], '-filter_complex', fc,
         '-map', '[v]', '-frames:v', '1', '-q:v', '2', dst])
    print('COVER', dst)


if __name__ == '__main__':
    spec = json.load(open(sys.argv[1]))
    mode = sys.argv[2] if len(sys.argv) > 2 else 'render'
    if mode == 'check': check(spec)
    elif mode == 'cover': cover(spec)
    elif mode == 'sheet': sheet(spec, [float(x) for x in sys.argv[3:]] or None)
    else:
        check(spec); render(spec)
