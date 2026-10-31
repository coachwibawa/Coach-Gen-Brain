"""Compare a new turns.json with an older answer key (turns.json from a hand parser).
Usage: python3 tests/compare_parse.py new_turns.json old_turns.json
Prints how many paragraphs match exactly (ignoring spaces), and lists the first differences. No book text is stored."""
import json, re, sys, difflib
new = json.load(open(sys.argv[1])); old = json.load(open(sys.argv[2]))
norm = lambda t: re.sub(r'\s', '', t)
def bounds(turns):
    out, pos = {}, 0
    for t in turns:
        pos += len(norm(t['t'])); out[pos] = t
    return out
nb, ob = bounds(new), bounds(old)
if ''.join(norm(t['t']) for t in new) != ''.join(norm(t['t']) for t in old):
    print('TEXT DIFFERS, cannot compare boundaries'); sys.exit(1)
new_splits = [p for p in nb if p not in ob]      # boundary only in new
lost = [p for p in ob if p not in nb]            # boundary only in old
def next_page(turns, pos):
    pass
old_list = list(ob.items())
pagebreak = 0
for i, (p, t) in enumerate(old_list[:-1]):
    if p in lost and old_list[i + 1][1]['s'] != t['s']: pagebreak += 1
print(f"new {len(new)} turns, old {len(old)} turns, same text")
print(f"boundaries in both: {len(set(nb) & set(ob))}")
print(f"only in old (new joins): {len(lost)}, of which at a page break: {pagebreak}")
print(f"only in new (new splits): {len(new_splits)}")
for label, ps, src in (('NEW SPLIT', new_splits, nb), ('NEW JOIN not at page break', [p for i, (p, t) in enumerate(old_list[:-1]) if p in lost and old_list[i + 1][1]['s'] == t['s']], ob)):
    for p in ps[:12]:
        t = src[p]; print(f"  {label} after p{t['s']}: ...{t['t'][-50:]!r}")
