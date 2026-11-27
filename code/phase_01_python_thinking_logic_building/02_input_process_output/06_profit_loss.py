"""
Problem:
Calculate Profit or Loss.

Pattern:
Comparison Pattern
"""


def profit_loss(cost_price, selling_price):

    if selling_price > cost_price:
        return {
            "status": "Profit",
            "amount": selling_price - cost_price
        }

    elif selling_price < cost_price:
        return {
            "status": "Loss",
            "amount": cost_price - selling_price
        }

    return {
        "status": "No Profit No Loss",
        "amount": 0
    }


if __name__ == "__main__":
    print(profit_loss(500, 650))