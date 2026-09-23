numbers = [10, 20, 30, 20, 40, 20, 50]
target = 20

last_index = -1

for index in range(len(numbers)):
    if numbers[index] == target:
        last_index = index
        pass

print("Last Occurrence Index =", last_index)