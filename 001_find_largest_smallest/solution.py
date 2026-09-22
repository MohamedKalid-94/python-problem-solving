numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for number in numbers:
    if largest < number:
        largest = number

print("Largest Number", largest)