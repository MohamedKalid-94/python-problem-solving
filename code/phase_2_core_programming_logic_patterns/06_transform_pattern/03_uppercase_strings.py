"""
Topic: Uppercase Strings

Problem:
Convert every string into uppercase.
"""

languages = ["python", "java", "c++", "javascript"]

uppercase = []

for language in languages:
    uppercase.append(language.upper())

print("Original :", languages)
print("Uppercase:", uppercase)