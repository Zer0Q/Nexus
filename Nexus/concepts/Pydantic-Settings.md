---
type: Concept
title: Pydantic Settings
description: pydantic-settings package for managing application configuration through
  environment variables. BaseSettings reads from env vars, .env files, and secrets,
  va...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Pydantic Settings

## Definition
pydantic-settings package for managing application configuration through environment variables. BaseSettings reads from env vars, .env files, and secrets, validating them against Pydantic models.

## Why It Matters
Application configuration (DB credentials, API keys, feature flags) lives in environment variables. BaseSettings validates these at startup, catching misconfiguration before runtime.

## Key Ideas
- BaseSettings inherits from BaseModel, reads missing fields from environment variables
- Case-insensitive env var matching by default (DATABASE_HOST matches database_host)
- SettingsConfigDict: env_file, env_file_encoding, case_sensitive, extra
- .env file loading with dotenv integration
- Same validation as BaseModel: types, Field constraints, validators
- SecretStr type for sensitive values (hidden in repr)
- Used by FastAPI for configuration management

## Tradeoffs
- Separate package (pydantic-settings) not included in base pydantic
- Env var matching can be surprising (case-insensitive by default)

## Related
- [[concepts/Pydantic-Model-Config]]
- [[concepts/Pydantic-BaseModel]]

## Source
[[summaries/RealPython-Pydantic-Data-Validation]]
