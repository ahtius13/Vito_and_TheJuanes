# Sistema Inteligente de Estimación de Precios de Viviendas

# 1. Definición del proyecto

## 1.1 Propósito del sistema

El objetivo de este proyecto es desarrollar una aplicación que permita estimar el precio de
una vivienda basándose en sus características mediante técnicas de Machine Learning,
además de generar automáticamente una descripción atractiva para su venta utilizando un
modelo de Inteligencia Artificial generativa.
En el sector inmobiliario, el precio de una vivienda depende de múltiples factores como el
tamaño, el número de habitaciones, la ubicación, el estado de la vivienda o los servicios
disponibles. Analizar manualmente estos factores para estimar un precio adecuado puede
ser complejo y subjetivo.
Este sistema automatiza este proceso mediante el uso de datos históricos de viviendas,
permitiendo estimar el precio de nuevas viviendas introducidas por el usuario.
El sistema está pensado para:
● Personas que quieren estimar el precio de una vivienda antes de venderla.
● Aplicaciones inmobiliarias que necesiten un sistema automático de valoración de
propiedades.
● Proyectos educativos que quieran demostrar el uso combinado de análisis de datos,
machine learning, modelos generativos y APIs REST.
El valor añadido frente a un análisis en notebook es que el sistema se implementa como
una API REST, permitiendo su integración en otras aplicaciones.
El sistema combina dos componentes principales de inteligencia artificial:

### Modelo propio de Machine Learning

Se entrena un modelo de regresión que analiza las características de las viviendas para
aprender la relación entre estas variables y el precio.
Este modelo permite estimar el precio de nuevas viviendas introduciendo sus
características.

### Modelo de IA generativa


El sistema utiliza un modelo generativo para crear automáticamente descripciones
atractivas de las viviendas a partir de sus características.
Esto permite transformar datos estructurados en contenido comercial útil para anuncios
inmobiliarios.

## 1.2 Dataset elegido

El dataset utilizado es:
Housing Prices Dataset disponible en Kaggle:
https://www.kaggle.com/datasets/yasserh/housing-prices-dataset
Este dataset contiene información sobre viviendas junto con sus características y su precio
final.
Las variables utilizadas en el proyecto son:
● price (variable objetivo)
● area
● bedrooms
● bathrooms
● stories
● mainroad
● guestroom
● basement
● hotwaterheating
● airconditioning
● parking
● prefarea
● furnishingstatus
El problema es de tipo regresión, ya que se busca predecir un valor numérico (el precio).

### Preprocesamiento de datos

El dataset contiene variables categóricas que han sido transformadas a valores numéricos
para poder ser utilizadas por el modelo:
Variables binarias:
● yes → 1
● no → 0
Columnas afectadas:


● mainroad
● guestroom
● basement
● hotwaterheating
● airconditioning
● prefarea
Variable categórica:
● furnishingstatus
Transformación:
● furnished → 2
● semi-furnished → 1
● unfurnished → 0
Este proceso permite que el modelo de Machine Learning pueda interpretar correctamente
todas las variables.

## 1.3 Tipo de aplicación

La aplicación es un servicio predictivo con generación automática de contenido.
El sistema permite:
● introducir las características de una vivienda
● estimar automáticamente su precio
● generar una descripción atractiva
● almacenar la información para su consulta

### Ejemplo de uso real

Un usuario introduce los datos de una vivienda:
● superficie
● número de habitaciones
● número de baños
● características adicionales (aire acondicionado, sótano, etc.)
El sistema:

1. Analiza los datos con el modelo de Machine Learning
2. Calcula el precio estimado
3. Genera una descripción atractiva


4. Guarda la información en un archivo JSON
Ejemplo de respuesta:
"Se estima que el precio de la vivienda es de 12.300.000. La propiedad destaca por su
amplitud, múltiples habitaciones y su ubicación en una zona preferente. Ideal para familias
que buscan comodidad y espacio."

# 2. Arquitectura y encaje de las piezas

## 2.1 Modelo de Machine Learning

Tipo de modelo:
Regresión (Random Forest Regressor).
Variable objetivo:
● price
Variables de entrada:
● area
● bedrooms
● bathrooms
● stories
● mainroad
● guestroom
● basement
● hotwaterheating
● airconditioning
● parking
● prefarea
● furnishingstatus
Proceso:

1. Carga del dataset
2. Conversión de variables categóricas a numéricas
3. Entrenamiento del modelo
4. Guardado del modelo en archivo .pkl
El modelo se guarda y posteriormente es cargado por la API para realizar predicciones.


## 2.2 Modelo de IA Generativa

Se utiliza un modelo de generación de texto para crear descripciones de viviendas.
El modelo recibe como entrada:
● superficie
● número de habitaciones
● número de baños
● características adicionales
Y genera una descripción como:
"Amplia vivienda con varias habitaciones, ubicada en una zona preferente y equipada con
todas las comodidades necesarias. Ideal para familias que buscan espacio y confort."
Para mejorar la calidad de salida:
● se estructuran los datos en un prompt claro
● se limita la longitud del texto
● se guía al modelo con instrucciones

## 2.3 Persistencia de datos

Las viviendas introducidas por los usuarios se almacenan en un archivo JSON:
data/houses.json
Cada registro incluye:
● características de la vivienda
● precio estimado
● descripción generada

## 2.4 Exposición mediante API REST

El sistema se expone mediante una API REST desarrollada con FastAPI.

# Endpoints


## 1. Crear ficha de vivienda

Endpoint:
POST /houses
Descripción:
Permite registrar una vivienda introduciendo sus características.
El sistema automáticamente:
● predice el precio con Machine Learning
● genera una descripción con IA generativa
● guarda los datos en un JSON

### Datos de entrada

#### {

"area": 7420,
"bedrooms": 4,
"bathrooms": 2,
"stories": 3,
"mainroad": "yes",
"guestroom": "no",
"basement": "no",
"hotwaterheating": "no",
"airconditioning": "yes",
"parking": 2,
"prefarea": "yes",
"furnishingstatus": "furnished"
}


### Respuesta

#### {

"area": 7420,
"bedrooms": 4,
"bathrooms": 2,
"stories": 3,
"mainroad": "yes",
"guestroom": "no",
"basement": "no",
"hotwaterheating": "no",
"airconditioning": "yes",
"parking": 2,
"prefarea": "yes",
"furnishingstatus": "furnished",
"estimated_price": 12300000,
"description": "Amplia vivienda con múltiples habitaciones..."
}

## 2. Obtener viviendas

Endpoint:
GET /houses
Descripción:
Devuelve todas las viviendas almacenadas en el sistema.

### Respuesta


#### [

#### {

"area": 7420,
"bedrooms": 4,
"bathrooms": 2,
"stories": 3,
"estimated_price": 12300000,
"description": "Amplia vivienda..."
}
]

# Flujo del sistema

1. El usuario envía datos mediante POST /houses
2. El modelo de Machine Learning calcula el precio
3. El modelo generativo crea la descripción
4. Se guarda la información en JSON
5. Se puede consultar con GET /houses

# Validaciones y errores

El sistema incluye:
● validación de tipos de datos
● control de valores inválidos
● validación de campos obligatorios
Códigos HTTP:
● 400 → datos incorrectos
● 404 → recurso no encontrado
● 500 → error interno