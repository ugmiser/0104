def sum_and_positive_elements_above_diagonal(matrix):
    n = len(matrix)
    total_sum = 0
    positive_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                total_sum += matrix[i][j]
                positive_count += 1

    return total_sum, positive_count

A = [[3, 5, 1],
     [9, 2, 7],
     [4, 8, 6]]

sum_result, positive_count_result = sum_and_positive_elements_above_diagonal(A)
print("Сумма элементов:", sum_result)
print("Количество положительных элементов:", positive_count_result)