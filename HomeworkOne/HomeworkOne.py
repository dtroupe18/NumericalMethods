# Created 1/20/18 by Dave
import sys
import math


# 1.1 - Compute 3^-n for n = 1 through 50
def raise_to_negative_exponent(iterations):
    values = []
    for n in range(1, iterations + 1):
        value = float(3 ** (-1 * n))
        values.append(value)
    return values


def print_list(x):
    sys.stdout.write("[")
    for value in x:
        sys.stdout.write("%.25f" % value)
        sys.stdout.write(", ")
    sys.stdout.write("]")


# x = raise_to_negative_exponent(50)
# print_list(x)


def recurrence_equation(iterations):
    x0 = 1
    x1 = float(1/3)
    values = [x0, x1]

    for n in range(2, iterations + 1):
        value = float(((13/3) * values[-1]) - ((-4/3) * values[-2]))
        values.append(value)
        # print(final_value)
    return values


# print(recurrence_equation(50))


def revised_recurrence(iterations):
    x0 = 1
    x1 = float(1/3 - (10 ** -4))
    values = [x0, x1]

    for n in range(2, iterations + 1):
        value = float(((13 / 3) * values[-1]) - ((-4 / 3) * values[-2]))
        values.append(value)
        # print(value)
    return values


# print(revised_recurrence(50))


def cos_taylor_series(x):
    # summation (-1)^k * x^2k / (2k!)
    k = 0
    n = 25
    summation = float(0.0)
    sign = 1.0

    while k < n:
        current_term = (sign * x ** k) / (math.factorial(k))
        summation += current_term
        k += 2
        sign = -sign

    return summation


def calculate_two_point_one(x):
    return float((cos_taylor_series(x) - 1) / x * x)


def calculate_two_point_one_without_taylor(x):
    return float((math.cos(x) - 1) / x * x)


def sin_taylor_series(x):
    # summation (-1)^k * x ^(2k + 1) / (2k + 1)!
    summation = 0.0
    for k in range(0, 25):
        current_term = ((-1) ** k) * (x ** (2 * k + 1)) / (math.factorial(2 * k + 1))
        summation += current_term
    return summation

# print(sin_taylor_series(-math.pi / 2))
print(sin_taylor_series(math.pi / 4))
print(sin_taylor_series(-math.pi / 4))


# print(calculate_two_point_one(0.000001))
# print(calculate_two_point_one_without_taylor(0.000001))
# print("\n")
# print(calculate_two_point_one(0.0000000001))
# print(calculate_two_point_one_without_taylor(0.0000000001))
# print("\n")
# print(calculate_two_point_one(0.0000000000000001))
# print(calculate_two_point_one_without_taylor(0.0000000000000001))
# print("\n")
#
# print(cos_taylor_series(0.000001))
# print(math.cos(0.000001))
# print("\n")
# print(cos_taylor_series(0.0000000001))
# print(math.cos(0.0000000001))
# print("\n")
# print(cos_taylor_series(0.0000000000000001))
# print(math.cos(0.0000000000000001))
# print("\n")