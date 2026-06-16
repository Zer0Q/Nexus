---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2066281700590567549?s=20"
author:
  - "[[@santtiagom_]]"
published: 2026-06-12
created: 2026-06-16
description: "agente = modelo + harness modelo → es el cerebro. interpreta el contexto y toma decisiones. harness (runtime) → es la capa que coordina la"
tags:
  - "clippings"
summary:
---
agente = modelo + harness

modelo → es el cerebro. interpreta el contexto y toma decisiones.

harness (runtime) → es la capa que coordina la ejecución del agente.

conecta al modelo con:

\> tools → para leer archivos, llamar APIs, consultar bases de datos o ejecutar código

\> memory → para recuperar contexto desde conversaciones anteriores y preferencias guardadas

\> loops → para ejecutar tareas, observar resultados y seguir avanzando hasta completar el objetivo

además suele encargarse de:

\> planificación → organizar los pasos necesarios para resolver una tarea

\> permisos → controlar qué archivos, tools o acciones puede utilizar

\> monitoreo → registrar qué hizo el agente y qué resultados obtuvo

\> validaciones → verificar que el resultado sea correcto antes de continuar

\> manejo de errores → detectar problemas y decidir cómo responder

\> reintentos → volver a intentar o cambiar de estrategia cuando algo falla

por eso cuando construís un agente, el modelo es solo una pieza.

gran parte del desafío está en diseñar el harness que coordina todo lo demás.

> **santi @santtiagom\_** · 2026-06-12
> 
> un agente es mucho más simple de lo que parece:
> 
> todo empieza con un modelo que solo genera tokens. si le hacés una pregunta, responde texto.
> 
> pero los problemas reales requieren más que eso. hay que leer archivos, ejecutar código, buscar información y usar APIs.
> 
> para eso x.com/santtiagom\_/st…
> 
> ![Imatge](https://pbs.twimg.com/media/HKznY2PXAAA2171?format=jpg&name=large)