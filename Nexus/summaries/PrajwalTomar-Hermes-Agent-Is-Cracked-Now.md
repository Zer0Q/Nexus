---
title: Hermes Agent Is CRACKED Now And Most Builders Have No Idea What It Actually
  Is.
author: '@PrajwalTomar_'
published: '2026-06-09'
type: article
resource: https://x.com/PrajwalTomar_/status/2064324584254710262
timestamp: '2026-06-09T00:00:00Z'
description: Prajwal Tomar provides a practical setup guide for Hermes Agent, contrasting
  it with session-based agents (Claude Code, Cursor, Codex) that lose context betw...
tags:
- summaries
---


# Hermes Agent Is CRACKED Now And Most Builders Have No Idea What It Actually Is

## Summary
Prajwal Tomar provides a practical setup guide for Hermes Agent, contrasting it with session-based agents (Claude Code, Cursor, Codex) that lose context between sessions. The guide walks through six steps: installation with SOUL.md identity, model tier selection (GPT-5.5 daily, Claude Opus for /goal, Qwen 3.7 Max for long runs), Telegram integration, multi-profile org charts, autonomous overnight runs via /goal, and the dashboard/Kanban board. The core thesis: Hermes compounds over weeks while session agents reset daily.

## Core Concepts
- [[concepts/Hermes-Agent-Architecture]] -- persistent agent platform with FTS5 memory, autonomous skill creation, multi-profile support, and 20+ messaging integrations
- [[concepts/SOUL-MD]] -- the identity file at slot #1 of the system prompt that defines agent personality, style, boundaries, and technical posture
- [[concepts/Goal-Command]] -- autonomous execution via /goal that breaks objectives into tasks and runs until completion, configurable max_turns (20-50 for serious work)
- [[concepts/Self-Evolving-Skills]] -- agent writes procedural memory after complex tasks (5+ tool calls), creating markdown skill files with triggers, steps, pitfalls, and verification
- [[concepts/Multi-Profile-Architecture]] -- isolated agents with separate SOUL.md, memory, skills, and models; converging pattern is org-chart profiles (Chief of Staff, Head of Research, etc.)

## Key Insights
- Hermes has ~185K GitHub stars, launched February 2026, MIT licensed by Nous Research
- The five differentiators: persistent memory (FTS5 + LLM summarization), autonomous skill creation, multi-profile architecture, multi-platform reach (20+ messaging), server-resident execution ($5 VPS)
- Model tiers: GPT-5.5 via ChatGPT subscription for daily work, Claude Opus/Sonnet for /goal runs, Qwen 3.7 Max for long-horizon autonomy (35 hours continuous, 1000+ tool calls)
- Telegram setup is three steps: BotFather → token → first message that goes into memory and filters proactive tasks
- Profiles mirror a funded team: Chief of Staff runs daily brief, Head of Research does competitor analysis, Head of Content drafts posts, Head of Finance reconciles subscriptions
- /goal default max_turns is 5-10 (too low); raise to 20 for research/content, 50 for code refactoring
- Dashboard at localhost:9119; Kanban daemon checks for new tasks every 60 seconds
- Skills compound over months: first week feels like setup tax, 30 days = noticeably better, 6 months = meaningfully better
- Safety: browser automation and computer use off by default; enable per-profile only when needed

## Open Questions
- How does [[concepts/Multi-Profile-Architecture]] handle cross-profile communication when Chief of Staff needs to delegate to Head of Research?
- What happens to [[concepts/Self-Evolving-Skills]] quality when the agent writes skills for tasks it only partially succeeded at?
- Can [[concepts/Goal-Command]] runs be budgeted per-profile to prevent one agent from burning the entire token budget?

## Source
- **Raw note:** [[raw-notes/hermes-agent-is-cracked-now-and-most-builders-have-no-idea-what-]]
- **Original URL:** https://x.com/PrajwalTomar_/status/2064324584254710262
