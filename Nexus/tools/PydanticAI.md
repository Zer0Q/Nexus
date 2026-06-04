# PydanticAI

## Definition
Python agent framework built by the Pydantic team, designed to bring FastAPI-like ergonomics to GenAI agent development. Model-agnostic, type-safe, with composable capabilities, dependency injection, and seamless observability via Logfire.

## Why It Matters
Built by the creators of Pydantic Validation (used by OpenAI SDK, Anthropic SDK, LangChain, etc.). Leverages Pydantic's type system for agent definitions, ensuring compile-time safety and IDE support. Alternative to LangChain, CrewAI, and smolagents.

## Key Ideas
- Agent(model, instructions, deps_type, output_type, capabilities)
- Model-agnostic: OpenAI, Anthropic, Gemini, Ollama, LiteLLM, 20+ providers
- Dependency injection via deps_type + RunContext for type-safe tool access
- Structured output: output_type=MyModel guarantees validated return type
- Tool decorators: @agent.tool (with context) and @agent.tool_plain
- Dynamic instructions: @agent.instructions decorator with dependency access
- Composable capabilities: Thinking(), WebSearch(), MCP(), custom units
- Reflection and self-correction: retries when output validation fails
- Graph support: type-hinted definitions for complex control flow
- Durable execution: preserves progress across failures and restarts
- Human-in-the-loop: tool approval based on arguments/history/preferences
- Streamed outputs: continuous structured output with real-time validation
- MCP, A2A, UI event stream integrations
- YAML/JSON agent specification (no-code agent definition)
- Logfire integration: OpenTelemetry tracing, evals, cost tracking

## Tradeoffs
- Relatively new framework -- smaller ecosystem than LangChain
- Tied to Pydantic ecosystem -- less flexible for non-Pydantic stacks
- Graph support still evolving vs LangGraph

## Related
- [[concepts/Agent-Dependency-Injection]]
- [[concepts/Agent-Structured-Output]]
- [[concepts/Durable-Agent-Execution]]
- [[concepts/Agent-Graph-Support]]

## Source
[[summaries/Pydantic-Team-Pydantic-AI-Overview]]
[[summaries/KusCamara-PydanticAI-Agent-Creation]]
