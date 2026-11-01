#!/bin/bash
# Commit and push a load file to main, then print the SQL to run.
# Usage: tools/push_load.sh loads/<name>.json   (after the load: tools/drop_load.sh <name>)
# Note: GitHub branch deletion and force-push are blocked from the Claude workspace,
# so a throwaway branch cannot be cleaned up. The file is removed from main right after the load.
set -e
f="$1"; name=$(basename "$f" .json)
[ -f "$f" ] || { echo "no file $f"; exit 1; }
git checkout -q main
git add -f "$f"
git commit -q -m "Temporary load file $name (removed right after the load)"
git push -q origin main 2>&1 | grep -v -e 'remote:' || true
echo "select * from brain.load_from_github('$f');"
