import time
import functools


#定义一个无缓存功能的斐波拉契序列生成函数。
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#定义一个有缓存功能的斐波拉契序列生成函数。
@functools.cache
def fibonacci_cache(n):
    if n < 2:
        return 1
    else:
        return fibonacci_cache(n-1) + fibonacci_cache(n-2)


#定义一个统计函数执行时间的函数。
def process_time(func, *args, **kwargs):
    starttime = time.time()
    func(*args, **kwargs)
    endtime = time.time()
    return endtime - starttime

