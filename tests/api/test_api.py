# tests/api/test_api.py
import requests

BASE_URL = 'http://localhost:8000'

def test_get_root():
    response = requests.get(f'{BASE_URL}/')
    assert response.status_code == 200

def test_post_generate_dialog():
    response = requests.post(f'{BASE_URL}/generate/dialog')
    assert response.status_code == 201

def test_post_generate_story():
    response = requests.post(f'{BASE_URL}/generate/story')
    assert response.status_code == 201
