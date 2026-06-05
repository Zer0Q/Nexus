---
title: "When AI builds itself"
source: "https://www.anthropic.com/institute/recursive-self-improvement"
author: "Marina Favaro, Jack Clark (Anthropic Institute)"
published: "2026-06-05"
type: article
---

# When AI Builds Itself — Recursive Self-Improvement

## Summary
Anthropic presenta evidencia pública y datos internos mostrando que la IA ya está acelerando el desarrollo de IA: los engineers de Anthropic ship 8x más código por trimestre que en 2021-2025, y los time horizons de tareas completadas por AI se duplican cada 4 meses. El artículo explora tres futuros posibles — la tendencia se estanca, gains compounding con humanos en el loop, o recursive self-improvement completo — y argumenta que el mundo necesita la opción de pausar el desarrollo de IA con mecanismos de verificación global, no pausas unilaterales.

## Core Concepts
- [[concepts/Recursive-Self-Improvement]] -- capacidad de un sistema AI de diseñar y desarrollar autónomamente su propio sucesor; Anthropic dice que no están ahí pero podría llegar antes de lo que las instituciones están preparadas
- [[concepts/Compounding-AI-Acceleration]] -- la retroalimentación donde AI acelera el desarrollo de AI: time horizons duplicándose cada 4 meses (4 min → 1.5h → 12h), engineers shipping 8x más código, benchmarks saturando en 2 años
- [[concepts/Amdahl-Law-in-AI-Development]] -- acelerar una parte del proceso desplaza el bottleneck: human code review se convirtió en el cuello de botella cuando Claude genera código más rápido de lo que los humanos pueden revisar
- [[concepts/Human-Comparative-Advantage]] -- la zona donde los humanos aún superan a AI: research taste, choosing which problems matter, which results to trust, when an approach is a dead end; esta zona se está estrechando

## Key Insights
- METR data: Claude Opus 3 (marzo 2024) completaba tareas de ~4 min, Claude Sonnet 3.7 (marzo 2025) ~1.5h, Claude Opus 4.6 (marzo 2026) ~12h — si la tendencia continúa, tareas de días llegarían este año y tareas de semanas en 2027
- SWE-bench saturó en 2 años: de dígitos individuales a ~100% en benchmarks de software engineering real
- >80% del código merged a producción en Anthropic es attributable a Claude (líderes estiman 90%+ incluyendo scripts y código experimental)
- GitHub vio ~1B commits en todo 2025; a mitad de 2026 veía 275M/semana, pace para ~14B anuales — infraestructura global bajo presión
- En engineering: Claude puede recibir un problema underspecified y figure out cómo resolverlo — humanos dan el goal, pero ya no necesitan dar el método
- En research: Claude ya matchea o supera humanos expertos ejecutando experiments bien-especificados, pero persisten gaps grandes en judgment para elegir goals
- "La perspiración se está automatizando" — la mayoría del progreso en frontier es incremental (scale, ver qué breaks, fix, repeat), exactamente el workflow donde Claude ahora excela
- Project Glasswing (Mythos Preview): en sus primeras semanas encontró 10,000+ vulnerabilidades de alta/crítica severidad — el bottleneck en cyber defense ya se movió de encontrar vulnerabilidades a patchearlas lo suficientemente rápido
- Tres futuros: (1) tendencia se estanca (S-curve, supply chain constraints), (2) compounding gains con humanos en loop (100-person companies doing work of 100K), (3) recursive self-improvement completo (pace determined by compute availability)
- Una pausa unilateral es achievable inmediatamente pero cambia quién es el front-runner sin crear deliberación más amplia; una pausa verificable multi-lab es necesaria pero requiere infraestructura que tomó décadas construir para armas nucleares
- "100-person companies could do the work of 10,000- or 100,000-person organizations" — pero también "turned to harmful ends: authoritarian surveillance, influence operations at scale no human team could match"

## Open Questions
- ¿El gap de research taste entre humanos y AI se cierra con más scale o requiere un cambio arquitectónico (post-Transformer)?
- ¿Cómo medir "productivity multipliers" de forma que distinga entre output que realmente importa vs output que solo existe porque ahora es barato generar?
- ¿Los sistemas de verificación para pausas globales de AI development son viables cuando training runs son más fáciles de ocultar que misiles y los inputs son general-purpose?

## Source
- **Raw note:** [[raw-notes/when-ai-builds-itself]]
- **Original URL:** https://www.anthropic.com/institute/recursive-self-improvement
