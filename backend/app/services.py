import os
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
from app.utils import delete_file

UPLOAD_FOLDER = "./uploads"

def process_uploaded_file(file):
    filename, filepath = save_file(file)
    try:
        text_content = extract_file_content(filename, filepath)
    finally:
        delete_file(filepath)
    return filename, text_content

def save_file(file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return filename, filepath

def extract_file_content(filename, filepath):
    if filename.lower().endswith(".txt"):
        return read_txt_file(filepath)
    elif filename.lower().endswith(".pdf"):
        return extract_pdf_content(filepath)
    else:
        raise ValueError("Unsupported file type")

def read_txt_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def extract_pdf_content(filepath):
    return extract_text(filepath)
