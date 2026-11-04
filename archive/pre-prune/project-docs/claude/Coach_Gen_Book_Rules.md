# Coach Gen Book Rules

Rules for writing the book *5 Laws of Lasting Change*. This file holds **Book Rules v2** (5 Oct 2026), built bottom-up, and below it, unchanged, the abandoned v1 kept as raw data.

---

# BOOK RULES v2 (5 Oct 2026)

**How v2 was built.** From the full read of the 5 books on his shelf: The Elements of Style (2018 Classic Edition), On Writing Well (6th edition), Atomic Habits, Mindset, and The Courage to Be Disliked (English). Full notes and findings: `claude/Findings_Guides.md`, `claude/Findings_Books.md`, `claude/Full_Read_Notes_1_Elements.md` to `_5_Courage.md`. Every rule below is checked against his own reactions, which are logged word for word in `claude/Coach_Gen_Book_Calibration_Log.md`.

**What earns a place here.** A rule must rest on what the books do **and** on something he said. A rule marked **[5 of 5]** is shared by both guides and all 3 books. A rule with weaker support says so. Nothing here comes from an edit he never complained about. Where a rule could be overfitting to one note, it says so.

**How this file relates to the Language Rules.** `Coach_Gen_Language_Rules.md` (protected) still governs his voice: plain words he would say, concrete nouns, quoted self-talk, glue, stakes over story, the prescription from the worksheet, no invented biography. For the book, these rules sit on top. Where the two disagree, section H lists the clash and his decision. Book craft may override the Language Rules (his decision, 4 Oct: "for this warning, language rules can be superceded").

**How to use these rules.** Not as a checklist while drafting. Round 3 failed because the findings were used to patch sentences one at a time, and he called the result "robotic and repeated." So: draft whole, from the material forward (section A). Then use section I as a review pass.

**Protected (5 Oct 2026).** This file is protected at the same level as `Coach_Gen_Language_Rules.md`. See `claude/Coach_Gen_Protected_Docs.md` before any write.

**Maintaining this file.** Add and annotate. Never condense. When a later round corrects a rule, keep the old line and mark the correction.

---

## 0. HIS MARKUP CODE (general rule, added 15 Oct 2026 at his request: "ADD GENERAL RULE.")

Applies to every draft he marks up: articles, the book, and anything else. His words, in full: "anything I put in [], like in this comment, means I am suggesting, and will be ok with you rewriting 50% of that sentence andor flow. anything I put in "", means I strongly believe in this sentence. and you will only be allowed to alter a 10%, while keeping my voice. if an instruction down the line says that this sentence in "" is to be changed or awkward, the newer always wins."

- **[Square brackets] are a suggestion.** Up to about half of that sentence, or its flow, may be rewritten to fit the piece.
- **"Double quotes" are a sentence he strongly believes in.** Change at most about a tenth of it, and keep his voice.
- **Newer wins.** If a later note says a quoted sentence should change, or reads awkwardly, the later note wins.
- **Paragraphs look separate.** In a Google Doc draft, every paragraph has visible space after it. His words (15 Oct): "always make the paragraphs look separate."
  Annotated 3 Nov 2026: chapter drafts now follow the printed book's layout, so a paragraph is set apart by a first-line indent, with no gap, as in the book. The newer rule wins for chapter drafts. Key moments docs and article drafts keep the visible gap. His words (3 Nov): "can you change the draft reviewing experience I do to also follow the layout of the finished book. I want to see it, and this changes everything about the feeling of reading." His pick: "a" (indent only, no gap).
- **/privileged** (added 3 Nov 2026): the line reads as privileged context. Keep the fact, make it acceptable, and say plainly where it was a privilege.

---

## A. BEFORE WRITING A WORD

**R1. Fill the blank, and pick one thread.** Write "this section is about ____" and the one thought the reader should leave with. Every paragraph must be a step on that thread. Zinsser: "Every successful piece of nonfiction should leave the reader with one provocative thought... Not two thoughts, or five." The Language Rules' overriding test says the same.
His words (epoch 1): "if james clear's introduction is a beautiful continuous x=y graph. epoch 1 feels like x=floor(y) graph." And: "too many ideas being put in (that should be put elsewhere...) that makes it feel like x is not even a function of y, and is just random."
Test: for each paragraph, say in one line how it moves the thread. If you cannot, it belongs somewhere else.

Annotated 30 Oct 2026.
1. The one thought must carry the whole chapter.
2. Pattern to reach for: sections plant arguments, and a later section of the same chapter joins them into one picture.
3. His words (29 Oct), on Chapter 3 epoch 2, scored 5.5: "the ideas feel they are fragmented and doesn't build a 10/10 idea".
4. His words (30 Oct), praising Chapter 3 epoch 3. By "chapter" he meant a later section: "I like the putting arguments in subchapter, and then using them in following chapter to reveal a grand picture."

**R2. Every idea lives in the chapter that owns it.** A book has room. An idea that belongs to a later chapter is not previewed early. If the Introduction and Chapter 1 both explain the same idea, one of them is wrong.
His words (epoch 1): "ideas that are repeated, or ideas that don't make sense to be included, or too many ideas being put in (that should be put elsewhere, since this is a book with leeway and most likely we will need MORE content to fulfill page or writing quota)."
Support: Clear stays on one idea per heading for 8 to 25 paragraphs, and a new idea gets its own heading (AH 449 to 767). Dweck's Introduction holds 5 moves in 349 words and leaves every idea to Chapter 1 (MS 49 to 78).

**R3. Only approved material.** Build scenes from the Testimony collection, his worksheet (`build_worksheet.js`), his published pieces and his own notes. A transcript is only for checking a fact, never a source of new detail. Never a body weight, health reading, money figure or health framing. Composite names in print (Melina, David, Dan Sato).
His words (round 3): "where the fuck did healthy come from?"
Support: none of the 3 books sources a private detail without a reason in the scene. Dweck labels background and keeps it to facts (MS 7257 to 7263).

Annotated 5 Oct 2026: for stories about people he coaches, R3b now governs the surface of the scene. R3's limits still hold for the core: the records stay the source, and no body weight, health reading or money figure goes in.

Annotated 4 Nov 2026: money and health.
1. Money may appear when it shows a struggle or a human side. It never appears as a flex or a promise of wealth.
2. His words (4 Nov): "money can enter the picture when it pictures a struggle or paints a picture or etc. the blanket rule was added so AI don't follow the flexes "here's how to make a million dollars"." On a built loan figure: "Money is fine as long as it's accompanied by a human side, which now it is not."
3. An everyday illness or a hospital stay, used as a cause, is not health framing (Built Detail Test, Q1.1 and Q1.4). A condition, a diagnosis, a medicine, a health reading or a body weight still is.

**R3b. Stories about people he coaches: true core, built surface.** (Added 5 Oct 2026, at his request: "ok do the rule change. also, keep my whole reasoning.")
His reasoning, word for word (5 Oct, on the Melina case in the 5 Oct article draft): "About Melina. there is something not quite right with this. it stands in the midpoint between being vague and being relatable. and because it's there, readers don't understand, and the case study person can still identify themselves. and because it's vague, the sentence constructions are choppy and fragmented. I suspect that the rule that pushes this phenomenon is the non-hallucinate rule, coupled with the fact that my coaching is built on context that the text doesn't have and clients in coaching talk exploratively, hence in fragments and all over the place. so you end up regurgitating fragments of thoughts. Let's solve this as main priority"
The rule. From the records, keep the core true: what the person was stuck on, what she did, what changed, which Law it shows, and his own words. Build the surface for the reader: a life, a scene, a setting, and full lines of speech, re-created from memory the way the anonymity line promises ("I changed the names and details of everyone I coach... Sometimes 2 or 3 people became 1... What people said is written from memory"). A built detail must make the core clearer and the person harder to recognise. It never changes what happened, never improves the result, never adds health, weight or money detail, never replaces his method, and never touches his own biography. Never quote a client's thinking-out-loud as a line: write the line she would say once she had found the words.
Every built detail is listed under the draft, next to what the records say, so he can strike any of them.
First applied: the 5 Oct article. His own surface changes on the next round (a 30-minute walk to work instead of the MRT, a business trip to China, oily food) show the method working the way he wants: he picks or approves the surface, the core comes from the records.

Annotated 4 Nov 2026: built details, what is allowed and what is not. From the Built Detail Test (3 and 4 Nov): 100 built versions of 20 real records, each marked by him. His marks: `Book/Research/taste_tests/built_detail_test_marks_full_2026-11-04.md`, and the Google Doc "5 Laws, Built Detail Test (20 questions)" (id 12X8BsIL9Wk2f4E6ggacLbUbB0f3v23NOMDNYriAZ7T0). "Q4.5" means question 4, version 5.

*Read this first*

1. This list says what is allowed and what is not. It never says what must appear.
2. An allowed detail does not have to appear.
3. When a record could be built out in several allowed ways, choose the one or two that do the most for the reader. This list exists so you can build with discretion and confidence, not so you build less.
4. The default is the record as it was said. Build only to answer a question the reader will ask and the record does not answer (R5), or to hide the person.
5. A built detail must do work for the reader. One that only decorates is cut, even when it is allowed. His word for a built weather line and a built line for HR: "useless".
6. Each detail was marked on its own, not as a set. After building, read the whole passage again as the reader would.
7. Ask "can I imagine this?" about this person, not about people in general.
8. When a detail is not on this list, leave it out and ask in the end note. Every built detail goes on the end note's built list (R3b).

*Never*

9. A better or invented result, or raised stakes: a setback, a loss or a threat the records do not show. His words: "Hard line on falsifying results or my accomplishment." On a built setback: "Similar to raising results, it generates a feeling of lying in me." One exception: an invented persona, made up only to show a point, may get a result.
10. The person's past: childhood, family history, where an idea of theirs came from, why they became who they are. A past the person told him is a record, and may be used.
11. An insight or a line moved from the person to someone else, such as a wife naming his pattern or a boss saying his realisation.
12. Family members acting or speaking: a wife's reply, a child's question, a parent at the table, a phone call. On a built call from his own mother: "Still not comfortable adding family or over chumming the book". A family event offstage, used as a cause, can pass (Q1.4).
13. Sensory detail in a scene he was not in. He can tell what the person told him, never what only a witness could see. On "The coffee went cold in his hands": "I am not there wtf."
14. What no real person would do. On a launch date set for a daughter's birthday: "I can't imagine him doing this."
15. In research: a made-up participant, a number not checked against the source, or a feeling given to the researchers.

*Border: no, unless*

16. An action built from something the person only said. On built push-ups in the session: "Moving from something he said to something he did is a big border." A small, ordinary action that carries the talk can pass, like "he showed me the cover" (Q2.2). A staged action that proves a point fails, above all one with a number that works like a result (the push-ups, Q5.4).
17. A feeling the person did not name. Only as his reading, framed as a hunch ("Underneath", "I suspect"), and earned by their own words: "Hunch that is substantiated and well earned by the words that accompany it." Q4.4 passed because his words point to it ("I want to play my game"). Q8.5 failed because nothing he said points to embarrassment.
18. What another person did, if it changes the tone or the dynamic of the story. A harmless line can pass: "this one info can change the tone of the whole story and the dynamic. The easy money earlier was quite harmless."
19. A session number or exact time that makes the record look more precise than it is. His words: "The session number itself is iffy".
20. A reworded version of his own coaching line, when the record holds his real words. Use his words (Q15.4).

*Allowed, as a reasonable assumption from his years of coaching*

21. A cause between two recorded events, of any size, even one that makes the person look weak, if real life works that way. His words (3 Nov): "david has a system->it worked for awhile-> something happened->it starts failing->he thinks he's lazy. is an example of a reasonable read I can do on the situation based on my flight hours."
22. What an unnamed thing was ("something else" became a language class), and what usually happens next ("one game became three").
23. Small facts the person could have told him: when they wrote the list, what the easy thing was, how long they tried.
24. Small things he saw in the session: a pause, a silence, where they looked, how loud they said it. On pauses: "Almost always ok. Since my process involves alot of pausing."
25. A plain scene of the problem that serves the reader ("she read every word off her slides").
26. The person's own odd fixes, if plausible. "Clients do weird shit all the time as their unique solution to their problems, from starting to raise chickens to wearing a tie everyday to work."
27. A result that matches the record, told as a scene, kept light. On one: "Plausible, but feels almost too much."
28. His narration taking the person's image a step further, or explaining their move.
29. The person's meaning in new words inside quote marks, in good faith: clearer, never sharper or better. On a line labelled "a sharper line": "The sentence itself I am ok with. But since you annotated as "a sharper line", try not to."
30. Swaps that hide the person: the object, the job, the meeting. Often is fine. Every other detail stays consistent with the swap. Change the role rarely. "Perfectly fine, I would be ok if you do this often. This adds variety, obfuscates the client, and keeps the message. But then make sure the other details are aligned"
31. Money, when it shows a struggle or a human side (R3, annotated 4 Nov).
32. In research: the names and the year from the citation, and a scene the reader is asked to picture ("Picture yourself in that room").

*Use very carefully*

33. A line built for him: "1 it has to fit my person. 2 you have to be sure that this one line will change everything and is the absolute best way to illustrate a certain point."
34. His first move in a session, when built: only a question, or something a coach would do.
35. Something the person did after the session: "Use very sparingly."
36. "Almost everyone I coach", followed by three quick examples.
37. His observations: one thing noticed, then a question. Never three stacked into a judgement. "A coach rarely and will not observe 3 things, assume a link, and use it to judge the client. A coach OFTEN observes 1 thing, is curious about it, and asks."
38. Singlish and other local words: a calculated risk, because they can identify the person.

*His own stories*

39. The same lines hold. A true event may move to another day: "I actually did this, but not that night." A built action of his own (Q18.3) is out, and so is his family (Q18.4).

**R4. Write whole, from the material forward. Never patch.** A redraft starts from the source material and the thread, not from the last draft's sentences. If the same passage has been rewritten 3 times, write from a different piece of material instead.
His words (round 3): "If you think you're overfitting, maybe try writing by taking a different piece or idea from the worksheet." Round 4, written whole from his own story: "it's fine."

**R29. Insight 2 and 3 are optional.** (Added 6 Oct 2026 at his request: "write all 1-5 rules.") When a chapter is built from an article, the article's Insight 2 (research) and Insight 3 (questions) may be left out. Use one only where the chapter's thread needs it. A study that stays in follows R28. Questions that stay in belong in the From Within You box.
His words (Chapter 1 epoch 1): "I think a good rule of thumb is that insight 2 and 3 is always optional to include in book. if an article is used as source."
Support: his own rule of thumb. The books agree in spirit: Clear's own story carries no research (R28).

---

## B. THE LINE: SENTENCE TO SENTENCE, PARAGRAPH TO PARAGRAPH

**R5. The reader's question sits between paragraphs, and the next first sentence answers it. [5 of 5]**
Zinsser reads a good article by writing the reader's question between its paragraphs ("But hadn't this been possible before?"). Dweck prints the question and answers it at once ("What did they know? They knew...", MS 137 to 138). Clear writes in the reader's doubt ("You may be thinking...", AH 2339). In Courage, the youth is the reader's voice.
His words: "No sentence feels smooth next to each other." "Sentence 1 talks about melina's internal talk, but 2 talks about something else."
Test: between every 2 paragraphs, write the reader's one-line question. If you cannot, the link is missing.

**R6. Each sentence hands something to the next. [5 of 5]**
The devices, in the order the books use them: a repeated key word, often narrowed ("our work" to "My work", MS 50 and 53), a pronoun with one clear referent, question then answer, a time word in a story, "But" at a real turn. In Atomic Habits, 63% of neighbouring sentences show a visible link (repeated word 38%, connector 15%, pronoun 15%, same opening frame 11%). Bare connectors are rare: "However" opens only 12 sentences in the whole book.
Name the real relation (Strunk): "because" for cause, "but" for contrast, a time word only when time moves.
His words: "then is not the right connector here."
Test: underline the word each sentence takes from the one before. A sentence with nothing underlined needs a reason to be there.

**R7. Repeat the words, not the idea.** When a reader has to recall a sentence from earlier, give the words again instead of "it" or "this". But a sentence that only says the last one again, louder, is cut.
His words: "it. is too vague. repeating the sentence in paraphrase would help here." And (round 3): "robotic and repeated."
Support: Courage's test for a restatement: delete it, and if nothing is lost but volume, it was a repeat, not a step (CG 2147 to 2152). Zinsser: "kill it or warm it up with specific detail."

**R8. Show it, then name it, then say it plainly. [4 of 5]**
Clear never names a concept before the reader has seen it (the ice cube before "the Plateau of Latent Potential", AH 572 to 607). Dweck's "mindset" first appears in quote marks as the name for what she has already described (MS 61). Courage names a term after the experience (CG 2445 to 2447).
His words: "wtf is this?" (on a line that named something the reader had not seen). On Dweck: "Titledrops with elegance."

**R9. A surprising idea never arrives bare.** One of 4 things sits right beside it: an example the reader has lived, the reason in the very next sentence, premises the reader already accepted, or the reader getting there first.
His words (on Courage's friend in his room): "the paradox and overturning mindset shift is presented directly, which can be hard to swallow for a new concept."
Support: Courage itself, at its best (CG 2411 to 2435, 3338 to 3346, 5338 to 5340). Overfitting check: this rests on one note of his plus one book. Treat it as strong, not yet proven.

**R32. Few things to remember, one name each. [Dweck and Clear, measured]** (Added 6 Oct 2026 at his request: "write all 1-5 rules.") Before drafting, list every term, label and name the reader must carry out of the chapter. Keep 2 or 3. Each keeps the same words every time it appears. No second name for a named thing. Labels from the source articles (Act 1, Insight 2, "the pattern") are not the reader's words: say the thing plainly. A name the reader does not need to keep (a researcher, a YouTuber) appears once with a role tag, or not at all.
His words (Chapter 1 epoch 1): "Some language can (must, should) be changed to keep down the number of vocabulary the reader needs to keep in his head."
Support: Dweck's Chapter 1 asks the reader to keep 2 named things, the fixed mindset (11 times) and the growth mindset (18 times), and repeats each phrase word for word ("carved in stone" 4 times, "cultivated" 4 times). Famous names pass once each with a role and are dropped. Clear's Chapter 1 names 3 things, each shown before it is named. Chapter 1 epoch 1 asked the reader to hold about 20 terms and 7 names, and gave one thing 3 names (acts, groups, stages).
Not the same as H3: H3 is about hard words. This rule is about how many names.

---

## C. SENTENCES

**R10. Short sentences have a job. [5 of 5]** Under 8 words only to compress, turn, reveal, answer at once, or hold a beat. Never to bring a new fact. About 1 sentence in 7 (Clear 13.8%) to 1 in 5 (Dweck 22.5%).
His words (Mindset vignette): "There are some extreme short sentences, but they are short and are used to amplify, not introduce new ideas." On a Claude draft: "maybe another : ? also these are choppy."
Test: label every sentence under 8 words with its job. No job, join it to its neighbour.

**R11. One event, one sentence.** Cutting one event into steps is choppy (Strunk's Macbeth example: 6 sentences become 1). A long sentence is fine when it holds a sequence in time order (Dweck's "As the students grunted, perspired, and toiled", MS 122).
His words: "each sentence is fleshed out and takes their time. and carries their own purpose."

**R12. Parallel only for items that truly match. Then keep the frame exact.** Strunk 15: "The likeness of form enables the reader to recognize more readily the likeness of content." Clear repeats one frame word for word and changes only the slot (AH 523 to 527). Keep the subject parallel too.
His words: "the parallel is still not that connected or is forced in a context that can't use that structure. Or when not enough material is there to make a parallel." And: "the and you should be parallel. either both thes or both you(r)ss"
Annotated 5 Oct 2026 (article "3 Stages of Consistency"): paragraphs that build on the same idea open in the same frame, so the reader sees at once that they belong together. His words: "the opener of paragraphs that build on the same idea, should be related to each other. this example is breaking this law". The failing openers: "That is stage 3.", "In her first weeks, she walked...", "Stage 2 is Law 4 in my coaching". The fix: "Stage 3 is where Melina is now.", "Stage 1 was her first weeks.", "Stage 2 was Law 4 in my coaching". Folded at his request ("write abc.").

**R13. Break a run.** After 3 or 4 sentences of the same shape, write one long sentence that moves the idea on (Clear's 41-word sentence after the lagging-measure run, AH 529 to 531).
His words (round 3): "yes now it's parallel and long, but it's just making it robotic and repeated."

**R14. The colon does the joining job.** No semicolons, no em dashes. A colon joins a statement to what explains or completes it. Commas or brackets hold an aside.
His words: "maybe a : or some better construction would help." "maybe another : ?"
Support: every em dash and semicolon in the 3 books can become a comma, colon, brackets or a full stop. 5 of the 6 Atomic Habits passages he loved have no em dash.

**R15. Grammar is correct, in his voice.** Fix tense slips (has and had, was and were), agreement and sentence fragments. Keep his words and his rhythm.
His words (4 Oct): "for book, grammar correctness is important, always make grammar changes while keeping my voice as intact as possible." (5 Oct): "fragments was the word I was looking for."
Warning: see H4. The books use deliberate fragments. Default: no fragments.
Annotated 5 Oct 2026: R15 applies to articles too, not only the book. Check every draft for spelling and grammar mistakes and fix them silently, without listing them, while keeping his voice. His words (article "3 Stages of Consistency"): "check for spelling and grammar mistakes." Then: "d should be the rule now. you can do it silently. make sure to keep my voice."

**R33. Oxford comma.** (Added 6 Oct 2026 at his request: "keep 1, 2, 3. others feel like overfitting.") In a list of three or more, a comma goes before the last "and" or "or": "School, my parents, and everyone else".
His words (Chapter 1 epoch 2): "oxford comma important".

---

## D. PEOPLE, SCENES AND QUOTES

**R16. A case has a set shape. [4 of 5]** One sentence gives the person (name, relation or role, what is at stake). The situation and stakes come before she speaks. An action or a feeling comes right before a short quote. The quote is long enough to carry itself, or comes last, as the payoff. Then one sentence of meaning, using a word planted before the case.
Models: Jim Marshall (MS 1046 to 1063), Brian Clark (AH 910 to 931), the blushing student (CG 1149 to 1158).
His words (Jim Marshall): "Short enough to not detract or have too long of tangent. But enough details and every sentence is curated beautifully to illustrate a point within a timeframe."
Annotated 5 Oct 2026 (article "3 Stages of Consistency"): a case from one area of life only reaches readers who share that area. After the case, carry the idea into at least one other area the reader lives in, using the same frame as the case, then name a few more areas. His words: "we are missing the generelazing examples. how is this example about weight loss usable for people building productivity, etc? it's missing and it feels." The fix that passed: after Melina's walking and oily food, one paragraph ran the same 3 stages through focused work, then named learning a language, saving money and going to the gym. Folded at his request ("write abc.").

**R17. Warm the water before a client's line.** A line that makes sense after hours of sessions can mean nothing on the page. Give the reader the facts they lack, never the meaning. Background is short and comes first. A quote of one sentence gets a longer setup, or the line runs a little longer, never shorter.
His words: "doesn't make sense. this might make sense in context of coaching with hours of context built between me and client, but not for reader. I think this is a BIG thing that you need to keep in mind." And: "quoted sentence feel too short... make it abit longer or explain it more to be more relatable."
Support: Zinsser (a hole "in the language or the logic"), Dweck (139 words of setup before the first quote in Ch 1), Clear (the reader must know what the person is answering).

**R18. Two or 3 exchanges are told in prose. [4 of 5]** Quote the turns that carry feeling, report the turns that carry facts. Use plain verbs that carry intent (asked, went on, pressed). Put something human between or after the lines: a look, a pause, "I'm glad I asked." One narrated beat can hold a silence.
His words (Clear's nurse): "Ten seconds passed is there, so this should be fine to use as coaching slow paced too." On Courage's script form: "the dialogue system is all or nothing it feels... if not then it's tiring."
His words on coaching scenes: "session feels transactional. I want to make it feel like I am a great coach, while being a warm interaction."

**R19. Set up a scene the way Courage's narrator does.** Body, setting only where it carries feeling, the inner voice, and one confident chain of cause and effect, all in one passage (CG 254 to 262). No pitying labels.
His words: "Telling of feelings while not really just telling the feelings but also with environment is cool. Also uses some psychological deductions I often use."
Project rule: never diagnostic, never pitying. The deduction says what a behaviour was for, not what is wrong with the person.

**R20. A mirror needs matching beats. [4 of 5]** Case, then a 1 or 2 sentence hinge naming what they share, then an explicit link ("I, too..."), then the second story with the same beats from the opposite angle, at a similar length (Robert and Dweck, MS 1019 to 1035). Not enough matching beats, no mirror.
His words: "mirroring case study with personal story, exemplary way to do so. P1 mirrors p2." And: "Or when not enough material is there to make a parallel."

**R28. Other people's research backs an idea. It never interrupts a story. [Clear and Dweck, measured]** (Added 6 Oct 2026 at his request: "write all 1-5 rules.") The idea comes first, in his words. Then the study in 2 to 5 sentences: who was studied, what was done, what happened. One finding. Then its meaning in one plain line. No year and no university. At most one name, with a role tag the reader can use ("the psychologist Carol Dweck"). Otherwise "psychologists", "researchers", "in one study". Never inside his own story's time line: the study waits until the story has finished, or until the chapter turns to the reader.
His words (Chapter 1 epoch 1, scored 70): "find how clear and dweck references other people's work or research. the way you put things is very jarring."
Support: Dweck refers to research in 148 sentences and gives a year in none, even for her own praise study ("So we conducted studies with hundreds of students, mostly early adolescents.", MS 2174 to 2175). Clear gives a year only when a study is a chapter's opening story (Thorndike, 1898), and mid-chapter writes "In one study, scientists...". A name comes with a role, one at a time ("Stanford professor BJ Fogg"). The meaning in one line: "The punch line is clear: people who make a specific plan for when and where they will perform a new habit are more likely to follow through." (AH 1836 to 1837). Clear's own story in his Introduction holds no study at all. Chapter 1 epoch 1 put 3 studies inside his story, each with 2 names and a year, 2 of them with a university.
Full findings: `claude/Findings_Books.md`, section F.

**R30. Quotes sit inside the prose. [Clear and Dweck, measured]** (Added 6 Oct 2026 at his request: "write all 1-5 rules.") Self-talk and quoted speech go inside the sentence that carries them. A quote stands on its own line only in 3 cases: a quick exchange of dialogue in a scene, a set of sample sentences shown as a list, or the chapter's payoff line, which is the author's own and needs no quote marks.
His words (Chapter 1 epoch 1): "for book, let's try making quotes inline. I believe other authors do this too."
Support: only 1% of Clear's paragraphs and 2.5% of Dweck's are a quote on its own (AH 13 of 1,130, MS 33 of 1,327). Self-talk inside the sentence: "What's wrong with them? I wondered." (MS 130). "We tell ourselves, "I'm going to eat healthier" or "I'm going to write more," but we never say when and where" (AH 1839 to 1840). The payoff line alone: "You do not rise to the level of your goals. You fall to the level of your systems." (AH 774 to 775).

Annotated 30 Oct 2026.
1. A call, session or talk is rewritten as book prose in his voice. It is never copied in the order it was said.
2. Quotes are welcome. Each quoted line must be as well written as the prose around it.
3. Which lines to quote and which to report: R18.
4. His words (28 Oct), on a run of quotes copied from a call: "putting quote in trains like how it happened in the call doesn't help the reader."
5. Context, not a rule: on 29 Oct he saw Claude's writing get weaker wherever a quote appeared. This is a note on Claude's drafts, not a ban on quotes.

**R35. Special lines.** (Added 6 Oct 2026 at his request: "keep 1, 2, 3. others feel like overfitting.") Only a few lines in the book are set apart on their own, centred and in italics: the line a chapter is built to deliver, such as its locked line. Most chapters have one, some none. In the master draft they are the "pull" blocks.
His words (Chapter 1 epoch 3, on "You do not fail to make lasting change. You succeed at staying who you are."): "this is a very special line that deserves a new line or its own paragraph or box. only some select lines will have this".

**R38. Tell a person's story once, then call back.** (Added 30 Oct 2026.)
1. Tell the whole story in one place, including the part that pays off later.
2. After that, the person returns only as a callback: the same words, a new layer of meaning, no new scene.
3. A new piece of a known person's story is not a callback. It reads as a retcon.
4. Material that doesn't fit goes to another person, another chapter, or out.
5. His words (30 Oct), on David coming back with new story pieces in Chapter 3 epoch 3: "introducing a new concept with the same name is not a callback".
6. His options: tell it whole then call back, tell it in pieces with clear "remember this" markers, or hand part of it to a fresh person.
7. Default: the first. The second at most once a chapter, one setup and one payoff.
8. Support: Clear tells Brailsford in one block (AH 386 to 427). Dweck tells Iacocca in one block, then one-line contrasts only. Epoch 3 had 11 new pieces of David and 3 true callbacks.

Annotated 3 Nov 2026.
1. Claude's reading: "once" means one story, not one list. One question runs from the first line of the telling to the last.
2. Pattern to reach for (his suggestion, to confirm on Chapter 3 epoch 5): the story follows the chapter's own shape, so each later section grows a part the reader already saw.
3. His words (30 Oct), on the line listing David's three patterns in Chapter 3 epoch 4: "why not build the david story above to follow this framework too?"
4. What went wrong (Chapter 3 epoch 4): every David fact went into the opening in plan order, and the reader felt "did I just miss several paragraphs".

---

## E. THE AUTHOR

**R21. Warmth is the author's own story: short, mirrored, admitting something. [5 of 5]** 1 to 8 lines from his own life, placed right after a case or idea, built on the same shape, with a small failing in it (Clear's food log, AH 4868 to 4870. Dweck's "So I cried.", MS 6946). Take the blame off the reader ("the problem isn't you. The problem is your system.", AH 770 to 771).
His words: "too blocky. No warmth." "still lacking some warmth." And on Dweck: "Even just comparing the 'that's why my 30 days' vs 'when I was a young researcher'."
Annotated 5 Oct 2026 (article "3 Stages of Consistency"): anything that shows the author in a negative or unfinished light is clearly placed in the past. The exception is the payoff of a long build of vulnerable stories, which is rare and deliberate. His words: "things that depict the author in a negative or incomplete light, must be clearly that it is in the past. unless it is payoff of a lot of buildup of vulnerable stories, which is rare and deliberate." The fix: "My routine never even needed a vacation to break" became "There was a time when my routine didn't even need a vacation to break." Folded at his request ("write abc.").

**R22. Confidence is calibrated, not loud. [5 of 5]** Flat claims where the evidence is solid ("It was mindset.", MS 3334). A hedge only at a real limit ("Can anyone do anything? I don't really know.", MS 2151). One honest limit per chapter. A verdict in the first person ("I think you would.", AH 687).
His words: "inconfident authorship." On Atomic Habits: "The use of you is confident and decisive, with bold and well thought out ideas." On Mindset: "Some diagnosis that feels confident too."

**R23. Check in with the reader.** A question the reader is already asking, answered at once. The reader's doubt said aloud before they can raise it ("Now, I know this idea might sound overly simplistic... But stick with me for a minute.", AH 3196 to 3197).
His words: "Think feel do seems really nice, checking in on the audience with questions." "author connecting with audience is important."

**R36. Once the piece turns to the reader, stay close to the reader.** (Added 15 Oct 2026 at his request: "add btoh.") When a paragraph ties off the presentation (the story, the history, the study), the paragraphs after it open on the reader's own life: "you", "we", their goals and their days. The far-off frame (agriculture, the animal, the lab) can still appear inside a sentence, but never as the opener. A callback that brings the story to the reader ("Remember David...") counts as close.
His words (Law 1 Part 2, draft 3): "since I wanted the previous paragraph to be the segway to audience, opening the paragraph with something far from the audience (agriculture) is no longer a good idea. I think this applies to all, not just this article. I don't know how to say this rule in a better way." And: "again, this is the time to connect with reader's experience. because previous paragraph already beautifully tied a ribbon on the presentation." And, on "Remember David": "this is example of a sentence close to the audience."
The fix in draft 4: "Why bother with agriculture at all, when gathering feels so good?" became "Think about what you really want." And "But agriculture has a hard part that gathering never had." became "You know the hard part already."

**R37. One leap of logic per step.** (Added 16 Oct 2026.) When a piece explains how something works, list the reasoning as steps before drafting, and give each step its own paragraph. A step that holds two leaps becomes two steps. Never merge steps to keep the piece short.
His words (Law 1 Part 2): "let's discuss this in parts first. what are the parts of the step by step scientific reasoning that led to this conclusion? then from there we can glue." On one paragraph that made two jumps at once (from the hunter-gatherer to starting something, and from starting to the reward): "2 different leaps of logic... hence might need a new number, if needed." The result: "good, that's reads like a proper argument chapter in a boo now."

---

## F. IMAGES

**R24. An image must already be in the reader's life. [all 3 books]** Take it from the reader's own memory, the author's life, the client's own words, or a story everyone knows. Hold one image. Pay it off in one plain line. Courage starts most images with "have you ever..." or names the picture already in the reader's head, then corrects it.
His words: "what is this vague metaphor no one ever uses?" The Language Rules already say: "a concept that is new by definition cannot be vivid."

---

## G. THE BOOK'S SHAPE

**R25. Plant and pay off threads. [all 3 books]** A word, image, case or promise appears early, comes back with something new, and pays off near the end. Call back with the exact words and a reminder tag ("Jimmy, the hard-core turned-off student from chapter 3", MS 7130). A callback must add a layer, never the same point again.
His words (memory, 1 Oct): he likes Courage for its "structure of book." He sees "not trying keeps an excuse alive" as the book's looming idea, the way freedom looms over Courage.
Annotated 15 Oct 2026 (article, Law 1 Part 2): in an article too, once the story has ended, the second half calls back to it at least once. His words: "on the second half, after story has ended. it's important to have callbacks. to the story. usually at least once." Draft 3 already did it ("Remember David, and the week of zeros that made him stop caring?"). Folded at his request ("add btoh").

Annotated 30 Oct 2026.
1. Bring a thing back in the exact words the reader first met, plus a short tag.
2. Name a chapter only when the reader must go back and use a tool.
3. Each chapter opens from where the last one left the reader.
4. Measured: Atomic Habits says "last chapter" once. Mindset says it three times. Chapter 3 epoch 3 pointed back by name ten times in 66 paragraphs.
5. His question (30 Oct), about those ten pointers: "is there a better way to nudge the audience to feel a callback without this very crude way".

**R26. Endings: the relationship, the echo, or one sayable line. [5 of 5]** Never a teacher's summary in the prose. A summary box lives outside the prose. Zinsser: readers "hear the laborious sound of cranking."

**R27. Open the book like Dweck.** Introduction (MS 49 to 78): a short origin scene with a person in it, the author's standing, the promise to "you" with the key term arriving as a name, a flat claim and promises that narrow from public to private, then what is inside, with the anonymity note in brackets. Chapter 1: the author's own scene in time order, one job per sentence.
His words (1 Oct): "it elegantly highlights the importance that this book carries while still being a thought leader." On the Introduction: "teaser feels important. Also helps to make the reader feel the book will be substantial, and help them achieve their goals."
His words on the first lines (epoch 0 and 1): "let's try a construction where this sentence is the first sentence" (Melina's line), and of epoch 1: "apart from the first sentence which I like."
Do not repeat the subtitle in the opening pages (epoch 0: "If you keep trying but never finish this is why is repeated 3 times in the first sequence of papers").

**R31. Headings mark a new idea, never an act of the story. [Clear and Dweck, measured]** (Added 6 Oct 2026 at his request: "write all 1-5 rules.") The opening story runs with no heading. A heading goes where the chapter turns to a new idea, about one every 400 to 600 words at most, never in the middle of a thread. It names the idea or asks the reader's question, in plain words, and the section before it ends on the question it answers. Never a line lifted from the story, never an article's act title. The same words are not reused as group names in the boxes.
His words (Chapter 1 epoch 1): "now it seems that the subheadlines are not needed? or maybe the subheadline feels too robotic that it detracts currently. explore how clear dweck does it"
Support: both books use a heading about every 400 to 600 words (MS Chapter 1, 3,800 words, 6 headings. AH Chapter 1, 4,300 words, 6). The opening story never has one (MS 428 words, AH 666 and 830 words before the first heading). Headings name the idea or ask the question: "Why Do People Differ?", "So, What's New?" (MS), "Why Small Habits Make a Big Difference", "What Progress Is Really Like" (AH). Brailsford's story ends "How does this happen?" and the next heading answers it. When the author's own story is headed, the heading is a plain label: "My Recovery" (AH).
This replaces, for the book, v1's "Story sections get real names" (1 Oct, archive section 6). Chapter 1 epoch 1's headings were lines from the story ("I Did Change") that cut one thread into acts.

Annotated 30 Oct 2026.
1. Default to headings that name the idea.
2. Use a question only where the reader is truly asking it.
3. Try to make each heading fresh and human, sometimes a pun. He may still rework it.
4. Claude's reading: when every heading is a question, every section closes itself.
5. His words (29 Oct), on a draft where every heading was a question: "Why is every subchapter heading a question".

**R34. The Chapter Summary box.** (Added 6 Oct 2026 at his request: "keep 1, 2, 3. others feel like overfitting.") The summary is never in "I". It uses "we", "you" or plain statements, and it holds the chapter's key phrases, so a reader can find the chapter again from the box alone. Every line still comes from the chapter.
His words (Chapter 1 epoch 2): "chapter summary should not be "I". should be we or anything else. Also chapter summary is a good place to house key phrases."

**R39. A section rises to one turn, then hands off.** (Added 30 Oct 2026.)
1. Shape: hook, build, turn, one hand-off line.
2. Examples and proof go before the turn.
3. Nothing comes after the turn except the hand-off.
4. His note (30 Oct) on Chapter 3 epoch 3: section openings were strong, then the quality "deteriorates as the subchapter progresses".
5. Claude's reading, to confirm on epoch 4: "Why Lazy Wins" ran six beats past its reveal.

**R40. Figures.** (Added 30 Oct 2026.)
1. A tool, grid or model the reader will use can be a figure.
2. Number by chapter: Figure 3.1, Figure 3.2.
3. One full-sentence caption under each.
4. Point to it once in the text.
5. A figure never replaces the prose explanation.
6. His words (30 Oct): "figures are a good credibility builder" and "refer to them as figure x.y".
7. Support: Atomic Habits captions each figure with a full sentence (AH 1297).
8. Open issue: the master draft build doesn't handle figures yet.

---

## H. WARNINGS: WHERE THE BOOKS AND THE LANGUAGE RULES DISAGREE

**H1. Numbers.** Language Rules: digits, "Spelled-out numbers are an instant tell." All 3 books: small counts as words ("Ten seconds passed"), digits for measures, percentages, years and labels. **Decided 5 Oct: "numbers are fine."** Claude's reading, given to him: follow the books. Small counts in words (the third time, two months, six years), digits for measures and labels (a 30-minute walk, 61 inches, chapter 1, Law 1). He may correct this.

**H2. Contractions.** His published pieces use none. The 3 books use 13 to 18 per 1,000 words, and they mark the warm, spoken voice. **Decided 5 Oct: "contractions are fine."** Use them where the sentence is spoken or warm, not everywhere.

**H3. Vocabulary.** Language Rules: simple words, readers with English as a second language. **Decided 4 Oct for the book: "vocabulary is not a concern, since book can be more complex."** Zinsser's bar still holds: "vivid and precise, but not long or fancy."
Annotated 6 Oct 2026: H3 covers hard words. How many terms the reader must hold is a separate rule, R32.

**H4. Fragments (new, 5 Oct).** His rule: fix fragments. All 3 books use deliberate fragments that hang off a full sentence and amplify it ("Mostly horrified.", MS 2097. "Tiny changes. Remarkable results.", AH 6204 to 6205). Default: no fragments. **Needs his call case by case** if a draft keeps one on purpose, and it must be flagged.

**H5. Narrating structure.** Language Rules: "Never narrate your own structure." Dweck's "But first some background" and a book's "In this book, you will..." do exactly that. **Decided 4 Oct: "language rules can be superceded"** for this. Keep it to a signpost the reader needs, never an explanation of the shape.

**H6. Semicolons and em dashes.** Strunk calls the semicolon "one of the most useful devices of composition", and Zinsser calls the dash "invaluable". **Ban kept.** The colon, commas and brackets do their jobs (R14).

**H7. "However" first.** Both guides say no. Dweck uses it to warn of a reversal, and he asked of it, "Maybe the However holds the key here?" Allowed when it turns the story.

**H8. Length.** The Language Rules' article ranges (280 to 450 words, 11 to 13 words per sentence) do not apply to the book. Word count is not the target. His words (1 Oct): "Length doesn't matter now, (this is not an instruction to hallucinate or elongate)."

**H9. "My clients".** Still banned in the book ("seems too straightforwardly condescending"). Use "the people I coach", "someone I coach", or the person's name.

**H10. Research and self-talk (new, 6 Oct).** Language Rules section 11 says he "Introduces research by naming the researcher and the year inside the story" and uses "Quoted lines carrying self-talk, dropped in as their own beat." R28 and R30 say the opposite for the book. **Decided 6 Oct: "keep the new rule in current merge conflict."** In the book, R28 and R30 apply. The Language Rules lines are unchanged and still govern his articles.

---

## I. REVIEW PASS (after the draft is whole, never during)

1. The blank is filled, and every paragraph moves the one thread (R1).
2. No idea here is owned by another chapter (R2).
3. Every fact traces to approved material. No weight, health, money or invented detail (R3).
3b. In a story about someone he coaches, the core traces to the records, and every built detail is listed under the draft (R3b).
3c. Every built detail in a story about a real person is on the allowed list (R3b, annotated 4 Nov), does work for the reader, and is listed in the end note. No result, raised stakes, past or family scene was added. Use one or two per gap, chosen for the reader. (Added 4 Nov 2026.)
4. Between every 2 paragraphs, the reader's question can be written, and the next first sentence answers it (R5).
5. Every sentence takes something from the one before (R6). No "it" pointing at a sentence far back (R7).
6. Nothing is named before it is shown (R8). No surprising idea arrives bare (R9).
7. Every sentence under 8 words has a job (R10). No run of more than 4 same-shape sentences (R13).
8. Every parallel joins items that truly match (R12).
8b. Paragraphs that build on the same idea open in the same frame (R12).
9. Every client line has its facts before it, and a one-line quote is set up or made longer (R17).
9b. A case from one area of life is carried into at least one other area the reader lives in (R16).
10. The author admits something, and the reader is checked in with (R21, R23).
10b. Anything showing the author in a negative or unfinished light is clearly in the past (R21).
11. Every image comes from a life the reader has, and there is only one per passage (R24).
12. Mechanics, checked by script: no em dashes, no semicolons, numbers per H1, British spelling, grammar and fragments per R15 and H4.
12b. Spelling and grammar are fixed silently in articles too, in his voice (R15).
13. No study sits inside his own story. A study has no year and no university, and at most one name with a role (R28).
14. Any Insight 2 or 3 material left in earns its place on the thread (R29).
15. Every quote sits inside its sentence, except a quick exchange of dialogue, a list of sample sentences, or the payoff line (R30).
16. The opening story has no heading. Every heading names an idea or asks the reader's question, and the section before ends on it (R31).
17. The terms the reader must keep are listed, there are 2 or 3, and each keeps one name every time (R32).
18. Every list of three or more has its Oxford comma (R33).
19. The Chapter Summary has no "I", and it holds the chapter's key phrases (R34).
20. Only the line the chapter is built to deliver is set apart (R35).
21. No person comes back with a new piece of their story once it has been told. Every later mention is a callback (R38).
22. No "in the last chapter" or chapter number where the planted words can carry the callback (R25).
23. Every section ends at its turn, plus one hand-off line (R39).
24. Every figure is numbered x.y, has a one-sentence caption, and is pointed to once (R40).

---
---

# ARCHIVE: BOOK RULES v1 (abandoned 4 Oct 2026)

Kept word for word below as raw data. Do not apply it.

# Coach Gen Book Rules (ABANDONED)

> **ABANDONED 4 Oct 2026, at Coach Gen's request.** His words: "let's then, abandon the current book rules. work from the bottom up." Do not apply any rule in this doc. It is kept only because his verbatim notes below (the epoch 0 log) are raw data for the bottom-up rebuild. The new book rules will be built from a full analysis of his reference books and writing guides, checked against his own reactions.


Rules for writing the book *5 Laws of Lasting Change*, and the calibration evidence behind them. Started 4 Oct 2026.

**How this doc relates to the Language Rules.** `Coach_Gen_Language_Rules.md` still governs the voice: simple words, numbers as digits, British spelling, no em dashes, no semicolons, quoted self-talk, glue between beats, stakes over story, the prescription from the worksheet, no invented biography. This doc adds only what changes when the piece is a book. Where the two disagree, this doc wins for the book. The `[article]` ranges (280 to 450 words, and the rest) do not apply here.

**Why it is a separate doc.** The Language Rules doc is protected and every write retypes about 9,000 words. Keeping the book track here means it can grow every round without touching that doc. Coach Gen can merge it in, or add this doc to the protected list, whenever he chooses.

**Maintaining this document.** The same rule as the Language Rules: add and annotate, never condense. When a later finding corrects an earlier rule, keep the old line and mark the correction.

**Where each rule comes from.** Every rule quotes Coach Gen's own words, with the date. A rule that is Claude's proposal and not yet confirmed sits under "Proposed" until he says yes.

---

# 1. WHY A BOOK IS DIFFERENT

His words (4 Oct): **"book has higher standard and differences to approach."**

His score of the first Introduction draft (4 Oct): **"rightnow it's like 80% of what I'm happy for article, but only 40% of book."**

His diagnosis (4 Oct): **"it seems you are being too concise here. no problem, since you were trained on beat to beat articles."** And: **"I feel most of my complaints come from oversuccinct."**

So the default failure in the book is the article habit: one sentence per beat, then move on. Every rule in sections 2 to 4 is a fix for that.

---

# 2. LENGTH AND ROOM

**Word count is not the target. Page count is, and formatting can move it.** His words (1 Oct): "Length doesn't matter now, (this is not an instruction to hallucinate or elongate). I'm mainly concerned about pagecount, that can easily be postmanipulated with formatting."

**Give every beat room.** In round 1, 3 of his 4 comments asked for more, and 1 asked for less. The fix is not padding. It is finishing each beat: set the scene, show the moment, then say the point again in plain words.

**Measured reference.** In *Mindset*, Chapter 1, Carol Dweck spends about 140 words on the puzzle-room scene before the first child's line ("I love a challenge!"), then several paragraphs on what it meant to her. Our round 1 draft gave Melina's line about 30 words of setup and 2 sentences after it.

**Cut details that do not serve the beat, even true ones.** "The first 2 people" (1 Oct): "is unecessary detail." "Before she had ever seen the cover of this book" (4 Oct): "this detail is not important."

---

# 3. SCENES WITH THE PEOPLE HE COACHES

**A coaching moment is a warm conversation, never a transaction.** His words (4 Oct), on "One of them said it in a session": "in a session can definitely be more powerful. session feels transactional. I want to make it feel like I am a great coach, while being a warm interaction. maybe can even add lines to describe how the conversation flowed in that session."

**Set the stage precisely, in words the reader already knows.** His words (4 Oct), on the client's line: "this setting the stage needs to precisely paint the picture of a coaching session and the client's progress, using words readers know and expect."

**Frame the client's line as her own realisation.** His model wording (4 Oct): "So what I realized is that, ...."

**Show the progress before the realisation.** The reader should see where the person started, what she has already done, and then the moment it clicks. (Derived from the two comments above. Round 1 used her 30-minute walk and the work trip she walked through.)

**Real material only.** He asked for the book to be written "like you are a professional writer writing a biography of a famous person, and corresponding with that person for realness to himself" (1 Oct). So: build scenes from what the Testimony collection and his published pieces record. Where a scene needs a detail nobody recorded (what he asked, how she reacted), Claude may draft it, but must list it in chat as a reconstruction and ask him. At most 3 questions per round.

**Composite names on every page.** Melina (Composite B), David (Composite A), Dan Sato (Composite C, no lines yet). The anonymity line sits once in the Introduction.

---

# 4. CLARITY AT BOOK LENGTH

**Never point back at a sentence with "it". Repeat the sentence in paraphrase.** His words (4 Oct), on "For years, I said it about myself too. This book is my answer to it.": "it. is too vague. repeating the sentence in paraphrase would help here."

Annotation: this is the Language Rules' "Reference decay" rule at book scale. In an article the reader can hold a sentence in mind for a line. In a book they need the words again.

---

# 5. OPENINGS AND THE FRONT PAGES

**Open like Dweck.** His words (1 Oct): "I want to open similar to carol dweck's introduction and chapter 1 chapters. it elegantly highlights the importance that this book carries while still being a thought leader."

**Do not repeat the subtitle in the first pages.** His words (1 Oct): "If you keep trying but never finish this is why is repeated 3 times in the first sequence of papers." The cover and the title page carry it. The Introduction does not.

**The Introduction's own first lines.** 1 Oct: "the first line of introduction can be 'I am excited to start a lot of things, but almost never finish anything.'" Then 4 Oct, on Melina's line: "let's try a construction where this sentence is the first sentence." (Epoch 1 tries the second. His 1 Oct line moves to where he says it about himself.)

---

# 6. STRUCTURE AND HEADINGS

**Story sections get real names.** His words (1 Oct): "Let's give Act1/act2/act proper names. just like bestselling books. if like act in this case of being just after the title, no need."

**Chapter 1 is the opening chapter, about the pattern. The Laws come after it.** (1 Oct: "yes of course ch1 is opening.")

**The form.** Atomic Habits as the model. "Also I like the classic self help structuring, styling, how they handle exercise blocks." (1 Oct)

---

# 7. THE READER

His words (1 Oct): "anyone who keeps trying but never finishes and is frustrated of this pattern about themselves. introvert is a subset of this that I happen to specialize on, when the problem to change is confidence/speaking and the identity clang is introverted."

---

# 8. PROPOSED, NOT YET CONFIRMED

**Draft long, he trims.** Claude's recommendation (4 Oct), after he asked "according to gold standards, is it better to write long and then trim or viceversa?" Basis: most professional advice drafts long and cuts (Stephen King's "2nd Draft = 1st Draft – 10%"). For this team, cutting costs him one strike-through, while adding costs him a comment and a round. Confirm or reject.

---

# 9. BENCHMARK: EPOCHS ON THE INTRODUCTION

His plan (4 Oct): **"I think a good benchmarking is to train and epoch on the introduction."**

**One epoch:**
1. Claude redrafts the whole Introduction from the current rules. His own typed words stay word for word.
2. Coach Gen marks it up in the Google Doc and gives one score: "x% as a book."
3. Claude logs his notes word for word below, with the rule each one produced, and adds the rule above.
4. Next epoch.

An epoch is a full redraft, not a patch. Patching one line at a time is how the article habit survives. A full redraft tests whether the rules work on their own.

## Epoch log

**Epoch 0 (the round 1 draft, 1 to 4 Oct).** Score: 80% as an article, 40% as a book.
Notes, word for word:
> "If you keep trying but never finish this is why is repeated 3 times in the first sequence of papers." → section 5
> "the first line of introduction can be 'I am excited to start a lot of things, but almost never finish anything.'" → section 5
> "'The first 2 people' is unecessary detail." → section 2
> "in a session can definitely be more powerful. session feels transactional..." → section 3
> "this detail is not important." → section 2
> "'So what I realized is that, .... ' this setting the stage needs to precisely paint the picture of a coaching session and the client's progress, using words readers know and expect." → section 3
> "it. is too vague. repeating the sentence in paraphrase would help here" → section 4
> "let's try a construction where this sentence is the first sentence" → section 5, applied in epoch 1

**Epoch 1 (4 Oct).** Drafted. Awaiting his markup and score.

---

# 10. REFERENCE SHELF

Books and style guides he likes, measured, never copied. Each entry: what he likes about it in his words, and the numbers.

**Carol Dweck, *Mindset* (updated edition).** Read 1 Oct.
- Why (his words): "it elegantly highlights the importance that this book carries while still being a thought leader."
- Introduction: about 2 pages. Why the book exists, in one scene. The promise in one belief. The anonymity note in brackets, inside the paragraph about where the stories come from. How to use the book. One closing line.
- Chapter 1: opens on one scene from early in her career, about 140 words before the first quoted line. Section headings in capitals. One boxed exercise at the end.
