---
type: Concept
title: Context Window
description: 'Límite fijo de texto que un modelo de IA puede "ver" en una sola solicitud.
  Incluye: system prompt, historial de conversación, documentos pasados, respuestas...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Context Window

## Definition
Límite fijo de texto que un modelo de IA puede "ver" en una sola solicitud. Incluye: system prompt, historial de conversación, documentos pasados, respuestas del modelo y mensaje actual.

## Why It Matters
La gestión de contexto es una de las habilidades más importantes en ingeniería de IA. Superar o malgestionar la ventana de contexto degrada la calidad de salida.

## Key Ideas
- Límites actuales: GPT-4o (128K), Claude 3.5 Sonnet (200K), Gemini 1.5 Pro (1M tokens)
- "Lost in the Middle": los modelos prestan más atención al inicio y final, ignorando el medio
- Poner instrucciones clave al top del system prompt y contexto clave antes de la pregunta del usuario
- No asumir que el modelo "vio" algo solo porque se incluyó
- Chunk y resumir documentos largos en lugar de dump completo

## Related
- [[concepts/Tokenization]]
- [[concepts/Attention-Mechanism]]
- [[concepts/RAG]]
- [[concepts/LLM-Hallucination]]

## Source
[[summaries/Sairahul1-10-AI-Concepts]]
