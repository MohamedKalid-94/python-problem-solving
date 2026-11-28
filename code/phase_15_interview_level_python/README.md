# Phase 15 - Interview-Level Python

## Overview

This phase collects the problems that come up again and again in Python interviews: strings, lists, dictionaries, sets, matrices, searching, sorting, recursion, file handling, OOP and the core coding patterns.

Each file contains small functions with a `main()` that prints example results. Every function handles its edge cases (empty input, bad values) and has comments that explain the idea.

## What You Will Learn

- Solve common string, list, dictionary and set problems
- Use `dict.fromkeys`, `Counter`-style counting and sets correctly
- Work with 2D lists (matrices)
- Write linear search, binary search, bubble sort and selection sort
- Understand recursion, base cases and memoization (`lru_cache`)
- Read and write files safely with `with open(...)`
- Build small classes with validation
- Recognize the accumulator, counter, frequency, two-pointer and sliding-window patterns
- State the time complexity of your solution

## Folder Structure

```
phase_15_interview_level_python/
├── 01_string_problems.py
├── 02_list_problems.py
├── 03_dictionary_problems.py
├── 04_set_problems.py
├── 05_matrix_problems.py
├── 06_searching_algorithms.py
├── 07_sorting_algorithms.py
├── 08_recursion_problems.py
├── 09_file_handling_problems.py
├── 10_oop_interview_problems.py
├── 11_coding_patterns.py
├── README.md
├── notes.md
├── practice.md
└── interview_qanda.md
```

## Files

| File | Functions | Key Idea |
|---|---|---|
| 01_string_problems.py | reverse, palindrome, frequency, remove duplicates, anagram, vowels, first non-repeating | Slicing, cleaning strings, counting with a dict |
| 02_list_problems.py | max, min, remove duplicates, reverse, rotate, move zeros, two sum | Order-preserving dedupe, `%` for rotation, hash map |
| 03_dictionary_problems.py | frequency, word count, merge, find duplicates | Counting with `get`, merging with `{**a, **b}` |
| 04_set_problems.py | unique, intersection, union, difference, subset | Set operators `& | - issubset` |
| 05_matrix_problems.py | add, transpose, diagonal sum, search | Nested lists, `zip(*matrix)`, shape check |
| 06_searching_algorithms.py | linear search, binary search | O(n) vs O(log n), sorted input required |
| 07_sorting_algorithms.py | bubble sort, selection sort | Nested loops, swapping, early exit |
| 08_recursion_problems.py | factorial, fibonacci, sum | Base case, recursive case, `lru_cache` |
| 09_file_handling_problems.py | write, read, count words | `with open`, modes, `encoding` |
| 10_oop_interview_problems.py | BankAccount, Employee | Classes, validation, `raise` |
| 11_coding_patterns.py | accumulator, counter, frequency, two pointer, sliding window | The patterns behind most problems |

## Sample Outputs

```
01: Remove Duplicates: progamin
02: Rotate (k > length): [3, 1, 2]
05: Transpose: [[1, 3], [2, 4]]
06: Binary (not found): -1
07: Bubble: [1, 2, 5, 8]
08: Fibonacci(40): 102334155
10: Error: insufficient balance
11: Sliding Window: 12
```

## How to Run

From the repository root:

```
python code/phase_15_interview_level_python/01_string_problems.py
```

Or `cd` into the folder and run `python 01_string_problems.py`.

Note: `09_file_handling_problems.py` creates `sample.txt` in the folder where you run it. Add `sample.txt` to `.gitignore`.

## How to Study This Phase

1. Read the problem, then **try it yourself for 10-15 minutes** before reading the solution.
2. Say the brute-force answer and its complexity out loud.
3. Read the solution and find the one idea that makes it better.
4. Re-write it from memory the next day.
5. Test with edge cases: empty input, one item, duplicates, negatives.

## Skills After This Phase

- Solve common interview problems in Python
- Explain the time complexity of your solution
- Choose between a list, dict and set for the job
- Write recursive functions with correct base cases
- Handle edge cases and bad input