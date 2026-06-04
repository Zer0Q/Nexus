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
- [[concepts/Pydantic]]
- [[concepts/PydanticAI]]
- [[concepts/BaseModel]]
- [[concepts/Field-Validator]]
- [[concepts/Model-Validator]]
- [[concepts/Field-Alias]]
- [[concepts/Data-Class]]
- [[concepts/JSON-Schema]]
- [[concepts/Type-Coercion]]
- [[concepts/Settings-Management]]
- [[concepts/Validate-Call]]

## Sources
- [[summaries/Pydantic-Team-Pydantic-Models]]
- [[summaries/Pydantic-Team-Pydantic-Validators]]
- [[summaries/Pydantic-Team-Pydantic-AI-Overview]]
- [[summaries/RealPython-Pydantic-Data-Validation]]
- [[summaries/Torque-Pydantic-Data-Transformation]]
- [[summaries/KusCamara-PydanticAI-Agent-Creation]]
