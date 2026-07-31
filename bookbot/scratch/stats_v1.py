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
    print (char_output)

