def main():
    report("books/frankenstein.txt")

def report(path):
    text = get_file_contents(path)
    print(f"==== begin report: {path} ====")
    words = count_words(text)
    print(f"found {words} words in the document")
    letters = count_letters(text)
    letterList = []
    for letter in letters:
        letterList.append({
            "letter": letter,
            "count": letters[letter],
            })
    letterList.sort(reverse=True, key=sort_on)
    for letter in letterList:
        char = letter["letter"]
        count = letter["count"]
        print(f"found '{char}' {count} times")
    print("==== end report ====")


def get_file_contents(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    result = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_on(dict):
    return dict["count"]

main()
