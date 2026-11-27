"""
Problem:
Convert INR to USD.

Pattern:
Transformation Pattern
"""


def inr_to_usd(amount_inr, exchange_rate):
    return round(amount_inr / exchange_rate, 2)


if __name__ == "__main__":
    print(inr_to_usd(8500, 85))