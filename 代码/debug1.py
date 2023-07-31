import functools


def fibonacci(n):
    if __debug__:
        #这里是调试用的代码，以跟踪递归过程。
        print('fibo(' + str(n) + ')')
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@functools.cache
def fibonacci_cache(n):
    if __debug__:
        #这里是调试用的代码，以跟踪递归过程。
        print('fibo(' + str(n) + ')')
    if n < 2:
        return 1
    else:
        return fibonacci_cache(n-1) + fibonacci_cache(n-2)

