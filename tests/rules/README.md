# Rule test set (step 5 of the Rules Refactor Plan)

`test_set.json` holds passages with Gen's verdicts. Every text was copied by script from its source (`build_test_set.py`), never retyped.

- **The checker judges the whole passage.** It reads every line, not only the flagged ones, and gives a verdict on the passage as a whole.
- **F cases (fail):** the checker must fail the passage. `flags[]` are the lines Gen marked back then: reminders of what went wrong, and the minimum the checker should also name. It may find other real problems. `keep[]` anchors are lines he praised inside a failed draft, and must not be flagged.
- **P cases (pass):** nothing may fail. `known_quirks` lists his own wording that a checker must leave alone.
- **F7** is a protected-phrase test, not a passage: a draft fails if it changes his typed wording, tense, or turns his first list item into a heading.

`his_words` and `his_note` are his words verbatim. `cause` is Claude's account from the logs, not his.

Gaps: the full Lasting Change Letters #1 v6 ("bravo. 90% there.") is not in the project, Drive or Notion, so P2 is the force paragraph alone. The F4 to F6 drafts carry "Insight 1 —" field headings from the chat log, which are not the failure being tested.
