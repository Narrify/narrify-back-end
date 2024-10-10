"""
TODO
"""

from fastapi import APIRouter

from src.models.dialog import DialogRequest
from src.models.story import StoryRequest

from src.prompts.dialog import generate_dialog_prompt
from src.prompts.story import generate_story_prompt

from src.clients.llm import make_request

router = APIRouter()


@router.post("/story")
async def generate_story(request: StoryRequest):
    """
    TODO
    """

    json = request.model_dump()
    prompt = generate_story_prompt(json)

    response = await make_request(prompt)

    return {
        "response": response
    }


@router.post("/dialog")
async def generate_dialog(request: DialogRequest):
    """
    TODO
    """

    json = request.model_dump()
    prompt = generate_dialog_prompt(json)

    response = await make_request(prompt)

    return {
        "response": response
    }
