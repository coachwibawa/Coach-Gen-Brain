#!/usr/bin/env python3
"""cg_lint.py: the mechanical checks for the Coach Gen Writing Rulebook (step 11).

Reads one draft and reports. Three kinds of finding:
  FAIL  a Tier 0 break a script can see: banned marks and words, a locked name or
        line not spelled exactly, a kept phrase of his changed.
  FORM  a delivery-format break from the output's card (article headers, letter name,
        figure labels). Counts as a break too.
  NOTE  Tier 2 mechanics (British spelling, Oxford comma, small counts in words,
        "everyday"). Never fails the draft.
Word count, sentence count and reading grade are reported, never failed.

What a script cannot see is left to the one-rule checkers (step 12): quality,
joins, invented facts, quotes. A clean lint is not a pass.

Usage:
  python3 tools/cg_lint.py DRAFT.md [--output article|letter|chapter|key-moments|case-study]
                                    [--keep "his typed phrase" ...] [--json]
  Use "-" for stdin. Exit code 1 when there is a FAIL or FORM finding, else 0.

Not checked here on purpose: bare "Lasting Change" (also ordinary English), print
names against brain.personas (needs the brain), "we" as the shared human "we".
"""
import argparse, difflib, json, re, sys

LOCKED_LINES = [
    "If you keep trying, but never finish, this is why.",
    "Every time you fail to make change, you succeed at staying who you are.",
]
# name -> (loose pattern, case matters)
LOCKED_NAMES = {
    "5 Laws of Lasting Change": (r"(?:5|five)[\s-]+laws?[\s-]+of[\s-]+lasting[\s-]+change", True),
    "3 Stages of Consistency": (r"(?:3|three)[\s-]+stages?[\s-]+of[\s-]+consistency", True),
    "Reset My Course": (r"reset[\s-]+my[\s-]+course", True),
    "Reframe Past Regret": (r"reframe[\s-]+past[\s-]+regret", True),
    "Resolve Present Friction": (r"resolve[\s-]+present[\s-]+friction", True),
    "Reap Future Habits": (r"reap[\s-]+future[\s-]+habits", True),
    "Relax To Results": (r"relax[\s-]+to[\s-]+results", True),
    "Energy Audit": (r"energy[\s-]+audit", False),
    "Consistent Effort": (r"consistent[\s-]+effort", False),
    "Momentum Engine": (r"momentum[\s-]+engine", False),
    "Effortless Result": (r"effortless[\s-]+result\b", False),
}
BUSINESS_WE = [
    r"\bour (?:team|company|clients|coaches|programmes?|programs?|services|courses|community|business|brand|mission|platform|products?|students|members|customers)\b",
    r"\bwe (?:offer|provide|specialise|specialize|help (?:you|people|introverts|clients))\b",
    r"\bwe are (?:a|the) (?:coaching|team|company)\b",
    r"\b(?:here )?at Coach Gen\b",
]
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⭐⭕⌀-⏿️‍]")
AMERICAN = {
    "color": "colour", "colors": "colours", "colored": "coloured", "favorite": "favourite", "behavior": "behaviour",
    "neighbor": "neighbour", "honor": "honour", "labor": "labour", "humor": "humour", "flavor": "flavour",
    "realize": "realise", "realized": "realised", "realizing": "realising", "recognize": "recognise",
    "recognized": "recognised", "organize": "organise", "organized": "organised", "apologize": "apologise",
    "emphasize": "emphasise", "prioritize": "prioritise", "summarize": "summarise", "analyze": "analyse",
    "minimize": "minimise", "maximize": "maximise", "criticize": "criticise", "visualize": "visualise",
    "center": "centre", "centered": "centred", "meter": "metre", "theater": "theatre", "gray": "grey",
    "judgment": "judgement", "defense": "defence", "offense": "offence", "traveling": "travelling",
    "traveled": "travelled", "cancelled": "cancelled", "fulfill": "fulfil", "enrollment": "enrolment",
    "practicing": "practising", "skeptical": "sceptical",
}
ARTICLE_HEADERS = ["Insights from me, to you.", "Insights from other experts.", "Insight from within you."]
SMALL = "one|two|three|four|five|six|seven|eight|nine|ten"


def norm_q(s):
    return s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def excerpt(text, a, b, pad=30):
    s = text[max(0, a - pad):b + pad].replace("\n", " ")
    return ("..." if a > pad else "") + s + ("..." if b + pad < len(text) else "")


def add(out, level, rule, text, a, b, msg):
    out.append({"level": level, "rule": rule, "line": line_of(text, a), "excerpt": excerpt(text, a, b), "msg": msg})


def syllables(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w:
        return 0
    g = re.findall(r"[aeiouy]+", w)
    n = len(g)
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1:
        n -= 1
    return max(1, n)


def stats(text):
    words = re.findall(r"[A-Za-z][A-Za-z'’-]*", text)
    sents = [s for s in re.split(r"(?<=[.!?])\s+|\n+", text) if re.search(r"[A-Za-z]", s)]
    nw, ns = len(words), max(1, len(sents))
    syl = sum(syllables(w) for w in words)
    grade = 0.39 * nw / ns + 11.8 * syl / max(1, nw) - 15.59 if nw else 0
    return {"words": nw, "sentences": len(sents), "reading_grade": round(grade, 1)}


def check_marks(text, out):
    for m in re.finditer("—", text):
        add(out, "FAIL", "T0 no em dashes", text, m.start(), m.end(), "em dash. Use a full stop, comma, colon or brackets")
    for m in re.finditer(r"(?<=\s)(?:--|–)(?=\s)", text):
        add(out, "FAIL", "T0 no em dashes", text, m.start(), m.end(), "a spaced dash stands in for an em dash")
    for m in re.finditer(";", text):
        add(out, "FAIL", "T0 no semicolons", text, m.start(), m.end(), "semicolon")
    for m in EMOJI.finditer(text):
        add(out, "FAIL", "T0 no emojis", text, m.start(), m.end(), "emoji or symbol character")
    for m in re.finditer(r"\bmy clients\b", norm_q(text), re.I):
        add(out, "FAIL", "T0 never \"my clients\"", text, m.start(), m.end(),
            "say \"someone I coach\", \"the people I coach\" or the person's name")
    for pat in BUSINESS_WE:
        for m in re.finditer(pat, text, re.I):
            add(out, "FAIL", "T0 no business \"we\"", text, m.start(), m.end(), "the company speaking")


def check_locked(text, out):
    for exact, (pat, strict_case) in LOCKED_NAMES.items():
        for m in re.finditer(pat, text, re.I):
            got = m.group(0)
            if got == exact:
                continue
            if got.lower() == exact.lower():
                level = "FAIL" if strict_case else "NOTE"
                add(out, level, "T0 locked names", text, m.start(), m.end(),
                    f"written \"{got}\", spelled \"{exact}\"" + ("" if strict_case else " (capitals only, may be ordinary prose)"))
            else:
                add(out, "FAIL", "T0 locked names", text, m.start(), m.end(), f"written \"{got}\", spelled \"{exact}\"")
    flat = re.sub(r"\s+", " ", text)
    words = flat.split(" ")
    for line in LOCKED_LINES:
        if line in flat:
            continue
        lw = line.split(" ")
        lset = {w.lower().strip('.,"') for w in lw}
        best, bi, bn = 0.0, 0, 0
        for n in range(len(lw) - 2, len(lw) + 4):
            for i in range(0, max(0, len(words) - n) + 1):
                win = words[i:i + n]
                if len({w.lower().strip('.,"') for w in win} & lset) < 3:
                    continue
                r = difflib.SequenceMatcher(None, line.lower(), " ".join(win).lower()).ratio()
                if r > best:
                    best, bi, bn = r, i, n
        if best >= 0.8:
            seen = " ".join(words[bi:bi + bn])
            pos = max(0, text.find(words[bi]))
            out.append({"level": "FAIL", "rule": "T0 locked lines", "line": line_of(text, pos),
                        "excerpt": seen, "msg": f"close to a locked line but not exact: \"{line}\""})


def check_material(text, out):
    for m in re.finditer(r"\[MATERIAL NEEDED(?!:\s*[^\]]+\])", text, re.I):
        add(out, "FAIL", "T0 missing material", text, m.start(), m.end(),
            "use [MATERIAL NEEDED: what, and where it would go]")


def check_keeps(text, keeps, out):
    flat = re.sub(r"\s+", " ", text)
    for k in keeps:
        kk = re.sub(r"\s+", " ", k).strip()
        i = flat.find(kk)
        if i < 0:
            out.append({"level": "FAIL", "rule": "T0 his words stay his", "line": 0, "excerpt": "",
                        "msg": f"his typed words are not in the draft exactly: \"{kk}\""})
            continue
        if re.match(r"\s*:", flat[i + len(kk):]):
            out.append({"level": "FAIL", "rule": "T0 his words stay his", "line": 0,
                        "excerpt": flat[max(0, i - 20):i + len(kk) + 25],
                        "msg": "his list item was turned into a heading (a colon follows it)"})


def paragraphs(text):
    return [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]


def check_article(text, out):
    lines = [l.strip() for l in text.split("\n")]
    pos = []
    for h in ARTICLE_HEADERS:
        if h in lines:
            pos.append(lines.index(h))
        else:
            out.append({"level": "FORM", "rule": "article card headers", "line": 0, "excerpt": "",
                        "msg": f"missing the header line \"{h}\" on a line of its own"})
            pos.append(None)
    if all(p is not None for p in pos) and not (pos[0] < pos[1] < pos[2]):
        out.append({"level": "FORM", "rule": "article card headers", "line": 0, "excerpt": "",
                    "msg": "the three header lines are out of order"})
    if pos[1] is not None:
        before = [l for l in lines[:pos[1]] if l]
        if not before or before[-1] != "Coach Gen":
            out.append({"level": "FORM", "rule": "article card sign-off", "line": pos[1] + 1, "excerpt": before[-1][:60] if before else "",
                        "msg": "Insight 1 ends with the line \"Coach Gen\""})
    nonblank = [l for l in text.split("\n") if l.strip()]
    if len(nonblank) > 3 and "\n\n" not in text:
        out.append({"level": "FORM", "rule": "article card spacing", "line": 0, "excerpt": "",
                    "msg": "a blank line between paragraphs"})


def check_letter(text, out):
    first = next((l for l in text.split("\n") if l.strip()), "")
    if not re.match(r"Lasting Change Letters #\d+", first.strip()):
        out.append({"level": "FORM", "rule": "letter card name", "line": 1, "excerpt": first[:70],
                    "msg": "named \"Lasting Change Letters #N\""})
    # His approved letter (P2, 90%) has one field and no Insight headers, so for letters the
    # article header lines are a note, not a break. The letter card says "everything on the
    # article card"; see tests/rules/README_LINT.md for the open question.
    sub = []
    check_article(text, sub)
    for f in sub:
        if f["rule"] == "article card headers":
            f = dict(f, level="NOTE", msg=f["msg"] + " (letter: his approved letter has none, so only a note)")
        out.append(f)


def check_chapter(text, out):
    for m in re.finditer(r"\bFigure\s+(\S+)", text):
        if not re.match(r"\d+\.\d+", m.group(1)):
            add(out, "FORM", "chapter card figures", text, m.start(), m.end(), "figures are numbered by chapter, like Figure 3.1")


def check_tier2(text, out):
    for m in re.finditer(r"\b([A-Za-z]+)\b", text):
        w = m.group(1)
        if w.lower() in AMERICAN:
            add(out, "NOTE", "T2 British spelling", text, m.start(), m.end(), f"\"{w}\" is \"{AMERICAN[w.lower()]}\" in British spelling")
    intro = re.compile(r"(?:Over|In|On|At|After|Before|When|If|While|During|For|By|As|Since|Once)\b")
    for m in re.finditer(r"\b([A-Za-z]+(?: [a-z]+)?), ([A-Za-z]+(?: [a-z]+)?) (and|or) ([A-Za-z]+)", text):
        s0 = max(text.rfind(".", 0, m.start()), text.rfind("\n", 0, m.start()), text.rfind("?", 0, m.start())) + 1
        if intro.match(text[s0:m.end()].lstrip()) or m.group(1) == "I":
            continue
        add(out, "NOTE", "T2 Oxford comma", text, m.start(), m.end(), "a list of three: comma before \"and\" or \"or\" (check it is a list)")
    for m in re.finditer(r"\beveryday\b(?=[\s]*(?:[,.:!?]|and\b|or\b|I\b|we\b|you\b|he\b|she\b|they\b|it\b))", text, re.I):
        add(out, "NOTE", "T2 everyday", text, m.start(), m.end(), "as an adverb it is \"every day\"")
    for m in re.finditer(r"\b([1-9]|10)\s+(times|days|weeks|months|years|hours|people|sessions|things|steps|ways|kinds|minutes)\b", text, re.I):
        add(out, "NOTE", "T2 numbers", text, m.start(), m.end(), "small counts in words (three times), digits for measures, percentages, years and labels")


def lint(text, output=None, keeps=()):
    out = []
    check_marks(text, out)
    check_locked(text, out)
    check_material(text, out)
    check_keeps(text, list(keeps), out)
    if output == "article":
        check_article(text, out)
    elif output == "letter":
        check_letter(text, out)
    elif output == "chapter":
        check_chapter(text, out)
    check_tier2(text, out)
    return out, stats(text)


def main():
    ap = argparse.ArgumentParser(description="Mechanical checks for the Coach Gen Writing Rulebook")
    ap.add_argument("file")
    ap.add_argument("--output", choices=["article", "letter", "chapter", "key-moments", "case-study"])
    ap.add_argument("--keep", action="append", default=[], help="a phrase he typed that must stay exactly")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8").read()
    findings, st = lint(text, a.output, a.keep)
    breaks = [f for f in findings if f["level"] in ("FAIL", "FORM")]
    if a.json:
        print(json.dumps({"result": "FAIL" if breaks else "CLEAN", "stats": st, "findings": findings}, ensure_ascii=False, indent=1))
    else:
        notes = [f for f in findings if f["level"] == "NOTE"]
        print(f"{'FAIL' if breaks else 'CLEAN'}: {len(breaks)} breaks, {len(notes)} Tier 2 notes. "
              f"{st['words']} words, {st['sentences']} sentences, reading grade {st['reading_grade']} (reported only)")
        for f in findings:
            where = f"line {f['line']}" if f["line"] else "draft"
            print(f"{f['level']:4}  {f['rule']}  ({where})  {f['msg']}" + (f"\n        {f['excerpt']}" if f["excerpt"] else ""))
        if not breaks:
            print("A clean lint is not a pass. Quality, joins, facts and quotes are checked in step 12.")
    sys.exit(1 if breaks else 0)


if __name__ == "__main__":
    main()
