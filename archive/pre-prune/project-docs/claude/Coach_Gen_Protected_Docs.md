# Protected Docs

Docs listed here are read-only. Do not write to them.

**Read this before calling `project_write` on anything in this project.**

---

## The list

| Doc | Status | Protected since |
|---|---|---|
| `Coach_Gen_Language_Rules.md` | Read-only | 2026-09-03 |
| `claude/Coach_Gen_Book_Rules.md` | Read-only | 2026-10-05 |
| `claude/Coach_Gen_Social_Posting_Rules.md` | Append-only (see below) | 2026-10-15 |

`claude/Coach_Gen_Book_Rules.md` was added on 5 Oct 2026 at Coach Gen's request ("protect this new rule document too. same level of protection as language rule"). If it were overwritten, the bottom-up Book Rules v2 would be lost: the rules built from the full read of his 5 reference books, each tied to his own words, plus the abandoned v1 kept as raw data. Its master copy lives on his Mac (`Book/Coach_Gen_Book_Rules.md`). The project copy is a mirror and gets the same protection.

`claude/Coach_Gen_Social_Posting_Rules.md` was added on 15 Oct 2026 at Coach Gen's request ("make sure social posting rules is segmented into sites, and also that it has the no delete rule now, since it's getting highly specific and lots of work."). If it were overwritten, the per-site posting rules built run by run with him would be lost: LinkedIn's flex menu, story-to-flex ratio, callback rule, approved posts and calibration log, and Facebook's audience decisions and Indonesian localization log.

---

## The rule

Never call `project_write` on a doc in the list.

Never condense, restructure, reformat, reorder or clean up its content. Never rewrite it to make it comply with a rule it contains.

If you believe a protected doc should change, say so in chat. Show the exact lines you would add or change, and why. Coach Gen decides.

## The one exception

Coach Gen can override in the moment. He has to ask for the specific change, in that turn, in his own words. "Update the language rules" is not enough on its own. Confirm what changes before writing anything.

When he does authorise a write:

1. `project_read` the doc first. Never write from an earlier read.
2. Change only the lines he named. Everything else goes back word for word.
3. Report exactly what changed, in the reply.

Additions and annotations only. `Coach_Gen_Language_Rules.md` carries its own maintenance rule: "Add and annotate. Never condense. When a later finding corrects an earlier rule, keep the old line and mark the correction, so the reasoning survives. A rule you delete is a lesson that has to be learned again from scratch." That rule governs any authorised write.

`claude/Coach_Gen_Book_Rules.md` carries the same kind of rule: "Add and annotate. Never condense. When a later round corrects a rule, keep the old line and mark the correction." It governs any authorised write to that doc. For that doc, edit the master on his Mac first, then upload the same bytes to the project with `local_path`. Never retype it.

## Append-only docs

An append-only doc is not read-only. It grows during normal work, but nothing in it is ever deleted.

- **Allowed:** adding new lines, and adding CORRECTION or annotation lines under existing ones, once Coach Gen has agreed to the exact line (for `claude/Coach_Gen_Social_Posting_Rules.md`, this happens inside `post-to-socials` runs).
- **Never:** deleting, condensing, merging, reordering, reformatting or rewriting an existing line, even to fix it. A wrong line stays, with a CORRECTION line under it.
- **How to write:** never retype the doc. Edit a local copy with exact find-and-insert edits, check the new version still contains every line of the old one, then upload those bytes with `project_write` and `local_path`.
- The doc carries its own no-delete rule at the top. That rule governs every write.

---

## Why this exists

The Projects tool has no patch operation. Editing one line means reading the whole doc and writing the whole doc back. Every write to `Coach_Gen_Language_Rules.md` retypes around 9,000 words, and a line dropped in transit is gone with no diff and no version history to recover it from.

That doc is 14 sections of calibration evidence: ten drafts of one piece, nine rounds of sentence-level ranking, and the verbatim reasons behind every accepted and rejected line. It is the most expensive doc in this project to rebuild and the easiest to damage without anyone noticing.

Claude Projects has no per-document read-only setting. Permissions are project-level, view or edit. This doc is the substitute for one.

---

## What is not protected

`.docx` and `.pdf` items in this project are file uploads. The Projects tool cannot write to them at all, listed here or not.

Text docs, the `.md` and `.js` files, are writable by the tool. Anything writable and not on the list above takes normal edits.

## Adding a doc to the list

Coach Gen adds it. Put the filename in the table, the date, and one line on what would be lost if it were overwritten.
