![Python](https://img.shields.io/badge/Python-Collections-blue)
Author: Mohamed Kalid

---

# Overview

Python provides a powerful built-in module called:

```python
collections

The collections module contains specialized container
data structures that extend Python's default:
- list
- tuple
- dictionary
- set
These containers provide better performance,
cleaner code, and useful patterns for real-world
software development.
Learning Objectives
After completing this module, you will understand:
- How Counter works internally
- How to count frequencies efficiently
- How defaultdict avoids KeyError
- How deque implements queues and stacks
- How namedtuple creates structured records
- How to select the correct collection
- How collections are used in real projects
Folder Structure
05_collections_module/

│
├── 01_counter_complete.py
│
├── 02_defaultdict_complete.py
│
├── 03_deque_complete.py
│
├── 04_namedtuple_complete.py
│
├── 05_collections_real_world_examples.py
│
├── interview_qanda.md
│
├── practice.md
│
└── notes.md

1. Counter
What is Counter?
Counter is a dictionary subclass used for
counting the frequency of hashable objects.

Import:
from collections import Counter


Example:
from collections import Counternumbers = [1,2,2,3,3,3]count = Counter(numbers)print(count)


Output:
Counter({
3:3,
2:2,
1:1
})

Counter Important Methods
Method	Purpose
most_common()	Find highest frequency items
elements()	Return repeated elements
update()	Add counts
subtract()	Remove counts
total()	Total count


Counter Use Cases
Examples:
- Word frequency
- Log analysis
- Product analytics
- NLP preprocessing
- Recommendation systems
2. defaultdict
What is defaultdict?
defaultdict is a dictionary that automatically
creates a default value when a missing key is accessed.

Import:
from collections import defaultdict


Example
Normal dictionary:
data = {}data["count"] += 1


Problem:
KeyError

Using defaultdict:
data = defaultdict(int)data["count"] += 1


Output:
count:1

Common Factories
int
Counting:
defaultdict(int)


list
Grouping:
defaultdict(list)


set
Unique grouping:
defaultdict(set)


lambda
Custom values:
defaultdict(lambda:"Unknown")


defaultdict Use Cases
Examples:
- Group employees
- Group students
- Data aggregation
- Graph representation
- Data pipelines
3. deque
What is deque?
deque means:
Double Ended Queue

It allows insertion and deletion from both ends.

Import:
from collections import deque


Why deque?
List:
insert(0,value)


Complexity:
O(n)

deque:
appendleft(value)


Complexity:
O(1)

deque Methods
Method	Purpose
append()	Add right
appendleft()	Add left
pop()	Remove right
popleft()	Remove left
rotate()	Rotate elements
maxlen	Fixed size queue


deque Use Cases
Examples:
- Queue systems
- Stack implementation
- Browser history
- BFS traversal
- Sliding window problems
- Message queues
4. namedtuple
What is namedtuple?
namedtuple creates tuple-like objects
with named fields.

Import:
from collections import namedtuple


Example
Without namedtuple:
employee[2]


Problem:

Unknown meaning.

With namedtuple:
employee.salary


Readable.
namedtuple Methods
Method	Purpose
_fields	Get field names
_asdict()	Convert to dictionary
_replace()	Create updated copy
_make()	Create from iterable


namedtuple Use Cases
Examples:
- API responses
- Database rows
- Configuration objects
- Lightweight records
Real World Examples
This module contains examples of:
Log Analyzer
Uses:
Counter

Purpose:

Count:
- ERROR
- WARNING
- INFO
E-Commerce Analytics
Uses:
Counter + defaultdict

Purpose:
- Product sales
- Category grouping
Task Queue System
Uses:
deque

Purpose:

FIFO processing.
Employee Database
Uses:
namedtuple

Purpose:

Store structured records.
Interview Topics Covered
This module covers:
Counter
- Frequency counting
- Top K problems
- Duplicate detection
- Word analysis
defaultdict
- Grouping problems
- Counting problems
- Nested dictionaries
deque
- Queue implementation
- Stack implementation
- Sliding window
- BFS
namedtuple
- Immutable records
- Data objects
- Tuple alternatives
Time Complexity Summary
Collection	Operation	Complexity
Counter	Lookup	O(1)
defaultdict	Lookup	O(1)
deque	append	O(1)
deque	appendleft	O(1)
deque	pop	O(1)
deque	popleft	O(1)
namedtuple	Access	O(1)


When To Use What?
Need frequency counting?
Use:
Counter

Need grouping?
Use:
defaultdict(list)

Need fast queue operations?
Use:
deque

Need readable immutable records?
Use:
namedtuple

Practice Roadmap
Complete:
practice.md

Topics:
- Counter problems
- Grouping problems
- Queue problems
- Stack problems
- BFS problems
- Real-world mini projects
Interview Preparation
Review:
interview_qanda.md

Includes:
- Concept questions
- Coding questions
- Comparison questions
- Real-world scenarios
Module Completion Checklist
Counter
- [x] Creation
- [x] Counting
- [x] Methods
- [x] Real examples
defaultdict
- [x] Factories
- [x] Grouping
- [x] Nested structures
deque
- [x] Queue
- [x] Stack
- [x] Sliding window
- [x] BFS
namedtuple
- [x] Creation
- [x] Methods
- [x] Comparisons
Final Outcome
After completing this module, you can:

✅ Choose the right Python collection
✅ Write cleaner Python code
✅ Solve common interview problems
✅ Build efficient data processing logic
✅ Apply collections in AI/Backend projects  
Next Learning Path
Continue with:
Advanced Python Concepts

Topics:

- Comprehensions
- Iterators
- Generators
- Decorators
- Context Managers
- Type Hints
- Async Python
---