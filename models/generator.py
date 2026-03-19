from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="datificate/gpt2-small-spanish"
)

def generate_description(data):

    prompt = f"""
    Escribe una descripción corta para vender esta vivienda:

    Superficie: {data["area"]} metros cuadrados
    Habitaciones: {data["bedrooms"]}
    Baños: {data["bathrooms"]}
    Plantas: {data["stories"]}
    Parking: {data["parking"]}

    Descripción:
    """

    result = generator(prompt, max_length=120, num_return_sequences=1)

    return result[0]["generated_text"]