def read_text_from_console():
    """Read and return text entered by the user in the console."""
    return input("Enter text")

def read_file_builtin(filepath):
    """Read and return the content of a file using built-in Python functions."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def read_file_with_pandas(filepath):
    """Read and return the content of a file using the pandas library."""
    import pandas as pd
    return pd.read_csv(filepath)