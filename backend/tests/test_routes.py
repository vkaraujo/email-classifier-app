import io
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_txt_file(client):
    data = {
        'file': (io.BytesIO("Este é um email de teste para verificar o pipeline.".encode("utf-8")), 'test.txt')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'categoria' in json_data
    assert 'resposta_sugerida' in json_data
    print(json_data)

def test_no_file_uploaded(client):
    response = client.post('/upload', data={}, content_type='multipart/form-data')
    assert response.status_code == 400
    assert 'error' in response.get_json()
