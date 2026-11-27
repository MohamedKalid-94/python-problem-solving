# Phase 9 — Iterators & Generators
# Practice Problems

---

# Beginner Level

## 1. Create an Iterator from a List

Create a list:

```python
numbers = [10, 20, 30, 40, 50]

Convert it into an iterator and print values using:
- iter()
- next()
2. Iterate Through a String
Create an iterator for:
text = "Python"


Print each character using next().
3. Iterate Through a Tuple
Create an iterator from:
languages = ("Python", "Java", "C++")


Print all values.
4. Handle StopIteration
Create an iterator with three values.

Call next() more times than available.

Handle the exception using:
try:    except StopIteration:


5. Compare Iterable and Iterator
Create examples of:
- Iterable object
- Iterator object
Check using:
type()


Iterator Protocol Practice
6. Create a Custom Counter Iterator
Create a class:
Counter

Requirements:
- Start value
- End value
- Implement __iter__()
- Implement __next__()
Example:
1
2
3
4
5

7. Reverse Iterator
Create a custom iterator that prints a list in reverse order.

Input:
[1, 2, 3, 4, 5]


Output:
5
4
3
2
1

8. Even Number Iterator
Create an iterator that generates only even numbers.

Example:
2
4
6
8
10

9. Fibonacci Iterator
Create a custom iterator that generates Fibonacci numbers.

Output:
0
1
1
2
3
5
8

10. Employee Iterator
Create an employee iterator.

Input:
employees = [    "John",    "Alice",    "Kalid"]


Iterate one employee at a time.
Generator Practice
11. Create a Simple Generator
Create a generator that produces:
1
2
3
4
5

using yield.
12. Generator for Squares
Create a generator that returns square values.

Input:
1 2 3 4 5

Output:
1 4 9 16 25

13. Even Number Generator
Create a generator that produces even numbers from 1 to 100.
14. Odd Number Generator
Create a generator that produces odd numbers.
15. Multiplication Table Generator
Create a generator for multiplication tables.

Example:

Input:
5

Output:
5
10
15
20

yield Keyword Practice
16. Difference Between yield and return
Create two functions:
- One using return
- One using yield
Compare their behavior.
17. Multiple Yield Statements
Create a generator:
def colors():


Generate:
Red
Green
Blue

18. Generator State
Create a generator that:
- Yields first value
- Receives input using send()
- Continues execution
19. Infinite Counter Generator
Create an infinite generator:

Example:
1
2
3
4
...

Stop manually after 10 values.
20. Random Number Generator
Create a generator that produces random numbers continuously.
Generator Expression Practice
21. Create Generator Expression
Convert:
[x*x for x in range(10)]


into a generator expression.
22. Filter Even Numbers
Create a generator expression that returns only even numbers.
23. Filter Positive Numbers
Input:
[-5, 10, -3, 8, 20]


Generate only positive values.
24. Convert Strings
Create a generator expression to convert:
["python", "ai", "ml"]


into uppercase.
25. Calculate Prices
Generate final prices after adding 18% GST.

Input:
[100, 200, 300]


Lazy Evaluation Practice
26. Large Range Processing
Create a generator for:
range(1000000)


Print only first five values.
27. Lazy File Reader
Create a generator that reads a file line by line.

Requirements:
- Do not load complete file
- Yield one line at a time
28. Lazy Data Filter
Create pipeline:
Data
 ↓
Filter
 ↓
Transform
 ↓
Output

Example:
- Select even numbers
- Square them
29. Lazy API Pagination
Create a generator that simulates:
Page 1
Page 2
Page 3

Fetch pages only when requested.
30. Lazy Log Processor
Process log records one by one.

Input:
INFO
ERROR
WARNING

Real-World Problems
31. CSV Data Processor
Create a generator that:
- Reads CSV rows
- Processes one row at a time
- Returns processed data
32. Large Dataset Loader
Create a dataset loader generator.

Features:
- Load batch by batch
- Avoid memory usage
33. Image Processing Pipeline
Create generator pipeline:
Images
 ↓
Resize
 ↓
Normalize
 ↓
Process

34. AI Dataset Generator
Create a generator that produces:
{    "input": text,    "label": category}


35. RAG Document Chunk Generator
Create a generator that:

Input:
Large Document

Output:
Chunk 1
Chunk 2
Chunk 3

Advanced Challenges
36. Build Custom Range Iterator
Implement your own version of:
range()


Using iterator protocol.
37. Build Infinite Fibonacci Generator
Generate Fibonacci numbers forever.
38. Build Data Pipeline
Create:
Reader Generator
        |
        ↓
Filter Generator
        |
        ↓
Transform Generator
        |
        ↓
Output

39. Build Streaming API Simulator
Create a generator that simulates real-time API responses.
40. Build AI Document Processing Pipeline
Design:
Document Loader
        ↓
Chunk Generator
        ↓
Embedding Generator
        ↓
Vector Storage

Mini Projects
1. Log Analyzer
Features:
- Read logs lazily
- Filter errors
- Count failures
2. CSV Data Pipeline
Features:
- Read CSV
- Filter records
- Transform data
3. Large File Processor
Features:
- Process GB-size files
- Avoid memory issues
4. AI Dataset Loader
Features:
- Batch loading
- Streaming data
- Lazy processing
5. RAG Document Chunking System
Features:
- Read documents
- Split chunks
- Generate embeddings