"""
Módulo responsável por salvar arquivos recebidos e extrair seu conteúdo,
suportando arquivos .txt e .pdf.

Funções:
- save_file: salva o arquivo enviado no diretório UPLOAD_FOLDER.
- read_txt_file: lê o conteúdo de um arquivo .txt.
- extract_pdf_content: extrai texto de um arquivo .pdf usando pdfminer.
- extract_file_content: determina o tipo do arquivo e extrai seu conteúdo.
"""

import os
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text

UPLOAD_FOLDER = "./uploads"

def save_file(file):
    """
    Salva o arquivo enviado no diretório UPLOAD_FOLDER.

    Args:
        file (werkzeug.datastructures.FileStorage): Arquivo recebido via request.

    Returns:
        tuple: (filename, filepath) com o nome seguro e caminho completo do arquivo salvo.
    """
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return filename, filepath

def read_txt_file(filepath):
    """
    Lê o conteúdo de um arquivo .txt.

    Args:
        filepath (str): Caminho do arquivo.

    Returns:
        str: Conteúdo do arquivo como string.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def extract_pdf_content(filepath):
    """
    Extrai o texto de um arquivo PDF usando pdfminer.

    Args:
        filepath (str): Caminho do arquivo PDF.

    Returns:
        str: Texto extraído do PDF.
    """
    return extract_text(filepath)

def extract_file_content(filename, filepath):
    """
    Determina o tipo do arquivo (txt ou pdf) e extrai seu conteúdo.

    Args:
        filename (str): Nome do arquivo.
        filepath (str): Caminho do arquivo.

    Returns:
        str: Conteúdo textual extraído do arquivo.

    Raises:
        ValueError: Caso o tipo do arquivo não seja suportado.
    """
    if filename.lower().endswith(".txt"):
        return read_txt_file(filepath)
    elif filename.lower().endswith(".pdf"):
        return extract_pdf_content(filepath)
    else:
        raise ValueError("Unsupported file type")
