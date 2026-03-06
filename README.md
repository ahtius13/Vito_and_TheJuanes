# Sistema Inteligente de Análisis de opiniones de Películas

## 1. Definición del proyecto

### 1.1 Propósito del sistema

El objetivo de este proyecto es desarrollar una aplicación que analice comentarios de
usuarios sobre películas y determine automáticamente si una película es recomendable o
no basándose en el sentimiento general de las opiniones.
Actualmente existen grandes cantidades de reseñas en internet (IMDb, TMDB, etc.), pero
analizar manualmente cientos de comentarios para decidir si una película merece la pena
puede ser tedioso. Este sistema utiliza técnicas de Machine Learning y modelos de lenguaje
para automatizar ese análisis.
El sistema está pensado para:

● Usuarios que quieren saber rápidamente si una película merece la pena.

● Plataformas o desarrolladores que quieran integrar un sistema de análisis de
opiniones.

● Proyectos educativos que quieran demostrar el uso combinado de análisis de datos,
machine learning, modelos preentrenados y APIs.

El valor añadido frente a analizar un dataset en un notebook es que este proyecto convierte
el análisis en un **servicio accesible mediante una API REST** , permitiendo:

● Registrar usuarios

● Publicar comentarios

● Analizar automáticamente el sentimiento de las opiniones

● Generar recomendaciones automáticas

Además, el sistema combina tres componentes de inteligencia artificial:

**Modelo propio de Machine Learning**
Se entrena un modelo sencillo que aprende a clasificar comentarios como positivos o
negativos.

**Modelo preentrenado de Hugging Face**
Se utiliza un modelo ya entrenado para enriquecer el análisis del texto y mejorar la
clasificación de sentimiento.

**Modelo de IA generativa**
Se utiliza para generar una explicación en lenguaje natural sobre si la película es
recomendable basándose en los comentarios analizados.


### 1.2 Dataset elegido

El dataset utilizado estará compuesto por comentarios de películas obtenidos desde APIs
públicas de películas como:

● IMDb

● TMDB

● o datasets públicos de reseñas de películas.

Cada registro del dataset contiene principalmente:

● Texto del comentario

● Puntuación (si existe)

● Identificador de la película

El problema que se plantea es un problema de **clasificación** , ya que el modelo debe
determinar si un comentario es:

● Positivo

● Negativo

Este dataset es adecuado para el proyecto porque permite:

**Entrenar un modelo propio de Machine Learning**
Los comentarios sirven para entrenar un modelo que aprenda a identificar el sentimiento del
texto.

**Aplicar un modelo preentrenado**
Los comentarios pueden analizarse con modelos de Hugging Face especializados en
clasificación de texto.

**Incorporar generación de lenguaje natural**
Los resultados del análisis pueden transformarse en explicaciones generadas
automáticamente para el usuario.

### 1.3 Tipo de aplicación

La aplicación se puede definir como un **analizador inteligente de opiniones con sistema
de recomendación**.

El sistema permite:

● Registrar usuarios

● Publicar comentarios sobre películas

● Analizar automáticamente el sentimiento de los comentarios

● Generar recomendaciones basadas en las opiniones acumuladas


Ejemplo de uso real:

Un usuario quiere saber si merece la pena ver una película.

1. El usuario consulta la película mediante la API.
 
2. El sistema analiza los comentarios existentes.
 
3. El modelo de Machine Learning clasifica los comentarios como positivos o negativos.

4. El modelo preentrenado refuerza el análisis de sentimiento.

5. La IA generativa crea una recomendación final.
    
Ejemplo de respuesta del sistema:

"Basándonos en 120 comentarios analizados, el 78% de los usuarios tienen opiniones
positivas sobre esta película. Destacan la historia y las actuaciones, por lo que se considera
una película recomendable."

# 2. Arquitectura y encaje de las piezas

## 2.1 Modelo propio de Machine Learning

El proyecto incluye un modelo sencillo de Machine Learning entrenado para clasificar el
sentimiento de los comentarios.

Tipo de modelo:

Clasificación de texto.

Variable objetivo:

Sentimiento del comentario:

● Positivo

● Negativo

Proceso:

1. Los comentarios se convierten en datos numéricos usando **TF-IDF** , una técnica que
    transforma palabras en vectores numéricos según su importancia en el texto.
   
2. Con estos vectores se entrena un modelo de **Logistic Regression** , que aprende
    patrones para distinguir comentarios positivos y negativos.
   
3. El modelo se evalúa utilizando métricas como:
   
● Accuracy

● Precision

● Recall

● F1-score


Una vez entrenado, el modelo se guarda en archivos .pkl para poder utilizarlo dentro de la
API sin necesidad de entrenarlo cada vez.

Dentro de la API, cada nuevo comentario se procesa con este modelo para determinar su
sentimiento.

## 2.2 Modelo preentrenado de Hugging Face

Además del modelo propio, el sistema utiliza un modelo preentrenado disponible en
Hugging Face para mejorar el análisis del texto.

En concreto se puede utilizar un modelo como:

GLiClass multitask model para clasificación de texto.
Este tipo de modelo ya ha sido entrenado con grandes cantidades de datos y puede
entender mejor el contexto del lenguaje.

El valor añadido frente al modelo propio es:

● Mayor comprensión del lenguaje natural

● Mejor detección de matices en los comentarios

● Posibilidad de clasificar textos sin necesidad de mucho entrenamiento

En el flujo del sistema, el modelo de Hugging Face puede utilizarse para validar o
enriquecer la predicción generada por el modelo propio.

## 2.3 Modelo de IA Generativa

El sistema incorpora un modelo de IA generativa para crear respuestas en lenguaje natural
que expliquen la recomendación de la película.

En lugar de devolver únicamente números o porcentajes, el sistema genera un pequeño
resumen interpretando los resultados del análisis.

Por ejemplo:

"La mayoría de los comentarios analizados son positivos. Los usuarios destacan
especialmente la trama y las actuaciones, por lo que la película se considera
recomendable."

Para controlar la calidad de la salida:

● Se limita el tamaño de las respuestas

● Se proporcionan instrucciones claras al modelo

● Se utilizan datos estructurados del análisis para generar el texto


## 2.4 Exposición mediante API REST

El sistema se expondrá mediante una **API REST desarrollada con FastAPI**.

Esta API permitirá interactuar con el sistema desde cualquier aplicación externa.

### Framework utilizado

FastAPI

Permite crear APIs rápidas, documentadas automáticamente y fáciles de integrar con
modelos de Machine Learning.

# Endpoints principales

## 1. Crear usuario

POST /users

Permite registrar un nuevo usuario en el sistema.

Entrada:

{

"username": "juan1",

"email": "juan1@email.com"

}

Salida:

{

"id": 1,

"username": "juan1",

"email": "juan1@email.com"

}

## 2. Listar usuarios

GET /users

Devuelve la lista de usuarios registrados.

Salida:

[

{

"id": 1,

"username": "juan1"

},

{

"id": 2,

"username": "vito"

}

]

## 3. Crear comentario

POST /comments

Permite que un usuario escriba un comentario sobre una película.

Entrada:

{

"user_id": 1,

"movie_id": "tt0111161",

"comment": "La película es increíble, muy recomendable."

}
Proceso interno:

1. Se guarda el comentario.

2. Se analiza el sentimiento usando el modelo de Machine Learning.

3. Se guarda la clasificación (positivo o negativo).

Salida:

{

"comment_id": 15,

"sentiment": "positive"

}

## 4. Obtener comentarios de una película

GET /movies/{movie_id}/comments

Devuelve todos los comentarios asociados a una película.

Salida:

[

{

"user": "juan1",

"comment": "Muy buena película",

"sentiment": "positive"

}

]


## 5. Obtener recomendación de película

GET /movies/{movie_id}/recommendation

Este endpoint analiza todos los comentarios de una película y genera una recomendación.

Proceso:

1. Se cuentan los comentarios positivos y negativos.

2. Se calcula el porcentaje de opiniones positivas.

3. Se genera un resumen utilizando el modelo de IA generativa.

Salida:

{

"movie_id": "tt0111161",

"positive_percentage": 82,

"recommendation": "La mayoría de los comentarios son positivos. Los usuarios destacan la
historia y los personajes, por lo que se considera una película recomendable."

}

# Validaciones y manejo de errores

La API incluye diferentes validaciones para garantizar el correcto funcionamiento:

● Verificación de usuarios existentes antes de crear comentarios.

● Validación de formato en los datos de entrada.

● Manejo de errores si una película no tiene comentarios.

● Respuestas con códigos HTTP adecuados.

Ejemplos:

400 → Datos incorrectos

404 → Recurso no encontrado

500 → Error interno del servidor

