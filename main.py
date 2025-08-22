from stats import get_num_words

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(text)
    print(f"{word_count} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
        return file_text

main()
