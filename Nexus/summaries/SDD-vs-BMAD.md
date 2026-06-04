---
title: "SDD vs BMAD — AI Development Frameworks Comparison"
source: "https://chatgpt.com/?temporary-chat=true"
author: "ChatGPT"
published: "2026-05-27"
type: article
---

# SDD vs BMAD Frameworks

## Summary
Comparison of AI-assisted development methodologies: Spec-Driven Development (GitHub Spec Kit, OpenSpec), BMAD Method (multi-agent Agile simulation), and traditional approaches (TDD, BDD, Contract-driven). The winning stack for serious AI-augmented software is a pipeline: BDD/SDD → Architecture Constraints → TDD → Contract Tests → Agentic Coding → CI/Evals. The core risk: AI amplifies ambiguity — without verifiable specs, you generate code faster and debt faster.

## Core Concepts
- [[concepts/Spec-Driven-Development]] -- spec-first methodology: define what before asking AI to build it
- [[concepts/BMAD-Method]] -- multi-agent Agile simulation with AI roles (analyst, PM, architect, dev, QA)
- [[concepts/Context-Engineering]] -- systematic curation of project info into AI working memory; quality of AI output bounded by quality of context
- [[concepts/Agentic-SDLC]] -- AI agents in analysis, coding, testing, PR phases; requires governance and security
- [[concepts/Code-Overload]] -- tech workers producing code so fast it becomes unmanageable; more code ≠ more productive
- [[concepts/Fitness-Function-Driven-Development]] -- automated architectural rules as quality gates
- [[concepts/Intent-Driven-Development]] -- intention → agents → implementation; emerging AI-native narrative
- [[concepts/Vibe-Coding]] -- prompt → code direct; good for demos/spikes, doesn't scale

## Key Insights
- BMAD is not revolutionary — it's Agile + Multi-Agent Orchestration + SDD operationalized for LLM agents
- The critical path: define artifact pipeline (Intent → Spec → Acceptance Criteria → Architecture Constraints → Tests → Code → Verification), not pick a tool
- AI amplifies ambiguity — without verifiable specs, you generate code faster AND debt faster
- For PoC: vibe coding + minimal TDD. For real features: Spec Kit/OpenSpec + TDD. For mission-critical: SDD + TDD + CDC + fitness functions
- BMAD's weakest link: context explosion. Large specs degrade agent quality
- The winning stack is never one methodology — it's a pipeline: BDD/SDD → Architecture Constraints → TDD → Contract Tests → Agentic Coding → CI/Evals
- Spec-Kit is minimalist spec-first; BMAD simulates full Agile team with AI roles; OpenSpec is lightweight iterative specs

## Open Questions
- How does [[concepts/Spec-Driven-Development]] compare to [[concepts/BMAD-Method]] in real enterprise teams with 50+ devs?
- Is [[concepts/Intent-Driven-Development]] a viable evolution or still too diffuse a concept?
- What's the overhead cost of [[concepts/Fitness-Function-Driven-Development]] for small teams?
