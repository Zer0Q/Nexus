---
type: Concept
title: Maker Checker Split
description: Separating the agent that creates work from the agent that verifies it,
  using different instructions or different models to catch self-justification bias.
  Th...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Maker Checker Split

## Definition
Separating the agent that creates work from the agent that verifies it, using different instructions or different models to catch self-justification bias. The model that wrote the code is too nice grading its own homework.

## Why It Matters
Without maker-checker separation, agents talk themselves into accepting mediocre or incorrect work. A fresh model decides if the loop is done — not the one that did the work. This is what /goal does under the hood in Claude Code.

## Key Ideas
- Three-agent split: one explores, one implements, one verifies against the spec
- Verification agent uses different instructions — sometimes a different model — from the creator
- The split prevents self-justification: the creator agent rationalizes its own mistakes
- Applied across domains: coding (test verification), research (claim verification against sources), content (critique agent reviews draft)
- This is what makes VERIFY honest in the 5-stage loop: DISCOVER → PLAN → EXECUTE → VERIFY → ITERATE

## Tradeoffs
- Doubles token cost for the verification step (two model calls instead of one)
- Overly strict checkers can cause infinite loops where nothing passes verification
- Requires well-defined success criteria — subjective domains make maker-checker harder to apply

## Related
- [[concepts/Loop-Engineering]]
- [[concepts/Open-vs-Closed-Loop]]
- [[concepts/Evaluator-Optimizer-Workflow]]
- [[concepts/Single-vs-Fleet-Loop]]

## Source
[[summaries/Sairahul1-Loops-What-Every-AI-Engineer-Needs-to-Know]]
