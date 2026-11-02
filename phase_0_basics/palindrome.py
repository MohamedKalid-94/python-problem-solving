"""Check whether a string reads the same forwards and backwards."""


def is_palindrome(s):
    reversed_s = ""
    for ch in s:
        reversed_s = ch + reversed_s

    if s == reversed_s:
        return True
    else:
        return False