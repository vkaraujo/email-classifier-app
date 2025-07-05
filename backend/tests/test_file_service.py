import pytest
from app.services.file_service import extract_file_content
import io
from unittest.mock import patch
from werkzeug.datastructures import FileStorage
from app.pipeline import process_uploaded_file


def test_full_pipeline_txt():
    stream = io.BytesIO("Este é um email de teste para o pipeline.".encode("utf-8"))
    file = FileStorage(stream=stream, filename="test.txt", content_type="text/plain")

    with patch("app.pipeline.classify_and_suggest") as mock_ai:
        mock_ai.return_value = {
            "categoria": "Produtivo",
            "resposta_sugerida": "Obrigado pelo email, vamos responder em breve."
        }

        resultado = process_uploaded_file(file)
        assert "categoria" in resultado
        assert "resposta_sugerida" in resultado
