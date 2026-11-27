# Phase 1 Interview Questions & Answers

## Beginner Level

## 1. What is a variable in Python?
Answer:
A variable is a name that refers to an object stored in memory.
---

## 2. Does Python store values inside variables?
Answer:
No.
Variables store references to objects.
---

## 3. What happens when we assign a variable?
Example:
```python
a = 10

Answer:

Python creates an integer object and variable a references that object.
4. What is dynamic typing?
Answer:

Dynamic typing means variable types are checked during runtime.

Example:
x = 10x = "Python"


5. What are mutable objects?
Answer:

Objects that can be changed after creation.

Examples:
- List
- Dictionary
6. What are immutable objects?
Answer:

Objects that cannot be changed after creation.

Examples:
- String
- Tuple
- Integer
Intermediate Questions
7. Difference between assignment and copy?
Assignment:
a = b


Both variables reference the same object.

Copy:
a = b.copy()


Creates a new object.
8. Difference between == and is?
==

Checks values.

is

Checks identity.
9. What does id() return?
Answer:

It returns the unique identity of an object during its lifetime.
10. Why are strings immutable?
Answer:

Immutability improves:
- Security
- Performance
- Memory optimization
11. Explain Python memory management.
Answer:

Python manages memory automatically using:
- Private heap
- Reference counting
- Garbage collection
12. What happens when we use del?
Answer:

del removes a variable reference.

If no references remain, the object can be garbage collected.
Advanced Questions
13. Why does changing one list reference affect another?
Answer:

Because both variables point to the same object.
14. Why does changing an integer variable not affect another variable?
Answer:

Integers are immutable.

A new object is created when the value changes.
15. How does garbage collection work?
Answer:

Python tracks object references.

When an object has no references, memory can be released.
16. Difference between mutable and immutable memory behavior?
Answer:

Mutable objects change the existing object.

Immutable objects create a new object when modified.
17. What is object identity?
Answer:

Object identity represents whether two variables refer to the same object in memory.
Practical Interview Tasks
1. Explain output of shared list reference.
2. Predict id() values.
3. Explain list copy vs assignment.
4. Identify mutable and immutable objects.
5. Debug reference-related issues.

---

These three files complete the **Phase 1 documentation package** while keeping your original structure unchanged.