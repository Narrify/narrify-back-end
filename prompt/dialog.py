"""
TODO
"""


def generate_dialog_prompt(json):
    """
    TODO
    """

    prompt = f"Story: {json['story']}. Scenes: {json['settings']['number_of_scenes']}, Characters: {json['settings']['number_of_characters']}. "
    prompt += "Characters: "

    for character in json['characters']:
        char_attrs = ", ".join([f"{attr['name']}: {attr['value']}" for attr in character['attributes']])
        prompt += f"{character['name']} ({character['name'][0]}): {char_attrs}. "

    prompt += "Generate a engaging dialog. Use character initials. Use plain text. No notes."

    return prompt
