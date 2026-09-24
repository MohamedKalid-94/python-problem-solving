numbers = [3, 1, 5, 2, 8, 4]

max_so_far = numbers[0]
running_max = []

for number in numbers:
    if number > max_so_far:
        max_so_far = number

    running_max.append(max_so_far)

print("Running Maximum:", running_max)