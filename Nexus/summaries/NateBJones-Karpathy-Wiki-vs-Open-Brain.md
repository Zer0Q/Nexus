---
title: "Karpathy's Wiki vs. Open Brain. One Fails When You Need It Most."
source: "https://www.youtube.com/watch?v=dxq7WtWxi44"
author: "Nate B. Jones"
published: "2026"
type: video
---

# Karpathy Wiki vs Open Brain

## Summary
Nate B. Jones compares two AI knowledge system architectures: Karpathy's write-time wiki (pre-compiled synthesis) vs Open Brain's query-time database (on-demand synthesis). The hybrid approach uses a graph layer to combine both without editorial drift.

## Core Concepts
- [[concepts/Write-Time-Knowledge-Systems]] -- AI synthesizes at ingestion
- [[concepts/Query-Time-Knowledge-Systems]] -- AI synthesizes on demand
- [[concepts/Editorial-Drift]] -- AI summaries lose nuance over time
- [[concepts/Error-Compounding]] -- baked-in errors propagate through wiki updates
- [[tools/AI-as-Maintainer]] -- AI as ongoing knowledge steward, not one-off oracle
- [[architectures/Graph-Knowledge-Layer]] -- structured data with wiki-like synthesis on top
- [[tools/Compilation-Agent]] -- agent that generates wiki views from structured data
- [[concepts/Knowledge-Source-of-Truth]] -- single reliable data layer

## Key Insights
- Write-time saves compute at query but risks permanent error accumulation
- Query-time is expensive per-request but always fresh
- Hybrid approach: store raw, compile wiki views on demand
- The AI role shifts from Oracle to Maintainer of compounding artifacts

## Open Questions
- How to detect editorial drift before it compounds?
- What's the optimal sync interval for compilation agents?
