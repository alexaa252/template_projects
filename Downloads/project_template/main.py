from app.io.input import read_text_from_console, read_file_builtin, read_file_with_pandas
from app.io.output import print_to_console, write_to_file

def main():
    text_console = read_text_from_console()
    print_to_console(text_console)
    write_to_file("data/from_console.txt", text_console)

    text_builtin = read_file_builtin("data/sample.txt")
    print_to_console(text_builtin)
    write_to_file("data/from_builtin.txt", text_builtin)

    text_pandas = read_file_with_pandas("data/sample.csv")
    print_to_console(text_pandas)
    write_to_file("data/from_pandas.txt", str(text_pandas))

if __name__ == "__main__":
    main()