---
type: Concept
title: Shared Directory Pattern
description: 'The AI agent and knowledge base share the same directory. Both systems
  look at the same files: when the agent creates a note, Obsidian shows it instantly;
  wh...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Shared Directory Pattern

## Definition
The AI agent and knowledge base share the same directory. Both systems look at the same files: when the agent creates a note, Obsidian shows it instantly; when you write in Obsidian, the agent can read it next session.

## Why It Matters
Eliminates the tab-switching friction between agent and notes. "Death by a thousand cuts" -- every context switch loses momentum. When agent and vault share a directory, they become one system.

## Key Ideas
- One folder for everything: agent terminal + Obsidian vault
- Integrated terminal plugin in Obsidian: agent lives as a tab inside notes
- AGENTS.md/CLAUDE.md gives agent persistent context across sessions
- Agent reads, updates, organizes notes and finds connections autonomously
- Three mistakes that break it: no context file, non-markdown formats, separate directories
- "Your notes are already there. Your agent is already there. The only thing missing was the folder they share."

## Tradeoffs
- Agent has write access to vault -- need safeguards against destructive edits
- Mixed agent output and human notes in same directory
- Requires discipline to keep everything in markdown

## Related
- [[concepts/CLAUDE-MD-as-Context-Layer]]
- [[concepts/Integrated-Terminal-Workflow]]
- [[concepts/Markdown-as-Universal-Format]]

## Source
[[summaries/Atenov-Self-Running-Brain]]
