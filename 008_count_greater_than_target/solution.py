numbers = [12, 45, 7, 89, 23, 56]

target = 30
count = 0

for number in numbers:
    if number > target:
        count += 1
    
print("Numbers greater than target =", count)