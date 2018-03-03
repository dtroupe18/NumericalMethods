def function_exact(x):
    return float(1 / (1 + (25 * x**2)))


def get_interpolated_points(n):
    points = []
    for i in range(-n, n + 1):
        xi = float(i / n)
        yi = function_exact(xi)
        points.append((xi, yi))
    return points


def newton_interpolation(n, x):
    # Example 1 page 127 from Numerical Analysis by Richard Burden
    #
    # points = [(1.0, 0.7651977), (1.3, 0.6200860), (1.6, 0.4554022),
    #           (1.9, 0.2818186), (2.2, 0.1103623)]
    #
    # p4(1.5) ~= 0.5118200

    points = get_interpolated_points(n)
    n = len(points)
    last_col = []
    current_col = []
    total = points[0][1]

    for i in range(1, n):

        if not last_col:
            for j in range(n - 1):
                # Create the first column of the triangular matrix
                #
                current_value = ((points[j + 1][1] - points[j][1]) / (points[j + 1][0] - points[j][0]))
                last_col.append(current_value)

                # Are we on the main diagonal?
                #
                if j == 0:
                    product_sum = 1
                    for k in range(i):
                        product_sum *= (x - points[k][0])

                    product_sum *= current_value
                    total += product_sum
                    # print("adding ", product_sum)
            # print("last col: ", last_col)

        else:
            for j in range(len(last_col) - 1):
                # Use the last column to create the next one
                #
                divided_diff = (last_col[j + 1] - last_col[j]) / (points[j + i][0] - points[j][0])
                current_col.append(divided_diff)

                # Are we on the main diagonal?
                #
                if j == 0:
                    product_sum = 1
                    for k in range(i):
                        product_sum *= (x - points[k][0])

                    product_sum *= divided_diff
                    total += product_sum
                    # print("adding ", product_sum)

            if current_col:
                last_col = current_col
                current_col = []

            # print("last col: ", last_col)

    # print("Total: ", total)
    return total


# estimate = newton_interpolation(5, 1/5)
# actual = function_exact((1/5))

# print("actual: ", actual)
# print("estimate: ", estimate)





