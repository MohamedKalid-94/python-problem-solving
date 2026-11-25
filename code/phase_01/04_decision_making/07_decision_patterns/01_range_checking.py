"""
Topic: Decision Pattern - Range Checking

Problem:
Classify marks based on ranges.

Pattern:

Range 1
Range 2
Range 3
Default
"""


marks = 78


if marks >= 90:
    print("Excellent")

elif marks >= 75:
    print("Very Good")

elif marks >= 50:
    print("Average")

else:
    print("Needs Improvement")