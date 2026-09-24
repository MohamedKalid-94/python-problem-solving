text = "python"

vowel_count = 0
consonant_count = 0

for character in text:
    if character in "aeiou":
        vowel_count += 1
    else:
        consonant_count += 1

print("Vowel Count:", vowel_count)
print("Consonant Count:", consonant_count)