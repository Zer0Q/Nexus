---
title: "How to Build an Obsidian Second Brain With AI: The Complete Guide Based on Karpathy's Framework"
source: "https://x.com/cyrilXBT/status/2059817560988676179"
author:
  - "[[@cyrilXBT]]"
published: 2026-05-28
created: 2026-05-31
description: "Andrej Karpathy does not use Obsidian as a note-taking app.He uses it as a thinking partner.The distinction sounds subtle. The difference in..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HJVVio3XIAA8q_f?format=jpg&name=large)

Andrej Karpathy does not use Obsidian as a note-taking app.

He uses it as a thinking partner.

The distinction sounds subtle. The difference in outcome is enormous.

A note-taking app is a place you put information so you do not have to remember it.

A thinking partner is a system that processes information, makes connections, challenges your assumptions, and produces output that advances your thinking rather than just storing it.

Karpathy's framework for building a second brain with AI is built on one insight that most productivity content completely misses.

The value of a second brain is not in what you put into it.

It is in what comes back out.

A vault full of notes that never gets read, never surfaces relevant connections, and never produces synthesis is not a second brain. It is an expensive filing cabinet.

The Obsidian second brain built on Karpathy's framework is designed from the output end. Every structural decision, every capture convention, every Claude integration is optimized for one thing: producing useful output from accumulated knowledge without requiring you to manually retrieve it.

This guide is the complete implementation.

## The Karpathy Insight That Changes Everything

Before the build understand the core principle.

Karpathy's approach to thinking with LLMs is not about asking better questions.

It is about building better context.

His argument is that the quality of AI output is almost entirely determined by the quality of context provided. Not by the model. Not by the prompt. By the context.

A generic question to a generic Claude session produces a generic answer.

The same question asked by a Claude instance that has been loaded with three years of your specific thinking, your specific knowledge domain, your specific ongoing projects, and your specific intellectual frameworks produces something categorically different.

The second brain built on Karpathy's framework is primarily a context-building machine.

Every note you capture is a piece of context that makes every future Claude interaction more intelligent.

Every connection you make between notes is a piece of reasoning that Claude can draw on when you need it.

Every synthesis you produce becomes a building block for the next synthesis.

The vault compounds because the context compounds.

## The Four Layers of the Karpathy Second Brain

The framework has four distinct layers. Each one serves a different function. Each one compounds differently.

**Layer 1: The Knowledge Layer**

Raw captured information. Notes, ideas, facts, references, observations. Everything you take in from reading, conversations, research, and experience.

This layer answers the question: what do I know.

**Layer 2: The Connection Layer**

Explicit links between notes that capture how ideas relate to each other. Not just filing notes in folders. Creating networks of meaning by linking concepts that share a relationship.

This layer answers the question: how does what I know fit together.

**Layer 3: The Synthesis Layer**

Outputs produced by combining information from multiple notes into a new understanding that no individual note contains. Maps of content, analysis documents, position statements, and frameworks.

This layer answers the question: what does what I know mean.

**Layer 4: The Intelligence Layer**

Claude connected to the vault via MCP, reading across all three layers simultaneously, making connections you did not make, surfacing relevant history when you need it, and producing outputs that your accumulated knowledge enables but that you could not produce manually.

This layer answers the question: what can I do with what I know.

Most second brain implementations build Layer 1 and partially build Layer 2. They stop there.

The Karpathy framework builds all four and designs them to work together.

## The Vault Architecture

The structure of your vault is the architecture of your thinking.

A vault organized by topic mirrors how a library organizes books. Useful for retrieval by category. Poor for surfacing unexpected connections between categories.

Karpathy's approach organizes by type of thinking rather than by topic.

00 - INBOX/ \[raw captures before processing\] 01 - LITERATURE/ books/ \[author-title\].md articles/ \[YYYY-MM-DD-title\].md papers/ \[author-year-title\].md videos/ \[YYYY-MM-DD-title\].md 02 - PERMANENT/ concepts/ \[concept-name\].md people/ \[person-name\].md questions/ \[open-question\].md 03 - PROJECTS/ \[project-name\]/ overview.md notes/ outputs/ 04 - DAILY/ \[YYYY-MM-DD\].md 05 - MAPS/ \[topic\]-map.md 06 - OUTPUTS/ essays/ analyses/ frameworks/ 07 - SYSTEM/ CLAUDE.md skills/ templates/

The critical distinction is between Literature notes and Permanent notes.

Literature notes capture what a source said. They are temporary processing stations. You read a book, you make a literature note summarizing what the book said, and then you process that literature note into permanent notes.

Permanent notes capture what you think. They are the atoms of your second brain. A permanent note about a concept contains your understanding of that concept in your own words, synthesized from multiple sources, connected to other concepts you know.

Karpathy's principle: you do not own knowledge until you can express it in your own words in a way that connects it to what you already know.

Literature notes are raw material.

Permanent notes are refined understanding.

## The Note-Making Process

The process that transforms raw captures into genuine knowledge is the most important habit in the entire system.

Most people take notes and stop.

The Karpathy framework has four stages that turn a note into a permanent asset.

**Stage 1: Capture**

When you encounter something worth keeping add it to the Inbox folder. Do not think about where it goes. Do not try to write it properly. Just capture the raw idea or reference.

Speed at capture time is the goal. The Inbox processes later.

**Stage 2: Literature Note**

For any source you engage with seriously create a literature note.

A literature note answers three questions: what did this source argue, what was the evidence, what do I think about it.

It does not summarize everything. It captures what is worth capturing.

\--- type: literature source: \[TITLE\] author: \[AUTHOR\] date\_read: \[DATE\] status: processed --- # \[TITLE\] — \[AUTHOR\] ## The Core Argument \[One paragraph: what is the main claim\] ## Key Evidence \[Bullet points: specific evidence or examples\] ## My Reaction \[Your genuine response: what do you agree with, what do you doubt, what does this connect to\] ## Notes to Process \[Specific ideas worth turning into permanent notes\]

**Stage 3: Permanent Note**

For each idea flagged in the literature note create a permanent note.

A permanent note is atomic. It contains one idea. It is written in your own words. It links to every other note that is related.

\--- type: permanent tags: \[relevant-topics\] created: \[DATE\] --- # \[CONCEPT NAME\] \[Your explanation of this concept in your own words. Not what anyone else said about it. What you understand it to mean after thinking about it.\] ## Why This Matters \[Why does this concept matter for the questions you care about\] ## Connections - \[\[Related Concept 1\]\] — \[how they connect\] - \[\[Related Concept 2\]\] — \[how they connect\] - \[\[Opposing Concept\]\] — \[the tension between them\] ## Source From: \[\[Literature Note Title\]\]

**Stage 4: Map of Content**

When enough permanent notes accumulate around a topic create a Map of Content.

A Map of Content is a note that links to all the permanent notes about a topic and adds a brief commentary on how they fit together.

It is the synthesis layer. The place where individual ideas become a coherent understanding.

## The CLAUDE.md That Powers the Second Brain

The CLAUDE.md file transforms your vault from a static knowledge base into a dynamic thinking partner.

\# Second Brain — CLAUDE.md ## Identity and Focus Name: \[YOUR NAME\] Primary intellectual interests: \[WHAT YOU THINK ABOUT MOST\] Professional domain: \[YOUR FIELD\] Current questions: \[THE BIG QUESTIONS YOU ARE WORKING ON\] ## Vault Structure 00 - INBOX: Raw unprocessed captures 01 - LITERATURE: Notes from external sources 02 - PERMANENT: Atomic notes in my own words 03 - PROJECTS: Active work 04 - DAILY: Daily notes 05 - MAPS: Topic syntheses 06 - OUTPUTS: Finished writing ## My Intellectual Framework \[Describe how you think. What frameworks you use. What you value in arguments. What makes an idea interesting to you.\] ## Current Intellectual Projects \[What you are actively trying to figure out. What questions are live in your thinking.\] ## How to Help Me Think When I ask a question: - Draw on relevant permanent notes from my vault - Surface connections I have not made explicitly - Challenge my assumptions using evidence from my own notes - Tell me when my thinking contradicts something I have written elsewhere When I am writing: - Help me find the relevant permanent notes - Identify gaps in my argument - Suggest connections to other things I have written - Push back on claims that lack support ## What I Do Not Want - Generic information not grounded in my specific vault - Summaries of what I already know - Answers that do not draw on my accumulated notes

## The Six Claude Integrations That Make the Brain Alive

Connecting Claude to your vault via MCP turns the accumulated knowledge into an active thinking partner. These six specific interactions are where Karpathy's framework produces its most distinctive value.

Integration 1: The Inbox Processor

Every evening drop a message into Claude:

Process my Obsidian Inbox. For each file in 00 - INBOX: 1. Identify what type of note it should become 2. If it is a reference to a source: create a literature note template for it 3. If it is a raw idea: assess whether it deserves a permanent note or can be added to an existing one 4. If it is a task: add it to the relevant project 5. Archive the inbox file after processing Report what you created and why.

The inbox processes itself every evening. Raw captures become structured notes without manual filing.

Integration 2: The Connection Finder

Once per week:

Read all permanent notes created or modified in the last 7 days. Search my entire vault for existing notes that connect to these new notes. For each connection found: - Name both notes - Explain specifically how they connect - Suggest the link text I should use when adding the connection Only surface non-obvious connections. Skip anything already linked.

This is the integration that makes the second brain genuinely intelligent. You write a note about one thing. Claude finds the note you wrote three years ago that connects to it. You would never have found that connection manually.

Integration 3: The Question Answerer

Any time you have a question about your own domain:

I have a question: \[YOUR QUESTION\] Before answering from general knowledge, first search my vault for: - Permanent notes directly relevant to this question - Literature notes that address it - Daily notes where I have thought about it before - Any Maps of Content covering this topic Tell me what my own notes say about this question before you add anything from outside my vault. Then tell me where my existing thinking has gaps that need new information to fill.

This integration embodies the core Karpathy insight. The answer you need is often already in your vault. Claude reads across it and surfaces your own prior thinking before reaching for external knowledge.

Integration 4: The Writing Assistant

When writing anything serious:

I am writing about: \[TOPIC\] Read all permanent notes and maps of content related to this topic in my vault. Tell me: 1. What is the strongest argument my notes support 2. What evidence exists in my vault for that argument 3. What counterarguments my own notes raise 4. What connections would strengthen the piece 5. What is missing from my vault that I should research before writing Then help me structure the argument using only what my notes actually support.

Writing becomes a process of articulating what your accumulated knowledge already knows rather than starting from a blank page.

Integration 5: The Contradiction Detector

Monthly:

Read all permanent notes in my vault. Identify any notes where I appear to hold contradictory positions. For each contradiction found: - State the two contradictory claims - Quote the relevant sections from each note - Ask me to clarify my actual position I want to know where my thinking is inconsistent so I can resolve the contradiction or understand why I hold both positions.

This integration produces the kind of intellectual honesty that is difficult to maintain manually. Your own vault becomes the evidence used to challenge your own thinking.

Integration 6: The Synthesis Generator

When enough notes have accumulated on a topic:

Read all permanent notes tagged with \[TOPIC\] and all notes linked from the \[TOPIC\] Map of Content. Generate a synthesis that: 1. Identifies the central claim my notes support 2. Organizes the supporting evidence hierarchically 3. Names the tensions and unresolved questions 4. Suggests the next questions worth investigating This synthesis should go beyond any individual note in my vault. It should be something only possible by reading all of them together. Save the synthesis to 06 - OUTPUTS/\[TOPIC\]-synthesis.md

The synthesis integration is where compound knowledge becomes compound output. The insight available from reading across fifty notes on a topic is not available from any individual note.

## The Daily Practice

The second brain only compounds if it is used daily.

The daily practice has three components that take fifteen minutes combined.

**Morning: Read and Set Intention**

Open your daily note. Check the questions you are currently working on in your CLAUDE.md. Set one intellectual intention for the day: one question to think about, one connection to explore, one piece to write.

Five minutes.

**During the Day: Capture Without Friction**

Every idea, observation, or reference worth keeping goes directly to the Inbox folder. No filing decisions. No thinking about where it goes. Just capture.

Zero extra time. This replaces the mental note you would have taken anyway and lost.

**Evening: Process and Connect**

Trigger the Inbox Processor. Review the output. Approve or adjust the filing decisions Claude made. Add one link you notice between a new note and an existing one.

Ten minutes.

That is the entire daily practice.

Fifteen minutes per day.

The compounding happens in the background.

## What Changes After 90 Days

The Karpathy second brain is not impressive after one week.

It becomes impressive over time as the context layer accumulates.

At day 30 you have enough permanent notes for the Connection Finder to start surfacing genuinely surprising links. Notes you wrote in week one connect to notes you wrote in week four in ways you did not consciously intend.

At day 60 the Question Answerer starts producing answers grounded in your own prior thinking that you had genuinely forgotten you had done. You ask a question and Claude finds the answer in a note you wrote six weeks ago.

At day 90 the Synthesis Generator produces its first output that surprises you. A synthesis of everything you have written about a topic reveals a position you hold more confidently than you realized because the evidence was distributed across fifty notes rather than concentrated in one place.

Karpathy's framework produces something that almost no other productivity system claims to produce: genuine intellectual growth that is measurable and traceable.

You can look at a synthesis produced at day 90 and trace every claim back through the permanent notes to the literature notes to the sources that generated them.

Your thinking is not just better.

It is auditable.

## The Difference Between This and Every Other Second Brain Guide

Most second brain guides teach you how to capture more.

Karpathy's framework teaches you how to think better.

The difference is the output orientation.

Every structural decision in this framework is made by asking: does this make my thinking better or does it just make my filing neater.

Permanent notes over literature notes because synthesis beats storage.

Maps of Content over folder hierarchies because navigating ideas beats filing them.

Claude integrations over manual review because intelligence beats retrieval.

Daily synthesis over weekly reviews because compounding beats accumulating.

The second brain built on this framework is not a place to keep things.

It is a system for becoming smarter.

Build the foundation this weekend.

Create the vault structure. Write your first literature note. Process it into three permanent notes. Write your CLAUDE.md. Connect Claude via MCP and run the first Inbox Processor.

Fifteen minutes per day from that point forward.

The second brain that Karpathy describes is not a tool you use.

It is a thinking system that compounds alongside you.

Build it this weekend.

Follow [@cyrilXBT](https://x.com/@cyrilXBT) for every Obsidian system, Claude integration, and thinking framework that makes your second brain compound over time.