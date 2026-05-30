---
title: "Working With Sessions in Hermes Agent"
source: "https://x.com/NeoAIForecast/status/2044515050057281808"
author:
  - "[[@NeoAIForecast]]"
published: 2026-04-15
created: 2026-05-31
description: "A lot of AI tools give you a conversation. Hermes gives you a session you can actually manage.That sounds small at first, but it changes a l..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HF67ZRNasAI2sCJ?format=jpg&name=large)

A lot of AI tools give you a conversation. Hermes gives you a session you can actually manage.

That sounds small at first, but it changes a lot. Because once sessions are persistent, searchable, renameable, resumable, exportable, and organizable, Hermes starts behaving less like a disposable chat window and more like a real working environment.

If you are new to Hermes, understanding sessions is one of the fastest ways to get more value out of it.

## What a session is in Hermes

In Hermes, every conversation is automatically saved as a session.

That includes conversations from:

- CLI
- Telegram
- Discord
- Slack
- WhatsApp
- Signal
- Matrix
- cron jobs
- API/server surfaces
- other supported platforms

A session is not just a transcript. It is the unit Hermes uses for continuity.

It tracks things like:

- the message history
- the title
- the source platform
- model and config details
- timestamps
- parent session relationships when a session continues through compression

That means when you come back later, Hermes is not guessing what happened before. It can resume from a real stored conversation history.

Takeaway: A session is Hermes’ persistent container for a conversation, not a temporary chat tab.

## Why sessions matter

Most new users treat AI chats as disposable.

That works for one-off questions, but it falls apart when you are doing real work:

- debugging over multiple passes
- writing something over several sittings
- revisiting research
- managing a project thread
- continuing work from one device or platform to another

Sessions solve that.

Instead of starting over every time, you can keep a thread alive, return to it later, organize it with a name, branch it into a new direction, and search older work when you need it.

This is one of the practical differences between “chatting with a model” and “working with an agent runtime.”

Takeaway: Sessions are what let Hermes support continuity instead of forcing restart-by-default behavior.

## How Hermes stores sessions

Hermes tracks sessions in two complementary systems.

First:

SQLite database at **~/.hermes/state.db**

This stores the structured session data, including metadata and full-text search support.

Second:

JSONL transcripts under **~/.hermes/sessions/**

These preserve raw conversation transcripts, including tool calls in the gateway flow. In practice, what matters for users is simple:

Hermes keeps both the structure and the history.

So you are not only getting a visible transcript. You are getting something Hermes can list, resume, search, filter, and manage.

Takeaway: Hermes sessions are real stored objects with metadata and history, not just a UI convenience.

## How to resume sessions

This is one of the first session workflows new users should learn.

To continue your most recent CLI session:

**hermes --continue** or **hermes -c**

To resume a specific session by ID:

**hermes --resume 20250305\_091523\_a1b2c3d4**

To resume by title:

**hermes -c "my project"**

This is especially useful once you start naming sessions properly.

Hermes also supports lineage behavior. If your session became:

- my project
- my project #2
- my project #3

then:

**hermes -c "my project"**

will resume the most recent one in that line.

That is a very practical feature, because it means you can think in terms of project names instead of memorizing IDs.

Takeaway: For day-to-day work, resume by title is usually the cleanest session habit.

## What happens when you resume

When you resume a session, Hermes reloads the prior conversation history and can show a compact recap before you continue.

That recap is meant to quickly reorient you:

- recent user messages
- recent assistant responses
- collapsed tool call summaries
- truncated long content
- hidden internal/system noise

This matters because the resume experience is not just “open old log file.” It is designed to put you back into the working thread quickly.

If you want a lighter resume display, Hermes also supports a minimal mode through config.

Takeaway: Resume is built for re-entry, not just archival access.

## Why naming sessions matters

If you do only one thing to improve your Hermes workflow, name your important sessions. Hermes can auto-generate titles after the first exchange, and that helps. But the real upgrade is setting intentional titles yourself.

Inside a session, use:

**/title my research project**

![Imatge](https://pbs.twimg.com/media/HF6_guYasAEiuSO?format=png&name=large)

From the CLI, you can rename an existing session:

**hermes sessions rename 20250305\_091523\_a1b2c3d4 "debugging auth flow"**

![Imatge](https://pbs.twimg.com/media/HF6_HplasAAcWAS?format=png&name=large)

A good session title makes the session easier to:

- resume later
- distinguish from similar conversations
- organize by project
- search mentally before you even search technically

Bad session habit:

having 40 unnamed threads that all begin with “help me…”

Better session habit:

naming them by project, decision, or workstream.

Examples:

- auth migration plan
- review tasks for PR
- daily recap workflow
- hermes sessions article draft

Takeaway: Titles turn sessions from saved chats into manageable working threads.

## How to list and browse sessions

Once you have more than a handful of sessions, listing and browsing becomes important.

Use:

**hermes sessions list**

You can also filter by source:

**hermes sessions list --source telegram**

Or show more:

**hermes sessions list --limit 50**

Hermes also has:

**hermes sessions browse**

![Imatge](https://pbs.twimg.com/media/HF7AiQabIAA1KcN?format=png&name=large)

That is useful when you want a more deliberate session-picking workflow instead of remembering IDs manually.

For new users, this is the practical pattern:

- use sessions list when you roughly know what you want
- use sessions browse when you want to inspect and choose

Takeaway: Listing is for quick access. Browsing is for session management at scale.

## How to organize sessions well

The simplest system is best.

A good Hermes session organization strategy usually looks like this:

**1\. One session per real thread of work**

Do not pile unrelated topics into one giant conversation if you know they are separate projects.

**2\. Name durable threads early**

If the conversation will matter tomorrow, title it today.

**3\. Resume instead of restarting**

If you are continuing the same project, continue the same session.

**4\. Branch when you want to explore a different direction**

Do not wreck a clean thread just to test an alternative path.

**5\. Prune and export occasionally**

Keep your session store useful, not messy. This is less about neatness and more about keeping the agent context aligned with the work.

Takeaway: Good session hygiene improves both your own recall and Hermes’ continuity.

## How branching works

Branching is one of the most underappreciated session tools.

Hermes includes:

**/branch**

also available as:

**/fork**

Its purpose is simple:

take the current session and fork it into a new independent copy so you can explore a different path without losing the original thread.

That is extremely useful when:

- you want to try a different plan
- you are comparing two implementations
- you want a safer drafting branch
- you are about to take the conversation in a very different direction

Instead of mutating your main thread into a confusing hybrid, you create a branch and keep both paths clean.

Takeaway: Use branch when the work is diverging, not just continuing.

## How compression affects sessions

Hermes can compress context manually or automatically.

When that happens, Hermes may create a continuation session in the same lineage. If the original session had a title, the follow-on sessions get numbered automatically:

- my project
- my project #2
- my project #3

This is important for two reasons.

First, it preserves continuity without pretending the context window is infinite.

Second, it keeps the lineage understandable.

So if a long-running thread needs to keep going across compressed boundaries, Hermes gives you a structured continuation instead of a vague reset.

Takeaway: Compression does not mean losing the thread. It means continuing it in an organized lineage.

## Best Practice for renaming sessions

A few useful title rules:

- titles must be unique
- they are capped at 100 characters
- Hermes sanitizes control characters and similar junk automatically

The practical advice is:

rename sessions based on the work they represent, not the first sentence you typed.

Takeaway: Rename sessions around outcomes, projects, or threads of work, not random opening prompts.

## How to export sessions

Sometimes you want portability, backup, or analysis. Hermes supports exporting all sessions, a filtered set, or one specific session.

Examples:

**hermes sessions export backup.jsonl**

![Imatge](https://pbs.twimg.com/media/HF7CjugasAAsSVi?format=png&name=large)

**hermes sessions export telegram-history.jsonl --source telegram**

**hermes sessions export session.jsonl --session-id 20250305\_091523\_a1b2c3d4**

That gives you a structured record with metadata and messages.

This is useful when you want to:

- back up history
- move data
- inspect old work outside Hermes
- build your own archive
- preserve a project thread before cleanup

Takeaway: Export is your backup and portability layer for session history.

## How to delete and prune sessions

Not every session deserves to live forever.

For one specific session:

**hermes sessions delete 20250305\_091523\_a1b2c3d4**

For general cleanup:

**hermes sessions prune**

**hermes sessions prune --older-than 30**

![Imatge](https://pbs.twimg.com/media/HF7DGo6asAIafD8?format=png&name=large)

I had no older sessions than 30 days

**hermes sessions prune --source telegram --older-than 60**

Important detail:

pruning only deletes ended sessions. Active sessions are not pruned. That makes pruning safer than people often assume.

The right mental model is not “delete everything old.”

It is:

remove stale finished threads so the session store stays manageable.

Takeaway: Pruning is maintenance, not destruction. Use it to keep your session history useful.

## How to inspect session health at a high level

Hermes also gives you:

**hermes sessions stats**

![Imatge](https://pbs.twimg.com/media/HF-SmJYawAAc6SG?format=png&name=large)

That helps you understand things like:

- total sessions
- total messages
- source breakdown
- database size

This is especially useful once Hermes becomes part of your daily workflow and you want to understand how much history is accumulating.

If you want deeper usage patterns, Hermes has separate insights tooling, but sessions stats is the first health check.

Takeaway: Stats helps you understand the shape of your session history before it becomes invisible clutter.

## Sessions vs session\_search

New users often confuse these.

A session is the stored conversation itself.

session\_search is the retrieval layer that helps Hermes look back across past conversations.

So:

- sessions are the underlying stored threads
- session\_search is how Hermes finds relevant prior threads when needed

That distinction matters because good session organization improves both your manual workflow and Hermes’ ability to retrieve useful past context later.

Takeaway: Sessions are the archive. session\_search is the recall mechanism.

## What new Hermes users should do first

If you are just starting with Hermes, these are the session habits worth building immediately:

1\. Resume ongoing work instead of starting fresh every time

Use:

**hermes -c**

or

**hermes -c "project name"**

2\. Name important sessions early

Use:

**/title my project**

3\. Use one session per meaningful workstream

Do not mix unrelated tasks into one endless thread.

4\. Branch when exploring alternatives

Use:

**/branch**

5\. List and prune occasionally

Use:

**hermes sessions list**

**hermes sessions prune**

These five habits alone make Hermes feel much more coherent over time.

Takeaway: Session discipline is one of the easiest ways to make Hermes more useful without changing any model settings.

## Final takeaway

If skills explain how Hermes stores reusable procedures, sessions explain how Hermes stores continuity.

They are the working memory structure that lets Hermes act like an environment you return to, not a blank page you reopen.

For a new user, learning how to create, name, resume, branch, export, prune, and organize sessions is not optional side knowledge.

It is one of the core operational habits that makes Hermes feel powerful.