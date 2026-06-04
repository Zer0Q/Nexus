# Orchestrator-Workers Workflow

## Definition
Central LLM dynamically breaks down tasks, delegates to worker LLMs, and synthesizes results. Subtasks are determined at runtime based on input, not predefined.

## Why It Matters
Some tasks can't be decomposed in advance. The orchestrator assesses the specific input and creates the right subtasks -- essential for coding, research, and complex analysis.

## Key Ideas
- Orchestrator: analyzes input, creates subtasks, delegates to workers
- Workers: execute specific subtasks, return results
- Key difference from parallelization: subtasks are dynamic, not predefined
- Best for: complex coding changes, multi-source research, adaptive problem-solving
- Orchestrator synthesizes worker results into final output

## Tradeoffs
- Orchestrator can make poor decomposition decisions
- Higher cost (orchestrator + multiple workers)
- Latency depends on number of worker rounds

## Related
- [[concepts/Agentic-System-Architecture]]
- [[concepts/Parallelization-Workflow]]
- [[concepts/Multi-Agent-Development]]

## Source
[[summaries/Anthropic-Building-Effective-AI-Agents]]
