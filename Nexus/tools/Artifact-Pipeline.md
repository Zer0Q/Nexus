---
type: Tool
title: Artifact Pipeline
description: 'The sequence of artifacts produced during AI-assisted development: Intent
  -> Spec -> Acceptance Criteria -> Architecture Constraints -> Tests -> Code -> Veri...'
tags:
- tools
timestamp: '2026-06-16T13:58:58Z'
---

# Artifact Pipeline

## Definition
The sequence of artifacts produced during AI-assisted development: Intent -> Spec -> Acceptance Criteria -> Architecture Constraints -> Tests -> Code -> Verification. Each artifact feeds the next, creating traceability through the development process.

## Why It Matters
Defining the artifact pipeline is more important than choosing a specific tool. The pipeline ensures that each stage produces verifiable output before proceeding, preventing the accumulation of technical debt at scale.

## Key Ideas
- Intent: what problem are we solving
- Spec: detailed requirements and constraints
- Acceptance Criteria: verifiable conditions for completion
- Architecture Constraints: technical boundaries and decisions
- Tests: automated verification before code generation
- Code: implementation guided by all previous artifacts
- Verification: final validation against acceptance criteria

## Related
- [[tools/Spec-Driven-Development]], [[tools/BMAD-Method]], [[concepts/Agentic-SDLC]]

## Source
[[summaries/SDD-vs-BMAD-Frameworks-Comparison]]
