from app.services.file_service import save_file, extract_file_content
from app.services.nlp_service import preprocess_text, get_text_hash
from app.services.ai_service import classify_and_suggest
from app.services.cache import cache
from app.utils import delete_file
import logging

logging.basicConfig(level=logging.INFO)

def process_uploaded_file(file):
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
