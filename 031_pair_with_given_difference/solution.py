numbers = [10, 20, 30, 40, 50]
target = 20

seen = {}

for number in numbers:
    required = number - target

    if required in seen:
        print("Pair =", required, number)
        break

    seen[number] = True