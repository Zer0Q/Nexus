---
title: "ChatGPT"
source: "https://chatgpt.com/?temporary-chat=true"
author:
published:
created: 2026-06-02
description: "ChatGPT es tu asistente de IA para el día a día. Habla con la IA más avanzada para explorar ideas, resolver problemas y aprender más rápido."
tags:
  - "clippings"
summary:
---
En **CI/CD**, un **canary** es una estrategia de despliegue donde liberas una nueva versión a un **grupo pequeño y controlado** antes de lanzarla al 100%.

**Idea base:**

- Despliegas la versión nueva a, por ejemplo, **1%–5% del tráfico**.
- Monitorizas errores, latencia, métricas de negocio y logs.
- Si todo va bien, aumentas progresivamente: **10% → 25% → 50% → 100%**.
- Si algo falla, haces **rollback rápido** o cortas el tráfico hacia la versión nueva.

## Ejemplo

Tienes:

- **v1**: versión estable.
- **v2**: nueva versión.

En vez de sustituir v1 por v2 de golpe:

```markdown
95% traffic -> v1
 5% traffic -> v2
```

Si v2 se comporta bien:

```markdown
50% traffic -> v1
50% traffic -> v2
```

Y finalmente:

```markdown
100% traffic -> v2
```

## Para qué sirve

**Reduce el riesgo** de un despliegue. Detectas fallos reales en producción con impacto limitado.

## Diferencia con blue/green

- **Blue/green:** cambias todo el tráfico de una versión a otra casi de golpe.
- **Canary:** mueves el tráfico gradualmente.

## Critical Path

Para usar canary bien necesitas:

1. **Routing controlado** de tráfico.
2. **Métricas claras** de salud.
3. **Rollback automático o muy rápido**.

## Weakest Link

El punto débil suele ser la **observabilidad**.  
Sin métricas fiables, un canary es solo “desplegar poco a poco a ciegas”.

## Next Step

Define estas 3 métricas mínimas antes de hacer canary:

```markdown
error_rate
latency_p95
business_success_rate
```