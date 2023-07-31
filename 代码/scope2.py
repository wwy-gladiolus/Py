a = -99


def outer():
    b = 35

    def inner():
        c = 2
        #该绑定屏蔽了外层本地变量b。
        b = 10
        #该绑定屏蔽了全局变量a。
        a = -20
        return abs(a + b*c)

    return inner()

