"""
Topic: Object References

Concept:
Updating one reference affects all references.
"""

bank_account = {
    "Account Holder": "Kalid",
    "Balance": 10000
}

primary_account = bank_account

primary_account["Balance"] = 15000

print("Bank Account")
print(bank_account)

print()

print("Primary Account")
print(primary_account)