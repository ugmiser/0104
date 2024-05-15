def sort_columns_by_kth_row(matrix, k):
    n = len(matrix[0])
    sorted_indices = sorted(range(n), key=lambda x: matrix[k-1][x])
    sorted_columns = [[matrix[row][i] for i in sorted_indices] for row in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(n):
            matrix[i][j] = sorted_columns[i][j]

# Пример использования
G = [[3, 2, 1],
     [6, 5, 4],
     [9, 8, 7]]

sort_columns_by_kth_row(G, 2)
for row in G:
    print(row)
