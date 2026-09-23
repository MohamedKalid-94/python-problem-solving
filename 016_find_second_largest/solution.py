numbers = [50, 50, 40, 30, 20]

largest = numbers[0]
second_largest = None


for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number

    elif second_largest is None and number != largest:
        second_largest = number

    elif number > second_largest and number != largest:
        second_largest = number

print("Largest Number", largest)
print("Second Largest Number", second_largest)