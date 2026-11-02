"""Reverse a string (without using [::-1])."""


def reverse_string(s):
    new_string = ""
    for ch in s:
        new_string = ch + new_string
    return new_string