# Variables
file_path = "books/frankenstein.txt"
file_contents = ""
word_count = []
num_words = ""

from stats import get_book_text

def main():
    get_book_text(file_path)

main()
