numbers = [2, 1, 5, 1, 3, 2]
window_size = 3

window_sum = 0

# First window
for index in range(window_size):
    window_sum += numbers[index]
    print("Window Sum =", window_sum)

max_sum = window_sum

# Slide the window
for index in range(window_size, len(numbers)):
    window_sum = window_sum - numbers[index - window_size] + numbers[index]
    print("Window Sum =", window_sum)
    if window_sum > max_sum:
        max_sum = window_sum

print("Maximum Sum =", max_sum)