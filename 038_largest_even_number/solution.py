numbers = [1, 7, 10, 4, 3, 14, 7]

largest_even = None

for number in numbers:

    if number % 2 == 0:
        if largest_even is None or number > largest_even:
            largest_even = number

print("Largest Even Number =", largest_even)