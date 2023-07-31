import math


def f(x, y):
    try:
        return math.exp(x)/y
    except ZeroDivisionError:
        print("Divisor cannot be 0.")
        return math.nan
    except ArithmeticError:
        print("Unknown arithmetic error.")
        return math.nan
