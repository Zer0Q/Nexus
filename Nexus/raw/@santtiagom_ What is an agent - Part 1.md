---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2065230988800647419"
author:
  - "[[@santtiagom_]]"
published: 2026-06-11
created: 2026-06-16
description: "un agente es mucho más simple de lo que parece: todo empieza con un modelo que solo genera tokens. si le hacés una pregunta, responde texto"
tags:
  - "clippings"
summary:
---
un agente es mucho más simple de lo que parece:

todo empieza con un modelo que solo genera tokens. si le hacés una pregunta, responde texto.

pero los problemas reales requieren más que eso. hay que leer archivos, ejecutar código, buscar información y usar APIs.

para eso existen las tools.

cada vez que el modelo usa una tool, obtiene información nueva.

mensajes, instrucciones, archivos y resultados de tools se van acumulando. a todo eso se le llama contexto.

cuanto mejor es el contexto, mejores decisiones puede tomar el modelo. pero hay un límite: no puede ver una cantidad infinita de información al mismo tiempo.

ese límite se llama context window.

hasta acá el modelo puede pensar y usar tools. el problema es que cuando termina la sesión, todo desaparece.

si volvés mañana, hay que volver a explicarle quién sos, qué estás construyendo y qué decisiones ya tomaste.

para evitar eso existe la memory. permite recuperar información importante de sesiones anteriores y volver a ponerla en contexto cuando hace falta.

ahora tenes un sistema que puede usar tools y recuperar información de sesiones anteriores.

pero todavía falta alguien que coordine todo eso.

¿qué memory cargar?

¿cuándo usar una tool?

¿cómo verificar que el resultado es correcto?

esa capa es el harness.

y como los problemas complejos rara vez se resuelven en el primer intento, aparece el loop:

ejecutar → observar → validar → corregir → repetir

cuando juntás modelo, contexto, memory, tools, harness y loop, obtenés un sistema capaz de perseguir objetivos por sí solo.

eso es un agente.

> **santi @santtiagom\_** · 2026-06-11
> 
> un error común en IA es pensar que los modelos pueden leer archivos, editar código o hacer requests a APIs.
> 
> un modelo por sí solo no puede hacer nada de eso.
> 
> recibe una entrada (texto, imágenes, audio, etc.), genera tokens de salida y nada más.
> 
> entonces:
> 
> ¿cómo hace gpt o
> 
> ![Imatge](https://pbs.twimg.com/media/HKjjOOMXUAAizzK?format=png&name=large)