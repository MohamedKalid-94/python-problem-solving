numbers = [10, 15, 22, 7, 30, 41, 56, 9]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even Numbers =", even_numbers)
print("Odd Numbers =", odd_numbers)