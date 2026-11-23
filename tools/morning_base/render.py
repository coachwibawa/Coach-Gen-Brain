#!/usr/bin/env python3
"""Morning Base renderer: one brief.json in, one fixed-layout HTML page out.

Usage: python3 tools/morning_base/render.py BRIEF.json OUT.html

The renderer owns the layout. Claude only fills brief.json. The 8 sections
always render, in the same order. An empty section shows "Clear." The only
optional block is Week, which renders when "week" is filled (Fridays).

Numbering: every item in Needs you, Money, Today's 3 and New calls gets one
number, counted on through the page and never restarted. The reply words
("done 2", "go 3", "draft 1", "snooze 4", "mine 6") use these numbers. The
number map is printed to stdout so the chat holds it.

brief.json (every key required, use [] or null when empty):
{
  "date": "2026-11-23",                      ISO date of the brief
  "day": 1,                                  streak day, Day 1 = 23 Nov 2026
  "headline": "one line from Setsu",
  "today": {
    "events": [{"time": "09:00 to 10:00", "title": "...", "notes": ["...", "..."]}],
    "tomorrow": {"time": "08:30", "title": "...", "prep": "..."} or null
  },
  "needs_you": [{"title": "...", "line": "..."}],          at most 5
  "money":     [{"who": "...", "amount": "Rp 1.500.000", "line": "..."}],
  "today3":    [{"title": "...", "next": "...", "claude": true}],   at most 3
  "new_calls": [{"title": "...", "when": "..."}],
  "wins":  {"done": ["..."], "week": 5},
  "brain": {"healthy": true, "failed": ["..."]},
  "week":  [{"day": "Mon", "closes": 3}, ...] or null
}

Checks (the page is not written if one fails): unknown or missing keys, caps
above, any em dash, en dash, semicolon or emoji in visible text.
"""
import base64
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = HERE / "fonts"

KEYS = ["date", "day", "headline", "today", "needs_you", "money", "today3",
        "new_calls", "wins", "brain", "week"]
CAPS = {"needs_you": 5, "today3": 3}
CLEAR = "Clear."
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿️‍]")


def fail(errors):
    sys.exit("render.py refused the brief:\n" + "\n".join("  " + e for e in errors))


def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, list):
        for x in o:
            yield from strings(x)
    elif isinstance(o, dict):
        for v in o.values():
            yield from strings(v)


def check(b):
    errors = []
    missing = [k for k in KEYS if k not in b]
    extra = [k for k in b if k not in KEYS]
    if missing:
        errors.append("missing keys: " + ", ".join(missing))
    if extra:
        errors.append("unknown keys: " + ", ".join(extra))
    for k, cap in CAPS.items():
        if len(b.get(k) or []) > cap:
            errors.append(f"{k}: {len(b[k])} items, cap is {cap}")
    for t in strings(b):
        if "—" in t or "–" in t:
            errors.append(f"dash in: {t[:60]}")
        if ";" in t:
            errors.append(f"semicolon in: {t[:60]}")
        if EMOJI.search(t):
            errors.append(f"emoji in: {t[:60]}")
    if errors:
        fail(errors)


def e(s):
    return html.escape(str(s), quote=True)


def font_face(family, file, weight):
    data = base64.b64encode((FONTS / file).read_bytes()).decode()
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:normal;"
            f"font-display:block;src:url(data:font/woff2;base64,{data}) format('woff2');}}")


CSS = """
:root{--abyss:#01131C;--deep:#0D4A59;--mist:#EAF5F6;--white:#FFFFFF;
--soft:rgba(1,19,28,.72);--line:rgba(13,74,89,.2);}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--mist)}
body{background:var(--mist);color:var(--abyss);font-family:'Montserrat',Arial,sans-serif;
font-weight:400;font-size:16px;line-height:26px;-webkit-text-size-adjust:100%}
.page{max-width:600px;margin:0 auto;padding:32px 24px 48px;border-top:2px solid var(--deep)}
.eyebrow{font-weight:600;font-size:12px;line-height:16px;letter-spacing:.12em;
text-transform:uppercase;color:var(--deep)}
.date{display:flex;justify-content:space-between;gap:16px}
h1{font-family:'Libre Baskerville',Georgia,serif;font-weight:400;font-size:24px;
line-height:36px;color:var(--abyss);margin:16px 0 24px}
.maze{display:block;width:100%;height:16px;margin-bottom:8px}
section{padding:24px 0;border-bottom:2px solid var(--line)}
section:last-of-type{border-bottom:0}
h2{font-weight:600;font-size:12px;line-height:16px;letter-spacing:.12em;
text-transform:uppercase;color:var(--deep);margin-bottom:16px}
.clear{color:var(--soft)}
ol{list-style:none}
li{display:flex;gap:16px;padding:8px 0}
li+li{border-top:1px solid var(--line)}
.n{flex:0 0 24px;font-weight:700;color:var(--deep);text-align:right}
.b{flex:1;min-width:0;overflow-wrap:anywhere}
.title{font-weight:600}
.sub{color:var(--soft)}
.tag{font-weight:600;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--deep)}
.prep{margin-top:16px;padding-top:16px;border-top:1px solid var(--line)}
.stat{display:flex;gap:32px;margin-top:16px}
.stat b{display:block;font-weight:700;font-size:24px;line-height:32px;color:var(--deep)}
.stat span{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--soft)}
.ok{font-weight:600;color:var(--deep)}
.bars{display:flex;align-items:flex-end;gap:8px;height:120px;margin-top:8px}
.bar{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%}
.bar i{display:block;width:100%;background:var(--deep)}
.bar b{font-weight:600;font-size:12px;line-height:16px;color:var(--deep);margin-bottom:4px}
.days{display:flex;gap:8px;margin-top:8px}
.days span{flex:1;text-align:center;font-size:12px;line-height:16px;letter-spacing:.06em;
text-transform:uppercase;color:var(--soft)}
footer{margin-top:24px;padding-top:16px;border-top:2px solid var(--deep);font-size:13px;
line-height:20px;color:var(--soft)}
footer b{font-weight:600;color:var(--deep)}
@media (max-width:480px){h1{font-size:22px;line-height:32px}}
"""

MAZE = ('<svg class="maze" viewBox="0 0 552 16" preserveAspectRatio="none" aria-hidden="true">'
        '<path d="M0 14H96V2H192V14H288V2H384V14H480V2H552" fill="none" stroke="#0D4A59" '
        'stroke-width="2" stroke-dasharray="8 6"/></svg>')


def section(title, body):
    return f'<section><h2>{e(title)}</h2>{body or f"<p class=clear>{CLEAR}</p>"}</section>'


def numbered(rows):
    if not rows:
        return ""
    return "<ol>" + "".join(
        f'<li><span class="n">{n}</span><div class="b">{inner}</div></li>' for n, inner in rows
    ) + "</ol>"


def render(b):
    n = 0
    numbers = []

    def take(label):
        nonlocal n
        n += 1
        numbers.append(f"{n}  {label}")
        return n

    d = dt.date.fromisoformat(b["date"])
    date_line = f"{d.strftime('%A')} {d.day} {d.strftime('%B %Y')}"

    # 1 Headline sits in the header
    # 2 Today
    t = b["today"] or {}
    ev = t.get("events") or []
    body = ""
    if ev:
        body = "<ol>" + "".join(
            '<li><div class="b"><div class="tag">{}</div><div class="title">{}</div>{}</div></li>'.format(
                e(x["time"]), e(x["title"]),
                "".join(f'<div class="sub">{e(s)}</div>' for s in (x.get("notes") or [])[:2]))
            for x in ev) + "</ol>"
    tm = t.get("tomorrow")
    if tm:
        body += ('<div class="prep"><span class="tag">Tomorrow {}</span>'
                 '<div class="title">{}</div><div class="sub">{}</div></div>').format(
            e(tm["time"]), e(tm["title"]), e(tm.get("prep", "")))
    s_today = section("Today", body)

    # 3 Needs you
    s_needs = section("Needs you", numbered([
        (take("needs you: " + x["title"]),
         f'<div class="title">{e(x["title"])}</div><div class="sub">{e(x["line"])}</div>')
        for x in b["needs_you"]]))

    # 4 Money
    s_money = section("Money", numbered([
        (take("money: " + x["who"]),
         f'<div class="title">{e(x["who"])}, {e(x["amount"])}</div><div class="sub">{e(x["line"])}</div>')
        for x in b["money"]]))

    # 5 Today's 3
    s_three = section("Today's 3", numbered([
        (take("today's 3: " + x["title"]),
         '<div class="title">{}</div><div class="sub">{}</div>{}'.format(
             e(x["title"]), e(x.get("next", "")),
             '<div class="tag">Claude can start</div>' if x.get("claude") else ""))
        for x in b["today3"]]))

    # 6 New calls
    s_calls = section("New calls", numbered([
        (take("new call: " + x["title"]),
         f'<div class="title">{e(x["title"])}</div><div class="sub">{e(x["when"])}. Say mine.</div>')
        for x in b["new_calls"]]))

    # 7 Wins
    w = b["wins"] or {}
    done = w.get("done") or []
    body = ""
    if done:
        body = "<ol>" + "".join(f'<li><div class="b">{e(x)}</div></li>' for x in done) + "</ol>"
    body += ('<div class="stat"><div><b>{}</b><span>Closed this week</span></div>'
             '<div><b>Day {}</b><span>Streak</span></div></div>').format(
        e(w.get("week", 0)), e(b["day"]))
    s_wins = section("Wins", body)

    # 8 Brain
    br = b["brain"] or {}
    if br.get("healthy"):
        body = '<p class="ok">Healthy.</p>'
    else:
        body = '<ol>' + "".join(f'<li><div class="b">{e(x)}</div></li>'
                                for x in (br.get("failed") or ["Health check did not run."])) + "</ol>"
    s_brain = section("Brain", body)

    # Fridays: Week
    s_week = ""
    wk = b.get("week")
    if wk:
        top = max([x["closes"] for x in wk] + [1])
        bars = "".join(
            f'<div class="bar"><b>{e(x["closes"])}</b><i style="height:{round(100 * x["closes"] / top)}%"></i></div>'
            for x in wk)
        days = "".join(f'<span>{e(x["day"])}</span>' for x in wk)
        s_week = section("Week", f'<div class="bars">{bars}</div><div class="days">{days}</div>')

    fonts = "".join([
        font_face("Montserrat", "montserrat-latin-400-normal.woff2", 400),
        font_face("Montserrat", "montserrat-latin-600-normal.woff2", 600),
        font_face("Montserrat", "montserrat-latin-700-normal.woff2", 700),
        font_face("Libre Baskerville", "libre-baskerville-latin-400-normal.woff2", 400),
    ])

    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Morning Base {e(b["date"])} | Coach Gen</title>
<style>{fonts}{CSS}</style></head>
<body><main class="page">
<div class="date"><span class="eyebrow">Morning Base</span><span class="eyebrow">Day {e(b["day"])}</span></div>
<h1>{e(b["headline"])}</h1>
<div class="eyebrow" style="margin-bottom:8px">{e(date_line)}</div>
{MAZE}
{s_today}{s_needs}{s_money}{s_three}{s_calls}{s_wins}{s_brain}{s_week}
<footer><b>Reply words:</b> done 2 5, go 3, draft 1, add a thing, snooze 4, list, mine 6</footer>
</main></body></html>
"""
    return page, numbers


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    b = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    check(b)
    page, numbers = render(b)
    Path(sys.argv[2]).write_text(page, encoding="utf-8")
    print("numbers:")
    print("\n".join(numbers) if numbers else "  none")


if __name__ == "__main__":
    main()
