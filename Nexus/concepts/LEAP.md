---
type: Concept
title: LEAP
description: Agentic scaffold that wraps a general-purpose LLM in Lean compiler verification,
  decomposing formal proofs into subgoals with informal blueprints, then forci...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# LEAP

## Definition
Agentic scaffold that wraps a general-purpose LLM in Lean compiler verification, decomposing formal proofs into subgoals with informal blueprints, then forcing every formal step through compiler checks before advancing.

## Why It Matters
Proves that a well-built harness, not a bespoke model, can close the gap on one of the hardest reasoning domains. Solves all 12 Putnam 2025 problems and lifts Lean-IMO-Bench from below 10% to 70% one-shot formal solve rate without any math-specific training of the base LLM.

## Key Ideas
- Decompose, then verify: breaks hard theorems into subgoals, drafts informal blueprint, Lean compiler checks each formal step
- Turns vague reasoning into machine-checkable proof through iterative verifier feedback
- No fine-tuning of the base LLM for math — relies on informal reasoning, instruction following, and self-refinement
- Surpasses the 48% set by a specialized gold-medal-caliber IMO system

## Tradeoffs
- Requires a formal verification environment (Lean); not applicable to domains without compilers/checkers
- Scaffold complexity may not generalize to non-mathematical reasoning tasks
- Performance depends on the base model's informal reasoning capabilities

## Related
- [[concepts/Harness-Engineering]]
- [[concepts/RLVR]]
- [[concepts/State-Externalizing-Harnesses]]

## Source
[[summaries/DAIR-Top-AI-Papers-of-the-Week-June-7]]
