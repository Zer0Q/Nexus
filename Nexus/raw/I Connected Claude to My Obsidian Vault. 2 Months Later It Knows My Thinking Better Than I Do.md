---
title: "I Connected Claude to My Obsidian Vault. 2 Months Later It Knows My Thinking Better Than I Do."
source: "https://x.com/DamiDefi/status/2057770204130582976"
author:
  - "[[@DamiDefi]]"
published: 2026-05-22
created: 2026-05-26
description: "Eight weeks ago Claude surfaced a connection I had completely missed.I had a note from six weeks prior about how attention scarcity was driv..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HI4Z7y_WMAAWY-g?format=jpg&name=large)

Eight weeks ago Claude surfaced a connection I had completely missed.

I had a note from six weeks prior about how attention scarcity was driving premium pricing in crypto. Sitting three folders away was a capture from a podcast about how scarcity mechanics in gaming drove in-app purchase behaviour. I had never linked these two ideas. They lived in completely separate parts of my brain.

Claude found them in 11 seconds and wrote a one-paragraph synthesis that became one of my best-performing posts.

That moment changed how I think about what a second brain is actually supposed to do.

## The Problem With Every Obsidian Setup You Have Read About

Most Obsidian guides teach you how to organise information. Better folder structures. Smarter tagging systems. Prettier dashboards.

None of that is the point.

Organisation is just a faster way to find something you already know exists. It does not create new knowledge. It does not surface what you forgot. It does not connect ideas that live in different parts of your vault.

After two months of running Claude as the intelligence layer on top of Obsidian, I now have a vault that does all three automatically. Every morning before I open anything else, Claude has already been through my recent captures and produced a synthesis of what it noticed. Not a summary. An actual output: connections I missed, patterns forming across weeks of notes, questions worth thinking about that day.

The difference between an organised vault and an intelligent one is the difference between a library and a researcher.

Here is exactly how the system is built.

## The Four Layers

Everything runs on four components. Remove any one of them and the system degrades into a slightly fancier note-taking app.

![Imatge](https://pbs.twimg.com/media/HI4YcHLWoAAipmD?format=jpg&name=large)

**Layer 1: Capture (Zero Friction)**

The system dies if capture requires effort. Every time you have to think about where something goes, you are burning willpower that should go toward thinking about the content itself.

Readwise handles everything I read. Every highlight from articles, books, PDFs, and newsletters flows automatically into Obsidian via the Readwise Official plugin. I do not touch it. I highlight, it appears.

For voice notes, Whisper transcribes them on my phone before they hit the vault. I speak the idea, the text lands in my inbox folder within a minute.

For X and web content, a Telegram bot catches anything I forward to it. I find something worth saving, I forward it to the bot, it writes the note and files it.

The rule: if saving something takes more than three seconds, the friction is too high and the system will fail over time.

**Layer 2: Automation (N8N as the Router)**

N8N runs in the background connecting everything together. It handles three specific jobs.

First, it takes the daily output from Readwise and formats it into structured notes before they land in Obsidian. Each note gets a date, a source tag, and a content type tag automatically. No manual tagging.

Second, it runs a nightly sweep that checks my inbox folder for anything uncategorised and moves items to the correct capture subfolder based on content type. Observations go to one place. Reactions go to another. Questions, numbers, and patterns each have their own home.

Third, it triggers the Claude synthesis every morning at 6am by passing the last 7 days of captures to Claude with the synthesis prompt. The output lands in a daily note waiting for me when I open my laptop.

N8N is free to self-host. The entire automation layer costs nothing to run once it is set up.

**Layer 3: Memory (Obsidian as the Context Layer)**

Obsidian is not the intelligence in this system. It is the memory. The distinction matters.

Everything is organised by note type, not by topic. This is the single most important architectural decision in the whole setup and most people get it wrong.

When you organise by topic, a note about attention economics in crypto and a note about attention mechanics in gaming live in completely separate folders and never encounter each other. When you organise by type, they both land in the patterns folder and Claude can find the connection between them.

My folder structure has six subfolders inside Captures: observations, reactions, patterns, questions, numbers, and references. Every note goes into one of these based on what kind of thinking it represents, not what it is about.

The CLAUDE.md file lives at the top of the vault and tells Claude everything it needs to know about who I am and how to reason about my notes. This file is what separates generic AI outputs from outputs that feel like they came from inside my work.

**Layer 4: Intelligence (Claude as the Cognitive Partner)**

This is where everything changes.

Most people use Claude with no context. They open a new chat, ask a question, get an answer, close the tab. The output is as good as whatever they typed in the prompt box.

With the vault connected, Claude is not answering a question. It is reasoning across months of accumulated thinking. It knows which ideas I keep returning to. It knows which questions I have not resolved. It knows which claims I have saved that contradict each other.

That context is what produces genuinely surprising output.

## The CLAUDE.md File

This is the most important file in the entire system and the one most people building this skip.

CLAUDE.md teaches Claude how to think alongside you specifically. Without it, every synthesis Claude produces is generic. With it, the outputs are calibrated to your thinking, your projects, your voice, and your unresolved questions.

Here is the template I use:

**Prompt**

> \# Vault Intelligence System## Who I Am My name is \[name\]. I work at the intersection of \[your domains\]. My audience is \[describe them specifically\]. My content pillars are \[list 2-3\].## What I Am Building \[One paragraph describing your current projects and goals\]## How This Vault Works Every note is raw material for thinking, content, or decisions. Notes are organised by type not topic. - Observations: things I noticed, unpolished - Reactions: my honest gut response to something - Patterns: the same principle in two different domains - Questions: things I genuinely do not know yet - Numbers: real data points with the source - References: saved content for future use## My Thinking Style \[Describe how you think: do you reason from first principles, from analogies, from data?\] \[What kinds of connections excite you?\] \[What questions do you keep returning to?\]## What I Want From You Surface connections I missed. Find contradictions between notes I saved weeks apart. Identify patterns forming across multiple captures. Flag questions that keep appearing without resolution. Never summarise. Always synthesise.## Hard Rules Do not produce generic insight. Every output must contain at least one connection traceable to a specific note. If you are pattern-matching to general knowledge rather than my notes, say so.

Fill every section with real specifics. A vague CLAUDE.md produces vague outputs. The more specific the context, the sharper the synthesis.

## The Daily Synthesis Prompt

This runs every morning via N8N at 6am. It passes the last 7 days of new captures to Claude and returns the synthesis to a daily note.

**Prompt**

> You have access to my recent Obsidian captures from the last 7 days. Read all of them across every subfolder.Produce a daily synthesis with exactly four sections:1. Connections: Two or three non-obvious links between notes I captured separately. Each connection must reference the specific notes by title. If the connection is obvious, it does not qualify.2. Patterns: Any theme, argument, or idea that appears across three or more notes. Name the pattern in one sentence. List the notes that form it.3. Contradictions: Any two notes where my stated positions conflict. Quote the relevant line from each. Do not resolve it. Just surface it.4. Open Questions: Any question that appears repeatedly across my notes without resolution. List it exactly as I phrased it, not [paraphrased.Do](https://paraphrased.do/) not produce summaries. Do not produce general insight. Every item must trace back to a specific note I actually captured.

The output from this prompt is not productivity content. It is actual thinking.

![Imatge](https://pbs.twimg.com/media/HI4YmQZXgAAkTjm?format=jpg&name=large)

The connections section alone has generated more original ideas in eight weeks than any brainstorming session I have run.

## The Weekly Connection Session

Once a week I run a deeper session manually. This one looks across 30 days of captures instead of 7.

**Prompt**

> Read all captures from the last 30 days across every subfolder.Find three connections that would genuinely surprise me. The test: would I have found this connection myself if I had searched for it deliberately? If yes, it is too obvious. Only surface connections that emerge from the full set of notes together.For each connection: - Name it in one sentence - Quote the relevant line from each source note - Write one paragraph on what this connection implies - Suggest one piece of content this connection could become

The weekly session produces the highest-quality content ideas I have. The daily synthesis catches what just happened. The weekly session finds what has been building for a month without me noticing.

## What Changes After Eight Weeks

The compounding is real and it is faster than I expected.

![Imatge](https://pbs.twimg.com/media/HI4Yuj2XQAATVWo?format=png&name=large)

At two weeks, the daily synthesis feels occasionally useful. It catches connections maybe once every three sessions.

At four weeks, it starts catching things that genuinely surprise me. The quality of what it surfaces is higher because it has more material to work across.

At eight weeks, it has effectively been studying my thinking in the background for two months. It knows which arguments I keep returning to. It knows which questions have not resolved. It knows which domains I am pulling from simultaneously.

The most useful thing it does at this stage is not the connections. It is the contradictions section. I have saved notes that directly conflict with each other because I read something on Tuesday that changed my view and forgot the note I wrote the previous Thursday. Claude surfaces these without judgment. I have updated my thinking on three significant positions in the last eight weeks because of this feature alone.

## How to Build This in One Weekend

Day 1: Install Obsidian. Set up the six-folder capture structure. Install the Readwise plugin and connect your Readwise account. Set up the Telegram bot for web and X captures using Zapier or Make if you do not want to touch N8N yet.

Day 2: Write your CLAUDE.md file. This takes longer than you think and matters more than anything else. Do not use placeholders. Fill every section with real specifics about your actual work and thinking.

Connect Claude to your vault using Claude Projects. Upload your CLAUDE.md as the project context. Add your first week of notes as additional context.

Run the daily synthesis prompt manually for the first two weeks before automating it. Reading it without automation forces you to notice what is good and what needs refinement. Calibrate the prompt based on what misses versus what lands.

Week 3: Set up the N8N automation. The daily synthesis trigger is a single workflow: schedule trigger at 6am, read the last 7 days of Obsidian notes via the Obsidian API, pass to Claude with the synthesis prompt, write the output to a daily note.

The entire setup takes a weekend. The compounding starts immediately and does not stop.

At six months you will have a vault that has been studying your thinking longer than most new employees have been at a job. The context it holds at that point is genuinely difficult to replicate from scratch.

That is the actual moat in the AI era. Not the tools. Not the prompts.

The accumulated context of someone who started six months ago.

Follow [@damidefi](https://x.com/@damidefi) on X for daily Claude AI tools, system builds, and the full journey to 100K. Bookmark this. Share it with one person still using Obsidian as a filing cabinet.