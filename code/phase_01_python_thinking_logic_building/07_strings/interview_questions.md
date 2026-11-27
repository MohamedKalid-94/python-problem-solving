# Phase 1 - Step 7: Strings Interview Questions & Answers

## Overview

This document contains the most frequently asked **Python String Interview Questions**, starting from beginner level to intermediate level.

Topics Covered:

- String Basics
- String Creation
- Indexing
- Slicing
- Iteration
- Searching
- Replacing
- Formatting
- Splitting
- Joining
- String Methods
- String Algorithms
- Real-world String Problems

---

# Beginner Level

## 1. What is a string in Python?

### Answer

A string is a sequence of characters enclosed within single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`).

Example

```python
name = "Python"
```

---

## 2. How do you create a string?

### Answer

Strings can be created using:

```python
name = "Python"

language = 'Python'

message = """Hello
World"""
```

---

## 3. Are Python strings mutable?

### Answer

No.

Python strings are **immutable**, meaning they cannot be modified after creation.

Wrong

```python
text = "Python"

text[0] = "J"
```

Produces

```
TypeError
```

Correct

```python
text = "Python"

text = "J" + text[1:]
```

---

## 4. What is indexing?

### Answer

Indexing is accessing individual characters using their position.

Example

```python
text = "Python"

print(text[0])
```

Output

```
P
```

---

## 5. What is positive indexing?

### Answer

Positive indexing starts from **0**.

```
Python

P  y  t  h  o  n

0  1  2  3  4  5
```

---

## 6. What is negative indexing?

### Answer

Negative indexing starts from **-1**.

```
Python

P  y  t  h  o  n

-6 -5 -4 -3 -2 -1
```

---

## 7. What happens if you access an invalid index?

### Answer

Python raises

```
IndexError
```

Example

```python
text = "Python"

print(text[20])
```

---

## 8. What is slicing?

### Answer

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

## 9. How do you reverse a string?

### Answer

Using slicing.

```python
text = "Python"

print(text[::-1])
```

Output

```
nohtyP
```

---

## 10. What does the step value mean in slicing?

### Answer

The third value specifies how many positions to move.

Example

```python
text[::2]
```

Returns every second character.

---

# String Iteration

## 11. How do you iterate through a string?

### Answer

Using a `for` loop.

```python
for character in text:
    print(character)
```

---

## 12. Can strings be iterated using a while loop?

### Answer

Yes.

```python
index = 0

while index < len(text):
    print(text[index])
    index += 1
```

---

## 13. What does enumerate() do?

### Answer

It returns both the index and the value.

Example

```python
for index, character in enumerate(text):
    print(index, character)
```

---

# Searching & Replacing

## 14. What does find() do?

### Answer

Returns the position of a substring.

Returns **-1** if not found.

Example

```python
text.find("Python")
```

---

## 15. What does index() do?

### Answer

Returns the position of a substring.

Raises

```
ValueError
```

if not found.

---

## 16. Difference between find() and index()?

### Answer

| find() | index() |
|----------|----------|
| Returns -1 | Raises ValueError |
| Safe search | Strict search |

---

## 17. What does replace() do?

### Answer

Replaces one substring with another.

Example

```python
text.replace("Java", "Python")
```

---

## 18. What does count() do?

### Answer

Counts occurrences of a substring.

Example

```python
text.count("a")
```

---

# String Formatting

## 19. What is an f-string?

### Answer

An f-string is the modern way to format strings.

Example

```python
name = "Kalid"

print(f"Hello {name}")
```

---

## 20. What is format()?

### Answer

A built-in method used to format strings.

Example

```python
print("Hello {}".format(name))
```

---

## 21. What is percentage (%) formatting?

### Answer

Older style formatting.

Example

```python
print("%s" % name)
```

---

## 22. Which formatting method is recommended?

### Answer

**f-strings** are recommended because they are:

- Faster
- Cleaner
- More readable

---

# Splitting & Joining

## 23. What does split() do?

### Answer

Splits a string into a list.

Example

```python
sentence.split()
```

---

## 24. What does splitlines() do?

### Answer

Splits multiline text into a list.

---

## 25. What does join() do?

### Answer

Joins list elements into a string.

Example

```python
",".join(names)
```

---

# String Methods

## 26. What does upper() do?

### Answer

Converts all letters to uppercase.

Example

```python
text.upper()
```

---

## 27. What does lower() do?

### Answer

Converts all letters to lowercase.

---

## 28. Difference between capitalize() and title()?

### Answer

| capitalize() | title() |
|--------------|----------|
| First letter only | Every word |

---

## 29. What does strip() do?

### Answer

Removes spaces from both ends.

Example

```python
text.strip()
```

---

## 30. Difference between strip(), lstrip(), and rstrip()?

### Answer

| Method | Removes |
|----------|----------|
| strip() | Both sides |
| lstrip() | Left side |
| rstrip() | Right side |

---

## 31. What does isalpha() check?

### Answer

Returns **True** if all characters are letters.

---

## 32. What does isdigit() check?

### Answer

Returns **True** if all characters are digits.

---

## 33. What does isalnum() check?

### Answer

Returns **True** if the string contains only letters and numbers.

---

## 34. What does startswith() do?

### Answer

Checks whether a string starts with a given value.

Example

```python
text.startswith("Py")
```

---

## 35. What does endswith() do?

### Answer

Checks whether a string ends with a given value.

---

# String Algorithms

## 36. What is a palindrome?

### Answer

A palindrome reads the same forward and backward.

Examples

```
madam

level

racecar
```

---

## 37. How do you check a palindrome?

### Answer

```python
text == text[::-1]
```

---

## 38. What is an anagram?

### Answer

Two words containing the same letters.

Example

```
listen

silent
```

---

## 39. How do you check an anagram?

### Answer

```python
sorted(word1) == sorted(word2)
```

---

## 40. How do you count character frequency?

### Answer

Using

```python
count()
```

or

a dictionary.

---

# Scenario-Based Questions

## 41. How do you count vowels?

### Answer

```python
count = 0

for character in text.lower():

    if character in "aeiou":
        count += 1
```

---

## 42. How do you count words?

### Answer

```python
len(sentence.split())
```

---

## 43. How do you validate a password?

### Answer

Check for:

- Minimum length
- Uppercase letter
- Lowercase letter
- Number
- Special character

---

## 44. How do you validate an email?

### Answer

Basic validation checks:

- Contains '@'
- Contains '.'
- No spaces

Production applications usually use **regular expressions (regex)** or dedicated validation libraries.

---

## 45. How do you reverse words in a sentence?

### Answer

```python
sentence.split()[::-1]
```

Then join using

```python
" ".join(...)
```

---

# Advanced Questions

## 46. Why are strings immutable?

### Answer

Immutability provides:

- Better performance
- Better security
- Hashability
- Safe memory optimization

---

## 47. What is string concatenation?

### Answer

Joining two or more strings.

Example

```python
first = "Hello"

second = "World"

print(first + second)
```

---

## 48. How do you repeat a string?

### Answer

Using `*`

Example

```python
print("Hi " * 3)
```

Output

```
Hi Hi Hi
```

---

## 49. How do you compare two strings?

### Answer

Using comparison operators.

Example

```python
if word1 == word2:
    print("Equal")
```

---

## 50. What are common real-world applications of strings?

### Answer

Strings are used in:

- Login systems
- Email validation
- Password validation
- Text processing
- Chat applications
- Search engines
- File handling
- CSV processing
- Data cleaning
- Natural Language Processing (NLP)

---

# Quick Revision Table

| Concept | Key Point |
|----------|-----------|
| String | Sequence of characters |
| Immutable | Cannot be modified after creation |
| Indexing | Access a single character |
| Slicing | Extract part of a string |
| Iteration | Visit each character |
| find() | Returns index or -1 |
| index() | Returns index or raises ValueError |
| replace() | Replaces text |
| count() | Counts occurrences |
| split() | Converts string to list |
| join() | Converts list to string |
| upper() | Uppercase |
| lower() | Lowercase |
| strip() | Removes spaces |
| f-string | Modern formatting |
| Palindrome | Same forward and backward |
| Anagram | Same letters |
| Character Frequency | Counts each character |

---

# Interview Checklist

- [ ] Explain strings
- [ ] Explain immutability
- [ ] Explain indexing
- [ ] Explain slicing
- [ ] Explain negative indexing
- [ ] Reverse a string
- [ ] Explain string iteration
- [ ] Compare `find()` and `index()`
- [ ] Explain `replace()` and `count()`
- [ ] Explain `split()` and `join()`
- [ ] Explain string formatting methods
- [ ] Explain common string methods
- [ ] Solve palindrome problems
- [ ] Solve anagram problems
- [ ] Count character frequencies
- [ ] Count vowels and words
- [ ] Explain password and email validation
- [ ] Explain why strings are immutable