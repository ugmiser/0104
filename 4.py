def swap_first_last_columns(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

swap_first_last_columns(A)
for row in A:
    print(row)
