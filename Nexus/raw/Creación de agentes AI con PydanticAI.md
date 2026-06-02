---
title: "Creación de agentes AI con PydanticAI"
source: "https://dev.to/kuscamara/creacion-de-agentes-ai-con-pydanticai-introduccion-h8"
author:
  - "[[Kus Cámara]]"
published: 2025-11-05
created: 2026-06-02
description: "En los últimos meses he tenido la suerte de explorar el mundo de los agentes AI, concretamente... Tagged with ai, python, spanish, pydanticai."
tags:
  - "clippings"
summary:
---
En los últimos meses he tenido la suerte de explorar el mundo de los agentes AI, concretamente utilizando la librería [PydanticAI](https://ai.pydantic.dev/). A fecha de la escritura de este post, no hay mucha información técnica en español sobre el tema, y dado que la librería es relativamente “nueva”, he decidido escribir una serie de posts para compartir lo que voy aprendiendo.

DISCLAIMER: No soy una experta, por lo que deberías tomar este post con la misma cautela que una respuesta de ChatGPT 😅

## Concepto de Agente AI

Definir qué es exactamente un agente no es tarea sencilla. Si te das una vuelta por LinkedIn, encontrarás fácilmente debates sobre si algo es realmente un agente, un workflow, o si tus agentes son menos agentes que los míos por haber usado herramientas *low-code*. Fuentes como HuggingFace, nos hablan incluso de [niveles de agencia](https://huggingface.co/docs/smolagents/conceptual_guides/intro_agents) en lugar de establecer una clasificación binaria.

[![Captura de pantalla de una tabla comparativa de niveles de agencia en HuggingFace](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fw0ounpkrfbflb0odgwxn.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fw0ounpkrfbflb0odgwxn.png)

Polémicas aparte, para el propósito de este post, nos quedaremos con la siguiente definición. Un agente es la combinación de los siguientes componentes:

- **Un LLM** (GPT, Claude, Gemini, etc.) -> el cerebro del agente. Responsable de procesar instrucciones en lenguaje natural, tomar decisiones sobre acciones a realizar y utilizar herramientas para interactuar con su entorno.
- **Un *system prompt*** -> un conjunto de instrucciones que configuran el comportamiento del LLM, definiendo su propósito y especialización, tono, medidas de seguridad (*guardrails*), etc.
- **Herramientas (*tools*)** -> funciones que el agente puede utilizar para llevar a cabo tareas específicas, como acceder a bases de datos, realizar búsquedas en la web o interactuar con APIs.

## Probar LLMs sin arruinarse

Sabiendo que lo primero que necesitamos es un LLM y que los más populares no son baratos, nos interesa encontrar formas de experimentar sin dejarnos una pasta.

Existen varias opciones que podemos probar:

- **[GitHub Models](https://docs.github.com/es/github-models):** GitHub te permite [experimentar de forma gratuita](https://docs.github.com/es/github-models/use-github-models/prototyping-with-ai-models#experimenting-with-ai-models-using-the-api) (con limitaciones de uso) con varios modelos LLM alojados en su plataforma. Es una excelente opción para empezar sin necesidad de configurar nada localmente. Solo necesitas una cuenta de GitHub y una API key.
- **[Google AI Studio](https://aistudio.google.com/):** Google también permite probar varios modelos de la serie Gemini de forma gratuita (con limitaciones) mediante Google AI Studio. Los modelos Gemini destacan por ofrecer una ventana de contexto enorme y un buen equilibrio entre rendimiento y coste.
- **[Ollama](https://ollama.com/):** Si prefieres trabajar completamente offline, Ollama te permite ejecutar modelos LLM de forma local en tu máquina. Eso sí, es importante elegir modelos adecuados para agentes (con capacidad de *thinking* y uso de tools) y que puedan funcionar con fluidez en tu equipo. En mi caso, usando un MacBook Air M3 con 16GB de RAM, los modelos con mejor rendimiento son **qwen2.5:7b-instruct**, **llama3.1:8b**, **gemma2:9b** y **mistral:7b-instruct**. Si bien estos modelos están lejos de la calidad de los grandes LLMs comerciales, pueden ser más que suficientes para experimentar y aprender.

[PydanticAI soporta estas tres opciones y otras](https://ai.pydantic.dev/models/overview/) como Anthropic, HuggingFace, OpenAI, etc.

## Creando un agente con PydanticAI

Una vez que tenemos un LLM y alguna idea de agente que queremos construir, podemos ponernos manos a la obra con PydanticAI.

En este ejemplo vamos a hacer algo sencillo y poco original: un agente que recomienda un plato de cocina en función de los ingredientes que el usuario le proporcione. Se llamará **DelicIA**.

### Configuración del proyecto Python e instalación de dependencias

He usado [uv](https://docs.astral.sh/uv/) como gestor de dependencias y entornos virtuales, pero puedes usar el que prefieras y adaptar los comandos según corresponda.

Crear un proyecto nuevo:

```
uv init delicia-agent
```

Instalación de dependencias:

```
uv add pydantic_ai
```

Creación del entorno virtual y activación:

```
uv venv .venv
source .venv/bin/activate  # Linux/Mac
```

## Configuración del agente

El archivo `main.py` se genera automáticamente al crear el proyecto con `uv`.  
  
Como LLM he optado por usar GitHub Models con `gpt-4o`.

```
# main.py

import asyncio
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.github import GitHubProvider

# Configuración del modelo LLM usando GitHub Models
model = OpenAIChatModel(
    "openai/gpt-4o",
    provider=GitHubProvider(api_key="github_pat_XXXXXXXXXXXXXXXXXXXXXX")  
)

# Definición del agente
delicia = Agent(
    name="DelicIA",
    model=model,
    # System prompt
    instructions=(
        "You are DelicIA, an AI specialized in providing delicious and healthy recipes. "
        "Your goal is to help users find recipes that can be made with the ingredients they provide. "
        "Provide a concise response with the recipe name and the preparation steps."
    )
)

async def main():
    await delicia.to_cli(prog_name="🥘 DelicIA")

if __name__ == "__main__":
    asyncio.run(main())
```

Estamos usando el método `to_cli()` de PydanticAI para interactuar con el agente desde la línea de comandos. Al ejecutar el script, se nos presentará un prompt para introducir los ingredientes, y el agente nos responderá con una recomendación de plato siguiendo las instrucciones definidas en el *system prompt*.

### Ejecución del agente

```
uv run python main.py
```

**Demo de ejecución**

[![Demostración de la ejecución del agente DelicIA en la línea de comandos](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fawvzyp723lazxpzy27ax.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fawvzyp723lazxpzy27ax.gif)

## Acceso a herramientas (tools)

Hasta ahora hemos podido materializar en el código dos de los componentes clave de un agente: el **LLM y el *system prompt*** con instrucciones básicas. Podríamos extender el *system prompt* mucho más con instrucciones para evitar respuestas no deseadas, ejemplos del formato de las respuestas a modo de *few-shot learning*, etc. Sin embargo, para que un agente sea realmente útil, y agente, necesita poder interactuar con su entorno a través de herramientas (*tools*).

Hay varias formas de [definir herramientas en PydanticAI](https://ai.pydantic.dev/tools/). En nuestro caso vamos a usar una *function tool* que simulará una consulta a una base de datos de recetas. Por simplicidad, usaremos un diccionario con un mapeo de ingredientes a recetas.

Para declarar una función como *tool* podemos usar el decorador `@tool`, si necesitamos acceso al contexto del agente, o `@tool_plain` si no necesitamos acceso al contexto. En nuestro caso, usaremos `@tool_plain`:

```
@delicia.tool_plain
def get_recipe(ingredient: str) -> str:
    """
    Returns a dish recipe based on the provided ingredient.
    Args:
        ingredient (str): The main ingredient for the recipe.
    Returns:
        str: A recipe suggestion or a message indicating no pre-established recipe is available.
    """
    recipes_dict = {
        "patatas": "Tortilla de patatas",
        "tomate": "Gazpacho andaluz",
        "pollo": "Pollo al ajillo",
        "arroz": "Paella valenciana",
        "huevos": "Huevos revueltos con jamón",
        "pescado": "Pescado a la plancha con limón",
        "pasta": "Espaguetis carbonara",
    }

    ingredient_lower = ingredient.lower().strip()

    if ingredient_lower in recipes_dict:
        return recipes_dict[ingredient_lower]
    else:
        return "croquetas"
```

**¿Cómo sabe el agente qué hace esta herramienta y qué parámetros necesita?**

Mediante la documentación de la función y los argumentos proporcionados en el docstring. PydanticAI utiliza esta información para generar un *schema* que describe la herramienta y sus parámetros. El LLM es el que se encarga de razonar sobre lo que debe hacer y las herramientas que tiene a su disposición para llevar a cabo las tareas solicitadas por el usuario.

Dependiendo del modelo que uses, puede que necesites ser más explícito en el *system prompt* e indicar que debe usar las herramientas disponibles. Incluso puede ser necesario incluir ejemplos de uso para guiar al modelo sobre cómo invocarlas correctamente y con qué parámetros. En nuestro caso con GPT-4o no ha sido necesario.

**Demo de ejecución con tool**

[![Demostración de la ejecución del agente DelicIA usando la tool get_recipe](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg2h60p2ch6phez6g789t.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg2h60p2ch6phez6g789t.png)

Esta parte puede resultar un poco confusa. Nuestra *tool* con una consulta ficticia a una base de datos devuelve solamente el nombre del plato. Sin embargo, la respuesta que estamos obteniendo del agente es mucho más completa, incluyendo los pasos de preparación. Lo que ocurre aquí es que el LLM incorpora la información devuelta por la tool en su razonamiento y genera una respuesta más elaborada con el objetivo de cumplir la instrucción dada en el *system prompt*, que es proporcionar una receta completa.

### Otros usos de las tools

Las *tools* no se limitan a obtener datos de fuentes externas. También son ideales para realizar cálculos, formatear datos o cualquier tarea que requiera la ejecución de código.

Por ejemplo, si necesitamos la fecha actual, es mucho más eficiente y fiable usar una *tool* que llame a `datetime.now()` que delegarlo al LLM. El LLM, muy probablemente, nos devolverá una fecha inventada en el pasado (los LLMs no tienen acceso a información en tiempo real) y además estaríamos consumiendo tokens innecesariamente. En general, cualquier operación determinista que pueda resolverse con código es una buena candidata para ser implementada como *tool*.

## Salida estructurada

Ya podemos decir que tenemos un agente, sin embargo, me gustaría mostrar una característica más de PydanticAI: la capacidad de definir un formato específico para la salida del agente. Esto puede ser útil cuando queremos que la salida del agente pueda ser consumida programáticamente por otras herramientas.

Para ello, vamos a necesitar [Pydantic](https://docs.pydantic.dev/latest/) para definir un modelo que represente la estructura de la salida que queremos.

Instalamos la dependencia:

```
uv add pydantic
```

En nuestro caso, definiremos un modelo `RecipeOutput` con los campos `name` y `preparation_steps`. Podríamos añadir campos como `cooking_time`, `difficulty`, `ingredients`, etc..

```
from pydantic import BaseModel

class RecipeOutput(BaseModel):
    name: str
    preparation_steps: list[str]
```

Luego, al definir el agente, podemos usar el parámetro `output_type` para especificar que queremos que la salida del agente siga la estructura definida en `RecipeOutput`.

```
delicia = Agent(
    name="DelicIA",
    model=model,
    instructions=(
        "You are DelicIA, an AI specialized in providing delicious and healthy recipes. "
        "Your goal is to help users find recipes that can be made with the ingredients they provide. "
        "Provide a concise response with the recipe name and the preparation steps."
    ),
    output_type=RecipeOutput  # Especificamos el tipo de salida
)
```

Al ejecutar el agente, la respuesta será una instancia de `RecipeOutput`, que podemos serializar fácilmente a JSON o manipular directamente como un objeto Python.

[![Captura de pantalla de la salida del agente con formato estructurado](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdt8lg7tn72txrci43hy3.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdt8lg7tn72txrci43hy3.png)

## Conclusión y próximos pasos

Hemos visto cómo crear un agente AI básico utilizando PydanticAI, incluyendo la configuración del LLM, el *system prompt*, la definición de herramientas (*tools*) y la estructuración de la salida utilizando Pydantic.

En próximos posts veremos temas como:

- Uso de MCPs
- Instrumentación mediante Pydantic Logfire
- Estrategias de reintentos para gestionar *rate limits*
- Optimización de mensajes para ajustarse a las ventanas de contexto de los LLMs

Si te interesan estos temas y estás empezando, no puedo dejar de recomendar los [cursos gratuitos de HuggingFace](https://huggingface.co/learn).

Hasta la próxima! 👋

DEV Community

[![Google AI Education track image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu09y9fffqrb2one15j3g.png)](https://dev.to/deved/build-apps-with-google-ai-studio?bb=238784)

## Work through these 3 parts to earn the exclusive Google AI Studio Builder badge!

This track will guide you through Google AI Studio's new "Build apps with Gemini" feature, where you can turn a simple text prompt into a fully functional, deployed web application in minutes.