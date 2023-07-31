#标识符a是全局变量。
a = -99


#标识符outer也是全局变量。
def outer():
    #标识符b是本地变量，其作用域在outer()的函数体内。
    b = 35

    #标识符inner也是本地变量，其作用域也在outer()的函数体内。
    def inner():
        #标识符c是本地变量，其作用域在inner()的函数体内。
        c = 2
        #这里使用了标识符abs、a、b和c。
        return abs(a + b*c)

    #这里使用了标识符inner。
    return inner()

