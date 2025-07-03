import pytest
from app.services.file_service import extract_file_content

def test_extract_file_content_txt(tmp_path):
    txt_file = tmp_path / "test.txt"
    txt_file.write_text("Este é um arquivo de teste.")

    content = extract_file_content("test.txt", str(txt_file))
    assert "arquivo de teste" in content
