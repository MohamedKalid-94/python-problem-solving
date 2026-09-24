numbers = [3, 1, 5, 2, 8, 4]

min_so_far = numbers[0]
running_min = []

for number in numbers:
    if number < min_so_far:
        min_so_far = number

    running_min.append(min_so_far)

print("Running Minimum:", running_min)