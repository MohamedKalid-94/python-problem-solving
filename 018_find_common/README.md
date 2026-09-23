# Problem 18 — Find Common Elements

## Problem

Find the elements that appear in both lists.

## Input

list1 = [10, 20, 30, 40, 50]
list2 = [20, 40, 60, 80, 10]

## Output

Common Elements = [10, 20, 40]

## Approach

* Create an empty `common` list.
* Loop through the first list.
* Check whether each number exists in the second list.
* If it exists, append it to `common`.

## Pattern

Membership Check + Conditional Append

## Complexity

* Time: O(n × m)
* Space: O(k)
