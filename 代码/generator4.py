#一个会使用yield表达式的求值结果的生成器函数。
def gen3(start, upper_limit):
    n = start
    while n < upper_limit:
        print(n)
        n *= (yield n)
