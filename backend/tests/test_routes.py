import io
import pytest
from app import app as flask_app

@pytest.fixture
def client():
    return flask_app.test_client()

def test_upload_txt_file(client):
    data = {
        'file': (io.BytesIO("Este é um email de teste para verificar o pipeline.".encode("utf-8")), 'test.txt')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert 'results' in json_data
    assert isinstance(json_data['results'], list)
    assert len(json_data['results']) == 1
    
    result = json_data['results'][0]
    assert 'categoria' in result
    assert 'resposta_sugerida' in result
    assert result['file'] == 'test.txt'
    assert result['type'] == 'file'

def test_upload_text(client):
    data = {
        'text': "Este é um texto direto para classificar."
    }
    response = client.post('/upload', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    
    assert 'results' in json_data
    assert isinstance(json_data['results'], list)
    assert len(json_data['results']) == 1
    
    result = json_data['results'][0]
    assert 'categoria' in result
    assert 'resposta_sugerida' in result
    assert result['type'] == 'text'

def test_no_file_uploaded(client):
    response = client.post('/upload', data={})
    assert response.status_code == 400
    json_data = response.get_json()
    assert 'error' in json_data

