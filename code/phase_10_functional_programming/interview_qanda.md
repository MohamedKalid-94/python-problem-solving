# Phase 10 — Functional Programming
# Interview Questions & Answers

---

# 1. What is Functional Programming?

**Answer:**

Functional Programming is a programming paradigm where computation is performed using functions.

Instead of modifying variables repeatedly, functional programming focuses on:

- Pure functions
- Immutable data
- Function composition
- Higher-order functions

Python supports functional programming through built-in functions like:

- map()
- filter()
- reduce()
- zip()
- enumerate()
- any()
- all()

---

# 2. What is map()?

**Answer:**

`map()` applies a function to every item in an iterable and returns a map object.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1,2,3]

result = map(lambda x:x*x, numbers)

print(list(result))
```

Output

```
[1,4,9]
```

---

# 3. When should you use map()?

**Answer**

Use map() when every element needs to be transformed.

Examples

- Convert strings to integers
- Convert Celsius to Fahrenheit
- Calculate GST
- Image preprocessing
- AI dataset transformation

---

# 4. What is filter()?

**Answer**

`filter()` selects elements that satisfy a condition.

Syntax

```python
filter(function, iterable)
```

Example

```python
numbers = [1,2,3,4]

result = filter(lambda x:x%2==0, numbers)

print(list(result))
```

Output

```
[2,4]
```

---

# 5. Difference between map() and filter()

| map() | filter() |
|--------|-----------|
| Transforms data | Filters data |
| Returns all elements | Returns selected elements |
| Applies function | Applies condition |

---

# 6. What is reduce()?

**Answer**

`reduce()` combines all elements into a single value.

It is available in:

```python
from functools import reduce
```

Example

```python
from functools import reduce

numbers = [1,2,3,4]

total = reduce(lambda x,y:x+y, numbers)
```

Output

```
10
```

---

# 7. Why is reduce() inside functools?

**Answer**

Because reduce() is used less frequently than map() and filter().

Python moved it to functools to keep the built-in namespace smaller.

---

# 8. What is zip()?

**Answer**

zip() combines multiple iterables element by element.

Example

```python
names = ["John","Alice"]

marks = [90,95]

print(list(zip(names, marks)))
```

Output

```
[('John',90),('Alice',95)]
```

---

# 9. What happens if zip() receives different length iterables?

**Answer**

zip() stops when the shortest iterable ends.

Example

```python
zip([1,2,3],[10,20])
```

Output

```
[(1,10),(2,20)]
```

---

# 10. What is enumerate()?

**Answer**

enumerate() returns both index and value.

Example

```python
languages = ["Python","Java"]

for index, value in enumerate(languages):
    print(index, value)
```

---

# 11. Why use enumerate() instead of range()?

**Answer**

enumerate()

- Cleaner
- Readable
- No manual indexing
- Less error-prone

---

# 12. What is any()?

**Answer**

Returns True if at least one element is True.

Example

```python
values = [False, False, True]

print(any(values))
```

Output

```
True
```

---

# 13. What is all()?

**Answer**

Returns True only if every element is True.

Example

```python
values = [True,True,False]

print(all(values))
```

Output

```
False
```

---

# 14. Difference between any() and all()

| any() | all() |
|--------|--------|
| One True is enough | Every value must be True |
| Logical OR | Logical AND |

---

# 15. What is sorted()?

**Answer**

sorted() returns a new sorted list.

Original data remains unchanged.

Example

```python
numbers = [4,2,8]

print(sorted(numbers))
```

---

# 16. Difference between sorted() and sort()

| sorted() | sort() |
|-----------|---------|
| Returns new list | Modifies original list |
| Works on iterable | Works only on list |

---

# 17. What is key in sorted()?

**Answer**

The key function determines how sorting happens.

Example

```python
words = ["Python","AI","MachineLearning"]

sorted(words, key=len)
```

Sorts according to string length.

---

# 18. Where else is key used?

Used in

- sorted()
- min()
- max()

---

# 19. What are Higher-Order Functions?

**Answer**

Higher-order functions either

- accept another function
- return another function

Example

```python
def calculate(operation,a,b):

    return operation(a,b)
```

---

# 20. Give examples of Higher-Order Functions.

Examples

- map()
- filter()
- reduce()
- sorted()
- min()
- max()

---

# 21. What is a callback function?

**Answer**

A callback is a function passed into another function.

Example

```python
def finished():

    print("Done")

def process(callback):

    callback()
```

---

# 22. Why are lambda functions commonly used with map()?

Because they are

- Short
- Anonymous
- Readable
- Useful for simple transformations

Example

```python
map(lambda x:x*x, numbers)
```

---

# 23. Can map() take multiple iterables?

Yes.

Example

```python
list(map(lambda x,y:x+y,[1,2],[10,20]))
```

Output

```
[11,22]
```

---

# 24. Is map() lazy?

Yes.

map() returns an iterator.

Data is generated only when needed.

---

# 25. Is filter() lazy?

Yes.

filter() returns an iterator.

---

# 26. Is zip() lazy?

Yes.

zip() also returns an iterator.

---

# 27. Is enumerate() lazy?

Yes.

enumerate() returns an iterator.

---

# 28. Advantages of Functional Programming

- Cleaner code
- Less repetition
- Easy testing
- Better readability
- Memory efficient
- Works well with iterators
- Suitable for pipelines

---

# 29. Real-world uses of Functional Programming

- Data cleaning
- ETL pipelines
- CSV processing
- API response processing
- Log analysis
- Machine Learning preprocessing
- AI dataset preparation
- RAG document chunking
- Feature engineering

---

# 30. Explain a Functional Programming pipeline.

Example

```
Raw Data
     │
     ▼
filter()
     │
     ▼
map()
     │
     ▼
sorted()
     │
     ▼
reduce()
     │
     ▼
Final Result
```

Each function performs one specific task, making the code modular, readable, and easy to maintain.

---

# Quick Revision

| Function | Purpose |
|----------|---------|
| map() | Transform data |
| filter() | Select data |
| reduce() | Combine data |
| zip() | Combine iterables |
| enumerate() | Index + Value |
| any() | At least one True |
| all() | All True |
| sorted() | Return sorted list |
| key | Custom sorting |
| Higher-order function | Accepts/returns functions |

---

# AI/GenAI Interview Applications

Functional programming is widely used in:

- Data preprocessing pipelines
- Feature engineering
- Text cleaning
- Batch processing
- LLM input transformation
- RAG document chunking
- Embedding generation pipelines
- API response processing
- Log analytics
- Streaming data processing

Understanding these concepts helps in writing clean, efficient, and scalable Python code for AI, Machine Learning, and Generative AI applications.