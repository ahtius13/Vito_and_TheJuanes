# Sistema Inteligente de Estimación de Precios de Viviendas
# 1. Definición del proyecto

## 1.1 Propósito del sistema

El objetivo de este proyecto es desarrollar una aplicación que permita estimar el precio de
una vivienda basándose en sus características mediante técnicas de Machine Learning,
además de generar automáticamente una descripción atractiva para su venta utilizando un
modelo de Inteligencia Artificial generativa.

En el sector inmobiliario, el precio de una vivienda depende de múltiples factores como el
tamaño, el número de habitaciones, la ubicación, la calidad de la construcción o el estado
de la vivienda. Analizar manualmente estos factores para estimar un precio adecuado
puede ser complejo y subjetivo.

Este sistema pretende automatizar ese proceso mediante el análisis de datos históricos de
viviendas, permitiendo estimar un precio aproximado para nuevas viviendas introducidas por
el usuario.

El sistema está pensado para:

```
● Personas que quieren estimar el precio de una vivienda antes de venderla.
● Aplicaciones inmobiliarias que necesiten un sistema automático de valoración de
propiedades.
● Proyectos educativos que quieran demostrar el uso combinado de análisis de datos,
machine learning, modelos generativos y APIs REST.
```
El valor añadido frente a realizar un análisis únicamente en un notebook es que el sistema
se implementa como un **servicio accesible mediante una API REST** , lo que permite
integrarlo fácilmente en otras aplicaciones.

Además, el proyecto combina tres componentes principales de inteligencia artificial:

### Modelo propio de Machine Learning

Se entrena un modelo que analiza las características de las viviendas para identificar
patrones que expliquen el precio de las mismas.

Este modelo permite estimar el precio de nuevas viviendas introduciendo sus
características.


### Modelo preentrenado de análisis de datos

El sistema utiliza librerías de Machine Learning que permiten analizar automáticamente la
importancia de cada variable en el precio de las viviendas.

Esto permite identificar factores clave como:

```
● superficie de la vivienda
● número de habitaciones
● calidad de construcción
● ubicación
```
### Modelo de IA generativa

El sistema incorpora un modelo de generación de texto que crea automáticamente una
descripción atractiva para vender la vivienda.

En lugar de mostrar únicamente datos técnicos, el sistema genera textos similares a los que
se utilizan en anuncios inmobiliarios.

Por ejemplo:

"Amplia vivienda de tres habitaciones situada en una zona tranquila. Destaca por su
luminosidad, su espacioso salón y su moderna cocina equipada. Ideal para familias que
buscan comodidad y buena conexión con servicios cercanos."

Esto permite transformar datos estructurados en contenido útil para plataformas
inmobiliarias.

# 1.2 Dataset elegido

El dataset utilizado para este proyecto es el siguiente:

Housing Prices Dataset disponible en Kaggle.

Fuente del dataset:

https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

Este dataset contiene información sobre diferentes viviendas junto con sus características y
el precio final de venta.

Entre las variables principales del dataset se encuentran:

```
● superficie de la vivienda
● número de habitaciones
```

```
● número de baños
● calidad de la construcción
● año de construcción
● estado de la vivienda
● superficie del terreno
● otras características estructurales
```
Cada registro del dataset representa una vivienda con sus características y su precio de
mercado.

El tipo de problema que se aborda es un problema de **regresión** , ya que el objetivo del
modelo es predecir un valor numérico (el precio de la vivienda) a partir de diferentes
variables.

Este dataset es adecuado para el proyecto por varias razones.

### Entrenamiento de un modelo propio de Machine Learning

El dataset contiene suficientes ejemplos de viviendas con sus precios reales, lo que permite
entrenar un modelo que aprenda la relación entre las características de una vivienda y su
precio.

### Análisis de importancia de variables

Las múltiples columnas del dataset permiten estudiar qué características influyen más en el
precio de las viviendas.

Por ejemplo:

```
● tamaño de la vivienda
● número de habitaciones
● calidad de construcción
```
Esto permite comprender mejor el comportamiento del mercado inmobiliario.

### Uso de generación de lenguaje natural

Las características de las viviendas pueden utilizarse como entrada para generar
descripciones atractivas que simulen anuncios inmobiliarios reales.

# 1.3 Tipo de aplicación

La aplicación se puede definir como un **servicio predictivo con generación automática
de contenido**.

El sistema permite:


```
● introducir las características de una vivienda
● estimar automáticamente su precio
● generar una descripción atractiva para su venta
```
Este sistema puede integrarse fácilmente en plataformas inmobiliarias o aplicaciones de
gestión de propiedades.

### Ejemplo de uso real

Un usuario quiere vender su vivienda y desea conocer un precio aproximado de mercado.

El proceso sería el siguiente:

1. El usuario introduce las características de la vivienda mediante la API.

Por ejemplo:

```
● superficie
● número de habitaciones
● número de baños
● calidad de construcción
```
2. La API envía estos datos al modelo de Machine Learning.
3. El modelo analiza las variables y estima el precio de la vivienda basándose en
    patrones aprendidos del dataset.
4. El modelo de IA generativa utiliza las características de la vivienda para generar una
    descripción atractiva.
5. El sistema devuelve una respuesta con:
● el precio estimado
● un resumen de los factores que influyen en el precio
● una descripción comercial de la vivienda

Ejemplo de respuesta:

"Según las características introducidas, el precio estimado de la vivienda es de 245.000€.
La superficie y la calidad de construcción son los factores que más influyen en la valoración.
Se trata de una vivienda espaciosa con excelentes acabados y múltiples habitaciones, ideal
para familias que buscan comodidad y funcionalidad."

# 2. Arquitectura y encaje de las piezas

## 2.1 Modelo propio de Machine Learning

El proyecto incluye un modelo de Machine Learning entrenado para estimar el precio de las
viviendas.


Tipo de modelo:

Regresión.

Variable objetivo:

Precio de la vivienda.

Proceso de entrenamiento:

Primero se realiza un proceso de preparación de los datos que incluye:

```
● limpieza de datos
● tratamiento de valores faltantes
● selección de variables relevantes
● normalización de datos si es necesario
```
Después de preparar el dataset, se entrena un modelo de regresión que aprende la relación
entre las características de las viviendas y su precio.

Algunos modelos que pueden utilizarse son:

```
● Linear Regression
● Random Forest Regressor
● Gradient Boosting
```
El modelo se evalúa utilizando métricas de regresión como:

```
● Mean Absolute Error (MAE)
● Mean Squared Error (MSE)
● R² Score
```
Una vez entrenado, el modelo se guarda en archivos .pkl para poder utilizarlo
posteriormente dentro de la API.

Cuando el usuario introduce las características de una vivienda, la API carga el modelo y
calcula el precio estimado.

## 2.2 Análisis de importancia de variables

Además de predecir el precio, el sistema puede analizar qué variables tienen mayor impacto
en el valor de una vivienda.

Esto permite interpretar el modelo y comprender qué factores influyen más en la predicción.

Por ejemplo, el sistema puede identificar que los factores más importantes son:

```
● superficie de la vivienda
```

```
● número de habitaciones
● calidad de la construcción
● tamaño del terreno
```
Este análisis permite ofrecer explicaciones más claras al usuario sobre el resultado de la
predicción.

## 2.3 Modelo de IA Generativa

El sistema incorpora un modelo de generación de texto que crea descripciones comerciales
de las viviendas basándose en sus características.

El modelo recibe como entrada:

```
● superficie
● número de habitaciones
● número de baños
● calidad de construcción
● otras características relevantes
```
A partir de estos datos, el modelo genera una descripción similar a las utilizadas en
anuncios inmobiliarios.

Ejemplo:

"Vivienda moderna y luminosa con amplios espacios interiores. Cuenta con varias
habitaciones y baños bien distribuidos, además de una excelente calidad de construcción.
Perfecta para quienes buscan confort y funcionalidad en una zona tranquila."

Para controlar la calidad de la salida generada se aplican varias medidas:

```
● limitar la longitud del texto generado
● estructurar los datos de entrada
● utilizar prompts claros para guiar la generación del texto
```
# 2.4 Exposición mediante API REST

El sistema se expondrá mediante una API REST desarrollada con **FastAPI** , que permite
crear servicios web rápidos y bien documentados en Python.

Esta API permitirá a otras aplicaciones enviar datos de viviendas y recibir estimaciones de
precio junto con descripciones generadas automáticamente.


# Endpoints principales

La API permite registrar viviendas introduciendo sus características principales.
Cuando una vivienda es registrada, el sistema automáticamente:

```
● analiza las características de la vivienda
```
```
● estima su precio utilizando un modelo de Machine Learning
```
```
● genera una descripción atractiva utilizando un modelo de IA generativa
```
```
● guarda la información completa en un archivo JSON
```
Posteriormente, los usuarios pueden consultar las viviendas registradas mediante un
endpoint de consulta.

# 1. Registrar una vivienda

## Endpoint

POST /houses

## Descripción

Este endpoint permite registrar una nueva vivienda en el sistema proporcionando sus
características principales.

Cuando el usuario envía los datos de una vivienda, el sistema realiza automáticamente los
siguientes procesos:

1. **Predicción del precio**
    Un modelo de Machine Learning analiza las características de la vivienda y estima
    su precio basándose en los patrones aprendidos del dataset de viviendas utilizado
    durante el entrenamiento.
2. **Generación de descripción**
    Un modelo de IA generativa genera automáticamente una descripción atractiva para
    la vivienda, similar a las utilizadas en anuncios inmobiliarios.
3. **Almacenamiento de la vivienda**
    La vivienda se guarda en un archivo JSON junto con:


```
○ las características introducidas
```
```
○ el precio estimado
```
```
○ la descripción generada
```
Esto permite construir un registro sencillo de viviendas analizadas por el sistema.

## Datos de entrada

El usuario debe proporcionar las características principales de la vivienda.

Ejemplo:

{

"area": 2000,

"bedrooms": 4,

"bathrooms": 3,

"stories": 2,

"parking": 1

}

```
Campo Descripción
```
```
area Superficie de la vivienda
```
```
bedrooms Número de habitaciones
```
```
bathroom
s
```
```
Número de baños
```

```
stories Número de plantas
```
```
parking Número de plazas de
aparcamiento
```
## Respuesta

La API devuelve la información completa de la vivienda registrada.

Ejemplo:

{

"area": 2000,

"bedrooms": 4,

"bathrooms": 3,

"stories": 2,

"parking": 1,

"price": 285000,

"description": "Spacious family home with modern amenities and multiple bedrooms,
perfect for comfortable living."

}

# 2. Obtener viviendas registradas

## Endpoint

GET /houses

## Descripción

Este endpoint permite consultar todas las viviendas que han sido registradas en el sistema.

La información se obtiene desde el archivo JSON donde se almacenan las viviendas
registradas.


Cada vivienda incluye:

```
● las características introducidas por el usuario
```
```
● el precio estimado generado por el modelo de Machine Learning
```
```
● la descripción generada por el modelo de IA generativa
```
Este endpoint permite visualizar fácilmente todas las propiedades analizadas por el sistema.

## Respuesta

La API devuelve una lista de viviendas registradas.

Ejemplo:

[

{

"area": 2000,

"bedrooms": 4,

"bathrooms": 3,

"stories": 2,

"parking": 1,

"price": 285000,

"description": "Spacious family home with modern amenities and multiple bedrooms."

},

{

"area": 1500,

"bedrooms": 3,

"bathrooms": 2,

"stories": 1,

"parking": 1,


"price": 210000,

"description": "Cozy and comfortable home ideal for small families."

}

]

# Flujo de funcionamiento del sistema

El funcionamiento general del sistema es el siguiente:

1. El usuario introduce las características de una vivienda mediante el endpoint POST
    /houses.
2. El modelo de **Machine Learning** analiza los datos y estima el precio de la vivienda.
3. El modelo de **IA generativa** crea automáticamente una descripción atractiva.
4. La vivienda se guarda en un archivo JSON junto con el precio estimado y la
    descripción generada.
5. Las viviendas registradas pueden consultarse posteriormente mediante el endpoint
    GET /houses.

# Validaciones y manejo de errores

La API incluye diferentes validaciones para garantizar el correcto funcionamiento.

Entre ellas:

```
● verificación de que las variables numéricas tengan valores válidos
```
```
● control de valores faltantes
```
```
● validación del formato de entrada
```
Los códigos HTTP utilizados incluyen:

400 → datos incorrectos
404 → recurso no encontrado
500 → error interno del servidor