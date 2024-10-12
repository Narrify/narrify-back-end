"""
TODO
"""

from fastapi import status
from tests.test import client


def test_generate_story():
    """
    TODO
    """

    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Hello World"


def test_generate_dialog():
    """
    TODO
    """

    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Hello World"
