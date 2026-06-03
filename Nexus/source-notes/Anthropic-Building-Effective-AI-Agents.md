---
title: "Building Effective AI Agents"
source: "https://www.anthropic.com/engineering/building-effective-agents"
author: "Anthropic"
published: ""
type: article
---

# Anthropic Guide to Building Effective AI Agents

## Summary
Anthropic's practical guide to building agentic systems, distilled from work with dozens of production teams. Key distinction: workflows (predefined code paths) vs agents (LLM directs own process). Presents five workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) and the autonomous agent pattern. Emphasizes simplicity over complexity.

## Core Concepts

- [[glossary/System-Prompt]] -- Initial instruction that sets AI behavior and constraints
- [[glossary/Evaluator-Optimizer]] -- Two-agent pattern where one generates and one evaluates
- [[glossary/Agentic-System]] -- Autonomous system that perceives, reasons, and acts toward goals
- [[concepts/Agentic-System-Architecture]] -- Workflows (predefined) vs agents (LLM-directed)
- [[concepts/Prompt-Chaining-Workflow]] -- Sequential LLM calls with programmatic gates
- [[concepts/Routing-Workflow]] -- Input classification directing to specialized downstream tasks
- [[concepts/Parallelization-Workflow]] -- Sectioning (independent subtasks) and voting (diverse outputs)
- [[concepts/Orchestrator-Workers-Workflow]] -- Central LLM delegates to worker LLMs dynamically
- [[concepts/Evaluator-Optimizer-Workflow]] -- Generate-evaluate-refine loop
- [[concepts/Augmented-LLM]] -- LLM + retrieval + tools + memory as building block
- [[concepts/Agent-Computer-Interface]] -- Tool design principles for LLM consumption
- [[concepts/Agent-Tool-Use]] -- Clear tool documentation and poka-yoke design
- [[concepts/Routing-Workflow]] -- Pattern for directing requests to specialized handlers
## Key Insights
- Start with simple prompts, add complexity only when it demonstrably improves outcomes
- Frameworks abstract away useful debugging visibility -- understand what's under the hood
- Augmented LLM (retrieval + tools + memory) is the foundational building block
- Prompt chaining: trade latency for accuracy by decomposing tasks
- Routing: separate concerns, optimize per input category, route easy->cheap model
- Parallelization: sectioning for guardrails/evals, voting for confidence
- Orchestrator-workers: flexible subtask decomposition (coding, multi-source search)
- Evaluator-optimizer: iterative refinement when LLM can articulate feedback
- Agents: LLM + tools + environment feedback loop, with stopping conditions
- Three core principles: simplicity, transparency, careful ACI design
- Poka-yoke tools: make it harder for the model to make mistakes (absolute paths > relative)
- Spent more time optimizing tools than overall prompt for SWE-bench agent
## Open Questions
- How do the workflow patterns compose when building multi-agent systems?
