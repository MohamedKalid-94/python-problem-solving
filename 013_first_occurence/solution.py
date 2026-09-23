numbers = [10, 20, 10, 30, 10, 40, 20]

target = 20

first_index = -1

for index in range(len(numbers)):
    if numbers[index] == target:
        first_index = index
        break

print("First Occurrence Index =", first_index)