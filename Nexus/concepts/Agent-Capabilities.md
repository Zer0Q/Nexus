# Agent Capabilities

## Definition
Composable units that bundle tools, hooks, instructions, and model settings into reusable agent features. Examples: Thinking(), WebSearch(), MCP(). Enable modular agent design.

## Why It Matters
Capabilities allow building agents from reusable, tested components rather than monolithic prompts. Similar to middleware or plugins in web frameworks.

## Key Ideas
- Capabilities bundle related functionality (tools + instructions + settings)
- Built-in: Thinking, WebSearch, MCP
- Custom: create your own capability classes
- Pydantic AI Harness library for shared capabilities
- Composable: stack multiple capabilities on one agent
- YAML/JSON agent specification for no-code capability definition

## Tradeoffs
- Each capability adds complexity and token overhead
- Capability interactions may have unintended side effects

## Related
- [[tools/PydanticAI]]
- [[concepts/Augmented-LLM]]

## Source
[[source-notes/Pydantic-Team-Pydantic-AI-Overview]]
