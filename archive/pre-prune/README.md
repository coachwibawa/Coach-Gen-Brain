# pre-prune archive (4 Nov 2026)

Snapshot of every rule doc, project doc, skill and memory file before the rules refactor. Nothing here is edited. Restore from this tag if a prune goes wrong: `git checkout pre-prune -- archive/pre-prune`.

- `project-docs/`: all 85 project docs at their project paths. 81 text docs are byte for byte as `project_read` returned them. The 4 `.docx` docs could only be read as text, so they are saved as `*.docx.txt-extract.md` (text conversion, not the original binaries, which are not reachable from here).
- `skills/`: every `/mnt/skills/plugins/*` folder plus `manifest.json`. `write-book-from-material` is no longer on disk, so `write-book-from-material_SKILL.md.from-transcript` is its text as read earlier in the session.
- `memory/`: 39 memory files (account level and the Project subtree), as the memory tool returned them, without its header line.
- `MANIFEST.md5`: md5 of every file here. Check with `md5sum -c MANIFEST.md5` from this folder.
