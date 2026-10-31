"""Re-run a book through the parser and compare with its regression key.
Usage: python3 tests/check_expected.py book.pdf books/<name>.json tests/expected/<name>.json
Needs the PDF again, because the repo holds no book text."""
import json, sys, subprocess, tempfile, os, hashlib
pdf, cfg, exp = sys.argv[1:4]
out = os.path.join(tempfile.mkdtemp(), 'turns.json')
subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), '..', 'tools', 'parse_book.py'), pdf, cfg, out], check=True, capture_output=True)
t = json.load(open(out)); e = json.load(open(exp))
got = {'turns': len(t), 'words': sum(len(x['t'].split()) for x in t),
       'all_md5': hashlib.md5('\n'.join(x['t'] for x in t).encode()).hexdigest()}
bad = {k: (got[k], e[k]) for k in got if got[k] != e[k]}
print('PASS' if not bad else f'FAIL {bad}')
sys.exit(1 if bad else 0)
