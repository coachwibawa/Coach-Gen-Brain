import re, sys

path = sys.argv[1]
raw = open(path, encoding="utf-8").read()
lines = raw.split("\n")
heading = lines[0]
body = "\n".join(lines[1:]).strip()
paras = [p for p in body.split("\n\n") if p.strip()]

def syllables(w):
    w = w.lower()
    w = re.sub(r"[^a-z]", "", w)
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    n = len(re.findall(r"[aeiouy]{1,2}", w))
    return max(1, n)

text = body
sents = [s for s in re.split(r"(?:(?<=[.!?])|(?<=[.!?]\"))\s+(?=[A-Z\"0-9])", text.replace("\n\n", " ")) if s.strip()]
words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-%]*", text)
nw = len(words)
ns = len(sents)
nsyl = sum(syllables(w) for w in words)
wps = nw / ns
spw = nsyl / nw
fk = 0.39 * wps + 11.8 * spw - 15.59
ease = 206.835 - 1.015 * wps - 84.6 * spw
short = [s for s in sents if len(re.findall(r"[A-Za-z0-9']+", s)) < 8]
print(f"heading: {heading}")
print(f"paragraphs: {len(paras)}")
print(f"words (body): {nw}  words incl heading: {nw + len(re.findall(r'[A-Za-z0-9]+', heading.lstrip('# ')))}")
print(f"sentences: {ns}  words/sentence: {wps:.1f}")
print(f"FK grade: {fk:.1f}  reading ease: {ease:.1f}")
print(f"sentences under 8 words: {len(short)} ({100*len(short)/ns:.0f}%)")
for s in short:
    print("   SHORT:", s)
caps = re.findall(r"\b(?:[A-Z][a-z]+|[A-Z]{2,})\b", text)
nums = re.findall(r"\b\d+[%\-]?\w*", text)
print(f"digits/numbers: {nums}")
print("longest sentence:", max(len(re.findall(r"[A-Za-z0-9']+", s)) for s in sents))

# mechanics
probs = []
if "—" in raw or "–" in raw or " - " in raw or "--" in raw:
    probs.append("em/en dash")
if ";" in raw:
    probs.append("semicolon")
if re.search(r"my clients", raw, re.I):
    probs.append("my clients")
us = ["realize", "realized", "color", "neighbor", "favorite", "practice ", "center", "behavior", "honor", "organize", "apologize", "recognize"]
for u in us:
    if re.search(r"\b" + u, raw, re.I):
        probs.append("US spelling: " + u)
if re.search(r"\bevery day\b", raw) is None and "everyday" in raw:
    pass
spelled = re.findall(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|forty|fifty|hundred)\b", raw, re.I)
print("spelled numbers (check H1):", spelled)
emoji = re.findall(r"[\U0001F300-\U0001FAFF☀-➿]", raw)
if emoji:
    probs.append("emoji")
curly = re.findall(r"[‘’“”]", raw)
print("curly quotes:", len(curly))
print("MECHANICS:", "clean" if not probs else probs)
# every list of three: crude Oxford comma check: ", X and Y" after a comma list
for m in re.finditer(r"[^.]*?,[^.,]+,[^.,]+ (and|or) [^.]*\.", text):
    seg = m.group(0)
    if re.search(r", (and|or) ", seg) is None:
        print("OXFORD? ", seg.strip())
