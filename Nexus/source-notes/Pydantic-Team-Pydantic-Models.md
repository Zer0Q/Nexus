---
title: "Models"
source: "https://pydantic.dev/docs/validation/latest/concepts/models/"
author: "Pydantic Team"
published: ""
type: article
---

# Pydantic Models Documentation

## Summary
Official Pydantic documentation on BaseModel, the primary way of defining data schemas. Covers model instantiation, validation modes, serialization, nested models, schema rebuild, data conversion, extra data handling, and ORM integration.

## Core Concepts
- [[concepts/Pydantic-Validation]] -- Data validation library using Python type hints
- [[concepts/Pydantic-BaseModel]] -- Core class for defining data schemas with automatic validation
- [[concepts/Pydantic-Field-Constraints]] -- Field-level customization with Field() for metadata and constraints
- [[concepts/Pydantic-Validators]] -- Custom validation at field and model levels
- [[concepts/Pydantic-Data-Conversion]] -- Automatic type coercion vs strict mode
- [[concepts/Pydantic-Nested-Models]] -- Hierarchical data structures using models as field types
- [[concepts/Pydantic-JSON-Schema]] -- Automatic JSON Schema generation from models

## Key Insights
- model_validate() vs __init__: validate() supports dicts, JSON, and arbitrary objects; __init__ only takes kwargs
- model_construct() bypasses validation entirely -- useful for performance with known-valid data
- model_rebuild() needed for forward references and recursive models
- Three validation modes: Python, JSON, strings (model_validate_strings for string-to-type coercion)
- Extra data handling: ignore (default), forbid, allow
- from_attributes=True enables ORM integration (reads object attributes as fields)
- model_copy() allows duplicating models with optional field updates, essential for frozen models

## Open Questions
- How does Pydantic V2 model_rebuild() differ from V1 update_forward_refs() in edge cases?
