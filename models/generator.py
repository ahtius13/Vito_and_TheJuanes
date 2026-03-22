from transformers import pipeline, set_seed

generator = pipeline(
    "text-generation",
    model="mrm8488/spanish-gpt2"
)

set_seed(42)


def generate_description(data: dict, price: int):

    base_text = f"""
    Vivienda de {data['bedrooms']} habitaciones y {data['bathrooms']} baños,
    con una superficie de {data['area']} m2.

    Cuenta con {data['stories']} plantas y {data['parking']} plazas de aparcamiento.

    """

    extras = []

    if data["airconditioning"]:
        extras.append("aire acondicionado")
    if data["basement"]:
        extras.append("sótano")
    if data["guestroom"]:
        extras.append("habitación de invitados")
    if data["prefarea"]:
        extras.append("ubicación en zona preferente")

    if extras:
        base_text += "Incluye " + ", ".join(extras) + ". "

    base_text += f"Precio estimado: {price} euros.\nDescripción:"

    result = generator(
        base_text,
        max_length=120,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7
    )

    generated = result[0]["generated_text"]

    description = generated.replace(base_text, "").strip()

    return description