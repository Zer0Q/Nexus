---
type: Concept
title: Pydantic JSON Schema
description: Automatic JSON Schema generation from Pydantic models via model_json_schema().
  Produces a standard JSON Schema document describing field types, constraints, ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Pydantic JSON Schema

## Definition
Automatic JSON Schema generation from Pydantic models via model_json_schema(). Produces a standard JSON Schema document describing field types, constraints, defaults, and relationships.

## Why It Matters
JSON Schema is the universal format for describing data structure. Pydantic generates it automatically from type annotations, enabling cross-language validation, API documentation, and IDE autocomplete.

## Key Ideas
- model_json_schema() returns dict representing JSON Schema
- Includes $defs for nested model definitions
- Field constraints (min_length, pattern, gt, enum) map to JSON Schema keywords
- Aliases affect the generated schema property names
- Used by FastAPI for OpenAPI documentation
- Consumable by any JSON Schema validator in any language

## Tradeoffs
- Complex validators don't always translate cleanly to JSON Schema
- Custom error types need manual schema extension

## Related
- [[concepts/Pydantic-BaseModel]]
- [[concepts/Pydantic-Field-Constraints]]

## Source
[[summaries/RealPython-Pydantic-Data-Validation]]
[[summaries/Pydantic-Team-Pydantic-Models]]
