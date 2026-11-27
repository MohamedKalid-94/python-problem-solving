# Python Comprehensions - Notes

## 1. Introduction to Comprehensions

Comprehension is a Python feature used to create collections in a concise and readable way.

It is a Pythonic way to replace simple loops.

Traditional approach:

```python
result = []

for item in iterable:
    result.append(item)
```

Using comprehension:

```python
result = [
    item
    for item in iterable
]
```

---

# 2. Types of Comprehensions

Python supports:

```
1. List Comprehension
2. Dictionary Comprehension
3. Set Comprehension
4. Generator Expression
```

---

# 3. List Comprehension

## Definition

List comprehension creates a new list by applying an expression on every item of an iterable.

Syntax:

```python
[
expression
for item in iterable
]
```

Example:

```python
numbers = [
    x
    for x in range(5)
]

print(numbers)
```

Output:

```
[0,1,2,3,4]
```

---

## List Comprehension Flow

```
Iterable
   |
   ↓
Take one item
   |
   ↓
Apply expression
   |
   ↓
Store result
   |
   ↓
Create new list
```

---

## Examples

### Square numbers

```python
squares = [
    x*x
    for x in range(10)
]
```

---

### Convert strings

```python
names = [
    name.upper()
    for name in names
]
```

---

### Extract characters

```python
chars = [
    char
    for char in "Python"
]
```

---

# 4. Conditional List Comprehension

Used for filtering data.

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
    for x in range(20)
    if x % 2 == 0
]
```

Output:

```
[0,2,4,6,8,...]
```

---

# 5. If-Else List Comprehension

Used for transformation.

Syntax:

```python
[
value_if_true if condition else value_if_false
for item in iterable
]
```

Example:

```python
result = [
    "Even" if x%2==0 else "Odd"
    for x in range(10)
]
```

---

# 6. Dictionary Comprehension

## Definition

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
    x:x*x
    for x in range(5)
}
```

Output:

```
{
0:0,
1:1,
2:4,
3:9,
4:16
}
```

---

## Dictionary Transformation

Example:

```python
prices = {
    "Laptop":1000,
    "Phone":500
}


discount = {
    item:price*0.9
    for item,price in prices.items()
}
```

---

## Dictionary Filtering

Example:

```python
employees = {
    "Alice":90000,
    "Bob":40000
}


result = {
    name:salary
    for name,salary in employees.items()
    if salary > 50000
}
```

---

# 7. Set Comprehension

## Definition

Set comprehension creates unique collections.

Syntax:

```python
{
expression
for item in iterable
}
```

Example:

```python
unique = {
    x
    for x in [1,2,2,3]
}
```

Output:

```
{1,2,3}
```

---

## Set Characteristics

```
No duplicates
Fast lookup
Unordered collection
```

---

# 8. Nested Comprehension

Nested comprehension is used for multi-dimensional data.

Syntax:

```python
[
expression
for outer_item in outer
for inner_item in inner
]
```

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

```
[
[0,1,2],
[0,1,2],
[0,1,2]
]
```

---

# 9. Flattening Nested Lists

Example:

Input:

```python
matrix = [
    [1,2],
    [3,4]
]
```

Comprehension:

```python
flat = [
    value
    for row in matrix
    for value in row
]
```

Output:

```
[1,2,3,4]
```

---

# 10. Conditional Comprehension

Used for:

- Filtering
- Cleaning
- Validation
- Transformation

Example:

Remove empty values:

```python
cleaned = [
    value
    for value in values
    if value
]
```

---

# 11. Comprehensions in Data Processing

Common use cases:

## JSON Processing

```python
names = [
    user["name"]
    for user in users
]
```

---

## API Response Transformation

```python
user_map = {
    user["id"]:user["name"]
    for user in response
}
```

---

## File Processing

```python
python_files = [
    file
    for file in files
    if file.endswith(".py")
]
```

---

# 12. Comprehensions in AI/GenAI

## RAG Document Filtering

Example:

```python
valid_chunks = [
    doc.page_content
    for doc in documents
    if len(doc.page_content) > 500
]
```

Purpose:

- Remove small chunks
- Prepare retrieval data


---

## Metadata Extraction

```python
metadata = {
    doc.id:doc.metadata
    for doc in documents
}
```

Used in:

- Vector databases
- Document search
- Retrieval systems

---

## Token Processing

```python
tokens = [
    word.lower()
    for word in sentence.split()
]
```

Used in:

- NLP preprocessing
- Text cleaning

---

# 13. Complexity Analysis

## Single comprehension

Example:

```python
[x for x in data]
```

Time Complexity:

```
O(n)
```

Space Complexity:

```
O(n)
```

Because a new collection is created.

---

## Nested comprehension

Example:

```python
[
x
for row in matrix
for x in row
]
```

Complexity:

```
O(rows * columns)
```

---

# 14. Comprehension vs Loop

| Feature | Loop | Comprehension |
|-|-|-|
| Readability | More lines | Compact |
| Debugging | Easier | Harder |
| Complex logic | Better | Avoid |
| Simple transformation | More code | Better |
| Pythonic style | Normal | Preferred |

---

# 15. Best Practices

## Use comprehension when:

✅ Simple transformation  
✅ Filtering data  
✅ Creating collections  
✅ Processing JSON data  


## Avoid comprehension when:

❌ Multiple nested loops  
❌ Complex business logic  
❌ Many conditions  
❌ Difficult to understand  

---

# 16. Common Mistakes

## Mistake 1: Overusing nested comprehension

Bad:

```python
[
z
for x in data
for y in x
for z in y
]
```

Better:

Use normal loops.

---

## Mistake 2: Forgetting memory usage

Large list:

```python
[x for x in range(10000000)]
```

creates a large list.

Use generator:

```python
(x for x in range(10000000))
```

---

# 17. Quick Revision

```
List Comprehension
        |
        ↓
Creates lists


Dictionary Comprehension
        |
        ↓
Creates key-value pairs


Set Comprehension
        |
        ↓
Creates unique values


Nested Comprehension
        |
        ↓
Handles multi-dimensional data


Conditional Comprehension
        |
        ↓
Filters and transforms data
```

---

# 18. AI Engineer Takeaway

Comprehensions are not just syntax shortcuts.

They are useful for:

- Data preprocessing
- JSON transformation
- Dataset cleaning
- RAG pipelines
- Embedding preparation
- API response handling

A good AI Engineer should write clean, readable Python data-processing code.