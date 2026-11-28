"""
Phase 13 - Writing Clean Python
02 PEP 8 Style Guide
The BAD functions below are written badly ON PURPOSE.
The "# noqa" comment only tells the style checker to ignore them.
"""

from helpers import separator


# ---------- BAD ----------
def bad_total(price,tax): return price+tax  # noqa


def bad_is_empty(items):  # noqa
    if len(items) == 0:
        return True
    else:
        return False


def bad_check_flag(flag, value):  # noqa
    if flag == True and value == None:
        return "ready"
    return "not ready"


# ---------- CLEAN ----------
def calculate_total(price, tax):
    return price + tax


def is_empty(items):
    return not items


def check_flag(flag, value):
    if flag and value is None:
        return "ready"
    return "not ready"


def build_message(first_name, last_name, city, country):
    # A long call is split over lines (keep lines under 79 characters)
    return (
        "Hello " + first_name + " " + last_name
        + ", welcome to " + city + ", " + country
    )


def main():
    separator("Spacing and one-line functions")
    print("BAD  :", bad_total(1000, 100))
    print("CLEAN:", calculate_total(1000, 100))

    separator("Empty check")
    print("BAD  :", bad_is_empty([]), bad_is_empty([1]))
    print("CLEAN:", is_empty([]), is_empty([1]))

    separator("Comparing with True and None")
    print("BAD  :", bad_check_flag(True, None))
    print("CLEAN:", check_flag(True, None))

    separator("Long lines")
    print(build_message("Kalid", "Ahmed", "Bengaluru", "India"))


if __name__ == "__main__":
    main()