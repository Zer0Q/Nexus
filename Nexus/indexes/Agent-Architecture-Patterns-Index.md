# Agent Architecture Patterns Index

## Overview
Patterns and anti-patterns for building reliable, scalable AI agent systems.

## Core Concepts
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
- [[tools/Firecrawl]] -- URL-to-markdown/JSON with JS rendering and CAPTCHA handling
- [[tools/Crawl4AI]] -- LLM-pipeline-focused scraper with clean structured output
- [[tools/Browser-Use]] -- full browser control for AI agents
- [[tools/AgentQL]] -- semantic query language for AI agents

## Related
- [[concepts/Agent-Swarm-Architecture]] -- swarm-based multi-agent coordination
- [[concepts/Multi-Agent-Development]] -- building systems with multiple cooperating agents
- [[concepts/Vault-Aware-Research]] -- agent research that queries existing knowledge vaults

## Sources
- [[source-notes/gkisokay-21-Mistakes-Building-AI-Agents]]
- [[source-notes/0xJeff-Hermes-Analyst-60-Days]]
- [[source-notes/DamiDefi-20-GitHub-Scraping-Repos]]
