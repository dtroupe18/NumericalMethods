import sys

"""
Let x = 2^12 + 2^-12

How is x represented in the IEEE floating point standard in double precision (i.e., with a total of 8 bytes)?
Give the exponent field and the mantissa field.

2^12 = 4096
2^-12 = 0.00024414062

x = 4096.00024414062

"""
n = 4096.00024414062
# sys.stdout.write("%.53f" % n)


# 2.1 Show floating point precision is not associative
def find_associative_error():
    x = 0.1
    y = 0.2
    z = 0.4

    done = False

    while not done:
        lhs = float(float(x + y) + z)
        rhs = float(x + float(y + z))

        if lhs != rhs:
            print("not equal for x = ", x, " y = ", y, " z = ", z)
            break

        else:
            x += 0.25
            y += 0.50
            z += 0.75


# find_associative_error()


def test_associative_property(x, y, z):
    lhs = float(float(x + y) + z)
    rhs = float(x + float(y + z))

    sys.stdout.write("%.53f\n" % lhs)
    sys.stdout.write("%.53f\n" % rhs)

    return lhs == rhs


# print(test_associative_property(0.5, 0.7, 0.1))

# 2.2 Give an example of a representable rational number x > 0 such that fl(x ∗ fl(1/x)) ̸= fl(1).
def test_rational_representation():
    x = 12.50
    done = False

    while not done:
        lhs = float(x * float(1 / x))
        rhs = float(1)

        if lhs != rhs:
            print("not equal for x = ", x)
            break

        else:
            x += 0.25

    # sys.stdout.write("%.53f\n" % lhs)
    # sys.stdout.write("%.53f\n" % rhs)


# test_rational_representation()


def rational_multiplication_error(x):
    lhs = float(x * float(1 / x))
    rhs = float(1)

    sys.stdout.write("%.53f\n" % lhs)
    sys.stdout.write("%.53f\n" % rhs)

    return lhs == rhs


# print(rational_multiplication_error(12.25))


# 2.3 Give an example of representable rational numbers x, y, z
# such that fl(fl(x∗y)∗z) ̸= fl(x∗fl(y∗z)).
def find_commutative_error():
    x = 0.25
    y = 0.7
    z = 0.9

    number_of_solutions = 0

    while number_of_solutions < 10:
        lhs = float(float(x * y) * z)
        rhs = float(x * float(y * z))

        if lhs != rhs:
            print("not equal for x = ", x, " y = ", y, " z = ", z)
            number_of_solutions += 1
            x += 0.25
            y += 0.50
            z += 0.75

        else:
            x += 0.25
            y += 0.50
            z += 0.75


find_commutative_error()
