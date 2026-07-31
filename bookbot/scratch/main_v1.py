# Variables
file_path = "books/frankenstein.txt"
file_contents = ""
word_count = []
num_words = ""


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        word_count = file_contents.split()
        num_words = len(word_count)
        output = f"Found {num_words} total words"
    print (output)


def main():
    get_book_text(file_path)

main()
