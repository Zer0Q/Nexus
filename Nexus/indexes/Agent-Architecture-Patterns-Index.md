---
type: Index
title: Agent Architecture Patterns Index
description: '## Related - [[concepts/Agent-Swarm-Architecture]] -- swarm-based multi-agent
  coordination - [[concepts/Multi-Agent-Development]] -- building systems with mu...'
tags:
- indexes
timestamp: '2026-06-16T13:58:58Z'
---

# Agent Architecture Patterns Index

## Overview
Patterns and anti-patterns for building reliable, scalable AI agent systems.

## Core Concepts
- [[concepts/Agentic-System-Architecture]] -- workflows vs agents distinction, start simple
- [[concepts/Augmented-LLM]] -- LLM + retrieval, tools, memory as foundational building block
- [[concepts/Agent-Computer-Interface]] -- tool design principles: tokens to think, natural formats, poka-yoke
- [[concepts/Prompt-Chaining-Workflow]] -- sequential LLM calls with gates between steps
- [[concepts/Routing-Workflow]] -- classify input, route to specialized handlers
- [[concepts/Parallelization-Workflow]] -- simultaneous LLM calls: sectioning and voting
- [[concepts/Orchestrator-Workers-Workflow]] -- central LLM delegates to workers dynamically
- [[concepts/Evaluator-Optimizer-Workflow]] -- iterative generation + feedback loop
- [[concepts/Agent-Dependency-Injection]] -- type-safe runtime data into agent tools
- [[concepts/Agent-Structured-Output]] -- constrain LLM responses to predefined schemas
- [[concepts/Durable-Agent-Execution]] -- preserve agent progress across failures and restarts
- [[concepts/Agent-Graph-Support]] -- type-hinted graph definitions for complex workflows
- [[concepts/Specialized-Agent-Crews]] -- multiple focused agents with clear ownership
- [[concepts/Research-First-Architecture]] -- research agent as input intelligence layer
- [[concepts/Runtime-Monitoring]] -- supervisor watching intended vs actual flow
- [[concepts/Cost-Tracking]] -- logging exact cost per run for autonomous loops
- [[concepts/Model-Diversity]] -- multi-provider resilience against downtime and pricing changes
- [[concepts/Agent-Decay]] -- gradual degradation without weekly audits
- [[concepts/Content-Agent-Architecture]] -- taste, thesis, proof, forbidden patterns beyond voice
- [[concepts/Feedback-Loop-Training]] -- 6-step cycle: produce, flag, correct, encode, tighten, repeat
- [[concepts/Skill-Bundling]] -- skills as directories with SKILL.md + references/ + scripts/
- [[concepts/Echo-Chamber-Bias]] -- self-reinforcing loops in agent-curated research
- [[concepts/Tool-Selection-Hierarchy]] -- direct API > MCP > skill > Browser CDP > web search

## Tools
- [[tools/PydanticAI]] -- Python agent framework by Pydantic team, type-safe, model-agnostic
- [[tools/Firecrawl]] -- URL-to-markdown/JSON with JS rendering and CAPTCHA handling
- [[tools/Crawl4AI]] -- LLM-pipeline-focused scraper with clean structured output
- [[tools/Browser-Use]] -- full browser control for AI agents
- [[tools/AgentQL]] -- semantic query language for AI agents

## Related
- [[concepts/Agent-Swarm-Architecture]] -- swarm-based multi-agent coordination
- [[concepts/Multi-Agent-Development]] -- building systems with multiple cooperating agents
- [[concepts/Vault-Aware-Research]] -- agent research that queries existing knowledge vaults

## Sources
- [[summaries/Anthropic-Building-Effective-AI-Agents]]
- [[summaries/Pydantic-Team-Pydantic-AI-Overview]]
- [[summaries/KusCamara-PydanticAI-Agent-Creation]]
- [[summaries/gkisokay-21-Mistakes-Building-AI-Agents]]
- [[summaries/0xJeff-Hermes-Analyst-60-Days]]
- [[summaries/DamiDefi-20-GitHub-Scraping-Repos]]
