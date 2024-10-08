"""
/TODO
"""

from typing import List
from pydantic import BaseModel


class Attribute(BaseModel):
    """
    /TODO
    """

    name: str
    value: str


class Character(BaseModel):
    """
    /TODO
    """

    name: str
    attributes: List[Attribute]
