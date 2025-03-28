import pytest
import pandas as pd
import tempfile
from app.io.input import read_file_builtin, read_file_with_pandas

def test_read_file_builtin_normal_text():
    content = "Hello, this is a test."
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    assert read_file_builtin(tmp_path) == content

def test_read_file_builtin_empty_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as tmp:
        tmp_path = tmp.name
    assert read_file_builtin(tmp_path) == ""

def test_read_file_builtin_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        read_file_builtin("nonexistent_file.txt")

