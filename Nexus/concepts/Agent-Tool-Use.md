# Agent Tool Use

## Definition
Mechanism for LLMs to interact with external systems through callable functions. Tools provide structured input/output interfaces for APIs, databases, web search, code execution, and file operations.

## Why It Matters
Agents without tools are limited to their training data. Tool use enables real-time information access, external system interaction, and concrete actions in the world.

## Key Ideas
- Tools are functions with structured schemas (name, description, parameters)
- LLM decides when and how to call tools based on context
- MCP (Model Context Protocol) standardizes tool integration
- Tool selection is a critical skill -- too many tools overwhelm the LLM
- Well-documented tools with clear examples improve accuracy
- Tool results are fed back to the LLM for further reasoning

## Tradeoffs
- Each tool call adds latency and token cost
- Poor tool documentation leads to incorrect usage
- Too many tools can cause selection errors

## Related
- [[concepts/Augmented-LLM]]
- [[concepts/Agent-Computer-Interface]]
- [[concepts/MCP]]
- [[concepts/Tool-Use]]

## Source
[[summaries/Anthropic-Building-Effective-AI-Agents]]
[[summaries/KusCamara-PydanticAI-Agent-Creation]]
