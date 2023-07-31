import math


def f(x, y):
    try:
        return math.sqrt(x)/y
    except TypeError:
        print('Please enter two numbers!')
        return math.nan
    except ValueError:
        print('x must be non-negative!')
        return math.nan
    except ZeroDivisionError:
        print('y cannot be 0!')
        return math.nan
