"""
Phase 15 - Interview-Level Python
05 Matrix Problems
"""


def matrix_add(a, b):
    # Both matrices must have the same number of rows and columns
    if len(a) != len(b) or any(len(ra) != len(rb) for ra, rb in zip(a, b)):
        raise ValueError("matrices must have the same shape")

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


def transpose(matrix):
    # zip(*matrix) pairs up the columns; each column becomes a row
    return list(map(list, zip(*matrix)))


def diagonal_sum(matrix):
    # Works for a square matrix (same number of rows and columns)
    return sum(matrix[i][i] for i in range(len(matrix)))


def search_matrix(matrix, target):
    for row in matrix:
        if target in row:
            return True
    return False


def main():
    matrix = [[1, 2], [3, 4]]

    print("Add:", matrix_add(matrix, matrix))
    print("Transpose:", transpose(matrix))
    print("Diagonal:", diagonal_sum(matrix))
    print("Search:", search_matrix(matrix, 3))


if __name__ == "__main__":
    main()