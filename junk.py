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
            # print("j: ", j)
            if i != j:
                identity_row.append(0)
            else:
                identity_row.append(1)

        # print("identity row: ", identity_row)
        A[i].extend(identity_row)
        # print("id_border progress: ", A)

    # print("id_border: ")
    # print_matrix(A)
    return A


def combine_rows(row_a, row_b, col_index):
    pivot = row_a[col_index]
    lower_value = row_b[col_index]
    factor = lower_value / pivot * -1

    # if pivot > 0 and lower_value > 0:
    #     factor = lower_value / pivot * -1
    #
    # else:  # pivot < 0 and lower_value < 0:
    #     factor = lower_value / pivot


    # print()
    # print("row_a", row_a)
    # print("row_b", row_b)
    # print("pivot", pivot)
    # print("lower_value", lower_value)
    # print("factor for column", col_index, "is", factor)
    # print()

    new_row_b = []
    for i in range(len(row_a)):
        value = row_a[i]
        value *= factor
        value += row_b[i]
        new_row_b.append(value)

        # print("combined row", new_row_b)

    return new_row_b


def gauss_elim(B):
    """
    Applies Guassian elimination to a matrix
    :param B: matrix, 2D list
    :return:
    """
    matrix = B
    print_matrix(matrix)
    num_rows = len(matrix)
    print("number of rows", num_rows)
    num_cols = 1 + len(matrix[0]) // 2

    # assume no all zero rows for now
    #
    i = 0
    while i < num_rows:
        for j in range(num_cols):
            print("(", i, j, ")")
            if matrix[i][j] != 0:
                # Eliminate other values in that column
                #
                row = matrix[i]
                # print("row", row)

                for k in range(i + 1, num_rows):
                    next_row = matrix[k]
                    # print("next_row", next_row)
                    # print()

                    matrix[k] = combine_rows(row, next_row, j)
                    # print("new next row ", matrix[k])
                    # print()

                # Check if we are on the last row
                #
                # if i + 1 == num_rows:
                #     pivot = row[j]
                #     for value in row:
                #         value /= pivot
                #     matrix[i] = row

                print_matrix(matrix)
                print()
                i += 1
            elif j == num_cols - 1:
                i += 1



    # for i in range(num_rows):
    #     for j in range(num_cols):
    #         # print("i, j", i, j)
    #         # print(matrix[i][j])
    #
    #         if matrix[i][j] != 0:


def gauss_eliminate(B):
    """
    Applies Guassian elimination to a matrix
    :param B: matrix, 2D list
    :return:
    """
    matrix = B
    print_matrix(matrix)
    num_rows = len(matrix)
    num_cols = 1 + len(matrix[0]) // 2

    # assume no all zero rows for now
    #
    i = 0
    j = 0
    reset_j = False

    while i < num_rows:
        # j = 0
        while j < num_cols:
            print("(", i, ",", j, ")")
            # print("value: ", matrix[i][j])

            if matrix[i][j] != 0:
                # Eliminate other values in that column
                #
                row = matrix[i]

                # This loop only works if we aren't on the last row!
                for k in range(i + 1, num_rows):
                    next_row = matrix[k]
                    matrix[k] = combine_rows(row, next_row, j)

                # Check if we are on the last row, if we are eliminate the
                if i + 1 == num_rows:
                    print("ON THE LAST FUCKING ROW")
                    if j == num_cols - 2:
                        print("WE ARE FUCKING DONE!")
                        return matrix

                    # pivot = row[j]
                    # for value in row:
                    #     value /= pivot
                    # matrix[i] = row

                # Done with this row increment i and reset j
                # print()
                # print("i: ", i)
                if i < num_rows - 1:
                    i += 1
                reset_j = True
                print_matrix(matrix)

            if reset_j:
                j = 0
                reset_j = False
                # print()
                # print("2 i: ", i)
            else:
                j += 1

        if i < num_rows - 1:
            i += 1
            # print()
            # print("3 i: ", i)


def inv(A):
    """
    :param A: n x n square matrix (i.e a 2D list of lists)
    :return: inverse or "singular"
    """
    augmented = id_border(A)
    gauss_eliminate(augmented)


inv(testing_matrix_two)


def while_loop_hell(matrix):

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    i = 0

    while i < num_rows:
        j = 0
        while j < num_cols:
            print("(", i, ",", j, ")")
            print("value: ", matrix[i][j])
            j += 1
        i += 1

# while_loop_hell(testing_matrix_two)

# SOME HOW THE SIZE OF THE ROW IS INCREASING


# for i in range(num_rows):
#     # print_matrix(matrix)
#
#     for j in range(num_cols):
#         print("i, j", i, j)
#         value = matrix[i][j]
#         print("value", value)
#         if matrix[i][j] != 0:
#             # Eliminate the other values in that column
#             row = matrix[i]
#             # print("working on row: ", row)
#
#             for k in range(i + 1, num_rows):
#                 next_row = matrix[k]
#                 # print("next row: ", next_row)
#                 matrix[k] = combine_rows(row, next_row, j)
#
#             # print_matrix(matrix)
#             break