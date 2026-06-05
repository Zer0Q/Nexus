# MCP Server

## Definition
Servidor que expone capabilities (database queries, file access, API calls) a MCP clients a través del Model Context Protocol.

## Why It Matters
Permite a agents acceder a sistemas externos de forma estandarizada: Google Calendar, Notion, Figma, databases enterprise, Blender. Los servers ejecutan código real — deben tratarse como software a instalar, no como prompts inofensivos.

## Key Ideas
- Expone tools, data sources y workflows a MCP clients
- Ejemplos: GitHub MCP, database MCP, n8n MCP, browser MCP, internal API MCP
- El buen approach: pick one system que usas daily y exponer solo los tools que Hermes necesita
- No instalar cada server que ves — seleccionar selectivamente
- Soporte broad ecosystem: un server sirve a Claude, ChatGPT, VS Code, Cursor

## Related
- [[concepts/MCP]]
- [[concepts/MCP-Client]]
- [[tools/mcpvault]]

## Source
[[summaries/MCP-Team-What-is-the-Model-Context-Protocol]]
