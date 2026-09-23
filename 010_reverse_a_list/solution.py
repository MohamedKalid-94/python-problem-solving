numbers = [10, 20, 30, 40, 50]

new_list = []

for index in range(len(numbers)-1,-1,-1):
    new_list.append(numbers[index])


print("Reversed List =", new_list)