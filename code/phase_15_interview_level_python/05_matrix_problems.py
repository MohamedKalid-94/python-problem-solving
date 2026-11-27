# Phase 15 - Interview-Level Python
# 05 Matrix Problems

def matrix_add(a,b): return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def transpose(matrix): return list(map(list,zip(*matrix)))

def diagonal_sum(matrix): return sum(matrix[i][i] for i in range(len(matrix)))

def search_matrix(matrix,target):
    for row in matrix:
        if target in row: return True
    return False

def main():
    matrix=[[1,2],[3,4]]

    print("Add:",matrix_add(matrix,matrix))
    print("Transpose:",transpose(matrix))
    print("Diagonal:",diagonal_sum(matrix))
    print("Search:",search_matrix(matrix,3))

if __name__=="__main__": main()