# Phase 9 — Iterators & Generators

## Overview

Iterators and generators are advanced Python concepts used for efficient and memory-friendly data processing.

They allow programs to process data one item at a time instead of loading the complete dataset into memory.

These concepts are widely used in:

- Backend development
- Data engineering
- Machine learning pipelines
- AI/GenAI applications
- Streaming systems
- Large-scale data processing

---

# Learning Objectives

After completing this phase, you will understand:

- Iterable vs Iterator
- Iterator protocol
- `iter()` and `next()`
- `StopIteration`
- Creating custom iterators
- Generator functions
- `yield` keyword
- Generator expressions
- Lazy evaluation
- Streaming data processing
- Real-world generator pipelines

---

# Folder Structure

```text
09_iterators_generators/

├── 01_iterator_protocol/
│   └── 01_iterator_protocol_complete.py
│
├── 02_yield_keyword/
│   └── 02_yield_keyword_complete.py
│
├── 03_generator_expressions/
│   └── 03_generator_expressions_complete.py
│
├── 04_lazy_evaluation/
│   └── 04_lazy_evaluation_complete.py
│
├── 05_iterators_generators_real_world_problems/
│   └── 05_iterators_generators_real_world_problems_complete.py
│
├── interview_qanda.md
├── notes.md
├── practice.md
└── README.md

Topics Covered
1. Iterator Protocol
Learn how Python iteration works internally.

Topics:
- Iterable objects
- Iterator objects
- __iter__()
- __next__()
- iter()
- next()
- StopIteration
Example:
numbers = iter([1, 2, 3])print(next(numbers))


2. Custom Iterators
Learn how to create your own iterator classes.

Concepts:
- Iterator class design
- Internal state management
- Custom sequence generation
Example:
class Counter:    def __iter__(self):        return self    def __next__(self):        return value


3. Generator Functions
Generators are special functions that return values using yield.

Example:
def numbers():    yield 1    yield 2    yield 3


Benefits:
- Memory efficient
- Lazy execution
- Handles large data
4. yield Keyword
The yield keyword:
- Returns a value
- Pauses execution
- Saves function state
- Resumes later
Difference:
return
 |
 └── Function ends

yield
 |
 └── Function pauses

5. Generator Expressions
Generator expressions provide a shorter way to create generators.

Syntax:
(expression for item in iterable)


Example:
squares = (x*x for x in range(10))


Benefits:
- Less memory usage
- Cleaner syntax
- Lazy processing
6. Lazy Evaluation
Lazy evaluation means delaying computation until the result is required.

Example:

List:
numbers = [x*x for x in range(100000)]


All values are created immediately.

Generator:
numbers = (x*x for x in range(100000))


Values are generated when needed.
Iterator vs Generator
Iterator	Generator
Created using class	Created using function
Requires __iter__()	Uses yield
Requires __next__()	Python manages automatically
More code	Less code
More control	Easier implementation


Eager vs Lazy Evaluation
Eager Evaluation	Lazy Evaluation
Executes immediately	Executes when required
Stores all results	Generates values one by one
More memory usage	Less memory usage
Suitable for small data	Suitable for large data


Real-World Applications
1. Large File Processing
Instead of loading the complete file:
file.readlines()


Process one line at a time:
for line in file:    process(line)


2. API Pagination
Generators can fetch API data page by page.

Example:
API
 |
Page 1
 |
Page 2
 |
Page 3

Only required pages are loaded.
3. Batch Data Processing
Large datasets can be processed in batches.

Example:
Dataset
   |
Batch 1
   |
Batch 2
   |
Batch 3

4. Machine Learning Data Loading
Generators are used for:
- Training data streaming
- Batch generation
- Large dataset loading
5. AI/GenAI Applications
Generators are commonly used in:
RAG Pipeline
Document
    |
    ↓
Chunk Generator
    |
    ↓
Embedding Model
    |
    ↓
Vector Database

LLM Streaming Response
User Query
    |
    ↓
LLM
    |
    ↓
Token Generator
    |
    ↓
Streaming Output

Skills Developed
Python Skills
- Iterator implementation
- Generator creation
- Lazy processing
- Memory optimization
Software Engineering Skills
- Streaming architecture
- Pipeline design
- Efficient data processing
- Resource optimization
AI/GenAI Skills
Understanding:
- Document chunk generators
- Dataset loaders
- Streaming responses
- Batch processing pipelines
Practice Coverage
This phase includes practice problems for:
- Creating iterators
- Custom iterator classes
- Generator functions
- Generator expressions
- Lazy pipelines
- File processing
- API pagination
- AI dataset loading
- RAG document chunking
Interview Preparation
Important interview topics:
- What is an iterator?
- Iterable vs iterator
- Iterator protocol
- How does for loop work internally?
- Difference between iterator and generator
- yield vs return
- Generator expressions
- Lazy evaluation
- Memory optimization
- Real-world generator use cases
Best Practices
- Use generators for large datasets.
- Avoid unnecessary list creation.
- Use lazy evaluation when possible.
- Use iterators for custom collection behavior.
- Build pipelines using generator chaining.
- Keep generator functions simple.
- Handle exhausted generators properly.
Learning Outcome
After completing Phase 9, you will be able to:
- Explain Python iteration internally.
- Create custom iterators.
- Write efficient generator functions.
- Use generator expressions.
- Apply lazy evaluation.
- Process large datasets efficiently.
- Build streaming data pipelines.
- Understand iterator/generator usage in AI and backend systems.