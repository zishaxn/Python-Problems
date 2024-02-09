
# Create a nested list representing a matrix and write a function to compute the transpose of the matrix.



matrix = [[1, 4], [2, 5]]


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    ans = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            ans[j][i] = matrix[i][j]

    return ans


transpose_matrix = transpose(matrix)

print(transpose_matrix)
