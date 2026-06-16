---
type: Concept
title: Pydantic Validation Context
description: Runtime context passed to validators via ValidationInfo.context. Enables
  dynamic validation behavior based on request-specific data without changing the
  mode...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Pydantic Validation Context

## Definition
Runtime context passed to validators via ValidationInfo.context. Enables dynamic validation behavior based on request-specific data without changing the model definition.

## Why It Matters
Some validation rules depend on runtime conditions: user role, feature flags, or request metadata. Context passes this information to validators without polluting the model schema.

## Key Ideas
- model_validate(data, context={'key': 'value'}) passes context to all validators
- ValidationInfo.context accessed in validator functions
- Context is optional -- validators must handle None context
- Use ContextVar + custom __init__ for context in direct model instantiation
- Common patterns: user permissions, request ID, tenant ID, feature flags
- Also works for serialization context

## Tradeoffs
- Context not available in __init__ constructor (only model_validate)
- Workaround with ContextVar adds complexity
- Context type is Any -- validators must check isinstance

## Related
- [[concepts/Pydantic-Validators]]
- [[concepts/Pydantic-Model-Config]]

## Source
[[summaries/Pydantic-Team-Pydantic-Validators]]
