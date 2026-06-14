# Parameter Golf

## Definition
Benchmark de Anthropic: entrenar el mejor modelo posible que quepa en 16MB, en menos de 10 minutos, sobre 8 GPUs H100. El agent tiene que editar código de entrenamiento, lanzar training, leer logs, ver score y decidir siguiente experimento.

## Why It Matters
Demuestra la diferencia entre prompting secuencial y loop engineering. Opus 4.7 encontró pequeña mejora y repitió misma plantilla 20x. Fable 5 apostó por cambios estructurales grandes y aguantó regresión que fue su mayor victoria.

## Key Ideas
- Constraint: 16MB model size, <10 minutes, 8 GPUs H100
- Agent: edit training code → run training → read logs → see score → decide next experiment
- Runs for 8 hours autonomously
- Opus 4.7: tocar un parámetro, medir, quedarse con lo que sume (20x plantilla)
- Fable 5: cambios estructurales (arquitectura, no constantes), aguantó regresión
- Fable 5 mejoró ~6x más que Opus 4.7
- Verificador independiente: 9 criterios de rúbrica que debían cumplirse

## Tradeoffs
- Benchmark específico: no generalizable a todos los tipos de model training
- Hardware requirement: 8 GPUs H100 para el benchmark
- Time constraint (10min) puede no representar training real
- Score metric puede no capturar todas las dimensiones de calidad

## Related
- [[concepts/Fable-5]]
- [[concepts/Loop-Engineering]]
- [[concepts/Maker-Checker-Split]]

## Source
[[summaries/angeldot-crear-loops-con-claude]]
