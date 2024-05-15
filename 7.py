def find_rows_with_extreme_sums(matrix):
    min_sum = float('inf')
    max_sum = float('-inf')
    min_row = None
    max_row = None

    for i, row in enumerate(matrix):
        row_sum = sum(row)
        if row_sum < min_sum:
            min_sum = row_sum
            min_row = i
        if row_sum > max_sum:
            max_sum = row_sum
            max_row = i

    return min_row, min_sum, max_row, max_sum


E = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

min_row, min_sum, max_row, max_sum = find_rows_with_extreme_sums(E)
print("Строка с минимальной суммой:", E[min_row])
