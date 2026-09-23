numbers = [10, 15, 12, 20, 25, 18, 30]

count = 0

for index in range(1, len(numbers)):
    if numbers[index] > numbers[index - 1]:
        count += 1
        print(numbers[index], numbers[index - 1], "Count =", count)

print("Count =", count)