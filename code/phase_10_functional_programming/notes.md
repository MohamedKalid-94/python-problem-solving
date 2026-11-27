# Phase 10 — Functional Programming

## Overview

Functional Programming is a programming paradigm where computation is performed using functions instead of changing program state.

Instead of writing loops repeatedly, Python provides built-in functions that make code shorter, cleaner, and easier to maintain.

Functional programming is widely used in:

- Data Processing
- Backend Development
- Machine Learning
- AI/GenAI
- ETL Pipelines
- Data Engineering

---

# Functional Programming Principles

The main principles are:

- Functions are first-class objects.
- Functions can be passed as arguments.
- Functions can return other functions.
- Prefer immutable data.
- Avoid unnecessary side effects.
- Use small reusable functions.

---

# 1. map()

## Definition

`map()` applies a function to every element in an iterable.

Syntax

```python
map(function, iterable)
```

Example

```python
numbers = [1, 2, 3, 4]

squares = map(lambda x: x * x, numbers)

print(list(squares))
```

Output

```text
[1, 4, 9, 16]
```

---

## Multiple Iterables

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]

result = map(lambda x, y: x + y, list1, list2)

print(list(result))
```

Output

```text
[11, 22, 33]
```

---

## Uses

- Data transformation
- Unit conversion
- Image preprocessing
- Text processing
- AI dataset transformation

---

# 2. filter()

## Definition

`filter()` selects elements that satisfy a condition.

Syntax

```python
filter(function, iterable)
```

Example

```python
numbers = [1,2,3,4,5,6]

even = filter(lambda x:x%2==0, numbers)

print(list(even))
```

Output

```text
[2,4,6]
```

---

## Uses

- Data validation
- Removing invalid records
- Filtering users
- Selecting AI training samples

---

# 3. reduce()

## Definition

`reduce()` combines all elements into one value.

Import

```python
from functools import reduce
```

Syntax

```python
reduce(function, iterable)
```

Example

```python
from functools import reduce

numbers = [1,2,3,4]

total = reduce(lambda x,y:x+y, numbers)

print(total)
```

Output

```text
10
```

---

## Uses

- Sum
- Product
- Maximum
- Minimum
- Aggregation

---

# 4. zip()

## Definition

`zip()` combines multiple iterables element by element.

Example

```python
names = ["John","Alice"]
marks = [90,95]

result = zip(names, marks)

print(list(result))
```

Output

```text
[('John',90),('Alice',95)]
```

---

## Unzipping

```python
students = [
    ("John",90),
    ("Alice",95)
]

names, marks = zip(*students)
```

---

## Uses

- Combining datasets
- Creating dictionaries
- Parallel iteration
- CSV processing

---

# 5. enumerate()

## Definition

Returns index and value together.

Syntax

```python
enumerate(iterable, start=0)
```

Example

```python
languages = ["Python","Java","Go"]

for index, language in enumerate(languages):
    print(index, language)
```

Output

```text
0 Python
1 Java
2 Go
```

---

## Uses

- Ranking
- Menu systems
- Report generation
- Data indexing

---

# 6. any()

## Definition

Returns True if at least one value is True.

Example

```python
values = [False, False, True]

print(any(values))
```

Output

```text
True
```

---

## Uses

- Permission checking
- Validation
- Login systems
- Feature flags

---

# 7. all()

## Definition

Returns True only if every value is True.

Example

```python
values = [True, True, True]

print(all(values))
```

Output

```text
True
```

---

## Uses

- Form validation
- Student eligibility
- Input verification
- Data completeness

---

# 8. sorted()

## Definition

Returns a new sorted list.

Example

```python
numbers = [5,2,8,1]

print(sorted(numbers))
```

Output

```text
[1,2,5,8]
```

---

## Reverse Sorting

```python
sorted(numbers, reverse=True)
```

---

## Sorting Dictionaries

```python
students = [
    {"name":"John","marks":90},
    {"name":"Alice","marks":95}
]

sorted(
    students,
    key=lambda x:x["marks"]
)
```

---

# 9. Key Functions

The `key` parameter defines how sorting or comparison is performed.

Example

```python
words = [
    "Python",
    "AI",
    "MachineLearning"
]

sorted(words, key=len)
```

Output

```text
['AI', 'Python', 'MachineLearning']
```

---

## key with min()

```python
min(words, key=len)
```

---

## key with max()

```python
max(words, key=len)
```

---

## Uses

- Salary sorting
- Student ranking
- Product sorting
- Date sorting

---

# 10. Higher-Order Functions

## Definition

A higher-order function either:

- Accepts another function as an argument.
- Returns another function.

Example

```python
def add(a,b):
    return a+b

def calculate(operation,a,b):
    return operation(a,b)

print(calculate(add,5,3))
```

Output

```text
8
```

---

## Returning Functions

```python
def multiplier(n):

    def multiply(x):
        return x*n

    return multiply

double = multiplier(2)

print(double(10))
```

Output

```text
20
```

---

## Benefits

- Code reuse
- Flexible design
- Cleaner programs
- Modular architecture

---

# Lazy Evaluation

The following return iterators and generate values only when needed:

- map()
- filter()
- zip()
- enumerate()

Benefits:

- Lower memory usage
- Faster startup
- Efficient for large datasets

---

# Functional Programming Pipeline

```text
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
Final Output
```

Each function performs one specific task, making the code modular and easy to understand.

---

# Real-World Applications

## Data Processing

- Data cleaning
- CSV processing
- JSON transformation

---

## Backend Development

- API response formatting
- Validation
- Request processing

---

## Machine Learning

- Feature engineering
- Data preprocessing
- Batch processing

---

## AI/GenAI

- Text preprocessing
- Token filtering
- Embedding preparation
- RAG document pipelines
- Prompt processing

---

## ETL Pipelines

- Extract data
- Filter records
- Transform values
- Aggregate results

---

# Advantages

- Cleaner code
- Less boilerplate
- Easy maintenance
- Better readability
- Reusable functions
- Efficient data processing
- Supports lazy evaluation

---

# Limitations

- Can be difficult for beginners.
- Excessive chaining may reduce readability.
- Debugging nested functions can be harder.
- Sometimes simple loops are easier to understand.

---

# Best Practices

- Use `map()` for transforming data.
- Use `filter()` for selecting data.
- Use `reduce()` only for aggregation.
- Use `zip()` for parallel iteration.
- Use `enumerate()` instead of manual indexing.
- Use `sorted()` with `key` for custom sorting.
- Keep higher-order functions simple and focused.

---

# Summary

| Function | Purpose |
|----------|---------|
| `map()` | Transform each element |
| `filter()` | Select elements |
| `reduce()` | Aggregate into one value |
| `zip()` | Combine iterables |
| `enumerate()` | Index and value |
| `any()` | At least one True |
| `all()` | All values True |
| `sorted()` | Return sorted list |
| `key` | Custom comparison |
| Higher-order functions | Accept or return functions |

---

# Phase 10 Learning Outcome

After completing this phase, you should be able to:

- Understand functional programming concepts.
- Use Python's built-in functional tools effectively.
- Transform and filter data efficiently.
- Aggregate values using `reduce()`.
- Work with multiple iterables using `zip()`.
- Iterate with indexes using `enumerate()`.
- Validate data using `any()` and `all()`.
- Perform custom sorting using `key`.
- Create and use higher-order functions.
- Apply functional programming in backend development, data engineering, machine learning, and AI/GenAI projects.