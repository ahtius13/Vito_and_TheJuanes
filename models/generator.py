from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="microsoft/phi-2"
)

def generate_description(house, price):

    prompt = f"""
    Eres un experto inmobiliario.

    Tu tarea es escribir una descripción de una vivienda usando solo los datos dados.

    Reglas:
    - No inventar información
    - No añadir características no mencionadas
    - No cambiar los números
    - Redactar de forma atractiva para venta
    - Máximo 120 palabras

    Datos:
    - Superficie: {house.area} m²
    - Habitaciones: {house.bedrooms}
    - Baños: {house.bathrooms}
    - Plantas: {house.stories}
    - Parking: {house.parking}
    - Aire acondicionado: {"Sí" if house.airconditioning else "No"}
    - Sótano: {"Sí" if house.basement else "No"}
    - Habitación invitados: {"Sí" if house.guestroom else "No"}
    - Zona preferente: {"Sí" if house.prefarea else "No"}
    - Precio: {price} euros

    Descripción:
    """

    result = generator(
        prompt,
        max_new_tokens=120,
        temperature=0.3,
        top_p=0.9,
        repetition_penalty=1.2,
        do_sample=True
    )

    text = result[0]["generated_text"]

    # Limpiar prompt para evitar repeticiones
    description = text.replace(prompt, "").strip()

    return description