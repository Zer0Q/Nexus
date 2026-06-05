# Transformer Architecture

## Definition
Arquitectura neural que corre bajo todos los modelos de IA modernos (GPT, Claude, Gemini, Llama, Mistral). Pipeline: texto → tokens → embeddings → capas de attention → predicción token por token.

## Why It Matters
Entender el pipeline transformer explica el comportamiento observable de los LLMs: por qué outputs largos tardan más, por qué son no-deterministas, y por qué cortar contexto rompe calidad.

## Key Ideas
- Predice un token a la vez, no oraciones completas
- Loop: predecir → añadir a secuencia → predecir siguiente → repetir
- Bilones de iteraciones por segundo producen el texto visible
- No-determinista por diseño: probabilidad en cada paso
- Tokens tempranos influyen en tokens posteriores

## Related
- [[concepts/Attention-Mechanism]]
- [[concepts/Tokenization]]
- [[concepts/Embeddings]]

## Source
[[summaries/Sairahul1-10-AI-Concepts]]
