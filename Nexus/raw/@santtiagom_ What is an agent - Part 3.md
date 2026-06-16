---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2065150466040664300"
author:
  - "[[@santtiagom_]]"
published: 2026-06-11
created: 2026-06-16
description: "un error común en IA es pensar que los modelos pueden leer archivos, editar código o hacer requests a APIs. un modelo por sí solo no puede"
tags:
  - "clippings"
summary:
---
un error común en IA es pensar que los modelos pueden leer archivos, editar código o hacer requests a APIs.

un modelo por sí solo no puede hacer nada de eso.

recibe una entrada (texto, imágenes, audio, etc.), genera tokens de salida y nada más.

entonces:

¿cómo hace gpt o claude para leer tu código, abrir archivos o modificar un proyecto?

a través de tools.

imaginate que le pedís a claude code que arregle un bug en el login de tu app.

1) el modelo recibe tu pedido.

2) solicita una tool para leer archivos.

3) claude code ejecuta la tool y le devuelve el resultado.

4) el modelo analiza la información.

5) solicita más tools si las necesita.

6) responde

el modelo nunca abrió un archivo, nunca ejecutó código y nunca tocó tu proyecto.

solo fue solicitando tools y recibiendo resultados.

podés pensar al modelo como el cerebro y a las tools como la forma que tiene de interactuar con archivos, APIs, bases de datos y otros sistemas.

lo importante:

\> el modelo solo genera texto.

\> claude code es quien ejecuta herramientas, lee archivos, corre comandos y le devuelve los resultados al modelo.

a esa capa que ejecuta tools y conecta al modelo con el mundo real se la suele llamar harness.

![Imatge](https://pbs.twimg.com/media/HKjjOOMXUAAizzK?format=png&name=large)