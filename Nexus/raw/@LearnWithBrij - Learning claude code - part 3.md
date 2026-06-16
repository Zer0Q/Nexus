---
title: "Post by @LearnWithBrij on X"
source: "https://x.com/LearnWithBrij/status/2050803172793372769"
author:
  - "[[@LearnWithBrij]]"
published: 2026-05-03
created: 2026-06-16
description: "Claude Code ships with 5 architectural layers most engineers never open. Not features. Not settings. Layers — each solving a distinct proble"
tags:
  - "clippings"
summary:
---
Claude Code ships with 5 architectural layers most engineers never open.

Not features. Not settings. Layers — each solving a distinct problem that LLMs alone can't solve. And four of them have nothing to do with prompting.

Here's the full Agent Development Kit:

Layer 1 — CLAUDE.md → The Memory Layer

Architecture rules, naming conventions, test expectations, repo map. Always loaded. Always active.

Two scopes:

• ~/.claude/CLAUDE.md → global

• .claude/CLAUDE.md → project

This isn't context you paste in before every session. It's context that never needs repeating. The agent's constitution.

Layer 2 — Skills → The Knowledge Layer

Each SKILL.md carries a description. Claude matches it at runtime and forks the skill into an isolated subagent. On-demand, never always-on.

Task-specific knowledge without inflating your main context window. Modular by design.

Layer 3 — Hooks → The Guardrail Layer

PreToolUse → PostToolUse → SessionStart → Stop → SubagentStop

This is the layer most teams skip. And the one they regret skipping first.

Hooks are NOT AI. They're deterministic event-driven shell commands.

• Auto-lint on every Write

• Hard-block on rm -rf

• Slack notification on Stop

Event fires → Matcher checks → Command runs

Quality enforced at the infrastructure level. Not the prompt level.

Layer 4 — Subagents → The Delegation Layer

Each subagent gets its own context window, model, tools, and permissions.

Main agent delegates down. Receives results up. That's it.

No infinite recursion — subagents can't spawn subagents. Main context stays clean. Hard boundaries by design.

Layer 5 — Plugins → The Distribution Layer

Bundle your skills + agents + hooks + commands into a plugin. One install. Whole team inherits the behavior.

Think npm packages — but for what your agent knows how to do.

Wrapping everything:

→ MCP Servers on the left (GitHub, databases, APIs, custom integrations)

→ Agent Teams on the right (parallel execution, message passing, shared permissions)

The 5-layer stack in one line:

CLAUDE.md sets rules → Skills provide expertise → Hooks enforce quality → Subagents delegate work → Plugins distribute to the team

Most production failures in agentic systems trace back to one missing layer.

Which one is the gap in your current setup?

![Imatge](https://pbs.twimg.com/media/HHXqmmmaIAAyN5Y?format=jpg&name=large)