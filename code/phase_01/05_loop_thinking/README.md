# Phase 1 - Step 5: Loop Thinking

## Overview

Loops are one of the most fundamental concepts in programming. They allow us to execute a block of code repeatedly without writing the same statements multiple times.

Python provides two primary looping constructs:

- **for loop**
- **while loop**

In addition to these, Python offers several loop control statements and advanced looping techniques such as:

- Nested loops
- `break`
- `continue`
- `pass`
- Loop `else`
- Infinite loops
- Sentinel loops
- Common loop patterns

Mastering loops is essential for solving programming problems, processing collections, automating repetitive tasks, and building real-world applications.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand loop fundamentals
- Write `for` loops
- Write `while` loops
- Use nested loops
- Control loop execution using `break`
- Skip iterations using `continue`
- Use `pass` as a placeholder
- Understand loop `else`
- Create infinite loops safely
- Build sentinel-controlled loops
- Apply common loop patterns
- Solve beginner and intermediate loop problems

---

# Prerequisites

Before starting this module, you should know:

- Variables
- Data Types
- Expressions
- Operators
- Decision Making (`if`, `if else`, `if elif else`)

Previous Module:

```
Phase 1 – Step 4
Decision Making
```

---

# Learning Flow

```
for Loop
      ↓
while Loop
      ↓
Nested Loops
      ↓
break
      ↓
continue
      ↓
pass
      ↓
Loop else
      ↓
Infinite Loops
      ↓
Sentinel Loops
      ↓
Loop Patterns
      ↓
Problem Solving
```

---

# Repository Structure

```
05_loop_thinking/

│
├── README.md
├── notes.md
├── practice.md
├── interview_questions.md
│
├── 01_for_loop/
│   ├── 01_print_numbers.py
│   ├── 02_print_even_numbers.py
│   ├── 03_multiplication_table.py
│   └── 04_sum_of_numbers.py
│
├── 02_while_loop/
│   ├── 01_print_numbers.py
│   ├── 02_countdown.py
│   ├── 03_sum_until_limit.py
│   └── 04_guess_attempts.py
│
├── 03_nested_loops/
│   ├── 01_number_pattern.py
│   ├── 02_star_pattern.py
│   ├── 03_multiplication_grid.py
│   └── 04_coordinate_pairs.py
│
├── 04_break_statement/
│   ├── 01_stop_at_number.py
│   ├── 02_search_item.py
│   ├── 03_exit_on_password.py
│   └── 04_break_nested_loop.py
│
├── 05_continue_statement/
│   ├── 01_skip_even_numbers.py
│   ├── 02_skip_negative_numbers.py
│   ├── 03_skip_specific_character.py
│   └── 04_skip_invalid_marks.py
│
├── 06_pass_statement/
│   ├── 01_empty_if.py
│   ├── 02_empty_loop.py
│   ├── 03_placeholder_program.py
│   └── 04_future_logic.py
│
├── 07_loop_else/
│   ├── 01_search_number.py
│   ├── 02_find_prime.py
│   ├── 03_login_attempt.py
│   └── 04_search_name.py
│
├── 08_infinite_loops/
│   ├── 01_basic_infinite_loop.py
│   ├── 02_break_infinite_loop.py
│   ├── 03_menu_program.py
│   └── 04_continuous_counter.py
│
├── 09_sentinel_loops/
│   ├── 01_exit_on_zero.py
│   ├── 02_exit_on_quit.py
│   ├── 03_sum_until_negative.py
│   └── 04_student_marks_input.py
│
└── 10_loop_patterns/
    ├── 01_counting_pattern.py
    ├── 02_searching_pattern.py
    ├── 03_filtering_pattern.py
    ├── 04_repeating_pattern.py
    └── 05_simulation_pattern.py
```

---

# Topics Covered

## 1. for Loop

Used when the number of iterations is known.

Examples:

- Print numbers
- Even numbers
- Multiplication tables
- Sum of numbers

---

## 2. while Loop

Used when the number of iterations depends on a condition.

Examples:

- Countdown
- Guess attempts
- Menu systems
- User input

---

## 3. Nested Loops

A loop inside another loop.

Examples:

- Star patterns
- Number patterns
- Multiplication grids
- Coordinate pairs

---

## 4. break Statement

Stops the loop immediately.

Examples:

- Search operations
- Login validation
- Menu exit
- Early termination

---

## 5. continue Statement

Skips the current iteration.

Examples:

- Skip even numbers
- Ignore invalid marks
- Skip unwanted characters

---

## 6. pass Statement

Acts as a placeholder.

Examples:

- Empty blocks
- Future implementation
- Template code

---

## 7. Loop else

Executes when the loop finishes normally (without `break`).

Examples:

- Search operations
- Prime number checking
- Login validation

---

## 8. Infinite Loops

Loops that continue until explicitly stopped.

Examples:

- Game loops
- ATM menus
- Chat applications
- Monitoring systems

---

## 9. Sentinel Loops

Loops that stop when a special value (sentinel) is entered.

Examples:

- Enter `0` to stop
- Enter `quit` to exit
- Enter `-1` to finish input

---

## 10. Loop Patterns

Common ways loops are used:

- Counting
- Searching
- Filtering
- Repeating
- Simulation

---

# Skills Developed

After completing this module, you will be able to:

- Write efficient loops
- Control loop execution
- Avoid infinite loops
- Process sequences
- Search and filter data
- Build menu-driven programs
- Solve iterative programming problems
- Apply loop patterns in real-world scenarios

---

# Real-World Applications

## Banking

- ATM menu
- PIN attempts
- Transaction processing

---

## Education

- Attendance processing
- Grade calculation
- Student record search

---

## E-Commerce

- Shopping cart
- Product filtering
- Order processing

---

## Gaming

- Game loop
- Score tracking
- Turn-based actions

---

## Data Processing

- File reading
- Log analysis
- Record searching
- Data filtering

---

# How to Run

Run any Python file individually.

Example:

```bash
python 01_for_loop/01_print_numbers.py
```

---

# Learning Checklist

## for Loop

- [ ] Print numbers
- [ ] Even numbers
- [ ] Multiplication table
- [ ] Sum of numbers

## while Loop

- [ ] Print numbers
- [ ] Countdown
- [ ] Sum until limit
- [ ] Guess attempts

## Nested Loops

- [ ] Number pattern
- [ ] Star pattern
- [ ] Multiplication grid
- [ ] Coordinate pairs

## break

- [ ] Stop at number
- [ ] Search item
- [ ] Exit on password
- [ ] Break nested loop

## continue

- [ ] Skip even numbers
- [ ] Skip negatives
- [ ] Skip characters
- [ ] Skip invalid marks

## pass

- [ ] Empty if
- [ ] Empty loop
- [ ] Placeholder
- [ ] Future logic

## Loop else

- [ ] Search number
- [ ] Prime check
- [ ] Login attempt
- [ ] Search name

## Infinite Loops

- [ ] Basic infinite loop
- [ ] Break infinite loop
- [ ] Menu program
- [ ] Continuous counter

## Sentinel Loops

- [ ] Exit on zero
- [ ] Exit on quit
- [ ] Sum until negative
- [ ] Student marks input

## Loop Patterns

- [ ] Counting
- [ ] Searching
- [ ] Filtering
- [ ] Repeating
- [ ] Simulation

---

# Interview Preparation

Be prepared to answer:

- What is a loop?
- Difference between `for` and `while`
- What is `range()`?
- What is a nested loop?
- Difference between `break` and `continue`
- Purpose of `pass`
- How does loop `else` work?
- What is an infinite loop?
- What is a sentinel loop?
- Explain counting, searching, and filtering patterns.

---

# Module Summary

In this module, you learned how to use loops to automate repetitive tasks and solve iterative problems.

You explored:

- `for` loops
- `while` loops
- Nested loops
- Loop control statements
- Infinite and sentinel loops
- Common looping patterns

These concepts are essential for writing efficient programs and form the foundation for advanced topics such as functions, data structures, file handling, algorithms, and problem solving.

---

# Next Module

```
Phase 1 – Step 6

Functions
```

Topics include:

- Function basics
- Parameters
- Return values
- Variable scope
- Lambda functions
- Recursion (introduction)

---

# Author

**Mohamed Kalid**

**Python Problem Solving Journey**