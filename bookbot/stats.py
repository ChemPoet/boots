###     Boot.Dev BookBot Python Project     ###

#bookbot text analysis functions code file

'''#CH2,L1 -> Test Python environment
print("greetings boots")
'''
'''#CH2,L2 -> imported Gutenburg's frankenstein.txt to dir: "books/frankenstein.txt"
'''
'''#CH2,L3 -> with Block; read() Method

def get_book_text(x):
    # "with..." ensures called file is closed when code exec. completes.
    with open(x) as f:
        file_content = f.read()
        print(file_content)
    # FXN receives directory to open (x) when it is called by FXN main
    # Directory MUST BE specified using plain text (str)!
        
def main():
    get_book_text('books/frankenstein.txt')
    # Relative path to file == argument passed to FXN

main()
'''
'''#Ch2,L4 -> Count Words

def get_book_text(x):
    with open(x) as f:
        file_content = f.read()
        word_list = str.split(file_content)
        word_count = len(word_list)
        print(f'Found {word_count} total words')

def main():
    get_book_text('books/frankenstein.txt')

main()
'''
'''#CH2,L5 -> Refactor: Organise code across different files according to the codes' purpose.
# main.py == entry point to our program and any code that doesn't fir elsewhere
# stats.py == functions for analyzing the text


def get_book_text(x):
    with open(x) as f:
        file_content = f.read()
        word_list = str.split(file_content)
        word_count = len(word_list)
        print(f'Found {word_count} total words')

def main():
    get_book_text('books/frankenstein.txt')
'''

'''#CH2,L6 -> Count Characters

# def get_book_text(x):
#     with open(x) as f:
#         file_content = f.read()
#         print(file_content)

def count_word(x):
    with open(x) as f:
        file_content = f.read()
        word_list = str.split(file_content)
        word_count = len(word_list)
    print(f'Found {word_count} total words')


def count_char(x):
    with open(x) as f:
        file_content = f.read()
        lowercase_file = str.lower(file_content)
        char_count = {}
    for index in lowercase_file:
        if index in char_count:
            char_count[index] = char_count[index]+1
        else:
            char_count[index] = 1
    print(char_count)
'''

#CH3,L1 -> Organize Data


def count_word(text: str) -> int:
    # FXN accepts STR type input, delivers INT type output
    word_list = text.split()
    word_count = len(word_list)
    return word_count


def count_char(text: str) -> dict[str, int]:
    # FXN accepts STR type input, delivers DICT as output containing [STR:INT] pairs
    lowercase_file = text.lower()
    char_count = {}
    for index in lowercase_file:
        if index in char_count:
            char_count[index] = char_count[index]+1
        else:
            char_count[index] = 1
    return(char_count)


def sorting_on(char_count: tuple[str, int]) -> int:
    # FXN accepts tuple as input (containing [STR, INT] data), gives INT type output
    return char_count[1]
# FXN == key used to sort the list of tuples. Sorts each LIST ENTRY based on the VALUE at tuple index 1.
#     == Ergo: The list of tuples is sorted by the second position.


def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
    #FXN accepts dict input (with [STR, INT] type data), and gives a list of tuples as output.
    sorting_list = []
    for char in char_count:
        sorting_list.append((char,char_count[char]))
        # Creates a LIST of TUPLES from the DICT values. Tuple == immutable; cannot change value of dict pairs!
        # Dict == unordered, but List == ordered (can be sorted!)
    sorted_list = sorted(sorting_list, reverse=True, key=sorting_on)
            # {sorted} FXN applied to "sorting_list"; reverse == Larges -> Small values; key == sort criteria/specifications
            # {key=sorting_on} tells FXN to sort based on tuple value at index 1.
    return sorted_list


