"""
TODO
"""

from fastapi import status
from tests.tests import client


def test_hello_world():
    """
    TODO
    """

    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Hello World"
