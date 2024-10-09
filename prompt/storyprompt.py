
def generateStoryPrompt(story_json):
  
  prompt = f"""Generate a story for a video game based on the following specifications:

Settings:

Size: {story_json['settings']['size']}
And the following attributes:

"""
  
  for attribute in story_json['settings']['attributes']:
    prompt += f"{attribute['name']}: {attribute['value']}\n"

  prompt += f"""\nCharacters:

"""
  
  for character in story_json['characters']:
    prompt += f"\n{character['name']}:\n"
    for attribute in character['attributes']:
      prompt += f"{attribute['name']}: {attribute['value']}\n"

  prompt += f"""\nThe title of the game is {story_json['title']}. Output an engaging and efficient story that reflects the settings and character traits. Don't put notes, use plain text not markdown, use only the initials and the response has minimal tokens."""

  return prompt


generateStoryPrompt(json_response)