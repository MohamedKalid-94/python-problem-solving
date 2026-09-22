numbers = [20,10]

if numbers[0] < numbers[1]:
    smallest = numbers[0]
    second_smallest = numbers[1]
else:
    smallest = numbers[1]
    second_smallest = numbers[0]

for number in numbers[2:]:
    if number < smallest:
        smallest = number
        second_smallest = smallest
    elif number < second_smallest:
        second_smallest = number

print("Smallest Number", smallest)
print("Second Smallest Number", second_smallest)