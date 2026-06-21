---
type: concept
title: "Champion-Gate"
description: "A promotion gate that requires a new model version to clear concrete thresholds on multiple criteria before replacing the current champion, protecting against surface-level improvements that degrade actual utility."
resource: "https://x.com/VibeMarketer_/status/2067967513246249337"
timestamp: 2026-06-19
tags:
  - evaluation
  - model-promotion
  - quality-gates
  - eval-harness
---

## Definition

A champion gate is a set of concrete thresholds a new model must clear before it can replace the current champion. It prevents promoting a model that looks better on surface metrics but is worse on the behaviors that actually matter.

## Typical Thresholds

- 100% parse rate
- No hard fails on any criteria
- Pass rate above incumbent
- Overall usefulness above incumbent
- Domain-specific metrics above incumbent
- Generic recommendation rate below cap

## Why It Matters

A newer model can clear more surface checks while being worse at the actual job. The champion gate asks: "Is this model better at the behavior we actually care about?" If not, it does not ship.

## Related Concepts

- [[Eval-Harness]]
- [[Rubric-Scoring]]
- [[Model-Promotion]]
- [[Failure-Analysis]]
