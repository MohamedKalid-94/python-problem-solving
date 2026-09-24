numbers = [1, 2, 3, 2, 4, 5, 6, 1]

current_streak = 1
longest_streak = 1

for index in range(1, len(numbers)):
    
    if numbers[index] > numbers[index - 1]:
        current_streak += 1
    else:
        current_streak = 1

    if current_streak > longest_streak:
        longest_streak = current_streak

print("Longest Increasing Streak =", longest_streak)