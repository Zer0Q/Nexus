# Masked Multi-Head Attention

## Definition
Mecanismo donde múltiples "heads" de causal self-attention corren en paralelo sobre los mismos input embeddings, cada uno capturando patrones diferentes (significado, gramática, estructura). Los outputs se concatenan y pasan por una capa lineal final para producir una representación unificada.

## Why It Matters
Un solo head de atención tiene capacidad limitada para capturar las múltiples relaciones presentes en el lenguaje. Multi-head permite aprender simultáneamente dependencias gramaticales, semánticas y estructurales.

## Key Ideas
- Step 1: dividir embeddings en partes más pequeñas (heads)
- Step 2: cada head ejecuta attention independentemente sobre sus propias dimensiones
- Step 3: concatenar outputs de todos los heads
- Step 4: capa lineal final combina la información diversa en una representación unificada
- Ejemplo: Head 1 conecta "moment" ↔ "beginning" (significado), Head 2 conecta "Every" → "moment" (gramática), Head 3 conecta "is" → "beginning" (estructura)
- Cada head usa causal masking para mantener la restricción autoregresiva

## Related
- [[concepts/Attention-Mechanism]]
- [[concepts/Causal-Self-Attention]]
- [[concepts/Transformer-Architecture]]

## Source
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-2]]
