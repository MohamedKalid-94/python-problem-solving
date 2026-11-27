# Phase 9 — Iterators & Generators
# Interview Questions and Answers

---

## 1. What is an iterator in Python?

An iterator is an object that allows sequential access to elements one at a time without storing the entire collection in memory.

An iterator implements:

- `__iter__()`
- `__next__()`

Example:

```python
numbers = iter([1, 2, 3])

print(next(numbers))

2. What is the difference between iterable and iterator?
Iterable	Iterator
Object that can be looped	Object that gives next value
Implements __iter__()	Implements __iter__() and __next__()
Example: list, tuple, string	Example: iter(list)


Example:
numbers = [1, 2, 3]iterator = iter(numbers)


3. What are examples of iterables in Python?
Common iterables:
- List
- Tuple
- String
- Dictionary
- Set
- Range
Example:
for value in [1, 2, 3]:    print(value)


4. What is the iterator protocol?
The iterator protocol defines rules that an object must follow to behave as an iterator.

It requires two methods:
__iter__()
Returns the iterator object.
__next__()
Returns the next value.
5. What does iter() function do?
iter() converts an iterable object into an iterator.

Example:
numbers = [10, 20, 30]iterator = iter(numbers)


6. What does next() function do?
next() retrieves the next item from an iterator.

Example:
print(next(iterator))


7. What happens when an iterator has no more values?
Python raises:
StopIteration


Example:
next(iterator)


after all values are consumed.
8. How does a for loop work internally?
A for loop internally:
1. Calls iter() on the object.
2. Calls next() repeatedly.
3. Stops when StopIteration occurs.
Example:
for item in numbers:    print(item)


is internally similar to:
iterator = iter(numbers)while True:    try:        item = next(iterator)    except StopIteration:        break


Generator Questions
9. What is a generator in Python?
A generator is a special type of iterator that generates values lazily using the yield keyword.

Example:
def numbers():    yield 1    yield 2


10. Difference between iterator and generator?
Iterator	Generator
Created using class	Created using function
Requires __iter__() and __next__()	Uses yield
More code	Less code
Manual implementation	Python handles internally


11. What is the yield keyword?
yield returns a value from a generator and pauses the function execution.

The function state is saved and continues from the same point later.
12. Difference between yield and return?
return	yield
Ends function	Pauses function
Returns single value	Returns multiple values
Stores complete result	Generates values one by one


Example:
def generator():    yield 1    yield 2


13. Why are generators memory efficient?
Generators do not store all values in memory.

They generate values only when required.

Example:
(number for number in range(1000000))


Only one value exists at a time.
14. Can a generator be reused?
No.

Once a generator is exhausted, it cannot restart.

A new generator object must be created.
15. What is generator state?
Generator state means the current execution position of a generator.

When yield pauses execution, Python remembers:
- Local variables
- Current position
- Execution state
16. What happens when a generator function is called?
Calling a generator function does not execute it immediately.

It returns a generator object.

Example:
result = my_generator()


Execution starts only when:
next(result)


is called.
Generator Expression Questions
17. What is a generator expression?
A generator expression creates generators using compact syntax.

Example:
numbers = (x*x for x in range(10))


18. Difference between list comprehension and generator expression?
List Comprehension	Generator Expression
Uses []	Uses ()
Creates entire list	Creates values lazily
More memory	Less memory


Example:
[x*x for x in range(10)](x*x for x in range(10))


19. When should we use generator expressions?
Use generator expressions when:
- Processing large data
- Reading large files
- Streaming data
- Memory optimization is required
Lazy Evaluation Questions
20. What is lazy evaluation?
Lazy evaluation means delaying computation until the result is actually needed.

Generators use lazy evaluation.
21. Difference between eager and lazy evaluation?
Eager Evaluation	Lazy Evaluation
Executes immediately	Executes when needed
Uses more memory	Uses less memory
Stores results	Generates results


22. Example of eager evaluation?
List comprehension:
numbers = [x*x for x in range(100000)]


All values are created immediately.
23. Example of lazy evaluation?
Generator expression:
numbers = (x*x for x in range(100000))


Values are created one by one.
24. Why is lazy evaluation useful?
Advantages:
- Lower memory usage
- Faster startup time
- Handles large datasets
- Supports streaming
Real-World Questions
25. Where are generators used in real applications?
Generators are used in:
- Large file processing
- Data pipelines
- API pagination
- Machine learning datasets
- Log processing
- Streaming systems
- RAG document chunking
26. How are generators used in AI/ML?
Examples:
- Loading large datasets
- Batch processing training data
- Creating document chunks
- Streaming embeddings
Example:
Document
    ↓
Chunk Generator
    ↓
Embedding Model
    ↓
Vector Database

27. How would you process a large CSV file?
Instead of loading the complete file:
data = file.readlines()


Use a generator:
for row in csv_reader:    process(row)


This reduces memory usage.
28. How does pagination use generators?
A generator can fetch pages only when required.

Example:
def pages():    for page in api_response:        yield page


Useful for APIs with thousands of records.
29. What is an infinite generator?
A generator that can produce unlimited values.

Example:
def counter():    value = 1    while True:        yield value        value += 1


30. Can generators improve application performance?
Yes.

They improve performance by:
- Reducing memory usage
- Avoiding unnecessary calculations
- Processing data incrementally
Interview Coding Questions
31. Create a generator for numbers from 1 to 10.
def numbers():    for i in range(1, 11):        yield i


32. Create a generator for even numbers.
def even_numbers(values):    for value in values:        if value % 2 == 0:            yield value


33. Create a custom iterator.
Implement:
- __iter__()
- __next__()
34. Read a large file using a generator.
Expected approach:
- Read one line
- Yield line
- Process line
- Avoid loading complete file
35. Create a generator pipeline.
Example:
Read Data
    ↓
Filter Data
    ↓
Transform Data
    ↓
Output Result