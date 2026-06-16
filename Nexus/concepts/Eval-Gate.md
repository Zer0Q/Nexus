# Eval Gate

## Definition
Punto en un loop de agente donde se evalúa si el resultado actual es suficiente para continuar iterando o para detenerse. Es la lógica de decisión que determina cuándo el loop debe terminar y cuándo necesita más iteraciones.

## Why It Matters
Sin eval gate, los loops pueden entrar en ciclos infinitos o detenerse prematuramente. El eval gate es lo que hace que un loop sea inteligente y eficiente.

## Key Ideas
- Evalúa si el resultado es "good enough" para continuar o parar
- Parte crítica de cualquier loop: trigger → signal → action → eval gate → stop condition
- Puede ser determinista (reglas fijas) o basado en LLM (el modelo evalúa su propio output)
- El eval gate + stop condition trabajan juntos para controlar la autonomía del loop
- Un eval gate mal diseñado causa loops infinitos o resultados incompletos

## Tradeoffs
- Eval gates basados en LLM son más flexibles pero más costosos
- Eval gates deterministas son más rápidos pero menos adaptativos
- El balance depende del tipo de tarea y el costo de errores

## Related
- [[concepts/Agent-Loop]]
- [[concepts/Stop-Condition]]
- [[concepts/Agent-Guardrails]]
- [[concepts/Evidence-Validation]]

## Source
[[summaries/Ericosiu-Revenue-Engineering-Loops]]
[[summaries/Revenue-Engineering]]
