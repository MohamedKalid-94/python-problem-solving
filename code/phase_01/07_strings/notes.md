# Phase 1 - Step 7: Strings Notes

## Overview

A **string** is one of the most commonly used data types in Python. It is a sequence of characters enclosed within quotes.

Strings are used to store:

- Names
- Sentences
- Passwords
- Email addresses
- URLs
- File paths
- Messages
- Source code
- JSON data
- User input

Almost every Python program works with strings.

---

# What is a String?

A string is a sequence of Unicode characters.

Example

```python
name = "Python"

language = 'Programming'
```

Both are valid strings.

---

# Creating Strings

Python supports three ways to create strings.

## Single Quotes

```python
name = 'Python'
```

---

## Double Quotes

```python
language = "Python"
```

---

## Triple Quotes

Useful for multiline strings.

```python
message = """
Hello
Welcome to Python
"""
```

---

# String Immutability

Strings are **immutable**.

This means once a string is created, its characters cannot be changed.

Wrong

```python
text = "Python"

text[0] = "J"
```

Output

```
TypeError
```

Correct

```python
text = "Python"

text = "J" + text[1:]
```

---

# Escape Characters

Escape characters begin with a backslash (`\`).

| Escape | Meaning |
|---------|----------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote |
| `\'` | Single quote |

Example

```python
print("Hello\nWorld")
```

Output

```
Hello
World
```

---

# String Indexing

Every character has a position.

Example

```
Python

P  y  t  h  o  n

0  1  2  3  4  5
```

Accessing characters

```python
text = "Python"

print(text[0])
```

Output

```
P
```

---

# Negative Indexing

Python also supports negative indexing.

```
Python

P  y  t  h  o  n

-6 -5 -4 -3 -2 -1
```

Example

```python
print(text[-1])
```

Output

```
n
```

---

# String Slicing

Slicing extracts part of a string.

Syntax

```python
string[start:stop]
```

Example

```python
text = "Programming"

print(text[0:7])
```

Output

```
Program
```

---

# Step Slicing

Syntax

```python
string[start:stop:step]
```

Example

```python
text[::2]
```

Output

```
Pto
```

---

# Reverse a String

Using slicing

```python
text[::-1]
```

Example

```python
Python

↓

nohtyP
```

---

# String Iteration

Strings can be traversed character by character.

Using a for loop

```python
for character in text:
    print(character)
```

Using a while loop

```python
index = 0

while index < len(text):
    print(text[index])
    index += 1
```

---

# enumerate()

Returns both the index and character.

Example

```python
for index, character in enumerate(text):
    print(index, character)
```

---

# Searching Strings

## find()

Returns the first occurrence.

Returns **-1** if not found.

Example

```python
text.find("Python")
```

---

## index()

Returns the first occurrence.

Raises

```
ValueError
```

if not found.

---

# Difference

| find() | index() |
|---------|----------|
| Returns -1 | Raises ValueError |

---

# Replacing Strings

Use

```python
replace()
```

Example

```python
text.replace("Java", "Python")
```

---

# Counting Characters

Use

```python
count()
```

Example

```python
text.count("a")
```

---

# String Formatting

Python supports three formatting styles.

---

## f-Strings

Recommended.

```python
name = "Kalid"

print(f"Hello {name}")
```

---

## format()

```python
print("Hello {}".format(name))
```

---

## Percentage Formatting

Old style.

```python
print("%s" % name)
```

---

# Alignment Formatting

Left

```python
f"{name:<10}"
```

Center

```python
f"{name:^10}"
```

Right

```python
f"{name:>10}"
```

---

# Splitting Strings

Converts a string into a list.

Example

```python
sentence.split()
```

Output

```python
["Python", "is", "easy"]
```

---

# split(separator)

Example

```python
text.split(",")
```

---

# splitlines()

Splits multiline text.

Example

```python
message.splitlines()
```

---

# Joining Strings

Combines list elements.

Example

```python
names = ["A","B","C"]

",".join(names)
```

Output

```
A,B,C
```

---

# Case Methods

| Method | Description |
|----------|-------------|
| upper() | Uppercase |
| lower() | Lowercase |
| title() | Title Case |
| capitalize() | First letter uppercase |
| swapcase() | Reverse cases |

---

# Check Methods

| Method | Description |
|----------|-------------|
| isalpha() | Letters only |
| isdigit() | Digits only |
| isalnum() | Letters and digits |
| islower() | Lowercase |
| isupper() | Uppercase |
| isspace() | Spaces only |
| startswith() | Starts with value |
| endswith() | Ends with value |

---

# Strip Methods

Remove unwanted spaces.

```python
strip()

lstrip()

rstrip()
```

---

# String Algorithms

## Palindrome

Reads the same forward and backward.

Examples

```
madam

level

racecar
```

Check

```python
text == text[::-1]
```

---

## Anagram

Words with the same letters.

Examples

```
listen

silent
```

Check

```python
sorted(word1) == sorted(word2)
```

---

## Character Frequency

Counts occurrences of every character.

Example

```
apple

a : 1

p : 2

l : 1

e : 1
```

---

## Reverse Words

Input

```
Python is easy
```

Output

```
easy is Python
```

---

# Common String Patterns

## Count Vowels

```python
for character in text.lower():

    if character in "aeiou":
        count += 1
```

---

## Count Words

```python
len(sentence.split())
```

---

## Password Validation

Common checks:

- Minimum length
- Uppercase letter
- Lowercase letter
- Digit
- Special character

---

## Email Validation

Basic checks:

- Contains '@'
- Contains '.'
- No spaces

Production applications generally use **regular expressions (regex)** or validation libraries.

---

## String Compression

Example

Input

```
aaabbcccc
```

Output

```
a3b2c4
```

---

# Useful String Functions

| Function | Purpose |
|----------|----------|
| len() | Length |
| max() | Largest character |
| min() | Smallest character |
| sorted() | Sorted list |
| ord() | ASCII/Unicode value |
| chr() | Character from Unicode |

Example

```python
len("Python")
```

Output

```
6
```

---

# String Operators

## Concatenation

```python
"Hello" + " World"
```

Output

```
Hello World
```

---

## Repetition

```python
"Hi " * 3
```

Output

```
Hi Hi Hi
```

---

## Membership

```python
"Py" in "Python"
```

Returns

```
True
```

---

# Common Errors

## IndexError

Occurs when accessing an invalid index.

---

## TypeError

Occurs when trying to modify a string.

---

## ValueError

Occurs when `index()` cannot find a substring.

---

# Best Practices

- Use meaningful variable names.
- Prefer **f-strings** for formatting.
- Use `find()` when the substring may not exist.
- Use `strip()` before processing user input.
- Use `split()` for parsing text.
- Use `join()` instead of repeated string concatenation.
- Avoid modifying strings directly.
- Keep string operations simple and readable.

---

# Real-World Applications

Strings are used in:

- Login systems
- Registration forms
- Password validation
- Email validation
- Search engines
- File names
- CSV processing
- JSON processing
- Data cleaning
- Chat applications
- Web scraping
- Natural Language Processing (NLP)

---

# Quick Revision

| Concept | Description |
|----------|-------------|
| String | Sequence of characters |
| Immutable | Cannot be modified |
| Indexing | Access character |
| Slicing | Extract substring |
| Iteration | Traverse characters |
| find() | Returns index or -1 |
| index() | Returns index or ValueError |
| replace() | Replace substring |
| count() | Count occurrences |
| split() | String → List |
| join() | List → String |
| upper() | Uppercase |
| lower() | Lowercase |
| strip() | Remove spaces |
| f-string | Modern formatting |
| Palindrome | Same forward and backward |
| Anagram | Same letters |
| Character Frequency | Count characters |

---

# Summary

After completing this module, you can:

- Create strings using different quote styles.
- Access characters using indexing.
- Extract substrings using slicing.
- Reverse strings efficiently.
- Iterate through characters.
- Search and replace text.
- Format strings using modern techniques.
- Split and join strings.
- Use built-in string methods.
- Solve common string interview problems.
- Build real-world text-processing applications.

---

# Next Module

```
Phase 1 – Step 8

Lists
```

Topics include:

- List Creation
- Indexing
- Slicing
- List Methods
- Nested Lists
- List Comprehensions
- Sorting
- Searching
- Algorithms
- Practical List Problems