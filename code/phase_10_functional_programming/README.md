# Phase 10 — Functional Programming

## Overview

Functional Programming is a programming paradigm where computation is performed using functions. Instead of writing repetitive loops and modifying data directly, functional programming focuses on applying functions to data.

Python provides several built-in functional programming tools that make code more concise, readable, reusable, and efficient.

This phase covers the most commonly used functional programming features that are frequently asked in Python interviews and widely used in backend development, data engineering, machine learning, and Generative AI applications.

---

# Learning Objectives

After completing this phase, you will be able to:

- Understand Functional Programming concepts
- Use `map()` effectively
- Filter data using `filter()`
- Aggregate values using `reduce()`
- Combine iterables using `zip()`
- Iterate using `enumerate()`
- Validate data using `any()` and `all()`
- Sort data using `sorted()`
- Perform custom sorting with `key`
- Create Higher-Order Functions
- Build real-world functional data pipelines

---

# Folder Structure

```text
10_functional_programming/

├── 01_map_function/
│   └── 01_map_function_complete.py
│
├── 02_filter_function/
│   └── 02_filter_function_complete.py
│
├── 03_reduce_function/
│   └── 03_reduce_function_complete.py
│
├── 04_zip_function/
│   └── 04_zip_function_complete.py
│
├── 05_enumerate_function/
│   └── 05_enumerate_function_complete.py
│
├── 06_any_function/
│   └── 06_any_function_complete.py
│
├── 07_all_function/
│   └── 07_all_function_complete.py
│
├── 08_sorted_function/
│   └── 08_sorted_function_complete.py
│
├── 09_key_functions/
│   └── 09_key_functions_complete.py
│
├── 10_higher_order_functions/
│   └── 10_higher_order_functions_complete.py
│
├── 11_functional_programming_real_world_problems/
│   └── 11_functional_programming_real_world_problems_complete.py
│
├── interview_qanda.md
├── notes.md
├── practice.md
└── README.md
```

---

# Topics Covered

## 1. map()

Used to transform every element of an iterable.

Example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * x, numbers)
```

Applications:

- Data transformation
- Unit conversion
- Feature engineering
- AI dataset preprocessing

---

## 2. filter()

Used to select elements based on a condition.

Example:

```python
numbers = [1,2,3,4]

result = filter(lambda x:x%2==0, numbers)
```

Applications:

- Data cleaning
- Validation
- Record selection
- Log filtering

---

## 3. reduce()

Used to combine multiple values into a single value.

Example:

```python
from functools import reduce

total = reduce(lambda x,y:x+y, numbers)
```

Applications:

- Sum
- Product
- Aggregation
- Statistics

---

## 4. zip()

Combines multiple iterables element by element.

Example:

```python
names = ["John","Alice"]

marks = [90,95]

result = zip(names, marks)
```

Applications:

- CSV processing
- Combining datasets
- Dictionary creation

---

## 5. enumerate()

Returns index and value together.

Example:

```python
for index, value in enumerate(items):
    print(index, value)
```

Applications:

- Ranking
- Menu systems
- Report generation

---

## 6. any()

Returns **True** if at least one element evaluates to True.

Example:

```python
any([False, True, False])
```

Applications:

- Permission checks
- Validation
- Feature flags

---

## 7. all()

Returns **True** only if every element evaluates to True.

Example:

```python
all([True, True, True])
```

Applications:

- Form validation
- Eligibility checking
- Data completeness

---

## 8. sorted()

Returns a new sorted list.

Example:

```python
sorted(numbers)
```

Supports:

- Ascending order
- Descending order
- Custom sorting

---

## 9. key Functions

The `key` parameter controls how sorting or comparison is performed.

Example:

```python
students = sorted(
    students,
    key=lambda student: student["marks"]
)
```

Used with:

- `sorted()`
- `min()`
- `max()`

---

## 10. Higher-Order Functions

Higher-order functions either:

- Accept another function as an argument.
- Return another function.

Example:

```python
def calculate(operation, a, b):
    return operation(a, b)
```

Applications:

- Callbacks
- Decorators
- Function factories
- Framework design

---

## 11. Real-World Functional Programming Problems

This module demonstrates practical use cases, including:

- Employee salary processing
- Student result analysis
- E-commerce order processing
- API response transformation
- Log file analysis
- AI dataset preprocessing
- RAG document processing pipeline
- Functional data pipelines

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
Final Result
```

Each function performs a single responsibility, making the pipeline clean, modular, and easy to maintain.

---

# Functional Programming vs Traditional Programming

| Traditional Programming | Functional Programming |
|-------------------------|------------------------|
| Uses loops | Uses functions |
| More mutable state | Prefers immutable data |
| Longer code | Concise code |
| Manual processing | Built-in functional tools |
| More boilerplate | Cleaner and reusable |

---

# Real-World Applications

## Backend Development

- Request processing
- Response formatting
- Data validation

---

## Data Engineering

- ETL pipelines
- Data cleaning
- Data transformation

---

## Machine Learning

- Feature engineering
- Dataset preprocessing
- Batch processing

---

## AI & Generative AI

- Prompt preprocessing
- Document filtering
- Embedding preparation
- RAG pipelines
- LLM input transformation

---

## Web Development

- JSON processing
- API response handling
- Report generation

---

# Skills Developed

By completing this phase, you will gain experience in:

- Functional programming concepts
- Data transformation
- Data filtering
- Data aggregation
- Custom sorting
- Callback functions
- Function composition
- Pipeline design
- Clean Python programming

---

# Interview Preparation

This phase prepares you for common Python interview questions such as:

- What is Functional Programming?
- Explain `map()`, `filter()`, and `reduce()`.
- Difference between `map()` and `filter()`.
- What is a Higher-Order Function?
- Explain `zip()` and `enumerate()`.
- Difference between `any()` and `all()`.
- Difference between `sorted()` and `sort()`.
- What is the `key` parameter?
- What are callback functions?
- Where is Functional Programming used?

---

# Best Practices

- Use `map()` for transforming data.
- Use `filter()` for selecting records.
- Use `reduce()` only for aggregation.
- Prefer `enumerate()` over manual indexing.
- Use `zip()` for parallel iteration.
- Use `sorted()` with `key` for custom sorting.
- Keep higher-order functions small and reusable.
- Write readable functional pipelines instead of deeply nested expressions.

---

# Learning Outcome

After completing **Phase 10**, you will be able to:

- Write clean and efficient functional Python code.
- Apply Python's built-in functional programming tools confidently.
- Process and transform large datasets.
- Build reusable higher-order functions.
- Design functional data pipelines.
- Solve real-world backend, data engineering, machine learning, and AI/GenAI problems using functional programming techniques.

---

# Next Phase

## Phase 11 — File Handling & Exception Handling

Topics:

- Reading and writing text files
- File modes (`r`, `w`, `a`, `x`, `rb`, `wb`)
- Working with CSV and JSON files
- File paths (`os` and `pathlib`)
- Exception handling (`try`, `except`, `else`, `finally`)
- Raising custom exceptions
- Creating custom exception classes
- Real-world file processing and error handling