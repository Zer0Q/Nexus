# Skill Files

## Definition
Documentos markdown reutilizables que enseñan al modelo CÓMO hacer algo, no QUÉ hacer. Funcionan como una "method call": toman parámetros y producen resultados diferentes según la invocación, pero el proceso es siempre el mismo.

## Why It Matters
Resuelven 3 problemas: consistencia (mismo resultado cada vez), calidad (revisar en el orden correcto), y eficiencia (no repetir contexto). La ventaja real es dejar de repetirse — las instrucciones se escriben una vez y se aplican siempre.

## Key Ideas
- SKILL.md tiene 2 partes: descripción (qué hace) y contexto (instrucciones detalladas)
- Una skill funciona como un método: misma procedura + diferentes parámetros = diferentes resultados
- Markdown es más perfecto que código rígido para describir proceso y judgment
- Se activan on-demand, no están siempre activas (a diferencia de CLAUDE.md)
- Se pueden empaquetar como plugins para distribución en equipo

## Tradeoffs
- Crear skills tiene costo de mantenimiento
- Demasiadas skills pueden degradar performance
- Skills muy específicas pueden no generalizar bien

## Related
- 
- [[concepts/Skill-Files]]
- [[concepts/Agent-Architecture]]
- [[tools/Claude-Code]]
- [[tools/Hermes-Agent]]

## Source
[[summaries/LearnWithBrij-Learning-Claude-Code-Part-3]]
[[summaries/Santtiagom-SKILL-MD-Guide]]
[[summaries/GarryTan-Thin-Harness-Fat-Skills]]
