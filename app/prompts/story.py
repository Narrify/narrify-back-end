"""
TODO
"""


def generate_story_prompt(json):
    """
    TODO
    """

    prompt = f"Story size: {json['settings']['size']}. Attributes: "
    prompt += ", ".join([f"{x['name']}: {x['value']}" for x in json['settings']['attributes']])
    prompt += ". Characters: "

    for character in json['characters']:
        char_attrs = ", ".join([f"{x['name']}: {x['value']}" for x in character['attributes']])
        prompt += f"{character['name']} ({character['name'][0]}): {char_attrs}. "

    prompt += "Generate a engaging story. Use character initials. Use plain text. No notes.Return JSON"

    return prompt


"""json_request={
  "title": "Echoes of Destiny",
  "settings": {
    "size": "short",
    "attributes": [
      {
        "name": "environment",
        "value": "lush forests and towering mountains"
      },
      {
        "name": "time period",
        "value": "futuristic with ancient ruins"
      }
    ]
  },
  "characters": [
    {
      "name": "Alex",
      "attributes": [
        {
          "name": "age",
          "value": "18"
        },
        {
          "name": "ability",
          "value": "telekinesis"
        }
      ]
    },
    {
      "name": "Luna",
      "attributes": [
        {
          "name": "age",
          "value": "20"
        },
        {
          "name": "ability",
          "value": "illusion"
        }
      ]
    },
    {
      "name": "Draco",
      "attributes": [
        {
          "name": "age",
          "value": "35"
        },
        {
          "name": "ability",
          "value": "fire"
        }
      ]
    }
  ],
  "plots": 1,
"endings":1}

response=generate_story_prompt(json_request)
print(response)"""
