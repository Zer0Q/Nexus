---
title: "What is the Model Context Protocol (MCP)?"
source: "https://modelcontextprotocol.io/docs/getting-started/intro"
author: "MCP Team"
published: "2026"
type: article
---

# What is the Model Context Protocol (MCP)

## Summary
MCP es un estándar open-source para conectar aplicaciones AI a sistemas externos, análogo a un puerto USB-C para AI. Permite que agentes accedan a data sources (files locales, databases), tools (search engines, calculators) y workflows (prompts especializados). Soporte amplio: Claude, ChatGPT, VS Code, Cursor, MCPJam. Beneficios: reduced development complexity para devs, ecosystem access para AI apps, agents más capaces para end-users.

## Core Concepts
- [[concepts/MCP]] -- protocolo open-source estandarizado para conectar aplicaciones AI a data sources, tools y workflows externos
- [[concepts/MCP-Client]] -- aplicación AI (Claude, ChatGPT, VS Code) que consume tools y data de MCP servers
- [[concepts/MCP-Server]] -- servidor que expone capabilities (database queries, file access, API calls) a MCP clients
- [[concepts/Agent-Tool-Use]] -- capacidad de agentes para interactuar con servicios externos de forma estandarizada vía MCP

## Key Insights
- La analogía USB-C: así como USB-C estandariza la conexión de dispositivos electrónicos, MCP estandariza la conexión de AI apps a sistemas externos
- Casos de uso: agentes accediendo Google Calendar y Notion, Claude Code generando web apps desde diseños Figma, chatbots enterprise conectando múltiples databases, AI models creando 3D en Blender e imprimiendo
- Para developers: reduce tiempo y complejidad al construir o integrar con AI applications
- Para AI applications: acceso a ecosistema de data sources, tools y apps que mejoran capabilities y UX
- Para end-users: aplicaciones AI más capaces que acceden a sus datos y toman acciones en su nombre
- Soporte broad ecosystem: Claude, ChatGPT, VS Code, Cursor, MCPJam — build once, integrate everywhere

## Open Questions
- ¿Cómo manejar security y permissions en MCP cuando un server expone acceso a datos sensibles de múltiples organizations?
- ¿Qué overhead de latencia introduce la capa MCP comparado con llamadas API directas?

## Source
- **Raw note:** [[raw-notes/what-is-the-model-context-protocol-mcp]]
- **Original URL:** https://modelcontextprotocol.io/docs/getting-started/intro
