"""
TODO
"""


def generate_story_prompt(json):
    """
    TODO
    """

    prompt = f"Story size: {json['settings']['size']}. Attributes: "
    prompt += ", ".join([f"{atr['name']}: {atr['value']}" for atr in json['settings']['attributes']])
    prompt += ". Characters: "

    for character in json['characters']:
        char_attrs = ", ".join([f"{atr['name']}: {atr['value']}" for atr in character['attributes']])
        prompt += f"{character['name']} ({character['name'][0]}): {char_attrs}. "

    prompt += "Generate a engaging story. Use character initials. Use plain text. No notes."

    return prompt
