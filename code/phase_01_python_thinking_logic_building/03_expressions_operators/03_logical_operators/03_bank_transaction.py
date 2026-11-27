"""
Topic: Logical Operators

Concept:
Validate bank transaction.

Conditions:
- Account is active
- Balance is sufficient
"""

account_active = True

balance = 10000

withdraw_amount = 5000


active_check = account_active == True

balance_check = balance >= withdraw_amount


transaction_allowed = active_check and balance_check


print("Bank Transaction")
print("----------------")

print("Account Active:", account_active)

print("Available Balance:", balance)

print("Withdraw Amount:", withdraw_amount)

print("Transaction Allowed:", transaction_allowed)