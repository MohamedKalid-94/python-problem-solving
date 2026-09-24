numbers = [1,2,2,2,3,3,3]

is_sorted = False

for index in range(1,len(numbers)):
    if numbers[index] < numbers[index - 1]:
        is_sorted = False
        break
    else:
        is_sorted = True
        
print("Sorting Status =", is_sorted)