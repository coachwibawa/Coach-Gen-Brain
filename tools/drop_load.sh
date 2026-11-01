#!/bin/bash
# Remove a load file from main after the load and push.
# Usage: tools/drop_load.sh <name>
set -e
name="$1"; f="loads/$name.json"
git checkout -q main
git rm -q --cached "$f" 2>/dev/null || git rm -q "$f"
rm -f "$f"
git commit -q -m "Remove load file $name after load (copyrighted text)"
git push -q origin main 2>&1 | grep -v -e 'remote:' || true
git ls-tree -r HEAD --name-only | grep -c '^loads/' | sed 's/^/load files left on main: /'
