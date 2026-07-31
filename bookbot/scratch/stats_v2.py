# Variables defined in main.py
char_output = dict()

# Word Count in File
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        word_count = file_contents.split()
        num_words = len(word_count)
        output = f"Found {num_words} total words"
    print (output)


# Character Count in File
def count_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        lowercase = file_contents.lower()
        for char in lowercase:
            if char in char_output:
                char_count = char_output[char] + 1
                char_output[char] = char_count
            else:
                char_output[char] = 1
#    print (char_output)


def sort_on(character: tuple[str, int]) -> int:
    return character[1]


def chars_dict_to_sorted_list(char_to_sort: dict[str, int]):
    sort_list = list
    
    
    return list[tuple[str, int]]