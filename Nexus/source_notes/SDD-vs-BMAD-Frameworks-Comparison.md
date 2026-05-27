---
title: "SDD vs BMAD - AI Development Frameworks Comparison"
source: "ChatGPT analysis"
published: "2026-05-27"
type: analysis
---

# AI Development Frameworks Landscape

## Summary
Comparison of AI-assisted development methodologies from classical (TDD, BDD) to AI-native (SDD, BMAD, Agentic SDLC). Key insight: no single framework wins — the winning stack layers multiple approaches. BMAD operationalizes classic Agile practices for LLM agents.

## Core Concepts
- [[Spec-Driven-Development]] -- spec as central artifact (Spec-Kit, OpenSpec, BMAD)
- [[BMAD-Method]] -- multi-agent Agile simulation for medium/large projects
- [[Vibe-Coding]] -- prompt-to-code for PoCs; lacks traceability
- [[Agentic-SDLC]] -- AI agents in full SDLC: analysis, code, test, PR
- [[Artifact-Pipeline]] -- Intent -> Spec -> Tests -> Code -> Verification
- [[Multi-Agent-Development]] -- specialized AI agents with role separation
- [[Context-Explosion]] -- large specs degrade agent quality

## Key Insights
- BMAD is not revolutionary — it's Agile + Multi-Agent Orchestration + SDD adapted for LLM agents
- Critical weakness: context explosion. Large specs degrade agent quality
- AI amplifies ambiguity — without verifiable specs, you generate code faster AND debt faster
- Artifact pipeline matters more than tool choice: Intent -> Spec -> Acceptance Criteria -> Architecture -> Tests -> Code -> Verification

## Open Questions
- How do fitness functions integrate with AI agent workflows?
- Can contract testing (Pact) work effectively with AI-generated code?
