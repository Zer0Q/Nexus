---
title: "La ineficiencia oculta de JSON frente a la revolución de TOON"
source: "https://www.codemotion.com/magazine/es/inteligencia-artificial/la-ineficiencia-oculta-de-json-frente-a-la-revolucion-de-toon/"
author: "Orli Dun"
published: "2025-12-16"
type: article
---

# TOON Format

## Summary
TOON (Token-Oriented Object Notation) es un formato de serialización diseñado para LLMs que reduce tokens en 30-54% comparado con JSON. Elimina redundancia sintáctica (comillas, llaves, espacios) optimizando para tokenizadores BPE.

## Core Concepts
- [[TOON-Format]] -- notación compacta orientada a tokens para comunicación con LLMs
- [[Token-Efficiency]] -- optimización de uso de tokens en prompts y respuestas de IA

## Key Insights
- JSON consume 15-25% de tokens en sintaxis pura en prompts RAG promedio
- TOON elimina comillas en keys, usa delimitadores token-friendly (|) y compresión de arrays
- Reducción de ~40% en tokens se traduce en menor latencia, menor coste y más espacio en contexto
- Requiere capa de conversión en backend para compatibilidad con herramientas existentes
