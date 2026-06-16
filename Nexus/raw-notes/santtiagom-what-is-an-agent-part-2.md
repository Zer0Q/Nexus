---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2065898594771591653"
author:
  - "[[@santtiagom_]]"
published: 2026-06-12
created: 2026-06-16
description: "una propiedad fundamental de los LLMs es que son stateless. ¿qué significa? que no recuerdan nada entre una llamada y la siguiente. vos l"
tags:
  - "clippings"
summary:
---
una propiedad fundamental de los LLMs es que son stateless.

¿qué significa?

que no recuerdan nada entre una llamada y la siguiente.

vos le enviás un mensaje. el modelo genera una respuesta. la llamada termina.

si le volvés a escribir, empieza desde cero.

entonces, ¿cómo puede seguir una conversación? ¿cómo puede acordarse de mensajes anteriores?

porque hay otro sistema (harness) que se encarga de guardar ese historial.

esto funciona más o menos así:

1) arrancás una sesión en claude code

2) le escribís un mensaje al modelo

3) el modelo responde

4) el sistema guarda esos mensajes

5) en la siguiente llamada, vuelve a enviar la conversación + tu nuevo mensaje

por eso parece que el modelo recuerda cosas, pero no. en cada llamada vuelve a recibir información que ya había visto antes.

y no solo la conversación.

también se agregan cosas como:

\> instrucciones sobre cómo debe comportarse

\> tools disponibles

\> información relevante para la tarea

volver a escribir todo eso manualmente en cada conversación sería absurdo.

por eso existen cosas como los system prompts, CLAUDE.md o AGENTS.md.

son mecanismos para agregar información importante al contexto en cada llamada.

gran parte de la ingeniería de agentes consiste en resolver este problema:

qué información vale la pena volver a mostrarle al modelo.

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
> ![Imatge](https://pbs.twimg.com/media/HKuLmIfWkAE9aI4?format=jpg&name=large)