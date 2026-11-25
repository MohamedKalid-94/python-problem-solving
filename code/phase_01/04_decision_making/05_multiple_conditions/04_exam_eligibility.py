"""
Topic: Multiple Conditions

Problem:
Check exam eligibility.

Conditions:

Attendance >= 75
AND
Fees Paid
"""


attendance = 85

fees_paid = True


if attendance >= 75 and fees_paid:

    print("Allowed for Exam")

else:

    print("Not Allowed for Exam")