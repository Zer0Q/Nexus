# Transformer Architecture

## Definition
Arquitectura neural que corre bajo todos los modelos de IA modernos (GPT, Claude, Gemini, Llama, Mistral). Pipeline: texto → tokens → embeddings → capas de attention → predicción token por token. Cada Transformer Block contiene: LayerNorm → Masked Multi-Head Attention → Residual Connection → LayerNorm → FFN → Residual Connection.

## Why It Matters
Entender el pipeline transformer explica el comportamiento observable de los LLMs: por qué outputs largos tardan más, por qué son no-deterministas, y por qué cortar contexto rompe calidad.

## Key Ideas
- Predice un token a la vez, no oraciones completas
- Loop: predecir → añadir a secuencia → predecir siguiente → repetir
- Bilones de iteraciones por segundo producen el texto visible
- No-determinista por diseño: probabilidad en cada paso
- Tokens tempranos influyen en tokens posteriores
- GPT usa pre-norm design: LayerNorm ANTES de attention y FFN (mejor estabilidad)
- Multi-Head Attention: múltiples heads paralelos capturan patrones diferentes (significado, gramática, estructura)
- FFN expande dimensión hidden 4x con GELU, luego comprime de vuelta
- Residual connections: Output = x + Sublayer(x), preservan info original y estabilizan gradients
- Output layer (unembedding): proyecta último vector a logits (tamaño = vocabulario), softmax → probabilidad

## Related
- [[concepts/Attention-Mechanism]]
- [[concepts/Tokenization]]
- [[concepts/Embeddings]]
- [[concepts/Causal-Self-Attention]]
- [[concepts/Masked-Multi-Head-Attention]]
- [[concepts/Residual-Connections]]
- [[concepts/Layer-Normalization]]

## Source
[[summaries/Sairahul1-10-AI-Concepts]]
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-2]]
