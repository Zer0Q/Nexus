---
type: Tool
title: Drum-Buffer-Rope
description: 'Flow control methodology derived from Theory of Constraints. Drum: the
  constraint''s pace sets the system rhythm. Buffer: time or inventory before the
  constra...'
tags:
- tools
timestamp: '2026-06-16T13:58:58Z'
---

# Drum-Buffer-Rope

## Definition
Flow control methodology derived from Theory of Constraints. Drum: the constraint's pace sets the system rhythm. Buffer: time or inventory before the constraint to ensure it never starves. Rope: synchronization mechanism that controls work release based on constraint consumption.

## Why It Matters
Prevents system overload and work-in-progress accumulation by synchronizing all upstream processes to the constraint's actual capacity. Directly applicable to any pipeline or queue-based system.

## Key Ideas
- Drum: constraint's processing rate dictates overall system pace
- Buffer: protective cushion before the constraint absorbs upstream variability
- Rope: signals when to release new work, preventing system saturation
- Without Rope, upstream produces faster than constraint can process -> WIP pileup

## Tradeoffs
- Requires accurate measurement of constraint capacity
- Buffer sizing is a balancing act: too small = starvation, too large = hidden waste

## Related
- [[tools/Theory-of-Constraints]], [[concepts/Continuous-Batching]], [[concepts/Async-Queue-Pattern]]

## Source
[[summaries/Goldratt-Theory-of-Constraints]]
