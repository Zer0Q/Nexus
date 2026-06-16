---
type: Tool
title: Hardware First Engine Selection
description: You do not pick an inference engine first. You pick a hardware strategy,
  a workload shape, and a serving model. The engine follows the answers.
tags:
- tools
timestamp: '2026-06-16T13:58:58Z'
---

# Hardware First Engine Selection

## Definition
You do not pick an inference engine first. You pick a hardware strategy, a workload shape, and a serving model. The engine follows the answers.

## Why It Matters
Choosing an engine before answering hardware and workload questions leads to mismatches: wrong parallelism strategy, underutilized memory, or unnecessary complexity.

## Key Ideas
- 10 decision questions: hardware, memory fit, bottleneck phase, context/concurrency, prefix sharing, model type, serving scope, quant format, interconnect, optimization target
- Engine selection is a constraint satisfaction problem, not a feature comparison
- The same engine is wrong for different workloads even on identical hardware

## Related
- [[concepts/Prefill-vs-Decode]]
- [[concepts/Memory-Bandwidth-Bottleneck]]
- [[concepts/Interconnect-Bottleneck]]

## Source
[[summaries/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
