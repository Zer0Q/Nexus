---
type: concept
related:
- Active-Recall-Learning
- Mastery-Score-Tracking
- Concept-Note-Template
description: A review scheduling system based on Hermann Ebbinghaus's forgetting curve,
  which shows that roughly 70% of new information is forgotten within 24 hours unles...
tags:
- concepts
---


# Spaced-Repetition-System

## Definition
A review scheduling system based on Hermann Ebbinghaus's forgetting curve, which shows that roughly 70% of new information is forgotten within 24 hours unless reviewed at strategic intervals. Reviews are timed at the point of near-forgetfulness.

## Why It Matters
Stops the forgetting curve by timing reviews at the exact moment material is about to be lost. You never re-review material you have already fully retained. Every review minute is spent on the exact material that needs it.

## Key Ideas
- First review: 1 day after initial study
- Second review: 3 days after first
- Third review: 7 days after second
- Fourth review: 14 days after third
- Fifth review: 30 days after fourth
- Subsequent reviews: 60 days
- Mastery score determines interval adjustment: correct answer advances to next interval, incorrect answer resets to previous
- Built into the frontmatter of every concept note via review-due field

## Tradeoffs
- Requires maintaining review-due dates across all concept notes
- Less flexible than Anki's SM-2 algorithm for individual calibration

## Related
- [[concepts/Active-Recall-Learning]]
- [[concepts/Mastery-Score-Tracking]]
- [[tools/Concept-Note-Template]]
- [[concepts/Synthesis-Session]]
- [[concepts/Sequential-vs-Network-Learning]]

## Source
[[summaries/NeilXBT-Obsidian-Knowledge-Graph-Learning]]
