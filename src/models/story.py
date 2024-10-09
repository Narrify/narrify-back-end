"""
TODO
"""

from typing import List
from pydantic import BaseModel

from src.models.shared import Attribute, Character


class StorySettings(BaseModel):
    """
    TODO
    """

    size: str
    attributes: List[Attribute]


class StoryRequest(BaseModel):
    """
    TODO
    """

    title: str
    settings: StorySettings
    characters: List[Character]
    plots: int
    endings: int
