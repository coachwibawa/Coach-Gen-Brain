# Book settings

One JSON file per book, no book text inside. Read by `tools/parse_book.py`.

Steps for a new book:
1. `python3 tools/parse_book.py book.pdf --profile` and read the report.
2. Write `books/<name>.json` from it.
3. `python3 tools/parse_book.py book.pdf books/<name>.json turns.json`. Read the checks and only the pages listed under PAGES TO LOOK AT.
4. `python3 tools/build_load.py turns.json loads/<name>.json meta.json`, then the GitHub load route.

Keys (all optional except `keep_pages` and `styles`):

| Key | Meaning |
|---|---|
| `keep_pages` | Pages to read, such as `"8-201,204-210"` |
| `skip_pages` | Pages to remove from that range |
| `styles` | Map of `"Font size"` to a role: `body`, `heading`, `chapter`, `part`, `figure`, `skip`. Names come from the profile report. An italic style with no entry falls back to the same style without italic. |
| `chapters` | List of `[pdf page, "Chapter label"]`. Lines in a `chapter` role at the top of that page become one heading. |
| `parts` | Pages that are part dividers. The whole page becomes one heading, filed under the next chapter. |
| `chapter_line_re` | Regex for a chapter line on a chapter page that has body type (for example `^Chapter \d$`) |
| `front_label` | Chapter label before the first chapter page |
| `drop_lines` | Regexes for lines to remove (rules of underscores, stray page numbers) |
| `speakers` | Map of a line prefix to a speaker, for dialogue books. The prefix is cut from the text and put in `sp`. |
| `paragraph_by` | `auto` (default), `indent` or `gap` |
| `indent` | Points of first-line indent that start a paragraph. Default 4. |
| `keep_running` | `true` keeps repeated headers and footers instead of removing them |
