"""
Topic: Currency Conversion

Problem:
Convert USD values into INR.
"""

usd_amounts = [10, 25, 50, 100]

exchange_rate = 83.50

inr_amounts = []

for amount in usd_amounts:
    inr_amounts.append(amount * exchange_rate)

print("USD :", usd_amounts)
print("INR :", inr_amounts)