"""
Módulo responsável por processar texto para classificação de emails,
incluindo limpeza (remoção de stopwords) e geração de hash do texto.

Funções:
- preprocess_text: realiza tokenização, remoção de pontuação e stopwords em português.
- get_text_hash: gera um hash SHA-256 único para o texto processado.
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import hashlib

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

def preprocess_text(text):
    """
    Pré-processa o texto recebido:
    - converte para minúsculas
    - tokeniza em palavras
    - remove pontuações e stopwords (português)

    Args:
        text (str): Texto original.

    Returns:
        str: Texto limpo, apenas com palavras significativas separadas por espaço.
    """
    text = text.lower()
    words = word_tokenize(text, preserve_line=True)
    stop_words = set(stopwords.words("portuguese"))
    filtered_words = [w for w in words if w.isalnum() and w not in stop_words]
    return " ".join(filtered_words)

def get_text_hash(text):
    """
    Gera um hash SHA-256 para o texto processado.

    Útil para usar como chave de cache, evitando processar o mesmo texto repetidamente.

    Args:
        text (str): Texto já pré-processado.

    Returns:
        str: Hash SHA-256 do texto.
    """
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
