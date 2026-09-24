numbers = [1, 5, 7, -1, 5]
target = 6

seen = {}
pair_count = 0

for number in numbers:
    complement = target - number

    if complement in seen:
        pair_count += 1

    seen[number] = True

print("Pair Count =", pair_count)