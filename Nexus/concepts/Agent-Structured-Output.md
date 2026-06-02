# Agent Structured Output

## Definition
Constraining agent/LLM responses to predefined schemas (Pydantic models, dataclasses). The framework generates JSON Schema from the model, instructs the LLM to conform, and validates the output at runtime.

## Why It Matters
Free-text LLM output is hard to parse programmatically. Structured output guarantees the response matches a known schema, enabling reliable downstream processing, API responses, and data pipelines.

## Key Ideas
- output_type parameter on Agent constrains response to a Pydantic model
- Framework generates JSON Schema, passes to LLM as output instructions
- Runtime validation: if LLM output doesn't match schema, agent retries (reflection)
- Field descriptions in the model become LLM instructions for each field
- Supports nested models, enums, lists, optional fields
- Streamed structured output: continuous validation as tokens arrive

## Tradeoffs
- Complex schemas increase token usage and LLM confusion
- Reflection retries add latency and cost
- LLM may struggle with deeply nested or highly constrained schemas

## Related
- [[tools/PydanticAI]]
- [[concepts/Pydantic-JSON-Schema]]
- [[concepts/Pydantic-Validation]]

## Source
[[source-notes/Pydantic-Team-Pydantic-AI-Overview]]
[[source-notes/KusCamara-PydanticAI-Agent-Creation]]
