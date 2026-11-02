# 004 · Is Prime

**Difficulty:** Easy · **Pattern:** Divisor loop · **Code:** [`is_prime.py`](../../phase_0_basics/is_prime.py)

## Problem
Return `True` if a number is prime, otherwise `False`.

## Examples
| Input | Output |
|---|---|
| `17` | `True` |
| `25` | `False` |
| `2` | `True` |
| `1` | `False` |

## Pseudocode
```text
if n < 2: return False
for i from 2 up to the square root of n:
    if n is divisible by i:
        return False
return True
```

## How it works
1. Numbers below 2 are not prime.
2. Try every possible divisor from 2 up to the square root of `n`.
3. If one divides `n` evenly, `n` is not prime.
4. We stop at the square root because every factor above it pairs with a smaller one we already checked.

## Edge cases
0, 1, 2 (the only even prime), and perfect squares like 25.

## Complexity
Time: O(√n) · Space: O(1)