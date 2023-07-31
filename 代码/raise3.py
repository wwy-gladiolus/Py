import math


def f(x, y):
    try:
        return math.sqrt(x)/y
    except TypeError as e:
        raise RuntimeError("Please enter two numbers!") from e
    except ValueError as e:
        raise RuntimeError("x must be non-negative!") from SyntaxError
    except ZeroDivisionError as e:
        raise RuntimeError("y cannot be 0!") from None


def exception_chain(x, y):
    try:
        f(x, y)
    except Exception as e:
        print(repr(e.__context__))
        print(repr(e.__cause__))
        print(e.__suppress_context__)
