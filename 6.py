def move_max_to_top_left(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_val = float('-inf')
    max_i, max_j = 0, 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_i, max_j = i, j

    matrix[0], matrix[max_i] = matrix[max_i], matrix[0]


    for i in range(n):
        matrix[i][0], matrix[i][max_j] = matrix[i][max_j], matrix[i][0]


D = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

move_max_to_top_left(D)
for row in D:
    print(row)
