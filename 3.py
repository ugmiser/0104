def swap_min_max_in_each_row(matrix):
    for row in matrix:
        min_val = min(row)
        max_val = max(row)
        min_index = row.index(min_val)
        max_index = row.index(max_val)
        row[0], row[min_index] = row[min_index], row[0]
        row[-1], row[max_index] = row[max_index], row[-1]


B = [[3, 5, 1],
     [9, 2, 7],
     [4, 8, 6]]

swap_min_max_in_each_row(B)
print(B)
