"""
Módulo pipeline

Responsável por orquestrar o fluxo completo do processamento dos emails,
incluindo extração de texto, pré-processamento, hashing para cache,
classificação via IA e salvamento dos resultados em cache.
"""

from app.services.file_service import save_file, extract_file_content
from app.services.nlp_service import preprocess_text, get_text_hash
from app.services.ai_service import classify_and_suggest
from app.services.cache import cache
from app.utils import delete_file
import logging

logging.basicConfig(level=logging.INFO)

def process_uploaded_file(file):
    """
    Processa um arquivo de email (TXT ou PDF) carregado pelo usuário.

    - Salva o arquivo no sistema de arquivos.
    - Extrai o texto do arquivo.
    - Pré-processa o texto (remove stopwords, normaliza).
    - Gera um hash do texto para verificar cache.
    - Caso já exista, reutiliza classificação anterior.
    - Caso não exista, envia para IA classificar e armazena o resultado no cache.
    - Exclui o arquivo salvo após o processamento.

    Args:
        file: Um objeto de arquivo recebido via upload (Flask `FileStorage`).

    Returns:
        dict: Um dicionário com a classificação e resposta sugerida.
              Exemplo: {"categoria": "Produtivo", "resposta_sugerida": "..."}
    """
    filename, filepath = save_file(file)
    try:
        text_content = extract_file_content(filename, filepath)
        cleaned_text = preprocess_text(text_content)
        text_hash = get_text_hash(cleaned_text)

        cached_result = cache.get(text_hash)
        if cached_result:
            logging.info("Cache hit - reutilizando classificação anterior.")
            return cached_result

        classification = classify_and_suggest(cleaned_text)
        cache.set(text_hash, classification)
    finally:
        delete_file(filepath)

    return classification

def process_raw_text(text):
    """
    Processa um texto bruto inserido diretamente pelo usuário.

    - Pré-processa o texto (remove stopwords, normaliza).
    - Gera um hash do texto para verificar cache.
    - Caso já exista, reutiliza classificação anterior.
    - Caso não exista, envia para IA classificar e armazena o resultado no cache.

    Args:
        text (str): Texto do email fornecido pelo usuário.

    Returns:
        dict: Um dicionário com a classificação e resposta sugerida.
              Exemplo: {"categoria": "Produtivo", "resposta_sugerida": "..."}
    """
    cleaned_text = preprocess_text(text)
    text_hash = get_text_hash(cleaned_text)

    cached_result = cache.get(text_hash)
    if cached_result:
        logging.info("Cache hit (text) - reutilizando classificação anterior.")
        return cached_result

    classification = classify_and_suggest(cleaned_text)
    cache.set(text_hash, classification)
    return classification
