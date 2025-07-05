"""
Módulo utils

Utilitários gerais para o projeto.
"""

import os

def delete_file(path):
    """
    Remove um arquivo do sistema de arquivos.

    Args:
        path (str): Caminho absoluto ou relativo do arquivo a ser removido.

    Ignora erros caso o arquivo não exista ou não possa ser deletado,
    permitindo que a aplicação siga sem falhar.

    Exemplo:
        >>> delete_file("./uploads/temp.txt")
    """
    try:
        os.remove(path)
    except OSError:
        pass
