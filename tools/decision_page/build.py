#!/usr/bin/env python3
"""Build a decision page: one card per decision, equal options, a notes box,
picks saved to the artifact's db (collection named in the spec).

Usage: python3 tools/decision_page/build.py SPEC.json OUT.html

Spec (JSON):
  title, description, intro: [paragraphs], collection
  sections: [{title, sub, cards: [card]}]
  card: {id, title, kind?, context?, said?: [his words],
         rows?: [[label, text]], items?: [text], start?: first item number,
         options: [[value, label]], placeholder?}
Numbering runs on through the whole page and never repeats: a card with
items shows the range of its items as its tag, a card without items shows its
own number. The script checks the run is continuous and that no visible text
holds an em dash or a semicolon. Publish OUT.html with the Artifact tool and
capabilities {"db": {}, "user": {}}. Read picks back with ArtifactData list.
"""
import html, json, sys
from pathlib import Path

spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
out = Path(sys.argv[2])

# continuous numbering check
n = 0
errors = []
for s in spec["sections"]:
    for c in s["cards"]:
        if c.get("items"):
            start = c.get("start", n + 1)
            if start != n + 1:
                errors.append(f"card {c['id']}: items start at {start}, expected {n + 1}")
            c["start"] = start
            n = start + len(c["items"]) - 1
            c["tag"] = f"{start} to {n}" if len(c["items"]) > 1 else str(start)
        else:
            n += 1
            if str(c["id"]) != str(n):
                errors.append(f"card {c['id']}: expected number {n}")
            c["tag"] = str(n)


def walk(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, list):
        for x in o:
            yield from walk(x)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in ("collection",):
                yield from walk(v)


for t in walk(spec):
    if "—" in t or ";" in t:
        errors.append(f"em dash or semicolon in: {t[:70]}")
if errors:
    sys.exit("\n".join(errors))

data = json.dumps(spec, ensure_ascii=False).replace("</", "<\\/")
e = html.escape
intro = "".join(f"<p>{e(p)}</p>" for p in spec["intro"])

page = f'''<title>{e(spec["title"])}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Work+Sans:wght@400;500;600&display=swap">
''' + r'''<style>
/* Layout: one reading column, each decision a sheet with its verdict strip at the foot */
:root{
 --paper:#f6f7f9; --sheet:#ffffff; --ink:#1b2430; --muted:#5b6676; --rule:#d9dee6;
 --accent:#2a6fb0; --accentbg:#e3eef9; --call:#8a5a00; --callbg:#f8ecd2; --cut:#a8323a; --cutbg:#f9e3e4; --ok:#1f7a4d; --okbg:#dcf1e5;
 --serif:"Libre Baskerville",Georgia,"Times New Roman",serif;
 --sans:"Work Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
 --paper:#11161d; --sheet:#18202a; --ink:#e4e9f0; --muted:#9aa6b6; --rule:#2c3644;
 --accent:#7fb4e8; --accentbg:#1c2f45; --call:#f0c26b; --callbg:#3d2f12; --cut:#ff8a90; --cutbg:#45212a; --ok:#6fd3a0; --okbg:#173a2a; color-scheme:dark}}
:root[data-theme="dark"]{
 --paper:#11161d; --sheet:#18202a; --ink:#e4e9f0; --muted:#9aa6b6; --rule:#2c3644;
 --accent:#7fb4e8; --accentbg:#1c2f45; --call:#f0c26b; --callbg:#3d2f12; --cut:#ff8a90; --cutbg:#45212a; --ok:#6fd3a0; --okbg:#173a2a; color-scheme:dark}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.55;
 padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:24px 64px}
.wrap{max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:28px}
h1{font-family:var(--serif);font-size:1.9rem;line-height:1.2;margin:0;text-wrap:balance}
h2{font-family:var(--serif);font-size:1.3rem;line-height:1.3;margin:0;text-wrap:balance}
h3{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0;font-weight:600}
p{margin:0}
.lede{display:flex;flex-direction:column;gap:10px;color:var(--muted)}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--paper);padding-block:10px;border-bottom:1px solid var(--rule);display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;font-size:.9rem}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--paper)}
.bar strong{font-variant-numeric:tabular-nums}
.status{color:var(--muted)}
.part{display:flex;flex-direction:column;gap:6px;padding-top:12px}
.part p{color:var(--muted)}
.card{background:var(--sheet);border:1px solid var(--rule);border-radius:6px;padding:20px;display:flex;flex-direction:column;gap:14px;min-width:0;scroll-margin-top:64px}
.head{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.tag{font-size:.75rem;font-weight:600;letter-spacing:.04em;padding:2px 9px;border-radius:99px;font-variant-numeric:tabular-nums;white-space:nowrap;background:var(--accentbg);color:var(--accent)}
.tag.call{background:var(--callbg);color:var(--call)} .tag.change{background:var(--cutbg);color:var(--cut)} .tag.settled{background:var(--okbg);color:var(--ok)}
.ctx{color:var(--muted);font-size:.95rem}
.said{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:6px}
.said li{font-family:var(--serif);font-style:italic;font-size:.95rem}
.rows{display:grid;grid-template-columns:max-content 1fr;gap:8px 14px;margin:0}
.rows dt{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600;padding-top:3px}
.rows dd{margin:0;font-family:var(--serif);min-width:0}
@media (max-width:480px){.rows{grid-template-columns:1fr}.rows dd{margin-bottom:6px}}
ol.items{margin:0;padding-left:2.4em;display:flex;flex-direction:column;gap:8px;font-family:var(--serif)}
ol.items li::marker{font-family:var(--sans);font-variant-numeric:tabular-nums;color:var(--muted);font-size:.9em}
.verdict{border-top:1px dashed var(--rule);padding-top:14px;display:flex;flex-direction:column;gap:10px}
.choices{display:flex;flex-direction:column;gap:8px}
.choices label{display:flex;align-items:flex-start;gap:8px;border:1px solid var(--rule);border-radius:12px;padding:8px 12px;cursor:pointer;font-size:.95rem}
.choices input{accent-color:var(--accent);margin-top:4px}
.choices label:has(input:checked){border-color:var(--accent);color:var(--accent);font-weight:600}
.choices label:focus-within{outline:2px solid var(--accent);outline-offset:2px}
textarea{width:100%;box-sizing:border-box;min-height:56px;font:inherit;color:var(--ink);background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:8px 10px;resize:vertical}
textarea:focus{outline:2px solid var(--accent);outline-offset:1px}
.saved{font-size:.8rem;color:var(--muted);min-height:1.2em}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
<div class="wrap">
 <header class="lede">
  <h1>''' + e(spec["title"]) + '''</h1>
  ''' + intro + r'''
 </header>
 <div class="bar"><span><strong id="done">0</strong> of <strong id="total">0</strong> decided</span><span class="status" id="status">Connecting…</span></div>
 <main id="list" class="wrap" style="gap:24px"></main>
</div>
<script id="spec" type="application/json">''' + data + r'''</script>
<script>
const SPEC = JSON.parse(document.getElementById('spec').textContent);
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const list = document.getElementById('list');
const CARDS = [];
for (const s of SPEC.sections){
  const sec = document.createElement('section'); sec.className = 'part';
  sec.innerHTML = `<h2>${esc(s.title)}</h2>` + (s.sub ? `<p>${esc(s.sub)}</p>` : '');
  list.appendChild(sec);
  for (const c of s.cards){
    CARDS.push(c);
    const id = String(c.id);
    const el = document.createElement('article'); el.className = 'card'; el.id = 'd-' + id;
    let b = `<div class="head"><span class="tag ${esc(c.kind||'')}">${esc(c.tag)}</span><h2>${esc(c.title)}</h2></div>`;
    if (c.context) b += `<p class="ctx">${esc(c.context)}</p>`;
    if (c.rows && c.rows.length) b += `<dl class="rows">${c.rows.map(([k,v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join('')}</dl>`;
    if (c.items && c.items.length) b += `<ol class="items" start="${c.start}">${c.items.map(t => `<li>${esc(t)}</li>`).join('')}</ol>`;
    if (c.said && c.said.length) b += `<div><h3>What you said</h3><ul class="said">${c.said.map(w => `<li>“${esc(w)}”</li>`).join('')}</ul></div>`;
    b += `<div class="verdict"><h3>Your call</h3><div class="choices" role="radiogroup" aria-label="${esc(c.title)}">${c.options.map(([v,l]) => `<label><input type="radio" name="v-${id}" id="v-${id}-${esc(v)}" value="${esc(v)}"> <span>${esc(l)}</span></label>`).join('')}</div>
      <textarea id="why-${id}" aria-label="Note for ${esc(c.title)}" placeholder="${esc(c.placeholder || 'Note (optional)')}"></textarea><p class="saved" id="saved-${id}"></p></div>`;
    el.innerHTML = b; list.appendChild(el);
  }
}
document.getElementById('total').textContent = CARDS.length;
const state = {};
function count(){ document.getElementById('done').textContent = Object.values(state).filter(s => s && s.call).length; }
(async () => {
  const st = document.getElementById('status');
  let db = null;
  try { db = await claude.use('db'); } catch (e) {}
  if (!db){ st.textContent = 'Saving is unavailable in this view. Open the page signed in to claude.ai.'; return; }
  const col = SPEC.collection || 'picks';
  const timer = setTimeout(() => { st.textContent = 'Still loading your picks…'; }, 10000);
  db.collection(col).onSnapshot(snap => {
    clearTimeout(timer); st.textContent = 'Picks save as you go.';
    for (const d of snap.docs){ const v = d.data(); state[d.id] = v;
      const r = document.getElementById(`v-${d.id}-${v.call}`); if (r && !r.checked) r.checked = true;
      const t = document.getElementById('why-' + d.id); if (t && document.activeElement !== t && v.why !== undefined) t.value = v.why; }
    count();
  }, err => { clearTimeout(timer); st.textContent = 'Could not load saved picks. Reload the page to try again.'; });
  const busy = {}, again = {};
  async function save(id){
    if (busy[id]){ again[id] = true; return; }
    busy[id] = true;
    const call = (document.querySelector(`input[name="v-${id}"]:checked`) || {}).value || '';
    const why = document.getElementById('why-' + id).value;
    const msg = document.getElementById('saved-' + id);
    try { await db.doc(col + '/' + id).set({call, why, at: new Date().toISOString()}); msg.textContent = 'Saved.'; state[id] = {call, why}; count(); }
    catch (e){ msg.textContent = 'Not saved. ' + (e && e.message ? e.message : 'Try again.'); }
    finally { busy[id] = false; if (again[id]){ again[id] = false; save(id); } }
  }
  for (const c of CARDS){
    const id = String(c.id);
    document.querySelectorAll(`input[name="v-${id}"]`).forEach(r => r.addEventListener('change', () => save(id)));
    let t; document.getElementById('why-' + id).addEventListener('input', () => { clearTimeout(t); t = setTimeout(() => save(id), 800); });
  }
})();
</script>
'''
out.write_text(page, encoding="utf-8")
print(f"ok: {sum(len(s['cards']) for s in spec['sections'])} cards, numbers 1 to {n}, {len(page)} bytes -> {out}")
