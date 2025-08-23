def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    res = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[j][i] = matrix[i][j]
    return res
mat = [[1, 2, 3], [4, 5, 6]]
print(transpose(mat)) 
