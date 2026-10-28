"""Turn cleaned turns into one load file for brain.load_from_github.

Input: turns.json, a list of {"s": page, "t": text, "ch": chapter label, "sec": section label, "sp": speaker (optional)}.
Output: loads/<name>.json plus a printed md5 per document to compare with what the database returns.

Usage:
  python3 tools/build_load.py turns.json loads/name.json meta.json
meta.json holds: source_id or source {...}, context_prefix, speaker, title_prefix, notes, added_by.
"""
import json, sys, hashlib
from collections import Counter

turns = json.load(open(sys.argv[1]))
out_path = sys.argv[2]
meta = json.load(open(sys.argv[3]))
TARGET = meta.get('target_words', 320)
MAX_DOC_BYTES = meta.get('max_doc_bytes', 60000)

def nwords(s):
    return len(s.strip().split())

# one document per chapter, split long chapters at section headings
docs, size = [], 0
for t in turns:
    l = len(json.dumps(t, ensure_ascii=False).encode())
    is_head = t['t'] == t.get('sec')
    if not docs or docs[-1]['ch'] != t['ch'] or (size > MAX_DOC_BYTES and is_head):
        docs.append({'ch': t['ch'], 'turns': []}); size = 0
    docs[-1]['turns'].append(t); size += l
cnt = Counter(d['ch'] for d in docs); seen = Counter()

out_docs, report = [], []
for d in docs:
    seen[d['ch']] += 1
    part = f" (part {seen[d['ch']]} of {cnt[d['ch']]})" if cnt[d['ch']] > 1 else ''
    T = d['turns']
    chunks, buf, words = [], [], 0
    for i, t in enumerate(T, start=1):
        w = nwords(t['t'])
        if words + w > TARGET and buf:
            chunks.append(buf); buf = buf[-1:]; words = sum(nwords(T[j-1]['t']) for j in buf)
        buf.append(i); words += w
    if buf: chunks.append(buf)
    pages = f"PDF pages {T[0]['s']} to {T[-1]['s']}"
    turns_out = []
    for t in T:
        o = {'s': t['s'], 't': t['t']}
        if t.get('sp') and t['sp'] != meta['speaker']:
            o['sp'] = t['sp']
        turns_out.append(o)
    out_docs.append({
        'title': f"{meta['title_prefix']}, {d['ch']}{part}",
        'chapter': d['ch'],
        'note_tail': f"This document: {d['ch']}{part}, {pages}, {len(T)} paragraphs.",
        'turns': turns_out,
        'chunks': [[p, b[0], b[-1], T[b[0]-1].get('sec', d['ch'])] for p, b in enumerate(chunks, start=1)],
    })
    report.append((out_docs[-1]['title'], len(T), len(chunks), hashlib.md5('\n'.join(t['t'] for t in T).encode()).hexdigest()))

f = {k: v for k, v in meta.items() if k not in ('title_prefix', 'target_words', 'max_doc_bytes')}
f['docs'] = out_docs
json.dump(f, open(out_path, 'w'), ensure_ascii=False, separators=(',', ':'))
for r in report: print(r)
print('docs', len(out_docs), 'turns', sum(r[1] for r in report), 'chunks', sum(r[2] for r in report),
      'all_md5', hashlib.md5('\n'.join(t['t'] for t in turns).encode()).hexdigest())
