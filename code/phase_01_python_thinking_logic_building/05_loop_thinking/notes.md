# Phase 1 - Step 5: Loop Thinking Notes

## Overview

A loop is a programming construct that allows a block of code to execute repeatedly until a condition becomes False or a sequence is exhausted.

Loops help us avoid writing the same code multiple times.

Without loops:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Using a loop:

```python
for number in range(1, 6):
    print(number)
```

---

# Why Do We Need Loops?

Loops are used to:

- Repeat tasks
- Process collections of data
- Read user input repeatedly
- Search data
- Count values
- Build patterns
- Automate repetitive work

Examples:

- ATM Menu
- Login Attempts
- Student Marks
- File Processing
- Games
- Traffic Signals

---

# Types of Loops in Python

Python provides two looping statements:

- for loop
- while loop

---

# 1. for Loop

A `for` loop is used when the number of iterations is known.

Syntax:

```python
for variable in sequence:
    statement
```

Example:

```python
for number in range(1, 6):
    print(number)
```

Output

```
1
2
3
4
5
```

---

## range()

The `range()` function generates a sequence of numbers.

### range(stop)

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

### range(start, stop)

```python
for i in range(1, 6):
    print(i)
```

Output

```
1
2
3
4
5
```

---

### range(start, stop, step)

```python
for i in range(2, 11, 2):
    print(i)
```

Output

```
2
4
6
8
10
```

---

## When to Use for Loop

Use when:

- Number of iterations is known
- Printing tables
- Traversing lists
- Counting
- Pattern printing

---

# 2. while Loop

A `while` loop executes as long as a condition remains True.

Syntax

```python
while condition:
    statement
```

Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## When to Use while Loop

Use when:

- Number of iterations is unknown
- Waiting for user input
- Menu-driven programs
- Games
- Validation

---

# Difference Between for and while

| for Loop | while Loop |
|-----------|------------|
| Known iterations | Unknown iterations |
| Uses range() or sequence | Uses condition |
| Easier for counting | Better for user input |

---

# 3. Nested Loops

A nested loop is a loop inside another loop.

Syntax

```python
for row in range(3):

    for column in range(3):
        print(row, column)
```

Flow

```
Outer Loop

    |

Inner Loop

    |

Execute
```

---

## Uses

- Star patterns
- Number patterns
- Multiplication tables
- Matrix processing
- Coordinate generation

---

# 4. break Statement

The `break` statement immediately terminates the nearest loop.

Example

```python
for number in range(10):

    if number == 5:
        break

    print(number)
```

Output

```
0
1
2
3
4
```

---

## Uses

- Search operations
- Exit menus
- Login validation
- Stop processing

---

# 5. continue Statement

The `continue` statement skips the current iteration and moves to the next one.

Example

```python
for number in range(6):

    if number == 3:
        continue

    print(number)
```

Output

```
0
1
2
4
5
```

---

## Uses

- Skip invalid data
- Ignore unwanted values
- Data filtering

---

# 6. pass Statement

The `pass` statement performs no action.

It acts as a placeholder.

Example

```python
if True:
    pass
```

---

## Uses

- Future implementation
- Empty loops
- Empty functions
- Empty classes

---

# 7. Loop else

Python allows an `else` block with loops.

The `else` block executes only if the loop finishes normally.

If the loop exits using `break`, the `else` block does not execute.

Example

```python
numbers = [10,20,30]

for number in numbers:

    if number == 50:
        break

else:
    print("Not Found")
```

---

## Uses

- Searching
- Prime number checking
- Validation

---

# 8. Infinite Loop

An infinite loop never ends unless stopped.

Example

```python
while True:
    print("Running")
```

Stop using

```
Ctrl + C
```

or

```python
break
```

---

## Uses

- Games
- Chat servers
- ATM menus
- Continuous monitoring

---

# 9. Sentinel Loop

A sentinel loop stops when a special value is entered.

Example

```python
while True:

    number = int(input())

    if number == 0:
        break
```

Here,

```
0
```

is the sentinel value.

Common sentinel values

- 0
- -1
- quit
- exit

---

# Loop Patterns

These are common ways loops are used.

---

## Counting Pattern

Counts items.

Example

```python
count = 0

for item in items:
    count += 1
```

Applications

- Student count
- Product count
- Employee count

---

## Searching Pattern

Find a required value.

Example

```python
found = False

for item in items:

    if item == target:
        found = True
        break
```

Applications

- Search user
- Search product
- Search student

---

## Filtering Pattern

Process only matching values.

Example

```python
for number in numbers:

    if number % 2 != 0:
        continue

    print(number)
```

Applications

- Even numbers
- Valid marks
- Active users

---

## Repeating Pattern

Repeat an action multiple times.

Example

```python
for i in range(5):
    print("Welcome")
```

Applications

- Notifications
- Printing
- Reports

---

## Simulation Pattern

Simulate a real-world process.

Example

```python
signals = ["Red","Yellow","Green"]

for signal in signals:
    print(signal)
```

Applications

- Traffic signals
- Dice games
- ATM
- Elevator
- Queue systems

---

# Choosing the Right Loop

Use **for loop** when:

- Number of repetitions is known
- Working with lists
- Working with strings
- Using range()

Use **while loop** when:

- Waiting for user input
- Condition controls execution
- Menu-driven programs
- Unknown repetitions

---

# Common Mistakes

## Infinite Loop

Wrong

```python
count = 1

while count <= 5:
    print(count)
```

Problem

```
count never changes
```

Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Wrong Indentation

Wrong

```python
for i in range(5):
print(i)
```

Correct

```python
for i in range(5):
    print(i)
```

---

## Using break Incorrectly

Remember:

```
break exits the loop completely.
```

---

## Using continue Incorrectly

Remember:

```
continue skips only one iteration.
```

---

# Best Practices

- Choose the correct loop.
- Avoid unnecessary infinite loops.
- Keep loop bodies small.
- Use meaningful variable names.
- Update loop variables in while loops.
- Use break only when necessary.
- Use continue for filtering.
- Avoid deep nesting.

---

# Real-World Applications

## Banking

- ATM menu
- PIN attempts
- Transaction history

---

## Education

- Student marks
- Attendance
- Grade processing

---

## E-Commerce

- Shopping cart
- Product search
- Order processing

---

## Gaming

- Game loop
- Score counting
- Player movement

---

## Data Processing

- Reading files
- Filtering records
- Searching data
- Report generation

---

# Quick Revision

| Concept | Purpose |
|----------|----------|
| for | Known iterations |
| while | Unknown iterations |
| Nested Loop | Loop inside loop |
| break | Exit loop |
| continue | Skip current iteration |
| pass | Placeholder |
| loop else | Execute when loop ends normally |
| Infinite Loop | Runs forever |
| Sentinel Loop | Stops on special value |
| Counting | Count items |
| Searching | Find value |
| Filtering | Select matching values |
| Repeating | Repeat actions |
| Simulation | Model real processes |

---

# Summary

After completing this module, you can:

- Write for loops
- Write while loops
- Create nested loops
- Use break, continue and pass
- Use loop else
- Build infinite and sentinel loops
- Apply common loop patterns
- Solve iterative programming problems

---

## Next Module

```
Phase 1 – Step 6

Functions
```