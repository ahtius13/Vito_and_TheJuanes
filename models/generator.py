from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="mrm8488/spanish-gpt2"
)

def generate_description(house, price):
    """
    Genera una descripción positiva combinando plantilla + IA
    """
    # Texto base
    base_description = (
        f"Se ofrece en venta una excelente vivienda de {house.area} m², "
        f"con {house.bedrooms} habitaciones y {house.bathrooms} baños, "
        f"distribuida en {house.stories} plantas. "
    )

    extras = []

    if house.airconditioning:
        extras.append("aire acondicionado")
    if house.basement:
        extras.append("sótano")
    if house.guestroom:
        extras.append("habitación de invitados")
    if house.mainroad:
        extras.append("acceso directo a vía principal")
    if house.prefarea:
        extras.append("ubicación en zona preferente")
    if house.hotwaterheating:
        extras.append("sistema de agua caliente")
    if house.parking > 0:
        extras.append(f"{house.parking} plazas de aparcamiento")

    if extras:
        base_description += "Cuenta con " + ", ".join(extras) + ". "

    base_description += (
        f"Su precio estimado es de {price} euros. "
        f"Es una propiedad ideal para quienes buscan comodidad, espacio y buena ubicación. "
    )

    # Prompt para IA
    prompt = (
        base_description +
        "Descripción adicional:"
    )

    result = generator(
        prompt,
        max_length=180,
        num_return_sequences=1,
        temperature=0.6,   # para que se ciña mas o menos a las reglas
        top_p=0.9,
        repetition_penalty=1.2,  # evita repeticiones
        do_sample=True
    )

    generated_text = result[0]["generated_text"]

    # Limpia el prompt para evitar repeticiones 
    extra_text = generated_text.replace(prompt, "").strip()

    # Limpiar cortes raros
    if "." in extra_text:
        extra_text = extra_text.split(".")[0] + "."

    # Combinar base + IA
    final_description = base_description + extra_text

    return final_description.strip()