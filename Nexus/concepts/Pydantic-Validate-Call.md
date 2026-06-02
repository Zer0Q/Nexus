# Pydantic @validate_call

## Definition
Decorator that applies Pydantic validation to regular Python function arguments. Type annotations on parameters become validation rules, eliminating manual input checking boilerplate.

## Why It Matters
Functions outside of models still need input validation. @validate_call brings Pydantic's validation to any function without wrapping it in a model.

## Key Ideas
- @validate_call on function validates all arguments against type annotations
- Supports Field constraints via Annotated: Annotated[str, Field(min_length=1)]
- Coerces types same as BaseModel (str '123' -> int 123)
- ValidationError raised with per-argument error details
- Works with async functions
- Less flexible than BaseModel (no model-wide config, no nested model validation)

## Tradeoffs
- Cannot use model_validate() methods
- No model-wide configuration options
- Best for simple argument validation, not complex schemas

## Related
- [[concepts/Pydantic-Validation]]
- [[concepts/Pydantic-Field-Constraints]]

## Source
[[source-notes/RealPython-Pydantic-Data-Validation]]
