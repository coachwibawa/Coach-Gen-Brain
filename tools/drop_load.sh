#!/bin/bash
# Delete the throwaway load branch on GitHub and locally, and the local load file.
# Usage: tools/drop_load.sh <name>
set -e
name="$1"; br="load-$name"
git push -q origin --delete "$br" 2>&1 | grep -v -e 'remote:' || true
git branch -q -D "$br" 2>/dev/null || true
rm -f "loads/$name.json"
git ls-remote --heads origin "$br" | grep -q . && echo "BRANCH STILL ON GITHUB" || echo "branch $br gone"
