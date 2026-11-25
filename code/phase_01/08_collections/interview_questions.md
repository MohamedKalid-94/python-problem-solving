# Phase 1 - Step 8: Collections Interview Questions & Answers

## Overview

This document contains the most frequently asked **Python Collections Interview Questions**, covering:

- Lists
- Tuples
- Sets
- Dictionaries
- Nested Collections
- Searching
- Sorting
- Copying
- Common Collection Algorithms

---

# Lists

## 1. What is a list in Python?

### Answer

A list is an **ordered, mutable collection** that can store multiple items of different data types.

Example

```python
numbers = [10, 20, 30]
```

---

## 2. What are the characteristics of a list?

### Answer

- Ordered
- Mutable
- Allows duplicates
- Dynamic size
- Supports indexing
- Supports slicing

---

## 3. How do you create a list?

```python
numbers = [1, 2, 3]
```

---

## 4. How do you access list elements?

Using indexing.

```python
numbers[0]
numbers[-1]
```

---

## 5. What is negative indexing?

Negative indexing starts from the end.

```
Python List

10 20 30 40

0  1  2  3

-4 -3 -2 -1
```

---

## 6. What is slicing?

Extracting a portion of a list.

```python
numbers[1:4]
```

---

## 7. How do you reverse a list?

Method 1

```python
numbers.reverse()
```

Method 2

```python
numbers[::-1]
```

---

## 8. Difference between append() and insert()?

| append() | insert() |
|-----------|----------|
| Adds at end | Adds at specific position |

---

## 9. Difference between extend() and append()?

### append()

Adds one object.

```python
a.append([4,5])
```

Output

```
[1,2,3,[4,5]]
```

### extend()

Adds every element.

```python
a.extend([4,5])
```

Output

```
[1,2,3,4,5]
```

---

## 10. Difference between remove() and pop()?

| remove() | pop() |
|-----------|--------|
| Removes by value | Removes by index |

---

## 11. Difference between sort() and sorted()?

| sort() | sorted() |
|----------|----------|
| Changes original list | Returns new list |

---

## 12. Difference between reverse() and reversed()?

| reverse() | reversed() |
|------------|------------|
| Changes original | Returns iterator |

---

## 13. How do you check whether an element exists?

```python
if 20 in numbers:
    print("Found")
```

---

## 14. What does index() do?

Returns first occurrence.

```python
numbers.index(20)
```

---

## 15. What does count() do?

Counts occurrences.

```python
numbers.count(20)
```

---

# Copying Lists

## 16. What happens during assignment?

```python
a = [1,2]

b = a
```

Both variables reference the same list.

---

## 17. How do you copy a list?

```python
b = a.copy()
```

---

## 18. Copy using slicing?

```python
b = a[:]
```

---

## 19. Difference between shallow and deep copy?

### Shallow Copy

Copies outer object only.

Nested objects remain shared.

### Deep Copy

Copies every nested object.

Uses

```python
copy.deepcopy()
```

---

# Tuples

## 20. What is a tuple?

A tuple is an **ordered, immutable collection**.

```python
numbers = (1,2,3)
```

---

## 21. Difference between list and tuple?

| List | Tuple |
|-------|-------|
| Mutable | Immutable |
| [] | () |

---

## 22. Why use tuples?

- Faster
- Read-only data
- Safe
- Can be dictionary keys

---

## 23. What is tuple unpacking?

```python
name, age = ("Alice",25)
```

---

## 24. Tuple methods?

Only two methods:

```python
count()

index()
```

---

# Sets

## 25. What is a set?

An unordered collection of unique values.

```python
numbers = {1,2,3}
```

---

## 26. Why use sets?

- Remove duplicates
- Fast searching
- Mathematical operations

---

## 27. Can a set contain duplicates?

No.

Duplicates are automatically removed.

---

## 28. Difference between remove() and discard()?

| remove() | discard() |
|-----------|-----------|
| Error if missing | No error |

---

## 29. What is union?

Combines both sets.

```python
A | B
```

---

## 30. What is intersection?

Common values.

```python
A & B
```

---

## 31. What is difference?

Elements only in first set.

```python
A - B
```

---

## 32. What is symmetric difference?

Elements present in either set but not both.

```python
A ^ B
```

---

# Dictionaries

## 33. What is a dictionary?

Stores key-value pairs.

```python
student = {
    "name":"Alice",
    "age":25
}
```

---

## 34. Characteristics of dictionaries

- Mutable
- Ordered (Python 3.7+)
- Unique keys
- Fast lookup

---

## 35. Difference between key and value?

Key identifies data.

Value stores information.

Example

```
"name" : "Alice"

Key     Value
```

---

## 36. How do you access dictionary values?

```python
student["name"]
```

or

```python
student.get("name")
```

---

## 37. Difference between [] and get()?

| [] | get() |
|----|--------|
| KeyError | Returns None/default |

---

## 38. How do you update values?

```python
student["age"] = 30
```

---

## 39. How do you add new key-value pairs?

```python
student["city"] = "Chennai"
```

---

## 40. How do you delete dictionary items?

```python
del student["age"]
```

or

```python
student.pop("age")
```

---

## 41. What do keys(), values(), and items() return?

```python
keys()

values()

items()
```

---

## 42. How do you iterate through a dictionary?

```python
for key, value in student.items():
    print(key, value)
```

---

# Nested Collections

## 43. What is a nested list?

A list containing another list.

```python
matrix = [
    [1,2],
    [3,4]
]
```

---

## 44. What is a list of dictionaries?

```python
students = [
    {"name":"A"},
    {"name":"B"}
]
```

---

## 45. What is a dictionary of lists?

```python
student = {
    "subjects":["Python","SQL"]
}
```

---

## 46. What is a nested dictionary?

```python
company = {
    "emp1":{
        "name":"Alice"
    }
}
```

---

# Scenario-Based Questions

## 47. How do you remove duplicates?

```python
list(set(numbers))
```

---

## 48. How do you count frequencies?

```python
frequency[item] = frequency.get(item,0)+1
```

---

## 49. How do you sort a dictionary?

```python
sorted(dictionary.items())
```

---

## 50. How do you merge dictionaries?

```python
merged = dict1 | dict2
```

(Python 3.9+)

or

```python
dict1.update(dict2)
```

---

# Advanced Questions

## 51. Which collection is fastest for searching?

Set

Average complexity:

```
O(1)
```

---

## 52. Which collection allows duplicate values?

- Lists
- Tuples
- Dictionaries (values)

Sets do not.

---

## 53. Which collection allows duplicate keys?

None.

Dictionary keys must be unique.

---

## 54. Which collection is immutable?

Tuple

---

## 55. Can lists contain different data types?

Yes.

```python
[1,"Python",3.14,True]
```

---

## 56. Can dictionary keys be lists?

No.

Lists are mutable.

Keys must be immutable.

---

## 57. Which objects can be dictionary keys?

Examples

- int
- float
- string
- tuple

---

## 58. Difference between mutable and immutable collections?

| Mutable | Immutable |
|----------|-----------|
| List | Tuple |
| Dictionary | String |
| Set | Integer |

---

## 59. Time complexity of searching?

| Collection | Average |
|------------|----------|
| List | O(n) |
| Tuple | O(n) |
| Set | O(1) |
| Dictionary | O(1) |

---

## 60. Real-world uses of collections?

Lists

- Shopping cart
- Playlist
- Student marks

Tuples

- Coordinates
- Database records

Sets

- Unique visitors
- Tags
- Duplicate removal

Dictionaries

- Employee records
- JSON data
- Contact book
- Configuration files

---

# Quick Revision Table

| Collection | Ordered | Mutable | Duplicates |
|------------|----------|----------|------------|
| List | ✅ | ✅ | ✅ |
| Tuple | ✅ | ❌ | ✅ |
| Set | ❌ | ✅ | ❌ |
| Dictionary | ✅ | ✅ | Keys ❌ Values ✅ |

---

# Common Interview Programs

Practice writing these without looking at notes:

- Create a list.
- Reverse a list.
- Sort a list.
- Find duplicates.
- Remove duplicates.
- Find the maximum and minimum values.
- Count element frequency.
- Merge two lists.
- Merge two dictionaries.
- Create a student record system.
- Implement a contact book.
- Perform set operations.
- Use tuple unpacking.
- Traverse nested collections.
- Copy lists using different methods.
- Demonstrate shallow vs deep copy.

---

# Interview Checklist

- [ ] Explain Lists.
- [ ] Explain Tuples.
- [ ] Explain Sets.
- [ ] Explain Dictionaries.
- [ ] Compare all collection types.
- [ ] Explain mutability.
- [ ] Explain indexing and slicing.
- [ ] Explain list methods.
- [ ] Explain dictionary methods.
- [ ] Explain set operations.
- [ ] Explain tuple unpacking.
- [ ] Explain shallow vs deep copy.
- [ ] Solve duplicate removal problems.
- [ ] Solve frequency counter problems.
- [ ] Work with nested collections.
- [ ] Build simple CRUD programs using collections.
```