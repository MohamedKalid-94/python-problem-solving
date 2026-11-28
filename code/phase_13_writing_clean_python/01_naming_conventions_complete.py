"""
Phase 13 - Writing Clean Python
01 Naming Conventions
Bad names and clean names, side by side.
"""

from helpers import separator

MAX_RETRY_COUNT = 3          # constants: UPPER_CASE, at the top of the module


# ---------- BAD ----------
def bad_calc(a, b, c):
    x = a * b
    return x + c             # what are a, b and c? what is x?


def bad_shadowing():
    max = 10                 # hides the built-in max() function
    return max([1, 5, 3])    # TypeError: 'int' object is not callable


# ---------- CLEAN ----------
def calculate_total_price(price, quantity, tax):
    subtotal = price * quantity
    return subtotal + tax


def highest_score(scores):
    highest = max(scores)    # a different name, so max() still works
    return highest


class BankAccount:
    """A small class to show the underscore conventions."""

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name    # public
        self._balance = balance         # _single: internal, do not touch
        self.__pin = "1234"             # __double: name mangling

    def is_rich(self):
        return self._balance > 100000


def main():
    separator("Function and variable names")
    print("BAD  :", bad_calc(100, 5, 50))
    print("CLEAN:", calculate_total_price(100, 5, 50))

    separator("Never reuse a built-in name")
    try:
        bad_shadowing()
    except TypeError as error:
        print("BAD  : TypeError ->", error)
    print("CLEAN:", highest_score([1, 5, 3]))

    separator("Underscore conventions in a class")
    account = BankAccount("Kalid", 5000)
    print("Public name        :", account.owner_name)
    print("_balance (works)   :", account._balance)
    print("Has attribute __pin:", hasattr(account, "__pin"))
    print("Mangled name       :", account._BankAccount__pin)

    separator("Constants and boolean names")
    is_active = True
    has_discount = False
    print("is_active:", is_active, "| has_discount:", has_discount)
    print("is_rich() :", account.is_rich())
    for attempt in range(1, MAX_RETRY_COUNT + 1):
        print("Attempt", attempt, "of", MAX_RETRY_COUNT)


if __name__ == "__main__":
    main()