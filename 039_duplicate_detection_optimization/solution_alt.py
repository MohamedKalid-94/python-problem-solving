numbers = [10, 20, 30, 40, 40, 50]

seen = {}
duplicate_found = False

for number in numbers:
    if number in seen:
        duplicate_found = True
        break

    seen[number] = True

print("Duplicate Found =", duplicate_found)