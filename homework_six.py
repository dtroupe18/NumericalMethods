import math


def calc_f_x(x):
    """
    calculate f(x) = e^(-x^2)
    :param x: double value of x
    :return: function value at x
    """
    return math.e ** (-x ** 2)


def calc_f_double_prime(x):
    """
    f''(x) = (4x^2 - 2) e^(-x^2)
    :param x: double value of x
    :return: function value at x
    """
    return ((4 * x ** 2) - 2) * math.e ** (-x ** 2)


def calc_f_quad_prime(x):
    """
    f''''(x) = (16x^4 - 48x^2 + 12) * e^(-x^2)
    :param x: double value of x
    :return: function value at x
    """
    return ((16 * x ** 4) - (48 * x ** 2) + 12) * math.e ** (-x ** 2)


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

    for j in range(n):
        x_j = a + h * j
        summation += calc_f_x(x_j)

    return (h / 2) * (f_a + 2 * summation + f_b) - (((b - a) / 2) * h ** 2 * calc_f_double_prime(b))


def composite_simpson_method(a, b, n):
    """
    :param a: int - starting value for the interval
    :param b: int - ending value for the interval
    :param n: number of sub-intervals between a and b
    :return: approximate value of the integral
    """
    if n % 2 != 0:
        return "Error: n must be even to use this function!"

    half_of_n = n // 2
    h = (b - a) / n
    f_a = calc_f_x(a)
    f_b = calc_f_x(b)

    first_summation = 0
    for j in range(1, half_of_n):
        x_2j = a + h * j * 2
        first_summation += calc_f_x(x_2j)

    second_summation = 0
    for j in range(1, half_of_n + 1):
        x_2j_1 = (a + h * j * 2) - 1
        second_summation += calc_f_x(x_2j_1)

    return (h / 3) * (f_a + 2 * first_summation + 4 * second_summation + f_b) - \
           (((b - a) / 180) * h ** 4 * calc_f_quad_prime(b))


# print(calc_f_double_prime(1))

# print(composite_trapezoidal_method(0, 1, 10))
# print(composite_trapezoidal_method(0, 1, 50))
# print(composite_trapezoidal_method(0, 1, 100))
# print(composite_trapezoidal_method(0, 1, 200))
# print(composite_trapezoidal_method(0, 1, 400))

# print("n = 10: ", composite_simpson_method(0, 1, 10))
# print("n = 50: ", composite_simpson_method(0, 1, 50))
# print("n = 100: ", composite_simpson_method(0, 1, 100))
# print("n = 200: ", composite_simpson_method(0, 1, 200))
# print("n = 400: ", composite_simpson_method(0, 1, 400))

