#!/usr/bin/env python3
"""Render the rulebook source (rulebook_vN.txt) to HTML for a Google Doc.

Source format: "# " title, "## " tier or section, "### " rule name,
"- " a rule line (numbered straight through the whole doc), anything else a
paragraph. Checks: no em dash, no semicolon, every rule has lines.
Usage: python3 rules/rulebook/build_rulebook.py SRC.txt OUT.html
"""
import html, sys
from pathlib import Path

src, out = Path(sys.argv[1]), Path(sys.argv[2])
lines = [l.rstrip() for l in src.read_text(encoding="utf-8").splitlines() if l.strip()]
bad = [l for l in lines if "—" in l or ";" in l]
if bad:
    sys.exit("em dash or semicolon:\n" + "\n".join(bad))

e = html.escape
parts, n, open_ol, rules, rule_lines = [], 0, False, 0, {}
current = None


def close():
    global open_ol
    if open_ol:
        parts.append("</ol>")
        open_ol = False


for l in lines:
    if l.startswith("### "):
        close()
        current = l[4:]
        rules += 1
        rule_lines[current] = 0
        parts.append(f"<h3>{e(current)}</h3>")
    elif l.startswith("## "):
        close()
        parts.append(f"<h2>{e(l[3:])}</h2>")
    elif l.startswith("# "):
        close()
        parts.append(f"<h1>{e(l[2:])}</h1>")
    elif l.startswith("- "):
        n += 1
        if not open_ol:
            parts.append(f'<ol start="{n}">')
            open_ol = True
        parts.append(f"<li>{e(l[2:])}</li>")
        if current:
            rule_lines[current] += 1
    else:
        close()
        parts.append(f"<p>{e(l)}</p>")
close()
empty = [k for k, v in rule_lines.items() if v == 0]
if empty:
    sys.exit("rules with no lines: " + ", ".join(empty))
body = "\n".join(parts)
out.write_text(f"<html><head><meta charset=\"utf-8\"></head><body>\n{body}\n</body></html>\n", encoding="utf-8")
words = sum(len(l.split()) for l in lines)
print(f"ok: {rules} rules and cards, {n} numbered lines, {words} words -> {out}")
