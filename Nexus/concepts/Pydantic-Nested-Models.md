# Pydantic Nested Models

## Definition
Using Pydantic models as field types to create hierarchical data structures. Models can reference other models, lists of models, or themselves (recursive models) via forward references.

## Why It Matters
Real-world data is rarely flat. APIs return nested JSON, configurations have hierarchical sections, and domain models have relationships. Nested models validate the entire tree automatically.

## Key Ideas
- Model fields can be other model types: foo: Foo, bars: list[Bar]
- model_dump() recursively serializes nested models to dicts
- Forward references: use string annotations ('Bar') when type is not yet defined
- model_rebuild() resolves forward references after all types are defined
- Self-referencing models: Node(children: list['Node']) for trees/graphs
- Nested validation: errors include path to nested field (bars.1.apple)
- from_attributes=True propagates to nested models for ORM integration

## Tradeoffs
- Forward references require model_rebuild() -- timing matters
- Deep nesting increases validation time
- Recursive models need careful schema generation

## Related
- [[concepts/Pydantic-BaseModel]]
- [[concepts/Pydantic-JSON-Schema]]

## Source
[[summaries/Pydantic-Team-Pydantic-Models]]
