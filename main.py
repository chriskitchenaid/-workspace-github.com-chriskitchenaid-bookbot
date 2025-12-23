from stats import print_word_count, print_char_dict, sort_dictionary

def get_book_text(file): 
    with open(file) as f:
        file_text = f.read()
    return file_text

def main():
    text = get_book_text("books/frankenstein.txt")
    print_word_count(text)
    print_char_dict(text)
    sort_dictionary()

main()