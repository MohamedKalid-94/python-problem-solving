# Phase 12 — Problem Solving Patterns
# Interview Questions & Answers

---

# 1. What are Problem Solving Patterns?

## Answer:

Problem solving patterns are reusable techniques used to solve
common programming problems efficiently.

Instead of solving every problem from scratch, developers identify
the pattern behind the problem and apply the correct algorithm.

Common patterns:

- Counter Pattern
- Frequency Map
- Two Pointer
- Sliding Window
- Prefix Sum
- Binary Search
- Stack
- Queue
- Recursion
- Divide and Conquer
- Greedy
- Dynamic Programming
- Graph Traversal
- Tree Traversal

These patterns help improve:

- Problem solving speed
- Code quality
- Time complexity
- Interview performance


---

# 2. How do you approach a coding problem in an interview?

## Answer:

A structured approach:

### Step 1: Understand the problem

Ask:

- What is the input?
- What is the expected output?
- Are there constraints?


### Step 2: Identify the pattern

Example:

Finding duplicates:

Use:

Frequency Map


Searching sorted data:

Use:

Binary Search


Continuous subarray:

Use:

Sliding Window


### Step 3: Write simple solution

First create a working solution.

### Step 4: Optimize

Check:

- Time complexity
- Space complexity


### Step 5: Test edge cases

Examples:

- Empty input
- Single element
- Duplicate values
- Large input



---

# 3. What is the Counter Pattern?

## Answer:

Counter Pattern counts occurrences of values.

Example:

Input:


[1,2,2,3,3,3]


Output:


1 -> 1
2 -> 2
3 -> 3


Python:

```python
counter = {}

for item in numbers:
    counter[item] = counter.get(item,0)+1

Used in:
- Log analysis
- Word frequency
- Duplicate detection
Time Complexity:

O(n)
4. What is Frequency Map?
Answer:
Frequency Map stores the count of each unique element.

Example:

Finding duplicate users:
{"user1":3,"user2":1}


Applications:
- Data analysis
- NLP
- Search systems
- Recommendation systems
5. Explain Two Pointer Pattern.
Answer:
Two Pointer uses two indexes to process data efficiently.

Example:

Array:
[1,2,3,4,5]

Pointers:
Left        Right

1             5

Common usage:
- Reverse array
- Palindrome checking
- Pair sum
- Removing duplicates
Complexity:

O(n)
6. Difference between Two Pointer and Sliding Window?
Answer:
Two Pointer
Used when comparing two positions.

Examples:
- Pair sum
- Reverse array
Sliding Window
Used for continuous ranges.

Examples:
- Maximum subarray
- Longest substring
Both reduce nested loops.
7. What is Sliding Window?
Answer:
Sliding Window maintains a moving range of elements.

Example:

Array:
[1,2,3,4,5]

Window size:

3

Windows:
1 2 3

2 3 4

3 4 5

Used in:
- Analytics
- Streaming data
- Rate monitoring
- LLM context management
Complexity:

O(n)
8. What is Prefix Sum?
Answer:
Prefix Sum stores cumulative values.

Example:

Array:
[2,4,6]

Prefix:
[0,2,6,12]

Benefits:

Range queries become faster.

Without Prefix:

O(n)

With Prefix:

O(1)
9. Explain Binary Search.
Answer:
Binary Search finds elements in sorted data.

Process:
1. Find middle element
2. Compare target
3. Remove half of search space
Example:
[10,20,30,40,50]

Target = 40

Search:

Middle = 30

Go right.

Complexity:

O(log n)
10. What is Stack?
Answer:
Stack follows:
LIFO

Last In First Out

Operations:
- Push
- Pop
- Peek
Examples:
- Function calls
- Undo operation
- Browser history
- Expression checking
11. What is Queue?
Answer:
Queue follows:
FIFO

First In First Out

Operations:
- Enqueue
- Dequeue
Examples:
- Task scheduling
- Message queues
- BFS traversal
12. Difference between Stack and Queue?
Answer:
Stack	Queue
LIFO	FIFO
Remove last item	Remove first item
Uses push/pop	Uses enqueue/dequeue
Function calls	Task processing


13. Explain Recursion.
Answer:
Recursion is when a function calls itself.

Every recursion requires:
1. Base Case
Stops execution.
2. Recursive Case
Calls function again.

Example:

Factorial:
5!

5 * 4 * 3 * 2 * 1

Used in:
- Trees
- Graphs
- Backtracking
14. What is Divide and Conquer?
Answer:
Divide and Conquer breaks a large problem into smaller problems.

Steps:
1. Divide
2. Solve
3. Combine
Examples:
- Binary Search
- Merge Sort
- Quick Sort
15. Explain Greedy Algorithm.
Answer:
Greedy chooses the best immediate option.

Example:

Selecting highest value first.

Advantages:
- Simple
- Fast
Limitations:

May not always produce optimal solution.

Examples:
- Activity scheduling
- Resource allocation
16. What is Dynamic Programming?
Answer:
Dynamic Programming solves repeated subproblems
and stores previous results.

Two approaches:
Memoization
Top-down recursion + cache
Tabulation
Bottom-up table

Used in:
- Optimization
- Path finding
- Resource allocation
17. Difference between Greedy and Dynamic Programming?
Answer:
Greedy	Dynamic Programming
Local best choice	Considers previous results
Faster	More computation
Less memory	More memory
Not always optimal	Usually optimal


18. What is Graph Traversal?
Answer:
Graph traversal means visiting nodes of a graph.

Two major algorithms:
BFS
Uses Queue.

Used for:
- Shortest path
- Level traversal
DFS
Uses Stack/Recursion.

Used for:
- Deep exploration
- Backtracking
19. What is Tree Traversal?
Answer:
Tree traversal means visiting every node
in a tree.

Types:
Preorder
Root → Left → Right
Inorder
Left → Root → Right
Postorder
Left → Right → Root
Level Order
Uses BFS.
20. How are these patterns used in AI Engineering?
Answer:
AI systems use these patterns everywhere.

Examples:
RAG Systems
Hash Map:

Metadata lookup

Queue:

Document processing

Graph:

Knowledge graph

Sliding Window:

Context management

Binary Search:

Ranking optimization

Stack:

Agent history

Dynamic Programming:

Optimization problems

Graph Traversal:

Relationship analysis
21. How should I prepare coding interviews?
Answer:
Preparation strategy:
Step 1
Master basic data structures:
- Lists
- Dictionaries
- Sets
- Stack
- Queue
Step 2
Practice patterns:
- Two Pointer
- Sliding Window
- Binary Search
- Recursion
Step 3
Solve problems repeatedly.
Step 4
Explain:
- Approach
- Complexity
- Trade-offs
Step 5
Practice real-world scenarios.
Final Interview Tip
Do not memorize solutions.

Learn to identify patterns.

The interviewer is checking:
- How you think
- How you analyze problems
- How you optimize solutions
- How clearly you explain your approach
A strong engineer can recognize patterns
and apply them to new problems.