"""
Topic: Guard Clauses

Problem:
Validate payment before processing.

Rules:
- Payment should be completed
- Amount should be greater than zero
"""


payment_completed = True

amount = 500


if payment_completed == False:
    print("Payment failed")

elif amount <= 0:
    print("Invalid payment amount")

else:
    print("Payment successful")