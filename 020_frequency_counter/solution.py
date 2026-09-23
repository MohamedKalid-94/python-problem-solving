numbers = [10, 20, 10, 30, 20, 10]

frequency = {}
count=0

for number in numbers:
    if number not in frequency:
        frequency[number] = 1
    else:
        frequency[number] += 1


print("Frequency Counter:", frequency)