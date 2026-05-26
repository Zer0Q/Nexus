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
- [[Prefill-vs-Decode]]
- [[Memory-Bandwidth-Bottleneck]]
- [[Interconnect-Bottleneck]]

## Source
[[TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
