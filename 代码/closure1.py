#定义外层函数f1。
def f1(a, b):
    x = a
    y = b
    #定义内层函数f2。
    def f2(z):
        return (x, y, z)
    #该return语句使f2成为了f1的闭包。
    return f2

