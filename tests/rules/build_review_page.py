import json
S = '/tmp/claude-0/-home-claude/20a7e8bf-877e-5974-b3fa-8df9b03d18a9/scratchpad'
ts = json.load(open(f'{S}/test_set_v2.json'))
exec(open(f'{S}/build_review_doc.py').read().split("CTX = {")[0].split("ts = json.load")[0])  # imports only
ctx_src = open(f'{S}/build_review_doc.py').read()
CTX = eval('{' + ctx_src.split('CTX = {', 1)[1].split('\n}\n', 1)[0] + '\n}')
cases = []
for c in ts['cases']:
    d = {k: c.get(k) for k in ('id', 'verdict', 'title', 'date', 'score', 'his_words', 'flags', 'keep', 'text', 'his_typed', 'failed_renderings', 'approved_rendering')}
    d['context'] = CTX[c['id']]
    d['part'] = 'A' if c['verdict'] == 'fail' else ('C' if c['id'] in ('P7', 'P8', 'P9', 'P10') else 'B')
    cases.append(d)
data = json.dumps(cases, ensure_ascii=False).replace('</', '<\\/')

page = r'''<title>Rule Test Set Review</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Work+Sans:wght@400;500;600&display=swap">
<style>
/* Layout: a single manuscript column, each passage a marked-up page with a verdict strip under it */
:root{
 --paper:#f6f7f9; --sheet:#ffffff; --ink:#1b2430; --muted:#5b6676; --rule:#d9dee6;
 --pen:#c2272d; --penbg:#fbe4e4; --keep:#1f7a4d; --keepbg:#dcf1e5; --accent:#2a6fb0;
 --serif:"Libre Baskerville",Georgia,"Times New Roman",serif;
 --sans:"Work Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
 --paper:#11161d; --sheet:#18202a; --ink:#e4e9f0; --muted:#9aa6b6; --rule:#2c3644;
 --pen:#ff7a7f; --penbg:#4a1f24; --keep:#6fd3a0; --keepbg:#173a2a; --accent:#7fb4e8; color-scheme:dark}}
:root[data-theme="dark"]{
 --paper:#11161d; --sheet:#18202a; --ink:#e4e9f0; --muted:#9aa6b6; --rule:#2c3644;
 --pen:#ff7a7f; --penbg:#4a1f24; --keep:#6fd3a0; --keepbg:#173a2a; --accent:#7fb4e8; color-scheme:dark}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.55;
 padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:24px 64px}
.wrap{max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:28px}
h1{font-family:var(--serif);font-size:1.9rem;line-height:1.2;margin:0;text-wrap:balance}
h2{font-family:var(--serif);font-size:1.3rem;margin:0;text-wrap:balance}
h3{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0;font-weight:600}
p{margin:0}
.lede{display:flex;flex-direction:column;gap:10px;color:var(--muted)}
.lede b{color:var(--ink)}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--paper);padding-block:10px;border-bottom:1px solid var(--rule);display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;font-size:.9rem}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--paper)}
.bar strong{font-variant-numeric:tabular-nums}
.status{color:var(--muted)}
.part{display:flex;flex-direction:column;gap:6px;padding-top:12px}
.part p{color:var(--muted)}
.case{background:var(--sheet);border:1px solid var(--rule);border-radius:6px;padding:20px;display:flex;flex-direction:column;gap:14px;min-width:0}
.head{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.tag{font-size:.75rem;font-weight:600;letter-spacing:.06em;padding:2px 8px;border-radius:99px}
.tag.fail{background:var(--penbg);color:var(--pen)} .tag.pass{background:var(--keepbg);color:var(--keep)}
.ctx{color:var(--muted);font-size:.92rem}
ul{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:6px}
.said li{font-family:var(--serif);font-style:italic;font-size:.95rem}
.notes li{font-size:.92rem}
.notes .q{font-family:var(--serif)}
.notes .n{color:var(--pen)} .notes.keep .n{color:var(--keep)}
.passage{font-family:var(--serif);font-size:1rem;line-height:1.75;border-top:1px solid var(--rule);padding-top:14px;display:flex;flex-direction:column;gap:12px;overflow-wrap:anywhere}
.passage h4{font-family:var(--sans);font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:6px 0 0}
.sep{font-family:var(--sans);font-size:.8rem;color:var(--muted);text-align:center}
mark.fl{background:var(--penbg);color:inherit;text-decoration:underline wavy var(--pen);text-underline-offset:4px;padding:0 1px}
mark.kp{background:var(--keepbg);color:inherit;padding:0 1px}
.verdict{border-top:1px dashed var(--rule);padding-top:14px;display:flex;flex-direction:column;gap:10px}
.choices{display:flex;flex-wrap:wrap;gap:8px}
.choices label{display:flex;align-items:center;gap:6px;border:1px solid var(--rule);border-radius:99px;padding:6px 12px;cursor:pointer;font-size:.9rem}
.choices input{accent-color:var(--accent)}
.choices label:has(input:checked){border-color:var(--accent);color:var(--accent);font-weight:600}
.choices label:focus-within{outline:2px solid var(--accent);outline-offset:2px}
textarea{width:100%;box-sizing:border-box;min-height:64px;font:inherit;color:var(--ink);background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:8px 10px;resize:vertical}
textarea:focus{outline:2px solid var(--accent);outline-offset:1px}
.saved{font-size:.8rem;color:var(--muted);min-height:1.2em}
.typed{font-family:var(--serif);background:var(--paper);border-radius:6px;padding:10px 12px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
<div class="wrap">
 <header class="lede">
  <h1>Rule Test Set Review</h1>
  <p>These passages become the exam for the new rules. The checker has to catch every problem in the passages you rejected and leave the ones you approved alone. A wrong verdict here trains the checker wrong, so judge each one by today's standard, the book, and not by the day you scored it.</p>
  <p><b>Red, wavy underline:</b> a line you flagged. <b>Green:</b> a line you liked. Pick one option under each passage. Your picks save as you go, and I read them from here.</p>
 </header>
 <div class="bar"><span><strong id="done">0</strong> of <strong id="total">0</strong> judged</span><span class="status" id="status">Connecting…</span></div>
 <main id="list" class="wrap" style="gap:24px"></main>
</div>
<script id="cases" type="application/json">''' + data + r'''</script>
<script>
const CASES = JSON.parse(document.getElementById('cases').textContent);
const PARTS = {
 A:['Part A. Drafts you rejected','Do they still fail?'],
 B:['Part B. Passages you approved before the book standard','Do they still pass?'],
 C:['Part C. Recent passages you liked','Add them as pass cases?']};
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function markUp(text, c){
  let h = esc(text);
  const marks = [...(c.flags||[]).map(f=>[f.anchor,'fl']), ...(c.keep||[]).map(f=>[f.anchor,'kp'])];
  for (const [a, cls] of marks){ const e = esc(a); const i = h.indexOf(e); if (i>=0) h = h.slice(0,i)+`<mark class="${cls}">`+e+'</mark>'+h.slice(i+e.length); }
  return h.split(/\n\s*\n/).map(p => {
    p = p.trim();
    if (p === '---') return '<p class="sep">next passage</p>';
    if (p.startsWith('## ')){ const [first,...rest] = p.split('\n'); return `<h4>${first.slice(3)}</h4>` + rest.map(r=>`<p>${r}</p>`).join(''); }
    return '<p>' + p.replace(/\*\*(.+?)\*\*/g,'<b>$1</b>').replace(/\n/g,'<br>') + '</p>';
  }).join('');
}
function options(c){
  const keep = c.part==='A' ? 'Still fails' : c.part==='B' ? 'Still passes' : 'Add as pass';
  const flip = c.part==='A' ? 'Now passes' : c.part==='B' ? 'Now fails' : 'Use as fail';
  return [['keep',keep],['flip',flip],['drop','Leave out of the test']];
}
const list = document.getElementById('list');
let lastPart = '';
for (const c of CASES){
  if (c.part !== lastPart){ lastPart = c.part; const s = document.createElement('section'); s.className='part'; s.innerHTML = `<h2>${PARTS[c.part][0]}</h2><p>${PARTS[c.part][1]}</p>`; list.appendChild(s); }
  const el = document.createElement('article'); el.className='case'; el.id = 'case-'+c.id;
  let body = `<div class="head"><span class="tag ${c.verdict}">${c.id}</span><h2>${esc(c.title)}</h2></div>
   <p class="ctx">${esc(c.context)} ${esc(c.date)}. Score then: ${esc(c.score)}.</p>`;
  if (c.his_words && c.his_words.length) body += `<div><h3>What you said then</h3><ul class="said">${c.his_words.map(w=>`<li>“${esc(w)}”</li>`).join('')}</ul></div>`;
  if (c.flags && c.flags.length) body += `<div><h3>Lines you flagged</h3><ul class="notes">${c.flags.map(f=>`<li><span class="q">“${esc(f.anchor)}”</span> <span class="n">${esc(f.his_note)}</span></li>`).join('')}</ul></div>`;
  if (c.keep && c.keep.length) body += `<div><h3>Lines you liked</h3><ul class="notes keep">${c.keep.map(f=>`<li><span class="q">“${esc(f.anchor)}”</span> <span class="n">${esc(f.his_note)}</span></li>`).join('')}</ul></div>`;
  if (c.id === 'F7'){
    body += `<div class="passage"><h4>What you typed</h4><p class="typed">${esc(c.his_typed)}</p><h4>My three wrong versions</h4>${c.failed_renderings.map(r=>`<p><mark class="fl">${esc(r.text)}</mark> (${esc(r.what)})</p>`).join('')}<h4>What went into the book</h4><p>${esc(c.approved_rendering)}</p></div>`;
  } else body += `<div class="passage">${markUp(c.text, c)}</div>`;
  body += `<div class="verdict"><h3>Your call</h3><div class="choices" role="radiogroup">${options(c).map(([v,l])=>`<label><input type="radio" name="v-${c.id}" id="v-${c.id}-${v}" value="${v}"> ${l}</label>`).join('')}</div>
   <textarea id="why-${c.id}" placeholder="Why, in a few words (optional)"></textarea><p class="saved" id="saved-${c.id}"></p></div>`;
  el.innerHTML = body; list.appendChild(el);
}
document.getElementById('total').textContent = CASES.length;
const state = {};
function count(){ document.getElementById('done').textContent = Object.values(state).filter(s=>s&&s.call).length; }
(async () => {
  const st = document.getElementById('status');
  let db = null;
  try { db = await claude.use('db'); } catch(e) {}
  if (!db){ st.textContent = 'Saving is unavailable in this view. Open the page signed in to claude.ai.'; return; }
  const timer = setTimeout(()=>{ st.textContent = 'Still loading your picks…'; }, 10000);
  db.collection('verdicts').onSnapshot(snap => {
    clearTimeout(timer); st.textContent = 'Picks save as you go.';
    for (const d of snap.docs){ const v = d.data(); state[d.id] = v;
      const r = document.getElementById(`v-${d.id}-${v.call}`); if (r && !r.checked) r.checked = true;
      const t = document.getElementById('why-'+d.id); if (t && document.activeElement !== t && v.why !== undefined) t.value = v.why; }
    count();
  }, err => { clearTimeout(timer); st.textContent = 'Could not load saved picks. Reload the page to try again.'; });
  const pending = {};
  async function save(id){
    const call = (document.querySelector(`input[name="v-${id}"]:checked`)||{}).value || '';
    const why = document.getElementById('why-'+id).value;
    const msg = document.getElementById('saved-'+id);
    if (pending[id]) return; pending[id] = true;
    try { await db.doc('verdicts/'+id).set({call, why, at: new Date().toISOString()}); msg.textContent = 'Saved.'; state[id] = {call, why}; count(); }
    catch(e){ msg.textContent = 'Not saved. ' + (e && e.message ? e.message : 'Try again.'); }
    finally { pending[id] = false; }
  }
  for (const c of CASES){
    document.querySelectorAll(`input[name="v-${c.id}"]`).forEach(r => r.addEventListener('change', ()=>save(c.id)));
    let t; document.getElementById('why-'+c.id).addEventListener('input', ()=>{ clearTimeout(t); t = setTimeout(()=>save(c.id), 800); });
  }
})();
</script>
'''
open(f'{S}/rule_test_review.html', 'w').write(page)
print(len(page))
