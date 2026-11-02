"""Count the vowels (a, e, i, o, u) in a string, ignoring case."""


def count_vowels(s):
    s = s.lower()
    count = 0
    for ch in s:
        if ch in "aeiou":
            count = count + 1
    return count