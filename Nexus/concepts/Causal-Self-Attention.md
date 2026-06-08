# Causal Self Attention

## Definition
Variante de self-attention donde cada token solo puede atender a sí mismo y a tokens anteriores en la secuencia, nunca a tokens futuros. Se implementa con una máscara triangular inferior que reemplaza los scores de posiciones bloqueadas con -inf antes del softmax, resultando en probabilidad 0.

## Why It Matters
Es esencial para generación de texto autoregresiva: sin causal masking, el modelo "vería" los tokens que está intentando predecir, colapsando la distribución de probabilidad a picos triviales. Es lo que diferencia modelos generativos (GPT) de modelos bidireccionales (BERT).

## Key Ideas
- Matriz de máscara: triangular inferior donde 1 = atención permitida, 0 = bloqueada
- Implementación: reemplazar scores con -inf antes de softmax → probabilidad = 0
- Token 1 solo ve sí mismo, Token 2 ve tokens 1 y 2, Token N ve tokens 1..N
- Contraste con self-attention estándar donde cada token ve todos los tokens
- Dropout se aplica después de attention durante training para reducir overfitting

## Related
- [[concepts/Attention-Mechanism]]
- [[concepts/Masked-Multi-Head-Attention]]
- [[concepts/Transformer-Architecture]]

## Source
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-2]]
