import math


class MyContextManager():
    def __enter__(self):
        def f(x, y):
            return math.sqrt(x)/y
        return f

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == TypeError:
            print('Please enter two numbers!')
            return True
        elif exc_type == ValueError:
            print('x must be non-negative!')
            return True
        else:
            return False

