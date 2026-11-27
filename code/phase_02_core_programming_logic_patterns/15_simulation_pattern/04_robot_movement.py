"""
Topic: Robot Movement

Problem:
Track robot movement on a one-dimensional line.
"""

position = 0

commands = ["RIGHT", "RIGHT", "LEFT", "RIGHT"]

for command in commands:

    if command == "RIGHT":
        position += 1

    elif command == "LEFT":
        position -= 1

print("Final Position:", position)