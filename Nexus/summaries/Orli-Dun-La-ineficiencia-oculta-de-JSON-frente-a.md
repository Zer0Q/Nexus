---
title: "La ineficiencia oculta de JSON frente a la revolución de TOON"
source: "https://www.codemotion.com/magazine/es/inteligencia-artificial/la-ineficiencia-oculta-de-json-frente-a-la-revolucion-de-toon/"
author: "Orli Dun"
published: "2025-12-16"
type: article
---

# TOON vs JSON: Reduciendo tokens en comunicación con LLMs

## Summary
Análisis de la ineficiencia de JSON como formato de serialización para LLMs: consume 15-25% de tokens en sintaxis pura (comillas, llaves, espacios, claves repetidas). TOON (Token-Oriented Object Notation) propone un formato compacto alineado con cómo los tokenizadores BPE agrupan palabras, logrando reducciones de 30-54% en tokens. El artículo presenta ejemplos prácticos, impacto en costes y latencia, y una guía para adoptar TOON en pipelines de IA existentes.

## Core Concepts

- [[tools/TOON-Format]] -- Formato de serialización compacto para LLMs que reduce tokens 30-54% vs JSON
- [[concepts/Tokenization]] -- Unidad básica de entrada/salida de modelos de IA; JSON desperdicia tokens en sintaxis
- [[concepts/Context-Window]] -- Ventana de contexto limitada; TOON libera espacio reduciendo overhead de serialización
- [[concepts/Context-Efficiency-Frontier]] -- Optimización del uso de tokens para maximizar información útil en la ventana de contexto

## Key Insights

- JSON consume 15-25% de tokens en sintaxis pura: comillas, llaves, espacios, claves repetidas
- TOON elimina comillas en keys y usa delimitadores token-friendly (`|`) alineados con tokenizadores BPE
- Ejemplo práctico: objeto JSON de ~55 tokens se reduce a ~25 tokens en TOON (54% de reducción)
- Menos tokens de salida significa menor latencia de inferencia y costes reducidos
- La compresión de arrays con definiciones de esquema implícitas amplía las ganancias en estructuras repetitivas
- Requiere capa de conversión en backend para compatibilidad con sistemas existentes
- SDK oficial `toon-parser` disponible para Python y Node.js
- A/B testing obligatorio: la compresión puede cambiar cómo el LLM interpreta contexto en casos edge

## Open Questions

- ¿Qué overhead de conversión introduce la capa TOON↔JSON en pipelines existentes?
- ¿Cómo afecta TOON a la capacidad de los LLMs para mantener consistencia estructural en respuestas complejas?

## Source

- **Raw Note**: [[JSON-vs-TOON]]
- **Original URL:** https://www.codemotion.com/magazine/es/inteligencia-artificial/la-ineficiencia-oculta-de-json-frente-a-la-revolucion-de-toon/
