#定义一个变量。
a = 1

#定义一个私有变量。
_b = 100


#定义一个函数。
def f1():
    return 'f1'


#定义一个私有函数。
def _f2():
    return 'f2'


#定义一个类。
class C1():
    def echo(self):
        return 'C1'


#定义一个私有类。  注意这里其实违背了PEP 8的相应推荐。
class _C2():
    def echo(self):
        return 'C2'


