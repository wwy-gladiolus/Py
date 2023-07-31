#这是一个通过循环实现阶乘的函数。
def factorial(n):
    product = 1

    while n > 1:
        product = product*n
        n = n-1

    return product
