"""
Topic: Logical Operators

Concept:
Check student eligibility using multiple conditions.

Conditions:
- Attendance should be above 75%
- Marks should be above 50
"""

attendance = 85

marks = 70


attendance_check = attendance >= 75

marks_check = marks >= 50


eligible = attendance_check and marks_check


print("Student Eligibility")
print("-------------------")

print("Attendance:", attendance)

print("Marks:", marks)

print("Eligible:", eligible)