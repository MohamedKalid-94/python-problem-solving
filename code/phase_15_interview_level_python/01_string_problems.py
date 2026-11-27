# Phase 15 - Interview-Level Python
# 01 String Problems

def reverse_string(s): return s[::-1]

def is_palindrome(s): return s==s[::-1]

def character_frequency(s):
    result={}
    for ch in s: result[ch]=result.get(ch,0)+1
    return result

def remove_duplicates(s): return "".join(set(s))

def check_anagram(a,b): return sorted(a)==sorted(b)

def count_vowels(s): return sum(1 for ch in s.lower() if ch in "aeiou")

def first_non_repeating(s):
    freq=character_frequency(s)
    for ch in s:
        if freq[ch]==1: return ch
    return None

def main():
    text="python"

    print("Reverse:",reverse_string(text))
    print("Palindrome:",is_palindrome("madam"))
    print("Frequency:",character_frequency(text))
    print("Remove Duplicates:",remove_duplicates("programming"))
    print("Anagram:",check_anagram("listen","silent"))
    print("Vowels:",count_vowels(text))
    print("First Non Repeating:",first_non_repeating("aabbcd"))

if __name__=="__main__": main()