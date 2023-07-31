#定义类B。
class B:
    #类属性b。
    b = 0


#定义类A。
class A:
    #类属性a。
    a = 1

    #在初始化时设置__class__特殊属性。
    def __init__(self):
        self.__class__ = B
