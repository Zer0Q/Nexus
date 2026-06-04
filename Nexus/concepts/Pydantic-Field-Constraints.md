# Pydantic Field Constraints

## Definition
Field-level customization in Pydantic using the Field() function. Adds metadata, validation constraints, and serialization behavior to model fields beyond what type annotations provide.

## Why It Matters
Type annotations define the data type, but Field() adds the business rules: minimum lengths, patterns, ranges, aliases, defaults, and mutability. This is where schema definition meets domain logic.

## Key Ideas
- default / default_factory: callable for dynamic defaults (uuid4, lambda)
- frozen: immutable field after instantiation
- min_length / max_length: string/collection length constraints
- pattern: regex matching for strings
- alias: alternate name for input/output (camelCase API <-> snake_case internal)
- gt / ge / lt / le: numeric range constraints
- repr: include/exclude field in model representation
- description / examples: JSON Schema metadata
- Field works with Annotated types for composable constraints

## Tradeoffs
- Overusing Field() constraints instead of custom validators can make logic harder to test
- Aliases improve external compatibility but add cognitive overhead internally

## Related
- [[concepts/Pydantic-BaseModel]]
- [[concepts/Pydantic-Validators]]
- [[concepts/Pydantic-Field-Aliases]]

## Source
[[summaries/RealPython-Pydantic-Data-Validation]]
[[summaries/Torque-Pydantic-Data-Transformation]]
