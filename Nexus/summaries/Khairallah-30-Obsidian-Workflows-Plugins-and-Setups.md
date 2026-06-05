---
title: "30 Obsidian Workflows, Plugins, and Setups That Most Users Don't Know"
source: "https://x.com/eng_khairallah1/status/2061012675824644161"
author: "@eng_khairallah1"
published: "2026-05-31"
type: article
---

# 30 Obsidian Workflows, Plugins, and Setups

## Summary
Catálogo de 30 elementos para convertir Obsidian + Claude en un sistema de conocimiento personal potente: 10 plugins esenciales (Smart Connections, Templater, Dataview, Tasks, Git, Calendar, Kanban, Periodic Notes, CLI), 10 workflows automatizados (Morning Synthesis, Meeting Processor, Research Ingestion, Weekly Review, etc.) y 10 setups avanzados (mcpvault MCP server, Multi-Vault Strategy, Claude Code Routines, Zettelkasten + AI). El stack diario del autor usa solo 6 plugins, 1 MCP server y 2 automatizaciones.

## Core Concepts
- [[tools/Smart-Connections-Plugin]] -- plugin AI más popular para Obsidian, usa RAG para chatear con todo el vault
- [[Dataview]] -- needs research: plugin de Obsidian para queries estructuradas -- convierte el vault en base de datos consultable con queries estructuradas
- [[Templater]] -- needs research: plugin de Obsidian para plantillas automatizadas -- plantillas automatizadas que disparan al crear notas específicas, asegurando consistencia
- [[Periodic-Notes]] -- needs research: plugin de Obsidian para notas periódicas -- automatiza creación de notas diarias/semanales/mensuales con plantillas
- [[Obsidian-CLI]] -- needs research: interfaz CLI para Obsidian (2026) -- interfaz de línea de comandos para Obsidian (2026), permite interacción programática con el vault
- [[tools/mcpvault]] -- MCP server sin dependencias para leer vaults con búsqueda BM25, 14 métodos MCP
- [[tools/Obsidian-Skills-Plugin]] -- skills oficiales de Obsidian creados por el CEO, 12,900+ stars en GitHub
- [[concepts/Feedback-Loop-Knowledge-System]] -- guardar outputs de Claude de vuelta en el vault con tag #ai-generated para compounding de conocimiento
- [[Multi-Vault-Strategy]] -- needs research: estrategia de vaults separados por contexto -- vaults separados por contexto (personal, trabajo, aprendizaje) para evitar bleed entre dominios
- [[Morning-Synthesis-Workflow]] -- needs research: workflow de síntesis matutina con Claude -- Claude lee notas de los últimos 3 días + proyectos activos, crea nota "Start of Day" con prioridades

## Key Insights
- Obsidian tiene 2,700+ plugins comunitarios, más de 100 relacionados con AI
- El CEO de Obsidian publicó oficialmente Claude Skills para la plataforma con 12,900+ GitHub stars en menos de 3 meses
- El stack diario del autor: Smart Connections, Templater, Dataview, Periodic Notes, Tasks + mcpvault MCP + nightly routine + weekly review
- La ruta de setup para principiantes: Hour 1 (Obsidian + Templater), Hour 2 (Smart Connections), Hour 3 (MCP server), Day 2 (10 notas con frontmatter), Day 3 (Morning Synthesis), Week 1-2 (Periodic Notes + Dataview)
- El "Idea Cross-Pollinator" busca conexiones no-obvias entre notas, donde viven los mejores insights
- El "Vault Health Check" mensual encuentra orphans, info desactualizada, proyectos estancados y tags inconsistentes
- El "Decision Journal" permite a Claude analizar patrones de decisión: qué tipos aciertas, dónde aparecen sesgos
- El "Feedback Loop System" hace que el vault contenga tanto tu pensamiento original como la síntesis de Claude, compounding exponencial

## Open Questions
- ¿Cómo manejar la escalabilidad del vault cuando crece a 2,000+ notas — sigue siendo viable el RAG local?
- ¿Cuál es el overhead real de mantener 6 plugins + MCP server + 2 automatizaciones en términos de tiempo de mantenimiento semanal?

## Source
- **Raw note:** [[raw-notes/30-obsidian-workflows-plugins-and-setups-that-most-users-dont-kn]]
- **Original URL:** https://x.com/eng_khairallah1/status/2061012675824644161
