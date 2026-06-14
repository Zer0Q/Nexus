# Fable 5

## Definition
Modelo de Anthropic optimizado para Loop Engineering: superó a Opus 4.7 ~6x en Parameter Golf (0.839 vs 0.700 en Continual Learning Bench). Diseñado para iterar autónomamente mediante loops verificables en vez de prompts secuenciales.

## Why It Matters
Demuestra que arquitectura de loop engineering supera a prompting secuencial. Fable 5 completa el ciclo de memoria (verifica 73% de diagnósticos y convierte en reglas) mientras Opus 4.7 se queda en nivel 3 y Sonnet 4.6 en nivel 1.

## Key Ideas
- Superó a Opus 4.7 6x en Parameter Golf (entrenar mejor modelo en 16MB en <10min sobre 8 GPUs H100)
- Continual Learning Bench: Fable 5 0.839 vs Opus 4.7 0.700 vs Sonnet 4.6 0.364
- Opus 4.7 repitió misma plantilla 20x tras pequeña mejora
- Fable 5 apostó por cambios estructurales grandes y aguantó regresión que fue su mayor victoria
- Los 5 niveles de memoria: fallar→investigar→verificar→destilar→consultar regla
- Sonnet 4.6: nivel 1 (apunta fallos), Opus 4.7: nivel 3 (crea referencias), Fable 5: nivel 5 (completo ciclo)
- "El modelo olvida entre sesiones. El archivo de memoria no."
- Verificador independiente no dejó parar a Fable 5 hasta cumplir 9 criterios de rúbrica

## Tradeoffs
- Fable 5 puede ser más lento por iteration en vez de single-shot
- Depende de buena memory persistence entre sesiones
- Requiere verificador independiente (cost computacional adicional)
- Optimizado para loop tasks, no necesariamente para chat/assistants

## Related
- [[concepts/Loop-Engineering]]
- [[concepts/Memory-Levels]]
- [[concepts/Maker-Checker-Split]]
- [[concepts/Parameter-Golf]]
- [[concepts/Continual-Learning-Bench]]

## Source
[[summaries/angeldot-crear-loops-con-claude]]
