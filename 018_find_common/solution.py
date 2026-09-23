list1 = [10, 20, 30, 40, 50]
list2 = [20, 40, 60, 80, 10]

common = []

for number in list1:
    if number in list2:
        common.append(number)

print("Common Number:", common)