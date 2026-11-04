---
name: "cite-outside-voices"
description: "Find passages by outside authors (Pressfield and others) to cite next to Coach Gen's own idea. Use whenever drafting or revising a chapter, article, letter, talk or post, or when he asks who else said this."
---

# Cite outside voices

Coach Gen wants to state his own idea and, next to it, show who else said something close, so he can cite them. The brain holds outside books as raw chunks, owned by `outside`, never mixed with his words.

## When to run

- You are about to write or revise a passage that makes a claim, tells a principle or names a Law idea.
- He asks "who else said this", "can I cite someone" or "what does Pressfield say".

Skip it for pure client stories, logistics and anything with no idea to back up.

## How

1. Read `claude/Brain_Rule.md`, sections 7 to 9, if you have not this chat.
2. Turn the idea into one plain sentence, in his words. Short and concrete works best.
3. Run it with `execute_sql` on project `zjedqjiuxkoncwsmylls`:

```sql
select voice, ref, author, source, place, round(similarity::numeric,2) sim, text
from brain.search_voices('<the idea in one sentence>', 'all');
```

   Scope `own` gives only his material. Scope `outside` gives only other authors (top 3, cutoff 0.25). Scope `all` gives both lists.
4. Read the outside rows. Keep a passage only if it makes the same point as his idea. A score between 0.25 and 0.31 is weak. Read the text and judge it yourself. Drop it if it only shares a topic.
5. If nothing fits, say "no outside passage fits" and move on. An empty list is a good result. Never stretch a weak match.

## Rules for using a passage

- Cite by author, book, page and exact words: Steven Pressfield, The War of Art, page 93. Quote the text as stored. Never reword inside the quote.
- It is always their idea, never his. Never present it as Coach Gen's words, memory or experience.
- Keep it short: one or two sentences of the quote, then his own idea in his voice.
- Show him the match and its score when you propose it, so he can judge. He decides what goes in the work.
- Outside quotes are not gold entries and are not logged in `brain.used_in` unless he asks.
- Quote length follows copyright sense. Quote a line or two. Never paste a page.

## Report a miss

If he says a citation should have come up and did not, or one that came up was wrong, add it as a new question to `claude/Brain_Test_Set.md` (add only), with the idea, what he expected and what came back. Then tell him it is logged.