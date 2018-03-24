import math


def calc_f_x(x):
    """
    calculate f(x) = e^(-x^2)
    :param x: double value of x
    :return: function value at x
    """
    return math.e ** (-x**2)


def calc_f_double_prime(x):
    """
    f''(x) = (4x^2 - 2) e^(-x^2)
    :param x: double value of x
    :return: function value at x
    """
    return ((4 * x**2) - 2) * math.e ** (-x**2)


def composite_trapezoidal_method(a, b, n):
    """
    :param a: int - starting value for the interval
    :param b: int - ending value for the interval
    :param n: number of sub-intervals between a and b
    :return: approximate value of the integral
    """
    h = (b - a) / n
    f_a = calc_f_x(a)
    f_b = calc_f_x(b)

    summation = 0

    for j in range(n + 1):
        x_j = a + h * j
        summation += calc_f_x(x_j)

    return (h / 2) * (f_a + summation + f_b) - (((b - a) / 2) * h**2 * calc_f_double_prime(b))


print(composite_trapezoidal_method(0, 1, 10))
print(composite_trapezoidal_method(0, 1, 50))
print(composite_trapezoidal_method(0, 1, 100))
# print(composite_trapezoidal_method(0, 1, 200))
# print(composite_trapezoidal_method(0, 1, 400))


