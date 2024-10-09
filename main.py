"""
/TODO
"""

import uvicorn

from fastapi import FastAPI

from models.dialog import DialogRequest
from models.story import StoryRequest

from prompt.dialogprompt import generateDialogPrompt
from prompt.storyprompt import generateStoryPrompt
from llm_client import send_to_llm

import json

app = FastAPI()


@app.get("/")
async def main():
    """
    /TODO

    :return:
    """

    return "Hello World"


@app.post('/generate/story')
async def generate_story(request: StoryRequest):
    
    request_json = request.dict()

    story_prompt = generateStoryPrompt(request_json)
    
    response = send_to_llm(story_prompt)

    return {
        "llm_response": response
    }


@app.post('/generate/dialog')
async def generate_dialog(request: DialogRequest):

    request_json = request.dict()

    story_prompt = generateDialogPrompt(request_json)

    response = send_to_llm(story_prompt)
    print(response)

    return {
        "llm_response": response
    }


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1")
