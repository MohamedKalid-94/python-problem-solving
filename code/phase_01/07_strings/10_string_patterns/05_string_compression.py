"""
Topic: String Compression

Problem:
Compress repeated characters.

Example:
aaabbcccc

Output:
a3b2c4
"""

text = input("Enter text: ")

result = ""

count = 1

for index in range(1, len(text)):

    if text[index] == text[index - 1]:
        count += 1

    else:
        result += text[index - 1] + str(count)
        count = 1

result += text[-1] + str(count)

print(result)