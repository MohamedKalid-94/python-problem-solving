interview_qanda.md
# Python Collections Module - Interview Questions & Answers

Author: Mohamed Kalid

Topics Covered:

- Counter
- defaultdict
- deque
- namedtuple

---

# 1. Counter Interview Questions

---

## Q1. What is Counter in Python?

### Answer:

`Counter` is a dictionary subclass from the `collections` module
used to count the frequency of elements.

Example:

```python
from collections import Counter

numbers = [1,2,2,3,3,3]

count = Counter(numbers)

print(count)

Output:
Counter({3:3, 2:2, 1:1})

Internally:
Element -> Frequency

Q2. Why use Counter instead of a normal dictionary?
Answer:
Without Counter:
count = {}for item in data:    if item not in count:        count[item] = 0    count[item] += 1


Using Counter:
from collections import Countercount = Counter(data)


Advantages:
- Less code
- Cleaner syntax
- Built-in methods
- Optimized implementation
Q3. How do you find the most common elements?
Answer:
Using:
most_common()


Example:
counter.most_common(3)


Returns top 3 frequent elements.
Q4. Difference between update() and subtract()?
update()	subtract()
Adds counts	Removes counts
Increases values	Decreases values


Example:
from collections import Counterc = Counter("banana")c.update("apple")c.subtract("ana")


Q5. What does elements() do?
Answer:
Returns elements repeated according to their count.

Example:
c = Counter({    "A":3,    "B":2})list(c.elements())


Output:
['A','A','A','B','B']

2. defaultdict Interview Questions
Q6. What is defaultdict?
Answer:
defaultdict is a dictionary subclass that automatically creates
a default value when a missing key is accessed.

Example:

Normal dictionary:
data = {}data["count"] += 1


Error:
KeyError

Using defaultdict:
from collections import defaultdictdata = defaultdict(int)data["count"] += 1


Output:
{'count':1}

Q7. Difference between dict and defaultdict?
dict	defaultdict
Missing key gives KeyError	Creates default value
Manual initialization needed	Automatic
More code	Less code


Q8. Why use defaultdict(list)?
Answer:
For grouping data.

Example:
from collections import defaultdictstudents = defaultdict(list)students["AI"].append("John")students["AI"].append("Alice")


Output:
{
"AI":["John","Alice"]
}

Q9. What are common default_factory values?
Common factories:
defaultdict(int)defaultdict(list)defaultdict(set)defaultdict(str)


Q10. Can defaultdict have a custom default value?
Yes.

Example:
data = defaultdict(    lambda:"Unknown")print(data["name"])


Output:
Unknown

3. deque Interview Questions
Q11. What is deque?
Answer:
deque means:
Double Ended Queue

It allows insertion and deletion from both ends.

Example:
from collections import dequequeue = deque()queue.append(10)queue.appendleft(20)


Q12. Why use deque instead of list?
Answer:
Because operations from both ends are faster.

List:
insert(0,value)


Complexity:
O(n)

deque:
appendleft(value)


Complexity:
O(1)

Q13. How to implement Queue using deque?
Queue follows:
FIFO

First In First Out

Example:
queue.append(item)queue.popleft()


Q14. How to implement Stack using deque?
Stack follows:
LIFO

Last In First Out

Example:
stack.append(item)stack.pop()


Q15. What is maxlen in deque?
Answer:
maxlen limits the size of deque.

Example:
history = deque(maxlen=3)history.append(1)history.append(2)history.append(3)history.append(4)


Output:
[2,3,4]

Old values are automatically removed.
Q16. Where is deque used?
Real-world:
- Browser history
- Task queues
- BFS algorithms
- Sliding window problems
- Undo/Redo systems
- Message queues
4. namedtuple Interview Questions
Q17. What is namedtuple?
Answer:
namedtuple is an extension of tuple that allows
accessing values using names.

Normal tuple:
employee[0]


namedtuple:
employee.name


Q18. Why use namedtuple?
Advantages:
- Better readability
- Immutable
- Memory efficient
- Lightweight alternative to class
Q19. Is namedtuple mutable?
No.

Example:
employee.salary = 90000


Raises:
AttributeError

Q20. Difference between tuple and namedtuple?
tuple	namedtuple
Access by index	Access by name
Less readable	More readable
Immutable	Immutable


Q21. Difference between namedtuple and class?
namedtuple	class
Immutable	Mutable
Less code	More code
Stores data	Stores data + behavior
Lightweight	More powerful


Q22. Difference between namedtuple and dataclass?
namedtuple	dataclass
Immutable	Mutable by default
Less memory	More features
No methods	Supports methods
Simple data objects	Business objects


5. Combined Collections Questions
Q23. How would you count log levels?
Example:

Input:
INFO
ERROR
INFO
WARNING
ERROR

Solution:
from collections import Counterlogs = ["INFO","ERROR","INFO","WARNING","ERROR"]Counter(logs)


Output:
{
INFO:2,
ERROR:2,
WARNING:1
}

Q24. How do you group employees by department?
Solution:
from collections import defaultdictemployees = defaultdict(list)employees["IT"].append("John")employees["HR"].append("Alice")


Q25. How do you maintain recent browser history?
Solution:
from collections import dequehistory = deque(maxlen=5)


Q26. How do you store API response data?
Solution:
from collections import namedtupleResponse = namedtuple(    "Response",    [        "status",        "message",        "data"    ])