###     Boot.Dev BookBot Python Project     ###

#bookbot main code file

#CH3,L3 -> Arguments
# Use built-in Python {sys} module to handle file path management
# Makes it possible to import any text file, not just the hardcoded on.

import sys

from stats import count_word, count_char, chars_dict_to_sorted_list

def main():
    sys_argv = sys.argv
    # {sys.argv} == list of system arguments passed to the Python script. List == indexed.
    # Default: [0] Python_script_name.py ; [1] file_name
    file_path = sys_argv[1]
    text = get_book_text(file_path)
    word_count = count_word(text)
    char_count = count_char(text)
    sorted_list = chars_dict_to_sorted_list(char_count)
    print_report(file_path, word_count, sorted_list)

def sys_argv_check():
    print(sys.argv)
    sys_argv = sys.argv
    if len(sys_argv) < 2:
        print("""Usage: python3 main.py <path_to_book>""")
        exit(sys.exit(1))
        
  
    

def get_book_text(file_path: str) -> str:
    # FXN accepts a STR type input & gives STR type output.
    with open(file_path) as f:
    # {with} FXN executes operation ON something
    # {open} FXN will fetch and open a file for the FXN, and ENSURE the file is closed to free up resources.
        file_content = f.read()
        return(file_content)


def print_report(file_path, word_count, sorted_list):
    print(
f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for item in sorted_list:
        # item == a tuple [e.g., ('b', 4)]
        if item[0].isalpha():
        # tuple == indexed; if value at index 0 is an alphabetical character, execute the loop.
            print(f"{item[0]}: {item[1]}")
        # loop == print the tuple value at index 0 (the char) and index 1 (the count).
        else:
            continue
    print("============= END ===============")

sys_argv_check()
main()


#CH2,L5 -> Refactor: Organise code across different files according to the codes' purpose.
# main.py == entry point to our program and any code that doesn't fir elsewhere
# stats.py == functions for analyzing the text
#          == incl. CH2,L1-4
'''#CH3,L1 -> Organise Data

from stats import count_word, count_char, chars_dict_to_sorted_list

def main():
    file_path = 'books/frankenstein.txt'
    text = get_book_text(file_path)
    word_count = count_word(text)
    char_count = count_char(text)
    sorted_list = chars_dict_to_sorted_list(char_count)
    print(f'Found {word_count} total words')
    # print(char_count)
    print(sorted_list)

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_content = f.read()
        return(file_content)


main()
'''
'''#CH3,L2 -> Print a Report

from stats import count_word, count_char, chars_dict_to_sorted_list

def main():
    file_path = 'books/frankenstein.txt'
    text = get_book_text(file_path)
    word_count = count_word(text)
    char_count = count_char(text)
    sorted_list = chars_dict_to_sorted_list(char_count)
    # print(f'Found {word_count} total words')
    # print(char_count)
    # print(sorted_list)
    print_report(file_path, word_count, sorted_list)

def get_book_text(file_path: str) -> str:
    # FXN accepts a STR type input & gives STR type output.
    with open(file_path) as f:
    # {with} FXN executes operation ON something
    # {open} FXN will fetch and open a file for the FXN, and ENSURE the file is closed to free up resources.
        file_content = f.read()
        return(file_content)


def print_report(file_path, word_count, sorted_list):
    print(
f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for item in sorted_list:
        # item == a tuple [e.g., ('b', 4)]
        if item[0].isalpha():
        # tuple == indexed; if value at index 0 is an alphabetical character, execute the loop.
            print(f"{item[0]}: {item[1]}")
        # loop == print the tuple value at index 0 (the char) and index 1 (the count).
        else:
            continue
    print("============= END ===============")


main()
'''

