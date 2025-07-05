"""
Pacote `app.services`

Este pacote contém os serviços principais usados pela aplicação
para processar arquivos, realizar pré-processamento NLP,
consultar o modelo de IA e gerenciar cache.

Módulos disponíveis:
- file_service: Funções para salvar e extrair conteúdo de arquivos .txt e .pdf.
- nlp_service: Pré-processamento de texto e geração de hash.
- ai_service: Integração com o modelo GPT-3.5 para classificação e sugestão.
- cache: Cache em memória para evitar reprocessamento de textos idênticos.
"""
