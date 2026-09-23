text = "kalid"
is_palindrome = True

for index in range(len(text)):
    if text[index] != text[len(text) - 1 - index]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")