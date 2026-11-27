# Phase 9 — Iterators & Generators

## Overview

Iterators and generators are advanced Python concepts used for efficient data processing. They allow programs to process data one item at a time instead of loading all data into memory.

These concepts are important for:

- Python backend development
- Data engineering
- Machine learning pipelines
- AI/GenAI applications
- Large file processing
- Streaming systems

---

# 1. Iterator

An iterator is an object that allows sequential access to elements.

It returns one value at a time.

Example:

```python
numbers = iter([10, 20, 30])

print(next(numbers))

Output:
10

Iterable vs Iterator
Iterable
An iterable is an object that can be converted into an iterator.

Examples:
- List
- Tuple
- String
- Dictionary
- Set
- Range
Example:
numbers = [1, 2, 3]


Iterator
An iterator is an object that produces values one by one.

Example:
iterator = iter(numbers)


2. Iterator Protocol
Python iterator protocol defines how an object behaves as an iterator.

An iterator must implement two methods:
iter()
Returns the iterator object.

Example:
def __iter__(self):    return self


next()
Returns the next value.

Example:
def __next__(self):    return value


Creating Custom Iterator
Example:
class Counter:    def __init__(self, limit):        self.limit = limit        self.current = 1    def __iter__(self):        return self    def __next__(self):        if self.current <= self.limit:            value = self.current            self.current += 1            return value        raise StopIteration


iter() Function
iter() converts an iterable object into an iterator.

Example:
numbers = [1, 2, 3]iterator = iter(numbers)


next() Function
next() retrieves the next item from an iterator.

Example:
print(next(iterator))


StopIteration
When an iterator has no more values, Python raises:
StopIteration


Example:
next(iterator)


after all values are completed.
How for Loop Works Internally
Code:
for item in numbers:    print(item)


Internally works like:
iterator = iter(numbers)while True:    try:        item = next(iterator)    except StopIteration:        break


3. Generator
A generator is a special type of iterator created using the yield keyword.

Generators produce values lazily.

Example:
def numbers():    yield 1    yield 2    yield 3


yield Keyword
yield:
- Returns a value
- Pauses function execution
- Saves function state
- Continues from the same position later
Example:
def generator():    yield 10    yield 20


yield vs return
return	yield
Ends function execution	Pauses execution
Returns once	Returns multiple values
Stores complete result	Generates values one by one
More memory usage	Less memory usage


Generator Execution
Calling a generator function:
result = generator()


does not execute immediately.

Execution starts when:
next(result)


is called.
Generator State
A generator remembers:
- Current execution position
- Local variables
- Internal state
Example:
yield value


pauses execution.

The next call continues from that point.
Infinite Generator
A generator can produce unlimited values.

Example:
def counter():    value = 1    while True:        yield value        value += 1


Used for:
- Counters
- Streams
- Sensor data
4. Generator Expressions
A generator expression creates a generator using compact syntax.

Syntax:
(expression for item in iterable)


Example:
squares = (x*x for x in range(10))


List Comprehension vs Generator Expression
List Comprehension	Generator Expression
Uses []	Uses ()
Creates all values immediately	Creates values when required
Uses more memory	Uses less memory
Good for small data	Good for large data


Example:

List:
[x*x for x in range(10)]


Generator:
(x*x for x in range(10))


5. Lazy Evaluation
Lazy evaluation means delaying computation until the value is actually needed.

Generators use lazy evaluation.
Eager vs Lazy Evaluation
Eager Evaluation
Calculation happens immediately.

Example:
numbers = [x*x for x in range(100000)]


All values are created and stored.
Lazy Evaluation
Calculation happens only when requested.

Example:
numbers = (x*x for x in range(100000))


Values are created one by one.
Advantages of Lazy Evaluation
Memory Efficiency
Only required values are stored.
Faster Execution Start
No need to calculate unused data.
Large Data Processing
Useful for:
- Large files
- Big datasets
- Streaming systems
Generator Pipeline
Multiple generators can be connected together.

Example:
Input Data
    |
    ↓
Read Generator
    |
    ↓
Filter Generator
    |
    ↓
Transform Generator
    |
    ↓
Output

Benefits:
- Cleaner code
- Better memory usage
- Efficient processing
Real-World Applications
1. Large File Processing
Instead of:
file.readlines()


Use:
for line in file:    process(line)


Only one line is processed at a time.
2. API Pagination
Generators can fetch data page by page.

Example:
Page 1
Page 2
Page 3

Only required pages are loaded.
3. Batch Processing
Large datasets can be processed in batches.

Example:
Data
 ↓
Batch 1
 ↓
Batch 2
 ↓
Batch 3

4. Machine Learning Data Loading
Generators are used for:
- Training data loading
- Batch generation
- Dataset streaming
5. RAG Document Processing
Generators are useful for document chunking.

Example:
Document
    ↓
Chunk Generator
    ↓
Embedding Model
    ↓
Vector Database

Large documents can be processed efficiently.
Iterator vs Generator
Iterator	Generator
Created using class	Created using function
Requires iter()	Uses yield
Requires next()	Python manages automatically
More code	Less code
More control	Easier implementation


Best Practices
- Use generators for large datasets.
- Avoid unnecessary list creation.
- Use lazy evaluation for streaming data.
- Use custom iterators when you need custom behavior.
- Use generator pipelines for data processing.
- Handle StopIteration properly.