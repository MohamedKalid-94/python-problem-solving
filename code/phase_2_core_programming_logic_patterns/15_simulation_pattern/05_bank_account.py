"""
Topic: Bank Account

Problem:
Simulate deposits and withdrawals.
"""

balance = 1000

transactions = [500, -200, 1000, -300]

for transaction in transactions:
    balance += transaction

print("Final Balance:", balance)