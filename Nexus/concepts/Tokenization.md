# Tokenization

## Definition
Proceso por el cual el texto de entrada se divide en tokens — pequeños fragmentos de texto que son la unidad básica de procesamiento de los modelos de IA. Un token puede ser una palabra completa, parte de palabra o puntuación.

## Why It Matters
Todo en IA se preciosifica, limita y mide en tokens: coste de API, ventana de contexto, rate limits. Entender tokenización es prerequisite para cualquier trabajo con LLMs.

## Key Ideas
- "build" = 1 token, "building" = "build" + "ing" = 2 tokens
- Regla práctica: 1,000 tokens ≈ 750 palabras
- La tokenización afecta directamente el coste y la eficiencia de prompts
- Formatos como JSON consumen 15-25% de tokens en sintaxis pura
- TOON y otros formatos optimizados reducen tokens en 30-54%

## Related
- [[TOON-Format]]
- [[Context-Window]]
- [[Embeddings]]

## Source
[[Sairahul1-10-AI-Concepts]]
