---
title: "CI/CD Canary Deployment Strategy"
source: "ChatGPT"
author: "-"
published: "2026-06-02"
type: note
---

# CI/CD Canary

## Summary
Estrategia canary en CI/CD: despliegue gradual a un grupo pequeño (1-5% del tráfico) antes del rollout completo. Requiere routing controlado, métricas claras de salud y rollback rápido.

## Core Concepts
- [[Canary-Deployment]] -- estrategia de despliegue gradual con monitoreo progresivo
- [[Observability]] -- métricas de error_rate, latency_p95 y business_success_rate como mínimo

## Key Insights
- Diferencia con blue/green: canary es gradual, blue/green es cambio casi instantáneo
- La observabilidad es el weak link: sin métricas fiables, el canary es "desplegar a ciegas"
- 3 métricas mínimas: error_rate, latency_p95, business_success_rate

## Source

- **Raw note:** [[ci-cd-canary.md]]
- **Original URL:** ChatGPT
