def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def factorial_while(num):
    product = 1

    while num >= 1:

        product = product * num

        num = num - 1

    return product


# Inspired by
# https://codippa.com/how-to-calculate-factorial-of-a-number-in-python-recursively/
