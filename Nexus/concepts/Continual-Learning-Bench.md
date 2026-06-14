# Continual Learning Bench

## Definition
Benchmark de aprendizaje secuencial donde preguntas son secuenciales sobre base de datos SQL, cada pregunta es sesión nueva pero memoria se comparte. Mide capacidad de agente para acumular conocimiento entre sesiones.

## Why It Matters
Demuestra que el bottleneck de agents no es inteligencia sino memory persistence. Diferencias dramáticas entre modelos en uso de memoria: Sonnet 4.6 (0.364) vs Opus 4.7 (0.700) vs Fable 5 (0.839).

## Key Ideas
- Preguntas secuenciales sobre base de datos SQL
- Cada pregunta = sesión nueva pero memoria compartida
- Scores: Fable 5 0.839 vs Opus 4.7 0.700 vs Sonnet 4.6 0.364
- Diferencia = cómo usan memoria, no inteligencia
- Sonnet 4.6: nivel 1 (falla y documenta)
- Opus 4.7: nivel 3 (verifica causa hasta convertirla en hecho)
- Fable 5: nivel 5 (completo ciclo: verificar→destilar→consultar regla)
- "El modelo olvida entre sesiones. El archivo de memoria no."

## Tradeoffs
- Benchmark específico a SQL queries, no generalizable
- Depende de quality de memory persistence mechanism
- No mide performance en single-shot tasks
- Memory usage puede ser costoso en tokens

## Related
- [[concepts/Fable-5]]
- [[concepts/Memory-Levels]]
- [[concepts/Loop-Engineering]]

## Source
[[summaries/angeldot-crear-loops-con-claude]]
