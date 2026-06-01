---
title: "6 Workflows, 6 Lessons, 60 Days with Hermes Analyst"
source: "https://x.com/0xJeff/status/2061361760968560887"
author: "@0xJeff"
published: "2026-05-25"
type: article
---

# 60 Days with Hermes Analyst

## Summary
Jeff shares lessons from 60 days running Hermes as an investment/data analyst agent. Key insight: agents fail on architecture, not intelligence — tools fighting each other, not model limitations. Covers provider selection, tool hierarchy, memory strategies, feedback loops, x402 payments, and skill bundling patterns.

## Core Concepts
- [[concepts/Agent-Architecture-over-Intelligence]] -- Agents fail due to architectural issues (tool conflicts), not model intelligence
- [[concepts/Tool-Selection-Hierarchy]] -- Direct API > MCP > Browser CDP > Headless browser, ranked by reliability and cost
- [[concepts/Skill-Bundling]] -- Structuring skills as directories with references/scripts instead of monolithic prompts
- [[concepts/Echo-Chamber-Bias]] -- Self-reinforcing analysis loops where AI gravitates toward existing holdings

## Key Insights
- Provider switching costs 2-3 debugging sessions per swap; stick with one provider
- Direct API access beats aggregator multi-hop (5-10s latency overhead)
- External memory (Hindsight) enables relationship-building but costs more than native recall
- Skill bundling saves ~5000 tokens per session vs monolithic prompts
- x402 agentic wallets eliminate tool discovery friction — $5-10 USDC unlocks hundreds of premium tools

## Open Questions
- How to solve echo chamber bias in recurring analysis workflows?
- What's the optimal balance between reflect (deep) and recall (fast) for cron jobs?
