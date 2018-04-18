testing_matrix = [[1, 3, 3], [1, 4, 3], [1, 3, 4]]
testing_matrix_two = [[1, 1, 1], [2, 3, 5], [4, 0, 5]]


def print_matrix(matrix):
    """
    :param matrix: 2D list
    :return: nice print out of the matrix
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            if j == 0:
                print("[", float(matrix[i][j]), ", ", end='', sep='')
            elif j == num_cols - 1:
                print(float(matrix[i][j]), "]", end='', sep='')
                print()
            elif j == 2:
                print(float(matrix[i][j]), " | ", end='', sep='')
            else:
                print(float(matrix[i][j]), ", ", end='', sep='')

    print("\n")


def id_border(A):
    """
    :param A: n x n square matrix (i.e a 2D list of lists)
    :return: matrix in the the form [A|I]
    """
    size = len(A)

    for i in range(size):
        identity_row = []

        for j in range(size):
            if i != j:
                identity_row.append(0)
            else:
                identity_row.append(1)

        A[i].extend(identity_row)

    return A


def combine_rows(row_a, row_b, col_index):
    pivot = row_a[col_index]
    lower_value = row_b[col_index]
    factor = lower_value / pivot * -1

    new_row_b = []
    for i in range(len(row_a)):
        value = row_a[i]
        value *= factor
        value += row_b[i]
        new_row_b.append(value)

    return new_row_b


def gauss_eliminate(B):
    """
    Assume no all zero rows for now: Applies Guassian elimination to a matrix
    :param B: matrix, 2D list
    :return:
    """
    matrix = B
    num_rows = len(matrix)
    num_cols = len(matrix[0]) // 2

    i = 0
    j = 0
    reset_j = False

    while i < num_rows:
        while j < num_cols:
            if matrix[i][j] != 0:
                # Eliminate other values in that column
                row = matrix[i]

                # This loop only works if we aren't on the last row!
                for k in range(i + 1, num_rows):
                    next_row = matrix[k]
                    matrix[k] = combine_rows(row, next_row, j)

                # Check if we are on the last row and column
                if i + 1 == num_rows and j == num_cols - 1:
                    return matrix

                if i < num_rows - 1:
                    i += 1
                reset_j = True

            if reset_j:
                j = 0
                reset_j = False
            else:
                j += 1

        if i < num_rows - 1:
            i += 1


def diag(B):
    """
    :param B: 2D matrix augmented with an identity matrix in upper triangular form
    :return: Diagonalized matrix
    """
    print("diagonal start")
    print_matrix(B)

    matrix = B
    num_rows = len(matrix)
    num_cols = len(matrix[0]) // 2

    print("num_cols", num_cols)
    for w in range(num_cols):
        print("w:", w)

    for i in range(num_rows):
        for j in range(num_cols):
            # Get main diagonal to be all 1's
            if i == j and matrix[i][j] != 1:
                value = matrix[i][j]
                row = matrix[i]
                adjusted_row = []

                for x in row:
                    x /= value
                    adjusted_row.append(x)
                matrix[i] = adjusted_row

    print()
    print("done loops")
    print_matrix(matrix)

    # eliminate values in the upper half of the matrix
    for i in range(num_rows):
        for j in range(num_cols):
            if i != j and matrix[i][j] != 0:
                row_to_adjust = matrix[i]
                # use the row that corresponds to the column value because it has a 1 in that spot
                row_to_add = matrix[j]
                # use combine rows in the opposite order since we want to cancel above not below
                combined_row = combine_rows(row_to_add, row_to_adjust, j)
                matrix[i] = combined_row
                print_matrix(matrix)


def inv(A):
    """
    :param A: n x n square matrix (i.e a 2D list of lists)
    :return: inverse or "singular"
    """
    augmented = id_border(A)
    gauss_eliminated_matrix = gauss_eliminate(augmented)
    print_matrix(gauss_eliminated_matrix)
    # diag(gauss_eliminated_matrix)


inv(testing_matrix_two)

# for i in range(num_rows):
#     for j in range(num_cols):
#         # Ignore the main diagonal
#         if i != j and matrix[i][j] != 0:
#             matrix[i] = combine_rows(matrix[i], matrix[i + 1], j)
#
#             print()
#             print("adjusted matrix for i", i, "j", j)
#             print_matrix(matrix)
#
# print()
# print("Loops over")
# print_matrix(matrix)