"""
TODO
"""

from tests.test import client
from fastapi import status


def test_hello_world():
    """
    TODO
    """

    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Hello World"
