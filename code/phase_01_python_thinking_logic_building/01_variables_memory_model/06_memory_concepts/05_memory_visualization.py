"""
Topic: Memory Concepts

Concept:
Visualize how variables reference objects.

Using id() to see memory identity.
"""

language = "Python"

another_language = language


print("Language")
print(language)

print()

print("Another Language")
print(another_language)


print()

print("Memory Identity")

print("language id:", id(language))

print("another_language id:", id(another_language))