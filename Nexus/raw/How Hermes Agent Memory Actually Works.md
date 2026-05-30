---
title: "How Hermes Agent Memory Actually Works"
source: "https://x.com/NeoAIForecast/status/2044899251768209502"
author:
  - "[[@NeoAIForecast]]"
published: 2026-04-17
created: 2026-05-31
description: "Most AI products talk about memory like it is one feature, Hermes Agent does something much more useful.Instead of treating memory as one va..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HGBYPTCa8AER-xy?format=jpg&name=large)

Most AI products talk about memory like it is one feature, Hermes Agent does something much more useful.

Instead of treating memory as one vague bucket, Hermes separates always-on memory, user profile, searchable session history, and optional external memory providers into distinct layers.

That design matters.

Because in Hermes, memory is not just about “remembering things.”

It is about deciding what should always stay in context, what should be searched only when needed, and what should live in a deeper long-term memory system.

That is a much more serious way to build an agent.

## What Hermes Means by “Memory”

A lot of AI products blur together several different ideas:

- chat history
- personalization
- saved facts
- retrieval

Hermes Agent does not.

Its memory system is structured around clear boundaries.

At the built-in level, Hermes has two persistent memory stores:

**MEMORY.md** and **USER.md** They are not the same thing.

**MEMORY.md** is the agent’s own operational memory:

Environment facts, project conventions, tool quirks, and lessons learned.

USER.md is the user profile:

Preferences, communication style, expectations, habits, and things the agent should remember about how you like to work.

This distinction is one of the most important parts of the design. Hermes does not just remember things. It remembers different kinds of things in different places.

Takeaway: Hermes memory is not one blob. It is structured memory with separate roles.

## Built-In Memory Is Small on Purpose

One of the most interesting things about Hermes memory is that it is intentionally bounded.

The built-in stores have strict size limits:

MEMORY.md gets 2,200 characters, roughly 800 tokens.

USER.md gets 1,375 characters, roughly 500 tokens.

That is not an accident. It is a design choice.

A lot of people assume more memory is always better. But if you keep injecting too much into the system prompt, you create bloat, noise, and rising token costs.

Hermes takes the opposite view:

The always-on memory layer should stay small, curated, and high-signal. That forces the agent to keep only the facts that matter enough to deserve permanent prompt space.

So built-in memory is not trying to be a giant archive.

It is the compact layer of information that should reliably shape future sessions.

Takeaway: Hermes treats built-in memory as scarce prompt real estate, not as unlimited storage.

## Where Hermes Stores Memory

Hermes stores its built-in memories in **~/.hermes/memories/**

![Imatge](https://pbs.twimg.com/media/HGDwmzIb0AA4QR0?format=png&name=large)

That means:

- these memories are durable across sessions
- They are not temporary context from a single conversation
- They persist and get carried forward.

But the really important detail is not just where they live. It is how they are loaded.

At the start of a session, Hermes reads those memory files and injects them into the system prompt as a frozen snapshot.

That frozen-snapshot behavior is one of the most important technical details in the whole system.

Takeaway: Hermes memory lives on disk, but it becomes active by being injected into the system prompt at session start.

## The Frozen Snapshot Design

This is where Hermes Agent memory becomes much more interesting than the average “AI memory” feature. Hermes does not continuously rewrite the live system prompt every time memory changes.

Instead, it captures memory once at session start and keeps that prompt snapshot fixed for the duration of the session.

If the agent adds or updates memory during the conversation, those changes are persisted immediately to disk. But they do not get re-injected into the prompt until the next session.

Why does Hermes do this?

Because changing the prompt mid-session would break prefix caching and hurt performance.

This is a very deliberate architectural tradeoff:

Hermes chooses prompt stability and efficiency over the illusion of constantly mutating in-session memory injection. That makes the system more predictable.

The agent still writes live memory updates.

The tool output can show current state.

But the session-level prompt remains stable until the next session starts.

This is the kind of design detail that tells you Hermes memory is not marketing language. It is an actual system with explicit constraints and performance-aware behavior.

Takeaway: Hermes saves memory immediately, but only reloads it into the prompt on the next session. That keeps prompt caching stable.

## How the Memory Tool Works

Hermes manages built-in memory through a memory tool.

The tool supports three actions:

- add
- replace
- remove

That minimalism is important.

There is no read action.

Why not you say?

Because the built-in memory is already injected into the system prompt at session start. The agent does not need to “query” it like a separate database in normal use.

It already has that memory in context.

Replace and remove operations use substring matching through old\_text.

So the agent does not need the exact full entry every time.

It just needs a unique enough substring to identify the right memory entry. That makes updating memory practical without turning memory management into a brittle exact-match system.

The built-in memory system also rejects exact duplicates.

And memory entries are scanned for dangerous patterns like prompt injection, exfiltration attempts, or suspicious hidden Unicode.

That means the memory layer is not just persistent.

It is also curated and guarded.

Takeaway: Hermes memory management is deliberately simple: small, editable, duplicate-resistant, and security-scanned.

## What Belongs in MEMORY.md vs USER.md

This split is worth understanding because it explains what Hermes thinks memory is for.

MEMORY.md is for the agent’s operational notes:

facts about the machine, tools installed, project structure, repo conventions, workflows, and lessons learned.

Examples:

- This machine runs Ubuntu 22.04
- Project uses Go 1.22 with sqlc and chi
- Docker commands do not need sudo on this host
- The staging server uses SSH port 2222

USER.md is for the human side:

response style, preferred formats, recurring requests, priorities, and preferences.

Examples:

- Prefers concise explanations
- Wants reusable Markdown sections
- Prefer open-weight models where possible
- When debugging, prioritise root cause over quick fixes

This separation matters because not all memory should be treated equally.

A user preference is not the same as a machine fact. A workflow habit is not the same as a repo convention. Hermes keeps those categories distinct.

Takeaway: Hermes separates “who the user is” from “what the environment and workflow are.”

## Memory Is Not Session Search

This is the conceptual distinction that probably matters most.

Hermes has built-in memory. But it also has session search.

Those are not the same feature. Built-in memory is small, curated, and always present in the prompt.

It is the layer for facts that should shape every future interaction. Session search is the recall layer. It lets the agent search past conversations when it needs to recover something specific from prior work.

This is session search as drawing from stored sessions in SQLite with FTS5 full-text search. That gives Hermes effectively much broader historical recall than what could ever fit into a prompt.

So Hermes does not try to shove all history into memory.

Instead, it splits the problem in two:

- memory for permanent high-value context
- search for long-tail historical recall

That is a much cleaner design.

If something should always be available, it belongs in memory.

If something only matters occasionally, it belongs in searchable history.

Takeaway: Session search is recall. Built-in memory is context.

## Why That Layering Matters

This layered design solves a very real agent problem.

If you put too much into always-on memory, the prompt becomes bloated. If you put too little into memory, the user keeps repeating themselves.

If you rely only on session history, long-term recall becomes too expensive and noisy.

Hermes avoids that by splitting responsibilities:

- small built-in memory for high-signal facts
- session search for recoverable history
- external providers for deeper long-term memory systems

That means Hermes can remember important things without pretending the prompt should contain everything.

This is one of the strongest parts of the overall architecture.

Takeaway: Hermes scales memory by layers, not by dumping the whole past into the context window.

## External Memory Providers Extend Hermes

Hermes does not stop at built-in memory.

It also ships with external memory provider plugins.

There are 8 supported external providers:

- Honcho
- OpenViking
- Mem0
- Hindsight
- Holographic
- RetainDB
- ByteRover
- Supermemory

An important design detail here:

Only one external provider can be active at a time, but the built-in memory remains active alongside it.

That means external providers do not replace Hermes memory.

They extend it.

This is a really strong architectural choice because it preserves the built-in, bounded, always-on memory layer while giving advanced users a deeper long-term memory backend.

![Imatge](https://pbs.twimg.com/media/HGDwTMJbUAAihS7?format=png&name=large)

When a provider is active, Hermes can:

- inject provider context into the system prompt
- prefetch relevant memories before each turn
- sync conversation turns after each response
- extract memories on session end for providers that support it
- mirror built-in memory writes to the external provider
- add provider-specific memory tools

That is much richer than a simple “save a preference” system.

It turns memory into a pluggable subsystem.

Takeaway: Hermes built-in memory is the core layer. External providers are additive depth.

## Different Providers, Different Memory Philosophies

One of the most interesting things in the Hermes docs is that memory providers are not all variations of the same thing.

They reflect different ideas about what memory should be.

- Honcho focuses on cross-session user modeling and alignment.
- OpenViking emphasizes a filesystem-style knowledge hierarchy with tiered retrieval.
- Mem0 leans into server-side fact extraction and semantic search.
- Hindsight brings knowledge graphs and cross-memory synthesis.
- Holographic offers a local SQLite fact store with trust scoring and algebraic retrieval.
- RetainDB focuses on hybrid search and typed memories.
- ByteRover is local-first and portable, with pre-compression extraction.
- Supermemory adds semantic recall, profile recall, and session-end graph ingest.

That variety matters because not every user wants the same memory system.

- Some want local-only memory.
- Some want cloud-backed semantic recall.
- Some want knowledge graphs.
- Some want structured browsing.
- Some want provider tools that can search, store, and synthesize long-term knowledge.

Hermes does not force one answer.

Takeaway: Hermes memory is extensible because different users need different kinds of recall.

## Conclusion

Most AI products describe memory as if it were one magic capability.

Hermes Agent treats memory as a layered system.

Built-in memory handles the small set of facts that should always be present. Session search handles historical recall when something older needs to be recovered.

External memory providers add deeper retrieval and long-term knowledge systems for users who need more.

That is what makes Hermes memory interesting.

It is not just persistent. It is structured, bounded, layered, and extensible.

And that is a much better foundation for an agent that is supposed to improve over time.