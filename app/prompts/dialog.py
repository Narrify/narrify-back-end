def generar_prompt_dialogo_responsive(json_data):
    """
    Genera un prompt basado en los datos proporcionados en el JSON, que es adaptable a variaciones como el número de escenas y personajes.
    El primer personaje en la lista será el personaje principal.
    """
    # Extraer los datos de la historia y configuración
    story = json_data.get('story', 'Una historia épica en un planeta distante.')
    number_of_scenes = json_data['settings'].get('number_of_scenes', 4)
    characters = json_data.get('characters', [])

    if not characters:
        raise ValueError("No se encontraron personajes en la entrada JSON.")

    # El primer personaje es el personaje principal
    personaje_principal = characters[0]['name']
    atributos_principal = ", ".join([f"{attr['name']}: {attr['value']}" for attr in characters[0].get('attributes', [])])

    # Los personajes restantes son secundarios
    personajes_secundarios = characters[1:]  # Los demás personajes son secundarios
    formatted_characters = []
    for character in personajes_secundarios:
        name = character.get('name', 'Personaje sin nombre')
        attributes = ", ".join([f"{attr['name']}: {attr['value']}" for attr in character.get('attributes', [])])
        formatted_characters.append(f"{name} ({name[0] if name else '?'})" + (f": {attributes}" if attributes else ""))

    # Unir personajes secundarios en una cadena
    characters_str = "; ".join(formatted_characters) if formatted_characters else "No supporting characters available."

    # Construcción del prompt adaptable
    prompt = (
        f"Story: {story}. "
        f"The main character is {personaje_principal} ({personaje_principal[0] if personaje_principal else '?'}): {atributos_principal}. "
        f"Supporting characters: {characters_str}. "
        f"""
        Create a set of dialogues where {personaje_principal} interacts with other characters.
        Each dialogue should provide the player with 2 or more options, and each option should lead to the next part of the dialogue.
        Format the output in the following structure:
        {{
            "dialogues": [
                {{
                    "id": 1,
                    "character": "{personaje_principal}",
                    "text": "Texto inicial del diálogo del personaje principal.",
                    "options": [
                        {{ "text": "Primera opción del jugador", "next": 2 }},
                        {{ "text": "Segunda opción del jugador", "next": 3 }}
                    ]
                }},
                {{
                    "id": 2,
                    "character": "Nombre del personaje",
                    "text": "Texto de la respuesta a la primera opción."
                }},
                {{
                    "id": 3,
                    "character": "Nombre del personaje",
                    "text": "Texto de la respuesta a la segunda opción."
                }}
            ]
        }}
        Make sure the dialogues follow a logical sequence, and each option leads to a different outcome.
        """
    )

    return prompt
