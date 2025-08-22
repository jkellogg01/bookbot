def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
        return file_text

main()
