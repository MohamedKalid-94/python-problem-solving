"""
Phase 13 - Writing Clean Python
08 Refactoring
Refactoring = improve the code WITHOUT changing what it does.
Always compare the old and new versions to prove the behavior is the same.
"""

from helpers import separator

# ---------- CLEAN: names for the "magic numbers" ----------
BASE_WEIGHT_KG = 5
MEMBER_DISCOUNT = 0.10
RATES = {
    "IN": {"base": 50, "per_kg": 10},
    "OTHER": {"base": 200, "per_kg": 40},
}


# ---------- BAD: nested ifs, magic numbers, repeated code ----------
def bad_shipping_cost(weight, country, is_member):
    if weight > 0:
        if country == "IN":
            if weight <= 5:
                cost = 50
            else:
                cost = 50 + (weight - 5) * 10
            if is_member == True:  # noqa
                cost = cost - cost * 0.1
            return cost
        else:
            if weight <= 5:
                cost = 200
            else:
                cost = 200 + (weight - 5) * 40
            if is_member == True:  # noqa
                cost = cost - cost * 0.1
            return cost
    else:
        return None


# ---------- CLEAN ----------
def calculate_shipping_cost(weight_kg, country, is_member):
    if weight_kg <= 0:               # guard clause: handle the bad case first
        return None

    rate = RATES["IN"] if country == "IN" else RATES["OTHER"]
    extra_kg = max(weight_kg - BASE_WEIGHT_KG, 0)
    cost = rate["base"] + extra_kg * rate["per_kg"]

    if is_member:
        cost -= cost * MEMBER_DISCOUNT
    return cost


def main():
    separator("Same answers from old and new code")
    print("BAD  :", bad_shipping_cost(8, "IN", True))
    print("CLEAN:", calculate_shipping_cost(8, "IN", True))

    separator("Prove the behavior did not change")
    test_cases = [
        (0, "IN", False), (-3, "US", True), (3, "IN", False),
        (5, "IN", True), (8, "IN", True), (7.5, "US", False),
        (12, "US", True), (1, "UK", False),
    ]
    matches = 0
    for weight, country, is_member in test_cases:
        old = bad_shipping_cost(weight, country, is_member)
        new = calculate_shipping_cost(weight, country, is_member)
        if old == new:
            matches += 1
        else:
            print("DIFFERENT for", weight, country, is_member, "->", old, new)
    print(matches, "of", len(test_cases), "cases give the same result")

    separator("Change a rule in one place")
    print("Members now get 20% off -> edit only MEMBER_DISCOUNT")


if __name__ == "__main__":
    main()