#这是一个通过递归实现阶乘的函数。
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
