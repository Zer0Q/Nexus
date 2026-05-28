---
title: "Harness y por qué los prompts complejos están perdiendo sentido"
source: "https://davidhurtado.substack.com/p/harness-y-por-que-los-prompts-complejos?utm_campaign=email-half-post&r=1f3hcu&utm_source=substack&utm_medium=email"
author:
  - "[[David Hurtado]]"
published: 2026-05-27
created: 2026-05-27
description: "Primera parte sobre prompts, harness y agentes."
tags:
  - "clippings"
summary:
---


![80-harnes-y-por-que-los-prompts-complejos-pierden-sentido.webp](https://substackcdn.com/image/fetch/$s_!4M11!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa19fcbd-58f3-408f-8f9a-7ce4cc4582d9_1383x821.webp)

Hace un par de años, si querías resultados decentes de un modelo de lenguaje, necesitabas construir el prompt con cierta complejidad: asignarle un rol, detallar el contexto, explicar el método paso a paso, estructurar las instrucciones en bloques. Era razonable. Los modelos respondían mejor cuando les dabas esa estructura.

Ahora es cada vez menos necesario. Con un prompt muy simple, la respuesta suele ser muy buena.

---

## ¿Modelos más listos?

![80-Harness-y-por-que-los-prompts-complejos-pierden-sentido.webp](https://substackcdn.com/image/fetch/$s_!Nz3Y!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1a7217c-7d7e-4076-aa91-8a9df3e218b0_2097x658.webp)

Los modelos de IA van mejorando, pero no es solo el modelo. Cuando interactúas con una IA hoy, no estás hablando directamente con un modelo. Entre tu prompt y el modelo hay una capa que gestiona el contexto, coordina los pasos intermedios y al final monta la respuesta. Esa capa tiene un nombre técnico: **harness**.

El harness vendría a ser *toda la maquinaria de software que rodea al modelo*. Y la mejora más sustancial de los últimos meses viene de harnesses más capaces.

Lo que percibes como “la IA me entiende mejor” es en buena parte el harness haciendo trabajo que antes tenías que hacer tú en el prompt.

---

## Entonces, ¿el prompt no importa?

![80-Harness-y-por-que-los-prompts-complejos-pierden-sentido-1.webp](https://substackcdn.com/image/fetch/$s_!aSz1!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94259816-a50a-4722-93c3-7aa33523a0d9_2097x634.webp)

Que el harness haga más trabajo no significa que puedas soltarle preguntas vagas y esperar que acierte. Hay tres elementos que siguen siendo muy útiles para conseguir buenas respuestas, y que ningún sistema puede inferir con fiabilidad:

#### 1\. El resultado que esperas

No el tema general, sino el entregable concreto. *“Un documento explicativo”* no es lo mismo que *“un documento explicativo orientado al comité de dirección, que está preocupado por la falta de adopción del último trimestre pero están reticentes a desbloquear más presupuesto”*

#### 2\. Para qué sirve ese resultado

El uso final cambia la forma en que la IA prioriza. En el ejemplo anterior, *“un documento explicativo”* no es lo mismo que *“un documento explicativo para ayudar a entender que el cambio a facturación por uso (tokens) puede ser beneficioso si creamos las métricas adecuadas, aunque sean nuevas y no tengamos precedente”*.

#### 3\. Formato del resultado.

Formato, extensión, registro, cómo sabes que está bien hecho. Si no lo dices, la IA elige. Puede elegir bien, pero no elegirá necesariamente lo que tú querías.

---

Esto último es un punto importante: si no aportas tú estos 3 aspectos, la IA hará lo que quiera. Obtendrás un resultado que que responderá muy bien a preguntas, pero no necesariamente a las preguntas de tu caso particular. Y esto es aplicable tanto a documentos como a cualquier tarea que le encomendemos a la IA.

Lo que ya no necesitas añadir es el método, el *cómo*. No le digas a la IA cómo quieres que lo haga. No incluyas en el prompt los pasos que la IA debería seguir internamente para llegar al resultado.

---

## Por qué definir el proceso suele empeorar las cosas

![80-Harness-y-por-que-los-prompts-complejos-pierden-sentido-2.webp](https://substackcdn.com/image/fetch/$s_!YT_k!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99f3b60b-671a-4198-af63-8c857d8f799e_2097x638.webp)

Especificar el proceso que debe seguir el modelo (el *cómo* quieres que la IA trabaje) es, en la mayoría de las tareas comunes, contraproducente. Esto no te gustará oirlo, pero en la mayoría de las tareas, la IA es mejor que tú y que yo decidiendo *cómo* afrontarla. Hay dos motivos.

#### 1\. Construir un buen método es difícil

Requiere que el usuario conozca suficientemente bien el problema como para descomponerlo en pasos correctos. Si lo conoces tan bien, probablemente puedas resolver la tarea sin IA.

#### 2\. Imponer un método limita el espacio de soluciones

La IA, cuando tiene libertad para decidir cómo aproximarse a un problema, suele proponer rutas más eficientes que las que el usuario habría diseñado. Al forzarle un método, le pones tu propio techo de conocimiento encima.

---

**La excepción**: tareas donde el método es parte del entregable, donde hay restricciones externas -normativas, procedimientos, estilo de un cliente concreto-, o donde quieres que la IA trabaje siguiendo una metodología que ya tienes definida. En esos casos, adjuntar el método tiene sentido. Lo que no tiene sentido es construir esa estructura por defecto, para todas las tareas, por inercia.

---

## Ahora el trabajo es validar

![80-Harness-y-por-que-los-prompts-complejos-pierden-sentido-3.webp](https://substackcdn.com/image/fetch/$s_!7t23!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e9c4a5c-d157-481b-b60c-0a5638c8ecd4_2097x638.webp)

Antes la dificultad estaba en construir un buen prompt. Ahora, el prompt es básicamente *saber preguntar* y hay que poner esfuerzo en validar el resultado.

La IA suele generar respuestas que *parecen mejor de lo que realmente son*. Es decir, respuestas correctas en apariencia pero desviadas en algún criterio relevante. Si no tienes claro qué hace que el resultado sea bueno, no puedes detectar esa desviación.

La práctica es sencilla: antes de ejecutar, decide cómo sabes que esto está bien hecho. Cuando llegue el resultado, compruébalo contra eso. Si algo falla, pide a la IA que explique el proceso que siguió y corrige de forma específica. No reescribas el prompt original: localiza lo que falló y trátalo directamente.

Reescribir el prompt es básicamente *volver a intentarlo*. Volver a intentar que *la IA lo haga bien a la primera*. Mejor itera, pregunta, refina, corrige. Es el proceso natural de para llegar a un resultado de calidad. Y además, te fuerza a estudiar y entender el resultado.

---

## Un atajo cuando el prompt se complica

![80-Harness-y-por-que-los-prompts-complejos-pierden-sentido-4.webp](https://substackcdn.com/image/fetch/$s_!e3-V!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10810633-ccd6-4f86-bc3c-060e1cc90525_2097x645.webp)

Si en algún momento sientes que la tarea requiere un prompt largo y estructurado, hay una alternativa antes de ponerte a construirlo: describir a la IA el resultado que buscas y pedirle que redacte ella misma el prompt óptimo para obtenerlo. A esto lo llamamos [Metaprompt](https://davidhurtado.ai/Posts/2025.04/27-Metaprompt).

Es una consecuencia lógica de lo que ya sabemos: la IA sabe más de hacer prompting que nosotros mismos. Usas esa información a tu favor, revisas lo que te propone, ajustas si es necesario, y ejecutas.

Esto reduce a casi nada la barrera de entrada a tareas que antes requerían experiencia en la mal llamada profesión de ingeniero de prompts. Bonus: siguiendo con esta idea, aquí tienes el [Curso de ChatGPT más corto del mundo, además de gratis](https://davidhurtado.ai/Posts/2025.06/15-Curso-ChatGPT)

---

## Qué queda de todo esto

![80-Harness-y-por-que-los-prompts-complejos-pierden-sentido-5.webp](https://substackcdn.com/image/fetch/$s_!tiZI!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cd34dab-2c25-489a-9f35-e2bb630e7383_2097x657.webp)

Saber hacer buenos prompts sigue siendo útil. Lo que ha dejado de ser indispensable es dedicar tiempo a construir prompts complejos como práctica habitual.

Un usuario que define con precisión el qué, el para qué y la forma del resultado, y sobre todo, que valida bien lo que recibe, obtiene tanto o más que alguien que invierte el mismo tiempo en estructura y elaboración.

Todo esto es consecuencia del *harness*, o como decíamos al principio, toda la maquinaria técnica lo que rodea. EL próximo día, ***harness*** en detalle.