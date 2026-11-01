#!/bin/bash
# Push a load file to its own throwaway branch, so book text never enters main.
# Usage: tools/push_load.sh loads/<name>.json
# Prints the SQL to run. After the load, run tools/drop_load.sh <name>.
set -e
f="$1"; name=$(basename "$f" .json); br="load-$name"
[ -f "$f" ] || { echo "no file $f"; exit 1; }
git checkout -q main
git checkout -q -b "$br"
git add -f "$f"
git commit -q -m "Temporary load file $name (branch is deleted after the load)"
git push -q -u origin "$br" 2>&1 | grep -v -e 'remote:' || true
git checkout -q main
echo "select * from brain.load_from_github('$f', '$br');"
