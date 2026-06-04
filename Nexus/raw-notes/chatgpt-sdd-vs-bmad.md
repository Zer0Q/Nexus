---
title: "ChatGPT - SDD vs BMAD"
source: "https://chatgpt.com/?temporary-chat=true"
author:
published:
created: 2026-05-27
description: "ChatGPT es tu asistente de IA para el día a día. Habla con la IA más avanzada para explorar ideas, resolver problemas y aprender más rápido."
tags:
  - "clippings"
summary:
---
En el contexto de **Spec-Driven Development (SDD)**, **BMAD** normalmente se refiere a:

> **BMad Method**  
> o  
> **Breakthrough Method for Agile AI-Driven Development**

Es un framework orientado a desarrollo asistido por IA donde:

- La **specificación** es el artefacto central.
- Se usan múltiples agentes/personas IA:
	- Analyst
		- PM
		- Architect
		- Developer
		- QA
- El flujo intenta reemplazar el “vibe coding” por:
	- PRDs estructurados
		- arquitectura explícita
		- task decomposition
		- validación antes de generar código

Idea base:

```markdown
Idea
  ↓
Requirements / PRD
  ↓
Architecture
  ↓
Stories / Tasks
  ↓
Implementation
  ↓
Validation
```

La diferencia importante frente a otros enfoques SDD como Spec-Kit:

| Tool | Filosofía |
| --- | --- |
| Spec-Kit | Spec-first minimalista |
| BMAD | Simulación de equipo Agile multi-agente |
| OpenSpec | Specs estructuradas + ejecución |
| Vibe Coding | Prompt → código directo |

BMAD enfatiza mucho:

- separación de roles,
- handoffs,
- contexto persistente,
- trazabilidad entre spec y código.

Repos oficiales/documentación:

- [BMAD Method Docs](https://docs.bmad-method.org/?utm_source=chatgpt.com)
- [BMAD GitHub](https://github.com/bmad-code-org/BMAD-METHOD?utm_source=chatgpt.com)

**Stress test rápido**

### Lo bueno

- Reduce drift del LLM.
- Mejor para proyectos medianos/grandes.
- Fuerza arquitectura antes de implementación.
- Encaja bien con perfiles de arquitecto.

### Lo malo

- Overhead alto.
- Mucho artifact generation.
- Fácil caer en “document-driven procrastination”.
- Para PoCs pequeñas puede ser más lento que útil.

### Mi lectura técnica

BMAD es básicamente:

```markdown
Agile + Multi-Agent Orchestration + Spec-Driven Development
```

No es una metodología revolucionaria nueva.  
Es una operacionalización de buenas prácticas clásicas adaptadas a agentes LLM.

**Critical Path**

- Entender que BMAD NO sustituye arquitectura.
- Sustituye coordinación/manual prompting.

**Weakest Link**

- Context explosion.
- Specs enormes degradan calidad del agente.

**Next Step**  
Si quieres, puedo hacerte:

- comparativa real BMAD vs Spec-Kit vs OpenSpec,
- arquitectura interna de BMAD,
- o cómo adaptar BMAD a un entorno enterprise serio (Wind/SCADA/mission-critical).

Haz una investiación de todos los frameworks, kits, metodologias relacionadas con el desarrollo usando IA que no solo incluya SDD y BMAD. Extiende este analisis a otras cubriendo tambien BDD, TDD, etc. Formatea esto en una tabla resumen con enlaces para extender la información

Voy a separar **metodologías clásicas**, **AI-native/spec-first**, **agentic coding**, y **governance/eval**. El objetivo: tabla útil para decidir, no inventario infinito.

Asumo que querías decir **Spec-Driven Development**, no “sped”.

## Mapa resumen

| Categoría | Framework / metodología | Qué controla | Encaja con IA | Mejor uso | Riesgo |
| --- | --- | --- | --- | --- | --- |
| **SDD** | **GitHub Spec Kit** | Spec → plan → tasks → code | Muy alto | Producto nuevo, features complejas | Overhead documental [GitHub+1](https://github.com/github/spec-kit?utm_source=chatgpt.com) |
| **SDD** | **OpenSpec** | Specs ligeras iterativas | Alto | Equipos que quieren menos ceremonia | Menos governance [GitHub](https://github.com/Fission-AI/OpenSpec?utm_source=chatgpt.com) |
| **SDD / Agile AI** | **BMAD Method** | Roles AI: analyst, PM, architect, dev, QA | Muy alto | Proyectos medianos/grandes | Burocracia / context explosion [Ran the Builder+1](https://ranthebuilder.cloud/blog/i-tested-three-spec-driven-ai-tools-here-s-my-honest-take/?utm_source=chatgpt.com) |
| **SDD / IDE-native** | **Kiro** | Specs + tasks dentro del IDE | Alto | Equipos AWS/IDE-centric | Lock-in de toolchain [Medium+1](https://medium.com/%40visrow/comprehensive-guide-to-spec-driven-development-kiro-github-spec-kit-and-bmad-method-5d28ff61b9b1?utm_source=chatgpt.com) |
| **Agentic coding** | **OpenHands** | Agente autónomo que modifica repos | Alto | Issues → PRs | Requiere sandbox/evals fuertes [OpenHands+1](https://openhands.dev/?utm_source=chatgpt.com) |
| **Agentic coding** | **Open SWE** | GitHub issue → plan → code → tests → PR | Alto | Delegar tareas bien acotadas | Calidad variable del PR [LangChain](https://www.langchain.com/blog/introducing-open-swe-an-open-source-asynchronous-coding-agent?utm_source=chatgpt.com) |
| **Agent SDK** | **smolagents** | Construcción de agentes simples | Medio/alto | Prototipos, tools, workflows | No es SDLC completo [Hugging Face](https://huggingface.co/blog/smolagents?utm_source=chatgpt.com) |
| **TDD** | **Test-Driven Development** | Tests antes del código | Muy alto | Guardrails para agentes | Tests pobres = código pobre [martinfowler.com+1](https://martinfowler.com/bliki/TestDrivenDevelopment.html?utm_source=chatgpt.com) |
| **BDD** | **Cucumber / Gherkin** | Behaviour specs ejecutables | Muy alto | Business rules, aceptación | Gherkin basura = teatro [cucumber.io+1](https://cucumber.io/docs/bdd/?utm_source=chatgpt.com) |
| **BDD + AI** | **LLM-assisted BDD** | Generar/validar escenarios BDD | Alto | Product + QA + dev alignment | Falsos escenarios plausibles [ResearchGate+1](https://www.researchgate.net/publication/389451796_Agentic_AI_for_Behavior-Driven_Development_Testing_Using_Large_Language_Models?utm_source=chatgpt.com) |
| **Contract-driven** | **Pact / CDC** | Contratos consumidor-proveedor | Muy alto | Microservicios, APIs, eventos | Contratos incompletos [docs.pact.io+1](https://docs.pact.io/?utm_source=chatgpt.com) |
| **Architecture governance** | **Fitness Function-Driven Development** | Reglas arquitectónicas automatizadas | Muy alto | Mission-critical, quality gates | Difícil definir métricas buenas [Thoughtworks+1](https://www.thoughtworks.com/en-gb/insights/articles/fitness-function-driven-development?utm_source=chatgpt.com) |
| **Evolutionary Architecture** | **Building Evolutionary Architectures** | Cambio guiado por constraints | Alto | Sistemas vivos, long-term | Requiere disciplina continua [Thoughtworks](https://www.thoughtworks.com/en-es/insights/books/building-evolutionaryarchitectures-second-edition?utm_source=chatgpt.com) |
| **Prompt-first** | **Vibe Coding** | Prompt → código | Bajo/medio | Demos, spikes, PoCs pequeñas | No escala, poca trazabilidad |
| **Intent-driven** | **Intent-Driven Development** | Intención → agentes → implementación | Medio | Narrativa AI-native emergente | Concepto aún difuso [KodeNerds](https://www.kodenerds.com/blog/intent-driven-development-2026?utm_source=chatgpt.com) |
| **Agentic engineering** | **Agentic SDLC** | Agentes en análisis, código, test, PR | Alto | Equipos con CI/CD maduro | Governance y seguridad [PwC+1](https://www.pwc.com/m1/en/publications/2026/docs/future-of-solutions-dev-and-delivery-in-the-rise-of-gen-ai.pdf?utm_source=chatgpt.com) |

## Lectura brutal

**Para software serio con IA, el stack ganador no es uno solo.**

Usaría esto:

```markdown
BDD/SDD -> Architecture Constraints -> TDD -> Contract Tests -> Agentic Coding -> CI/Evals
```

## Ranking práctico

| Caso | Mejor enfoque |
| --- | --- |
| PoC rápida | Vibe coding + TDD mínimo |
| Feature real | Spec Kit / OpenSpec + TDD |
| Producto nuevo | BMAD o Spec Kit |
| Microservicios | SDD + Pact |
| Mission-critical | SDD + TDD + CDC + fitness functions |
| Equipo enterprise | BMAD + architecture fitness functions |
| Repo existente con issues | OpenHands / Open SWE con tests obligatorios |

## Critical Path

**No empieces por elegir herramienta.**  
Empieza por definir el **artifact pipeline**:

```markdown
Intent -> Spec -> Acceptance Criteria -> Architecture Constraints -> Tests -> Code -> Verification
```

## Weakest Link

**La IA amplifica ambigüedad.**  
Sin specs verificables, solo generas código más rápido y deuda más rápido.

## Next Step

Haz una matriz propia con **3 candidatos**:

- **Spec Kit**
- **BMAD**
- **OpenSpec**

Y evalúalos contra un caso real tuyo de 1 feature.