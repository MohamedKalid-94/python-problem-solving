# Python Collections Module - Notes

Author: Mohamed Kalid

---

# 1. Introduction to Collections Module

Python provides a built-in module called:

```python
collections

It contains specialized container data types that extend
Python's built-in:
- list
- tuple
- dictionary
- set
Import:
import collections


Commonly used classes:
Class	Purpose
Counter	Count frequency
defaultdict	Dictionary with default values
deque	Double-ended queue
namedtuple	Named immutable records


2. Counter
Definition
Counter is a dictionary subclass used for counting
hashable objects.

Import:
from collections import Counter


Example:
numbers = [1,2,2,3,3,3]count = Counter(numbers)print(count)


Output:
{3:3,2:2,1:1}


Counter Internally
Counter stores:
Element -> Frequency

Example:

Input:
Python

Memory:
P : 1
y : 1
t : 1
h : 1
o : 1
n : 1

Counter Important Methods
most_common()
Find highest frequency elements.
counter.most_common(3)


Example:
Counter({"A":5,"B":3,"C":1})


Output:
A -> 5
B -> 3
C -> 1

elements()
Returns repeated elements.

Example:
Counter({"A":3,"B":2})


Output:
A A A B B

update()
Adds counts.

Example:
counter.update("python")


subtract()
Removes counts.

Example:
counter.subtract("python")


Counter Use Cases
Used in:
- Word frequency
- Log analysis
- Data analytics
- NLP preprocessing
- Recommendation systems
3. defaultdict
Definition
defaultdict automatically creates values
for missing keys.

Import:
from collections import defaultdict


Normal Dictionary Problem
Example:
data = {}data["count"] += 1


Error:
KeyError

defaultdict Solution
data = defaultdict(int)data["count"] += 1


Output:
count:1

defaultdict Factories
int
Used for counting.
defaultdict(int)


Example:
word -> count

list
Used for grouping.
defaultdict(list)


Example:
department -> employees

set
Used for unique grouping.
defaultdict(set)


Example:
student -> courses

str
Creates empty string.
defaultdict(str)


lambda
Custom default value.

Example:
defaultdict(lambda:"Unknown")


defaultdict Use Cases
Used in:
- Grouping data
- Aggregation
- Data processing pipelines
- Graph representation
- AI data preparation
4. deque
Definition
deque means:
Double Ended Queue

It allows insertion and deletion from both ends.

Import:
from collections import deque


List vs deque
List:
insert(0,value)


Complexity:
O(n)

because elements shift.

deque:
appendleft(value)


Complexity:
O(1)

deque Methods
append()
Add right side.
queue.append(item)


appendleft()
Add left side.
queue.appendleft(item)


pop()
Remove right side.
popleft()
Remove left side.
rotate()
Move elements.

Example:
deque([1,2,3]).rotate(1)


Output:
[3,1,2]

maxlen
Creates fixed-size deque.

Example:
history = deque(maxlen=5)


When new item arrives:

Oldest item removed automatically.
deque Use Cases
Used in:
- Queue systems
- Stack implementation
- Browser history
- BFS algorithms
- Sliding window problems
- Message queues
5. namedtuple
Definition
namedtuple creates tuple subclasses
with named fields.

Import:
from collections import namedtuple


Normal Tuple Problem
Example:
employee[2]


Question:

What is index 2?
namedtuple Solution
Example:
employee.salary


Readable.
Creating namedtuple
Employee = namedtuple("Employee",["name","salary"])


Create object:
emp = Employee("John",50000)


namedtuple Properties
_fields
Returns field names.
Employee._fields


_asdict()
Convert to dictionary.
employee._asdict()


_replace()
Create updated copy.
employee._replace(salary=60000)


_make()
Create object from iterable.
Employee._make(data)


namedtuple Characteristics
- Immutable
- Memory efficient
- Faster than class
- Easy to read
namedtuple vs tuple
tuple	namedtuple
Index access	Name access
Less readable	More readable
Immutable	Immutable


namedtuple vs class
namedtuple	class
Immutable	Mutable
Less code	More code
Data only	Data + behavior


namedtuple vs dataclass
namedtuple	dataclass
Immutable	Mutable
Lightweight	Feature rich
Simple data	Business objects


6. Time Complexity
Counter
Operation	Complexity
Access	O(1)
Update	O(1)
Count	O(n)


defaultdict
Operation	Complexity
Insert	O(1)
Access	O(1)


deque
Operation	Complexity
append	O(1)
appendleft	O(1)
pop	O(1)
popleft	O(1)


namedtuple
Operation	Complexity
Access field	O(1)


7. Collections Module Selection Guide
Need frequency counting?

Use:
Counter

Need automatic dictionary values?

Use:
defaultdict

Need fast insert/remove from both ends?

Use:
deque

Need lightweight structured object?

Use:
namedtuple

8. Real World Mapping
Log Analyzer
Tools:
Counter

Problem:

Count:
- ERROR
- WARNING
- INFO
E-Commerce Analytics
Tools:
Counter
defaultdict

Problem:
- Product sales
- Category grouping
Task Queue
Tool:
deque

Problem:

FIFO processing.
API Response Object
Tool:
namedtuple

Problem:

Store structured response data.
9. Interview Summary
Remember:
Counter
=
Frequency Counter


defaultdict
=
Dictionary without KeyError


deque
=
Fast Queue + Stack


namedtuple
=
Readable Immutable Tuple

Final Learning Outcome
After completing this module:

You should be able to:

✅ Choose correct collection type
✅ Solve frequency problems
✅ Build grouping logic
✅ Implement queues/stacks
✅ Handle structured data
✅ Answer Python interview questions  