# Phase 1 - Step 6: Functions

## Overview

Functions are one of the most important building blocks in Python. A function is a reusable block of code designed to perform a specific task. Instead of writing the same code multiple times, you can write it once inside a function and call it whenever needed.

Functions make programs:

- Modular
- Reusable
- Easy to understand
- Easy to test
- Easy to maintain

This module covers everything from basic function creation to advanced topics such as variable arguments, scope, lambda functions, recursion, and common function design patterns.

---

# Learning Objectives

After completing this module, you will be able to:

- Define and call functions
- Pass data using parameters and arguments
- Return values from functions
- Use default arguments
- Use positional arguments
- Use keyword arguments
- Use variable-length arguments (`*args` and `**kwargs`)
- Understand local, global, and nonlocal scope
- Work with lambda functions
- Understand recursion
- Build reusable functions for real-world applications

---

# Prerequisites

Before starting this module, you should know:

- Variables
- Data Types
- Operators
- Decision Making
- Loops

Previous Module:

```
Phase 1 – Step 5
Loop Thinking
```

---

# Learning Flow

```
Function Basics
        ↓
Parameters
        ↓
Arguments
        ↓
Return Values
        ↓
Default Arguments
        ↓
Keyword Arguments
        ↓
Positional Arguments
        ↓
*args
        ↓
**kwargs
        ↓
Variable Scope
(Local → Global → nonlocal)
        ↓
Lambda Functions
        ↓
Recursion Basics
        ↓
Function Design Patterns
        ↓
Problem Solving
```

---

# Repository Structure

```
06_functions/

│
├── README.md
├── notes.md
├── practice.md
├── interview_questions.md
│
├── 01_function_basics/
│   ├── 01_define_function.py
│   ├── 02_call_function.py
│   ├── 03_multiple_functions.py
│   └── 04_function_with_input.py
│
├── 02_parameters_arguments/
│   ├── 01_single_parameter.py
│   ├── 02_multiple_parameters.py
│   ├── 03_function_arguments.py
│   └── 04_parameter_vs_argument.py
│
├── 03_return_values/
│   ├── 01_return_number.py
│   ├── 02_return_string.py
│   ├── 03_return_multiple_values.py
│   └── 04_return_calculation.py
│
├── 04_default_keyword_arguments/
│   ├── 01_default_argument.py
│   ├── 02_keyword_argument.py
│   ├── 03_positional_argument.py
│   └── 04_mixed_arguments.py
│
├── 05_variable_arguments/
│   ├── 01_args_example.py
│   ├── 02_kwargs_example.py
│   ├── 03_args_kwargs.py
│   └── 04_variable_arguments_practice.py
│
├── 06_scope/
│   ├── 01_local_variable.py
│   ├── 02_global_variable.py
│   ├── 03_global_keyword.py
│   └── 04_scope_practice.py
│
├── 07_nonlocal_scope/
│   ├── 01_nonlocal_keyword.py
│   ├── 02_nested_functions.py
│   ├── 03_scope_comparison.py
│   └── 04_nonlocal_practice.py
│
├── 08_lambda_functions/
│   ├── 01_basic_lambda.py
│   ├── 02_lambda_multiple_parameters.py
│   ├── 03_lambda_with_sort.py
│   └── 04_lambda_practice.py
│
├── 09_recursion_basics/
│   ├── 01_simple_recursion.py
│   ├── 02_factorial_recursion.py
│   ├── 03_countdown_recursion.py
│   └── 04_recursion_vs_loop.py
│
└── 10_function_patterns/
    ├── 01_validation_function.py
    ├── 02_calculation_function.py
    ├── 03_search_function.py
    ├── 04_conversion_function.py
    └── 05_menu_function.py
```

---

# Topics Covered

## 1. Function Basics

Learn how to:

- Define functions
- Call functions
- Create multiple functions
- Accept user input

---

## 2. Parameters & Arguments

Learn the difference between:

- Parameters
- Arguments
- Single parameter
- Multiple parameters

---

## 3. Return Values

Learn how to:

- Return numbers
- Return strings
- Return multiple values
- Return calculated results

---

## 4. Default, Keyword & Positional Arguments

Understand:

- Default arguments
- Keyword arguments
- Positional arguments
- Mixed arguments

---

## 5. Variable Arguments

Learn to work with:

- `*args`
- `**kwargs`
- Multiple positional arguments
- Multiple keyword arguments

---

## 6. Variable Scope

Understand:

- Local variables
- Global variables
- `global` keyword
- Scope rules

---

## 7. Nonlocal Scope

Learn about:

- Nested functions
- `nonlocal` keyword
- Scope comparison
- Enclosing scope

---

## 8. Lambda Functions

Learn:

- Anonymous functions
- One-line functions
- Multiple parameters
- Sorting using lambda

---

## 9. Recursion Basics

Learn:

- Recursive functions
- Base case
- Recursive case
- Factorial
- Countdown
- Recursion vs Loop

---

## 10. Function Design Patterns

Build reusable functions for:

- Validation
- Calculations
- Searching
- Data conversion
- Menu systems

---

# Skills Developed

After completing this module, you will be able to:

- Write reusable functions
- Pass and receive data correctly
- Return values efficiently
- Use different argument types
- Handle unlimited arguments
- Understand Python scope rules
- Write recursive functions
- Use lambda expressions
- Design clean and reusable code

---

# Real-World Applications

## Banking

- Deposit
- Withdraw
- Balance inquiry

---

## Education

- Grade calculation
- Attendance processing
- Student search

---

## E-Commerce

- Product search
- Discount calculation
- Price conversion

---

## Web Applications

- User authentication
- Form validation
- Menu navigation

---

## Data Processing

- Data validation
- Unit conversion
- Searching
- Filtering

---

# How to Run

Run any Python file individually.

Example:

```bash
python 01_function_basics/01_define_function.py
```

---

# Learning Checklist

## Function Basics

- [ ] Define a function
- [ ] Call a function
- [ ] Create multiple functions
- [ ] Accept user input

---

## Parameters & Arguments

- [ ] Single parameter
- [ ] Multiple parameters
- [ ] Function arguments
- [ ] Parameter vs Argument

---

## Return Values

- [ ] Return number
- [ ] Return string
- [ ] Return multiple values
- [ ] Return calculation

---

## Default & Keyword Arguments

- [ ] Default arguments
- [ ] Keyword arguments
- [ ] Positional arguments
- [ ] Mixed arguments

---

## Variable Arguments

- [ ] *args
- [ ] **kwargs
- [ ] Combined usage
- [ ] Practice

---

## Scope

- [ ] Local variables
- [ ] Global variables
- [ ] global keyword
- [ ] Scope practice

---

## Nonlocal Scope

- [ ] nonlocal keyword
- [ ] Nested functions
- [ ] Scope comparison
- [ ] Practice

---

## Lambda Functions

- [ ] Basic lambda
- [ ] Multiple parameters
- [ ] Lambda with sort
- [ ] Practice

---

## Recursion

- [ ] Simple recursion
- [ ] Factorial
- [ ] Countdown
- [ ] Recursion vs Loop

---

## Function Patterns

- [ ] Validation
- [ ] Calculation
- [ ] Searching
- [ ] Conversion
- [ ] Menu function

---

# Interview Preparation

Be prepared to answer:

- What is a function?
- Why are functions used?
- What is the difference between parameters and arguments?
- What is the difference between `print()` and `return`?
- What are default arguments?
- What are keyword arguments?
- What are positional arguments?
- What are `*args` and `**kwargs`?
- What is variable scope?
- What is the LEGB rule?
- What is the difference between `global` and `nonlocal`?
- What is a lambda function?
- What is recursion?
- What is a base case?
- When should recursion be preferred over loops?

---

# Module Summary

In this module, you learned how to create reusable blocks of code using functions. You explored different ways to pass data, return results, manage variable scope, write anonymous functions, and solve problems using recursion.

By completing this module, you now have the skills to write modular, reusable, and maintainable Python programs.

---

# Next Module

```
Phase 1 – Step 7

Exception Handling
```

Topics include:

- Exceptions
- try
- except
- else
- finally
- raise
- Custom exceptions
- File exception handling

---

# Author

**Mohamed Kalid**

**Python Problem Solving Journey**