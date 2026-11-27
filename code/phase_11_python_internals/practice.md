# Phase 11 — Python Internals
# Practice Exercises

---

# Module 1: Memory Model

## Exercise 1: Object Identity

Create variables and check their identities.

Requirements:

- Create an integer variable.
- Create a string variable.
- Print their values.
- Print their memory identities using `id()`.

Example:

```python
number = 100

print(number)
print(id(number))

Exercise 2: Object Information
Create different objects:
- Integer
- String
- List
- Dictionary
Print:
- Type
- Value
- Identity
Expected output:
Type:
Value:
ID:

Module 2: References
Exercise 3: Reference Sharing
Create a list:
numbers = [1,2,3]


Create another variable pointing to it.

Tasks:
1. Modify the second variable.
2. Check the first variable.
3. Check using is.
Expected learning:
- Both variables point to the same object.
Exercise 4: Reference Debugging
Given:
user = {    "name":"Kalid"}backup = user


Tasks:
1. Change backup name.
2. Observe user.
3. Explain why both changed.
Module 3: Copy
Exercise 5: Assignment Copy
Create:
data = [10,20,30]


Perform:
copy_data = data


Tasks:
- Append new value.
- Check both lists.
- Explain the behavior.
Exercise 6: List Shallow Copy
Create:
numbers = [1,2,3]


Use:
- copy()
- slicing
- list()
Tasks:

Compare:
original is copied


Module 4: Deep Copy
Exercise 7: Nested Object Copy
Create:
students = [    {        "name":"John",        "skills":["Python"]    }]


Tasks:
1. Create shallow copy.
2. Create deep copy.
3. Modify skills.
4. Compare results.
Exercise 8: Configuration Backup
Create AI configuration:
config = {    "model":"LLM",    "parameters":{        "temperature":0.7    }}


Tasks:
1. Create backup using shallow copy.
2. Create backup using deep copy.
3. Modify temperature.
4. Observe differences.
Module 5: Mutable Objects
Exercise 9: Mutable List
Create:
skills = [    "Python",    "SQL"]


Tasks:
- Add new skill.
- Remove skill.
- Check object ID before and after modification.
Exercise 10: Mutable Dictionary
Create:
employee = {"name":"Kalid","role":"Developer"}


Tasks:
- Update role.
- Add experience.
- Delete a key.
Module 6: Immutable Objects
Exercise 11: String Modification
Create:
language = "Python"


Tasks:
1. Print ID.
2. Add " AI".
3. Print new ID.
4. Compare identities.
Exercise 12: Tuple Modification
Create:
data = (    1,    2,    3)


Try:
data[0] = 100


Observe the error.

Explain why.
Module 7: Hashing
Exercise 13: Hash Values
Find hash values for:
- Integer
- String
- Tuple
Example:
print(hash("Python"))


Exercise 14: Non-Hashable Objects
Try:
hash([1,2,3])


Questions:
1. What error occurs?
2. Why?
Exercise 15: Dictionary Keys
Create dictionary using:

Valid keys:
- String
- Integer
- Tuple
Invalid keys:
- List
- Dictionary
Observe the difference.
Module 8: Identity
Exercise 16: == vs is
Create:
a = [1,2,3]b = [1,2,3]


Compare:
a == ba is b


Explain output.
Exercise 17: Shared Object Detection
Create:
a = {    "name":"AI"}b = a


Check:
a is b


Modify b.

Observe a.
Module 9: Namespaces
Exercise 18: LEGB Practice
Create:

Global variable:
name = "Global"


Create function:
def test():    name = "Local"


Print both values.

Understand LEGB rule.
Exercise 19: Global Keyword
Create:
count = 0


Create function that increases count.

Use:
global


Exercise 20: Nonlocal Keyword
Create nested functions.

Outer variable:
value = 10


Modify inside inner function using:
nonlocal


Module 10: Real-World AI Engineering Problems
Exercise 21: RAG Pipeline State Copy
Create:
state = {"documents":[],"chunks":[],"status":"loading"}


Tasks:
1. Create experiment copy.
2. Add chunks.
3. Update status.
4. Keep original unchanged.
Use:
deepcopy()


Exercise 22: AI Cache System
Create a simple cache:
cache = {}


Tasks:
1. Create prompt.
2. Generate hash key.
3. Store response.
4. Retrieve response using hash.
Exercise 23: Memory Optimization
Create:

Large list:
data = [    x for x in range(1000000)]


Compare with generator:
(x for x in range(1000000))


Observe:
- Memory usage
- Performance
Exercise 24: Debug Shared State Bug
Scenario:

Two modules share configuration.

Problem:

Changing one configuration changes another.

Tasks:
1. Reproduce using references.
2. Fix using deep copy.
3. Explain the solution.
Interview Practice Questions
Basic Level
1. What is an object in Python?
2. What is object identity?
3. What does id() return?
4. What is a reference?
5. Difference between mutable and immutable objects?
Intermediate Level
6. Difference between shallow copy and deep copy?
7. Why are dictionary keys hashable?
8. Why are lists not hashable?
9. Explain LEGB rule.
10. Difference between == and is?
Advanced Level
11. Explain Python memory management.
12. How does garbage collection work?
13. Explain reference counting.
14. What happens internally during assignment?
15. How do Python internals affect AI applications?
Mini Project
Build: AI Pipeline State Manager
Features:
- Store documents
- Manage chunks
- Maintain processing status
- Create backups
- Compare states
- Track object identities
- Implement cache using hashing
Concepts Used:

✅ Memory model
✅ References
✅ Copy
✅ Deep copy
✅ Mutable objects
✅ Immutable objects
✅ Hashing
✅ Identity
✅ Namespaces