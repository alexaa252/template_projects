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

def test_read_file_with_pandas_simple_csv():
    csv_content = "name,age\nAlice,30\nBob,25"
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8', suffix='.csv') as tmp:
        tmp.write(csv_content)
        tmp_path = tmp.name
    df = read_file_with_pandas(tmp_path)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["name", "age"]
    assert df.iloc[0]["name"] == "Alice"

def test_read_file_with_pandas_empty_csv():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8', suffix='.csv') as tmp:
        tmp.write("")
        tmp_path = tmp.name
    with pytest.raises(pd.errors.EmptyDataError):
        read_file_with_pandas(tmp_path)

def test_read_file_with_pandas_incorrect_format():
    bad_content = "Just some random text\nthat is not csv"
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8', suffix='.csv') as tmp:
        tmp.write(bad_content)
        tmp_path = tmp.name

    df = read_file_with_pandas(tmp_path)

    assert df.shape[1] == 1
    assert "Just some random text" in df.columns[0]
    assert df.iloc[0, 0] == "that is not csv"

