numbers = [10, 20, 10, 5, 20, 40, 30]

seen = {}
first_repeating = None

for number in numbers:
    if number in seen:
        first_repeating = number
        break

    seen[number] = True

print("First Repeating Number =", first_repeating)