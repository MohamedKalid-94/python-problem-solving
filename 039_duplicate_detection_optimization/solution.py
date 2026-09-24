numbers = [10, 20, 30, 40, 40, 50]

duplicate_found = False


for i in range(len(numbers)):
    if duplicate_found:
        break

    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate_found = True
            break

print(duplicate_found)