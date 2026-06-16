---
type: Concept
title: Adversarial Model Spiral
description: 'The ARROWHEAD method: pitting two or more AI models against each other
  in successive iterations, where each model reviews the other''s output, critiques
  it, a...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Adversarial Model Spiral

## Definition
The ARROWHEAD method: pitting two or more AI models against each other in successive iterations, where each model reviews the other's output, critiques it, and generates an improved version. The spiral continues until both models agree the work cannot be improved further.

## Why It Matters
A single model's output is bounded by its own reasoning. Adversarial review forces each model to defend its conclusions, find weaknesses, and incorporate counterarguments. The result is a sharpened, more rigorous output than any single model produces alone.

## Key Ideas
- Named ARROWHEAD by @javilopen (adversarial model spiral)
- Minimum 7 iterations recommended
- Each round: Model A reviews Model B's output, generates improved version; then Model B reviews Model A's new output
- Stopping criterion: both models say the work is perfect and cannot be improved further
- Claimed to be domain-agnostic: works in medicine, programming, math, and any analytical field
- Can be automated with AutoGen, LangGraph, or CrewAI

## Tradeoffs
- Token-intensive: 7+ iterations across 2+ models is expensive
- Time-consuming: each ChatGPT 5 Pro call takes ~40 minutes with extended thinking
- Models may converge on confidently wrong answers if both share the same blind spots
- No guarantee of convergence -- some problems may never reach agreement

## Related
- [[concepts/Multi-Model-Convergence]] -- the parallel approach this builds on
- [[concepts/Iterative-Model-Refinement]] -- the iterative mechanism
- [[concepts/Expert-Committee-Simulation]] -- the metaphor this method enacts

## Source
[[summaries/JaviLopen-AI-Medical-Research-ARROWHEAD]]
