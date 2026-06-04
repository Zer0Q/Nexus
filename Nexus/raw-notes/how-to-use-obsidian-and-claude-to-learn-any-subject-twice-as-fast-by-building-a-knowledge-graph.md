---
title: "How to Use Obsidian and Claude to Learn Any Subject Twice as Fast by Building a Knowledge Graph."
source: "https://x.com/neil_xbt/status/2060607326206206232"
author:
  - "[[@neil_xbt]]"
published: 2026-05-30
created: 2026-05-30
description: "The way most people study feels like learning but produces almost none of it.They read the chapter. They highlight the key sentences. They r..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HJi-eagXsAAqa-a?format=jpg&name=large)

**The way most people study feels like learning but produces almost none of it.**

They read the chapter. They highlight the key sentences. They review their highlights. They feel the comfortable familiarity of material they have seen before and mistake that familiarity for understanding. Then they sit down for the exam, or try to apply the knowledge in a real situation, and discover that familiarity is not the same thing as being able to use something.

The research on this is unambiguous. Passive review of study material by re-reading notes or highlighting textbooks creates a false sense of familiarity rather than true understanding. The most popular study methods are also the least effective. Re-reading creates an illusion of knowledge. Highlighting produces passive engagement with zero retrieval practice. Cramming the night before works for roughly twenty-four hours and then it is gone.

What actually works is the opposite of what feels comfortable. Active recall: the deliberate effort to retrieve information from memory rather than passively review it. Spaced repetition: reviewing material at increasing intervals over time rather than massed practice sessions. The discomfort of not being able to remember something is not evidence that you are failing to learn. It is evidence that learning is happening.

Research by Roediger and Karpicke showed that students who spent more time testing themselves through active recall retained significantly more information a week later than students who spent the same amount of time in passive review. Combining spaced repetition with active recall improved exam performance by fifteen to twenty percent compared to traditional study schedules, according to a 2025 study published in BMC Medical Education.

The Obsidian and Claude learning system described in this article builds both mechanisms into the study process itself.

Every concept you add to your vault is immediately tested, connected, and scheduled for review. The knowledge graph does not replace studying. It transforms what studying means.

## The Problem With Studying in Isolation

Before the system, the problem.

Traditional note-taking is linear. You read in sequence and write in sequence. Concept A appears on page twelve, concept B on page twenty, and concept C on page forty-five. Nothing in the act of writing down concept C connects it to concept A even when they are deeply related. The connections exist in the subject matter. They do not exist in your notes unless you deliberately create them.

The connection is where the understanding lives.

A student who knows that concept A, concept B, and concept C each exist has surface familiarity with three separate facts. A student who understands that concept A causes concept B under certain conditions, that concept C is the mechanism that explains when those conditions arise, and that this relationship maps onto a real-world pattern they have already observed has understanding. The second student is not smarter. They built the connections. The first student collected isolated nodes.

The knowledge graph approach changes the structure of the notes from a collection of nodes to a network of connected nodes. Every new concept added to the graph is not stored in isolation. It is connected to what is already there. The tenth concept is more valuable than the first because there are nine existing concepts for it to connect to. The fiftieth is more valuable than the tenth for the same reason.

Claude accelerates this in two ways. First, it finds connections that you would not have found yourself, because it can reason across everything in your vault simultaneously in a way your sequential reading brain cannot. Second, it generates the retrieval practice that forces you to pull information from memory rather than passively review it, which is where the actual learning occurs.

## The Vault Structure for Learning

This system uses a focused structure designed specifically for knowledge acquisition rather than the general second brain vault described elsewhere. You can build this as a standalone vault or as a sub-section of an existing Obsidian vault.

```text
learning-vault/
├── CLAUDE.md              (system instructions)
├── 00-active/
│   └── [subject]/         (current study area)
├── 01-concepts/
│   └── [concept-name].md  (one file per concept)
├── 02-connections/
│   └── [link-name].md     (explicit relationship notes)
├── 03-questions/
│   └── YYYY-MM-DD.md      (active recall questions)
├── 04-reviews/
│   └── [concept]-review.md (spaced review schedule)
├── 05-synthesis/
│   └── [topic]-synthesis.md (integrated understanding documents)
└── 06-skills/
    ├── concept-add.md
    ├── connection-find.md
    ├── recall-generate.md
    └── review-schedule.md
```

The CLAUDE.md for this vault:

```text
# Learning Vault — CLAUDE.md

## Purpose
This vault is a knowledge graph for active learning.
Every concept is a node. Every relationship between 
concepts is a link. The goal is not to store information.
The goal is to build understanding through connection.

## Core Principle
A fact stored in isolation is forgotten.
A fact connected to five other facts is retained.
Every concept added must be connected to at least 
two existing concepts before it is considered complete.

## Claude's Role
1. Find non-obvious connections between concepts
2. Generate active recall questions that test understanding
3. Schedule spaced reviews at scientifically optimal intervals
4. Identify gaps where connections are missing
5. Produce synthesis documents that integrate related concepts

## What Claude Never Does
Never create a summary that just restates the source.
Summaries do not produce learning. Connections do.
If a concept note does not link to anything, it is incomplete.
```

## Module 1: The Concept Note

Every piece of material you study gets added to the vault as a concept note. Not a page summary. Not a chapter outline. A concept note captures one idea precisely enough to be tested on and connected to other ideas.

The structure of every concept note is the same:

```text
---
concept: [name]
subject: [subject area]
source: [where this came from]
date-added: YYYY-MM-DD
review-due: YYYY-MM-DD
connections: []
mastery: 0
---

# [Concept Name]

## What It Is
[The concept explained in your own words. Not the source's 
words. Your words. If you cannot write this section, 
you do not understand it yet.]

## Why It Matters
[What problem does this concept solve or what question 
does it answer?]

## The Mechanism
[How does it work? What are the moving parts?]

## Where It Breaks Down
[Under what conditions does this concept not apply, 
fail, or produce incorrect predictions?]

## Connections
[Links to other concept notes — added by Claude]

## The Test
[Active recall question generated by Claude]
```

The "What It Is" section, written in your own words, is the most important part. Not a copy of the source text. Your words. The cognitive effort of translating from source language to your language is the first act of retrieval practice. If you cannot write it in your own words, you have encountered the gap before Claude has to surface it for you.

After writing the first three sections yourself, trigger Claude:

```text
Read this concept note: [paste the note]

Read my existing concept notes for [subject].

Do three things:
1. Find at least two connections to existing concepts 
   and add them to the Connections section. For each 
   connection, write one sentence explaining what the 
   relationship reveals.
2. Identify the single most important thing this concept 
   needs to be connected to that I have not connected it 
   to yet.
3. Write one active recall question for the Test section 
   that requires application, not definition. The question 
   should be impossible to answer correctly just by 
   memorizing the definition.
```

The active recall question is the key output of this step. Not "define concept X." That tests familiarity.

A question that requires application tests understanding. "Given situation Y, which of these three approaches would concept X suggest and why?" That question cannot be answered by someone who only memorized the definition.

## Module 2: The Connection Protocol

The connection protocol runs at the end of every study session. Its purpose is to find the connections between new concepts and existing ones that you did not see while studying.

This is where the knowledge graph produces its most distinctive value. You studied sequentially. The graph stores non-sequentially. Claude can read across everything in your vault simultaneously and find patterns that your sequential study session could not produce.

After adding three to five new concept notes in a session, run this prompt:

```text
I have just added [N] new concept notes to my learning vault 
on [subject]. I am also studying [related subjects in the vault].

Read all the new concepts I added today and all existing 
concepts in the vault.

Find three non-obvious connections I probably missed:

For each connection:
1. Name the two concepts being connected
2. Write the relationship in one precise sentence 
   (not "these are related" — what is the specific 
   relationship?)
3. Explain why this connection matters for understanding 
   the subject deeply
4. Generate one question that can only be answered by 
   someone who understands both concepts and their 
   relationship

Non-obvious means: not mentioned in either concept note 
already, and not immediately apparent from the surface 
descriptions of both concepts. The connection should 
produce an insight that neither concept produces alone.
The non-obvious connection requirement is the critical instruction. Without it, Claude finds the obvious links: concept A is similar to concept B, concept C relates to concept D. Those connections are useful but not the ones that produce understanding.
```

The non-obvious connection is the one where understanding the relationship changes how you understand both concepts individually. In chemistry, understanding the relationship between electron configuration and reactivity does not just connect two facts. It explains a pattern that predicts dozens of other relationships across the entire subject. Finding that connection early restructures everything that comes after it.

## Module 3: The Active Recall Generator

Active recall is a study method where students test themselves to enhance memory retention, and the research consistently shows it produces dramatically better outcomes than any passive review method. The challenge is that generating good active recall questions is time-consuming and most self-generated questions are too easy, asking for definitions rather than application.

Claude generates the questions. You answer them. The vault tracks which ones you get right.

Once per study session, run this prompt:

```text
Generate an active recall session for my learning on [subject].

Pull questions from:
- Concept notes added in the last 7 days (recent material)
- Concept notes with mastery score below 3 (weak areas)
- One connection question from 02-connections/ (integration test)

Generate 10 questions in this format:

For each question:
- Question type: [application / analysis / connection / prediction]
- The question itself
- What a correct answer requires (not the answer — what 
  demonstrates understanding)
- Which concept note this tests

Rules for questions:
- Never ask for a definition
- At least 3 questions must require connecting 
  two or more concepts
- At least 2 questions must ask the student to 
  predict what would happen in a novel situation

After I answer each question, evaluate:
- Whether my answer demonstrates actual understanding
- What my answer reveals about gaps in my knowledge
- Whether the mastery score for that concept should 
  increase, stay the same, or decrease
```

Answer each question before reading the evaluation. Cover the evaluation section. Write your answer. Then read what Claude says about the answer.

The mastery score in the frontmatter of each concept note is updated after every recall session. A concept with a mastery score of five or above moves to a longer review interval. A concept that you consistently answer incorrectly is flagged for the synthesis session rather than more repetition.

## Module 4: The Spaced Review System

Spaced repetition is based on Hermann Ebbinghaus's forgetting curve, the discovery that we forget roughly 70% of new information within 24 hours unless we review it at strategic intervals.

The review schedule in this vault is built into the frontmatter of every concept note. The review-due field is updated after every recall session based on performance.

The intervals follow the established spaced repetition pattern:

- First review: 1 day after initial study
- Second review: 3 days after first review
- Third review: 7 days after second review
- Fourth review: 14 days after third review
- Fifth review: 30 days after fourth review
- Subsequent reviews: 60 days

Mastery score determines interval adjustment. Answer the recall question correctly: move to next interval. Answer incorrectly: reset to the previous interval.

Run this prompt at the start of every study session:

```text
Read all concept notes in 01-concepts/ where review-due 
is today or earlier.

Generate the review session:
1. List every concept due for review today with its 
   current mastery score
2. Sort by mastery score, lowest first (weakest concepts 
   reviewed with highest attention)
3. For each concept, generate one review question 
   harder than the previous session's question for 
   that concept
4. After I complete the session, update the review-due 
   dates in each concept note based on my performance

Today's date: [date]
```

The review session takes fifteen to twenty minutes. It covers every concept that is on the verge of being forgotten. The concepts you know well appear less frequently. The concepts you are still developing appear more often.

This is what produces the compression in learning time. Spaced repetition stops the forgetting curve by timing reviews at the point of near-forgetfulness. You are never re-reviewing material you have already fully retained. Every review minute is spent on the exact material that needs it.

## Module 5: The Synthesis Session

Active recall and spaced repetition build the nodes and maintain them. The synthesis session builds the integrated understanding that makes the knowledge usable rather than just retained.

Synthesis is where isolated competence becomes real understanding. A student who can answer questions about ten separate concepts has studied well. A student who can explain how those ten concepts interact to produce a phenomenon, predict what would happen when conditions change, and identify where the conventional explanation is incomplete has understood the subject.

Run a synthesis session every two weeks per subject:

```text
I have been studying [subject] for [duration].
My concept notes cover: [list your main concept areas]

Run a synthesis session:

1. PATTERN IDENTIFICATION
   Read across all concept notes in this subject.
   What patterns emerge that are not stated explicitly 
   in any individual concept note?

2. THE DEEPEST CONNECTION
   What is the single most important relationship 
   in this subject that ties the most concepts together?
   What would a student miss if they never understood 
   this relationship?

3. THE PREDICTIVE TEST
   Given what I have learned, generate three novel 
   scenarios I have not studied. For each one, tell 
   me what my knowledge graph predicts would happen 
   and why.
   (Do not tell me the answers — ask me to predict 
   first, then evaluate my predictions.)

4. GAP ANALYSIS
   Based on what I know and do not know, what are the 
   three most important concepts I have not yet studied 
   that would most increase my understanding of what 
   I have?

5. SYNTHESIS DOCUMENT
   Write a synthesis document (400-600 words) that 
   integrates the most important concepts into a 
   coherent understanding of the subject.
   This should read like something a genuine expert 
   would write, not like a list of facts.
   Save to 05-synthesis/[subject]-synthesis.md
```

The synthesis document is the artifact that proves understanding rather than familiarity. If you can read the synthesis document and recognize every claim as something you genuinely understand, you are ready for any application of this knowledge. If you read it and encounter claims you cannot explain, you have identified the next round of study.

## What the System Produces That Passive Study Cannot

Retrieval practice creates stronger and more durable memory traces, improving the long-term retention rate and applicability of knowledge. The Obsidian and Claude learning system is essentially a systematic retrieval practice machine that runs continuously as you study.

Every concept note you write is a retrieval practice act. Writing in your own words forces retrieval. The recall questions force retrieval again at increasing intervals. The synthesis sessions force retrieval across the entire knowledge graph simultaneously.

The knowledge graph adds something that standard spaced repetition systems like Anki do not produce: the connections. Individual flashcards test individual facts. The connection protocol and synthesis sessions test relationships, which is where understanding lives.

The practical result is measurable. Students who combine spaced repetition with active recall improve exam performance by fifteen to twenty percent compared to those using traditional study schedules. The system described here implements both, adds the connection layer, and runs the scheduling automatically. The compression in learning time comes not from studying harder but from studying in a way that produces retention on the first pass rather than requiring multiple passes through the same material.

## Starting This Weekend

You do not need a complete vault setup before you begin. You need three things to start today.

Create one concept note in the format described above for the most important concept in whatever you are currently studying. Write the "What It Is" section in your own words. If you struggle to write it without looking at your source, you have already identified your first gap.

Run the connection prompt on that first note against whatever else you already have in Obsidian, or even against a brief description of what you are studying if the vault is empty. Read what Claude identifies as the missing connections.

Write down your answer to the recall question Claude generates without looking at the concept note. Evaluate honestly whether you answered it correctly.

Three actions. Thirty minutes. The entire difference between passive study and active learning is in those thirty minutes.

The subject you have been trying to learn is not difficult. The method you have been using to learn it is. Passive review feels productive and produces almost nothing. Active recall with connection-building feels harder and produces retention that lasts.

The knowledge graph is the difference between knowing things and understanding them.

**The vault is available. The tool is free.**

**The only variable is whether you build the first concept note today or continue highlighting things you will forget by next week.**