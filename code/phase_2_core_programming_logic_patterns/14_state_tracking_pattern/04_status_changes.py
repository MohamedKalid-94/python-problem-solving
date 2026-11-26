"""
Topic: Status Changes

Problem:
Count how many times a traffic signal changes.
"""

signals = ["Red", "Red", "Green", "Green", "Yellow", "Red"]

changes = 0

previous = signals[0]

for signal in signals[1:]:

    if signal != previous:
        changes += 1

    previous = signal

print("Status Changes:", changes)