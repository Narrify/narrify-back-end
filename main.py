"""
/TODO
"""

import uvicorn

from fastapi import FastAPI

from models.dialog import DialogRequest
from models.story import StoryRequest

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
    """
    /TODO

    :param request:
    :return:
    """

    return {
        "title": request.title,
        "settings": request.settings,
        "characters": request.characters,
        "plots": request.plots,
        "endings": request.endings
    }


@app.post('/generate/dialog')
async def generate_dialog(request: DialogRequest):
    """
    /TODO

    :param request:
    :return:
    """

    return {
        "story": request.story,
        "settings": request.settings,
        "characters": request.characters
    }


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1")
