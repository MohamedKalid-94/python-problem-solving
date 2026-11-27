# Phase 11 — Python Internals
# Notes

---

# 1. Python Memory Model

Python manages memory automatically.

Unlike low-level languages like C/C++, developers do not manually allocate or free memory.

Python uses:

- Private heap
- Reference counting
- Garbage collection
- Memory optimization techniques

---

## Object Model

Everything in Python is an object.

An object contains:


Object
|
├── Type
|
├── Value
|
└── Identity

Example:

```python
number = 100

Object information:
Type     → int
Value    → 100
Identity → Memory address

Check identity:
id(number)


2. Variables and References
Python variables do not store actual values.

They store references to objects.

Example:
name = "Python"


Memory:
Variable
   |
   |
   ▼
Object
"Python"

Multiple References
Example:
a = [1,2,3]b = a


Memory:
        ┌─────────┐
a ─────▶│         │
        │ [1,2,3] │
b ─────▶│         │
        └─────────┘

Both variables point to the same object.

Check:
a is b


Output:
True

3. Reference Counting
Python tracks how many references point to an object.

Example:
data = [1,2,3]


Reference count:
data
 |
 ▼
[1,2,3]

Adding another reference:
copy = data


Reference count increases.

Deleting:
del copy


Reference count decreases.

When reference count becomes zero:
Object → Removed from memory

4. Garbage Collection
Reference counting cannot handle circular references.

Example:
a = []b = []a.append(b)b.append(a)


Objects reference each other.

Python garbage collector removes such unused objects.
5. Copy in Python
There are three ways to copy objects.
Assignment Copy
Example:
a = [1,2,3]b = a


Characteristics:
- No new object
- Same reference
- Changes affect both
Shallow Copy
Example:
import copyb = copy.copy(a)


Characteristics:
- New outer object
- Nested objects shared
Example:
Original

[
 [1,2]
]


Shallow Copy

[
 [1,2]
]

Inner list is the same object.
Deep Copy
Example:
b = copy.deepcopy(a)


Characteristics:
- New outer object
- New nested objects
- Completely independent
6. Shallow Copy vs Deep Copy
Feature	Shallow Copy	Deep Copy
Outer object	New	New
Nested object	Shared	Copied
Memory usage	Low	High
Speed	Faster	Slower
Method	copy.copy()	copy.deepcopy()


7. Mutable Objects
Mutable objects can change after creation.

Examples:
list
dict
set
bytearray

Example:
numbers = [1,2,3]numbers.append(4)


Same object is modified.

Check:
id(numbers)


Before and after modification:
Same ID

Mutable Object Examples
List
items.append()items.remove()


Dictionary
user["name"]="Kalid"


Set
values.add()


8. Immutable Objects
Immutable objects cannot change after creation.

Examples:
int
float
str
tuple
frozenset

Example:
name="Python"name=name+" AI"


Python creates a new object.

Memory:

Before:
name
 |
 ▼
"Python"

After:
name
 |
 ▼
"Python AI"

9. Mutable vs Immutable
Feature	Mutable	Immutable
Change value	Yes	No
Same object modified	Yes	No
New object created	No	Yes
Examples	list, dict	int, str


10. Hashing
Hashing converts an object into an integer value.

Example:
hash("Python")


Output:
Some integer value

Hashing Uses
Used in:
- Dictionary
- Set
- Cache systems
- Database indexing
Hashable Objects
Hashable:
int
float
str
tuple
frozenset

Non-hashable:
list
dict
set

Reason:

Mutable objects can change.
11. Identity
Identity tells whether two variables point to the same object.

Operators:
is
is not

Example:
a=[1,2]b=aa is b


Output:
True

Equality vs Identity
Equality
Checks values.
==


Example:
[1,2] == [1,2]


Output:
True

Identity
Checks memory object.
is


Example:
[1,2] is [1,2]


Output:
False

12. Namespaces
Namespace stores names and their objects.

Python has four namespaces.
Built-in Namespace
Python predefined names.

Examples:
print()len()type()


Global Namespace
Variables created at module level.

Example:
company="AI"


Local Namespace
Variables inside functions.

Example:
def test():    value=10


Enclosing Namespace
Variables from outer functions.

Example:
def outer():    x=10    def inner():        print(x)


13. LEGB Rule
Python searches variables in this order:
L → Local

E → Enclosing

G → Global

B → Built-in

Example:
print(len("Python"))


Python searches:
Local
 ↓
Enclosing
 ↓
Global
 ↓
Built-in

14. Global Keyword
Used to modify global variables.

Example:
count = 0def update():    global count    count += 1


15. Nonlocal Keyword
Used to modify enclosing function variables.

Example:
def outer():    value = 10    def inner():        nonlocal value        value += 1


16. Python Internals in AI Engineering
Python internals are important when building:
Machine Learning Systems
- Large datasets
- Model objects
- Memory optimization
Generative AI Systems
Examples:
- RAG pipelines
- Embedding processing
- Document chunks
- Vector storage
Backend Systems
Examples:
- API caching
- Configuration management
- Object lifecycle
17. Common Mistakes
Mistake 1: Assignment Instead of Copy
Wrong:
backup = config


Correct:
backup = copy.deepcopy(config)


Mistake 2: Mutable Default Arguments
Wrong:
def add(item, data=[]):


Correct:
def add(item, data=None):


Mistake 3: Using is for Value Comparison
Wrong:
name is "Python"


Correct:
name == "Python"


Phase 11 Summary
After completing Python Internals:

You understand:

✅ Memory management
✅ Objects and references
✅ Copy mechanisms
✅ Deep copy vs shallow copy
✅ Mutable and immutable objects
✅ Hashing
✅ Identity checking
✅ Namespace management
✅ Variable scope
✅ Python memory optimization