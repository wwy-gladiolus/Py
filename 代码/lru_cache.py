import functools
import time


#定义一个能缓存128个映射的斐波拉契序列生成函数。
@functools.lru_cache
def fibonacci_lru(n):
    if n < 2:
        return 1
    else:
        return fibonacci_lru(n-1) + fibonacci_lru(n-2)


#定义一个能缓存10个映射的斐波拉契序列生成函数。
@functools.lru_cache(10)
def fibonacci_10(n):
    if n < 2:
        return 1
    else:
        return fibonacci_10(n-1) + fibonacci_10(n-2)


#定义一个统计函数执行时间的函数。
def process_time(func, *args, **kwargs):
    starttime = time.time()
    func(*args, **kwargs)
    endtime = time.time()
    return endtime - starttime

