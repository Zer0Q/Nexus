---
type: Concept
title: Pydantic Field Aliases
description: Mapping between internal field names and external data keys using Field(alias='externalName').
  Enables seamless integration with APIs and databases using dif...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Pydantic Field Aliases

## Definition
Mapping between internal field names and external data keys using Field(alias='externalName'). Enables seamless integration with APIs and databases using different naming conventions (camelCase, PascalCase, SCREAMING_SNAKE_CASE).

## Why It Matters
External systems rarely use the same naming conventions as your codebase. Aliases bridge the gap without renaming internal fields or writing manual transformation code.

## Key Ideas
- alias parameter: Field(..., alias='camelCaseName')
- allow_population_by_field_name: accept both field name and alias
- alias_generator: function applied to all fields (e.g., lambda x: x.upper())
- by_alias=True in model_dump() serializes using aliases
- Popularity in API integration: camelCase JSON <-> snake_case Python

## Tradeoffs
- Aliases add cognitive overhead -- readers must know both names
- Overusing aliases internally defeats their purpose (external compatibility only)

## Related
- [[concepts/Pydantic-Field-Constraints]]
- [[concepts/Pydantic-Model-Config]]

## Source
[[summaries/Torque-Pydantic-Data-Transformation]]
[[summaries/RealPython-Pydantic-Data-Validation]]
