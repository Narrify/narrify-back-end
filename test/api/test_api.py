""" 
usaremos un mock server de postman para simular la respuesta de la API
"""


import os
import requests


BASE_URL = os.getenv('BASE_URL') or 'https://ce38683d-884f-4967-85aa-722f3fc2b983.mock.pstmn.io'
assert BASE_URL is not None, "La variable de entorno BASE_URL no está definida o está vacía."

def test_get_root():
    """
    Test para verificar que la API está en línea
    """

    response = requests.get(f'{BASE_URL}/', timeout=10)
    assert response.status_code == 200


def test_post_generate_dialog():
    """
    Test para verificar que la API puede generar un diálogo
    """
    response = requests.post(f'{BASE_URL}/generate/dialog', timeout=10)
    assert response.status_code == 201


def test_post_generate_story():
    """
    Test para verificar que la API puede generar una historia
    """
    response = requests.post(f'{BASE_URL}/generate/story', timeout=10)
    assert response.status_code == 201
