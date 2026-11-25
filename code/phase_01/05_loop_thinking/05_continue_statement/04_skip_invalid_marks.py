"""
Topic: continue Statement

Problem:
Skip invalid marks.
"""

marks = [85, -10, 90, 110, 75]

for mark in marks:

    if mark < 0 or mark > 100:
        continue

    print(mark)