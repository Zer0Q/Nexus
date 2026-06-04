---
title: "Creación de agentes AI con PydanticAI"
source: "https://dev.to/kuscamara/creacion-de-agentes-ai-con-pydanticai-introduccion-h8"
author: "Kus Cámara"
published: "2025-11-05"
type: article
---

# PydanticAI Agent Creation Tutorial

## Summary
Spanish-language tutorial on building AI agents with PydanticAI. Covers LLM setup (GitHub Models, Google AI Studio, Ollama), agent configuration with system prompts, tool integration, and structured output using Pydantic models. Practical example: a recipe recommendation agent.

## Core Concepts
- [[tools/PydanticAI]] -- Python agent framework built by the Pydantic team
- [[concepts/Agent-System-Prompt]] -- Instructions that configure LLM behavior, purpose, and guardrails
- [[concepts/Agent-Tool-Use]] -- Functions agents call to interact with external systems
- [[concepts/LLM-Structured-Output]] -- Forcing LLM responses into predefined schemas
- [[concepts/Local-LLM-Options]] -- Ollama, local model selection for agent experimentation

## Key Insights
- Agent = LLM + system prompt + tools (three-component model)
- Tool descriptions come from function docstrings -- PydanticAI generates schemas automatically
- LLM reasons about tool output and generates elaborated responses beyond raw tool return values
- Deterministic operations (datetime.now, calculations) should be tools, not LLM tasks
- output_type parameter constrains agent output to a Pydantic BaseModel structure
- Free LLM options: GitHub Models, Google AI Studio, Ollama for local experimentation

## Open Questions
- How does PydanticAI tool schema generation compare to Anthropic's tool format recommendations?
