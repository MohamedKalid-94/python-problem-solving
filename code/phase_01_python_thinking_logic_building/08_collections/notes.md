# Phase 1 - Step 8: Collections Notes

## Overview

Python Collections are data structures used to store and manage multiple values in a single variable.

Python provides four main built-in collection types:

1. List
2. Tuple
3. Set
4. Dictionary

Collections help in:

- Storing data
- Searching data
- Updating information
- Removing data
- Sorting data
- Processing large amounts of information

---

# 1. Lists

## What is a List?

A list is an **ordered, mutable collection** that stores multiple values.

Example:

```python
numbers = [10, 20, 30, 40]
```

---

## Characteristics of Lists

- Ordered
- Mutable
- Allows duplicate values
- Supports indexing
- Supports slicing
- Dynamic size
- Can store different data types

Example:

```python
data = [10, "Python", 3.14, True]
```

---

# Creating Lists

## Empty List

```python
numbers = []
```

---

## List with Values

```python
numbers = [1,2,3,4]
```

---

## Mixed Data Types

```python
data = [
    10,
    "Python",
    5.5,
    True
]
```

---

# List Indexing

Lists use index positions to access elements.

Example:

```python
fruits = [
    "Apple",
    "Banana",
    "Orange"
]
```

Index:

```
Apple    Banana    Orange
 0         1          2
```

Access:

```python
fruits[0]
```

Output:

```
Apple
```

---

# Negative Indexing

Negative indexes start from the end.

```
Apple    Banana    Orange

-3        -2        -1
```

Example:

```python
fruits[-1]
```

Output:

```
Orange
```

---

# List Slicing

Slicing extracts a portion of a list.

Syntax:

```python
list[start:stop:step]
```

Example:

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

Output:

```
[20,30,40]
```

---

## Reverse List

```python
numbers[::-1]
```

---

## Step Slicing

```python
numbers[::2]
```

Output:

```
[10,30,50]
```

---

# List Operations

## append()

Adds element at the end.

```python
numbers.append(60)
```

---

## insert()

Adds element at specific position.

```python
numbers.insert(1,15)
```

---

## extend()

Adds multiple elements.

```python
numbers.extend([70,80])
```

---

## remove()

Removes element by value.

```python
numbers.remove(20)
```

---

## pop()

Removes element by index.

```python
numbers.pop()
```

Default removes last element.

---

## clear()

Removes all elements.

```python
numbers.clear()
```

---

# Updating Lists

Lists are mutable.

Example:

```python
numbers[0] = 100
```

Before:

```
[10,20,30]
```

After:

```
[100,20,30]
```

---

# Traversing Lists

## Using for Loop

```python
for item in numbers:
    print(item)
```

---

## Using while Loop

```python
index = 0

while index < len(numbers):

    print(numbers[index])

    index += 1
```

---

## Using enumerate()

Returns index and value.

```python
for index,value in enumerate(numbers):

    print(index,value)
```

---

# Searching in Lists

## in Operator

Checks existence.

```python
20 in numbers
```

---

## index()

Returns position.

```python
numbers.index(20)
```

---

## count()

Counts occurrences.

```python
numbers.count(20)
```

---

# Sorting Lists

## sort()

Changes original list.

```python
numbers.sort()
```

Descending:

```python
numbers.sort(reverse=True)
```

---

## sorted()

Creates new sorted list.

```python
new_list = sorted(numbers)
```

---

# Reversing Lists

## reverse()

```python
numbers.reverse()
```

---

## Slicing Method

```python
numbers[::-1]
```

---

# Copying Lists

## Assignment Copy

```python
list2 = list1
```

Both variables point to same object.

---

## copy()

```python
list2 = list1.copy()
```

Creates independent copy.

---

## Slice Copy

```python
list2 = list1[:]
```

---

# Shallow Copy

Copies only outer object.

Example:

```python
import copy

copy.copy(data)
```

Nested objects are shared.

---

# Deep Copy

Copies all nested objects.

```python
copy.deepcopy(data)
```

---

# 2. Tuples

## What is a Tuple?

A tuple is an ordered and immutable collection.

Example:

```python
numbers = (10,20,30)
```

---

# Tuple Characteristics

- Ordered
- Immutable
- Allows duplicates
- Faster than lists
- Supports indexing
- Supports slicing

---

# Creating Tuple

```python
values = (1,2,3)
```

Single element tuple:

```python
value = (10,)
```

---

# Tuple Access

```python
values[0]
```

---

# Tuple Slicing

```python
values[1:3]
```

---

# Tuple Unpacking

Example:

```python
student = (
    "Kalid",
    25,
    "Python"
)

name,age,course = student
```

---

# Tuple Methods

Only two methods:

## count()

```python
numbers.count(10)
```

## index()

```python
numbers.index(20)
```

---

# List vs Tuple

| List | Tuple |
|-|-|
| Mutable | Immutable |
| [] | () |
| More memory | Less memory |
| More methods | Limited methods |

---

# 3. Sets

## What is a Set?

A set is an unordered collection of unique values.

Example:

```python
numbers = {1,2,3}
```

---

# Set Characteristics

- Unordered
- Mutable
- No duplicates
- Fast searching

---

# Creating Set

```python
numbers = {10,20,30}
```

Empty set:

```python
set()
```

---

# Adding Elements

```python
numbers.add(40)
```

---

# Removing Elements

## remove()

```python
numbers.remove(20)
```

Raises error if value does not exist.

---

## discard()

```python
numbers.discard(20)
```

No error.

---

# Set Operations

## Union

Combines values.

```python
A | B
```

---

## Intersection

Common values.

```python
A & B
```

---

## Difference

Values only in A.

```python
A - B
```

---

## Symmetric Difference

Different values from both sets.

```python
A ^ B
```

---

# 4. Dictionaries

## What is a Dictionary?

A dictionary stores data as key-value pairs.

Example:

```python
student = {

"name":"Kalid",

"age":25

}
```

---

# Dictionary Characteristics

- Mutable
- Ordered
- Keys are unique
- Fast lookup

---

# Creating Dictionary

```python
person = {

"name":"John",

"age":30

}
```

---

# Accessing Values

Using key:

```python
person["name"]
```

Using get():

```python
person.get("name")
```

---

# Adding Values

```python
person["city"]="Chennai"
```

---

# Updating Values

```python
person["age"]=31
```

---

# Removing Values

## del

```python
del person["age"]
```

---

## pop()

```python
person.pop("age")
```

---

# Dictionary Methods

## keys()

Returns keys.

```python
person.keys()
```

---

## values()

Returns values.

```python
person.values()
```

---

## items()

Returns key-value pairs.

```python
person.items()
```

---

# Dictionary Traversal

```python
for key,value in person.items():

    print(key,value)
```

---

# Nested Collections

Collections can contain other collections.

---

# Nested List

Example:

```python
matrix = [

[1,2,3],

[4,5,6]

]
```

Access:

```python
matrix[0][1]
```

---

# List of Dictionaries

Example:

```python
students = [

{
"name":"A"
},

{
"name":"B"
}

]
```

---

# Dictionary of Lists

Example:

```python
student = {

"subjects":[
"Python",
"SQL"
]

}
```

---

# Nested Dictionary

Example:

```python
company = {

"employee":{

"name":"John"

}

}
```

---

# Collection Algorithms

## Frequency Counter

Count occurrences.

Example:

```python
numbers=[1,2,2,3]
```

Output:

```python
{
1:1,
2:2,
3:1
}
```

Implementation:

```python
frequency[item] = frequency.get(item,0)+1
```

---

# Remove Duplicates

Using set:

```python
unique = list(set(numbers))
```

---

# Collection Comparison

| Collection | Ordered | Mutable | Duplicate |
|-|-|-|-|
| List | Yes | Yes | Yes |
| Tuple | Yes | No | Yes |
| Set | No | Yes | No |
| Dictionary | Yes | Yes | Keys No |

---

# Real World Applications

## Lists

Used for:

- Shopping carts
- Student marks
- Playlist

---

## Tuples

Used for:

- Coordinates
- Database records
- Fixed configuration

---

## Sets

Used for:

- Removing duplicates
- Unique users
- Tags

---

## Dictionaries

Used for:

- JSON data
- User profiles
- Configuration
- Database records

---

# Important Interview Concepts

## Mutable Collections

Can change after creation:

- List
- Set
- Dictionary

---

## Immutable Collections

Cannot change:

- Tuple

---

## Fast Searching

Set and Dictionary:

Average:

```
O(1)
```

List:

```
O(n)
```

---

# Final Learning Checklist

- [ ] Understand Lists
- [ ] Perform List Operations
- [ ] Traverse Lists
- [ ] Search and Sort Lists
- [ ] Copy Lists
- [ ] Understand Shallow and Deep Copy
- [ ] Understand Tuples
- [ ] Understand Sets
- [ ] Perform Set Operations
- [ ] Understand Dictionaries
- [ ] Work with Nested Collections
- [ ] Solve Collection Algorithms
- [ ] Build Real-World Collection Programs