---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2026426248122216501?s=20"
author:
  - "[[@santtiagom_]]"
published: 2026-02-24
created: 2026-06-16
description: "Tenés un e-commerce y bajaron tus ventas. Entonces le decís a Claude: “Analizá por qué bajaron las ventas esta semana.” Eso es el prompt"
tags:
  - "clippings"
summary:
---
Tenés un e-commerce y bajaron tus ventas.

Entonces le decís a Claude:

“Analizá por qué bajaron las ventas esta semana.”

Eso es el prompt → lo que pedís en ese momento.

Para que pueda mirar datos reales, por ejemplo tu base de datos, necesitás conectarlo a tus sistemas. Podés hacerlo con MCP (Model Context Protocol) o con una tool custom definida por vos.

Eso le permite listar ventas, agrupar por fecha o traer campañas.

Pero no querés que Claude analice como quiera.

Querés que siempre compare contra la semana pasada, separe por channel, detecte qué producto cayó más y marque alerta si la caída supera el 20%. Y que cualquier equipo use exactamente ese mismo criterio.

Por eso lo convertís en una Skill.

Una skill son instrucciones y pasos definidos en archivos que Claude lee como contexto. Esto no es un prompt suelto ni una función que se ejecuta sola. Es tu forma de trabajar formalizada para que siempre analice con el mismo criterio.

Y si el problema fuera más grande, el agente podría delegar partes del trabajo. Por ejemplo, crear un subagent para revisar campañas y otro para analizar cohorts, y después combinar todo en una conclusión final.

Un Subagent es un agente invocado por otro para encargarse de una parte del proceso

Entonces:

Prompt → lo que pedís

MCP o tool custom → acceso a datos

Skill → instrucciones formales que Claude usa como contexto

Subagent → agente que puede encargarse de una parte del proceso