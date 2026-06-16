---
title: how to be good at research
author: '@itsreallyvivek'
published: '2026-06-10'
type: article
resource: https://x.com/itsreallyvivek/status/2064686372737454155
timestamp: '2026-06-10T00:00:00Z'
description: 'Vivek presents research as a stack of trainable skills rather than innate
  talent. The framework covers seven dimensions: choosing your own problems (Hamming''...'
tags:
- summaries
---


# How to Be Good at Research

## Summary
Vivek presents research as a stack of trainable skills rather than innate talent. The framework covers seven dimensions: choosing your own problems (Hamming's "important problems" habit, Schulman's outcome-driven mode), upgrading inputs (old material, cross-disciplinary range, reading papers not threads), writing everything down (Feynman's anti-self-deception, Darwin's contradiction log), tightening the loop (Radford's volume, Karpathy's single-batch overfit), staring at outputs (Andrew Ng's failure analysis), wandering on purpose (breadth as insurance, ablation before publishing), and finding your people (Hamming's open door, generosity as compounding). The core thesis: research speed is the speed at which you discover you're wrong.

## Core Concepts
- [[concepts/Research-Taste]] -- the ability to predict experiment outcomes, identify important problems, and forecast which papers will matter; trained through repeated prediction + correction cycles
- [[concepts/Research-Speed]] -- research velocity determined by how fast you discover you're wrong; tooling is first-class research activity (one-command launches, reproducible configs, seconds-to-compare)
- [[concepts/Outcome-Driven-Research]] -- choosing an outcome you genuinely want to exist and reasoning backwards to experiments, rather than reading literature and hunting for improvements
- [[concepts/Failure-Analysis]] -- pulling 100 failures, reading all of them, sorting into piles, attacking the biggest pile; works on models and evals equally
- [[concepts/Research-Debt]] -- undigested ideas that choke fields; clear explanations are genuine contributions, not service jobs; public writing is the strongest unfakeable credential

## Key Insights
- Richard Hamming asked colleagues at Bell Labs what the important problems in their field were and why they weren't working on them — people changed lunch tables to avoid the question
- John Schulman's guide splits research into two modes: reading literature to find improvements vs choosing an outcome and reasoning backwards — the latter manufactures originality
- Taste is trained like a muscle: predict experiment results before running them, cover paper results and guess from methods, forecast which releases will matter in two years
- Old material is criminally underpriced: mixture of experts (1991), LSTMs (1997), backprop (1986), Shannon's creative thinking talk (1952) — the field reruns its own past on delay
- Claude Shannon's trick: shrink a problem until nearly trivial, crack the small version, reintroduce difficulty one piece at a time
- "Read the paper itself, not the thread summarizing it. The appendix is where the bodies are buried, and the limitations section is usually the most honest paragraph"
- Writing finds gaps your head papers over: untested assumptions, steps that don't follow, quiet contradictions
- Darwin wrote down any fact that cut against his theory on the spot — his own memory deleted inconvenient evidence faster than convenient kind
- Karpathy's recipe: overfit a single batch before training at scale — thirty seconds, half your bugs gone
- "The researcher who can build the harness, the eval, and the data pipeline is the one whose hypotheses actually get tested. Everyone else is waiting in a queue."
- Andrew Ng's failure analysis: pull 100 failures, read all, sort into piles, attack the biggest — one transcript of genuinely strange behavior teaches more than the next decimal of accuracy
- "A descending loss curve is not analysis, it's reassurance"
- Hamming's open door pattern: closed-door colleagues got more done per year, open-door colleagues did the work that mattered because interruptions carried information

## Open Questions
- How does [[concepts/Research-Taste]] transfer across domains — can taste trained in ML generalize to systems research or interpretability?
- If [[concepts/Research-Speed]] is about discovering you're wrong faster, what tooling patterns minimize the feedback loop for non-empirical research?
- Can [[concepts/Outcome-Driven-Research]] be combined with literature scanning without losing the originality advantage?

## Source
- **Raw note:** [[raw-notes/how-to-be-good-at-research]]
- **Original URL:** https://x.com/itsreallyvivek/status/2064686372737454155
