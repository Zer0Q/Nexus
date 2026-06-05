# Canary Deployment

## Definition
Estrategia de despliegue en CI/CD donde una nueva versión se libera a un grupo pequeño y controlado (1-5% del tráfico) antes del rollout completo, con monitoreo progresivo y rollback rápido.

## Why It Matters
Reduce el riesgo de despliegues detectando fallos en producción con impacto limitado. Esencial para entornos donde los agentes IA generan código a velocidad máquina.

## Key Ideas
- Progresión: 1-5% → 10% → 25% → 50% → 100% del tráfico
- Diferencia con blue/green: canary es gradual, blue/green es cambio casi instantáneo
- 3 requisitos: routing controlado, métricas claras de salud, rollback rápido
- 3 métricas mínimas: error_rate, latency_p95, business_success_rate
- La observabilidad es el weak link: sin métricas fiables, el canary es "desplegar a ciegas"

## Related
- [[concepts/AI-Native-Engineering]]
- [[concepts/Agentic-Development-Life-Cycle]]

## Source
[[summaries/ChatGPT-CICD-Canary]]
