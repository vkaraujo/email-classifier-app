import pytest
from app.services.nlp_service import preprocess_text, get_text_hash

def test_preprocess_text_removes_stopwords():
    texto = "Olá, este é um teste para verificar as stopwords."
    resultado = preprocess_text(texto)
    assert "este" not in resultado.split()
    assert "teste" in resultado

def test_get_text_hash_is_consistent():
    texto1 = "um texto simples"
    texto2 = "um texto simples"
    assert get_text_hash(texto1) == get_text_hash(texto2)

def test_get_text_hash_changes_with_text():
    texto1 = "um texto"
    texto2 = "outro texto"
    assert get_text_hash(texto1) != get_text_hash(texto2)
