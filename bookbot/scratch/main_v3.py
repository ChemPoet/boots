# Variables
file_path = "books/frankenstein.txt"
file_contents = ""
word_count = []
num_words = ""
char_list = ""


from stats import get_book_text
from stats import count_book_text

def main():
    get_book_text(file_path)
    count_book_text(file_path)

main()
