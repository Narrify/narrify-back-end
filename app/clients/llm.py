"""
TODO
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()

API_KEY = os.getenv("API_KEY_OPENAI")

if API_KEY is None:
    print("Error: La variable API_KEY_OPENAI no se ha cargado.")


client = OpenAI(api_key=API_KEY)


async def make_request(prompt: dict, model: str = "gpt-4o-mini"):
    """
    TODO
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a dialog and story generator for videogames."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=750,
            n=1,
            temperature=0.7
        )
        response=response.choices[0].message.content


        return response
    except OpenAIError as error:
        print(f'ocurrio un error en la llamada a OpenAI: ${error}')
        return None


def format_dialog_to_json(dialog_text):
    """
    Convierte un texto con formato 'Scene X: A: line' en un formato JSON sin agregar 'response' extra.
    """
    # Reemplazar las comillas escapadas y los saltos de línea
    dialog_text = dialog_text.replace('\\"', '"').replace("\\n", " ").strip()

    # Separar las escenas usando "Scene X" como separador
    scenes = dialog_text.split('Scene ')
    scenes_data = []

    for scene in scenes:
        if scene.strip():  # Asegurarse de que no haya escenas vacías
            # Dividir en ID de escena y los diálogos
            scene_parts = scene.strip().split(' ', 1)  # Separa el número de escena del resto
            if len(scene_parts) > 1:
                scene_id = scene_parts[0].strip()  # Obtiene el ID de la escena (por ejemplo, 1, 2, 3, etc.)
                scene_dialog = scene_parts[1]  # Obtiene el diálogo de la escena

                # Separar los diálogos por las comas, pero asegurarse de no dividir dentro de una línea de diálogo
                scene_lines = scene_dialog.split("', '")
                dialog = []

                # Procesar cada línea de diálogo
                for line in scene_lines:
                    line = line.strip("'").strip()  # Eliminar comillas innecesarias
                    if ": " in line:
                        speaker, line_text = line.split(": ", 1)
                        dialog.append({"speaker": speaker.strip(), "line": line_text.strip()})

                # Añadir los datos de la escena al resultado final
                scenes_data.append({"scene_id": int(scene_id), "dialog": dialog})

    return scenes_data

