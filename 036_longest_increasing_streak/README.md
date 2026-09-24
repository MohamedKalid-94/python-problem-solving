# Problem 36 — Longest Increasing Streak

## Problem
Find the length of the longest consecutive increasing streak in a list of numbers.

A streak continues when each number is greater than the number immediately before it.

## Input
numbers = [1, 2, 3, 2, 4, 5, 6, 1]

## Output
Longest Increasing Streak = 4

## Approach
- Start `current_streak` at `1` because the first number itself forms a streak of length `1`.
- Start `longest_streak` at `1`.
- Loop from index `1` because each number must be compared with its previous number.
- If the current number is greater than the previous number, increase `current_streak`.
- Otherwise, reset `current_streak` to `1`.
- Compare `current_streak` with `longest_streak`.
- Update `longest_streak` when a longer streak is found.

## Pattern
Running State + Previous Element Comparison + Best-So-Far

## Key Concept
Two states are maintained:

`current_streak` → length of the current increasing sequence

`longest_streak` → longest sequence found so far

## Complexity
- Time: O(n)
- Space: O(1)