import io
import pytest
from unittest.mock import patch
from app import app as flask_app

@pytest.fixture
def client():
    return flask_app.test_client()

@patch("app.pipeline.classify_and_suggest")
def test_upload_txt_file(mock_ai, client):
    mock_ai.return_value = {
        "categoria": "Produtivo",
        "resposta_sugerida": "Resposta simulada."
    }

    data = {
        'file': (io.BytesIO("Este é um email de teste para verificar o pipeline.".encode("utf-8")), 'test.txt')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()

    assert 'results' in json_data
    assert len(json_data['results']) == 1
    result = json_data['results'][0]
    assert result['categoria'] == "Produtivo"
    assert result['resposta_sugerida'] == "Resposta simulada."

@patch("app.pipeline.classify_and_suggest")
def test_upload_text(mock_ai, client):
    mock_ai.return_value = {
        "categoria": "Improdutivo",
        "resposta_sugerida": "Resposta simulada."
    }

    data = {'text': "Texto direto"}
    response = client.post('/upload', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    result = json_data['results'][0]
    assert result['categoria'] == "Improdutivo"
    assert result['resposta_sugerida'] == "Resposta simulada."

def test_no_file_uploaded(client):
    response = client.post('/upload', data={})
    assert response.status_code == 400
    json_data = response.get_json()
    assert 'error' in json_data
