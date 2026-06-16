---
type: Concept
title: Failure Analysis
description: The systematic practice of pulling failure cases, reading all of them,
  sorting into piles by failure mode, and attacking the biggest pile. Works on models
  an...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Failure Analysis

## Definition
The systematic practice of pulling failure cases, reading all of them, sorting into piles by failure mode, and attacking the biggest pile. Works on models and evals — a benchmark you have never read transcripts from is a benchmark you do not actually understand.

## Why It Matters
A descending loss curve is not analysis, it is reassurance. Most ML bugs live in the data and fail silently — nothing crashes, you simply get a mediocre model and a wrong theory about why. One transcript of genuinely strange behavior teaches more than the next decimal of accuracy.

## Key Ideas
- Andrew Ng's method: pull 100 failures, read all of them, sort into piles, attack the biggest pile
- Karpathy's recipe starts before any training code: hours spent on raw data by hand
- Most ML bugs live in the data and fail silently — no crash, just a mediocre model
- Experiments throw off far more information than you consume: transcripts, failure cases, the strange tail of the distribution
- Most of it dies unread in a logs folder

## Tradeoffs
- Failure analysis is unglamorous and time-consuming — easier to chase benchmark numbers
- Requires access to raw failure transcripts, not just aggregate metrics
- Can reveal data quality issues that require starting over rather than quick fixes

## Related
- [[concepts/Research-Speed]]
- [[concepts/Research-Taste]]
- [[concepts/Bad-Data-as-Diagnostic]]

## Source
[[summaries/ItsReallyVivek-How-to-Be-Good-at-Research]]
