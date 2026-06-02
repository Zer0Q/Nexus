# Pydantic & Data Validation Index

## Overview
Pydantic ecosystem: data validation, serialization, settings management, and agent framework. Core of FastAPI, LangChain, OpenAI SDK, and many Python frameworks.

## Core Concepts
- [[concepts/Pydantic-Validation]] -- type-based data validation with minimal boilerplate
- [[concepts/Pydantic-BaseModel]] -- schema definition via class inheritance
- [[concepts/Pydantic-Field-Constraints]] -- Field() for min/max, pattern, description
- [[concepts/Pydantic-Validators]] -- custom validation: field, model, before, after, wrap, plain
- [[concepts/Pydantic-Data-Conversion]] -- automatic type coercion (str→int, etc.)
- [[concepts/Pydantic-Nested-Models]] -- nested BaseModel for complex structures
- [[concepts/Pydantic-JSON-Schema]] -- automatic JSON Schema generation from models
- [[concepts/Pydantic-Field-Aliases]] -- map model fields to different input keys
- [[concepts/Pydantic-Model-Config]] -- model-level settings (extra, strict, populate_by_name)
- [[concepts/Pydantic-Validate-Call]] -- validate function arguments with @validate_call
- [[concepts/Pydantic-Settings]] -- app config from env vars, .env files, defaults
- [[concepts/Pydantic-Validation-Context]] -- pass context to validators

## Agent Framework
- [[tools/PydanticAI]] -- Python agent framework, type-safe, model-agnostic
- [[concepts/Agent-Dependency-Injection]] -- type-safe runtime data into agent tools
- [[concepts/Agent-Structured-Output]] -- constrain LLM responses to Pydantic schemas
- [[concepts/Durable-Agent-Execution]] -- preserve agent progress across failures
- [[concepts/Agent-Graph-Support]] -- type-hinted graph definitions for workflows

## Glossary
- [[glossary/Pydantic]]
- [[glossary/PydanticAI]]
- [[glossary/BaseModel]]
- [[glossary/Field-Validator]]
- [[glossary/Model-Validator]]
- [[glossary/Field-Alias]]
- [[glossary/Data-Class]]
- [[glossary/JSON-Schema]]
- [[glossary/Type-Coercion]]
- [[glossary/Settings-Management]]
- [[glossary/Validate-Call]]

## Sources
- [[source-notes/Pydantic-Team-Pydantic-Models]]
- [[source-notes/Pydantic-Team-Pydantic-Validators]]
- [[source-notes/Pydantic-Team-Pydantic-AI-Overview]]
- [[source-notes/RealPython-Pydantic-Data-Validation]]
- [[source-notes/Torque-Pydantic-Data-Transformation]]
- [[source-notes/KusCamara-PydanticAI-Agent-Creation]]
