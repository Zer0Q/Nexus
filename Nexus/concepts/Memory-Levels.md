# Memory Levels

## Definition
5 niveles de uso de memoria en agentes de IA: 1) fallar y documentarlo, 2) investigar por qué fallaste, 3) verificar la causa hasta convertirla en hecho, 4) destilar el hecho en regla general, 5) consultar la regla en vez de rederivarla cada vez.

## Why It Matters
La diferencia entre un agente que empieza de cero cada día y uno que acumula conocimiento. Modelos con mejor memory levels performance superan significativamente en benchmarks de continual learning.

## Key Ideas
- Nivel 1: Fallar y documentarlo (Sonnet 4.6 se queda aquí)
- Nivel 2: Investigar por qué fallaste
- Nivel 3: Verificar la causa hasta convertirla en hecho (Opus 4.7 llega aquí, verifica ~17%)
- Nivel 4: Destilar el hecho en regla general
- Nivel 5: Consultar regla en vez de rederivar (Fable 5 completa el ciclo, verifica 73%)
- "El modelo olvida entre sesiones. El archivo de memoria no."
- Diferencia entre agentes = memory levels, no intelligence

## Tradeoffs
- Más niveles = más overhead de memory management
- Memory persistence requiere storage y retrieval mechanism
- Reglas destiladas pueden ser outdated sin revalidación
- Balance entre memory usage y performance

## Related
- [[concepts/Fable-5]]
- [[concepts/Loop-Engineering]]
- [[concepts/Continual-Learning-Bench]]

## Source
[[summaries/angeldot-crear-loops-con-claude]]
