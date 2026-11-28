"""
Phase 13 - Writing Clean Python
04 Type Hints
Hints document what a function expects and returns.
Python does NOT enforce them. Tools like mypy and pyright check them.
(This file needs Python 3.10 or newer for the "int | None" syntax.)
"""

from helpers import separator


# ---------- BAD ----------
def bad_add(a, b):
    return a + b                 # numbers? strings? lists? nobody knows


# ---------- CLEAN ----------
def add_numbers(a: int, b: int) -> int:
    return a + b


def get_user_name() -> str:
    return "Kalid"


def get_scores() -> list[int]:
    return [90, 80, 70]


def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


def find_age(ages: dict[str, int], name: str) -> int | None:
    """Return the age, or None if the name is not in the dictionary."""
    return ages.get(name)


def main():
    separator("BAD vs CLEAN")
    print("BAD  :", bad_add(10, 20))
    print("CLEAN:", add_numbers(10, 20))

    separator("Hints are information, not rules")
    wrong = add_numbers("a", "b")        # it runs! mypy would warn here
    print("add_numbers('a', 'b') ->", wrong)
    print("The hints are stored here:", add_numbers.__annotations__)

    separator("More type hints")
    print(get_user_name(), get_scores(), average(get_scores()))
    ages = {"Kalid": 28, "Asha": 25}
    print("find_age('Kalid'):", find_age(ages, "Kalid"))
    print("find_age('Zed')  :", find_age(ages, "Zed"))


if __name__ == "__main__":
    main()