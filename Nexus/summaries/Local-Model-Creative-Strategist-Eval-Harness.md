---
type: article
title: "How to build a local-model creative strategist"
description: "Building an eval harness for creative strategy judgment: why the loop around training matters more than the fine-tune itself."
resource: "https://x.com/VibeMarketer_/status/2067967513246249337"
timestamp: 2026-06-19
tags:
  - eval-harness
  - creative-strategy
  - local-models
  - fine-tuning
  - evaluation
---

## Synthesis

The author built a Meta ads creative performance analyst using a local VLM — not to beat frontier models on general intelligence, but to learn one narrow judgment: given a creative asset, campaign objective, and metric pattern, what should we test next?

The key finding: the eval harness became more valuable than the fine-tune. Training the model was only one part. The real product was the loop: dataset -> model output -> review -> score -> failure cluster -> correction -> promotion gate. This loop turned the project from "fine-tune a model" into "build a system that can tell whether the model is improving."

Six evaluation criteria were defined: visual truthfulness (does the model describe what's actually visible?), metric reasoning (does it understand the performance pattern?), objective discipline (does the recommendation respect the campaign objective?), next-test quality (is it specific enough to run?), overall usefulness, and generic recommendation rate.

The most useful result was a negative one: a newer model candidate that looked better on surface metrics (pass rate 81.6% -> 82.9%) but was actually worse on usefulness (4.17 -> 4.03) and had generic CTA recommendations jump from 35.5% to 72.4%. The champion gate prevented promoting it.

## Key Insights

- Training is not the product. The product is the loop around training: dataset quality, rubric design, review workflow, failure analysis, promotion gates
- Meta ad metrics are signals, not causal proof. The model must frame conclusions as hypotheses, not causal claims
- A clean schema can make weak reasoning look more finished than it is. Schema validity is the entry ticket, not the goal
- The "useful failure" taxonomy is more valuable than overall quality scores: different failure clusters point to different fixes
- Champion gates protect against the bias of wanting your new model to win after investing time in training

## Questions

- Can this eval harness pattern be generalized to other narrow judgment domains beyond creative strategy?
- What's the minimum viable dataset size for teaching creative strategy judgment?
- How does multimodal input affect the evaluation rubric compared to text-only?
