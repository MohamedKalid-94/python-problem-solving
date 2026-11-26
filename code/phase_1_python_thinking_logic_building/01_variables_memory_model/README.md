# Phase 1 - Python Variables & Memory Model

## Overview

This phase builds the foundation of Python programming.

Before learning advanced topics like loops, functions, OOP, and problem-solving patterns, it is important to understand how Python stores data, manages variables, and handles objects in memory.

In this phase, we learn:

- How variables work
- How objects are stored in memory
- How references work
- How assignment works
- How Python handles different data types
- Difference between mutable and immutable objects
- Object identity
- Basic garbage collection concepts


---

# Learning Objectives

By completing this phase, you will understand:
✅ Variables and values
✅ Object references
✅ Variable assignment
✅ Dynamic typing
✅ Mutable vs Immutable objects
✅ Memory behavior
✅ Object identity using id()
✅ Basic garbage collection


---

# Phase Learning Flow

Variables
↓
Object References
↓
Assignment
↓
Dynamic Typing
↓
Mutable vs Immutable
↓
Memory Concepts
↓
Object Identity
↓
Garbage Collection

---

# Folder Structure

phase_01/
│
├── 01_variables/
│
├── 02_object_references/
│
├── 03_assignment/
│
├── 04_dynamic_typing/
│
├── 05_mutable_vs_immutable/
│
├── 06_memory_concepts/
│
├── 07_object_identity/
│
└── 08_garbage_collection/


---

# Step 1 - Variables

Folder:

01_variables/


## Concepts Covered

- Creating variables
- Variable naming
- Storing values
- Using variables in calculations


## Real World Examples

- Student information
- Employee salary
- Rectangle calculation
- Circle area calculation


## Key Understanding

Variables are names that refer to objects stored in memory.


Example:

```python
student_name = "Kalid"

Python creates an object "Kalid" and the variable points to that object.
Step 2 - Object References
Folder:

02_object_references/

Concepts Covered
- Variables store references
- Multiple variables can point to the same object
- Shared object behavior
Key Understanding
Example:
cart_1 = cartcart_2 = cart


Both variables refer to the same object.

Changing one reference affects the same object.
Step 3 - Assignment
Folder:
03_assignment/

Concepts Covered
- Simple assignment
- Multiple assignment
- Tuple unpacking
- Variable reassignment
Examples
a = 10x, y = 10, 20name, age = ("Kalid", 28)


Step 4 - Dynamic Typing
Folder:
04_dynamic_typing/

Concepts Covered
- Python variables do not have fixed types
- Object types
- Type checking
- Type conversion
Example:
value = 100value = "Python"


The same variable can reference different object types.
Step 5 - Mutable vs Immutable
Folder:
05_mutable_vs_immutable/

Mutable Objects
Objects that can be changed after creation.

Examples:
- List
- Dictionary
Example:
numbers.append(10)


Immutable Objects
Objects that cannot be changed after creation.

Examples:
- Integer
- String
- Tuple
Example:
name = name + " Python"


A new object is created.
Step 6 - Memory Concepts
Folder:
06_memory_concepts/

Concepts Covered
- Same reference
- Copying objects
- Immutable object behavior
- Memory identity
Key Understanding:

Reference:
variable → object

Copy:
variable → new object

Step 7 - Object Identity
Folder:
07_object_identity/

Concepts Covered
- id()
- Identity comparison
- Difference between == and is
Comparison
Value comparison:
==


Checks whether values are equal.

Identity comparison:
is


Checks whether both variables point to the same object.
Step 8 - Garbage Collection
Folder:

08_garbage_collection/

Concepts Covered
- Reference counting
- del keyword
- gc module
- Memory cleanup

How to Run
Navigate to any file:
Example:
python 01_variables/01_student_info.py

Skills Developed
After completing Phase 1, you can:
✅ Understand Python variable behavior
✅ Predict object reference behavior
✅ Identify mutable and immutable objects
✅ Understand memory concepts
✅ Debug reference-related issues
✅ Explain Python memory management in interviews