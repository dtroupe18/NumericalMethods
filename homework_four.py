# Lagrange interpolation


def function_exact(x):
    return float(1 / (1 + (25 * x**2)))


def get_interpolated_points(n):
    points = []
    for i in range(-n, n + 1):
        xi = float(i / n)
        yi = function_exact(xi)
        points.append((xi, yi))
    return points


def calc_lagrange_value(n, x):
    points = get_interpolated_points(n)
    y = float(0.0)

    for j in range(len(points)):
        xj, yj = points[j]

        multiplication_sum = None

        for i in range(len(points)):
            if j != i:
                xi, yi = points[i]

                if multiplication_sum is None:
                    multiplication_sum = (x - xi) / (xj - xi)
                else:
                    multiplication_sum *= (x - xi) / (xj - xi)

        y += yj * multiplication_sum

    return y


estimate = calc_lagrange_value(5, -1/5)
actual = function_exact(-1/5)

first = abs(function_exact((1 - 1/14)) - calc_lagrange_value(7, (1 - 1/14)))
second = abs(function_exact((1 - 1/14)) - calc_lagrange_value(7, (1 - 3/14)))
third = abs(function_exact((1 - 1/14)) - calc_lagrange_value(10, (1 - 1/20)))
fourth = abs(function_exact((1 - 1/14)) - calc_lagrange_value(10, (1 - 3/20)))
fifth = abs(function_exact((1 - 1/14)) - calc_lagrange_value(20, (1 - 1/40)))
sixth = abs(function_exact((1 - 1/14)) - calc_lagrange_value(20, (1 - 3/40)))

print("first: ", first)
print("second: ", second)
print("thirds: ", third)
print("fourth: ", fourth)
print("fifth: ", fifth)
print("sexith: ", sixth)



