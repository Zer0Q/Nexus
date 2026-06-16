---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2044190166655611087?s=20"
author:
  - "[[@santtiagom_]]"
published: 2026-04-13
created: 2026-06-16
description: "Se habla mucho de agentes. Pero hay un concepto más importante para entender cómo funcionan: el harness. Si usás Claude Code, Cursor o Cod"
tags:
  - "clippings"
summary:
---
Se habla mucho de agentes.

Pero hay un concepto más importante para entender cómo funcionan: el harness.

Si usás Claude Code, Cursor o Codex, gran parte de lo que pasa viene de ahí.

Un LLM, por sí solo, solo genera texto. No puede leer tus archivos, ejecutar código ni hacer cambios. Para eso existe el harness: el sistema que lo conecta con tu entorno, le da acceso a herramientas (leer, editar, ejecutar) y se encarga de ejecutar lo que el modelo propone.

Funciona así:

→ el modelo recibe contexto (tu código, instrucciones, historial)

→ con eso decide qué hacer

→ el sistema ejecuta esa acción (leer archivo, correr comando, etc.)

→ le devuelve el resultado como nuevo contexto

→ el modelo decide el siguiente paso

Y repite ese loop hasta resolver la tarea.

En el video lo baja a algo muy concreto.

Dice que con 3 tools ya podés armar algo básico: encontrar código, leer archivos y editarlos. Con eso ya tenés un agente funcional que puede trabajar sobre un repo.

Y ahí está la clave.

Ese sistema es el que define qué información ve el modelo, cómo puede actuar y cómo avanza en cada paso. Por eso, pequeños cambios en el harness cambian completamente el resultado.

De hecho, muestra un caso donde el mismo modelo (Opus) pasa de ~77% a ~93% en un benchmark de código, solo por cambiar el harness.

Por eso, la diferencia ya no está solo en el modelo, sino en cómo armás el sistema alrededor.

Recomiendo el video. Muy bueno.

> **Theo - t3.gg @theo** · 2026-04-13
> 
> Agent harnesses aren't the black magic many of y'all seem to think they are. To prove it, I built one.