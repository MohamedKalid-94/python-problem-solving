"""
Topic: if elif else

Problem:
Calculate student grade based on marks.

Logic:
90-100 : Grade A
75-89  : Grade B
50-74  : Grade C
Below 50 : Fail
"""


marks = 82


if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")