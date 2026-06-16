---
type: Concept
title: Comprehension Debt
description: The gap between what code exists in your codebase and what you actually
  understand. Grows faster when loops ship code you didn't write yourself — the smoothe...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Comprehension Debt

## Definition
The gap between what code exists in your codebase and what you actually understand. Grows faster when loops ship code you didn't write yourself — the smoother the loop, the faster the debt accumulates unless you actively read what the loop produced.

## Why It Matters
Comprehension debt is invisible until you need to change something and don't understand the system. A loop running unattended is also a loop making mistakes unattended. If you rely entirely on automated loops without reviewing the output, your product quality suffers and you end up digging yourself into a deeper hole.

## Key Ideas
- The faster the loop ships code you didn't write, the bigger the comprehension gap
- A smooth loop just makes comprehension debt grow faster unless you read what the loop made
- Your job is to ship code you confirmed works — verification is still on you
- The comfortable posture is the risky one: when the loop runs itself, it's tempting to stop having an opinion
- Two people can build the exact same loop and get opposite results: one moves faster on work they understand deeply, the other uses it to avoid understanding the work entirely

## Related
- [[concepts/Cognitive-Surrender]]
- [[concepts/Loop-Engineering]]
- [[concepts/Agent-Loop]]

## Source
[[summaries/AddyOsmani-Loop-Engineering]], [[summaries/Tonbis-What-Actually-Are-Loops]]
