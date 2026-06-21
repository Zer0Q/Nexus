---
type: concept
title: "Eval-Harness"
description: "A system for evaluating whether a model is improving across multiple criteria, not just surface metrics. Includes rubric design, review interface, failure taxonomy, and promotion gates."
resource: "https://x.com/VibeMarketer_/status/2067967513246249337"
timestamp: 2026-06-19
tags:
  - evaluation
  - eval-harness
  - model-assessment
  - quality-assurance
---

## Definition

An eval harness is a system for evaluating whether a model is improving across multiple criteria. It includes rubric design, a review interface, failure taxonomy, and a promotion gate. The harness determines whether a new model is better at the specific behavior the system cares about, not just whether it looks better on surface metrics.

## Components

- **Rubric:** Multi-criteria scoring system specific to the domain
- **Review interface:** Side-by-side comparison of source and output
- **Failure taxonomy:** Categorized failure modes (not just "bad output")
- **Promotion gate:** Concrete thresholds a new model must clear
- **Champion:** The current best model being defended

## Key Insight

"The product is the loop around training: dataset quality, rubric design, review workflow, failure analysis, promotion gates, and operator judgment." Training changes the model; the harness changes the workflow around the model.

## Related Concepts

- [[Champion-Gate]]
- [[Rubric-Scoring]]
- [[Failure-Analysis]]
- [[Model-Assessor]]
