numbers = [2, 4, 1, 5, 3]

count = 0
prefix_sum = []

for number in numbers:
    count += number
    prefix_sum.append(count)

print("Prefix Sum:",prefix_sum)
