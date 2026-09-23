numbers = [10, 20, 10, 5, 20, 40, 30]

frequency = {}

# Phase 1
for number in numbers:
    if number not in frequency:
        frequency[number] = 1
    else:
        frequency[number] += 1

# Phase 2
first_non_repeating = None

for number in numbers:
    if frequency[number] == 1:
        first_non_repeating = number
        break

print("First Non-Repeating Number =", first_non_repeating)