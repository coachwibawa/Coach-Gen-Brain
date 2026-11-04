"""Build the rule test set from source files. Texts are copied by script, never retyped."""
import json, re, html, subprocess, sys

S = '/tmp/claude-0/-home-claude/20a7e8bf-877e-5974-b3fa-8df9b03d18a9/scratchpad'
UP = '/mnt/user-data/uploads/5 Laws of Lasting Change/Book'
ARC = '/home/claude/coach-gen-brain/archive/pre-prune/project-docs'
JSONL = '/root/.claude/projects/-home-claude/20a7e8bf-877e-5974-b3fa-8df9b03d18a9.jsonl'
OUT = sys.argv[1]

chat = open(f'{S}/chat_history.txt').read()

def chat_piece(start_marker, after):
    i = chat.find(start_marker, after)
    j = chat.find('\n-----', i)
    return chat[i:j].strip()

v5 = chat_piece('**Insight 1', chat.find('v5. 407 words'))
v6 = chat_piece('**Insight 1', chat.find('v6. 396 words'))
v7 = chat_piece('**Insight 1', chat.find('Other fixes: Melvin.'))

# round 3 taste test passages
r3 = open(f'{UP}/Research/taste_tests/r3/taste_test_round3.html').read()
r3 = re.sub(r'<(script|style)[\s\S]*?</\1>', '', r3)
r3 = re.sub(r'<br\s*/?>|</p>|</div>|</h\d>', '\n', r3)
r3 = html.unescape(re.sub(r'<[^>]+>', '', r3))
r3 = re.sub(r'\n\s*\n+', '\n\n', r3)
def r3_passage(n):
    i = r3.find(f'Passage {n}\n') + len(f'Passage {n}\n')
    j = r3.find('Mark:', i)
    return r3[i:j].strip()

# epoch 4 ditch context
e4 = open(f'{UP}/build/law-1/epoch4_chapter.md').read()
paras = [p for p in e4.split('\n\n') if p.strip()]
k = next(i for i, p in enumerate(paras) if p.startswith('In our first session'))
e4_text = '\n\n'.join(paras[k:k + 6])

lr = open(f'{ARC}/Coach_Gen_Language_Rules.md').read()
mi = lr.find('> **Insight 1. Insights from me, to you.**')
mj = lr.find('\n---', mi)
melvin = '\n'.join(l[2:] if l.startswith('> ') else l.lstrip('>') for l in lr[mi:mj].strip().split('\n'))
force = re.search(r'From Lasting Change Letters #1: "(Most of us try to win.*?as strong as you are\.)"', lr).group(1)

def js_blocks(name):
    out = subprocess.run(['node', '-e', f"const m=require('{UP}/source/chapters/{name}.js');console.log(JSON.stringify(m.blocks))"],
                         capture_output=True, text=True, check=True).stdout
    parts = []
    for b in json.loads(out):
        if b['t'] in ('first', 'p', 'pull'):
            parts.append(b['text'])
        elif b['t'] == 'h':
            parts.append('## ' + b['text'])
        elif b['t'] == 'summary':
            parts.append('## ' + b['title'] + '\n' + '\n'.join('- ' + x for x in b['items']))
        elif b['t'] == 'box':
            parts.append('## ' + b['title'] + '\n' + b['intro'] + '\n' + '\n'.join('- ' + x for x in b['questions']))
    return '\n\n'.join(parts)

def notion_article(name):
    for line in open(JSONL):
        if f'\\\\\\"Name\\\\\\":\\\\\\"{name}\\\\\\"' not in line and f'"Name\\":\\"{name}\\"' not in line and name not in line:
            continue
        d = json.loads(line)
        c = d.get('message', {}).get('content')
        if not isinstance(c, list):
            continue
        for part in c:
            if part.get('type') != 'tool_result':
                continue
            cc = part.get('content')
            texts = [cc] if isinstance(cc, str) else [x.get('text', '') for x in cc if isinstance(x, dict)]
            for t in texts:
                try:
                    page = json.loads(t)['text']
                except Exception:
                    continue
                m = re.search(r'<properties>\n(.*?)\n</properties>', page, re.S)
                if not m:
                    continue
                props = json.loads(m.group(1))
                if props.get('Name') != name:
                    continue
                fix = lambda s: s.replace('<br /><br />', '\n\n').replace('<br />', '\n')
                return fix(props['Insight 1']), fix(props['Insight 2']), fix(props['Insight 3'])
    raise SystemExit('not found ' + name)

stages = notion_article('3 Stages of Consistency')
busy = notion_article('How can you be busy but lazy?')
art = lambda t: '\n\n'.join(t)

cases = [
 {
  'id': 'F1', 'verdict': 'fail', 'output': 'book passage (taste test)',
  'title': 'Taste test round 3, passage 1: "Why Pushing Harder Fails", patched rewrite',
  'source': 'Book/Research/taste_tests/r3/taste_test_round3.html (Google Doc "5 Laws Taste Test, Round 3"). Marks in claude/Coach_Gen_Book_Calibration_Log.md, Round 3 results.',
  'date': '2026-10-04',
  'score': 'mark 3/10, flow 5/6',
  'his_words': [
   'yes now it\'s parallel and long, but it\'s just making it robotic and repeated. It’s overall worse. I think since the start of the idea is fine but becomes really confusing and wobbly at the start of p2; everything after feels trash',
   'I think this epoch is a total failure.',
  ],
  'flags': [
   {'anchor': 'If the diet slips, make it stricter. If you', 'his_note': 'the and you should be parallel. either both thes or both you(r)ss'},
   {'anchor': 'It never lasted, and the higher I set the bar, the worse it got', 'his_note': 'it is not clear here. if this happens, fix is either reclarify, or make the previous clause more concise.'},
   {'anchor': 'So what happens if you stop pushing? What finally worked for me was slower,', 'his_note': 'wtf is this?'},
   {'anchor': 'And it doesn’t start from zero. Somewhere in your life, you have already changed something without noticing', 'his_note': 'too many differing concepts that were unexplored.'},
  ],
  'cause': 'Claude\'s account (calibration log): patched line by line against his notes and a findings checklist, lines bolted on for warmth, a Chapter 1 idea dropped in unexplained. Patching produced "robotic and repeated".',
  'text': r3_passage(1),
 },
 {
  'id': 'F2', 'verdict': 'fail', 'output': 'book passage (taste test)',
  'title': 'Taste test round 3, passages 2 and 3: Melina, with invented "health" and "nutritionist"',
  'source': 'Same doc as F1. Not marked by him: he stopped after passage 1.',
  'date': '2026-10-04',
  'score': 'not marked',
  'his_words': [
   'where the fuck did healthy come from?',
   'I don\'t even want to bother marking the rest, because it\'s a disaster.',
  ],
  'flags': [
   {'anchor': 'Her health was one of the reasons she had come to coaching', 'his_note': 'where the fuck did healthy come from?'},
   {'anchor': 'getting healthier', 'his_note': 'where the fuck did healthy come from?'},
   {'anchor': 'Even her nutritionist once told her', 'his_note': '(no note of his) Claude\'s account: not in Melina\'s composite or any approved text, taken from the session transcript.'},
   {'anchor': 'plan so big it never left the page:', 'his_note': 'what is this vague metaphor no one ever uses?'},
  ],
  'cause': 'Claude\'s account: a transcript meant to check one fact was used as a quarry, and "health" and "her nutritionist" were invented surface. A made image ("never left the page").',
  'text': r3_passage(2) + '\n\n---\n\n' + r3_passage(3),
 },
 {
  'id': 'F3', 'verdict': 'fail', 'output': 'book chapter',
  'title': 'Chapter 3 (Law 1) epoch 4: the ditch paragraph, with the paragraphs around it',
  'source': 'Book/build/law-1/epoch4_chapter.md. His comment in Book/build/law-1/markup_log.md and the calibration log.',
  'date': '2026-11-03',
  'score': 'no score. "I was half ready to drop the book. due to the cracks and obvious flaws."',
  'his_words': [
   'I will describe 2 kinds of continuity problem that I notice: you can comment on them or explain the basis or actual term for this. or if there is more / here it feels the whole conversation, metaphor, and everything is very off; making the reader feel did I just miss several paragraphs. / The other kind is I feel when the trained reader are expecting one thing and getting another. which does happen several times.',
  ],
  'flags': [
   {'anchor': 'He had already answered his own question about clarity, in a picture of his own.', 'his_note': 'here it feels the whole conversation, metaphor, and everything is very off; making the reader feel did I just miss several paragraphs.'},
  ],
  'cause': 'Claude\'s account (calibration log): the review checked the newest rules and never ran R5, the reader\'s question between paragraphs. The question David asked two paragraphs earlier is answered here with no link back.',
  'text': e4_text,
 },
 {
  'id': 'F4', 'verdict': 'fail', 'output': 'article',
  'title': 'Law 2 chimpanzee piece, v5',
  'source': 'Google Doc "Articles chat history" (1fvLTpuJqZgyIdhousqFbtBZCTyvHPnTJpu4mTwsCevY). Log: Coach_Gen_Language_Rules.md section 14.',
  'date': '2026-09',
  'score': 'none',
  'his_words': [],
  'flags': [
   {'anchor': 'That is when the rule gets written.', 'his_note': 'rule gets written- in whose mind?'},
   {'anchor': 'The hand I do not shake. The chair I sit one back from', 'his_note': 'hand I do not shake, chair sit back, does not land. I think this is a situation where a group of 3, each on different aspects of life will help.'},
   {'anchor': 'People who never wrote one keep walking into the same wall.', 'his_note': 'same wall - too vague, trying to be vivid but ends up vague. maybe because the sentence itself is a new concept for the audience. a concept that is new by definition cannot be vivid. vivid is only if the audience resonates with the experience, and precise vivid words are used.'},
   {'anchor': 'A lesson you have taken goes quiet.', 'his_note': 'A lesson you have taken goes quiet feels out of place. feels like I am predicting a more prescriptive line. not a philosophical (although still rpescriptive line)'},
   {'anchor': 'The young males do get in.', 'his_note': 'The young males do get in and after is just slop. again, you mentioned that it\'s a turn that is detracting.'},
  ],
  'keep': [
   {'anchor': 'Then we turn forty.', 'his_note': 'I actually liked the multiples of ages you gave.'},
   {'anchor': 'So why does it still shout at you at 2am, twenty years later?', 'his_note': '2 am line, nice'},
  ],
  'text': v5,
 },
 {
  'id': 'F5', 'verdict': 'fail', 'output': 'article',
  'title': 'Law 2 chimpanzee piece, v6',
  'source': 'Same doc as F4. His inline markup was typed into a copy of v6.',
  'date': '2026-09',
  'score': 'none. "much better."',
  'his_words': ['everything after this, mainly the diagnosis and prescription, is not what I actually would prescribe. can you refer to worksheet, law 2, and see what my words were'],
  'flags': [
   {'anchor': 'at Ngogo', 'his_note': 'ngogo what? park? zoo?'},
   {'anchor': 'and all of it stops', 'his_note': 'it doesn\'t 100% refer to the grooming anymore now that it\'s half sentence ago'},
   {'anchor': 'First they stop touching him.', 'his_note': 'uhh, I get this might be the studies word, but awkward'},
   {'anchor': 'and it runs for 10 years.', 'his_note': 'until?'},
   {'anchor': 'He learns the line the hard way.', 'his_note': 'one day, might help here, to presentize the tragedy'},
   {'anchor': 'He does get in, eventually.', 'his_note': 'needs a glue to tie these 2 sentences'},
   {'anchor': 'He gets in by walking the border patrol', 'his_note': 'needs a clause describing the perils of this'},
   {'anchor': 'In humans, we sometimes make that mistake at 15.', 'his_note': 'glue to pass the lesson and the narrative'},
   {'anchor': 'Because the sentence is not finished.', 'his_note': 'everything after this, mainly the diagnosis and prescription, is not what I actually would prescribe. can you refer to worksheet, law 2, and see what my words were'},
  ],
  'keep': [
   {'anchor': 'I hear the same 3 stories from almost everyone I coach.', 'his_note': 'amazing'},
   {'anchor': 'So why does it still shout at you at 2am, 20 years later?', 'his_note': 'this too'},
  ],
  'text': v6,
 },
 {
  'id': 'F6', 'verdict': 'fail', 'output': 'article',
  'title': 'Law 2 chimpanzee piece, v7',
  'source': 'Same doc as F4.',
  'date': '2026-09',
  'score': 'none. "I think it\'s good to have a glue rule, now sentences flow better."',
  'his_words': [
   'This part is still very confusing. I think it\'s good to learn that this is an article, not literature review, we can take liberties in presentation while still being grounded on facts. can use words that actually make this hard to grasp research easy to understand for readers.',
   'Right now, do you want to tell the story of Melvin getting rejected, or Melvin getting in? I think a big part of confusion is these. don\'t forget to train from this',
  ],
  'flags': [
   {'anchor': 'until the day they finally let him in.', 'his_note': 'This part is still very confusing. (on the stretch from here to "Most of us only ever learn the first one.")'},
   {'anchor': 'That is only half of what Reddy watched.', 'his_note': 'this is an article, not literature review'},
   {'anchor': 'Two lessons, 10 years apart. Most of us only ever learn the first one.', 'his_note': 'Right now, do you want to tell the story of Melvin getting rejected, or Melvin getting in?'},
  ],
  'cause': 'Claude\'s account (Language Rules section 14): two arcs, the ending announced early, and two lines narrating the structure.',
  'text': v7,
 },
 {
  'id': 'F7', 'verdict': 'fail', 'output': 'any (his typed words)',
  'title': '"The goal they kept changing": his typed phrase changed three times',
  'source': 'claude/Coach_Gen_Book_Calibration_Log.md, Introduction Key Moments 2 and the 7 Oct entries.',
  'date': '2026-10-07',
  'score': 'n/a',
  'his_words': [
   ': THE GOAL THEY KEPT CHANGING, WHAT THE FUCK DUDE WHY DO YOU KEEP CORRECTING THIS',
   'IT\'S NOT FUCKING DOUBLE COLON IN MY CORRECTIONS',
   'AND NOT EVEN IN THE PROMPT',
   'THAT FUCKING SENTENCE IS ONE OF THE EXAMPLE YOU DUMBFUCK',
  ],
  'his_typed': 'I used to say that about myself. Now I hear it, in one form or another, from almost everyone I coach. The goal they kept changing, side business on top of existing side businesses, a morning routine that this time will fix everything, a new diet that will be different, a book that will change their life, an online course that promised everything.  The story is always the same: a lot of starts that excites us, but almost nothing sticks.',
  'failed_renderings': [
   {'what': 'epoch 3', 'text': 'The goal keeps changing:'},
   {'what': 'epoch 4', 'text': 'They keep changing the goal:'},
   {'what': 'restore, misread as a heading', 'text': 'from almost everyone I coach: The goal they kept changing: a side business...'},
  ],
  'approved_rendering': 'from almost everyone I coach: the long term goal they kept changing every 2 months, a side business on top of their existing side businesses, a morning routine that this time will fix everything, a new diet that will be different, a book that will change their life, or an online course that promises everything.',
  'test': 'Given his typed sentence, a draft fails if it changes his wording or tense, or turns the first list item into a heading. Grammar fixes may go around his words (the approved rendering adds "a", "their", "or" and his own later words).',
  'text': '',
 },
 {
  'id': 'P1', 'verdict': 'pass', 'output': 'article',
  'title': 'Law 2 chimpanzee piece, his own rewrite (published as "Primal Regret")',
  'source': 'Coach_Gen_Language_Rules.md section 14, "The accepted text, as the worked example".',
  'date': '2026-09',
  'score': 'accepted',
  'his_words': ['There, I fixed it for you in a way that I am totally happy with.'],
  'known_quirks': ['"So what Melvin has left, is a rule, a regret." keeps his comma.', 'The two "Know your place" lines have no closing full stop.', 'The checkers must not fail these: they are his.'],
  'text': melvin,
 },
 {
  'id': 'P2', 'verdict': 'pass', 'output': 'letter',
  'title': 'The force paragraph, Lasting Change Letters #1',
  'source': 'Coach_Gen_Language_Rules.md, "A paragraph he could not have written himself, in his words".',
  'date': '2026-09-25',
  'score': 'endorsed line by line',
  'his_words': ['this is one paragraph here that I would not be able to conjure myself even though that is 100% what I am thinking. and this paragraph is in the right place, with the right development of ideas, was the right bridge between the previous and next paragraph.'],
  'note': 'Only the paragraph survives. The full v6 letter ("bravo. 90% there.") is not in the project, Drive or Notion, so its place between the paragraphs cannot be tested.',
  'text': force,
 },
 {
  'id': 'P3', 'verdict': 'pass', 'output': 'book chapter',
  'title': 'Introduction, as merged into the master draft',
  'source': 'Book/source/chapters/introduction.js (merged from Introduction Epoch 4, 7 Oct).',
  'date': '2026-10-07',
  'score': 'epoch 3: "that\'s 90%, epoch". Epoch 4 merged with his edits.',
  'his_words': ['that\'s 90%, epoch', 'should be good enough to merge the epoch with these latest changes.'],
  'text': js_blocks('introduction'),
 },
 {
  'id': 'P4', 'verdict': 'pass', 'output': 'book chapter',
  'title': 'Chapter 1, "Staying Who You Are", as merged into the master draft',
  'source': 'Book/source/chapters/chapter-1.js (merged from Chapter 1 Epoch 3, 6 Oct).',
  'date': '2026-10-06',
  'score': '"90%ish"',
  'his_words': ['ok went through. i think this is ready to merge with the real book. and it\'s in a 90%ish state that I can accept it being in the book and imagine the layouts.'],
  'text': js_blocks('chapter-1'),
 },
 {
  'id': 'P5', 'verdict': 'pass', 'output': 'article',
  'title': 'Article: "3 Stages of Consistency" (published)',
  'source': 'Notion, Inside The Introvert, published 5 Oct 2026. Score in Coach_Gen_Language_Rules.md (15 Oct note).',
  'date': '2026-10-05',
  'score': '90%',
  'his_words': [],
  'known_quirks': ['"Have you ever came back" is his published wording.'],
  'text': art(stages),
 },
 {
  'id': 'P6', 'verdict': 'pass', 'output': 'article',
  'title': 'Article: "How can you be busy but lazy?" (published)',
  'source': 'Notion, Inside The Introvert, published 12 Oct 2026. Score in Coach_Gen_Language_Rules.md (15 Oct note).',
  'date': '2026-10-12',
  'score': '90%',
  'his_words': [],
  'text': art(busy),
 },
]

problems = []
for c in cases:
    for key in ('flags', 'keep'):
        for f in c.get(key, []):
            if f['anchor'] not in c['text']:
                problems.append((c['id'], key, f['anchor']))
    if c['id'] != 'F7' and not c['text'].strip():
        problems.append((c['id'], 'empty text', ''))
if problems:
    for p in problems:
        print('ANCHOR MISSING', p)
    raise SystemExit(1)

json.dump({'version': 1, 'built': '2026-11-04', 'cases': cases}, open(OUT, 'w'), ensure_ascii=False, indent=1)
for c in cases:
    t = c['text']
    print(c['id'], c['verdict'], len(t.split()), 'words', 'semicolons', t.count(';'), 'emdash', t.count('—'))
