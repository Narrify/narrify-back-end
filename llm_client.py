import openai
from openai import OpenAI

client = OpenAI(api_key="Api_Key")


def send_to_llm(prompt, model="gpt-4o-mini"):
    try:
        response = client.chat.completions.create(model = model,
        messages = [
            {"role": "system", "content": "You are a dialog and story generator for videogames."},
            {"role": "user", "content": prompt}
        ],
        max_tokens = 750,
        n = 1,
        temperature = 0.7)
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None
