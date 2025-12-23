def print_work_to_console(text):
    ####below is to print the entire text to the console:
    text_to_print = text
    print(text_to_print)

def print_word_count(text):
    ####below is to count the number of words in the entire text and print result to console
    split_text = text.split()
    counted_text = len(split_text)
    print(f"Found {counted_text} total words")

def print_char_dict(text):
    ####below is to count the number of each character (including spaces and symbols) in the entire text and print result to console
    char_dict = {}
    chars = list(text)
    for char in chars:
        lower_char = char.lower()
        if lower_char not in char_dict:
            char_dict[lower_char] = 1
        else:
            char_dict[lower_char] += 1
    print(char_dict)

def sort_dictionary():
    sorted_dict = print_char_dict.sort()