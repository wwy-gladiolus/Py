#该函数根据参数n生成序列[1!, 2!, ..., n!]。
def factorial_sequence(n):
    """This function is the factorial sequence generator."""

    l = []
    i = 1
    factorial = 1

    while i <= n:
        factorial = factorial * i
        i = i + 1
        l.append(factorial)

    return l

