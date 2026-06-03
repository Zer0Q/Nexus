---
title: "Pydantic AI"
source: "https://pydantic.dev/docs/ai/overview/"
author: "Pydantic Team"
published: ""
type: article
---

# Pydantic AI Overview

## Summary
Official overview of Pydantic AI, a Python agent framework designed to bring the "FastAPI feeling" to GenAI development. Key features: model-agnostic, type-safe, composable capabilities, dependency injection, structured outputs, MCP/A2A integration, durable execution, graph support, and seamless Logfire observability.

## Core Concepts

- [[tools/PydanticAI]] -- Agent framework built by Pydantic team with FastAPI-like ergonomics
- [[concepts/Agent-Dependency-Injection]] -- Type-safe way to pass data/connections into agent tools and instructions
- [[concepts/Agent-Structured-Output]] -- Constraining LLM output to Pydantic models with automatic validation
- [[concepts/Agent-Tool-Use]] -- Functions decorated with @agent.tool, using RunContext for dependency access
- [[concepts/Agent-Reflection-Self-Correction]] -- Agent retries when output validation fails
- [[concepts/Agent-Capabilities]] -- Composable units bundling tools, hooks, instructions, and model settings
- [[concepts/Durable-Agent-Execution]] -- Preserving agent progress across failures and restarts
- [[concepts/Agent-Graph-Support]] -- Type-hinted graph definitions for complex control flow
- [[tools/PydanticAI]] -- Python framework for building AI agents with type safety
## Key Insights
- Pydantic Validation underlies OpenAI SDK, Google ADK, Anthropic SDK, LangChain, LlamaIndex, CrewAI, Instructor
- Model-agnostic: supports OpenAI, Anthropic, Gemini, Ollama, LiteLLM, 20+ providers
- Dynamic instructions via @agent.instructions decorator can access injected dependencies
- Tool docstrings become LLM descriptions; param descriptions extracted automatically
- Reflection: if output validation fails, agent is prompted to retry
- Graph support replaces spaghetti code in complex multi-agent applications
- YAML/JSON agent specification -- define agents without code
- Human-in-the-loop tool approval based on arguments, history, or user preferences
## Open Questions
- How does Pydantic AI's graph support compare to LangGraph or temporal workflows?
