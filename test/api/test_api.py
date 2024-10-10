import os
import requests

# usaremos un mock server de postman
BASE_URL = os.getenv('BASE_URL')


def test_get_root():

    response = requests.get(f'{BASE_URL}/', timeout=30)
    assert response.status_code == 200


def test_post_generate_dialog():

    response = requests.post(f'{BASE_URL}/generate/dialog', timeout=30)
    assert response.status_code == 201


def test_post_generate_story():

    response = requests.post(f'{BASE_URL}/generate/story', timeout=30)
    assert response.status_code == 201
