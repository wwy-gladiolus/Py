import warnings


#调用该函数会发布一个用户自定义警告。
def f(a, b, c):
    warnings.warn_explicit(
            'Using this function should be warned!',
            UserWarning,
            f.__code__.co_filename,
            f.__code__.co_firstlineno + 1,
    )
    return a*b-c
