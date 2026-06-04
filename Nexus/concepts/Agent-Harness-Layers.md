# Agent Harness Layers

## Definition
Three-layer architecture for production AI agents: Model Layer (LLM selection and routing), Agent Layer (identity, memory, tools), and Runtime Layer (session management, sandboxing, CI).

## Why It Matters
Most "AI agents" are demos — a prompt wrapped in a loop. Production agents need proper layering: model routing, identity management, tool access control, session persistence, and automated testing.

## Key Ideas
- Model Layer: config-driven model selection, fallback providers
- Agent Layer: identity as URL path, tool permissions, memory scope
- Runtime Layer: session management, sandboxing, CI/CD integration
- Each layer is independently configurable
- Runtime config file controls model layer behavior

## Tradeoffs
- More complexity than single-prompt agents
- Requires infrastructure knowledge
- Debugging spans multiple layers

## Related
- [[summaries/AddyOsmani-Agent-Harness-Engineering]]
- [[concepts/Hermes-Agent-Architecture]]
- [[concepts/Five-Layer-AI-Stack]]

## Source
[[summaries/Av1dlive-build-ai-agents-2026-course]]
