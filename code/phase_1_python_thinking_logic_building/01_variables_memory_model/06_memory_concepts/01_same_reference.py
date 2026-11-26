"""
Topic: Memory Concepts

Concept:
Two variables can refer to the same object in memory.

Real-World Example:
Two names referring to the same document.
"""

student_marks = [80, 90, 95]

marks_copy = student_marks


print("Student Marks")
print(student_marks)

print()

print("Marks Copy")
print(marks_copy)


marks_copy.append(100)


print()

print("After Modification")

print("Student Marks")
print(student_marks)

print("Marks Copy")
print(marks_copy)