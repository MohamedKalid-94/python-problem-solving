# Phase 11 — Python Internals
# Interview Questions and Answers

---

# 1. How does Python manage memory?

## Answer:

Python manages memory using a private heap space.

All Python objects and data structures are stored in this heap.

Python memory management includes:

- Reference counting
- Garbage collection
- Memory allocation
- Memory deallocation

Example:

```python
name = "Python"

Python creates a string object in memory and the variable name stores a reference to that object.
2. What is a Python object?
Answer:
Everything in Python is an object.

An object contains:
1. Type
2. Value
3. Identity
Example:
number = 100


Here:
- Type → int
- Value → 100
- Identity → memory address
Identity can be checked using:
id(number)


3. What is a reference in Python?
Answer:
A reference is a connection between a variable and an object.

Variables do not store values directly. They store references to objects.

Example:
a = [1,2,3]b = a


Both variables point to the same list object.
a is b


Output:
True

4. Is Python pass-by-value or pass-by-reference?
Answer:
Python uses pass-by-object-reference (also called pass-by-assignment).

The function receives a reference to the object.

For mutable objects:
def update(data):    data.append(100)numbers = [1,2,3]update(numbers)print(numbers)


Output:
[1,2,3,100]

The original object changes.

For immutable objects:
def update(value):    value = value + 10


A new object is created.
5. What is the difference between assignment and copy?
Answer:
Assignment creates another reference.

Example:
a = [1,2,3]b = a


Both point to the same object.

Copy creates a new object.

Example:
b = a.copy()


Now:
a is b


Output:
False

6. What is shallow copy?
Answer:
Shallow copy creates a new outer object but shares nested objects.

Example:
import copya = [[1,2]]b = copy.copy(a)


Outer list is different.

Nested list is shared.

Changes inside nested objects affect both.
7. What is deep copy?
Answer:
Deep copy creates a completely independent copy.

It copies:
- Outer object
- Nested objects
Example:
import copyb = copy.deepcopy(a)


Changes in b do not affect a.
8. Difference between shallow copy and deep copy?
Feature	Shallow Copy	Deep Copy
Outer object	New	New
Nested objects	Shared	Copied
Memory usage	Less	More
Speed	Faster	Slower
Method	copy.copy()	copy.deepcopy()


9. What are mutable objects?
Answer:
Mutable objects can be modified after creation.

Examples:
- list
- dictionary
- set
- bytearray
Example:
numbers = [1,2]numbers.append(3)


The same object is modified.
10. What are immutable objects?
Answer:
Immutable objects cannot be modified after creation.

Examples:
- int
- float
- string
- tuple
- frozenset
Example:
name = "Python"name += " AI"


A new object is created.
11. Why are strings immutable in Python?
Answer:
Strings are immutable because it provides:
- Security
- Memory optimization
- Hashing support
- Thread safety
Example:
text = "Python"text[0] = "J"


Raises:
TypeError

12. Difference between == and is?
Answer:
== compares values.

is compares object identity.

Example:
a = [1,2]b = [1,2]


Value comparison:
a == b


True

Identity comparison:
a is b


False
13. What does id() function do?
Answer:
id() returns the unique identity of an object.

Example:
name = "Python"print(id(name))


It represents the object's memory identity during its lifetime.
14. What is hashing?
Answer:
Hashing converts an object into a fixed integer value.

Example:
hash("Python")


Hashing is used in:
- Dictionary keys
- Sets
- Caching
- Fast lookup
15. Why can lists not be dictionary keys?
Answer:
Dictionary keys must be hashable.

Lists are mutable, so their hash value can change.

Example:

Invalid:
data = {    [1,2]: "value"}


Error:
TypeError: unhashable type: list

16. What objects are hashable?
Answer:
Hashable objects:
- int
- float
- string
- tuple with immutable elements
- frozenset
Non-hashable:
- list
- dict
- set
17. What is namespace in Python?
Answer:
A namespace is a container that stores names and their object references.

Types:
1. Built-in namespace
2. Global namespace
3. Local namespace
4. Enclosing namespace
18. Explain LEGB rule.
Answer:
Python searches variables in this order:
L → Local
E → Enclosing
G → Global
B → Built-in

Example:
print(len("Python"))


Python finds:
len()

inside built-in namespace.
19. What is global keyword?
Answer:
global allows modifying global variables inside functions.

Example:
count = 0def update():    global count    count += 1


20. What is nonlocal keyword?
Answer:
nonlocal allows modifying variables from enclosing functions.

Example:
def outer():    value = 10    def inner():        nonlocal value        value += 1


21. What is reference counting?
Answer:
Reference counting tracks how many references point to an object.

When reference count becomes zero, Python can remove the object.

Example:
a = [1,2,3]b = adel b


The reference count decreases.
22. What is garbage collection?
Answer:
Garbage collection removes unused objects from memory.

Python automatically manages memory cleanup.

It mainly handles cyclic references.
23. What is object interning?
Answer:
Object interning is a memory optimization technique where Python reuses some immutable objects.

Example:
a = "Python"b = "Python"a is b


May return:
True

24. Why is Python memory management important for AI engineers?
Answer:
AI applications handle:
- Large datasets
- Embeddings
- Model objects
- Documents
- Vector databases
Understanding memory helps:
- Reduce memory usage
- Avoid unnecessary copies
- Improve performance
- Debug hidden reference issues
25. Real-world Python Internals Example in RAG System
Question:
Why is deep copy useful in RAG pipelines?
Answer:
During RAG processing, different pipeline stages may modify state.

Example:
state = {    "documents": [],    "chunks": []}


Creating a deep copy allows:
- Experimenting safely
- Maintaining original state
- Avoiding accidental modifications
Key Interview Takeaways
Remember:
- Variables store references, not values.
- Mutable objects can change.
- Immutable objects create new objects.
- is checks identity.
- == checks equality.
- Shallow copy shares nested objects.
- Deep copy creates independent objects.
- Hashing enables fast lookup.
- Namespaces control variable visibility.
- LEGB explains variable resolution.