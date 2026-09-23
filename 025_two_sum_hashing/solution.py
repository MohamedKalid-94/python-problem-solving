numbers = [10, 20, 30, 40, 50]
target = 70

seen = {}

for number in numbers:

    complement = target - number

    if complement in seen:
        print("Pair =", complement, number)
        break

    seen[number] = True