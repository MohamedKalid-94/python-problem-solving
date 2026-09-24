# Problem 40 — First Repeated Number and Second Occurrence Index

## Problem

Given a list of numbers, find the first number that appears more than once and return the index of its second occurrence.

If there is no repeated number, return `None` for the repeated number and `-1` for the index.

## Input

numbers = [10, 20, 30, 20, 40, 10, 50]

## Output

First Repeated Number = 20
Second Occurrence Index = 3

## Approach

- Create an empty dictionary called `seen`.
- Traverse the list from left to right using the index.
- Get the current number using `numbers[index]`.
- Check whether the current number already exists in `seen`.
- If it exists:
  - Store the current number as `first_repeated`.
  - Store the current index as `second_occurrence_index`.
  - Stop the loop using `break`.
- If it does not exist, store the number in `seen`.
- If no duplicate is found, keep `first_repeated = None` and `second_occurrence_index = -1`.

## Pattern

Hashing + Lookup + Index Tracking + Early Exit

## Key Concept

Use a dictionary to remember numbers that have already appeared.

```text
Number already in seen?
        ↓
      YES → Duplicate found
             ↓
        Capture number
        Capture current index
        Break
      NO  → Store number