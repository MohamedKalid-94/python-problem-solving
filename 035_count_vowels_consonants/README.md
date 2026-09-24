# Problem 35 — Count Vowels and Consonants

## Problem
Count the number of vowels and consonants in a given string.

## Input
text = "python"

## Output
Vowel Count = 1
Consonant Count = 5

## Approach
- Initialize two counters: `vowel_count` and `consonant_count`.
- Loop through each character in the string.
- Check whether the character exists in `"aeiou"`.
- If it does, increment `vowel_count`.
- Otherwise, increment `consonant_count`.

## Pattern
String Traversal + Classification + Counting

## Key Concept
Check each character individually.

`character in "aeiou"` → Vowel

Otherwise → Consonant

## Complexity
- Time: O(n)
- Space: O(1)