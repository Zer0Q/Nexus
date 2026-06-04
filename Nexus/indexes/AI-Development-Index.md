# AI Development Index

## Overview
Frameworks, tools, and concepts for AI-assisted software development — from vibe coding to structured multi-agent workflows.

## Core Concepts
- [[concepts/Vibe-Coding]] -- prompt-to-code, no intermediate artifacts
- [[concepts/Multi-Agent-Development]] -- specialized AI agents with defined roles
- [[concepts/Context-Explosion]] -- large specs degrade agent quality
- [[concepts/Agentic-SDLC]] -- AI agents in analysis, code, test, PR
- [[tools/Artifact-Pipeline]] -- Intent -> Spec -> Tests -> Code -> Verification

## Frameworks
- [[tools/Spec-Driven-Development]] -- spec as central artifact
- [[tools/BMAD-Method]] -- Agile simulation with AI agents
- [[tools/Artifact-Pipeline]] -- structured artifact flow

## Tools
- [[tools/PydanticAI]] -- Python agent framework by Pydantic team, type-safe, model-agnostic
- [[tools/BMAD-Method]] -- full Agile simulation (npx bmad-method)
- [[tools/Spec-Kit]] -- GitHub's minimalist SDD toolkit
- [[tools/OpenSpec]] -- lightweight iterative specs
- [[tools/OpenHands]] -- autonomous repo modification agent
- [[tools/Open-SWE]] -- GitHub issue to PR agent
- [[tools/smolagents]] -- Hugging Face agent SDK

## Comparison
| Approach | Best For | Risk |
| --- | --- | --- |
| Vibe Coding | PoCs, spikes | No traceability |
| Spec-Kit / OpenSpec | Features, medium projects | Document overhead |
| BMAD | Products, complex systems | Context explosion |
| OpenHands / Open-SWE | Existing repos with issues | Variable PR quality |

## Glossary
- [[concepts/SDD]]
- [[concepts/PRD]]
- [[concepts/BDD]]
- [[concepts/TDD]]

## Sources
- [[summaries/Pydantic-Team-Pydantic-AI-Overview]]
- [[summaries/KusCamara-PydanticAI-Agent-Creation]]
- [[summaries/Pydantic-Team-Pydantic-Models]]
- [[summaries/Pydantic-Team-Pydantic-Validators]]
- [[summaries/RealPython-Pydantic-Data-Validation]]
- [[summaries/Torque-Pydantic-Data-Transformation]]
- [[summaries/Anthropic-Building-Effective-AI-Agents]]
- [[summaries/BMAD-Method-Getting-Started]]
- [[summaries/SDD-vs-BMAD-Frameworks-Comparison]]
