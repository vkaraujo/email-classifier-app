"""
Módulo que implementa um cache simples em memória.

Usado para armazenar resultados de classificações de textos
já processados, evitando chamadas repetidas ao modelo de IA
para o mesmo conteúdo.

Classes:
- InMemoryCache: cache em memória baseado em dicionário Python.
"""

class InMemoryCache:
    """
    Classe que representa um cache em memória.

    Armazena pares chave-valor, onde a chave geralmente
    é o hash SHA-256 do texto processado.

    Métodos:
    - get(key): retorna o valor associado à chave ou None.
    - set(key, value): salva o valor no cache para a chave dada.
    """

    def __init__(self):
        """
        Inicializa o dicionário interno do cache.
        """
        self.store = {}

    def get(self, key):
        """
        Busca um valor no cache.

        Args:
            key (str): A chave a ser buscada.

        Returns:
            any: O valor armazenado ou None se não encontrado.
        """
        return self.store.get(key)

    def set(self, key, value):
        """
        Armazena um valor no cache.

        Args:
            key (str): A chave única (ex: hash do texto).
            value (any): O valor a ser armazenado.
        """
        self.store[key] = value

# Instância global do cache para uso em toda a aplicação.
cache = InMemoryCache()
