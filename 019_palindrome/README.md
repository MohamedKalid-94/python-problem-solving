# Problem 19 — Check Palindrome

## Problem

Check whether a string reads the same forward and backward.

## Input

text = "madam"

## Output

Palindrome

## Approach

* Assume the string is a palindrome.
* Loop through each character using its index.
* Compare the current character with the character at the opposite index.
* The opposite index is calculated using:
  `len(text) - 1 - index`
* If any pair does not match, set `is_palindrome` to `False` and stop the loop.
* Print the result.

## Pattern

Opposite Index Comparison

## Complexity

* Time: O(n)
* Space: O(1)
