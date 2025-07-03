import pytest
from unittest.mock import patch
from app.services.ai_service import classify_and_suggest

@patch("app.services.ai_service.OpenAI")
def test_classify_and_suggest_parses_json(mock_openai):
    mock_openai.return_value.chat.completions.create.return_value.choices[0].message.content = """
    {
        "categoria": "Produtivo",
        "resposta_sugerida": "Obrigado pelo contato, vamos analisar."
    }
    """
    resultado = classify_and_suggest("texto processado")
    assert resultado["categoria"] == "Produtivo"
    assert "resposta_sugerida" in resultado
