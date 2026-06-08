# Residual Connections

## Definition
Conexiones de salto (skip connections) que suman el input original a la salida de una subcapa: Output = x + Sublayer(x). En lugar de aprender una representación completamente nueva, la capa aprende un update residual.

## Why It Matters
Resuelven el problema de vanishing/exploding gradients en redes profundas. Cuando los gradients se desvanecen durante backpropagation, las capas tempranas aprenden muy lentamente porque la señal de training se desvanece. Los residual connections preservan la señal original a través de las capas.

## Key Ideas
- Formula: Output = x + Sublayer(x) donde Sublayer puede ser attention o FFN
- Se aplican tanto después de Masked Multi-Head Attention como después de FFN
- Permiten entrenar redes más profundas (GPT apila muchos transformer blocks)
- Preservan información de palabras originales a través de múltiples capas
- Estabilizan gradients durante backpropagation

## Related
- [[concepts/Transformer-Architecture]]
- [[concepts/Layer-Normalization]]

## Source
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-2]]
