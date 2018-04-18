import copy

testing_matrix = [[1, 3, 3], [1, 4, 3], [1, 3, 4]]
testing_matrix_two = [[1, 1, 1], [2, 3, 5], [4, 0, 5]]
no_inverse = [[1, 6, 4], [2, 4, -1], [-1, 2, 5]]
no_inverse_two = [[3, 4], [6, 8]]


def print_matrix(matrix, augmented=True):
    """
    :param matrix: 2D list
    :param augmented: bool whether the matrix is augmented with the identity matrix
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
            elif j == (num_cols // 2) - 1 and augmented:
                print(float(matrix[i][j]), " | ", end='', sep='')
            else:
                print(float(matrix[i][j]), ", ", end='', sep='')

    print("\n")


def id_border(A):
    """
    :param A: n x n square matrix (i.e a 2D list of lists)
    :return: matrix in the the form [A|I]
    """
    new_list = copy.deepcopy(A)
    size = len(new_list)

    for i in range(size):
        identity_row = []

        for j in range(size):
            if i != j:
                identity_row.append(0)
            else:
                identity_row.append(1)

        new_list[i].extend(identity_row)

    return new_list


def get_identity_matrix(n):
    """
    :param n: int size for nxn identity matrix
    :return: 2D list where the main diagonal is all 1's
    """
    identity_matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            if i != j:
                row.append(0)
            else:
                row.append(1)
        identity_matrix.append(row)

    # print_matrix(identity_matrix, False)
    return identity_matrix


def get_zero_matrix(rows, columns):
    """
    :param rows: int number of rows in zero matrix
    :param columns: int number of columns in zero matrix
    :return: n x n 2D list of zeros
    """
    zero_matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        zero_matrix.append(row)

    return zero_matrix


def multiply_matrices(A, B):
    """
    :param A: 2D list
    :param B: 2D list
    :return: 2D list
    """
    if len(A[0]) != len(B):
        return "Cannot multiply matrices"

    result = get_zero_matrix(len(A), len(B[0]))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Used by gauss_eliminate
def combine_rows(row_a, row_b, col_index):
    pivot = row_a[col_index]
    lower_value = row_b[col_index]
    factor = lower_value / pivot * -1

    new_row_b = []
    for i in range(len(row_a)):
        value = row_a[i]
        value *= factor
        value += row_b[i]
        if value < 0.0000000001:
            # print("round off error")
            value = 0.0
        new_row_b.append(value)

    return new_row_b


def gauss_eliminate(B):
    """
    Assume no all zero rows for now: Applies Gaussian elimination to a matrix
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
                    print()
                    print_matrix(matrix)

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
        else:
            return matrix


def diag(B):
    """
    :param B: 2D matrix augmented with an identity matrix in upper triangular form
    :return: Diagonalized matrix
    """
    matrix = B
    num_rows = len(matrix)
    num_cols = len(matrix[0]) // 2

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

    return matrix


def inv(A):
    """
    :param A: n x n square matrix (i.e a 2D list of lists)
    :return: inverse or "singular"
    """
    list_copy = copy.deepcopy(A)
    augmented = id_border(list_copy)
    gauss_eliminated_matrix = gauss_eliminate(augmented)

    # If the matrix has an all zero row after elimination then it is singular
    for row in gauss_eliminated_matrix:
        all_zero_row = True
        left_side = row[:len(A)]
        for value in left_side:
            if value != 0:
                all_zero_row = False
                break
        if all_zero_row:
            return "Singular"

    diagonal_matrix = diag(gauss_eliminated_matrix)
    size = len(diagonal_matrix)
    inverse = []

    for i in range(size):
        full_row = diagonal_matrix[i]
        inverse.append(full_row[size:])

    return inverse


def get_h_n(n):
    """
    :param n: int
    :return: 2d list
    """
    # start will an n x n  zero matrix to make insertion easier
    h_n = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(1 / (i + j - 1))
        h_n.append(row)

    return h_n


def get_m_n(n, a_n):
    """
    :param n: int
    :param a_n: list
    :return: 2D list
    """
    m_n = []
    for i in range(1, n + 1):
        row_i = []
        for j in range(1, n + 1):
            value = a_n[i - 1]

            if value == 0 and j == 0:
                row_i.append(1)
            else:
                x = value ** (j - 1)
                row_i.append(x)
        m_n.append(row_i)

    return m_n


# h_5 = get_h_n(5)
# h_5_inverse = inv(h_5)
#
# print("h_5")
# print_matrix(h_5, False)
# print("**********************")
# print("h_5_inverse")
# print_matrix(h_5_inverse, False)
#
#
# h_inverse_h = multiply_matrices(h_5_inverse, h_5)
# print_matrix(h_inverse_h, False)


# print_matrix(h_5, False)

#print()

# h_5_inverse = inv(h_5)
# if h_5_inverse != "Singular":
#     print_matrix(h_5_inverse, False)
# else:
#     print(h_5_inverse)



M_5 = get_m_n(5, [0, 0.1, 0.2, 0.3, 0.4])
M_5_inverse = inv(M_5)

print("\n\n*************************************")
M_5_M_5_inverse = multiply_matrices(M_5, M_5_inverse)
print_matrix(M_5_M_5_inverse, False)

print("\n\n*************************************")
M_5 = get_m_n(5, [0, 0.1, 0.2, 0.3, 0.4])
M_5_inverse = inv(M_5)
M_5_inverse_M_5 = multiply_matrices(M_5_inverse, M_5)
print_matrix(M_5_inverse_M_5, False)




# inverse = inv(no_inverse_two)
# if inverse != "Singular":
#     print_matrix(inverse, False)
# else:
#     print(inverse)

# result = multiply_matrices(testing_matrix, inverse)
# print_matrix(result, False)


# first = get_identity_matrix(3)
# second = get_identity_matrix(5)
#
# print(multiply_matrices(first, second))
