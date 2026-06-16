---
type: Concept
title: Pydantic Validation
description: Type-hint-based data validation and serialization library for Python.
  Uses Python type annotations to define schemas, then automatically validates, coerces,
  ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Pydantic Validation

## Definition
Type-hint-based data validation and serialization library for Python. Uses Python type annotations to define schemas, then automatically validates, coerces, and serializes data at runtime. Core validation engine written in Rust (pydantic-core) for performance.

## Why It Matters
- Most widely used data validation library in Python ecosystem
- Foundation for FastAPI, LangChain, OpenAI SDK, Anthropic SDK, Google ADK, CrewAI, Instructor
- Bridges the gap between Python's dynamic typing and production-grade data safety
- Catches schema issues at write-time (IDE autocomplete, type checkers) and runtime

## Key Ideas
- BaseModel defines schemas via type-annotated class attributes
- Automatic type coercion: str '123' -> int 123, tuple -> list, etc.
- Strict mode disables coercion for exact type matching
- Three validation modes: Python (dicts/objects), JSON (strings/bytes), strings (string-to-type)
- ValidationError aggregates all errors in a single exception with detailed context
- model_validate() for dicts, model_validate_json() for JSON, model_validate_strings() for string coercion
- model_dump() for Python dict serialization, model_dump_json() for JSON string output
- model_json_schema() generates JSON Schema for cross-language validation

## Tradeoffs
- Coercion is convenient but can silently lose information (float -> int truncation)
- Strict mode prevents coercion but rejects valid input formats
- Abstract container types (Sequence, Mapping) hurt validation performance vs concrete types (list, dict)

## Related
- [[concepts/Pydantic-BaseModel]]
- [[concepts/Pydantic-Validators]]
- [[concepts/Pydantic-Field-Constraints]]
- [[concepts/Pydantic-Data-Conversion]]

## Source
[[summaries/RealPython-Pydantic-Data-Validation]]
[[summaries/Pydantic-Team-Pydantic-Models]]
