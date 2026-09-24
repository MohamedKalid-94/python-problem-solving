# Problem 34 — Group Numbers by Sign

## Problem
Separate a list of numbers into three groups:
- Positive numbers
- Negative numbers
- Zero

## Input
numbers = [10, 20, -10, -5, 0, 40, 30]

## Output
Positive Numbers = [10, 20, 40, 30]
Negative Numbers = [-10, -5]
Zero Numbers = [0]

## Approach
- Create three empty lists.
- Loop through each number.
- If the number is greater than `0`, add it to `positive`.
- If the number is less than `0`, add it to `negative`.
- Otherwise, add it to `zero`.

## Pattern
Classification + Conditional Append

## Complexity
- Time: O(n)
- Space: O(n)

## Key Concept
Every number belongs to exactly one of three categories:

`number > 0` → Positive

`number < 0` → Negative

`number == 0` → Zero