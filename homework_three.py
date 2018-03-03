import sys
import math
import homework_one


def calculate_pi(x):
    """
    Calculate Pi with high precision using the following formula
    summation of a_n * (16^-n) where:
    a_n = (4 / ((8 * n) + 1)) - (2 / ((8 * n) + 4)) - (1 / ((8 * n) + 5)) - (1 / ((8 * n) + 6))
    :param x: number of iterations for the summation
    :return: float -> calculated value for Pi
    """

    n = 0
    summation = float(0.0)

    while n <= x:
        a_n = (4 / ((8 * n) + 1)) - (2 / ((8 * n) + 4)) - (1 / ((8 * n) + 5)) - (1 / ((8 * n) + 6))
        a_n *= (1 / 16 ** n)
        summation += a_n
        n += 1

    return summation


# pi = calculate_pi(8)
# print("Pi: ", pi)


def find_smallest_n():
    """
    Find smallest value of n such that:
    (1 / 15) * An + 1 * (1/16)^n <= (1/2) * 10^-12

    :return: int n and x the approximate value for pi at that n
    """
    n = 0
    limit = float((1/2) * (10 ** -12))
    values = []

    while True:
        a_n = (4 / ((8 * n) + 1)) - (2 / ((8 * n) + 4)) - (1 / ((8 * n) + 5)) - (1 / ((8 * n) + 6))
        a_n *= (1 / 16) ** n
        a_n *= (1 / 15)
        values.append(a_n)

        if a_n <= limit:
            return n, values

        n += 1

    # End While


# n_value, a_n_values = find_smallest_n()
# print("\nSmallest n: ", n_value)
# print("last: ", a_n_values[-1])
# sys.stdout.write("%.25f\n" % a_n_values[-1])
# sys.stdout.write("%.25f\n" % float((1/2) * (10 ** -12)))
# print(a_n_values[-1] <= float((1/2) * (10 ** -12)))


def apply_newton_raphson():
    """
    p_n+1 = p_n - ((f(p_n) / (f'(p_n))
    where f = sin(x)
    :return: int n, float difference, float final value
    """
    n = 0
    limit = 0.5 * (10 ** -9)
    p_n_values = []

    x_0 = float(3.0)
    p_n_values.append(x_0)

    while True:
        f = math.sin(p_n_values[-1])
        f_prime = math.cos(p_n_values[-1])

        p_n = float(p_n_values[-1] - (f / f_prime))
        p_n_values.append(p_n)
        n += 1

        if n > 1:
            diff_one = abs(p_n_values[n - 2] - p_n_values[n - 1])
            diff_two = abs(p_n_values[n - 1] - p_n_values[n])
            max_diff = max(diff_one, diff_two)
            if max_diff <= limit:
                return n, max_diff, p_n_values[-1]

        else:
            diff_two = abs(p_n_values[n - 1] - p_n_values[n])
            if diff_two <= limit:
                return n, diff_two, p_n_values[-1]
    # End While


# n_value, max_difference, value = apply_newton_raphson()
# print("n: ", n_value)
# print("maxDifference: ", max_difference)
# print("Value: ", value)
# sys.stdout.write("%.25f" % max_difference)

def find_approximate_root():
    """
    f(x) = e^x - (x - ln2)^2 - 2x -2 +2ln2
    :return: float calculated root
    """
    n = 0
    values = []
    x = float(1.0)

    while True:
        f_x = math.exp(x) - ((x - math.log(2))**2) - (2 * x) - 2 + (2 * math.log(2))
        values.append(f_x)
        x -= 0.0000001
        if f_x == 0.0:
            return x


#  print(find_approximate_root())


def apply_newton_raphson_again():
    """
    f(x) = e^x - (x - ln2)^2 - 2x -2 +2ln2
    f'(x) = e^x - 2(x -ln2) - 2
    :return: float calculated root
    """

    n = 0
    limit = float(10 ** -10)
    p_n_values = []

    x_0 = float(1.0)
    p_n_values.append(x_0)

    while True:
        f = math.exp(p_n_values[-1]) - ((p_n_values[-1] - math.log(2))**2) - (2 * p_n_values[-1]) - 2 + (2 * math.log(2))
        f_prime = math.exp(p_n_values[-1]) - (2 * (p_n_values[-1] - math.log(2))) - 2

        p_n = float(p_n_values[-1] - (f / f_prime))
        p_n_values.append(p_n)
        n += 1

        value_of_f = math.exp(p_n) - ((p_n - math.log(2))**2) - (2 * p_n) - 2 + (2 * math.log(2))

        if abs(value_of_f) < limit:
            return n, p_n_values

    # End While


# number, values = apply_newton_raphson_again()
# print("n: ", number)
# print("p*: ", values[-1])
#
# HomeworkOne.print_list(values)


def calc_value_at_derivatives(x):
    """
    f(x) = e^x - (x - ln2)^2 - 2x -2 +2ln2
    f'(x) = e^x - 2(x -ln2) - 2
    f''(x) = e^x - 2
    f'''(x) = e^x
    :param x: float -> value to plug in
    :return: float tuple contains all values
    """
    values = []
    values.append(math.exp(x) - ((x - math.log(2)) ** 2) - (2 * x) - 2 + (2 * math.log(2)))
    values.append(math.exp(x) - (2 * (x - math.log(2))) - 2)
    values.append(math.exp(x) - 2)
    values.append(math.exp(x))

    return values


# der_values = calc_value_at_derivatives(0.6936330309301341)
der_values = calc_value_at_derivatives(0.6931525202806265)
homework_one.print_list(der_values)


def apply_modified_newton_raphson(m):
    """
    f(x) = e^x - (x - ln2)^2 - 2x -2 +2ln2
    f'(x) = e^x - 2(x -ln2) - 2
    :param m: int -> multiplicity of f
    :return: float root of f
    """

    n = 0
    limit = float(10 ** -10)
    p_n_values = []

    x_0 = float(1.0)
    p_n_values.append(x_0)

    while True:
        f = math.exp(p_n_values[-1]) - ((p_n_values[-1] - math.log(2))**2) - (2 * p_n_values[-1]) - 2 + (2 * math.log(2))
        f_prime = math.exp(p_n_values[-1]) - (2 * (p_n_values[-1] - math.log(2))) - 2

        p_n = float(p_n_values[-1] - (m * (f / f_prime)))
        p_n_values.append(p_n)
        n += 1

        value_of_f = math.exp(p_n) - ((p_n - math.log(2))**2) - (2 * p_n) - 2 + (2 * math.log(2))

        if abs(value_of_f) < limit:
            return n, p_n_values

    # end while


# number, values = apply_modified_newton_raphson(3)
# print("n: ", number)
# print("p*: ", values[-1])
#
# HomeworkOne.print_list(values)