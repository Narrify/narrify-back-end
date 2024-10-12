"""
TODO
"""

import os

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

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

        return response.choices[0].message.content
    except OpenAIError as error:
        print(error)
        return None
