# Python Comprehensions - Interview Q&A

## 1. What is comprehension in Python?

### Answer

Comprehension is a Python feature used to create collections in a shorter and cleaner way.

It reduces the need for traditional loops with `append()` operations.

Python supports:

- List comprehension
- Dictionary comprehension
- Set comprehension
- Generator expression

Example:

```python
numbers = [x for x in range(5)]

print(numbers)
```

Output:

```text
[0, 1, 2, 3, 4]
```

---

# List Comprehension

## 2. What is list comprehension?

### Answer

List comprehension is a way to create a new list from an existing iterable.

Syntax:

```python
[expression for item in iterable]
```

Example:

```python
squares = [
    x * x
    for x in range(5)
]

print(squares)
```

Output:

```text
[0, 1, 4, 9, 16]
```

---

## 3. Difference between normal loop and list comprehension?

### Normal loop

```python
numbers = []

for i in range(5):
    numbers.append(i)
```

### List comprehension

```python
numbers = [
    i
    for i in range(5)
]
```

Both produce the same result.

Comprehension provides:

- Less code
- Better readability
- Pythonic style

---

## 4. How to add condition in list comprehension?

Syntax:

```python
[
expression
for item in iterable
if condition
]
```

Example:

```python
even_numbers = [
    x
    for x in range(10)
    if x % 2 == 0
]
```

Output:

```text
[0,2,4,6,8]
```

---

## 5. Difference between filtering and if-else comprehension?

### Filtering

Removes unwanted values.

```python
[
x
for x in numbers
if x > 5
]
```

### if-else

Transforms values.

```python
[
"Even" if x%2==0 else "Odd"
for x in numbers
]
```

---

# Dictionary Comprehension

## 6. What is dictionary comprehension?

### Answer

Dictionary comprehension creates dictionaries dynamically.

Syntax:

```python
{
key:value
for item in iterable
}
```

Example:

```python
squares = {
    x: x*x
    for x in range(5)
}
```

Output:

```text
{
0:0,
1:1,
2:4,
3:9,
4:16
}
```

---

## 7. How to filter dictionary using comprehension?

Example:

```python
marks = {
    "Alice":90,
    "Bob":40,
    "Chris":80
}


passed = {
    name:score
    for name,score in marks.items()
    if score >= 50
}
```

Output:

```text
{
"Alice":90,
"Chris":80
}
```

---

## 8. How to swap dictionary keys and values?

Example:

```python
data = {
    "Python":1,
    "Java":2
}


result = {
    value:key
    for key,value in data.items()
}
```

Output:

```text
{
1:"Python",
2:"Java"
}
```

---

# Set Comprehension

## 9. What is set comprehension?

### Answer

Set comprehension creates a set using comprehension syntax.

Example:

```python
numbers = {
    x
    for x in [1,2,2,3]
}

print(numbers)
```

Output:

```text
{1,2,3}
```

Duplicates are automatically removed.

---

## 10. Difference between list comprehension and set comprehension?

| List | Set |
|-|-|
| Allows duplicates | Removes duplicates |
| Maintains order | No guaranteed order |
| Uses [] | Uses {} |

Example:

List:

```python
[1,1,2]
```

Set:

```python
{1,2}
```

---

# Nested Comprehension

## 11. What is nested comprehension?

### Answer

Nested comprehension is used when one loop exists inside another loop.

Example:

```python
matrix = [
    [
        j
        for j in range(3)
    ]
    for i in range(3)
]
```

Output:

```text
[
[0,1,2],
[0,1,2],
[0,1,2]
]
```

---

## 12. How to flatten a nested list?

Example:

```python
matrix = [
    [1,2],
    [3,4]
]


result = [
    value
    for row in matrix
    for value in row
]
```

Output:

```text
[1,2,3,4]
```

---

# Conditional Comprehension

## 13. What is conditional comprehension?

### Answer

Conditional comprehension applies filtering or transformation based on conditions.

Example:

```python
positive_numbers = [
    x
    for x in numbers
    if x > 0
]
```

---

## 14. Can we use multiple conditions?

Yes.

Example:

```python
result = [
    x
    for x in range(100)
    if x % 2 == 0
    if x % 5 == 0
]
```

Output:

```text
[10,20,30,...]
```

---

# Performance and Complexity

## 15. Are comprehensions faster than loops?

### Answer

Usually yes.

Python optimizes comprehension internally.

Example:

```python
[x for x in range(10000)]
```

is generally faster than:

```python
result=[]

for x in range(10000):
    result.append(x)
```

---

## 16. What is the time complexity of comprehension?

For one loop:

```python
[x for x in data]
```

Time complexity:

```text
O(n)
```

Space complexity:

```text
O(n)
```

Because a new collection is created.

---

## 17. When should we avoid comprehensions?

Avoid when:

- Logic is complicated
- Too many nested loops
- Multiple operations are required
- Debugging is difficult

Example:

Bad:

```python
[
x
for a in data
for b in a
for c in b
if condition(c)
]
```

Normal loops are better.

---

# AI / GenAI Related Questions

## 18. How are comprehensions used in AI projects?

### Answer

Common use cases:

### RAG document filtering

```python
chunks = [
    doc.page_content
    for doc in documents
    if len(doc.page_content) > 500
]
```

### Extract metadata

```python
metadata = {
    doc.id:doc.metadata
    for doc in documents
}
```

### Token processing

```python
tokens = [
    word.lower()
    for word in text.split()
]
```

---

## 19. List comprehension vs generator expression?

### List comprehension

```python
[x for x in range(10000)]
```

- Creates complete list
- More memory usage


### Generator expression

```python
(x for x in range(10000))
```

- Creates values lazily
- Less memory usage

---

## 20. Why are comprehensions important for Python AI Engineers?

### Answer

AI systems frequently process:

- JSON data
- Documents
- Embeddings
- API responses
- Dataset records

Comprehensions help write:

- Cleaner data pipelines
- Faster transformations
- Readable preprocessing code

Examples:

- RAG chunk filtering
- Metadata extraction
- Token cleaning
- Dataset preparation

---

# Key Interview Summary

Remember:

```
List comprehension
        ↓
Create lists

Dictionary comprehension
        ↓
Create key-value mappings

Set comprehension
        ↓
Create unique collections

Nested comprehension
        ↓
Process multi-dimensional data

Conditional comprehension
        ↓
Filter and transform data
```

For AI Engineer interviews:

Focus on:

✅ List comprehension  
✅ Dictionary comprehension  
✅ Filtering  
✅ Nested data processing  
✅ JSON transformation  
✅ RAG preprocessing examples