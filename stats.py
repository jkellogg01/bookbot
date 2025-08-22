def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    return counts

def sort_chars(counts):
    char_dicts = []
    for key in counts:
        count = counts[key]
        char_dicts.append({
            "char": key,
            "num": count,
            })
    char_dicts.sort(reverse=True, key=sort_chars_on)
    return char_dicts

def sort_chars_on(char_count):
    return char_count["num"]
