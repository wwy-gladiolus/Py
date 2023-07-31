import warnings


#调用该函数会将一个用户自定义警告写入warning.log文件。
def f(a, b, c):
    with open('warning.log', 'a') as fd:
        warnings.showwarning(
                'Using this function should be warned!',
                UserWarning,
                f.__code__.co_filename,
                f.__code__.co_firstlineno + 2,
                fd
        )
    return a*b-c
