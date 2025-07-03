import os
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text

UPLOAD_FOLDER = "./uploads"

def save_file(file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return filename, filepath

def read_txt_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def extract_pdf_content(filepath):
    return extract_text(filepath)

def extract_file_content(filename, filepath):
    if filename.lower().endswith(".txt"):
        return read_txt_file(filepath)
    elif filename.lower().endswith(".pdf"):
        return extract_pdf_content(filepath)
    else:
        raise ValueError("Unsupported file type")
