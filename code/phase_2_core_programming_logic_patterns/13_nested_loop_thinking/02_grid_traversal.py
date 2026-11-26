"""
Topic: Grid Traversal

Problem:
Traverse a 2D grid using row and column indices.
"""

grid = [
    [1, 2],
    [3, 4]
]

for row in range(len(grid)):
    for column in range(len(grid[row])):
        print(f"({row}, {column}) = {grid[row][column]}")