# Single vs Fleet Loop

## Definition
The scale distinction in loop engineering: single-agent loops use one brain running the full DISCOVER → PLAN → EXECUTE → VERIFY → ITERATE cycle on itself, while fleet loops deploy an orchestrator that breaks goals into pieces, hands each to specialist agents, which spawn their own subagents — every agent in the tree runs the same 5-stage loop.

## Why It Matters
A single-agent loop is like a person redoing their own draft. A fleet loop is a whole team running a project end-to-end. The fleet pattern enables parallelization across specialized domains but multiplies token costs by the number of agents in the tree.

## Key Ideas
- Single-agent: one brain, self-improving, good for focused tasks with limited scope
- Fleet: orchestrator owns the goal, specialists own the steps, subagents do narrow work, eval gates ensure quality
- Example fleet structure: orchestrator → research specialist + engineering specialist + QA specialist → each spawns subagents (web researcher, code debugger, bug tracker)
- Every agent in the fleet runs the same 5-stage loop: DISCOVER → PLAN → EXECUTE → VERIFY → ITERATE
- Fleet loops cost 500K-2M tokens vs 50K-200K for single-agent loops

## Tradeoffs
- Fleet loops enable parallel work but multiply token costs proportionally
- Coordination overhead: the orchestrator must track progress across all specialists
- Single-agent loops are simpler to debug but bottleneck on one model's capabilities

## Related
- [[concepts/Loop-Engineering]]
- [[concepts/Open-vs-Closed-Loop]]
- [[concepts/Token-Burn]]
- [[concepts/Maker-Checker-Split]]

## Source
[[summaries/Sairahul1-Loops-What-Every-AI-Engineer-Needs-to-Know]]
