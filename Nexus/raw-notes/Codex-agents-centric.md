---
title: "Ingeniería de sistemas: Codex en un mundo centrado en agentes"
source: "https://openai.com/es-419/index/harness-engineering/"
author:
published: 2026-05-27
created: 2026-06-04
description: "Por Ryan Lopopolo, miembro del personal técnico"
tags:
  - "clippings"
summary:
---
Durante los últimos cinco meses, nuestro equipo ha estado llevando a cabo un experimento: desarrollar y lanzar una versión beta interna de un producto de software con **0 líneas de código escritas manualmente**.

El producto cuenta con usuarios internos diarios y evaluadores alfa externos. Se lanza, se despliega, se rompe y se arregla. Lo que es diferente es que cada línea de código (lógica de la aplicación, pruebas, configuración de CI, documentación, observabilidad y herramientas internas) ha sido escrita por Codex. Calculamos que construimos esto en aproximadamente una décima parte del tiempo que nos habría llevado escribir el código a mano.

**Los seres humanos guían. Los agentes ejecutan.**

Elegimos intencionalmente esta restricción para construir lo necesario y aumentar la velocidad de ingeniería en órdenes de magnitud. Tuvimos semanas para entregar lo que terminó siendo un millón de líneas de código. Para lograrlo, necesitábamos comprender qué cambia cuando la tarea principal de un equipo de ingeniería de software deja de ser escribir código y pasa a ser diseñar entornos, especificar intenciones y construir bucles de retroalimentación que permitan a los agentes de Codex hacer un trabajo fiable.

Esta publicación trata sobre lo que aprendimos al crear un producto completamente nuevo con un equipo de agentes: qué se rompió, qué se complicó y cómo maximizar nuestro único recurso verdaderamente escaso: el tiempo y la atención humanos.

## Comenzamos con un repositorio git vacío

El primer commit en un repositorio vacío se llevó a cabo a finales de agosto de 2025.

El andamiaje inicial (estructura del repositorio, configuración de CI, reglas de formato, configuración del gestor de paquetes y marco de la aplicación) se generó por Codex CLI usando GPT‑5, guiado por un pequeño conjunto de plantillas existentes. Incluso el archivo inicial AGENTS.md que indica a los agentes cómo trabajar en el repositorio fue escrito por Codex.

No existía código preexistente escrito por seres humanos para fijar el sistema. Desde el principio, el repositorio fue moldeado por el agente.

Cinco meses después, el repositorio contiene aproximadamente un millón de líneas de código en términos de lógica de la aplicación, infraestructura, herramientas, documentación y utilidades internas para desarrolladores. Durante ese período, se abrieron y fusionaron aproximadamente 1 500 pull requests, con un pequeño equipo de solo tres ingenieros a cargo de Codex. Esto se traduce en un rendimiento promedio de 3.5 PRs por ingeniero al día, y sorprendentemente el rendimiento ha *aumentado* a medida que el equipo ha crecido hasta llegar a siete ingenieros. Es importante destacar que esto no fue un resultado por el resultado mismo: el producto ha sido utilizado internamente por cientos de usuarios, incluidos usuarios avanzados que lo utilizan diariamente.

Durante todo el proceso de desarrollo, los seres humanos nunca aportaron directamente ningún código. Esto se convirtió en una filosofía central para el equipo: **ningún código escrito manualmente**.

## Redefinir el papel del ingeniero

La falta de programación práctica a cargo de seres humanos **introdujo un tipo diferente de trabajo de ingeniería, centrado en sistemas, estructuras y aprovechamiento**.

El progreso inicial fue más lento de lo que esperábamos, no porque Codex fuera incapaz, sino porque el entorno no estaba bien definido. Al agente le faltaban las herramientas, las abstracciones y la estructura interna necesarias para avanzar hacia metas de alto nivel. La tarea principal de nuestro equipo de ingeniería se convirtió en habilitar a los agentes para que hicieran un trabajo útil.

En la práctica, esto significó trabajar de manera profunda: descomponer objetivos más grandes en componentes más pequeños (diseño, código, revisión, prueba, etc.), motivar al agente a construir esos bloques y utilizarlos para desbloquear tareas más complejas. Cuando algo fallaba, la solución casi nunca era “esforzarse más.” Porque la única manera de avanzar era lograr que Codex hiciera el trabajo, los ingenieros humanos siempre intervenían en la tarea y preguntaban: “¿qué capacidad falta y cómo hacemos que sea tanto legible como aplicable para el agente?”.

Los seres humanos interactúan con el sistema casi por completo a través de prompts: un ingeniero describe una tarea, ejecuta el agente y permite que abra una pull request. Para completar una PR, le indicamos a Codex que revise sus propios cambios localmente, solicite revisiones adicionales específicas de agentes tanto localmente como en la nube, responda a cualquier comentario proporcionado por seres humanos o agentes, e itere en un bucle hasta que todos los agentes revisores estén satisfechos (en la práctica, esto es un [Ralph Wiggum Loop ⁠](https://ghuntley.com/loop/)). Codex utiliza nuestras herramientas estándar de desarrollo directamente (gh, scripts locales y habilidades integradas en el repositorio) para recopilar contexto sin que las personas tengan que copiar y pegar en la CLI.

Las personas pueden revisar las pull requests, pero no están obligadas a hacerlo. Con el tiempo, hemos dirigido casi todo el esfuerzo de revisión para que se maneje de agente a agente.

## Mejorar la legibilidad de la aplicación

A medida que aumentó el rendimiento del código, nuestro cuello de botella se convirtió en la capacidad humana para el control de calidad. Dado que la restricción fija ha sido el tiempo y la atención humanos, hemos trabajado para añadir más capacidades al agente haciendo que elementos como la interfaz de usuario de la aplicación, los registros y las métricas de la aplicación sean directamente legibles para Codex.

Por ejemplo, hicimos que la aplicación fuera arrancable por git worktree, de modo que Codex pudiera iniciar y manejar una instancia por cada cambio. También conectamos el protocolo de Chrome DevTools en el entorno de ejecución del agente y desarrollamos habilidades para trabajar con instantáneas del DOM, capturas de pantalla y navegación. Esto permitió a Codex reproducir errores, validar correcciones y razonar directamente sobre el comportamiento de la interfaz de usuario.

Hicimos lo mismo con las herramientas de observabilidad. Los registros, las métricas y los trazos se exponen a Codex a través de una pila de observabilidad local que es efímera para cualquier árbol de trabajo. Codex opera en una versión completamente aislada de esa aplicación, incluidos sus registros y métricas, que se eliminan una vez que se completa la tarea. Los agentes pueden consultar los registros con LogQL y las métricas con PromQL. Con este contexto disponible, prompts como “asegura que el inicio del servicio se complete en menos de 800 ms” o “ningún intervalo en estos cuatro recorridos críticos del usuario supera los dos segundos” se vuelven manejables.

Con frecuencia vemos que ejecuciones individuales de Codex trabajan en una sola tarea durante más de seis horas (a menudo mientras los seres humanos duermen).

## Hicimos del conocimiento del repositorio el sistema de registro

La gestión del contexto es uno de los mayores desafíos para que los agentes sean efectivos en tareas grandes y complejas. Una de las primeras lecciones que aprendimos fue simple: **dale a Codex un mapa, no un manual de instrucciones de 1000 páginas.**

Probamos el enfoque “one big [`AGENTS.md` ⁠](https://agents.md/) ”. Falló de maneras predecibles:

- **El contexto es un recurso limitado.** Un archivo de instrucciones gigantesco desplaza la tarea, el código y la documentación relevante, por lo que el agente o bien pasa por alto restricciones clave o empieza a optimizar para las incorrectas.
- **Demasiada orientación se convierte en** ***desorientación*****.** Cuando todo es “importante”, nada lo es. Los agentes terminan emparejando patrones localmente en lugar de navegar intencionadamente.
- **Se descompone al instante.** Un manual monolítico se transforma en un cementerio de reglas caducas. Los agentes no pueden saber qué sigue siendo cierto, los seres humanos dejan de mantenerlo y el archivo se convierte silenciosamente en un atractivo peligro.
- **Es difícil de verificar.** Un solo bloque no se presta a verificaciones mecánicas (cobertura, frescura, propiedad, enlaces cruzados), por lo que el desvío es inevitable.

Así que, en lugar de tratar `AGENTS.md` como la enciclopedia, lo tratamos como **el índice**.

La base de conocimientos del repositorio se encuentra en un directorio estructurado `docs/` que se considera el sistema de registro. Un breve `AGENTS.md` (aproximadamente 100 líneas) se inyecta en el contexto y sirve principalmente como un mapa, con referencias a fuentes de información más profundas en otros lugares.

#### Texto plano

```
AGENTS.md
ARCHITECTURE.md
docs/
├── design-docs/
│   ├── index.md
│   ├── core-beliefs.md
│   └── ...
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── generated/
│   └── db-schema.md
├── product-specs/
│   ├── index.md
│   ├── new-user-onboarding.md
│   └── ...
├── references/
│   ├── design-system-reference-llms.txt
│   ├── nixpacks-llms.txt
│   ├── uv-llms.txt
│   └── ...
├── DESIGN.md
├── FRONTEND.md
├── PLANS.md
├── PRODUCT_SENSE.md
├── QUALITY_SCORE.md
├── RELIABILITY.md
└── SECURITY.md
```

Diseño de la estructura del almacén de conocimiento en el repositorio.

La documentación de diseño se cataloga e indexa, incluyendo el estado de verificación y un conjunto de creencias fundamentales que definen los principios operativos centrados en el agente. La [documentación de arquitectura ⁠](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html) ofrece un mapa de alto nivel de dominios y la organización de capas de paquetes. Un documento de calidad evalúa cada dominio del producto y de la capa arquitectónica, rastreando las brechas a lo largo del tiempo.

Los planes se consideran artefactos de primera categoría. Los planes efímeros y ligeros se utilizan para cambios pequeños, mientras que el trabajo complejo se documenta en [planes de ejecución ⁠](https://cookbook.openai.com/articles/codex_exec_plans) con registros de progreso y decisiones que se integran en el repositorio. Los planes activos, los planes completados y la deuda técnica conocida están versionados y colocalizados, permitiendo a los agentes operar sin depender de un contexto externo.

Esto permite la **divulgación progresiva**: los agentes comienzan con un punto de entrada pequeño y estable y se les enseña dónde mirar a continuación, en lugar de abrumarlos desde el principio.

Hacemos que el cumplimiento se verifique de manera mecánica. Linters y trabajos de CI especiales verifican que la base de conocimientos esté actualizada, enlazada de manera cruzada y estructurada correctamente. Un agente recurrente de “doc-gardening” busca documentación desactualizada u obsoleta que no refleja el comportamiento real del código y abre pull requests para corregirla.

## La claridad del agente es el objetivo

A medida que el código base evolucionó, el marco de Codex para decisiones de diseño también debía evolucionar.

Dado que el repositorio es completamente generado por el agente, está optimizado primero para la *legibilidad* de *Codex*. De la misma manera que los equipos buscan mejorar la navegabilidad de su código para los nuevos empleados de ingeniería, el objetivo de nuestros ingenieros humanos era hacer posible que un agente pudiera razonar sobre todo el dominio empresarial **directamente desde el propio repositorio.**

Desde el punto de vista del agente, cualquier cosa a la que no pueda acceder en contexto mientras se ejecuta efectivamente no existe. El conocimiento que reside en Google Docs, hilos de chat o en la mente de las personas no es accesible para el sistema. Los artefactos versionados y locales del repositorio (p. ej., código, markdown, esquemas, planes ejecutables) son todo lo que puede ver.

Aprendimos que necesitábamos agregar cada vez más contexto al repositorio con el tiempo. ¿Esa conversación en Slack que alineó al equipo respecto de un patrón arquitectónico? Si el agente no puede encontrarla, es ilegible, de la misma manera que sería desconocida para un nuevo empleado que se una tres meses después.

Dar a Codex más contexto significa organizar y exponer la información adecuada para que el agente pueda razonar sobre ella, en lugar de abrumarlo con instrucciones ad hoc. De la misma manera que comunicarías a un nuevo compañero de equipo en los principios del producto, las normas de ingeniería y la cultura del equipo (incluidas las preferencias de emojis), proporcionar esta información al agente da lugar a un resultado mejor alineado.

Este marco aclaró muchas disyuntivas. Favorecimos dependencias y abstracciones que pudieran ser completamente internalizadas y razonadas dentro del repositorio. Las tecnologías que a menudo se describen como “aburridas” tienden a ser más fáciles de modelar para los agentes debido a su componibilidad, la estabilidad de la API y la representación en el conjunto de entrenamiento. En algunos casos, resultaba más económico que el agente reimplementara subconjuntos de funcionalidad en lugar de sortear el comportamiento opaco de las bibliotecas públicas. Por ejemplo, en lugar de incorporar un paquete genérico al estilo de `p-limit`, implementamos nuestro propio asistente de mapeo con concurrencia: está estrechamente integrado con nuestra instrumentación de OpenTelemetry, tiene un 100 % de cobertura de pruebas y se comporta exactamente como lo espera nuestro entorno de ejecución.

Incorporar más del sistema en un formato que el agente pueda inspeccionar, validar y modificar directamente aumenta la capacidad de influencia, no solo para Codex, sino también para otros agentes (por ejemplo, [Aardvark](https://openai.com/es-419/index/introducing-aardvark/)) que también están trabajando en la base de código.

## Imposición de la arquitectura y el gusto

La documentación por sí sola no logra mantener coherente una base de código completamente generada por agentes. **Al implementar los invariantes, en lugar de microgestionar las implementaciones, permitimos que los agentes avancen rápidamente sin socavar los cimientos.** Por ejemplo, requerimos que Codex [analice las estructuras de datos en el límite ⁠](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/), pero no somos prescriptivos sobre cómo debe hacerse (al modelo parece gustarle Zod, pero no especificamos esa biblioteca en particular).

Los agentes son más efectivos en entornos con [límites estrictos y una estructura predecible ⁠](https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code), por lo que construimos la aplicación en torno a un modelo arquitectónico rígido. Cada dominio empresarial se divide en un conjunto fijo de capas, con direcciones de dependencia estrictamente validadas y un conjunto limitado de conexiones permitidas. Estas restricciones se imponen mecánicamente a través de linters (generados por Codex, ¡por supuesto!) y pruebas estructurales personalizados.

El diagrama a continuación muestra la regla: dentro de cada dominio empresarial (por ejemplo, Configuración de la app), el código solo puede depender “hacia adelante” a través de un conjunto fijo de capas (Tipos → Configuración → Repositorio → Servicio → Tiempo de ejecución → Interfaz de usuario). Las inquietudes transversales (auth, conectores, telemetría, feature flags) ingresan a través de una única interfaz explícita: Providers. No se permite nada más y se aplica de forma mecánica.

Este es el tipo de arquitectura que normalmente pospones hasta que cuentas con cientos de ingenieros. Con los agentes de codificación, es un requisito previo temprano: las restricciones son lo que permite la velocidad sin deterioro ni desviación arquitectónica.

En la práctica, aplicamos estas reglas con linters y pruebas estructurales personalizados, además de un pequeño conjunto de “invariantes de estilo.” Por ejemplo, aplicamos de manera estática el registro estructurado, las convenciones de nomenclatura para esquemas y tipos, los límites de tamaño de archivo y los requisitos de confiabilidad específicos de la plataforma con lints personalizados. Dado que los lints son personalizados, redactamos los mensajes de error para incluir instrucciones de remediación en el contexto del agente.

En un flujo de trabajo centrado en las personas, estas reglas podrían parecer pedantes o limitantes. Con los agentes, se convierten en multiplicadores: una vez codificados, se aplican en todas partes simultáneamente.

Al mismo tiempo, somos claros sobre dónde importan las restricciones y dónde no. Esto se asemeja a liderar una gran organización de plataformas de ingeniería: establecer límites de manera centralizada y permitir autonomía localmente. Te importan mucho los límites, la corrección y la reproducibilidad. Dentro de esos límites, permites a los equipos (o a los agentes) una libertad significativa en la forma en que se expresan las soluciones.

El código resultante no siempre coincide con las preferencias estilísticas de las personas, y eso está bien. Mientras el resultado sea correcto, mantenible y legible para futuras ejecuciones del agente, cumple con el estándar.

El gusto humano se introduce de nuevo en el sistema de manera continua. Los comentarios de revisión, las pull requests de refactorización y los errores visibles para el usuario se documentan como actualizaciones o se integran directamente en las herramientas. Cuando la documentación es insuficiente, promovemos la regla al código

## El rendimiento altera la filosofía de integración.

A medida que aumentó el rendimiento de Codex, muchas normas convencionales de ingeniería se volvieron contraproducentes.

El repositorio opera con compuertas de fusión que bloquean mínimamente. Las pull requests son de corta duración. Las pruebas inestables a menudo se resuelven con ejecuciones de seguimiento en lugar de detener el progreso indefinidamente. En un sistema donde el rendimiento del agente supera ampliamente la atención humana, las correcciones son económicas y esperar resulta costoso.

Esto sería irresponsable en un entorno de bajo rendimiento. Aquí, a menudo es el punto medio adecuado.

## Qué significa realmente "generado por el agente"

Cuando decimos que el código base es generado por agentes de Codex, nos referimos a todo lo que hay en el código base.

Los agentes producen:

- Código de producto y pruebas
- Configuración de CI y herramientas de publicación
- Herramientas internas para desarrolladores
- Documentación e historia de diseño
- Arneses de evaluación
- Revisión de comentarios y respuestas
- Scripts que gestionan el repositorio en sí mismo
- Archivos de definición del tablero de producción

Los seres humanos siempre permanecen involucrados, pero trabajan en un nivel de abstracción diferente al que solíamos. Priorizamos el trabajo, convertimos los comentarios de los usuarios en criterios de aceptación y validamos los resultados. Cuando el agente tiene dificultades, lo tratamos como una señal: identificamos qué falta (herramientas, controles, documentación) y lo devolvemos al repositorio, siempre haciendo que Codex mismo escriba la corrección.

Los agentes utilizan directamente nuestras herramientas estándar de desarrollo. Extraen comentarios de revisión, responden en línea, envían actualizaciones y, a menudo, combinan y fusionan sus propias pull requests.

## Aumentar los niveles de autonomía

A medida que más del bucle de desarrollo se codificó directamente en el sistema (pruebas, validación, revisión, gestión de comentarios y recuperación), el repositorio cruzó recientemente un umbral significativo en el que Codex puede gestionar de principio a fin una nueva funcionalidad.

Dado un solo prompt, el agente ahora puede:

- Validar el estado actual del código base
- Reproducir un bug reportado
- Grabar un video que demuestre la falla
- Implementar una solución
- Validar la corrección conduciendo la aplicación
- Grabar un segundo video demostrando la resolución
- Abrir una pull request
- Responder a los comentarios del agente y de las personas
- Detectar y remediar fallas de compilación
- Escalar a un ser humano solo cuando se requiera criterio humano.
- Fusionar el cambio

Este comportamiento depende en gran medida de la estructura y las herramientas específicas de este repositorio y no debe suponerse que se generalice sin una inversión similar, al menos, todavía no.

## Entropía y gestión de basura

**La autonomía completa del agente también presenta problemas nuevos.** Codex replica patrones que ya existen en el repositorio, incluso los desiguales o subóptimos. Con el tiempo, esto inevitablemente lleva a una desviación.

Inicialmente, los seres humanos las abordaban manualmente. Nuestro equipo solía dedicar todos los viernes (20 % de la semana) a limpiar la “basura de la IA”. Como era de esperarse, eso no escaló.

En su lugar, comenzamos a codificar lo que llamamos “principios dorados” directamente en el repositorio y establecimos un proceso de limpieza recurrente. Estos principios son reglas mecánicas y con una postura definida que mantienen la base de código legible y consistente para futuras ejecuciones del agente. Por ejemplo: (1) preferimos paquetes de utilidades compartidos en lugar de ayudantes hechos a mano para mantener las invariantes centralizadas, y (2) no exploramos datos "al estilo YOLO"; validamos los límites o confiamos en SDK tipeados para que el agente no pueda construir accidentalmente sobre formas supuestas. Con una cadencia regular, tenemos un conjunto de tareas de Codex en segundo plano que escanean en busca de desviaciones, actualizan las calificaciones de calidad y abren pull requests de refactorización dirigidas. La mayoría de estas se pueden revisar en menos de un minuto y fusionarse automáticamente.

Esto funciona como la recolección de basura. La deuda técnica es como un préstamo con intereses altos: casi siempre es mejor pagarla continuamente en pequeñas cuotas que dejar que se acumule y abordarla en tandas difíciles. El gusto humano se captura una vez y luego se aplica continuamente en cada línea de código. Esto también nos permite identificar y solucionar patrones problemáticos diariamente, en lugar de permitir que se extiendan en la base de código durante días o semanas.

## Lo que aún tenemos que aprender

Hasta ahora, esta estrategia ha funcionado bien durante el lanzamiento interno y la adopción en OpenAI. Desarrollar un producto auténtico para usuarios reales nos ayudó a consolidar nuestras inversiones en la realidad y a orientarnos hacia la sostenibilidad a largo plazo.

Lo que todavía no sabemos es cómo evoluciona la coherencia arquitectónica a lo largo de los años en un sistema completamente generado por agentes. Todavía estamos aprendiendo dónde el juicio humano aporta el mayor valor y cómo codificar ese juicio para que se multiplique. Tampoco sabemos cómo evolucionará este sistema a medida que los modelos sigan mejorando sus capacidades con el tiempo.

Lo que está claro es que crear software sigue exigiendo disciplina, pero esa disciplina se nota más en el andamiaje que en el código. Las herramientas, las abstracciones y los bucles de retroalimentación que mantienen la coherencia de la base de código son cada vez más importantes.

**Nuestros desafíos más difíciles ahora se centran en diseñar entornos, bucles de retroalimentación y sistemas de control** que ayuden a los agentes a lograr nuestro objetivo: construir y mantener software complejo y confiable a gran escala.

A medida que agentes como Codex asumen porciones más grandes del ciclo de vida del software, estas preguntas serán aún más importantes. Esperamos que compartir algunas lecciones iniciales te ayude a reflexionar sobre dónde invertir tu esfuerzo para que [puedas simplemente construir cosas](https://openai.com/es-419/codex/).