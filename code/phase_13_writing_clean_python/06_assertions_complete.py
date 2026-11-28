"""
Phase 13 - Writing Clean Python
06 Assertions
assert checks a mistake in YOUR code. It is not for checking user input.
Try it:  python -O 06_assertions_complete.py   (assertions are switched off)
"""

from helpers import separator


# ---------- BAD ----------
def bad_divide(a, b):
    assert b != 0, "Cannot divide by zero"    # input check with assert: unsafe
    return a / b


# ---------- CLEAN ----------
def divide(a, b):
    if b == 0:                                  # input checks use raise
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_percentage(score, total):
    if total <= 0:
        raise ValueError("total must be greater than 0")
    percentage = score / total * 100
    # assert: a "this must never happen" check on our own logic
    assert 0 <= percentage <= 100, "percentage out of range, bug in the code"
    return percentage


def main():
    separator("Are assertions switched on?")
    print("__debug__ is", __debug__, "(False when run with python -O)")

    separator("BAD vs CLEAN: checking input")
    try:
        bad_divide(10, 0)
    except AssertionError as error:
        print("BAD   : AssertionError ->", error)
    except ZeroDivisionError as error:
        print("BAD   : with -O the assert vanished ->", error)

    try:
        divide(10, 0)
    except ValueError as error:
        print("CLEAN : ValueError ->", error)

    separator("A good use of assert")
    print("calculate_percentage(45, 50) ->", calculate_percentage(45, 50))
    try:
        calculate_percentage(80, 50)            # score bigger than total
    except AssertionError as error:
        print("assert caught a bug ->", error)


if __name__ == "__main__":
    main()