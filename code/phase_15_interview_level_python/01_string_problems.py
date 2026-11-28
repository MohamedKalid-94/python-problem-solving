"""
Phase 15 - Interview-Level Python
01 String Problems
"""


def reverse_string(s):
    # [::-1] means "take the whole string, stepping backwards"
    return s[::-1]


def is_palindrome(s):
    # Keep only letters and digits, and ignore upper/lower case.
    # "A man, a plan, a canal: Panama" becomes "amanaplanacanalpanama"
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned = cleaned + ch.lower()
    return cleaned == cleaned[::-1]


def character_frequency(s):
    result = {}
    for ch in s:
        # get(ch, 0) returns 0 when the character is not in the dictionary yet
        result[ch] = result.get(ch, 0) + 1
    return result


def remove_duplicates(s):
    # dict.fromkeys keeps each character once AND keeps the original order.
    # (set() would remove duplicates but mix up the order.)
    return "".join(dict.fromkeys(s))


def check_anagram(a, b):
    # Anagrams have the same letters. Ignore case and spaces, then compare sorted letters.
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)


def count_vowels(s):
    # Add 1 for every character that is a vowel
    return sum(1 for ch in s.lower() if ch in "aeiou")


def first_non_repeating(s):
    freq = character_frequency(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


def main():
    text = "python"

    print("Reverse:", reverse_string(text))
    print("Palindrome:", is_palindrome("madam"))
    print("Palindrome (sentence):", is_palindrome("A man, a plan, a canal: Panama"))
    print("Frequency:", character_frequency(text))
    print("Remove Duplicates:", remove_duplicates("programming"))
    print("Anagram:", check_anagram("listen", "silent"))
    print("Vowels:", count_vowels(text))
    print("First Non Repeating:", first_non_repeating("aabbcd"))


if __name__ == "__main__":
    main()