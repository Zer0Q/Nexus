# AI Development Index

## Overview
Frameworks, tools, and concepts for AI-assisted software development — from vibe coding to structured multi-agent workflows.

## Core Concepts
- [[Vibe-Coding]] -- prompt-to-code, no intermediate artifacts
- [[Multi-Agent-Development]] -- specialized AI agents with defined roles
- [[Context-Explosion]] -- large specs degrade agent quality
- [[Agentic-SDLC]] -- AI agents in analysis, code, test, PR
- [[Artifact-Pipeline]] -- Intent -> Spec -> Tests -> Code -> Verification

## Frameworks
- [[Spec-Driven-Development]] -- spec as central artifact
- [[BMAD-Method]] -- Agile simulation with AI agents
- [[Artifact-Pipeline]] -- structured artifact flow

## Tools
- [[BMAD-Method]] -- full Agile simulation (npx bmad-method)
- [[Spec-Kit]] -- GitHub's minimalist SDD toolkit
- [[OpenSpec]] -- lightweight iterative specs
- [[OpenHands]] -- autonomous repo modification agent
- [[Open-SWE]] -- GitHub issue to PR agent
- [[smolagents]] -- Hugging Face agent SDK

## Comparison
| Approach | Best For | Risk |
| --- | --- | --- |
| Vibe Coding | PoCs, spikes | No traceability |
| Spec-Kit / OpenSpec | Features, medium projects | Document overhead |
| BMAD | Products, complex systems | Context explosion |
| OpenHands / Open-SWE | Existing repos with issues | Variable PR quality |

## Glossary
- [[SDD]]
- [[PRD]]
- [[BDD]]
- [[TDD]]

## Sources
- [[BMAD-Method-Getting-Started]]
- [[SDD-vs-BMAD-Frameworks-Comparison]]
