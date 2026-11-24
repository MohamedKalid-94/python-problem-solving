---

# `notes.md`

```markdown
# Phase 1 Notes - Variables & Memory Model


# 1. Variables

A variable is a name that refers to an object.

Example:

```python
name = "Python"

Python creates an object and the variable points to it.
2. Object References
Variables store references, not actual values.

Example:
a = [1,2,3]b = a


Both variables point to the same list object.
3. Assignment
Assignment connects a variable name with an object.

Example:
age = 25


Multiple assignment:
a,b = 10,20


4. Dynamic Typing
Python is dynamically typed.

The variable type is decided during runtime.

Example:
value = 10value = "Python"


Same variable can reference different objects.
5. Mutable vs Immutable
Mutable
Object can be changed after creation.

Examples:
- List
- Dictionary
Example:
numbers.append(10)


Immutable
Object cannot be changed after creation.

Examples:
- Integer
- String
- Tuple
Modification creates a new object.
6. Memory Concepts
Python memory contains objects.

Variables point to objects.

Flow:
Variable
   |
   ↓
Object
   |
   ↓
Memory

7. Object Identity
id() gives object identity.

Example:
id(value)


Comparison:
==

Checks value equality.
is

Checks object identity.
8. Garbage Collection
Python automatically manages memory.

When objects are no longer referenced, Python removes them.

Important concepts:
- Reference counting
- del keyword
- gc module
Quick Revision
Variable

↓

Reference

↓

Object

↓

Memory

↓

Identity

↓

Garbage Collection