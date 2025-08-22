from stats import get_num_words, get_num_chars, sort_chars

def main():
    print("============ BOOKBOT ============")
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = get_num_chars(text)
    chars_sorted = sort_chars(char_counts)
    for char_dict in chars_sorted:
        char = char_dict["char"]
        if not char.isalpha():
            continue
        count = char_dict["num"]
        print(f"{char}: {count}")

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
        return file_text

main()
