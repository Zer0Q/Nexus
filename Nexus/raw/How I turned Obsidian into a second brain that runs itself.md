---
title: "How I turned Obsidian into a second brain that runs itself"
source: "https://x.com/Atenov_D/status/2032528386745315553"
author:
  - "[[@Atenov_D]]"
published: 2026-03-13
created: 2026-05-26
description: "I work faster than most people on my team. Not because I'm smarter. Because my AI agent and my notes live in the same folder.Thats it. Thats..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HDO11RNXEAAiFoX?format=jpg&name=large)

I work faster than most people on my team. Not because I'm smarter. Because my AI agent and my notes live in the same folder.

**Thats it. Thats the entire secret.**

Most people use AI agents in one window and their notes in another. Copy-paste. Switch tabs. Lose context. Start over. They're working twice as hard to get half the result.

Here's what nobody tells you: if your agent and your knowledge base share the same directory - they become one system. The agent reads your notes. Updates them. Organizes them. Finds connections you didn't notice. Without you lifting a finger.

**Let me show you exactly how to build this.**

## The foundation: one folder to rule them all

Create a folder. Call it Workspace, Brain, whatever. Open your AI agent terminal inside it. Then open Obsidian - don't create a new vault, just point it at that same folder.

That's it. Both systems now look at the same files. When the agent creates a note - Obsidian shows it instantly. When you write something in Obsidian - the agent can read it next time you ask.

![Imatge](https://pbs.twimg.com/media/HDOyeK6asAAMuzK?format=jpg&name=large)

## The terminal inside your notes

Switching between Obsidian and a terminal window sounds like nothing. It's actually death by a thousand cuts.

Install the Terminal plugin in Obsidian Community Plugins. Open it in integrated mode. Now your agent lives as a tab inside your notes - same window, same context, zero friction.

This sounds minor. It isn't. When the interface stops fighting you, you actually use the system.

## AGENTS.md - the file that makes your agent smart

Without instructions, your agent is an LLM with amnesia. Every session it wakes up blank. Doesn't know your projects. Doesn't know your format. Doesn't know what "organize this" means to you specifically.

Create AGENTS.md in the root of your folder. Write in it: who this agent is, what its supposed to do, how to handle files, what format to use. The agent reads this before every response. It becomes context that never disappears.

**One rule that changes everything**: store everything as Markdown. .md is Obsidian's native format and the cleanest format for any LLM to read. No conversion errors. Just clean text the agent can actually use.

## Your notes become a searchable database

Dump your working materials into the folder. News exports. Research. Meeting notes. Old decisions. Doesnt matter how messy.

> Now ask the agent: "Whats the most recent update on X?"

It scans directories, opens files, reads content - and answers from your data. Your actual notes, your actual decisions, your actual context.

This is the difference between an AI assistant and an AI that actually knows you.

![Imatge](https://pbs.twimg.com/media/HDOyvIfWUAASwS6?format=jpg&name=large)

## The graph that thinks

Obsidian's killer feature is linked notes - connections between ideas, like synapses. Most people build the graph and then just look at it.

Enable Command line in Obsidian settings. Now the agent gets hands - direct access to Obsidian's functions from the terminal.

Ask it to read a note and find everything connected to it. It follows backlinks, reads related files, synthesizes across your entire knowledge base and returns insights you would have missed manually.

You're not searching your notes anymore. You're asking them questions.

## The Kanban board that fills itself

Install the Kanban plugin. Now paste any messy block of text - a dump of Telegram messages, a voice memo transcript, a list of half-formed tasks - and tell the agent to distribute it across your board.

The secret to making this work perfectly: give the agent a strict card template. A reference example of exactly what a card should look like. Without it, it improvises. With it, every card is identical, consistent, usable.

## The shift that changes how you work

When this is all set up, something strange happens.

You stop opening apps. You stop creating files manually. You stop navigating folders.

You just talk to the terminal.

"Brainstorm angles for this topic and save them as a new note" "Find everything I wrote about X last month and summarize it" "Take this message thread and turn it into a project board"

The agent generates, creates the .md file in the right place, and opens it in Obsidian automatically. **You asked - it appeared.**

This is what people mean when they say AI changes how you work. That it removes entire categories of work from your day.

![Imatge](https://pbs.twimg.com/media/HDOyXViWIAM1or7?format=jpg&name=large)

## Three mistakes that break this setup

No AGENTS.md. The agent has no context. Every session you're starting from scratch and paying tokens to re-explain yourself.

Everything in non-Markdown formats. PDFs, .docx, random text - the agent can technically handle them but Markdown is cleaner, faster. One format for everything.

Agent and notes in different folders. Sounds obvious now. But this is how 90% of people run it. Two separate systems pretending to cooperate. Fix this first.

**Your notes are already there.** **Your agent is already there.**

The only thing missing was the folder they share.

**Bookmark this. The setup takes 20 minutes. The leverage lasts for years.**