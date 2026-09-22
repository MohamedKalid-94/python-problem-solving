numbers = [-4, -3, 0, 7, 12]

count_odd =0
count_even =0

for number in numbers:
    if number % 2 == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1
	

print("Odd Count =", count_odd)
print("Even Count =", count_even)