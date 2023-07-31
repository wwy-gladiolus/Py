import math


def f(x, y):
    try:
        return math.sqrt(x)/y
    except (TypeError, ValueError, ZeroDivisionError):
        return math.nan
