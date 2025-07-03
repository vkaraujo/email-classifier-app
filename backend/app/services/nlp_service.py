import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import hashlib

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

def preprocess_text(text):
    text = text.lower()
    words = word_tokenize(text, preserve_line=True)
    stop_words = set(stopwords.words("portuguese"))
    filtered_words = [w for w in words if w.isalnum() and w not in stop_words]
    return " ".join(filtered_words)

def get_text_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
