# Phase 12 — Problem Solving Patterns Notes

## Overview

Problem Solving Patterns are reusable techniques that help developers
solve coding problems efficiently.

Instead of creating a new solution every time, we identify the
underlying pattern and apply the correct approach.

These patterns are extremely important for:

- Coding interviews
- Software engineering
- AI engineering
- System optimization


---

# 1. Counter Pattern

## Concept

Counter Pattern counts occurrences of elements.

Example:

Input:


[1,2,2,3,3,3]

Output:


1 -> 1
2 -> 2
3 -> 3


## Python Implementation

```python
count = {}

for item in numbers:
    count[item] = count.get(item,0)+1

Applications
- Duplicate detection
- Word frequency
- Log analysis
- User activity counting
2. Frequency Map
Concept
A Frequency Map stores the relationship:
Value -> Count

Example:
{
 "python":5,
 "AI":3
}

Applications
- NLP
- Search engines
- Recommendation systems
- Data analytics
3. Filter Pattern
Concept
Extract elements that satisfy a condition.

Example:

Find even numbers.

Input:
[1,2,3,4]

Output:
[2,4]

Applications
- Data cleaning
- Filtering users
- Removing invalid records
4. Transform Pattern
Concept
Convert data from one format to another.

Example:

Convert:
["python","ai"]

into:
["PYTHON","AI"]

Applications
- Data preprocessing
- ETL pipelines
- Feature engineering
5. Search Pattern
Concept
Find required information from data.

Examples:
- Linear Search
- Binary Search
Applications:
- Database lookup
- Document retrieval
- Information systems
6. Maximum / Minimum Pattern
Concept
Find the highest or lowest value.

Example:

Largest transaction:
1000
5000
2000

Answer:
5000

Applications:
- Analytics
- Monitoring
- Ranking systems
7. Running Total Pattern
Concept
Maintain cumulative values while processing data.

Example:

Input:
10 20 30

Running total:
10
30
60

Applications:
- Finance
- Reports
- Analytics
8. Two Pointer Pattern
Concept
Use two indexes to process data efficiently.

Common approaches:
Left and Right Pointer
Example:
[1,2,3,4,5]

L       R

Applications:
- Reverse array
- Pair sum
- Palindrome
- Removing duplicates
Complexity:

O(n)
9. Sliding Window
Concept
Maintain a moving range of elements.

Example:

Array:
[1,2,3,4,5]

Window size:

3

Windows:
1 2 3

2 3 4

3 4 5

Applications:
- Moving average
- API monitoring
- Streaming analytics
- LLM context handling
10. Prefix Sum
Concept
Store cumulative calculations.

Example:

Array:
[2,4,6]

Prefix:
[0,2,6,12]

Benefits:

Fast range queries.

Complexity:

Preprocessing:

O(n)

Query:

O(1)
11. Binary Search
Concept
Search sorted data by repeatedly dividing
the search space.

Steps:
1. Find middle
2. Compare value
3. Remove half
Complexity:
O(log n)

Applications:
- Database indexes
- Search optimization
- Ranking systems
12. Stack Pattern
Concept
Stack follows:
LIFO

Last In First Out

Operations:
- Push
- Pop
- Peek
Applications:
- Undo feature
- Browser history
- Function calls
- Agent rollback
13. Queue Pattern
Concept
Queue follows:
FIFO

First In First Out

Operations:
- Enqueue
- Dequeue
Applications:
- Task scheduling
- Message queues
- Background jobs
- AI pipelines
14. Recursion Pattern
Concept
A function calling itself.

Every recursion requires:
Base Case
Stops recursion.
Recursive Case
Calls itself with smaller input.

Applications:
- Tree traversal
- Graph algorithms
- Backtracking
15. Divide and Conquer
Concept
Break a large problem into smaller problems.

Steps:
1. Divide
2. Conquer
3. Combine
Examples:
- Binary Search
- Merge Sort
- Quick Sort
16. Greedy Thinking
Concept
Choose the best immediate option.

Advantages:
- Simple
- Fast
Limitations:

May not always produce optimal solution.

Applications:
- Scheduling
- Resource allocation
- Ranking systems
17. Dynamic Programming
Concept
Solve repeated subproblems and store results.

Two approaches:
Memoization
Top-down:
Recursion + Cache

Tabulation
Bottom-up:
Build Table

Applications:
- Optimization
- Planning
- Path finding
18. Graph Traversal
Concept
Visit nodes in a graph.

Two algorithms:
BFS
Uses Queue.

Applications:
- Shortest path
- Network traversal
DFS
Uses Stack/Recursion.

Applications:
- Backtracking
- Deep exploration
19. Tree Traversal
Concept
Visit every node in a tree.

Types:
Preorder
Root → Left → Right

Inorder
Left → Root → Right

Postorder
Left → Right → Root

Level Order
Uses BFS.
Problem Solving Decision Guide
Problem Type	Pattern
Count occurrences	Frequency Map
Find duplicates	Counter
Sorted search	Binary Search
Pair matching	Two Pointer
Continuous range	Sliding Window
Range calculations	Prefix Sum
Undo/backtracking	Stack
Processing tasks	Queue
Tree problems	Recursion
Optimization	Dynamic Programming
Scheduling	Greedy
Network relationships	Graph


AI Engineering Applications
RAG Systems
Patterns used:
Hash Map
Metadata lookup
Queue
Document processing
Graph
Knowledge relationships
Sliding Window
Context management
Binary Search
Ranking optimization
Stack
Agent execution history
Dynamic Programming
Optimization
Interview Preparation Rules
Always Explain:
1. Problem understanding
2. Approach
3. Data structure choice
4. Algorithm
5. Time complexity
6. Space complexity
Complexity Reference
Complexity	Meaning
O(1)	Constant
O(log n)	Very efficient
O(n)	Linear
O(n log n)	Sorting efficiency
O(n²)	Nested loops
O(2^n)	Exponential


Final Learning Goal
The objective is not memorizing algorithms.

The goal is:

Recognize the pattern → Choose the right approach → Build an efficient solution.

A strong AI/software engineer combines:
- Data structures
- Algorithms
- Problem solving patterns
- System thinking
- Real-world application knowledge