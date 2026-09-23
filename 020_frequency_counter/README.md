# Problem 20 — Frequency Counter

## Problem

Count how many times each number appears in a list using a dictionary.

## Input

numbers = [10, 20, 10, 30, 20, 10]

## Output

Frequency Counter = {10: 3, 20: 2, 30: 1}

## Approach

* Create an empty dictionary called `frequency`.
* Loop through each number.
* If the number is not already in the dictionary, initialize its count to `1`.
* If it already exists, increment its count using `+= 1`.

## Pattern

Dictionary Frequency Counting

## Complexity

* Time: O(n)
* Space: O(k)

Where `k` is the number of unique values.
