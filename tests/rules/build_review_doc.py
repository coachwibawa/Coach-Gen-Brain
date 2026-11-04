"""Build the review doc (HTML for Drive conversion) and test_set v2 extras. Texts copied by script."""
import json, re, html, sys

S = '/tmp/claude-0/-home-claude/20a7e8bf-877e-5974-b3fa-8df9b03d18a9/scratchpad'
UP = '/mnt/user-data/uploads/5 Laws of Lasting Change/Book'
JSONL = '/root/.claude/projects/-home-claude/20a7e8bf-877e-5974-b3fa-8df9b03d18a9.jsonl'
ts = json.load(open(f'{S}/test_set.json'))
C = {c['id']: c for c in ts['cases']}

def jsonl_texts():
    for line in open(JSONL):
        try:
            d = json.loads(line)
        except Exception:
            continue
        m = d.get('message', {})
        c = m.get('content')
        if isinstance(c, str):
            yield m.get('role'), 'msg', c
        elif isinstance(c, list):
            for p in c:
                if p.get('type') == 'text':
                    yield m.get('role'), 'msg', p['text']
                elif p.get('type') == 'tool_result':
                    cc = p.get('content')
                    for t in ([cc] if isinstance(cc, str) else [x.get('text', '') for x in cc if isinstance(x, dict)] if isinstance(cc, list) else []):
                        yield m.get('role'), 'tool', t

letter = cs1 = None
for role, kind, t in jsonl_texts():
    if role == 'user' and kind == 'msg' and 'Lasting Change Letters #1:Never Split The Difference' in t:
        i = t.find('Lasting Change Letters #1:Never Split The Difference')
        letter = t[i:].strip()
    if kind == 'tool' and '# **Case Study Test**' in t and cs1 is None:
        cs1 = json.loads(t)['fileContent']
assert letter and cs1

def cs_passage(n):
    i = cs1.find(f'## **Passage {n}**') + len(f'## **Passage {n}**')
    j = cs1.find('\n|', i)
    return cs1[i:j].strip()

e4 = [p for p in open(f'{UP}/build/law-1/epoch4_chapter.md').read().split('\n\n') if p.strip()]
parent = next(p for p in e4 if p.startswith('If you are a parent who has paid'))
week = next(p for p in e4 if p.startswith('If you have ever called yourself lazy, look at your own week'))
ml = open(f'{UP}/build/law-1/markup_log.md').read()
i = ml.find('His rewrite, word for word:\n"') + len('His rewrite, word for word:\n"')
j = ml.find('"\n\nHis words, word for word', i)
points = ml[i:j]

new = [
 {'id': 'F8', 'verdict': 'fail', 'output': 'case study (book)', 'title': 'Case Study Test round 1, passage 2: Aiman',
  'source': 'Google Doc "5 Laws, Case Study Test (8 passages)" (1xAwmGFpjozX_NZhuKM30pIPySXkb7X_lB0eY5wuRTMo)', 'date': '2026-11-04', 'score': '2/10',
  'his_words': ['Wtf is this, nothing after the first sentence make any sense'],
  'flags': [{'anchor': 'In late October, he came to me with a deadline', 'his_note': 'nothing after the first sentence make any sense'}],
  'cause': 'Claude\'s reading of the marks: under-built. Each gap between two recorded moments needed one or two reasonable bridges.',
  'text': cs_passage(2)},
 {'id': 'P2', 'verdict': 'pass', 'output': 'letter', 'title': 'Lasting Change Letters #1: Never Split The Difference (full, as you pasted it)',
  'source': 'Pasted by Gen in chat, 4 Nov 2026. Accepted 25 Sep at "90%, which is a passing mark."', 'date': '2026-09-25', 'score': '90%. The force paragraph endorsed line by line.',
  'his_words': ['90%, which is a passing mark. if I want 100% I\'ll write it without AI.',
                'this is one paragraph here that I would not be able to conjure myself even though that is 100% what I am thinking. and this paragraph is in the right place, with the right development of ideas, was the right bridge between the previous and next paragraph.'],
  'keep': [{'anchor': 'Most of us try to win this negotiation by force.', 'his_note': 'the force paragraph'}],
  'text': letter},
 {'id': 'P7', 'verdict': 'pass', 'output': 'book chapter', 'title': 'Chapter 3 epoch 4: the parent paragraph',
  'source': 'Book/build/law-1/epoch4_chapter.md. Comment in markup_log.md.', 'date': '2026-10-30', 'score': 'praised',
  'his_words': ['good passage.', 'good mix of credibility and argument'], 'text': parent},
 {'id': 'P8', 'verdict': 'pass', 'output': 'book chapter', 'title': 'Chapter 3 epoch 4: the reader\'s-week paragraph',
  'source': 'Book/build/law-1/epoch4_chapter.md. Comment in markup_log.md.', 'date': '2026-11-03', 'score': 'praised',
  'his_words': ['good way to conclude, I like it.'], 'text': week},
 {'id': 'P9', 'verdict': 'pass', 'output': 'book chapter', 'title': 'Chapter 3 epoch 5: David\'s points system, your rewrite',
  'source': 'Book/build/law-1/markup_log.md, 3 Nov.', 'date': '2026-11-03', 'score': 'his own rewrite',
  'his_words': ['my rewrites here makes it feel better.'], 'text': points},
 {'id': 'P10', 'verdict': 'pass', 'output': 'case study (book)', 'title': 'Case Study Test round 1, passage 6: your door-to-door story',
  'source': 'Google Doc "5 Laws, Case Study Test (8 passages)"', 'date': '2026-11-04', 'score': '8/10',
  'his_words': ['Good and concise, short and sweet.', 'Note that not all stories has to be short, and not all stories have to be long.'], 'text': cs_passage(6)},
]
for n in new:
    for f in n.get('flags', []) + n.get('keep', []):
        assert f['anchor'] in n['text'], (n['id'], f['anchor'])
    C[n['id']] = n

E = lambda s: html.escape(s, quote=False)
def paras(t):
    out = []
    for p in re.split(r'\n\s*\n', t.strip()):
        p = p.strip()
        if p == '---':
            out.append('<p><b>(next passage)</b></p>')
        elif p.startswith('## '):
            lines = p.split('\n')
            out.append(f'<h3>{E(lines[0][3:])}</h3>')
            for l in lines[1:]:
                out.append(f'<p>{E(l)}</p>')
        else:
            p = re.sub(r'\*\*(.+?)\*\*', lambda m: '\x00b' + m.group(1) + '\x00e', p)
            p = E(p).replace('\x00b', '<b>').replace('\x00e', '</b>').replace('\n', '<br>')
            out.append(f'<p>{p}</p>')
    return '\n'.join(out)

box = ('<table border="1" cellpadding="6" style="border-collapse:collapse;width:100%"><tr>'
       '<td style="width:30%"><b>Your call</b></td><td><b>Why</b></td></tr>'
       '<tr><td>still {v} / now {o} / drop</td><td>&nbsp;</td></tr></table>')

CTX = {
 'F1': 'I rewrote my own round 2 passage line by line against your notes and the guide findings, after the full read of Strunk and Zinsser.',
 'F2': 'The Melina scene and her old sentence, round 3. I added her health and a nutritionist from the session transcript. Neither was in any approved text. You stopped marking after passage 1.',
 'F3': 'Chapter 3 epoch 4, the David opening. He asks if his problem is clarity. Two paragraphs later the ditch image arrives with no bridge back to the question. Shown with the paragraphs around it.',
 'F4': 'Article era. Chimp piece v5, 407 words.',
 'F5': 'Article era. Chimp piece v6. Your notes were typed inline into a copy of this draft.',
 'F6': 'Article era. Chimp piece v7, after your v6 notes. Two arcs at once, the ending announced early, two lines narrating the structure.',
 'F7': 'Not a passage: a test that your typed words survive. You typed this phrase as the first item in a list. I changed it three times.',
 'F8': 'Case Study Test round 1. My build of a client case from his record, written short.',
 'P1': 'Your own rewrite of the chimp piece, after v10. Published as "Primal Regret".',
 'P2': 'The full letter. The force paragraph is the one you endorsed line by line.',
 'P3': 'Book Introduction as merged into the master draft (epoch 4 with your edits). Scored at epoch 3, before the book standard rose.',
 'P4': 'Chapter 1 as merged (epoch 3 with your edits). Scored before the later Book Rules (R36 to R41).',
 'P5': 'Article era (about 600 words). Scored 90% as an article, not as a book passage.',
 'P6': 'Article era. Scored 90% as an article, not as a book passage.',
 'P7': 'Recent, book standard. One paragraph you praised in the epoch 4 draft that otherwise failed.',
 'P8': 'Recent, book standard. The paragraph you called a good conclusion, same draft.',
 'P9': 'Recent. Your rewrite of my paragraph, the one that started the Built Detail Test (the "sick" detail).',
 'P10': 'Recent. My build of your own story (record F-85), 8/10 in the Case Study Test.',
}

parts = ['<h1>Rule Test Set, Review</h1>',
 '<p>These passages become the exam for the new rules. The checker must catch every problem in the fail cases and leave the pass cases alone. A wrong verdict here trains the checker wrong, so judge each one again by today\'s standard (the book), not the standard of the day you scored it.</p>',
 '<p>For each passage: read it, then fill the box. <b>still fail / still pass</b> keeps it. <b>now pass / now fail</b> flips it. <b>drop</b> takes it out of the test. A few words of why help. Comments on lines work too.</p>',
 '<h1>Part A. Drafts you rejected. Still fail?</h1>']

def entry(c):
    v = 'fail' if c['verdict'] == 'fail' else 'pass'
    o = 'pass' if v == 'fail' else 'fail'
    h = [f'<h2>{c["id"]}. {E(c["title"])}</h2>', f'<p><i>{E(CTX[c["id"]])} {E(c["date"])}. Score then: {E(c["score"])}.</i></p>']
    if c.get('his_words'):
        h.append('<p><b>What you said then:</b></p><ul>' + ''.join(f'<li>"{E(w)}"</li>' for w in c['his_words']) + '</ul>')
    if c.get('flags'):
        h.append('<p><b>Lines you flagged:</b></p><ul>' + ''.join(f'<li>"{E(f["anchor"])}" : {E(f["his_note"])}</li>' for f in c['flags']) + '</ul>')
    if c.get('keep'):
        h.append('<p><b>Lines you liked inside it:</b></p><ul>' + ''.join(f'<li>"{E(f["anchor"])}" : {E(f["his_note"])}</li>' for f in c['keep']) + '</ul>')
    if c['id'] == 'F7':
        h.append('<p><b>What you typed:</b></p>' + paras(c['his_typed']))
        h.append('<p><b>My three wrong versions:</b></p><ul>' + ''.join(f'<li>{E(r["what"])}: "{E(r["text"])}"</li>' for r in c['failed_renderings']) + '</ul>')
        h.append('<p><b>What went into the book:</b></p>' + paras(c['approved_rendering']))
    else:
        h.append('<p><b>The passage:</b></p>' + paras(c['text']))
    h.append(box.format(v=v, o=o))
    return '\n'.join(h)

for k in ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8']:
    parts.append(entry(C[k]))
parts.append('<h1>Part B. Passages you approved before the book standard. Still pass?</h1>')
for k in ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']:
    parts.append(entry(C[k]))
parts.append('<h1>Part C. Recent passages you liked. Add them as pass?</h1>')
for k in ['P7', 'P8', 'P9', 'P10']:
    parts.append(entry(C[k]))

open(f'{S}/review_doc.html', 'w').write('<html><body>' + '\n'.join(parts) + '</body></html>')
order = ['F1','F2','F3','F4','F5','F6','F7','F8','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10']
ts['version'] = 2
ts['status'] = 'under review by Gen, 4 Nov 2026'
ts['cases'] = [C[k] for k in order]
json.dump(ts, open(f'{S}/test_set_v2.json', 'w'), ensure_ascii=False, indent=1)
print(len(open(f'{S}/review_doc.html').read()), 'chars', len(order), 'cases')
