---
title: "SKILLS en Claude Code: la guía completa para empezar hoy"
source: "https://x.com/santtiagom_/status/2030305647535751338"
author:
  - "[[@santtiagom_]]"
published: 2026-03-07
created: 2026-06-16
description: "Estas semanas creé más de 50 Skills.Algunas para revisar mi código antes de ir a producción, otras para documentar pull requests y procesos...."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HC0Tj_kWEAAO91k?format=jpg&name=large)

Estas semanas creé más de 50 Skills.

Algunas para revisar mi código antes de ir a producción, otras para documentar pull requests y procesos. La mayoría las terminé eliminando a los 2 días. Pero las que quedaron, cambiaron completamente cómo trabajo con Claude.

Pero para entender por qué importan, primero hay que entender el problema que resuelven.

Cuando usás Claude Code todos los días, empezás a notar un patrón. Le pedís un code review el lunes y te da un análisis detallado. El martes lo mismo y te lista tres bullets genéricos. Mismo modelo, mismo pedido, resultado completamente distinto.

No es que esté mal. Es un modelo que predice tokens, no una máquina exacta. Cada vez que lo usás, empieza de 0. Sin memoria de cómo lo hizo antes. Sin contexto de cómo trabajás vos.

¿Y si hubiera una forma de enseñarle? ¿De escribir una vez cómo querés que trabaje y que lo aplique siempre?

Eso son las Skills. Estuve semanas experimentando con ellas, rompiendo cosas, descartando lo que no funcionaba. Por eso escribí este artículo. No busco resumirte la documentación, sino contarte todo lo que aprendí. Al final, vas a entender qué son, cómo funcionan por dentro y vas a poder crear la tuya desde cero. Empecemos.

## ¿Qué es una Skill?

Una Skill son instrucciones. Le explicás a Claude cómo querés que haga una tarea: qué revisar primero, qué ignorar, qué formato usar. La próxima vez que le pedís esa tarea, la hace exactamente como vos le indicaste.

Pensalo así: un chef sabe cocinar. Tiene técnica, criterio, años de experiencia. Pero si entra a trabajar a tu restaurante sin conocer tus recetas, va a cocinar bien, pero a su manera. No es que sea malo, sino que nadie le explicó cómo trabajás vos.

Una Skill es la receta. No le enseñás a cocinar, eso ya lo sabe. Le explicás cómo querés que cocine.

![Imatge](https://pbs.twimg.com/media/HCxJLJWWYAA1avl?format=jpg&name=large)

Ejemplo concreto: una Skill de code review. En el archivo le explicás que primero revise la legibilidad, después la complejidad, después la performance. Que las funciones de más de 20 líneas hay que refactorizar. Que siempre termine con un resumen ordenado por impacto. Todo eso, escrito una vez.

Ahora cada vez que le pedís un code review, sigue esas indicaciones. Sin que vos se las repitas. Sin que tengas que aclarar nada. Claude trabaja como vos querés, no como le parece a él.

**Y esa es la ventaja real de las Skills: dejás de repetirte.**

![Imatge](https://pbs.twimg.com/media/HCxN-5HWgAA_3iL?format=jpg&name=large)

Si todavía te suena abstracto, no te preocupes. Vamos a seguir profundizando y va a hacer click.

## Por qué esto importa

3 problemas que tiene casi todo el que usa Claude regularmente:

**El problema de consistencia.** Le pedís un code review el lunes y te da un análisis detallado. El martes lo mismo y te lista tres bullets genéricos. Skills bloquean eso porque Claude sigue las mismas instrucciones cada vez.

**El problema de calidad.** Claude sabe hacer code review, pero no sabe que vos querés que revise legibilidad antes que performance, o que las funciones de más de 20 líneas son candidatas a refactorizar. Skills le enseñan lo que aprendiste vos.

**El problema de eficiencia.** Cada vez que abrís una conversación nueva, tenés que volver a explicar todo ese contexto. Tu stack, tus preferencias, tus restricciones. Skills lo recuerdan por vos.

## La anatomía de una Skill

El único archivo obligatorio es el **SKILL.md**. Tiene 2 partes.

![Imatge](https://pbs.twimg.com/media/HC0Od8SXwAAB61g?format=jpg&name=large)

**El frontmatter.** Un bloque YAML al inicio del archivo con el nombre y la descripción. El nombre se convierte en el comando que usás para invocarla. La descripción es lo que Claude lee para decidir si activarla o no.

Tenés 2 formas de activarla. La primera es escribiendo /code-review directamente en el chat. La segunda es automática: si tu descripción dice "usá cuando el usuario pida revisar un PR", Claude la activa solo cuando le pedís eso, sin que vos la invoques manualmente.

**El body.** Las instrucciones en markdown. Acá es donde escribís el workflow, tu expertise, las herramientas a usar y los recursos disponibles.

![Imatge](https://pbs.twimg.com/media/HCxOnmjWcAEBUvr?format=jpg&name=large)

Después del SKILL.md, podés agregar carpetas según lo que necesite la Skill:

**references/** para documentación extra que Claude consulta cuando la necesita. Guías de estilo, esquemas, convenciones del equipo.

**scripts/** para código que Claude puede ejecutar. Validar un archivo antes de entregarlo, verificar que algo se generó correctamente.

**templates/** para archivos base que Claude usa en el output. Tu template de PowerPoint, un archivo HTML de base, tu logo.

## Cómo Claude carga una Skill

Claude no carga todas las Skills de una. Usa un sistema llamado progressive disclosure: carga solo lo que necesita, cuando lo necesita.

Funciona en 3 niveles. Siguiendo el ejemplo de la Skill de code review:

**Nivel 1: nombre y descripción.** Es lo único que se carga al inicio de cada sesión. Claude escanea todas las descripciones disponibles y decide cuál activar. Ve code-review: Revisá el código para detectar bugs... y lo tiene en cuenta.

**Nivel 2: el SKILL.md completo.** Le pedís "revisá este PR" y matchea. Recién ahí lee todo el SKILL.md: el workflow, tus reglas, los criterios de refactorización.

**Nivel 3: scripts, references y templates.** Si tu Skill tiene un script que valida el formato del código, lo carga solo si lo necesita para esa tarea. Si no, no existe.

![Imatge](https://pbs.twimg.com/media/HCxPE1zXcAAzEmj?format=jpg&name=large)

Esto significa que podés tener 50 Skills instaladas con mucho contenido cada una, y nada de eso afecta el rendimiento hasta que se necesita.

Por eso **la descripción es lo más importante que escribís**. Si es vaga, Claude no sabe cuándo activar la Skill y todo lo que escribiste adentro queda invisible.

Y hay un límite práctico: 15.000 caracteres para la lista completa de Skills. Si tenés muchas con descripciones largas, las últimas pueden quedar fuera. Cortas y precisas.

## Cuándo tiene sentido crear una Skill

La señal más clara: si te encontrás escribiendo el mismo contexto en cada conversación, ya tenés una Skill sin escribir.

3 casos concretos donde vale la pena:

**Cuando el output depende de contexto que el modelo no tiene.** Tu stack, tus convenciones, cómo trabaja tu equipo. Por ejemplo: cada vez que pedís un componente de React, terminás aclarando que usás Tailwind, que los props necesitan defaults, que los estilos van inline. Si lo repetís en cada conversación, es una Skill.

**Cuando el resultado tiene que ser consistente.** Si le pedís una presentación y a veces arranca con un slide, otras va directo al problema, otras te pregunta qué querés, la razón es que nadie le explicó cómo querés que lo haga.

**Cuando el proceso tiene pasos que se olvidan.** Querés que en un code review siempre revise seguridad antes de sugerir refactors. Sin una Skill, a veces lo hace, a veces no.

![Imatge](https://pbs.twimg.com/media/HCxSdJQW0AAEJHa?format=jpg&name=large)

Lo que no tiene sentido: crear una Skill para algo que hacés una vez, o para tareas donde el contexto cambia tanto que instrucciones fijas no ayudan. Una Skill es un marco, no una solución universal.

## Skills que ya podés usar hoy

Anthropic tiene Skills oficiales que podés instalar directamente desde Claude Code. Las encontrás en: [https://github.com/anthropics/skills](https://github.com/anthropics/skills)

Para instalarlas, ejecutás este comando en Claude Code:

```bash
/plugin install document-skills@anthropic-agent-skills
```

**DOCX.** Crea y edita documentos de Word. Maneja tracked changes, comentarios, tablas e imágenes manteniendo el formato correcto. También extrae texto y analiza el contenido de archivos existentes.

**XLSX.** Crea spreadsheets con fórmulas, formato y visualizaciones. Lee y analiza datos de archivos existentes, modifica hojas manteniendo las fórmulas intactas y genera gráficos a partir de los datos.

**PDF.** Extrae texto y tablas, crea nuevos PDFs, mergea y splitea documentos, rota páginas, llena formularios y procesa archivos escaneados con OCR.

**PPTX.** Crea y edita presentaciones. Genera slides con layouts, tipografías y paletas de colores. También lee y analiza presentaciones existentes.

**Frontend Design.** Genera interfaces web con criterio de diseño: tipografía, color, composición y jerarquía visual. Produce componentes que se ven trabajados, no genéricos.

Si querés explorar miles de Skills de la comunidad, podés hacerlo desde [https://skills.sh](https://skills.sh/). Pero tené cuidado: estas Skills no están verificadas por Anthropic. Una Skill puede incluir scripts que Claude ejecuta directamente en tu entorno. Si instalás una sin revisarla, ese script podría acceder a archivos, hacer requests a servicios externos o ejecutar comandos en tu máquina.

Antes de instalar cualquier Skill de la comunidad, revisá el SKILL.md y los scripts. Si tiene código que no entendés, no la instales.

## Skills para tu equipo

Las Skills no son solo personales. Las podés compartir con todo tu equipo.

Hay 2 tipos según dónde las guardás:

**Skills personales.** Van en ~/.claude/skills/ y están disponibles en todos tus proyectos. Son las que creás para tu flujo de trabajo individual, las que experimentás, las que todavía no estás seguro si compartir.

**Skills de proyecto.** Van en .claude/skills/ dentro del repositorio. Se commitean a git y cuando alguien hace pull, las tiene disponibles automáticamente. Acá van las convenciones del equipo, los workflows compartidos, los scripts que todos usan.

![Imatge](https://pbs.twimg.com/media/HC0MTuLWgAAaran?format=jpg&name=large)

La ventaja es clara: **escribís la Skill una vez y todo el equipo trabaja con el mismo criterio.** No más inconsistencias entre lo que genera un dev y otro.

Y hay algo más que vale la pena mencionar: podés restringir qué herramientas puede usar Claude cuando una Skill está activa. Con el campo allowed-tools en el frontmatter, le decís exactamente con qué puede trabajar.

```yaml
---
name: code-reviewer
description: Revisá el código para detectar bugs y mejorar calidad.
allowed-tools: Read, Grep, Glob
---
```

En este caso, la Skill solo puede leer archivos. No puede modificar nada. Útil cuando querés que el agente analice sin tocar.

## Skills + MCP: el siguiente nivel

Las Skills también se pueden combinar con tools y servidores MCP. Esto las hace mucho más poderosas porque el agente no solo sigue instrucciones, sino que puede interactuar con servicios externos.

![Imatge](https://pbs.twimg.com/media/HCxQLFPX0AAvkUz?format=jpg&name=large)

Por ejemplo, una Skill que automatiza el flujo completo de un PR en GitHub. Le pedís "revisá y mergeá el PR #42" y el agente ejecuta todo:

El agente usa el MCP de GitHub para ejecutar cada paso. Vos solo pedís el resultado.

![Imatge](https://pbs.twimg.com/media/HCxQms2WgAA9Axp?format=jpg&name=large)

**Esta combinación es donde las Skills se vuelven verdaderamente agénticas.** Dejás de pedirle cosas a Claude y empezás a delegarle procesos completos.

## Tu primera Skill, paso a paso

El error más común es querer diseñar la Skill perfecta desde el principio. No funciona así. Las mejores que tengo las construí iterando, no planificando.

**Paso 1: detectá la repetición.** Esta semana, cada vez que le des contexto al agente antes de pedirle algo, anotalo. "Tené en cuenta que usamos Tailwind", "el formato tiene que ser este", "primero validá antes de procesar". Si lo escribiste más de 3 veces, es candidata.

**Paso 2: creá la carpeta.** Una vez que tenés el caso de uso, creás la carpeta y el archivo:

```bash
mkdir ~/.claude/skills/nombre-de-tu-skill
touch ~/.claude/skills/nombre-de-tu-skill/SKILL.md
```

**\***también podes pedirle a Claude que lo haga por vos. **Paso 3: escribí la versión mínima.** Solo lo esencial para el caso más común. Una Skill de cinco líneas que funciona bien vale más que una de cien que el agente sigue a medias. Si tu Skill de code review tiene 80 reglas, va a ignorar la mitad.

**Paso 4: probala con casos reales.** Ejecutá la misma tarea con y sin la Skill. Si el output con Skill es notablemente mejor, vas bien. Si no ves diferencia, las instrucciones son demasiado genéricas.

**Paso 5: iterá en base a lo que falla.** Cada vez que el agente haga algo que no querías, preguntate si esa corrección debería estar en la Skill. Si le estás diciendo "no, el resumen va al principio" por tercera vez, eso va a la Skill.

**Paso 6: usá a Claude para mejorarla.** Pegá tu SKILL.md en una conversación y pedile que la revise. Que identifique instrucciones ambiguas, que sugiera ejemplos, que mejore la descripción para que matchee mejor. Claude entiende el formato y puede ayudarte a iterar mucho más rápido que haciéndolo solo.

Y si querés ir un paso más allá, Anthropic tiene una Skill oficial llamada **skill-creator** que te guía paso a paso en el proceso de crear una Skill desde cero: desde definir el caso de uso hasta escribir el frontmatter y validar las instrucciones. La encontrás en el mismo repositorio que las demás Skills oficiales.

## Buenas prácticas (según Anthropic)

Estas son las que más impacto tienen en la calidad de tus Skills:

**Sé conciso.** Claude ya es inteligente. No le expliques cosas que ya sabe. Cada línea que escribís compite con el resto del contexto. Si te preguntás "¿realmente necesita saber esto?", probablemente no.

**La descripción lo es todo.** Escribila en tercera persona, que incluya qué hace la Skill y cuándo activarla. "Procesa archivos Excel" no alcanza. "Analizá spreadsheets, creá pivot tables y generá gráficos. Usá cuando el usuario mencione archivos Excel, datos tabulares o .xlsx" sí.

**Mantené el SKILL.md bajo 500 líneas.** Si necesitás más, mové el contenido a archivos separados en references/ y referencialos desde el SKILL.md. Un nivel de profundidad, no más.

**Usá workflows con pasos claros.** Para tareas complejas, definí el orden exacto. Paso 1, paso 2, paso 3. Sin esto, Claude decide solo qué hacer primero.

**Implementá loops de validación.** Si la Skill genera algo, que valide el output antes de darlo por terminado. Ejecutar → validar → corregir → repetir. Mejora enormemente la calidad.

**Dale el nivel de libertad correcto.** Si la tarea tiene una sola forma correcta de hacerse, dásela exacta. Si tiene múltiples enfoques válidos, dejale margen. No todo necesita instrucciones estrictas.

**Probala con casos reales, no con ejemplos ideales.** Una Skill puede funcionar perfecto en teoría y fallar en la práctica. Testear con tareas reales es lo único que revela los gaps.

![Imatge](https://pbs.twimg.com/media/HC0NKqLXYAAmvWn?format=jpg&name=large)

## Cómo saber si una Skill funciona bien

Ejecutá la misma tarea 3 veces. Si cada ejecución parece una conversación distinta, la Skill necesita trabajo.

3 señales de que algo está mal:

**El agente ignora instrucciones.** Le pediste que valide antes de ejecutar y lo saltea. Generalmente las instrucciones están enterradas o son ambiguas. "Tené en cuenta la seguridad" no es una instrucción, es una sugerencia. "Antes de ejecutar cualquier query, validá que los inputs no contengan caracteres especiales" sí lo es.

**La descripción no matchea.** La Skill se activa cuando no debería, o no se activa cuando sí debería. Revisá la descripción antes que el body, casi siempre el problema está ahí.

**El output es genérico.** Se parece a lo que Claude haría sin la Skill. La diferencia entre "hacé un buen code review" y "revisá legibilidad primero, después complejidad, marcá funciones de más de 20 líneas como candidatas a refactorizar, y terminá con un resumen ordenado por impacto" es enorme.

La pregunta después de cada ejecución es una sola: ¿esto es mejor que lo que hubiera producido sin la Skill? Si la respuesta no es clara, hay algo para mejorar.

![Imatge](https://pbs.twimg.com/media/HC0NZFlbcAANqMJ?format=jpg&name=large)

## Patrones avanzados

Dos patrones que vale la pena conocer una vez que tenés experiencia con Skills básicas.

**Inyectar contexto dinámico.** Con la sintaxis !comando podés ejecutar comandos de shell antes de que Claude vea el contenido de la Skill. El output reemplaza al placeholder, así Claude recibe datos reales, no el comando en sí.

Por ejemplo, una Skill de resumen de PR que fetchea los datos del pull request automáticamente:

![Imatge](https://pbs.twimg.com/media/HC0NpObXkAAte52?format=jpg&name=large)

Cuando la Skill corre, los comandos se ejecutan primero y Claude recibe el prompt ya con los datos adentro. Esto es preprocesamiento, no algo que Claude ejecuta.

**Correr una Skill en un subagente.** Agregando context: fork al frontmatter, la Skill corre en un contexto aislado. No tiene acceso al historial de la conversación. Útil para tareas de research o análisis que no necesitan contexto previo y que querés que corran de forma independiente.

![Imatge](https://pbs.twimg.com/media/HC0Nx9zXsAEPd1W?format=jpg&name=large)

## Para cerrar

Skills funcionan muy bien para que Claude trabaje como vos querés. No es fácil diseñarlas, requiere ser preciso en lo que pedís y anticipar casos que no contemplás. Pero es una habilidad que se va entrenando. Una combinación de prompt engineering y testing.

Una vez que hacés click, empezás a notar que hay tareas del día a día que se pueden convertir en Skills. El agente empieza a pensar como vos, a ejecutar las cosas como a vos te gustan.

A mí me sirven mucho para automatizar procesos. La última en la que estuve trabajando mapea todas las requests HTTP a servicios externos y exporta una colección a Postman o Insomnia. **Extremadamente útil cuando trabajás en un equipo con más de 10 repositorios.**

Podés crear Skills para resolver vulnerabilidades, para que el agente haga research y te resuma un tema a tu manera, para cualquier tarea que repitas y que tenga un proceso claro detrás.

**Mi consejo: empezá hoy.** Probá a crear una Skill chica. Que lea un texto que le pasás y te haga un resumen con puntos importantes y que te recomiende temas para seguir profundizando.

No importa si después la eliminás. Hacela para practicar. Para entrenar el ojo y saber qué necesita ser una Skill.

Espero que este artículo te sirva 🙂

Santi

## Para seguir profundizando

- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) — Anthropic
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — Anthropic
- [Agent Skills — Claude Code Docs](https://code.claude.com/docs/en/skills) — Anthropic