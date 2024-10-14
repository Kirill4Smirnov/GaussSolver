def check_shapes(matrix1, matrix2):
    num_cols_matrix1 = len(matrix1[0])

    num_rows_matrix2 = len(matrix2)

    return num_cols_matrix1 == num_rows_matrix2


def multiply_matrices(matrix1, matrix2):
    if not check_shapes(matrix1, matrix2):
        raise ValueError("Matrix shapes are incompatible for multiplication.")

    result_rows = len(matrix1)
    result_cols = len(matrix2[0])

    result = [[0 for _ in range(result_cols)] for _ in range(result_rows)]

    for i in range(result_rows):
        for j in range(result_cols):
            for k in range(len(matrix2)):  # Same as len(matrix1[0])
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

try:
    product = multiply_matrices(matrix1, matrix2)
    print("Matrix multiplication result:")
    for row in product:
        print(row)
except ValueError as e:
    print(e)
