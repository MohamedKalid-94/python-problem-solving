# Problem 17 — Separate Even and Odd Numbers

## Problem

Separate the numbers in a list into two lists: even numbers and odd numbers.

## Input

numbers = [10, 15, 22, 7, 30, 41, 56, 9]

## Output

Even Numbers = [10, 22, 30, 56]
Odd Numbers = [15, 7, 41, 9]

## Approach

* Create two empty lists.
* Loop through each number.
* Use `% 2` to check whether the number is even.
* Append the number to the appropriate list.

## Pattern

Classification + Conditional Append

## Complexity

* Time: O(n)
* Space: O(n)
