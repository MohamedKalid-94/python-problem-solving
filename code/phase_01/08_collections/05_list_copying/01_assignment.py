"""
Topic: Assignment Copy

Problem:
Observe reference behavior.
"""

list1 = [10, 20, 30]

list2 = list1

list2.append(40)

print("List1:", list1)
print("List2:", list2)