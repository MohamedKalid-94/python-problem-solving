"""
Topic: ATM Simulation

Problem:
Simulate a withdrawal.
"""

balance = 5000

withdraw = 1200

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal Successful")

else:
    print("Insufficient Balance")

print("Balance:", balance)