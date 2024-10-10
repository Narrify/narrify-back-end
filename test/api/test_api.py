import os
import requests

# usaremos un mock server de postman
BASE_URL = os.getenv('BASE_URL') or 'https://ce38683d-884f-4967-85aa-722f3fc2b983.mock.pstmn.io'
assert BASE_URL is not None, "La variable de entorno BASE_URL no está definida o está vacía."

def test_get_root():

    response = requests.get(f'{BASE_URL}/', timeout=10)
    assert response.status_code == 200


def test_post_generate_dialog():

    response = requests.post(f'{BASE_URL}/generate/dialog', timeout=10)
    assert response.status_code == 201


def test_post_generate_story():

    response = requests.post(f'{BASE_URL}/generate/story', timeout=10)
    assert response.status_code == 201
