import warnings


def f(a, b, c):
    warnings.warn('Using this function should be warned!')
    return a*b-c
