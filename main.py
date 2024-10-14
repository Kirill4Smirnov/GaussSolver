def is_row_echelon_form(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    prev_leading_col = -1

    for row in range(rows):
        leading_col_found = False
        for col in range(cols):
            if matrix[row][col] != 0:
                if col <= prev_leading_col:
                    return False
                prev_leading_col = col
                leading_col_found = True
                break
        if not leading_col_found and any(matrix[row][col] != 0 for col in range(cols)):
            return False
    return True


def is_reduced_row_echelon_form(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    prev_leading_col = -1

    for row in range(rows):
        leading_col_found = False
        for col in range(cols):
            if matrix[row][col] != 0:
                if col <= prev_leading_col or matrix[row][col] != 1:
                    return False
                for r in range(row):
                    if matrix[r][col] != 0:
                        return False
                prev_leading_col = col
                leading_col_found = True
                break
    return True


def find_nonzero_row(matrix, pivot_row, col):
    for row in range(pivot_row, len(matrix)):
        if matrix[row][col] != 0:
            return row
    return None


def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def make_pivot_one(matrix, pivot_row, col):
    pivot_element = matrix[pivot_row][col]
    if pivot_element != 0:
        matrix[pivot_row] = [element /
                             pivot_element for element in matrix[pivot_row]]


def eliminate_below(matrix, pivot_row, col):
    pivot_element = matrix[pivot_row][col]
    for row in range(pivot_row + 1, len(matrix)):
        factor = matrix[row][col]
        matrix[row] = [matrix[row][i] - factor * matrix[pivot_row][i]
                       for i in range(len(matrix[row]))]


def eliminate_above(matrix, pivot_row, col):
    for row in range(pivot_row - 1, -1, -1):
        factor = matrix[row][col]
        matrix[row] = [matrix[row][i] - factor * matrix[pivot_row][i]
                       for i in range(len(matrix[row]))]


def reduced_row_echelon_form(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    pivot_row = 0

    for col in range(ncols):
        nonzero_row = find_nonzero_row(matrix, pivot_row, col)
        if nonzero_row is not None:
            swap_rows(matrix, pivot_row, nonzero_row)
            make_pivot_one(matrix, pivot_row, col)
            eliminate_below(matrix, pivot_row, col)
            eliminate_above(matrix, pivot_row, col)
            pivot_row += 1
    return matrix


def row_echelon_form(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    pivot_row = 0

    for col in range(ncols):
        nonzero_row = find_nonzero_row(matrix, pivot_row, col)
        if nonzero_row is not None:
            swap_rows(matrix, pivot_row, nonzero_row)
            make_pivot_one(matrix, pivot_row, col)
            eliminate_below(matrix, pivot_row, col)
            pivot_row += 1
    return matrix


matrix = [
    [24, -23, 6, -64, 6],
    [-9, 9, -2, 25, -2],
    [6, -6, 2, -16, 2],
    [-4, 4, -1, 11, -1]
]

print("Matrix Before Converting:")
for row in matrix:
    print(row)

result = row_echelon_form(matrix)

print("\nAfter Converting to Row Echelon Form:")
for row in result:
    print(row)

result_rref = reduced_row_echelon_form(result)

print("\nAfter Converting to Reduced Row Echelon Form:")
for row in result_rref:
    print(row)

if is_reduced_row_echelon_form(result_rref):
    print("In RREF")
else:
    print("Not in RREF")
