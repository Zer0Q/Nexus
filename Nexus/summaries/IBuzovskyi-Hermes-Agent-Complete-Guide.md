---
title: "HERMES AGENT: THE COMPLETE GUIDE. From Zero to Self-Improving AI Employee"
source: "https://x.com/IBuzovskyi/status/2059675518966894767"
author: "@IBuzovskyi"
published: "2026-05-27"
type: article
---

# Hermes Agent Complete Guide

## Summary
Comprehensive guide to running Hermes Agent as a 24/7 autonomous AI employee by @IBuzovskyi. Covers installation, model selection tiers, the dashboard, /goal command system, self-improvement loop, Kanban-based multi-agent workflows, security stack (Bitwarden + iron-proxy), and practical use cases from overnight research to multi-agent org charts.

## Core Concepts
- [[concepts/Hermes-Dashboard]] -- web UI at localhost:9119 with Models, Cron, Skills, Plugins, Profiles, and Kanban tabs
- [[concepts/Goal-Command]] -- /goal turns the agent from reactive chatbot into autonomous background worker
- [[concepts/Self-Improvement-Loop]] -- task execute → review → save skill → reuse; compounds over months
- [[concepts/Session-Recall]] -- FTS5 full-text search across entire conversation history with LLM summarization
- [[concepts/Model-Selection-Tiers]] -- expensive (Claude), moderate (GPT-5.5), affordable (Qwen/Grok/Nous Portal)
- [[concepts/Hermes-vs-Competitors]] -- comparison with OpenClaw, Claude Code, Codex; different jobs, complementary use
- [[concepts/Kanban-Board-Workflow]] -- Triage → To-Do → Ready → In Progress → Blocked → Done; daemon checks every 60s
- [[concepts/Overnight-Goal-Runs]] -- complex tasks (research reports, refactoring) run while you sleep
- [[concepts/Mission-Control-Dashboard]] -- agent-built custom dashboards described in natural language
- [[concepts/Multi-Agent-Org-Chart]] -- profile-based agents with distinct roles (CoS, Head of Research, Head of Content)
- [[concepts/Bitwarden-Secrets-Integration]] -- credential management: one bootstrap token, all secrets in Bitwarden
- [[concepts/Iron-Proxy-Egress-Firewall]] -- credential protection: opaque proxy tokens swap for real keys at network boundary
- [[concepts/Max-Turns-Configuration]] -- configuring goal complexity via goals.max_turns (default 5-10, raise for complex tasks)

## Key Insights
- The real edge is compounding: day 1 knows nothing, month 6 knows how you think and work
- Dashboard's Skills tab is where the real value lives (150+ skills for a well-used agent)
- Kanban board: drop tasks in Triage, walk away, half your to-do list done by breakfast
- Security for personal use: common sense + soul.md ground rules. Production: Bitwarden + iron-proxy
- Hermes handles day-to-day so you can go deep with Claude Code/Codex when needed
- 99% use the dashboard wrong — they don't open the Skills tab first

## Open Questions
- How does the Kanban daemon handle task conflicts between multiple profiles?
- What's the token cost of running 4-5 profile agents simultaneously overnight?
- How does iron-proxy perform with high-frequency tool calls?
