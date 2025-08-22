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
