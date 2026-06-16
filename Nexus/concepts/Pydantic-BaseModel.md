---
type: Concept
title: Pydantic BaseModel
description: Core class in Pydantic for defining data schemas. Subclasses declare
  fields as type-annotated attributes; Pydantic generates validation logic, serialization
  ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Pydantic BaseModel

## Definition
Core class in Pydantic for defining data schemas. Subclasses declare fields as type-annotated attributes; Pydantic generates validation logic, serialization methods, and JSON Schema automatically. Similar to Python dataclasses but focused on validation and serialization.

## Why It Matters
BaseModel is the primary abstraction for structured data in Pydantic. Every validation, serialization, and schema generation feature flows through it. It replaces manual input checking with declarative type annotations.

## Key Ideas
- Fields defined as type-annotated class attributes (id: int, name: str = 'default')
- Constructor (__init__) validates kwargs; model_validate() accepts dicts/objects
- model_construct() bypasses validation for known-valid data (performance)
- model_copy() duplicates with optional field updates (essential for frozen models)
- model_rebuild() resolves forward references and recursive types
- model_fields: mapping of field names to FieldInfo definitions
- model_computed_fields: mapping of @computed_field definitions
- model_fields_set: set of explicitly provided field names
- model_extra: dict of extra fields when extra='allow'
- Custom __init__ possible but not recommended (loses validation parameters)
- model_post_init() hook runs after validation for side effects

## Tradeoffs
- model_construct() skips validation -- caller must guarantee data integrity
- Custom __init__ loses strictness/extra/context control from model_validate()
- Nested models require model_rebuild() for forward references

## Related
- [[concepts/Pydantic-Validation]]
- [[concepts/Pydantic-Field-Constraints]]
- [[concepts/Pydantic-Nested-Models]]
- [[concepts/Pydantic-JSON-Schema]]

## Source
[[summaries/Pydantic-Team-Pydantic-Models]]
