numbers = [12, 45, 7, 89, 23, 56]
target = 23

found = False

for number in numbers:
    if number == target:
        found = True

if found:
    print("Found")
else:
    print("Not Found")