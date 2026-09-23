numbers = [10, 15, 20, 22, 30, 35, 40]

divisor = 5

count = 0

for number in numbers:
    if number % divisor == 0:
        count += 1

print("Count =", count)