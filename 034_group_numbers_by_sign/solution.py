numbers = [10, 20, -10, -5, 0, 40, 30]

positive = []
negative = []
zero = []

for number in numbers:
    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
    else:
        zero.append(number)


print("Postive Numbers",positive)
print("Negative Numbers",negative)
print("Zero Numbers",zero)