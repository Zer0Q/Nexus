# LLM Structured Output

## Definition
Constraining LLM responses to conform to predefined schemas (JSON Schema, Pydantic models, dataclasses). Ensures output is parseable and validated at runtime.

## Why It Matters
Free-text LLM output is unreliable for programmatic consumption. Structured output guarantees the response matches a known schema, enabling downstream processing.

## Key Ideas
- Schema generated from model definitions (Pydantic, dataclass, JSON Schema)
- LLM instructed to conform to schema in its response
- Runtime validation catches non-conforming output
- Reflection/retry when validation fails
- Supports: nested objects, enums, lists, optional fields, unions

## Tradeoffs
- Complex schemas increase token usage and LLM confusion
- LLM may struggle with deeply nested or highly constrained schemas
- Retry loops add latency

## Related
- [[concepts/Agent-Structured-Output]]
- [[concepts/Pydantic-JSON-Schema]]

## Source
[[source-notes/KusCamara-PydanticAI-Agent-Creation]]
