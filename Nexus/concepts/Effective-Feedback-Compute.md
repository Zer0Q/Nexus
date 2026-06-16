---
type: Concept
title: Effective Feedback Compute
description: Trace-level scaling coordinate (EFC) that credits feedback only when
  it is informative, valid, non-redundant, and retained for later decisions, then
  normaliz...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Effective Feedback Compute

## Definition
Trace-level scaling coordinate (EFC) that credits feedback only when it is informative, valid, non-redundant, and retained for later decisions, then normalizes by task demand. Replaces raw tokens and tool calls as the predictor of agent success.

## Why It Matters
Raw tokens and tool calls explain limited variation in outcomes (R-squared 0.33-0.42), while EFC normalized by task demand reaches R-squared of 0.99. Improving feedback quality raises success from 0.27 to 0.90 at fixed budget. Reframes harness engineering as a feedback-quality problem.

## Key Ideas
- Feedback must be informative, valid, non-redundant, and retained to count toward EFC
- Quality beats quantity at fixed budget: better feedback outperforms more feedback dramatically
- Oracle-EFC (with perfect feedback quality measurement) nearly explains all scaling behavior
- Gives a concrete coordinate to optimize against, rather than blindly increasing compute budgets

## Tradeoffs
- Oracle-EFC requires knowing true feedback quality; practical EFC estimation is an open problem
- May not apply equally to all task types (tested on controlled scaling experiments)
- Requires trace-level instrumentation of agent runs

## Related
- [[concepts/Harness-Engineering]]
- [[concepts/Scaling-Laws]]
- [[concepts/LEAP]]

## Source
[[summaries/DAIR-Top-AI-Papers-of-the-Week-June-7]]
