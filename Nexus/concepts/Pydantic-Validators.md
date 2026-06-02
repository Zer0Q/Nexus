# Pydantic Validators

## Definition
Custom validation logic in Pydantic at field and model levels. Four field validator types (after, before, plain, wrap) and three model validator types (after, before, wrap). Defined via Annotated pattern (reusable) or decorator pattern (multi-field).

## Why It Matters
Built-in type validation covers basic cases, but real-world data needs custom rules: cross-field checks, business logic, data transformation, and conditional validation. Validators bridge the gap between type safety and domain constraints.

## Key Ideas
- After validators: run after internal validation, type-safe, easiest to implement
- Before validators: run before parsing, handle raw Any input, ideal for data transformation
- Plain validators: replace all validation, bypass Pydantic internal checks
- Wrap validators: most flexible, control before/after internal validation, can short-circuit
- Annotated pattern: reusable type aliases (EvenNumber = Annotated[int, AfterValidator(is_even)])
- Decorator pattern: @field_validator('f1', 'f2') applies to multiple fields
- Model validators: @model_validator(mode='after') for instance-level checks
- ValidationInfo: access to already-validated data, user context, validation mode, field name
- Validation ordering: before/wrap right-to-left, after left-to-right in Annotated stack
- Raise ValueError, AssertionError, or PydanticCustomError for custom error types

## Tradeoffs
- Root/model validators are less performant than field validators
- Before validators must handle Any type -- more error-prone
- Plain validators bypass type checking -- use only when you fully control validation

## Related
- [[concepts/Pydantic-BaseModel]]
- [[concepts/Pydantic-Field-Constraints]]
- [[concepts/Pydantic-Validation-Context]]
- [[concepts/Pydantic-Data-Conversion]]

## Source
[[source-notes/Pydantic-Team-Pydantic-Validators]]
[[source-notes/Torque-Pydantic-Data-Transformation]]
