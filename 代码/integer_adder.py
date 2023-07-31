#该函数只具有仅位置形式参数。
def add1(x, y, /):
    return x+y


#该函数只具有仅关键字形式参数。
def add2(*, x, y):
    return x+y


#该函数只具有位置或关键字形式参数。
def add3(x, y):
    return x+y

