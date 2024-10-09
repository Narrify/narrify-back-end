"""
TODO
"""

import requests

BASE_URL = 'http://localhost:8000'


def test_get_root():
    """
    TODO
    """

    response = requests.get(f'{BASE_URL}/', timeout=30)
    assert response.status_code == 200


def test_post_generate_dialog():
    """
    TODO
    """

    response = requests.post(f'{BASE_URL}/generate/dialog', timeout=30)
    assert response.status_code == 201


def test_post_generate_story():
    """
    TODO
    """

    response = requests.post(f'{BASE_URL}/generate/story', timeout=30)
    assert response.status_code == 201
