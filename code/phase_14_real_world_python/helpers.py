"""
Phase 14 - Real World Python
Shared input helpers used by the projects.

Each helper keeps asking until the user types a valid value,
so the program never crashes on bad input.
"""

import math


def ask_text(prompt):
    """Keep asking until the user types something (not empty)."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please type something.")


def ask_number(prompt, minimum=None, maximum=None):
    """Keep asking until the user types a valid number in the allowed range."""
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if not math.isfinite(number):          # rejects nan and inf
            print("Please enter a valid number.")
            continue
        if minimum is not None and number < minimum:
            print("Number must be at least", minimum)
            continue
        if maximum is not None and number > maximum:
            print("Number must be at most", maximum)
            continue
        return number


def ask_int(prompt, minimum=None, maximum=None):
    """Keep asking until the user types a valid whole number in the allowed range."""
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if minimum is not None and number < minimum:
            print("Number must be at least", minimum)
            continue
        if maximum is not None and number > maximum:
            print("Number must be at most", maximum)
            continue
        return number