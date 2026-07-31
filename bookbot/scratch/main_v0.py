# Variables
file_path = "books/frankenstein.txt"
file_contents = ""


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    print(file_contents)


def main():
    get_book_text(file_path)

main()
