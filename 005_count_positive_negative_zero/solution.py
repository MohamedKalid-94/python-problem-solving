numbers = [-10, -1, 0, 0, 0, 5, 20]

count_positive =0
count_negative =0
count_zero =0

for number in numbers:
    if number > 0:
        count_positive = count_positive + 1
    elif number < 0:
        count_negative = count_negative + 1
    else:
        count_zero = count_zero + 1

print("Positive Numbers =", count_positive)
print("Negative Numbers =", count_negative)
print("Zeros =", count_zero)