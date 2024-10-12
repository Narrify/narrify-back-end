"""
TODO
"""

from tests.test import client
from fastapi import status


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
