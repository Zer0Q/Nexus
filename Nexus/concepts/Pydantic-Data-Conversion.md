# Pydantic Data Conversion

## Definition
Pydantic's automatic type coercion system converts input data to match declared field types. String '123' becomes int 123, float 3.0 becomes int 3, bytes become strings. Controlled by strict mode and validator timing.

## Why It Matters
Data from external sources (APIs, user input, databases) rarely matches exact types. Pydantic's coercion handles the conversion automatically, reducing boilerplate. Strict mode provides an escape hatch when exact types are required.

## Key Ideas
- Default mode: permissive coercion (str->int, float->int, bytes->str, tuple->list)
- Strict mode: exact type matching, no coercion
- Per-field strict via Field(strict=True) or model-wide ConfigDict(strict=True)
- Before validators run before coercion (raw input)
- After validators run after coercion (validated type)
- model_validate_strings() validates string dicts in JSON mode with coercion
- Abstract container types (Sequence, Mapping) cause performance penalties vs concrete types

## Tradeoffs
- Coercion loses information (3.9 -> 3 when target is int)
- Strict mode rejects valid-but-different-type input
- Concrete types (list) outperform abstract types (Sequence) in validation speed

## Related
- [[concepts/Pydantic-Validation]]
- [[concepts/Pydantic-Validators]]
- [[concepts/Pydantic-BaseModel]]

## Source
[[summaries/Pydantic-Team-Pydantic-Models]]
[[summaries/Torque-Pydantic-Data-Transformation]]
