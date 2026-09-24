numbers = [10, 20, 30, 20, 40, 10, 50]

seen = {}
first_repeated = None
second_occurrence_index = -1

for index in range(len(numbers)):
    number = numbers[index]
    if number in seen:
        first_repeated = number
        second_occurrence_index = index
        break

    seen[number] = True


print("First Repeated Number = ",first_repeated)
print("Second Occurrence Index = ",second_occurrence_index)