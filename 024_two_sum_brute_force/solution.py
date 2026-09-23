numbers = [10, 20, 30, 40, 50]
target = 70

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Pair =", numbers[i], numbers[j])