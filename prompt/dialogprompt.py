
def generateDialogPrompt(dialog_json):
  
  prompt = f"""Generate a dialog for a video game based on the following specifications:

Story: {dialog_json['story']}

Settings:

Scenes: {dialog_json['settings']['number_of_scenes']}
Characters: {dialog_json['settings']['number_of_characters']}

Characters:
"""
  
  for character in dialog_json['characters']:
    prompt += f"\n{character['name']} ({character['name'][0]}) has the following attributes: \n"
    for attribute in character['attributes']:
      prompt += f"{attribute['name']}: {attribute['value']}\n"

  prompt = prompt + f"""
Output an engaging and efficient dialog that reflects the story development and character traits. Don't put notes,  use plain text not markdown, use only the initials and the response has minimal tokens.
"""
  
  return prompt


generateDialogPrompt(json_response)