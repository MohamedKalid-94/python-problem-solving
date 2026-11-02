"""Count how many times each word appears in a text."""


def word_frequency(text):
    counts = {}
    words = text.lower().split()

    for w in words:
        if w in counts:
            counts[w] = counts[w] + 1
        else:
            counts[w] = 1
    return counts