# Attention Mechanism

## Definition
Mecanismo que permite a cada token en una secuencia "mirar" todos los demás tokens y decidir dinámicamente qué información es más relevante. Permite que los modelos entiendan contexto relacional en lugar de leer secuencialmente.

## Why It Matters
Es la innovación clave que hace posible los modelos de IA modernos. Sin attention, los modelos no podrían resolver ambigüedad contextual ni capturar conexiones de largo alcance.

## Key Ideas
- No lee de izquierda a derecha: ve la oración completa y conecta puntos dinámicamente
- "Apple" presta alta atención a "bought" y "stock" → concluye compañía
- "apple" presta alta atención a "ate" → concluye fruta
- Antes de attention: modelos lentos que perdían conexiones de largo alcance
- Explica por qué prompts ambiguos producen outputs inconsistentes

## Related
- [[Transformer-Architecture]]
- [[Tokenization]]
- [[Context-Window]]

## Source
[[Sairahul1-10-AI-Concepts]]
