#一个具有参数且使用yield语句的第二种语法的生成器函数。
def gen2(n):
    """This generator generates sequence 0, 1, ..., n-1."""
    yield from range(n)
