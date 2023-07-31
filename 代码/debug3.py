import functools, sys


#自定义审计钩子。
def myaudithook(event, parameters):
    if event == 'fibo':
        print('fibo(' + str(parameters[0]) +')')


#注册审计钩子。
sys.addaudithook(myaudithook)


def fibonacci(n):
    #触发自定义审计事件。
    sys.audit('fibo', n)
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@functools.cache
def fibonacci_cache(n):
    #触发自定义审计事件。
    sys.audit('fibo', n)
    if n < 2:
        return 1
    else:
        return fibonacci_cache(n-1) + fibonacci_cache(n-2)

