---
title: Validators
author: Pydantic Team
published: ''
type: article
resource: https://pydantic.dev/docs/validation/latest/concepts/validators/
timestamp: ''
description: Official Pydantic documentation on custom validators. Covers four field
  validator types (after, before, plain, wrap) via both Annotated pattern and decorator...
tags:
- summaries
---


# Pydantic Validators Documentation

## Summary
Official Pydantic documentation on custom validators. Covers four field validator types (after, before, plain, wrap) via both Annotated pattern and decorator. Three model validator types (after, before, wrap). Validation info/context, error handling, and validator ordering.

## Core Concepts
- [[concepts/Pydantic-Validators]] -- Custom validation at field and model levels
- [[concepts/Pydantic-Validation-Context]] -- Passing runtime context to validators via ValidationInfo
- [[concepts/Pydantic-Field-Constraints]] -- Built-in constraints vs custom validators
- [[concepts/Pydantic-Data-Conversion]] -- Before validators for coercion, after for type-safe checks

## Key Insights
- After validators: run after internal validation, type-safe, easier to implement
- Before validators: run before parsing, handle raw input (Any type), more flexible
- Plain validators: terminate validation immediately, bypass Pydantic internal checks
- Wrap validators: most flexible, can run code before/after internal validation, or short-circuit
- Annotated pattern: reusable validators across models (type alias)
- Decorator pattern: apply to multiple fields with @field_validator('f1', 'f2')
- Model validators: after (instance method), before (classmethod, raw data), wrap (classmethod + handler)
- Validation ordering: before/wrap right-to-left, after left-to-right
- ValidationInfo provides: data (already validated fields), context (user-defined), mode, field_name
- PydanticCustomError for custom error types with formatted messages
- InstanceOf for runtime type checking, SkipValidation for performance bypass

## Open Questions
- None

## Source

- **Raw note:** [[pydantic-docs-validators.md]]
- **Original URL:** https://pydantic.dev/docs/validation/latest/concepts/validators/
