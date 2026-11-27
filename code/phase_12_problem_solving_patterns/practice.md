# Phase 12 — Problem Solving Patterns Practice

## Purpose

This practice file contains problems designed to build
problem-solving ability using common programming patterns.

Goal:

- Understand the pattern
- Identify the correct approach
- Write efficient solutions
- Explain complexity during interviews


---

# Level 1 — Basic Pattern Practice

---

# 1. Counter Pattern

## Problem 1: Count Frequency

Given:


numbers = [1,2,2,3,3,3,4]

Find the frequency of each number.


Expected Output:


{
1:1,
2:2,
3:3,
4:1
}


Pattern:

Counter Pattern


---

## Problem 2: Find Duplicate Values

Given:


numbers = [10,20,30,20,40,10]


Find duplicate elements.


Expected:


[10,20]


Pattern:

Frequency Map



---

# 2. Filter Pattern

## Problem 3: Find Even Numbers

Input:


[1,2,3,4,5,6]


Output:


[2,4,6]


Pattern:

Filtering



---

## Problem 4: Filter Active Users

Input:

```python
users = [
    {
        "name":"A",
        "active":True
    },
    {
        "name":"B",
        "active":False
    }
]

Return only active users.

Pattern:

Filter Pattern
3. Transform Pattern
Problem 5: Convert Names
Input:
["python","ai","llm"]

Output:
["PYTHON","AI","LLM"]

Pattern:

Transform Pattern
Level 2 — Intermediate Problems
4. Maximum / Minimum Pattern
Problem 6: Highest Transaction
Input:
[
1000,
5000,
2000,
8000
]

Find maximum transaction.

Pattern:

Maximum Pattern
Problem 7: Lowest Temperature
Input:
[
32,
25,
28,
30
]

Find minimum value.

Pattern:

Minimum Pattern
5. Running Total Pattern
Problem 8: Calculate Running Balance
Input:
[100,-20,50,-10]

Output:
100
80
130
120

Pattern:

Running Total
6. Two Pointer Pattern
Problem 9: Reverse Array
Input:
[1,2,3,4,5]

Output:
[5,4,3,2,1]

Pattern:

Two Pointer
Problem 10: Check Palindrome
Input:
"madam"

Output:
True

Pattern:

Two Pointer
7. Sliding Window
Problem 11: Maximum Sum Subarray
Input:
[2,1,5,1,3,2]

Window:

3

Find maximum sum.

Pattern:

Sliding Window
Problem 12: Average Traffic
API requests:
[100,120,150,200,180]

Window:

3

Find moving average.

Pattern:

Sliding Window
8. Prefix Sum
Problem 13: Range Sum Query
Array:
[2,4,6,8]

Query:
index 1 to 3

Output:
18

Pattern:

Prefix Sum
9. Binary Search
Problem 14: Search Number
Input:
[10,20,30,40,50]

Target:
40

Return index.

Pattern:

Binary Search
Level 3 — Data Structure Problems
10. Stack Pattern
Problem 15: Valid Parentheses
Input:
"({[]})"

Output:
True

Pattern:

Stack
Problem 16: Browser History
Operations:
visit google

visit github

back

Return previous page.

Pattern:

Stack
11. Queue Pattern
Problem 17: Task Processing
Tasks:
[
"Email",
"Report",
"Backup"
]

Process in order.

Pattern:

Queue
Level 4 — Recursive Problems
12. Recursion Pattern
Problem 18: Factorial
Input:
5

Output:
120

Pattern:

Recursion
Problem 19: Sum of Numbers
Input:
10

Output:
55

Pattern:

Recursion
Problem 20: Reverse String
Input:
"python"

Output:
"nohtyp"

Pattern:

Recursion
Level 5 — Algorithmic Thinking
13. Divide and Conquer
Problem 21: Implement Binary Search
Input:

Sorted array:
[1,3,5,7,9]

Find:
7

Pattern:

Divide and Conquer
Problem 22: Merge Two Sorted Lists
Input:
[1,3,5]

[2,4,6]

Output:
[1,2,3,4,5,6]

Pattern:

Divide and Conquer
14. Greedy Problems
Problem 23: Coin Change
Coins:
[25,10,5,1]

Amount:
63

Find minimum coins.

Pattern:

Greedy
Problem 24: Activity Selection
Given meetings:
(1,3)

(2,5)

(4,6)

Select maximum non-overlapping meetings.

Pattern:

Greedy
15. Dynamic Programming
Problem 25: Fibonacci DP
Find:
F(10)

Use:
- Memoization
- Tabulation
Pattern:

Dynamic Programming
Problem 26: Climbing Stairs
A person can climb:
- 1 step
- 2 steps
Find number of ways for:
5 steps

Pattern:

Dynamic Programming
16. Graph Problems
Problem 27: BFS Traversal
Graph:
A -> B,C

B -> D

C -> E

Output BFS order.

Pattern:

Graph Traversal
Problem 28: DFS Traversal
Same graph.

Output DFS order.

Pattern:

Graph Traversal
17. Tree Problems
Problem 29: Preorder Traversal
Tree:
      A

    /   \

   B     C

Output:
A B C

Pattern:

Tree Traversal
Problem 30: Level Order Traversal
Tree:
       1

     /   \

    2     3

Output:
1 2 3

Pattern:

BFS Tree Traversal
Real-World AI Engineering Practice
31. Log Analyzer
Input:
[
"ERROR",
"INFO",
"ERROR"
]

Find error frequency.

Patterns:
- Counter
- Dictionary
32. Document Search
Input:

Documents:
[
"python ai",
"machine learning",
"python programming"
]

Search:
python

Patterns:
- Search
- Filtering
33. RAG Chunk Processing
Given:

100 documents.

Tasks:
1. Split documents
2. Process chunks
3. Store embeddings
Identify patterns:

Answer:
- Queue
- Hash Map
- Sliding Window
34. AI Agent Task Planner
Agent tasks:
Research

Analyze

Generate

Validate

Choose suitable data structures.

Expected:
- Queue
- Stack
- Graph
Interview Practice Checklist
For every problem:
Step 1
Explain the problem.
Step 2
Identify pattern.
Step 3
Choose data structure.
Step 4
Write solution.
Step 5
Explain complexity.