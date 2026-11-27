"""
Topic: Nested if

Problem:
Bank withdrawal validation.

Conditions:

1. Account should be active
2. Balance should be sufficient
3. Withdrawal should be allowed
"""


account_active = True

balance = 10000

withdraw_amount = 5000


if account_active:

    if balance >= withdraw_amount:
        print("Withdrawal Successful")

    else:
        print("Insufficient Balance")

else:
    print("Account is inactive")