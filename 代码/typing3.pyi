import typing


#定义一个静态鸭子类型Container。
class Container(typing.Protocol):
    def __len__(self) -> int: ...

    def __contains__(self, ele) -> bool: ...


#Example1实现了Container代表的协议。
class Example1():
    def __len__(self):
        return 0

    def __contains__(self, ele):
        return False


#Example2的__contains__不符合Container的要求，因此没有实现Container代表的协议。
class Example2():
    def __len__(self):
        return 0

    def __contains__(self):
        return False


#声明变量a应该实现Container代表的协议。
a: Container

#该赋值语句不会报错，因为tuple实现了Container代表的协议。
a = (1, 2, 3)
#该赋值语句不会报错，因为str实现了Container代表的协议。
a = "abc"
#该赋值语句会报错，因为int没有实现Container代表的协议。
a = 0
#该赋值语句不会报错，因为Example1实现了Container代表的协议。
a = Example1()
#该赋值语句会报错，因为Example2没有实现Container代表的协议。
a = Example2()

