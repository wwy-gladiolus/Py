import time


def factorial1(n):
    """This function calculates n! using loop."""

    product = 1
    while n > 1:
        time.sleep(0.01)
        product = product * n
        n = n-1
    return product


def factorial2(n):
    """This function calculates n! using recursion."""

    time.sleep(0.01)
    if n > 1:
        return n * factorial2(n-1)
    else:
        return 1

