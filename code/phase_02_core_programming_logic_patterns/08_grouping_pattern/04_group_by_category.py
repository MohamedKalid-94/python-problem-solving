"""
Topic: Group by Category

Problem:
Group books by category.
"""

books = [
    ("Python Basics", "Programming"),
    ("AI Guide", "Programming"),
    ("History Book", "Education"),
    ("Physics", "Science")
]

grouped_books = {}

for book, category in books:
    grouped_books.setdefault(category, []).append(book)

print(grouped_books)