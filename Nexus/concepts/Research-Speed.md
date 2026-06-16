---
type: Concept
title: Research Speed
description: 'The velocity at which a researcher discovers they are wrong. Research
  speed is determined by feedback loop tightness: how fast you can launch an experiment,
  ...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Research Speed

## Definition
The velocity at which a researcher discovers they are wrong. Research speed is determined by feedback loop tightness: how fast you can launch an experiment, plot results, compare runs, and update your mental model. Tooling is a first-class research activity.

## Why It Matters
The stories about breakthrough researchers rarely involve single strokes of genius — they involve volume. More runs per day, more wrong ideas discarded per week, a model of reality that updated faster than anyone else's. The researcher who can build the harness, the eval, and the data pipeline is the one whose hypotheses actually get tested. Everyone else is waiting in a queue.

## Key Ideas
- Launching a run should be one command. Plotting it should be one more. Comparing two runs should take seconds, not an afternoon of archaeology
- Karpathy's recipe: overfit a single batch before training at scale — thirty seconds, half your bugs gone
- Shrink everything until it is cheap, get it right, then spend the compute
- Every experiment should be reproducible from its config
- Engineering and research have fused at the frontier — the researcher who cannot build their own tooling is rate-limited by the engineering queue

## Tradeoffs
- Over-investing in tooling can delay actual research — the harness should serve the hypothesis, not become the project
- Reproducibility infrastructure has upfront cost that pays off over many runs
- Fast loops encourage quantity over depth — balance volume with careful analysis of failures

## Related
- [[concepts/Research-Taste]]
- [[concepts/Failure-Analysis]]
- [[concepts/Outcome-Driven-Research]]

## Source
[[summaries/ItsReallyVivek-How-to-Be-Good-at-Research]]
