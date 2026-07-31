###     Boot.Dev BookBot Python Project     ###

#bookbot main code file
#CH2,L5 -> Refactor: Organise code across different files according to the codes' purpose.
# main.py == entry point to our program and any code that doesn't fir elsewhere
# stats.py == functions for analyzing the text
#          == incl. CH2,L1-4

from stats import get_book_text, count_word, count_char

def main():
    get_book_text('books/frankenstein.txt')
    count_word(get_book_text)
    count_char(count_word)

main()

