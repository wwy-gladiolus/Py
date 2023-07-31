import warnings


#调用该函数会将一段用户自定义警告信息写入标准输出。
def f(a, b, c):
    msg = warnings.formatwarning(
            'Using this function should be warned!',
            UserWarning,
            f.__code__.co_filename,
            f.__code__.co_firstlineno + 1,
    )
    print(msg)
    return a*b-c
