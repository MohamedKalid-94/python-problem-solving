numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
	

print("Largest Number =", largest)
print("Smallest Number =", smallest)