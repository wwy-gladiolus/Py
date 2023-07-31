import math
import sys


def f(x, y):
    try:
        result = math.nan
        result = math.sqrt(x)/y
    except TypeError:
        print('Please enter two numbers!')
    except ValueError:
        print('x must be non-negative!')
    finally:
        print(sys.exc_info())
        return result
