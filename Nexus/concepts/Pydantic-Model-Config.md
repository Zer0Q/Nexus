# Pydantic Model Config

## Definition
Model-wide configuration via ConfigDict (V2) or Config class (V1). Controls validation behavior, serialization, extra field handling, and naming conventions.

## Why It Matters
Some settings apply globally to a model rather than per-field. ConfigDict centralizes these decisions: should extra data be rejected? Should models be immutable? How should aliases be generated?

## Key Ideas
- extra: 'ignore' (default), 'forbid' (reject unknown), 'allow' (store in __pydantic_extra__)
- frozen: make entire model immutable
- strict: enforce exact types, no coercion
- validate_assignment: re-validate on field modification
- str_strip_whitespace: auto-trim strings
- from_attributes: enable ORM mode (read object attributes)
- alias_generator: auto-generate aliases for all fields
- revalidate_instances: 'always', 'subclass-instances', 'never'
- SettingsConfigDict (pydantic-settings): env_file, env_file_encoding, case_sensitive

## Tradeoffs
- frozen models require model_copy() for updates
- strict mode increases validation failures from type mismatches
- validate_assignment adds runtime overhead to every field change

## Related
- [[concepts/Pydantic-BaseModel]]
- [[concepts/Pydantic-Field-Aliases]]
- [[concepts/Pydantic-Settings]]

## Source
[[source-notes/Torque-Pydantic-Data-Transformation]]
