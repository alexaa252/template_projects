def print_to_console(text):
    """Print the given text to the console."""
    return(text)

def write_to_file(filepath, text):
    """Write the given text to a file using built-in Python functions."""
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text)