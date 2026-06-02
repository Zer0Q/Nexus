# Workflow Compilation

## Definition
Distilling a full agentic workflow -- multi-step LLM calls, tool invocations, intermediate scratchpads, and decision points -- into the weights of a fine-tuned small model. The student internalizes orchestration logic rather than only imitating final outputs, producing a "subterranean agent" that runs at ~100x lower inference cost.

## Why It Matters
Most production agents pay repeatedly for an orchestration loop they run thousands of times a day. Compiling that loop once into a cheap model changes the economics of deploying agentic systems, especially for high-volume narrow workflows.

## Key Ideas
- The whole workflow is compiled, not just the answer -- including tool calls and decision points
- Orchestrator dissolved into the model -- no per-call orchestration overhead
- Near-frontier quality preserved while cutting inference cost by ~two orders of magnitude
- Savings come from collapsing many model calls into one forward pass
- Best suited for high-volume, narrow workflows where the procedure is stable

## Tradeoffs
- Compilation is a one-time cost; if the workflow changes, recompilation is needed
- Narrow specialization -- compiled model handles specific workflows, not general tasks
- Quality gap vs original workflow -- "near-frontier" means some degradation

## Related
- [[concepts/Harness-Engineering]]
- [[concepts/Context-Efficiency-Frontier]]
- [[concepts/Agent-Logic]]

## Source
[[source-notes/DAIR-Top-AI-Papers-of-the-Week]]
