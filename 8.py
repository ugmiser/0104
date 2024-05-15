def transform_matrix(matrix):
    for row in matrix:
        min_value = min(row)
        min_index = row.index(min_value)
        if min_value % 2 == 0:
            row[min_index] = 0
        else:
            row[min_index] = 1

F = [[4, 2, 3],
     [1, 5, 6],
     [7, 8, 9]]

transform_matrix(F)
for row in F:
    print(row)
