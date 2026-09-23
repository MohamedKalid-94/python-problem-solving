numbers = [10, 20, 10, 30, 20, 40, 50, 10]

seen = []
duplicates = []

for number in numbers:
    if number in seen:
        if number not in duplicates:
            duplicates.append(number)
    else:
        seen.append(number)

print("Duplicate Values =", duplicates)