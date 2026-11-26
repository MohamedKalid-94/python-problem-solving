"""
Topic: if elif else

Problem:
Classify weather based on temperature.

Logic:

Above 35  : Hot
20-35     : Normal
Below 20  : Cold
"""


temperature = 18


if temperature > 35:
    print("Hot Weather")

elif temperature >= 20:
    print("Normal Weather")

else:
    print("Cold Weather")